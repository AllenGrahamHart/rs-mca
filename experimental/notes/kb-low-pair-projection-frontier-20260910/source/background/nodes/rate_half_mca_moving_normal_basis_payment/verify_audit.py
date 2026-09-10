"""Independent polynomial reconstruction, with no primary/compiler imports."""

from fractions import Fraction as Q
from math import prod


def need(ok, message):
    if not ok:
        raise ValueError(message)


def add(a, b):
    return [(a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)
            for i in range(max(len(a), len(b)))]


def scale(a, b):
    return [x*b for x in a]


def multiply(a, b):
    result = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result


def value(poly, x):
    result = Q(0)
    for coefficient in reversed(poly):
        result = result*x+coefficient
    return result


def compose(poly, constant, slope):
    result = [Q(0)]
    for coefficient in reversed(poly):
        result = add(multiply(result, [constant, slope]), [coefficient])
    return result[:len(poly)]


def main():
    gap, E, X, L, R = 67465, 21499, 5000, 9965, 1048576
    poly = scale(multiply([gap, 1], [2*gap+1, 1]), Q(1, 2*(gap+2)))
    curvature = poly[2]
    for rank in range(4, 11):
        need(poly[1] >= gap*poly[2] >= 0, "input theorem gate")
        H = gap+rank-1
        spike = add(compose(poly, -1, 1), scale([-(rank-1), 1], value(poly, rank-1)/H))
        equal = scale(multiply([gap, 1], compose(poly, Q(1, rank-1), Q(rank-2, rank-1))), Q(1, H))
        tangent_target = add(equal, [0, 0, -curvature])
        slope = value([i*tangent_target[i] for i in range(1, len(tangent_target))], X)
        intercept = value(tangent_target, X)-slope*X
        candidate = [intercept, slope, curvature]
        shift = max(Q(0), value(candidate, rank)-value(spike, rank),
                    value(candidate, E)-value(spike, E))
        candidate[0] -= shift
        need(all(value(candidate, k) <= value(spike, k) for k in (rank, E)), "affine spike endpoints")
        need(spike[2] == candidate[2] and equal[2] >= curvature and equal[3] >= 0,
             "global nonnegative remainder coefficients")
        remainder = add([shift], multiply([X*X, -2*X, 1],
                                         [equal[2]-curvature+2*X*equal[3], equal[3]]))
        need(add(equal, scale(candidate, -1)) == remainder, "exact polynomial squared identity")
        need(min(candidate) > 0 and candidate[1] >= gap*curvature, "next universal theorem gate")
        poly = candidate
    need((poly[1]+2*poly[2]*L)*(R+L-10) > 11*value(poly, E), "whole-interval derivative comparison")
    low = Q(5*prod(range(R+L-10, R+L+1)), 11*prod(range(gap+1, gap+10)))/value(poly, L)
    M = low.numerator//low.denominator
    need(M == 222676884802638507 and M <= low < M+1, "exact low mass floor")
    pn, pd = 1, 1
    for s in range(11, 0, -1):
        bad, n, A = E-s, R+E, E+gap
        need(2*s > s and A > bad >= 0, "strict rank-two anchor guard")
        pn, pd = pn*(n-bad), pd*(A-bad)
    P = pn//pd
    need(P == 12774319384974, "actual pair floor")
    W, near, budget = 624373932788019251, 134944, 274980728111395087
    amount = W+7*(M+E-6+5*P)
    need(amount//8+near == 272944903448274111 < budget, "all exceptions and high records")
    need((W+7*(M+E-6))//8+near == 272889015800964850, "all pair lines contained")
    outside = 2326656757852545
    target = 8*(budget-near+1)-amount
    need(7*(outside-1) < target <= 7*outside, "strict outside-label ceiling")
    print("PASS seven polynomial identities, guarded pair floors and independent original-slope prices")
    print("Universal basis, moving-normal ownership and original HIGH44 remain proved-source inputs")


if __name__ == "__main__":
    main()
