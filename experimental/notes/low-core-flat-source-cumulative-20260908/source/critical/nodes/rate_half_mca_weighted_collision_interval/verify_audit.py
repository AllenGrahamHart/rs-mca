"""Separate integer-pair weighted-collision certificate; no Fraction/primary import."""

import hashlib
import importlib.util
from math import prod
from pathlib import Path


path = Path(__file__).resolve().parents[1]/"rate_half_mca_collision_profile_interval/verify_audit.py"
spec = importlib.util.spec_from_file_location("previous_integer_audit", path)
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
D, R, GAP, NEAR = 67466, 1048576, 67472, 134944
LO, HI, TOTAL = 21800, 22499, 274954262108377832
TRIGGER = 274960000000000000
EXPECTED = "b0d340b813df77e827f49d3b4d273c8de17c42214f12e4823ee1d87edc8aaafb"
frac, minimum, maximum = b.fraction, b.minimum, b.maximum


def check(ok, why):
    if not ok:
        raise ValueError(why)


def add(a, c):
    return frac(a[0]*c[1]+c[0]*a[1], a[1]*c[1])


def neg(a):
    return -a[0], a[1]


def mul(a, c):
    return frac(a[0]*c[0], a[1]*c[1])


def printed(a):
    return str(a[0]) if a[1] == 1 else f"{a[0]}/{a[1]}"


def polynomial_with_derivative(argument, slopes):
    xn, xd = argument
    check(xn >= xd > 0, "positive convex argument")
    numerator, derivative, denominator = D+1, 0, 1
    for sn, sd in slopes:
        factor_n, factor_d = (D+1)*xd*sd+(xn-xd)*sn, xd*sd
        # Both value and derivative use one common denominator at every step.
        derivative = derivative*factor_n+numerator*sn*xd
        numerator *= factor_n
        denominator *= factor_d
    return frac(numerator, denominator), frac(derivative, denominator)


def root_costs(left, right, t, first, last, credit, Tmax):
    m0, m1, ell, k = D+left, D+right, 11-t, right-first
    mu = b.coefficients(11, left, right, last, t)
    cmin = (first*(first-1) if t == 1 else 0, 1)
    moment = ((D+k)**2, 1) if ell == 1 else maximum(
        ((D+k)*(k-1), ell-1), (D+k+(k-ell+1)*(k-ell), 1))
    on, od = minimum(moment, ((D+k)*last, t))
    split = (last*last*od+t*on-m0*t*od, t*od)
    cmax = minimum((m1*(last-t), t),
                   (m1*((right-1)*mu[11][0]-mu[11][1]), mu[11][1]),
                   (Tmax, 1), split)
    check(not b.less(cmax, cmin), "no omitted parameter box")
    check(left*t-last >= t and (left-2)*m0*cmax[1] >= cmax[0],
          "whole convex domain guards")
    G = b.product(10, (left*t-last, t), mu)
    bonus_coefficient = mul((11, 1), mul(credit, G))
    slopes = [frac(prod(mu[r][1]-mu[r][0] for r in range(a+1, 11)),
                   prod(mu[r][1] for r in range(a+1, 11))) for a in range(2, 11)]
    lower = (0, 1)
    for i in range(5):
        point = add(mul(cmin, (4-i, 4)), mul(cmax, (i, 4)))
        x = add((left-1, 1), neg(mul(point, (1, m0))))
        value, derivative = polynomial_with_derivative(x, slopes)
        coefficient = add(bonus_coefficient, neg(derivative))
        endpoint = cmin if coefficient[0] >= 0 else cmax
        candidate = add(add(mul((m0, 1), value), mul(point, derivative)),
                        mul(coefficient, endpoint))
        lower = maximum(lower, candidate)
    check(lower[0] > 0, "positive record cost")
    return lower, mul(bonus_coefficient, cmin), cmin, cmax


