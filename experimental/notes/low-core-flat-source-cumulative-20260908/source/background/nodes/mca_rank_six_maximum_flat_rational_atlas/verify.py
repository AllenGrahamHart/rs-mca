"""Tiny actual-field annihilator controls and exact finite atlas envelopes."""

from fractions import Fraction
from itertools import combinations
from math import isqrt


def need(ok, why):
    if not ok:
        raise ValueError(why)


def trim(a, p):
    a = [x % p for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p, sign=1):
    return trim([(a[i] if i < len(a) else 0)
                 + sign*(b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))], p)


def mul(a, b, p):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out, p)


def evaluate(a, x, p):
    out = 0
    for c in reversed(a):
        out = (out*x+c) % p
    return out


def locator(xs, p):
    out = [1]
    for x in xs:
        out = mul(out, [-x, 1], p)
    return out


def divide_exact(a, b, p):
    out, remainder = [0]*max(1, len(a)-len(b)+1), trim(a, p)
    while remainder != [0] and len(remainder) >= len(b):
        shift = len(remainder)-len(b)
        coefficient = remainder[-1]*pow(b[-1], -1, p) % p
        out[shift] = coefficient
        remainder = add(remainder, [0]*shift+[coefficient*x for x in b], p, -1)
    need(remainder == [0], "full locator divides actual annihilator polynomial")
    return trim(out, p)


def combination(coefficients, polynomials, p):
    out = [0]
    for c, f in zip(coefficients, polynomials):
        out = add(out, [c*x for x in f], p)
    return out


def rref(rows, p):
    a = [[v % p for v in row] for row in rows]
    pivots = []
    for column in range(len(a[0])):
        pivot = next((i for i in range(len(pivots), len(a)) if a[i][column]), None)
        if pivot is None:
            continue
        r = len(pivots)
        a[r], a[pivot] = a[pivot], a[r]
        scale = pow(a[r][column], -1, p)
        a[r] = [v*scale % p for v in a[r]]
        for i in range(len(a)):
            if i != r:
                scale = a[i][column]
                a[i] = [(x-scale*y) % p for x, y in zip(a[i], a[r])]
        pivots.append(column)
        if len(pivots) == len(a):
            break
    return a, pivots


def rank(rows, p):
    return len(rref(rows, p)[1])


def kernel(rows, p):
    reduced, pivots = rref(rows, p)
    result = []
    for free in range(len(rows[0])):
        if free in pivots:
            continue
        v = [0]*len(rows[0])
        v[free] = 1
        for i, pivot in enumerate(pivots):
            v[pivot] = -reduced[i][free] % p
        need(all(sum(x*y for x, y in zip(row, v)) % p == 0 for row in rows),
             "actual coefficient-kernel vector")
        result.append(v)
    return result


def monomial(i):
    return [0]*i+[1]


def coefficient_rows(polynomials):
    size = max(map(len, polynomials))
    return [a+[0]*(size-len(a)) for a in polynomials]


def triple(p, K, carrier, sets, expected_dimension, expected_direction=None,
           annihilators=None):
    need(all(p % i for i in range(2, isqrt(p)+1)), "prime field")
    H = sorted(set().union(*map(set, sets)))
    need(len(H) > K and len(carrier) == 11 and max(map(len, carrier)) <= K,
         "actual polynomial source")
    need(rank(coefficient_rows(carrier), p) == 11, "actual carrier dimension")
    need(all(any(evaluate(f, x, p) for f in carrier) for x in H),
         "all core evaluations are nonzero")
    locators = [locator(xs, p) for xs in sets]
    spaces = annihilators or [[mul(P, monomial(i), p) for i in range(5)] for P in locators]
    for xs, space in zip(sets, spaces):
        need(rank([[evaluate(f, x, p) for f in carrier] for x in xs], p) == 6,
             "actual rank-six evaluation flat")
        need(rank(coefficient_rows(carrier+space), p) == 11,
             "five locator multiples belong to the carrier")
        need({x for x in H if all(evaluate(f, x, p) == 0 for f in space)} == set(xs),
             "complete flat, no hidden removed roots")
    for A, B in combinations(sets, 2):
        need(rank([[evaluate(f, x, p) for f in carrier] for x in set(A) | set(B)], p) == 11,
             "pairwise full joins")
    signed = spaces[0]+spaces[1]+[[-c % p for c in f] for f in spaces[2]]
    relations = kernel(list(map(list, zip(*coefficient_rows(signed)))), p)
    need(len(relations) == expected_dimension, "actual intersection dimension")
    normalized = [[divide_exact(f, P, p) for f in space]
                  for P, space in zip(locators[:2], spaces[:2])]
    pairs = [(combination(v[:5], normalized[0], p),
              combination(v[5:10], normalized[1], p)) for v in relations]
    minors = [add(mul(f, gg, p), mul(ff, g, p), p, -1)
              for (f, g), (ff, gg) in combinations(pairs, 2)]
    outside = set(sets[2])-set(sets[0])-set(sets[1])
    bound = 2*K-len(sets[0])-len(sets[1])-2
    need(all(evaluate(D, x, p) == 0 for D in minors for x in outside),
         "cross determinants have every required actual root")
    if expected_direction is not None:
        f0, g0 = expected_direction
        need(len(outside) > bound and all(D == [0] for D in minors),
             "strict-root rank-one conclusion")
        need(all(add(mul(f, g0, p), mul(f0, g, p), p, -1) == [0]
                 for f, g in pairs), "predicted common primitive direction")
    else:
        need(len(outside) <= bound and any(D != [0] for D in minors),
             "omitting root threshold really fails on an actual source")
    print("FIELD", p, "M/K", len(H), K, "sizes", list(map(len, sets)),
          "intersection", len(relations), "outside/degree", len(outside), bound,
          "nonzero cross minors", sum(D != [0] for D in minors), flush=True)
    return pairs


