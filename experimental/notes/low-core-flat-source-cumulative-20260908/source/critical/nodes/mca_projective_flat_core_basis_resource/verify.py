"""Small exact arc/basis controls and the two finite source payments."""

from fractions import Fraction as Q
from itertools import combinations, permutations
from math import prod

P = 7


def check(ok, message):
    if not ok:
        raise ValueError(message)


def rank(rows, modulus=P):
    a = [[x % modulus for x in row] for row in rows]
    height = 0
    for column in range(len(a[0])):
        pivot = next((i for i in range(height, len(a)) if a[i][column]), None)
        if pivot is None:
            continue
        a[height], a[pivot] = a[pivot], a[height]
        inv = pow(a[height][column], -1, modulus)
        a[height] = [(x * inv) % modulus for x in a[height]]
        for i in range(len(a)):
            if i != height and a[i][column]:
                v = a[i][column]
                a[i] = [(x - v * y) % modulus for x, y in zip(a[i], a[height])]
        height += 1
    return height


def tuple_set(core, defect, evaluate, modulus=P):
    support = tuple(core) + (defect,)
    normals = {x: (int(x == defect),) + tuple(-v % modulus for v in evaluate(x))
               for x in support}
    return {xs for xs in permutations(support, 4) if rank([normals[x] for x in xs], modulus) == 4}


def normalized(v):
    inv = pow(next(x for x in v if x), -1, P)
    return tuple(x * inv % P for x in v)


def main():
    arc = lambda x: (1, x % P, x * x % P)
    left = tuple_set((0, 1, 2, 3), 4, arc)
    right = tuple_set((0, 1, 2, 3), 5, arc)
    check(len(left) == len(right) == 96 and left.isdisjoint(right), "two slope tuple owners")
    check(96 == 4 * prod((4, 3, 2)), "insertion factor")
    # Actual receiver: u=v=0 on 0..3; (u,v)=(0,1) at 4, (-1,1) at 5.
    check(len(left | right) <= prod((6, 5, 4, 3)), "one global tuple budget")
    check(96 + 32 > len(left), "do not add overlapping within-record lower counts")

    nonarc = lambda x: (1, x % P, pow(x, 3, P))
    failed = tuple_set((0, 1, 2, 6), 3, nonarc)
    check(rank([nonarc(x) for x in (0, 1, 6)]) == 2, "distinct but dependent")
    check(len(failed) == 72 < 96, "rank-two occupancy bound cannot be dropped")
    zeros = lambda x: (x % P, x * x % P, pow(x, 3, P))
    corrected = tuple_set((0, 1, 2, 3), 4, zeros)
    check(len(corrected) == 4 * prod((3, 2, 1)) == 24 < 96, "subtract agreeing carrier zero")
    repeated = lambda x: (1, x * x % P, pow(x, 4, P))
    rep = tuple_set((0, 1, 2, 3, 4), 5, repeated)
    check(len(rep) == 168 >= 4 * prod((5, 3, 1)), "fiber h=2")
    check(len(rep) < 4 * prod((5, 4, 3)), "false singleton fibers")

    weak = lambda x: (1, x, pow(x, 3, 11))
    weak_tuples = tuple_set((0, 1, 10, 2, 3, 4, 5), 6, weak, 11)
    check(rank([weak(x) for x in (0, 1, 10)], 11) == 2, "weaker source is not an arc")
    check(len(weak_tuples) == 792 >= 4 * 7 * 5 * 3, "positive bound from weaker flat hypothesis")
    check(4 * 7 * Q(11, 2) * 4 == 616 <= len(weak_tuples), "real h=3/2 occupancy")

    # rho=(X^2+1)/X includes its infinity fiber at X=0.
    rational = lambda x: (x * x % P, x * (x * x + 1) % P, (x * x + 1)**2 % P)
    fibers = {}
    for x in range(P):
        fibers.setdefault(normalized(rational(x)), []).append(x)
    check(max(map(len, fibers.values())) <= 2, "rational fibers including pole")
    check(normalized(rational(0)) == (0, 0, 1), "infinity retained")
    check(all(rank(list(vs)) == len(vs) for k in (1, 2, 3)
              for vs in combinations(fibers, k)), "homogeneous progression arc")

    c = 23067643444721720934
    b = 2130706433**6 // 2**128
    near = 134944
    for j in (4801, 169999):
        f = Q(prod(1048576 + j - i for i in range(12)),
              (67472 + j) * prod(67472 + i for i in range(1, 11)))
        check(f <= c, "original interval resource endpoints")
    check(c // 5500 + near == 4194116990084347, "all HIGH once")
    check(12 * 500 < 67473, "beta increasing on all LOW margins")
    check(34 * (1048576 + 4801 - 11) - 120 * (169999 + 67472) == 7317924 > 0,
          "all-J variable-height derivative certificate")
    check(11 * (1048576 + 10000 - 11) > 12 * (169999 + 67471),
          "all-J singleton derivative certificate")
    expected = ((10000, Q(1), 273674135808267711, 1306592303127376),
                (23000, Q(22999, 10), 268724670028139326, 6256058083255761))
    for j, h, target, reserve in expected:
        num = prod(1048576 + j - i for i in range(12))
        den = 12 * prod(Q(j + 67471) - i * h for i in range(11))
        total = max(int(num / den), c // 5500) + near
        check(total == target and b - total == reserve > 0, "whole-source row payment")
        vals = [12 * r * prod(Q(j + 67472 - r) - i * h for i in range(11))
                for r in (1, 2, 125, 500)]
        check(vals == sorted(vals), "recordwise product controls")
    print("PASS: slope ownership, necessary flat/zero/fiber bounds, strict weakening and infinity")
    print("PASS: ARC1 source cap 273674135808267711; ARC-H/GP cap 268724670028139326")
    print("Arbitrary carrier coverage remains 4801..9940; no curve cover or prize closure asserted")


if __name__ == "__main__":
    main()
