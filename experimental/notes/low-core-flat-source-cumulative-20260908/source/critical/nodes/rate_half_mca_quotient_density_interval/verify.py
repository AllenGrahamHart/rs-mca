"""Exact fixed-grid certificate; the universal argument is in proof.md."""

from functools import lru_cache
import hashlib
from math import comb, prod


R, GAP, D, C, NEAR = 1048576, 67472, 67466, 67467, 134944
BUDGET = 274980728111395087
LO, HI, JSTEP, APARTS, OCC, HEAVY = 32000, 39999, 2000, 8, 64, 8
SCALE = 1 << 128
CHILD = (0, 10755802499540570, 737012707696078, 50371450079970,
         3424826154478, 231038329409, 15278131113, 983145945,
         63264449, 4070947, 981105)
EXPECTED = {32000: 261925431454675420, 34000: 242907143759668079,
            36000: 225655255580817422, 38000: 220471747439971004}
EXPECTED_DIGESTS = {
    32000: "8d75b09e52c77b49efef7d35152906afaf9615d6812783a6dcebb69f7e0443f5",
    34000: "1fa689aad105afb8bd68753e3a27fc54cce6bf206b160d85f639a5c2f24724e1",
    36000: "c759ee3312cafb8a1c032031957eb8e59c737af75e410fe90d317af71fd650f4",
    38000: "8bab9ef29e113d834d30698ea054ad195e70c5edf620450b7126955e942f6466",
}


def need(ok, message):
    if not ok:
        raise ValueError(message)


