"""Tiny actual-source controls for receiver colors, exceptions and locator transport."""

from fractions import Fraction as F
from itertools import combinations
from math import factorial


def require(ok, message):
    if not ok:
        raise ValueError(message)


def rank(rows, p):
    a = [list(row) for row in rows]
    if not a:
        return 0
    used = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(used, len(a)) if a[i][col] % p), None)
        if pivot is None:
            continue
        a[used], a[pivot] = a[pivot], a[used]
        inv = pow(a[used][col] % p, -1, p)
        a[used] = [x*inv % p for x in a[used]]
        for i in range(used+1, len(a)):
            factor = a[i][col]
            a[i] = [(x-factor*y) % p for x, y in zip(a[i], a[used])]
        used += 1
        if used == len(a):
            break
    return used


def add(a, b, p):
    return [((a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)) % p
            for i in range(max(len(a), len(b)))]


def scale(a, c, p):
    return [c*x % p for x in a]


def mul(a, b, p):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j]+x*y) % p
    return out


def value(a, x, p):
    return sum(c*pow(x, i, p) for i, c in enumerate(a)) % p


def locator(points, p):
    out = [1]
    for x in points:
        out = mul(out, [-x, 1], p)
    return out


def divide(a, b, p):
    work = a[:]
    out = [0]*max(1, len(a)-len(b)+1)
    for i in range(len(a)-len(b), -1, -1):
        out[i] = work[i+len(b)-1] % p
        for j, c in enumerate(b):
            work[i+j] = (work[i+j]-out[i]*c) % p
    require(not any(work), "full locator division")
    return out


def fits(word, points, k, p):
    rows = [[pow(x, j, p) for j in range(k)] for x in points]
    return rank(rows, p) == rank([row+[word[x]] for row, x in zip(rows, points)], p)


def bad(u, v, points, k, p):
    return not (fits(u, points, k, p) and fits(v, points, k, p))


