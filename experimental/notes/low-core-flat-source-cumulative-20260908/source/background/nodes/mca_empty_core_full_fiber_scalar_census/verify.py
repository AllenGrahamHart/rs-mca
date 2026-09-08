"""Tiny actual-source and rational profile controls, not a universal proof."""

from fractions import Fraction as F
import importlib.util
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT / "critical/nodes/mca_receiver_fiber_peeling/verify.py"
spec = importlib.util.spec_from_file_location("fiber_controls", HELPER)
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)
need = h.require


def source(scaled):
    if scaled:
        p, k, m, points, aa = 23, 7, 9, list(range(19))+[22], list(range(4))
        f, hstar = [-22, 1], [0, 0, 1]
        core0 = [0, 1]+list(range(4, 10))
        core1 = [2, 3]+list(range(10, 16))
        base = {x: (0, 0) for x in points}
        base.update({x: (1, 1) for x in core1})
        base.update({16: (-1, 1), 17: (3, 0), 18: (4, 0)})
        records = ((p-1, 0, 0, 2), (1, 0, 0, 16),
                   (2, 1, 1, 17), (3, 1, 1, 22))
    else:
        p, k, m, points, aa = 17, 5, 7, list(range(11)), list(range(3))
        f, hstar = [1], [0]
        core0, core1 = [0, 1]+list(range(3, 8)), []
        base = {x: (0, 0) for x in points}
        base.update({2: (1, 1), 8: (-1, 1), 9: (-2, 1), 10: (-3, 1)})
        records = ((p-1, 0, 0, 2), (1, 0, 0, 8),
                   (2, 0, 0, 9), (3, 0, 0, 10))
    loc = h.locator(aa, p)
    direction = h.mul(h.mul(f, loc, p), [0, 1], p)
    carrier = [f, h.mul(f, loc, p), direction]
    u = {x: (h.value(hstar, x, p)+h.value(f, x, p)*base[x][0]) % p for x in points}
    v = {x: (h.value(direction, x, p)+h.value(f, x, p)*base[x][1]) % p for x in points}
    if scaled:
        u[22], v[22] = (h.value(hstar, 22, p)-3) % p, 1
    ev = {x: tuple(h.value(g, x, p) for g in carrier) for x in points}
    need(h.rank(list(ev.values()), p) == 3, "actual carrier dimension")
    zeros = [x for x in points if not any(ev[x])]
    need(all((u[x]-h.value(hstar, x, p)) % p or v[x] for x in zeros), "empty core")
    families, pairs, supports = {}, {}, {}
    for gamma, alpha, beta, defect in records:
        ap = h.add(hstar, h.scale(f, alpha, p), p)
        bp = h.add(direction, h.scale(f, beta, p), p)
        hg = h.add(ap, h.scale(bp, gamma, p), p)
        support = (core1 if beta else core0)[:m-1]+[defect]
        need(len(set(support)) == m, "original exact support")
        need(all((u[x]+gamma*v[x]-h.value(hg, x, p)) % p == 0 for x in support), "scalar agreement")
        need(h.bad(u, v, support, k, p), "full-code bad witness")
        need(sum(v[x] != h.value(bp, x, p) for x in support) == 1, "raw-one minimizing pair")
        families[gamma], pairs[gamma], supports[gamma] = hg, (ap, bp), support
    fibers = {}
    for x in points:
        if x in zeros:
            continue
        pivot = next(i for i, a in enumerate(ev[x]) if a)
        key = tuple(a*pow(ev[x][pivot], -1, p) % p for a in ev[x])
        fibers.setdefault(key, []).append(x)
    need(any(xs == aa for xs in fibers.values()), "complete repeated fiber")
    total, enlarged, essential, children, charged = 0, 0, 0, 0, 0
    for key, xs in fibers.items():
        a, x0 = len(xs), xs[0]
        pivot = next(i for i, c in enumerate(key) if c)
        ff = carrier[pivot]
        locator = h.locator(xs, p)
        outside = [x for x in points if x not in xs]
        ws = [h.divide(h.add(g, h.scale(ff, -key[i], p), p), locator, p)
              for i, g in enumerate(carrier) if i != pivot]
        need(h.rank([[h.value(g, x, p) for g in ws] for x in outside], p) == 2,
             "actual quotient rank")
        colors = {}
        for x in xs:
            inv = pow(h.value(ff, x, p), -1, p)
            color = ((u[x]-h.value(hstar, x, p))*inv % p, v[x]*inv % p)
            colors.setdefault(color, []).append(x)
        for (alpha, beta), cc in colors.items():
            labels = [gamma for gamma, hg in families.items()
                      if (h.value(hg, x0, p)-h.value(hstar, x0, p))*pow(h.value(ff, x0, p), -1, p) % p
                      == (alpha+gamma*beta) % p]
            ug = {x: (u[x]-h.value(hstar, x, p)-alpha*h.value(ff, x, p)) % p for x in points}
            vg = {x: (v[x]-beta*h.value(ff, x, p)) % p for x in points}
            uc = {x: ug[x]*pow(h.value(locator, x, p), -1, p) % p for x in outside}
            vc = {x: vg[x]*pow(h.value(locator, x, p), -1, p) % p for x in outside}
            exceptions = [g for g in labels if any((ug[x]+g*vg[x]) % p == 0 for x in xs if x not in cc)]
            need(len(exceptions) <= a-len(cc), "explicit exceptional labels")
            need(all(uc[x] or vc[x] for x in outside if not any(h.value(g, x, p) for g in ws)),
                 "child empty universal core, including nonuniversal zeros")
            for gamma in labels:
                hg = families[gamma]
                agreement = [x for x in points if (u[x]+gamma*v[x]-h.value(hg, x, p)) % p == 0]
                remaining = [x for x in agreement if x in outside]
                quotient = h.divide(h.add(h.add(hg, h.scale(hstar, -1, p), p),
                                               h.scale(ff, -(alpha+gamma*beta), p), p), locator, p)
                need(all((uc[x]+gamma*vc[x]-h.value(quotient, x, p)) % p == 0 for x in remaining),
                     "same original scalar label")
                if gamma in exceptions:
                    essential += not h.bad(uc, vc, remaining, k-a, p)
                    continue
                children += 1
                need([x for x in agreement if x in xs] == cc, "complete removed set")
                need(h.bad(uc, vc, remaining, k-a, p), "full child badness")
                need(any(h.bad(uc, vc, witness, k-a, p)
                         for witness in combinations(remaining, m-a)), "exact bad subset")
            incidence = sum(sum(x in cc for x in ss) for ss in supports.values())
            need(incidence <= len(cc)*len(labels), "scalar-incidence coverage")
            total += incidence
            charged += len(cc)*len(exceptions)
            for gamma in labels:
                ap, bp = pairs[gamma]
                if a > 1 and any(x in cc for x in supports[gamma]):
                    enlarged += any(h.value(ap, x, p) != u[x] or h.value(bp, x, p) != v[x] for x in cc)
    zero_incidences = sum(sum(x in zeros for x in ss) for ss in supports.values())
    need(total+zero_incidences == m*len(families), "one original incidence ledger")
    need(zero_incidences <= len(zeros), "zero-coordinate charge")
    need(enlarged > 0, "restricting to minimizing-pair groups misses incidences")
    if not scaled:
        need(essential > 0, "first source witnesses loss of badness without exceptions")
    need(zero_incidences == int(scaled), "retained agreeing carrier-zero control")
    print("PASS source", p, "children", children, "weighted exceptions", charged,
          "beyond pair groups", enlarged, "essential exceptions", essential,
          "zero incidences", zero_incidences)