def ceildiv(a, b):
    need(b > 0, "positive denominator")
    return -(-a//b)


@lru_cache(maxsize=8192)
def quadratic_coefficients(rank, gap, maximum):
    need(3 <= rank <= maximum <= gap, "quadratic domain")
    denominator = 2*(gap+2)
    a = SCALE*gap*(2*gap+1)//denominator
    b = SCALE*(3*gap+1)//denominator
    c = SCALE//denominator
    point = min(5000, maximum//2)
    for r in range(4, rank+1):
        need(b >= gap*c >= 0, "contraction coefficient gate")
        m, t, h = r-1, r-2, gap+r-1
        den = m*m*h
        f = a+b*m+c*m*m
        s1, s0 = (b-2*c)*h+f, (a-b+c)*h-m*f
        u3 = c*t*t
        u2 = b*t*m+2*c*t+gap*c*t*t
        u1 = a*m*m+b*m+c+gap*(b*t*m+2*c*t)
        u0 = gap*(a*m*m+b*m+c)
        need(u2 >= c*den, "convex tangent remainder")
        t1 = u1+2*(u2-c*den)*point+3*u3*point*point
        t0 = u0-(u2-c*den)*point*point-2*u3*point**3
        aa, bb = t0//den, t1//den
        shift = max(0, *(ceildiv((aa+bb*k)*h-s0-s1*k, h) for k in (r, maximum)))
        a, b = aa-shift, bb
        need(a*den <= t0 and b*den <= t1 and b >= gap*c, "rounded tangent gates")
        need(all((a+b*k)*h <= s0+s1*k for k in (r, maximum)), "whole-interval spike gate")
    return a, b, c


def quadratic(rank, gap, maximum, at):
    need(rank <= at <= maximum <= gap, "actual quotient range")
    if rank == 1:
        return gap+at
    if rank == 2:
        return (gap+at)*(gap+1)
    a, b, c = quadratic_coefficients(rank, gap, maximum)
    need(b >= 0 and c >= 0 and a+b*at+c*at*at > 0, "increasing positive quotient bound")
    return prod(gap+i for i in range(1, rank))*(a+b*at+c*at*at)//SCALE


def size(J, j, r, u, scale):
    den = APARTS*r*(r+1)
    num = (APARTS*(J-9)+u*(J-3993) if j == r == 1 else
           j*(den+(J-11)*(APARTS*r+u)))
    need(scale % den == 0, "size grid")
    return num*(scale//den)


def source_data(J0, J1, j, r, u):
    scale = APARTS*r*(r+1)*OCC*4*j
    corners = [(J, size(J, j, r, w, scale)) for J in (J0, J1) for w in (u, u+1)]
    a0, a1 = min(a for J, a in corners), max(a for J, a in corners)
    ell = 11-j
    degree0 = min(J*scale-a for J, a in corners)//scale
    degree1 = ceildiv(max(J*scale-a for J, a in corners), scale)
    need(ell <= degree0 <= degree1 <= D, "quotient rank and integer degree hull")
    factors = [min(max((C+i)*scale, (J+D)*scale-(10-i)*(a//j))
                   for J, a in corners) for i in range(j)]
    hybrid = min(prod([(J+D)*scale]+[(J+D)*scale-min(i*(a//j), (J-11+i)*scale)
                                   for i in range(1, 11)]) for J, a in corners)
    return scale, corners, a0, a1, ell, degree0, degree1, factors, hybrid


def core_cost(data, j, v):
    scale, corners, a0, a1, ell, degree0, degree1, factors, hybrid = data
    z0, z1, h1 = v*(a0//OCC), (v+1)*(a1//OCC), a1//j
    need(z1 < C*scale and z1 % 4 == 0, "positive completion / tangent grid")
    gap0 = D+(OCC-v-1)*(a0//OCC)//scale

    def outside(J, a, vv):
        x = (J+D)*scale-vv*(a//OCC)
        return prod([x]+[x-min((J-ell+i)*scale-a, i*(a//j)) for i in range(1, ell)])

    greedy = min(outside(J, a, vv) for J, a in corners for vv in (v, v+1))
    quote = quadratic(ell, gap0, degree1, degree0)
    base = prod(x-z1 for x in factors)
    inner = base
    for calibration in range(5):
        q, previous_d, coefficients = calibration*(z1//4), 0, []
        for b in range(1, j+1):
            vals = [x-q for x in factors[:j-b]]
            derivative = sum(prod(vals[i] for i in range(len(vals)) if i != v)
                             for v in range(len(vals)))
            coefficients.append(comb(11, b)*(prod(vals)+q*derivative)-previous_d)
            previous_d = comb(11, b)*derivative
        tail = coefficients[-1]
        for b in range(j-1, 0, -1):
            ratio = max(z0-b*h1, 0) if tail >= 0 else max(z1-b*scale, 0)
            tail = coefficients[b-1]+ratio*tail
        inner = max(inner, base+tail*(z0 if tail >= 0 else z1))
    count, direct = 1, base
    for b in range(1, j+1):
        count *= max(z0-(b-1)*h1, 0)
        direct += comb(11, b)*count*prod(x-z1+b*scale for x in factors[:j-b])
    inner = max(inner, direct)
    if j <= 5:
        old = prod((C+i)*scale-z0 for i in range(j))
        old += 11*prod((C+i)*scale for i in range(j-1))*z0
        inner = max(inner, old)
    need(inner > 0 and greedy > 0 and quote > 0, "positive basis factors")

    terms = [[] for b in range(j+1)]
    for J, a in corners:
        ds = [max((C+i)*scale, (J+D)*scale-(10-i)*(a//j)) for i in range(j)]
        for vv in (v, v+1):
            p, z, e = outside(J, a, vv), vv*(a//OCC), 1
            for b in range(j+1):
                if b:
                    e *= max(z-(b-1)*(a//j), 0)
                terms[b].append(comb(11, b)*p*e*prod(x-z+b*scale for x in ds[:j-b]))
    lower = max(greedy*inner//scale**11, quote*inner//scale**j,
                sum(min(values) for values in terms)//scale**11, hybrid//scale**11)
    return 12*lower


def run(J0, J1):
    digest = hashlib.sha256()
    resource = prod(R+J1-i for i in range(12))
    high = (GAP+J0)*prod(GAP+i for i in range(1, 11))*10488//125
    low_basis = prod((J0+D)*11-i*J0 for i in range(11))//11**11
    low_cap = resource//min(12*low_basis, high)+NEAR
    maximum, where = low_cap, ("low-density",)
    costs_seen, source_boxes = 0, 0
    for j in range(1, 11):
        for r in range(j, 11):
            for u in range(APARTS):
                data = source_data(J0, J1, j, r, u)
                costs = [min(high, core_cost(data, j, v)) for v in range(OCC)]
                costs_seen += len(costs)
                for v, cost in enumerate(costs):
                    digest.update(f"C:{J0},{j},{r},{u},{v}:{cost}\n".encode("ascii"))
                scale = data[0]
                aa, ab = size(J0, j, r, u+1, scale), size(J1, j, r, u+1, scale)
                for v in range(HEAVY):
                    den = 2*j*HEAVY
                    k0, k1 = (2*j-1)*HEAVY+v, (2*j-1)*HEAVY+v+1
                    light = (2*j-1)*HEAVY-v
                    bl = min(costs[:min(OCC, light*OCC//den+1)])
                    bh = min(costs[max(0, k0*OCC//den-1):min(OCC, ceildiv(k1*OCC, den)+1)])
                    qn = ((R+J0)*scale-aa)*den*CHILD[j]
                    qd = (GAP+J0)*scale*den-k1*aa
                    en, ed = (den-k0)*ab, den*scale
                    child = ceildiv(qn*ed+en*qd, qd*ed)
                    cap = (resource+max(0, bl-bh)*child)//bl+NEAR
                    source_boxes += 1
                    digest.update(f"S:{J0},{j},{r},{u},{v}:{cap}\n".encode("ascii"))
                    if cap > maximum:
                        maximum, where = cap, (j, r, u, v)
        print("PREFIX", (J0, J1), "rank", j, "maximum", maximum, where, flush=True)
    need(costs_seen == 28160 and source_boxes == 3520, "complete box inventory")
    need(maximum < BUDGET, "all source boxes fit budget")
    need(maximum == EXPECTED[J0], "frozen interval maximum")
    need(digest.hexdigest() == EXPECTED_DIGESTS[J0], "all record costs and source bounds")
    print("INTERVAL", J0, J1, "cap", maximum, "at", where,
          "cost boxes", costs_seen, "source boxes", source_boxes, flush=True)
    print("DIGEST", J0, digest.hexdigest(), flush=True)
    return maximum, where


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=int, choices=range(LO, HI+1, JSTEP))
    args = parser.parse_args()
    starts = [args.start] if args.start is not None else range(LO, HI+1, JSTEP)
    for start in starts:
        run(start, min(start+JSTEP-1, HI))
    need(84*125*(GAP+1-77) > 10488*(GAP+1) and GAP+1 > 12*84, "HIGH weight gate")
    need(max(EXPECTED.values()) > 248408859318207582, "old large-fiber class fits new maximum")
    need(max(EXPECTED.values()) < 274929007493481160 < BUDGET, "whole-source union")
