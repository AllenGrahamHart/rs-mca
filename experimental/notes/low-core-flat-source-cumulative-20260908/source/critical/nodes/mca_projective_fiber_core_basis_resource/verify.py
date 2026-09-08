"""Small exact core/fiber controls and the finite source envelope."""

from fractions import Fraction as Q
from itertools import permutations
from math import prod


def require(ok, message):
    if not ok:
        raise ValueError(message)


def rank(rows, p=13):
    rows = [[x % p for x in row] for row in rows]
    height = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(height, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[pivot], rows[height] = rows[height], rows[pivot]
        inv = pow(rows[height][col], -1, p)
        rows[height] = [x * inv % p for x in rows[height]]
        for i in range(len(rows)):
            if i != height:
                v = rows[i][col]
                rows[i] = [(x - v * y) % p for x, y in zip(rows[i], rows[height])]
        height += 1
    return height


def outside_count(x, k, s, a):
    e = k - a - s + 1
    return x * prod(x - e - i for i in range(1, s - 1))


def core_min(m, k, s, a):
    c = m - k + 1
    f = lambda t: outside_count(m - t, k, s, a) * (s * t + max(c - t, 0))
    points = (0, a, c) if c <= a else (0, a)
    return min(f(t) for t in points)


def tuple_set(core, defect, evaluate):
    support = tuple(core) + (defect,)
    normals = {x: (int(x == defect),) + tuple(-v for v in evaluate(x)) for x in support}
    return {xs for xs in permutations(support, 4) if rank([normals[x] for x in xs]) == 4}


def main():
    g = lambda x: x * (x - 1) * (x - 2)
    evaluate = lambda x: (1, g(x), x * g(x))
    core = (0, 1, 2, 3, 4, 5)
    left, right = (tuple_set(core, y, evaluate) for y in (6, 7))
    require(len(left) == len(right) == 240 and left.isdisjoint(right), "distinct slope owners")
    require(core_min(6, 5, 3, 3) == 54 and 4 * 54 <= len(left), "saturated fiber")
    require(len(core) >= 5, "actual full-code badness root threshold")
    require(len(left | right) <= prod((8, 7, 6, 5)), "one original tuple budget")

    g2 = lambda x: x * (x - 1)
    partial = lambda x: (1, g2(x), x * x * g2(x))
    core2 = (0, 2, 3, 4, 9, 10)
    actual = tuple_set(core2, 6, partial)
    require(len(actual) == 432 >= 4 * core_min(6, 5, 3, 2), "nonsaturated fiber")
    outside = (2, 3, 4, 9, 10)
    count = sum(rank([(1, x*x), (1, y*y)]) == 2 for x, y in permutations(outside, 2))
    require(count == 16 >= outside_count(5, 5, 3, 2), "remaining degree excess")
    require(count < 5 * 4, "false free independence without degree excess")

    scaled = lambda x: tuple((x - 12) * v for v in evaluate(x))
    zero_defect = tuple_set(core, 12, scaled)
    require(len(zero_defect) == 240, "nonuniversal carrier-zero defect retained")
    require(len(core) >= 6, "scaled actual degree-K badness threshold")
    bad_core = (0, 1, 2, 3, 4, 12)
    false_zero = tuple_set(bad_core, 6, scaled)
    require(len(false_zero) == 72 < 4 * core_min(6, 6, 3, 3), "g=0 cannot be omitted")

    checked = 0
    for k in range(3, 11):
        for s in range(2, min(k, 5) + 1):
            for a in range(1, k - s + 2):
                for m in range(k, k + 5):
                    lower = core_min(m, k, s, a)
                    for t in range(a + 1):
                        actual_bound = outside_count(m-t, k, s, a) * (s*t+max(m-k+1-t, 0))
                        require(actual_bound >= lower > 0, "three-endpoint minimum")
                    checked += 1

    d, r, near, c = 67466, 1048576, 134944, 23067643444721720934
    p = prod(d + i for i in range(1, 10))
    expected = {
        65000: (34003655554524123, 266514954058742090, 216764665972142342, 216763564029644353),
        169999: (1252453225033902, 220398387206020840, 244346006891976872, 244365664452173214),
    }
    for j, targets in expected.items():
        u = prod(r + j - i for i in range(12))
        envelopes = (Q((j+d)*(d+1))*Q(2*d+j+2, 2)**9,
                     Q(p*(2*d+j)*(d+1+5*j), 2),
                     11*(j-10)*(d+10)*p, 11*(d+1)*(j-1)*p)
        totals = tuple(int(Q(u, 12)/b) + near for b in envelopes)
        require(totals == targets, "finite endpoint floors")
        for a in ((j+1)//2, j-10):
            require(core_min(j+d, j, 11, a) >= min(envelopes), "fiber-size envelope")
    l0, h0 = r+65000-11, 169999+2*d
    require(9*l0 > 12*(h0+2), "Q0 decreases on full interval")
    require(l0*l0 > 12*h0*h0, "Q1..Q3 log-convex on full interval")
    require(12*84 < 67473, "all HIGH weight monotonicity")
    require(84*Q(67473-77, 67473) > Q(10488, 125), "HIGH Bernoulli floor")
    total = 125*c//10488 + near
    require(total == 274929007493481160, "one HIGH quotient")
    require(2130706433**6//2**128-total == 51720617913927, "positive source reserve")
    require(max(max(row) for row in expected.values()) < total, "whole source combines by maximum")
    print("PASS: original tuples, fiber degree excess, carrier-zero guard;", checked, "endpoint controls")
    print("PASS: large-fiber source 65000..169999 <=", total, "; exact reserve 51720617913927")
    print("Universal geometry and interval extension are hand proofs; arbitrary carrier coverage unchanged")


if __name__ == "__main__":
    main()
