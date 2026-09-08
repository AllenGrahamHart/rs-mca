"""Exact exhaustive box certificates; analytic completeness is proved in proof.md."""

from fractions import Fraction as Q
from functools import lru_cache
from math import comb, prod


R, GAP, LO, HI, NEAR = 1048576, 67472, 40000, 44999, 134944
D, C, BUDGET = GAP-6, GAP-5, 274980728111395087
NEW_CAP, OLD_CAP = 264060029243645954, 274929007493481160
J_STEP, A_PARTS, T_PARTS, SIX_PARTS = 1000, 8, 8, 64
CHILD = (0, 10755802499540570, 737012707696078, 50371450079970,
         3424826154478, 231038329409)
PD = prod(GAP+i for i in range(1, 11))


def need(ok, message):
    if not ok:
        raise ValueError(message)


def size(J, j, r, u):
    return j*(1+(J-11)*Q(r*A_PARTS+u, A_PARTS*r*(r+1)))


def ceil(x):
    return -((-x.numerator)//x.denominator)


def resource(J):
    return prod(R+J-i for i in range(12))


@lru_cache(maxsize=32768)
def basis(J, j, a, lam):
    t, ell, h = lam*a, 11-j, a/j
    x, e = J+D-t, J-a-ell
    factors = [x]+[x-min(e+i, i*h) for i in range(1, ell)]
    inside = prod(C+i-t for i in range(j))+11*prod(C+i for i in range(j-1))*t
    need(all(x > 0 for x in factors) and 0 <= t <= a < C, "positive coupled basis")
    return 12*prod(factors)*inside


def low_rank_box(J0, J1, j, r, u, v):
    den = 2*j*T_PARTS
    k0, k1 = Q((2*j-1)*T_PARTS+v, den), Q((2*j-1)*T_PARTS+v+1, den)
    light_cap = 2-Q(1, j)-k0
    corners = [(J, size(J, j, r, w)) for J in (J0, J1) for w in (u, u+1)]
    low_light = min(basis(J, j, a, lam) for J, a in corners for lam in (Q(0), light_cap))
    low_heavy = min(basis(J, j, a, lam) for J, a in corners for lam in (k0, k1))
    high = (GAP+J0)*PD*10488//125
    bl, bh = min(int(low_light), high), min(int(low_heavy), high)
    a0, a1 = size(J0, j, r, u+1), size(J1, j, r, u+1)
    child = ceil((R+J0-a0)*CHILD[j]/(GAP+J0-k1*a0)+(1-k0)*a1)
    need(bl > 0 and bh > 0 and child > 0, "positive costs and child cap")
    cap = (resource(J1)+max(0, bl-bh)*child)//bl+NEAR
    return cap, bl, bh, child


def six_box(J0, J1, u, v):
    a0, a1 = size(J0, 6, 6, u), size(J1, 6, 6, u+1)
    l0, l1 = Q(v, SIX_PARTS), Q(v+1, SIX_PARTS)
    t0, t1, h1 = l0*a0, l1*a1, a1/6
    p = C-t1
    need(p > 0, "convex tangent domain")
    inner = p**6+11*(p**5+5*t1*p**4)*t0
    for b in range(2, 7):
        k = 6-b
        coefficient = (comb(11, b)*(p**k+(k*t1*p**(k-1) if k else 0))
                       -comb(11, b-1)*(k+1)*p**k)
        low = prod(max(t0-i*h1, 0) for i in range(b))
        upper = t1**b
        inner += coefficient*(low if coefficient >= 0 else upper)
    first = min(J+D-lam*size(J, 6, 6, w)
                for J in (J0, J1) for w in (u, u+1) for lam in (l0, l1))
    rest = prod(D+(1-l1)*a0+5-i for i in range(1, 5))
    need(first > 0 and rest > 0, "positive outside quotient factors")
    lower = int(12*first*rest*inner)
    high = (GAP+J0)*PD*10488//125
    if lower <= 0:
        return None
    return resource(J1)//min(lower, high)+NEAR


def main():
    need(HI < C and R+HI > 2*(GAP+HI), "all source and child convexity gates")
    h7 = Q(LO-4, 7)
    low = (LO+D)*prod(LO+D-i*h7 for i in range(1, 7))*prod(D+11-i for i in range(7, 11))
    low_cap = int(Q(resource(LO), 12)/low)+NEAR
    need(4*(R+LO-11) > 12*(D+HI), "whole-J low-density derivative")
    need(low_cap == 240281411914853457, "exact low-density floor")
    need(resource(HI)//((GAP+LO)*PD*10488//125)+NEAR < low_cap, "uniform HIGH source cap")
    need(84*125*(GAP+1-77) > 10488*(GAP+1) and GAP+1 > 12*84, "HIGH weight gate")
    print("LOW DENSITY", low_cap, flush=True)
    records, failures, six_records = [], [], []
    for J0 in range(LO, HI+1, J_STEP):
        J1 = min(J0+J_STEP-1, HI)
        for j in range(1, 6):
            for r in range(j, 7):
                for u in range(A_PARTS):
                    for v in range(T_PARTS):
                        cap, _, _, _ = low_rank_box(J0, J1, j, r, u, v)
                        tag = (J0, j, r, u, v)
                        records.append((cap, tag))
                        if cap > NEW_CAP:
                            failures.append((cap, tag))
        for u in range(A_PARTS):
            for v in range(SIX_PARTS):
                cap = six_box(J0, J1, u, v)
                if cap is None:
                    raise ValueError("nonpositive rank-six lower count")
                tag = (J0, 6, 6, u, v)
                six_records.append((cap, tag))
                if cap > NEW_CAP:
                    failures.append((cap, tag))
        print("PREFIX through", J1, "low-rank max", max(records),
              "rank-six max", max(six_records), "failures", len(failures), flush=True)
    print("TOTAL boxes", len(records), len(six_records), "maxima", max(records), max(six_records))
    print("FAILURES", sorted(failures, reverse=True)[:8])
    need(not failures and low_cap <= NEW_CAP, "all box upper bounds fit the printed total")
    need(len(records) == 6400 and len(six_records) == 2560, "complete fixed box inventory")
    need(max(records) == (NEW_CAP, (40000, 1, 3, 0, 7)), "exact low-rank maximum")
    need(max(six_records) == (231762550270308532, (40000, 6, 6, 0, 0)), "exact rank-six maximum")
    need(NEW_CAP < OLD_CAP < BUDGET, "whole-source union and budget")
    need(BUDGET-NEW_CAP == 10920698867749133, "new field reserve")
    print("PASS: EVERY normalized J=40000..44999; total", NEW_CAP, "; union", OLD_CAP)
    print("Finite arithmetic does not certify the universal proof or original-source transport")


if __name__ == "__main__":
    main()
