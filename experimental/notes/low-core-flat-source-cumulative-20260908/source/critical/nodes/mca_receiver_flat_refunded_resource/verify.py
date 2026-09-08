"""Tiny actual rank-two flat transport, overlap and shared-budget controls."""

import importlib.util
from fractions import Fraction as F
from itertools import combinations
from math import factorial
from pathlib import Path


path = Path(__file__).resolve().parents[1]/"mca_receiver_fiber_peeling"/"verify.py"
spec = importlib.util.spec_from_file_location("fiber_controls", path)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
need, rank, value = helper.require, helper.rank, helper.value
mul, scale, locator, divide, bad = helper.mul, helper.scale, helper.locator, helper.divide, helper.bad


def actual_source():
    p, k, m, s = 23, 10, 12, 4
    points, fiber = list(range(15))+[22], list(range(7))
    q, loc = [-22, 1], locator(fiber, p)
    direction = mul(mul(q, loc, p), [0, 1], p)
    carrier = [q, mul(q, [0, 1], p), mul(q, loc, p), direction]
    need(rank([f+[0]*(k-len(f)) for f in carrier], p) == s, "actual carrier rank")
    base = {x: (0, 0) for x in points}
    base.update({6: (1, 1), 12: (-1, 1), 13: (-2, 1), 14: (-3, 1)})
    u = {x: value(q, x, p)*base[x][0] % p for x in points}
    v = {x: (value(q, x, p)*base[x][1]+value(direction, x, p)) % p for x in points}
    u[22] = 1
    ev = {x: tuple(value(f, x, p) for f in carrier) for x in points}
    actual = [x for x in points if any(ev[x]) and ev[x][2:] == (0, 0)]
    need(actual == fiber and rank([ev[x] for x in fiber], p) == 2, "complete rank-two flat")
    keys = {tuple(y*pow(ev[x][0], -1, p) % p for y in ev[x]) for x in points if any(ev[x])}
    need(len(keys) == 15, "no repeated projective evaluation fiber")
    quotient = [divide(f, q, p) for f in carrier]
    need(max(map(len, quotient)) == 9, "common factor gives effective degree nine")
    need(F(9-4+2, 2) == F(7, 2) > F(9-4+3, 3), "rank-two/three root density ceilings")
    need(not any(not any(ev[x]) and u[x] == v[x] == 0 for x in points), "empty universal core")
    delta, t = F(7, 2), 6
    need(t > 7-delta/2, "actual heavy flat core")
    outside = [x for x in points if x not in fiber]
    uc = {x: u[x]*pow(value(loc, x, p), -1, p) % p for x in outside}
    vc = {x: v[x]*pow(value(loc, x, p), -1, p) % p for x in outside}
    child_space = [divide(f, loc, p) for f in carrier[2:]]
    need(rank([f+[0]*(3-len(f)) for f in child_space], p) == 2, "actual lower rank and degree")
    need(22 in outside and uc[22] != 0 and vc[22] == 0, "nonuniversal zero retained")
    need(not any(not any(value(f, x, p) for f in child_space) and uc[x] == vc[x] == 0
                 for x in outside), "empty child universal core")
    seen, supports, discarded = set(), {}, []
    for gamma, defect in ((p-1, 6), (1, 12), (2, 13), (3, 14)):
        h = scale(direction, gamma, p)
        core = [x for x in points if u[x] == 0 and v[x] == value(direction, x, p)]
        support = core+[defect]
        need(len(core) == m-1 and len(set(support)) == m, "raw-one support")
        need(all((u[x]+gamma*v[x]-value(h, x, p)) % p == 0 for x in support), "scalar agreement")
        need(bad(u, v, support, k, p), "full-code bad original support")
        bases = factorial(s)*sum(rank([ev[x] for x in xs], p) == s
                                 for xs in combinations(core, s))
        tuples = {xs for xs in combinations(sorted(support), s+1)
                  if rank([(v[x], *ev[x]) for x in xs], p) == s+1}
        need(factorial(s+1)*len(tuples) == (s+1)*bases, "exact core/defect tuple count")
        need(not seen.intersection(tuples), "same-source original label ownership")
        seen.update(tuples)
        complete = [x for x in points if (u[x]+gamma*v[x]-value(h, x, p)) % p == 0]
        child = [x for x in complete if x in outside]
        if 6 in complete:
            discarded.append(gamma)
            need(not bad(uc, vc, child, 3, p), "uncharged exception loses badness")
            continue
        need(len(child) == m-t == 6 and bad(uc, vc, child, 3, p), "actual m-t child, not m-a")
        hc = divide(h, loc, p)
        need(all((uc[x]+gamma*vc[x]-value(hc, x, p)) % p == 0 for x in child), "original slope retained")
        supports[gamma] = child
        for anchor in child:
            qa = value(q, anchor, p)
            need(qa != 0, "nonzero anchor evaluation")
            ap = scale(q, uc[anchor]*pow(qa, -1, p), p)
            bp = scale(q, vc[anchor]*pow(qa, -1, p), p)
            rest = [x for x in outside if x != anchor]
            au = {x: (uc[x]-value(ap, x, p))*pow((x-anchor) % p, -1, p) % p for x in rest}
            av = {x: (vc[x]-value(bp, x, p))*pow((x-anchor) % p, -1, p) % p for x in rest}
            witness = [x for x in child if x != anchor]
            need(bad(au, av, witness, 2, p), "full-code anchored child")
            need(any(bad(au, av, xs, 2, p) for xs in combinations(witness, 4)),
                 "baseline-gap bad subset from larger actual gap")
    need(discarded == [p-1] and len(supports) == 3, "one charged, three retained")
    need(sum(sum(x in support for support in supports.values()) for x in outside) == 18,
         "actual scalar incidence ledger")
    print("PASS: actual rank-two maximizing flat, singleton fibers, scaled carrier and retained zero")
    print("PASS: 4 original labels, 1 essential exception, 3 full-code-bad m-t children, 18 anchors")


def overlap_and_budget():
    a, delta = 7, 6
    c0, c1 = {0, 1, 2, 3}, {0, 4, 5, 6}
    # On A, the receiver equals 0 on c0 and X on c1; both agree at 0.
    need(len(c0 & c1) == a-delta and len(c0) == len(c1) == a-delta/2, "strict threshold equality")
    need(c0 & c1, "projected cores are not disjoint colors")
    large = {0, 1, 2, 3, 4, 5}
    other = {0, 6}
    need(len(large & other) <= a-delta and len(other) == 2*a-delta-len(large),
         "sharp complement occupancy")
    need(len(other) > a-len(large), "rank-one complement bound would be false")
    budget, light_charge, heavy_charge = 100, 10, 5
    h, light = 8, 6
    need(heavy_charge*h+light_charge*light == budget, "one actual resource")
    need(h+light == F(budget, light_charge)+F(h, 2), "sharp half-credit identity")
    need(h+light > F(budget, light_charge), "dropping heavy remainder fails")
    need(h+light < F(budget, light_charge)+h, "free heavy addition is strictly weaker")
    need(0*20+10*10 <= budget and 20+10 > F(budget, light_charge)+F(20, 2),
         "without the common heavy charge the claimed discount fails")
    print("PASS: overlapping projected cores, strict boundary and necessary shared-charge controls")


if __name__ == "__main__":
    actual_source()
    overlap_and_budget()
    print("Small controls do not certify the universal source and tuple proofs")