def actual_sources():
    p, a = 193, 24
    fibers = {}
    for x in range(1, p):
        fibers.setdefault(pow(x, a, p), []).append(x)
    alpha, beta, gamma = sorted(fibers)[:3]
    carrier = [monomial(i) for i in (*range(6), *range(a, a+5))]
    inv = pow((alpha-beta) % p, -1, p)
    f, g = (gamma-beta)*inv % p, (alpha-gamma)*inv % p
    sets = [fibers[c] for c in (alpha, beta, gamma)]
    triple(p, 29, carrier, sets, 5, ([f], [g]))
    need(all(len(xs) == 24 for xs in sets), "three maximum-density flats")
    need(all(r+18 <= 4*r for r in range(6, 11)), "root caps imply density<=4")
    # P_<=5 lies in this carrier, so every <=6 distinct evaluations are independent.
    need(carrier[:6] == [monomial(i) for i in range(6)], "small-flat density gate")
    need(Fraction(4) > Fraction(29-4, 7), "strict maximum-density gate")
    need(36*4 > 72 and 3 <= Fraction(5*72, 36*4-72), "actual three-flat packing")
    need(carrier[:2] == [[1], [0, 1]], "projective fibers are singletons")

    p, a = 1201, 24
    A = [x for x in range(p) if pow(x, a, p) == 1]
    B = [x for x in range(p) if pow(x, a, p) == p-1]
    C = [x for x in range(p) if pow(x, a+1, p) == 1]
    PA, PB = locator(A, p), locator(B, p)
    R = add(mul(PA, [1, 1], p), mul(PB, [-1, 1], p), p)
    carrier = [mul(P, monomial(i), p) for P in (PA, PB) for i in range(5)]
    carrier.append(mul(R, monomial(4), p))
    need([len(A), len(B), len(C)] == [24, 24, 25], "split locator sizes")
    triple(p, 30, carrier, (A, B, C), 4, ([1, 1], [-1, 1]))

    root = next(x for x in range(p) if x not in set(A+B+C))
    factor = [-root, 1]
    directions = ([1, 1], [-1, 1])
    spaces = [[P]+[mul(mul(P, mul(component, factor, p), p), monomial(i), p)
                   for i in range(4)] for P, component in zip((PA, PB), directions)]
    PC = locator(C+[root], p)
    spaces.append([mul(PC, monomial(i), p) for i in range(5)])
    carrier = spaces[0]+spaces[1]+[spaces[2][-1]]
    pairs = triple(p, 31, carrier, (A, B, C+[root]), 4, directions, spaces)
    need(evaluate(R, root, p) != 0 and all(evaluate(f, root, p) == 0
         and evaluate(g, root, p) == 0 for f, g in pairs),
         "multiplier gcd root is indispensable: primitive R alone misses it")

    triple(23, 11, [monomial(i) for i in range(11)],
           (list(range(6)), list(range(6, 12)), list(range(12, 18))), 4)


def finite_controls():
    D, top = 67466, 22999
    for start, cap in ((20481, 25), (22500, 17)):
        denominator = 29*start-7*D-144
        bound = Fraction(35*(D+start), denominator)
        need(denominator > 0 and cap < bound < cap+1, "exact endpoint envelope")
        need(-35*(36*D+144) < 0, "entire degree interval decreases")
        need(16*Fraction(start-4, 7) > 2*start-2, "strict cross-root gate")
        for wrong in (cap-1, cap+1):
            need(not wrong <= bound < wrong+1, "reject adjacent wrong envelope floor")
        print("WHOLE INTERVAL", start, top, "atlas bound", cap, "envelope", bound)
    degree = -(-(top+24)//7)-1
    need(degree == 3288 and degree-4 == 3284, "strict integer quotient-degree pin")
    need(36*Fraction(22500-4, 7) < 1048576+22500,
         "the full original domain does NOT satisfy the packing denominator gate")
    need(16*Fraction(25-4, 7) == 2*25-2, "retain K>=26 strict guard")
    tested = 0
    for K in range(26, 41):
        for a in range(6, K-4):
            h = Fraction(a, 6)
            for b in range(6, a+1):
                if 2*b-5*h <= K-4:
                    continue
                e = 6*h-b
                need(e >= 0 and 7*(h-1) > K-11+2*e, "robust proper-join exclusion")
                need(3*b-2*h > 2*K-2, "robust strict cross-root gate")
                tested += 1
    need(tested > 0, "nonempty near-maximum controls")
    print("PASS", tested, "exact near-maximum band gates")
    print("PASS: no label count, no whole degree removed, unrestricted Prize remains open")


if __name__ == "__main__":
    actual_sources()
    finite_controls()
