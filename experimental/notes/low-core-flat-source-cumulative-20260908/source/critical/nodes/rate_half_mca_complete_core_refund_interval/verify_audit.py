"""Independent integer-scaled replay of every parameter box, without the primary API."""

from functools import lru_cache
from math import comb, lcm, prod


R, D, GAP, C = 1048576, 67466, 67472, 67467
LO, HI, STEP, AS, TS, SIX, NEAR = 40000, 44999, 1000, 8, 8, 64, 134944
LIMIT = 264060029243645954
U = (0, 10755802499540570, 737012707696078, 50371450079970, 3424826154478, 231038329409)
PD = prod(GAP+i for i in range(1, 11))


def need(ok, message):
    if not ok:
        raise ValueError(message)


def size_pair(J, j, r, u):
    den = AS*r*(r+1)
    return j*(den+(J-11)*(AS*r+u)), den


def numerator(J):
    return prod(R+J-i for i in range(12))


@lru_cache(maxsize=32768)
def basis_floor(J, j, r, u, ln, ld):
    an, ad = size_pair(J, j, r, u)
    scale = ad*ld*j
    a, t, ell = an*ld*j, an*ln*j, 11-j
    need(a % j == 0 and 0 <= t <= a < C*scale, "scaled occupancy and density")
    x, e = (J+D)*scale-t, J*scale-a-ell*scale
    factors = [x]+[x-min(e+i*scale, i*(a//j)) for i in range(1, ell)]
    need(min(factors) > 0, "positive scaled quotient")
    inside = (prod((C+i)*scale-t for i in range(j))
              +11*prod(C+i for i in range(j-1))*t*scale**(j-1))
    return 12*prod(factors)*inside//scale**11


def low_rank_box(J0, J1, j, r, u, v):
    kd = 2*j*TS
    kl, kh = (2*j-1)*TS+v, (2*j-1)*TS+v+1
    light = (2*j-1)*TS-v
    lcost = min(basis_floor(J, j, r, w, ln, ld)
                for J in (J0, J1) for w in (u, u+1) for ln, ld in ((0, 1), (light, kd)))
    hcost = min(basis_floor(J, j, r, w, kn, kd)
                for J in (J0, J1) for w in (u, u+1) for kn in (kl, kh))
    high = (GAP+J0)*PD*10488//125
    bl, bh = min(lcost, high), min(hcost, high)
    an0, ad = size_pair(J0, j, r, u+1)
    an1, ad1 = size_pair(J1, j, r, u+1)
    need(ad == ad1, "fixed affine size denominator")
    cn, cd = ((R+J0)*ad-an0)*U[j]*kd, (GAP+J0)*ad*kd-kh*an0
    en, ed = (kd-kl)*an1, kd*ad
    need(cd > 0 and bl > 0 and bh > 0, "positive two-cost denominators")
    q = (cn*ed+en*cd+cd*ed-1)//(cd*ed)
    num = numerator(J1)+max(0, bl-bh)*q
    return num//bl+NEAR, num, bl


def rank_six_box(J0, J1, u, v):
    an0, ad = size_pair(J0, 6, 6, u)
    an1, ad1 = size_pair(J1, 6, 6, u+1)
    need(ad == ad1, "rank-six affine denominator")
    scale = lcm(ad*SIX, ad*6)
    t0 = an0*v*(scale//(ad*SIX))
    t1 = an1*(v+1)*(scale//(ad*SIX))
    h = an1*(scale//(ad*6))
    p = C*scale-t1
    need(p > 0, "scaled calibration stays below c")
    inside = p**6+11*(p**5+5*t1*p**4)*t0
    for b in range(2, 7):
        k = 6-b
        coef = comb(11, b)*(p**k+(k*t1*p**(k-1) if k else 0))-comb(11, b-1)*(k+1)*p**k
        count = prod(max(t0-i*h, 0) for i in range(b)) if coef >= 0 else t1**b
        inside += coef*count
    first = min((J+D)*scale-size_pair(J, 6, 6, w)[0]*ln*(scale//(ad*SIX))
                for J in (J0, J1) for w in (u, u+1) for ln in (v, v+1))
    retained = an0*(SIX-v-1)*(scale//(ad*SIX))
    outside = first*prod((D+5-i)*scale+retained for i in range(1, 5))
    need(inside > 0 and outside > 0, "positive signed inner and quotient box bounds")
    cost = min(12*outside*inside//scale**11, (GAP+J0)*PD*10488//125)
    need(cost > 0, "positive rank-six tuple charge")
    num = numerator(J1)
    return num//cost+NEAR, num, cost


def floor_control(num, den, answer):
    need(den > 0 and answer*den <= num < (answer+1)*den, "exact endpoint floor")


def main():
    low_num = numerator(LO)*7**6
    low_den = 12*(LO+D)*prod(7*(LO+D)-i*(LO-4) for i in range(1, 7))
    low_den *= prod(D+11-i for i in range(7, 11))
    floor_control(low_num, low_den, 240281411914853457-NEAR)
    need(4*(R+LO-11) > 12*(D+HI) and C > HI and R+HI > 2*(GAP+HI), "global analytic gates")
    need(numerator(HI)//((GAP+LO)*PD*10488//125)+NEAR < 240281411914853457, "global HIGH bound")
    maxima = [0, 0]
    counts = [0, 0]
    mutations = 0
    for block in range(5):
        j0, j1 = LO+block*STEP, LO+(block+1)*STEP-1
        for j in range(1, 7):
            for r in range(j, 7):
                for u in range(AS):
                    for v in range(SIX if j == 6 else TS):
                        cap, num, den = (rank_six_box(j0, j1, u, v) if j == 6 else
                                         low_rank_box(j0, j1, j, r, u, v))
                        kind = int(j == 6)
                        maxima[kind] = max(maxima[kind], cap)
                        counts[kind] += 1
                        need(cap <= LIMIT, "every box fits the printed total")
                        floor_control(num, den, cap-NEAR)
                        for wrong in (cap-NEAR-1, cap-NEAR+1):
                            try:
                                floor_control(num, den, wrong)
                            except ValueError:
                                mutations += 1
                            else:
                                raise ValueError("accepted incorrect box floor")
        print("AUDITED PREFIX", j1, "maxima", maxima, "boxes", counts, flush=True)
    need(counts == [6400, 2560] and mutations == 17920, "exhaustive inventory and floor controls")
    need(maxima == [LIMIT, 231762550270308532], "independent exact maxima")
    budget = 2130706433**6//2**128
    need(budget == 274980728111395087 and budget-LIMIT == 10920698867749133, "field budget and reserve")
    print("PASS: independent integer-scaled replay of all 8960 boxes and 17920 floor mutations")
    print("PASS: new total 264060029243645954; unchanged union total 274929007493481160")
    print("Finite controls do not certify the universal proof or original-source assembly")


if __name__ == "__main__":
    main()
