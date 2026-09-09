"""Independent integer prices and the actual preferred-slope obstruction."""

from collections import Counter
from itertools import product
from math import comb, lcm


def need(ok, message):
    if not ok:
        raise ValueError(message)


def combine(terms):
    denominator = lcm(*(d for _, d in terms))
    numerator = sum(n*(denominator//d) for n, d in terms)
    return numerator, denominator


def preferred_control():
    p, domain = 17, range(12)
    received = {x: (0, 0) if x < 6 else (x, p-1) for x in domain}
    complete, total_raw = set(), 0
    for gamma in domain:
        if gamma < 6:
            support = tuple(range(6, 12))+(gamma,)
            a, b, h = (0, 1), (p-1, 0), (-gamma % p, 1)
        else:
            support = tuple(range(6))+(gamma,)
            a, b, h = (0, 0), (0, 0), (0, 0)
        evaluate = lambda f, x: (f[0]+f[1]*x) % p
        need(all((received[x][0]+gamma*received[x][1]) % p == evaluate(h, x)
                 for x in support), "actual selected scalar agreement")
        minima = []
        best = len(support)+1
        for poly in product(range(p), repeat=2):
            raw = sum(evaluate(poly, x) != received[x][1] for x in support)
            if raw < best:
                best, minima = raw, [poly]
            elif raw == best:
                minima.append(poly)
        need(best == 1 and minima == [b], "actual unique minimizing carrier polynomial")
        values = Counter(received[x][1] for x in support)
        need(sorted(values.values()) == [1, 6] and 6 > 3-1,
             "six equal values force a degree-below-three interpolant constant, contradicted by seventh")
        core = {x for x in domain if received[x] == (evaluate(a, x), evaluate(b, x))}
        defects = set(support)-core
        need(len(core) == 6 and defects == {gamma}, "complete core and actual cross-core defect")
        need(all((received[x][0]+x*received[x][1]) % p == 0 for x in core), "primitive pencil row")
        complete.update(core)
        total_raw += best
    need(complete == set(domain) and total_raw == 12, "all low complete cores cover the domain")
    preferred = {gamma for gamma in domain if any((x-gamma) % p == 0 for x in complete)}
    need(preferred == set(domain), "every assigned label is preferred")
    gain_times_three = 3*12-total_raw
    need(gain_times_three == 24 > 0 and gain_times_three <= 3*len(preferred),
         "e=0 does not give zero gain; preferred charge repairs the assertion")


def main():
    r, d, hi, w, near = 1048576, 67472, 21499, 624373932788019251, 134944
    budget = 2130706433**6//2**128
    terms = [(w, 3)]
    for t in (1, 2):
        terms.append(((r-d+t)*(r-hi+2)*(r+1)**8,
                      t*(t+1)*(d-hi+2-t)*(d+1-t)**8))
    numerator, denominator = combine(terms)
    two = numerator//denominator+near
    need(two == 257846243054097181 and budget-two == 17134485057297906,
         "independent common-denominator two-anchor price")
    need((two-near)*denominator <= numerator < (two-near+1)*denominator, "exact final floor")
    for wrong in (two-1, two+1):
        need(not (wrong-near)*denominator <= numerator < (wrong-near+1)*denominator,
             "wrong printed exact total rejected")

    z = r+1
    derivative = [(i+1)*(-1)**i*comb(10, i)*z**(10-i) for i in range(11)]
    factored = [0]*11
    for i in range(10):
        c = (-1)**i*comb(9, i)*z**(9-i)
        factored[i] += z*c
        factored[i+1] -= 11*c
    need(derivative == factored, "exact derivative (Z-e)^9*(Z-11e)")
    peak_num, peak_den = z**11*10**10, 11**11
    for e in (0, z//11, z//11+1, r-d+2, z):
        need(0 <= e <= z and e*(z-e)**10*peak_den <= peak_num, "peak boundary controls")
    terms = [(w, 3), (r+hi, 1), (peak_num, peak_den*2*d**10),
             (peak_num, peak_den*6*(d-1)**10)]
    pn, pd = combine(terms)
    pencil = pn//pd+near
    need(pencil == 228260637755610995 and budget-pencil == 46720090355784092,
         "independent charged pencil price")
    need(w//3+r+hi+near == 208124644263878102 < pencil < two < budget,
         "all exhaustive branches below the original budget")
    need((r+1)-(r-d+2) == d-1 > 0, "small-union numerator stays positive")
    need(hi-9965+1 == 11535 and d-hi > 0, "entire unchanged remaining interval")
    preferred_control()
    print("PASS independent integer branch prices, derivative identity and exact floors")
    print("PASS actual F17 source: all12 preferred cross-core labels retained when outside union is empty")
    print("No primary imports; mathematical source and incidence proofs remain required")


if __name__ == "__main__":
    main()
