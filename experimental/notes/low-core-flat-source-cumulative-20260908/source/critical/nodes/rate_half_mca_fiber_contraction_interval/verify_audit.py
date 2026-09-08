"""Independent unnormalized polynomial certificate and exact floor audit."""

from fractions import Fraction as F
from math import prod


def need(ok, message):
    if not ok:
        raise ValueError(message)


def add(a, b):
    return [(a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)
            for i in range(max(len(a), len(b)))]


def scale(a, c):
    return [x*c for x in a]


def mul(a, b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def compose(a, b):
    out = [F(0)]
    for c in reversed(a):
        out = add(mul(out, b), [c])
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def value(a, x):
    total = F(0)
    for c in reversed(a):
        total = total*x+c
    return total


def derivative(a):
    return [i*a[i] for i in range(1, len(a))]


def same(a, b):
    return not any(add(a, scale(b, -1)))


def floor_certificate(ratio, proposed):
    need(proposed*ratio.denominator <= ratio.numerator < (proposed+1)*ratio.denominator,
         "exact floor cross products")


def main():
    d, end, start, anchor = 67466, 65000, 53000, 5000
    polynomial = scale(mul([d, 1], [F(2*d+1, 2), F(1, 2)]), d+1)
    for rank in range(4, 12):
        need(polynomial[1] >= d*polynomial[2] >= 0, "child concavity")
        spike = add(scale([-(rank-1), 1], value(polynomial, rank-1)),
                    scale(compose(polynomial, [-1, 1]), d+rank-1))
        equal = mul([d, 1], compose(polynomial, [F(1, rank-1), F(rank-2, rank-1)]))
        curvature = (d+rank-1)*polynomial[2]
        residual = add(equal, [0, 0, -curvature])
        need(residual[2] >= 0 and residual[3] >= 0, "nonnegative cubic remainder")
        slope = value(derivative(residual), anchor)
        intercept = value(residual, anchor)-anchor*slope
        raw = [intercept, slope, curvature]
        shift = max(F(0), *(value(raw, k)-value(spike, k) for k in (rank, end)))
        following = [intercept-shift, slope, curvature]
        factorized = add([shift], mul(mul([-anchor, 1], [-anchor, 1]),
                                      [residual[2]+2*anchor*residual[3], residual[3]]))
        need(same(add(equal, scale(following, -1)), factorized), "global uniform factorization")
        need(shift >= 0 and all(x >= 0 for x in factorized[-2:]), "remainder high coefficients")
        difference = add(spike, scale(following, -1))
        need(difference[2] == 0, "affine spike remainder")
        need(all(value(difference, k) >= 0 for k in (rank, end)), "whole spike interval")
        need(following[1] >= d*following[2], "next child concavity")
        hostile = add(following, [1])
        need(any(value(hostile, k) > min(value(spike, k), value(equal, k))
                 for k in (rank, end, anchor)), "reject upward certificate mutation")
        polynomial = following
    r0, slack, near = 1048576, 67472, 134944
    need(value(polynomial, start) > 0, "positive basis count")
    need(value(derivative(polynomial), start)*(r0+start-11)
         > 12*value(polynomial, end), "uniform decreasing quotient")
    ratio = F(prod(r0+start-i for i in range(12)), 12)/value(polynomial, start)
    target = 274171207928811099-near
    floor_certificate(ratio, target)
    for mutated in (target-1, target+1):
        try:
            floor_certificate(ratio, mutated)
        except ValueError:
            pass
        else:
            raise ValueError("accepted incorrect LOW floor")
    pd = prod(slack+i for i in range(1, 11))
    resource = [F(prod(r0+k-i for i in range(12)), (slack+k)*pd) for k in (start, end)]
    ceiling = 14024864706947406176
    need(all(x <= ceiling for x in resource) and resource[1] > ceiling-1, "resource ceilings")
    high_ratio = F(125*ceiling, 10488)
    floor_certificate(high_ratio, 167153707891861276-near)
    need(167153707891861276 < target+near < 274929007493481160, "one-budget max and union")
    need(2130706433**6//2**128-274929007493481160 == 51720617913927, "field reserve")
    print("PASS: eight independent polynomial identities and eight upward mutations rejected")
    print("PASS: LOW 274171207928811099; HIGH 167153707891861276; two floor mutations rejected")
    print("No hull pruning, heuristic carrier sampling or floating-point gates")


if __name__ == "__main__":
    main()