def partitions(total, largest):
    if not total:
        yield ()
        return
    for first in range(min(total, largest), 0, -1):
        for rest in partitions(total-first, first):
            yield (first,)+rest


def profiles():
    checked, wrong_minimum = 0, 0
    def f(k):
        return 1+F(100, 7+k)+F(50, (7+k)**2)
    for k in range(2, 10):
        n = k+4
        for s in range(2, min(k, 5)+1):
            w, b = k-s+1, F(k-1, s-1)
            spike = w*f(s-1)+(n-w)*f(k-1)+w*(w-1)
            balanced = n*(f(k-b)+b-1)
            for sizes in partitions(n, w):
                if len(sizes) < s or sum(sizes[:s-1]) > k-1:
                    continue
                value = sum(a*(f(k-a)+a-1) for a in sizes)
                need(value <= max(spike, balanced), "joint partition upper profiles")
                wrong_minimum += value > min(spike, balanced)
                checked += 1
    need(checked > 100 and wrong_minimum > 0, "nonvacuous profile controls")
    print("PASS", checked, "exact partitions;", wrong_minimum, "wrong-minimum controls")


if __name__ == "__main__":
    source(False)
    source(True)
    profiles()
    print("Controls only; uniform cap and convexity inputs are not supplied by a numerical iteration")
