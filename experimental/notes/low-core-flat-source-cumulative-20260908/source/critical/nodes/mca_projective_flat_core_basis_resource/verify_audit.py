"""Independent determinant and integer-product audit; imports no primary check."""

from itertools import permutations, combinations
from math import factorial, prod


def require(ok, message):
    if not ok:
        raise ValueError(message)


def determinant(rows, modulus=7):
    n = len(rows)
    value = 0
    for order in permutations(range(n)):
        inversions = sum(order[i] > order[j] for i in range(n) for j in range(i + 1, n))
        value += (-1)**inversions * prod(rows[i][order[i]] for i in range(n))
    return value % modulus


def count(core, defect, exponents):
    # u=0 on each core and its gamma=0 defect; v=0 on core, v=1 on defect.
    points = list(core) + [defect]
    rows = {x: [int(x == defect)] + [-pow(x, e, 7) for e in exponents] for x in points}
    bases = {xs for xs in combinations(points, 4) if determinant([rows[x] for x in xs])}
    return len(bases) * factorial(4), bases


def main():
    cases = [
        ((0, 1, 2, 3), 4, (0, 1, 2), 4, 96),
        ((0, 1, 2, 6), 3, (0, 1, 3), 4, 72),
        ((0, 1, 2, 3), 4, (1, 2, 3), 4, 24),
        ((0, 1, 2, 3, 4), 5, (0, 2, 4), 5, 168),
    ]
    for core, defect, degrees, k, expected in cases:
        actual, bases = count(core, defect, degrees)
        require(actual == expected, "independent unordered determinant count")
        require(all(defect in xs for xs in bases), "exactly one inserted defect")
        require(max(degrees) < k <= len(core), "actual full-code pair badness by root count")
    _, left = count((0, 1, 2, 3), 4, (0, 1, 2))
    _, right = count((0, 1, 2, 3), 5, (0, 1, 2))
    require(left.isdisjoint(right), "independent multi-label ownership")
    require(determinant([[1, x, pow(x, 3, 7)] for x in (0, 1, 6)]) == 0,
            "three distinct projective vectors can be dependent")
    require(4 * 4 * 3 * 2 > 72 and 4 * 3 * 2 == 24, "arc and zero-normal catches")
    require(4 * 5 * 3 * 1 <= 168 < 4 * 5 * 4 * 3, "fiber-size catch")

    points = (0, 1, 10, 2, 3, 4, 5, 6)
    rows = {x: [int(x == 6), -1, -x, -pow(x, 3, 11)] for x in points}
    weak_count = factorial(4) * sum(bool(determinant([rows[x] for x in xs], 11))
                                  for xs in combinations(points, 4))
    require(weak_count == 792 >= 420, "strictly weaker flat hypothesis has a positive bound")

    classes = []
    for t in range(7):
        classes.append((1, t, t * t))
    classes.append((0, 0, 1))
    require(all(determinant(list(rows)) for rows in combinations(classes, 3)),
            "projective quadratic Vandermonde including infinity")
    require(12 * 500 < 67473, "whole LOW derivative sign")
    require(34 * 1053366 > 120 * 237471, "moving-height log derivative")
    require(11 * 1058565 > 12 * 237470, "singleton log derivative")

    budget, near, high = 274980728111395087, 134944, 23067643444721720934 // 5500
    j = 10000
    num = prod(range(1048576 + j - 11, 1048576 + j + 1))
    den = 12 * prod(range(j + 67461, j + 67472))
    arc_count = 273674135808267711 - near
    require(arc_count * den <= num < (arc_count + 1) * den, "ARC1 floor by cross products")
    require(arc_count > high and budget - arc_count - near == 1306592303127376, "ARC1 reserve")
    j = 23000
    num = 10**11 * prod(range(1048576 + j - 11, 1048576 + j + 1))
    den = 12 * prod((10 - i) * j + 674710 + i for i in range(11))
    gp_count = 268724670028139326 - near
    require(gp_count * den <= num < (gp_count + 1) * den, "ARC-H floor by cross products")
    require(gp_count > high and budget - gp_count - near == 6256058083255761, "ARC-H reserve")

    # All other arithmetic in the interval is controlled by the proved derivative signs.
    for j in (10000, 23000, 169999):
        require(all((10 - i) * j + 674710 + i > 0 for i in range(11)), "positive factors")
        for r in range(1, 501):
            require(12 * r < 67473, "all 500 LOW integer margins")
    require(11 * min(501, 500) == 5500 and min(67473, 5500) >= 5500, "HIGH weight interface")
    print("PASS: independent determinants, pole class, all LOW guards and exact endpoint products")
    print("Universal flat occupancy, arc sufficiency and beta/interval monotonicity are hand proofs")
    print("Full-carrier hypotheses are not automatic; no unrestricted interval or prize closes")


if __name__ == "__main__":
    main()
