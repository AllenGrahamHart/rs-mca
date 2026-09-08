"""Tiny actual inside-count and complete-core tuple controls; no field-scale search."""

import importlib.util
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial, prod
from pathlib import Path


path = Path(__file__).resolve().parents[1]/"mca_maximum_density_flat_core_basis_resource"/"verify.py"
spec = importlib.util.spec_from_file_location("small_source_helpers", path)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
need, rank = helper.check, helper.rank


def bad(u, v, support, k, p):
    rows = [[pow(x, i, p) for i in range(k)]+[u[x], v[x]] for x in support]
    return rank(rows, p) > k


def falling(n, k):
    return prod(max(n-i, 0) for i in range(k))


def inside_controls():
    s, j, m, c, h = 11, 6, 17, 7, 1
    # The F_29 degree-<11 Vandermonde carrier has maximum flat density one.
    for t in range(7):
        e = [falling(t, b) for b in range(j+1)]
        need(all((t-b)*e[b] == (e[b+1] if b < j else 0) for b in range(j+1)),
             "actual inside-extension identity")
        outside = falling(m-t, s-j)
        exact = outside*sum(comb(s, b)*e[b]*prod(c+i-(t-b) for i in range(j-b))
                            for b in range(j+1))
        need(exact == falling(m, s), "actual uniform inside-cardinality partition")
        for q in (F(0), F(c, 2), F(c-1)):
            p = c-q
            l = lambda k: p**k+(k*q*p**(k-1) if k else 0)
            d = lambda k: k*p**(k-1) if k else 0
            coupled = (c-t)**j+11*l(j-1)*t
            before_bounds = coupled
            for b in range(2, j+1):
                coefficient = comb(s, b)*l(j-b)-comb(s, b-1)*d(j-b+1)
                before_bounds += coefficient*e[b]
                low, upper = prod(max(t-i*h, 0) for i in range(b)), t**b
                need(low <= e[b] <= upper, "actual tuple sandwich")
                coupled += coefficient*(low if coefficient >= 0 else upper)
            direct_tangents = (c-t)**j+sum(comb(s, b)*(l(j-b)*e[b]
                                  -d(j-b)*(e[b+1] if b < j else 0)) for b in range(1, j+1))
            need(before_bounds == direct_tangents, "couple before taking sign bounds")
            need(coupled <= before_bounds and outside*before_bounds <= exact, "valid signed lower count")
    print("PASS: 21 exact rank-six Vandermonde tangent/coupling controls")


def complete_core_controls():
    p, k, s, m = 29, 4, 3, 5
    points, full_core, flat = list(range(10)), list(range(8)), [0, 1]
    u, v = {x: 0 for x in points}, {x: 0 for x in points}
    v[8], u[9], v[9] = 1, -1, 1
    ev = {x: (1, x, x*x % p) for x in points}
    rows = [ev[x] for x in flat]
    need(rank(rows, p) == 2 and [x for x in points if rank(rows+[ev[x]], p) == 2] == flat,
         "complete actual flat")
    frozen_core = [2, 3, 4, 5]
    packed_core = [0, 1, 2, 3]
    need(len(packed_core) == m-1 and set(flat) <= set(packed_core), "pack all actual flat-core points")
    all_tuples = set()
    for gamma, defect in ((0, 8), (1, 9)):
        witness = frozen_core+[defect]
        need(bad(u, v, witness, k, p), "original full-code-bad witness")
        need(all((u[x]+gamma*v[x]) % p == 0 for x in witness), "original scalar equation")
        need(not set(flat).intersection(witness), "original witness omits complete flat core")
        need(all(u[x] == v[x] == 0 for x in packed_core), "extra points match the frozen pair")
        tuples = {tuple(xs) for xs in combinations(sorted(packed_core+[defect]), s+1)
                  if rank([(v[x], *ev[x]) for x in xs], p) == s+1}
        bases = factorial(s)*sum(rank([ev[x] for x in xs], p) == s
                                 for xs in combinations(packed_core, s))
        need(factorial(s+1)*len(tuples) == (s+1)*bases, "full-core/old-defect insertion count")
        need(any(not set(xs) <= set(witness) for xs in tuples), "tuples genuinely leave the old witness")
        need(not all_tuples.intersection(tuples), "original labels have disjoint tuples")
        all_tuples.update(tuples)
    print("PASS: actual full-code-bad witnesses omit A; packed core tuples retain original labels")
    # TWO-COST is sharp on this elementary same-resource ledger.
    need(10*6+8*5 == 100 and 6+5 == F(100, 10)+(1-F(8, 10))*5, "sharp two-cost bound")
    need(max(0, 1-F(12, 10)) == 0, "nonnegative heavy coefficient when its cost is larger")
    print("PASS: exact heavy cost, positive-part branch and no support/minimizer reselection")


if __name__ == "__main__":
    inside_controls()
    complete_core_controls()
    print("These component controls do not certify the universal hand proof or a finite Prize row")