def old_cost(left, right, t, first, last):
    ell, k0, k1 = 11-t, max(11-t, left-last), right-first
    factors = [max(D+11-r, D+left-r*last//t) for r in range(10, ell-1, -1)]
    caps = [i*last//t for i in range(1, t)]
    inner = b.old.inner(factors, first, last, caps)
    if ell == 1:
        quotient = (D+k0, 1)
    else:
        greedy = (D+k0)*prod(max(D+ell-i, D+k0-i*last//t) for i in range(1, ell))
        hn, hd = minimum((k1-ell+1, 1), (last, t))
        quotient = maximum(b.old.quotient(ell, k0, k1, greedy),
                           b.profile_bound(ell, k0, k1, hn, hd))
    hybrid = (D+left)*prod(max(D+11-r, D+left-r*last//t) for r in range(1, 11))
    return maximum(mul(quotient, (inner, 1)), (hybrid, 1),
                   b.profile_bound(11, left, right, last, t))


def data(left, right):
    n0, n1 = R+left, R+right
    check(n0 >= 10*(right-10), "first source-cap branch on whole box")
    Tmax = n1*(right-11)//10
    cn = 66*(n0-2)*(n0-3)-660*(right-6003)*(n1-3)-1485*Tmax
    cd = 12*(n1-1)*(n1-2)*(n1-3)
    check(cn > 0, "positive common source credit")
    credit = frac(cn, cd)
    resource = prod(range(n1-11, n1+1))
    high = frac(10488*(GAP+left)*prod(range(GAP+1, GAP+11)), 125)
    return credit, Tmax, resource, high, right-11+Tmax//2+NEAR


def main():
    digest = hashlib.sha256()
    left, blocks, boxes, floors, used = LO, 0, 0, 0, 0
    peak = 0, None
    ranks = [0]*10
    while left <= HI:
        right = min(left+15, HI)
        credit, Tmax, resource, high, addback = data(left, right)
        digest.update(f"R:{left},{right}:{printed(credit)}:{Tmax}:{resource}:{addback}\n".encode())
        for t in range(1, 11):
            top = min(right-11+t, right-6001 if t == 1 else right)
            width = (top-t+128)//128
            first = t
            while first <= top:
                last = min(first+width-1, top)
                lower, bonus, cmin, cmax = root_costs(left, right, t, first, last, credit, Tmax)
                cost = mul((12, 1), lower)
                preliminary = minimum(cost, high)
                if resource*preliminary[1]//preliminary[0]+addback > TRIGGER:
                    cost = maximum(cost, mul((12, 1), add(old_cost(left, right, t, first, last), bonus)))
                    used += 1
                cost = minimum(cost, high)
                quotient, remainder = divmod(resource*cost[1], cost[0])
                check(0 <= remainder < cost[0], "exact Euclidean resource division")
                for wrong in (quotient-1, quotient+1):
                    check(not 0 <= resource*cost[1]-wrong*cost[0] < cost[0], "reject adjacent wrong floor")
                    floors += 1
                cap = quotient+addback
                check(cap <= TOTAL, "every box paid")
                digest.update(f"B:{left},{right},{t},{first},{last}:{printed(cmin)}:{printed(cmax)}:{printed(lower)}:{printed(bonus)}:{printed(cost)}:{cap}\n".encode())
                if cap > peak[0]:
                    peak = cap, (left, right, t, first, last)
                boxes += 1
                ranks[t-1] += 1
                first = last+1
            check(first == top+1, "all sizes covered without gaps")
        blocks += 1
        print("AUDIT BLOCK", left, right, "boxes", boxes, "maximum", peak[0], flush=True)
        left = right+1
    check(left == HI+1 and blocks == 44 and boxes == 56320 and floors == 112640
          and set(ranks) == {5632} and used == 12990, "independent full inventory")
    check(peak == (TOTAL, (22056, 22071, 5, 19554, 19726)), "exact certificate maximum")
    print("CERTIFICATE", peak, "old-used", used, "DIGEST", digest.hexdigest(), flush=True)
    check(digest.hexdigest() == EXPECTED, "all exact entries agree with frozen digest")
    print("PASS independent integer audit; all weighted boxes; no primary/Fraction import")


if __name__ == "__main__":
    main()