def run_case(multiple):
    if multiple:
        p, k, m, points, fiber = 23, 7, 9, list(range(19))+[22], list(range(4))
        q, hstar = [-22, 1], [0, 0, 1]
        core0, core1 = [0, 1]+list(range(4, 10)), [2, 3]+list(range(10, 16))
        base = {x: (0, 0) for x in points}
        base.update({x: (1, 1) for x in core1})
        base.update({16: (-1, 1), 17: (3, 0), 18: (4, 0)})
        records = ((p-1, 0, 0, 2), (1, 0, 0, 16), (2, 1, 1, 17), (3, 1, 1, 18))
        theta, expected_heavy = F(1, 3), 2
    else:
        p, k, m, points, fiber = 17, 5, 7, list(range(11)), list(range(3))
        q, hstar = [1], [0]
        core0 = [0, 1]+list(range(3, 8))
        base = {x: (0, 0) for x in points}
        base.update({2: (1, 1), 8: (-1, 1), 9: (-2, 1), 10: (-3, 1)})
        records = ((p-1, 0, 0, 2), (1, 0, 0, 8), (2, 0, 0, 9), (3, 0, 0, 10))
        theta, expected_heavy = F(1, 2), 1
    loc = locator(fiber, p)
    direction = mul(mul(q, loc, p), [0, 1], p)
    carrier = [q, mul(q, loc, p), direction]
    require(rank([f+[0]*(k-len(f)) for f in carrier], p) == 3, "actual carrier rank")
    require(all(len(f) <= k for f in carrier), "actual polynomial degree")
    u = {x: (value(hstar, x, p)+value(q, x, p)*base[x][0]) % p for x in points}
    v = {x: (value(direction, x, p)+value(q, x, p)*base[x][1]) % p for x in points}
    if multiple:
        u[22] = (value(hstar, 22, p)+1) % p
    ev = {x: tuple(value(f, x, p) for f in carrier) for x in points}
    require(not any(not any(ev[x]) and v[x] == 0 and u[x] == value(hstar, x, p)
                    for x in points), "empty universal core")
    actual_fiber = [x for x in points if ev[x][0] and ev[x][1:] == (0, 0)]
    require(actual_fiber == fiber, "complete nonzero evaluation fiber")
    colors = {}
    for x in fiber:
        inverse = pow(value(q, x, p), -1, p)
        color = ((u[x]-value(hstar, x, p))*inverse % p, v[x]*inverse % p)
        colors.setdefault(color, []).append(x)
    heavy = {c for c, xs in colors.items() if len(xs) > theta*len(fiber)}
    require(len(heavy) == expected_heavy, "strict heavy class count")
    require(len(heavy) < 1/theta, "bounded actual class multiplicity")
    if multiple:
        require(not any(len(xs) > F(len(fiber), 2) for xs in colors.values()), "strict half boundary")
        require(len({((u[x]-value(hstar, x, p)) % p, v[x]) for x in fiber})
                > len(colors), "unscaled receiver values lose a class")
    outside = [x for x in points if x not in fiber]
    child_space = [divide(f, loc, p) for f in carrier[1:]]
    require(rank([f+[0]*(k-len(fiber)-len(f)) for f in child_space], p) == 2,
            "annihilator quotient has actual dimension two")
    if multiple:
        require(22 in outside and not any(value(f, 22, p) for f in child_space),
                "nonuniversal zero retained in the child")
    seen_tuples, children_by_color, charged, survivors = set(), {}, 0, 0
    for gamma, alpha, beta, defect in records:
        h = add(add(hstar, scale(q, alpha+gamma*beta, p), p), scale(direction, gamma, p), p)
        b = add(scale(q, beta, p), direction, p)
        ap = add(hstar, scale(q, alpha, p), p)
        core = [x for x in points if u[x] == value(ap, x, p) and v[x] == value(b, x, p)]
        require(core == (core1 if beta else core0), "complete pair core, not only selected support")
        require([x for x in fiber if x in core] == colors[(alpha, beta)], "complete core color")
        support = core[:m-1]+[defect]
        require(len(set(support)) == m and all((u[x]+gamma*v[x]-value(h, x, p)) % p == 0
                                             for x in support), "original scalar support")
        require(sum(v[x] != value(b, x, p) for x in support) == 1, "raw one")
        require(bad(u, v, support, k, p), "full-code original badness, hence minimizing pair")
        basis = factorial(3)*sum(rank([ev[x] for x in xs], p) == 3
                                 for xs in combinations(support[:-1], 3))
        t, size_a, size_h = sum(x in fiber for x in support[:-1]), len(fiber), m-1
        e, c = k-size_a-2, size_h-k+1
        lower = (size_h-t)*(size_h-t-e-1)*(3*t+max(c-t, 0))
        require(basis >= lower, "actual core basis lower bound")
        tuples = {xs for xs in combinations(sorted(support), 4)
                  if rank([(v[x], *ev[x]) for x in xs], p) == 4}
        require(factorial(4)*len(tuples) == 4*basis, "exact core/one-defect tuple count")
        require(not seen_tuples.intersection(tuples), "original distinct-slope tuple ownership")
        seen_tuples.update(tuples)
        ug = {x: (u[x]-value(hstar, x, p)-alpha*value(q, x, p)) % p for x in points}
        vg = {x: (v[x]-beta*value(q, x, p)) % p for x in points}
        agreement = [x for x in points if (u[x]+gamma*v[x]-value(h, x, p)) % p == 0]
        exceptional = any((ug[x]+gamma*vg[x]) % p == 0
                          for x in fiber if x not in colors[(alpha, beta)])
        uc = {x: ug[x]*pow(value(loc, x, p), -1, p) % p for x in outside}
        vc = {x: vg[x]*pow(value(loc, x, p), -1, p) % p for x in outside}
        hc = divide(scale(direction, gamma, p), loc, p)
        row = tuple((x, uc[x], vc[x]) for x in outside)
        require(children_by_color.setdefault((alpha, beta), row) == row, "one fixed child per color")
        child_agreement = [x for x in agreement if x in outside]
        require(all((uc[x]+gamma*vc[x]-value(hc, x, p)) % p == 0 for x in child_agreement),
                "same finite label after polynomial quotient")
        if exceptional:
            charged += 1
            if not multiple:
                require(not bad(uc, vc, child_agreement, k-size_a, p),
                        "dropping exception charge would lose actual badness")
            continue
        survivors += 1
        require([x for x in agreement if x in fiber] == colors[(alpha, beta)], "exact removed agreements")
        require(bad(uc, vc, child_agreement, k-size_a, p), "full-code child badness")
        witness = next((xs for xs in combinations(child_agreement, m-size_a)
                        if bad(uc, vc, xs, k-size_a, p)), None)
        require(witness is not None, "exact smaller bad subset")
    require(charged == 1 and survivors == 3, "original label accounting")
    print("PASS", "two-color/scaled/zero" if multiple else "essential exception",
          "source; 4 labels, 3 retained, 1 explicitly charged")


if __name__ == "__main__":
    run_case(False)
    run_case(True)
    print("Tiny actual-source controls, not certification of the universal hand proof")
