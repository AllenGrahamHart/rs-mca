"""Small actual polynomial contractions and exact ordered-basis recounts."""

from fractions import Fraction as Q
from itertools import combinations
from math import factorial, prod


def check(ok, message):
    if not ok:
        raise ValueError(message)


def evaluate(f, x, p):
    out = 0
    for c in reversed(f):
        out = (out*x+c) % p
    return out


def rank(rows, p):
    a = [list(row) for row in rows]
    if not a:
        return 0
    used = 0
    for column in range(len(a[0])):
        pivot = next((i for i in range(used, len(a)) if a[i][column] % p), None)
        if pivot is None:
            continue
        a[used], a[pivot] = a[pivot], a[used]
        inverse = pow(a[used][column], -1, p)
        a[used] = [x*inverse % p for x in a[used]]
        for i in range(used+1, len(a)):
            factor = a[i][column]
            a[i] = [(x-factor*y) % p for x, y in zip(a[i], a[used])]
        used += 1
        if used == len(a):
            break
    return used


def locator(points, p):
    out = [1]
    for x in points:
        following = [0]*(len(out)+1)
        for i, value in enumerate(out):
            following[i] = (following[i]-x*value) % p
            following[i+1] = (following[i+1]+value) % p
        out = following
    return out


def divide(f, g, p):
    remainder = list(f)
    quotient = [0]*(len(f)-len(g)+1)
    for i in range(len(f)-len(g), -1, -1):
        quotient[i] = remainder[i+len(g)-1] % p
        for j, value in enumerate(g):
            remainder[i+j] = (remainder[i+j]-quotient[i]*value) % p
    check(not any(remainder), "exact locator division")
    return quotient


def rows_for(polys, points, p):
    return [tuple(evaluate(f, x, p) for f in polys) for x in points]


def basis_count(rows, p, r):
    return factorial(r)*sum(rank(subset, p) == r for subset in combinations(rows, r))


def seed(d, k):
    return (d+1)*(d+k)*(d+Q(k+1, 2))


def run_case(p, k, d, points, polys):
    r = len(polys)
    check(len(points) == d+k and len(set(points)) == len(points), "actual row")
    rows = rows_for(polys, points, p)
    check(rank(rows, p) == r and all(any(row) for row in rows), "actual rank/nonzero")
    fibers = {}
    for x, row in zip(points, rows):
        inverse = pow(next(v for v in row if v), -1, p)
        key = tuple(v*inverse % p for v in row)
        fibers.setdefault(key, []).append(x)
    before, after, warnings = basis_count(rows, p, r), 0, 0
    for key, fiber in fibers.items():
        x = fiber[0]
        pivot = next(i for i, v in enumerate(key) if v)
        pivot_value = evaluate(polys[pivot], x, p)
        ann = []
        for i, f in enumerate(polys):
            if i == pivot:
                continue
            scalar = evaluate(f, x, p)*pow(pivot_value, -1, p) % p
            ann.append([(f[j]-scalar*polys[pivot][j]) % p for j in range(k)])
        g = locator(fiber, p)
        child = [divide(f, g, p) for f in ann]
        outside = [x for x in points if x not in fiber]
        child_rows = rows_for(child, outside, p)
        check(all(len(f) == k-len(fiber) for f in child), "actual quotient degree")
        check(rank(child_rows, p) == r-1, "actual quotient rank")
        check(all(any(row) for row in child_rows), "no remaining zero evaluation")
        check(len(outside)-(k-len(fiber)) == d, "gap preserved")
        after += len(fiber)*basis_count(child_rows, p, r-1)
        if len(fiber) > 1:
            check(all(evaluate(f, fiber[1], p) == 0 for f in ann), "whole fiber vanishes")
            wrong = [divide(f, locator([fiber[0]], p), p) for f in ann]
            check(not any(evaluate(f, fiber[1], p) for f in wrong), "single-point contraction leaves zero")
            warnings += 1
    check(before == after, "exact fiber contraction identity")
    if r == 3:
        check(before >= seed(d, k), "rank-three seed")
    elif r == 4:
        spike = (k-3)*seed(d, 3)+(d+3)*seed(d, k-1)
        equal = (d+k)*seed(d, Q(2*k+1, 3))
        check(before >= min(spike, equal), "rank-four quadratic step")
    print("ACTUAL", (p, k, d, r), "fibers", sorted(map(len, fibers.values())),
          "bases", before, "single-point warnings", warnings)
    return before


def main():
    monomials = lambda k, powers: [tuple(int(i == j) for i in range(k)) for j in powers]
    check(run_case(11, 3, 4, list(range(7)), monomials(3, range(3))) == 210, "MDS seed equality")
    check(run_case(17, 4, 5, list(range(9)), monomials(4, range(4))) == 3024, "MDS step equality")
    g = locator((0, 1, 2), 19)
    polys = [[1]+[0]*5] + [([0]*i+g+[0]*(2-i)) for i in range(3)]
    run_case(19, 6, 7, list(range(13)), polys)
    points = [x % 23 for x in range(-8, 9) if x]
    check(run_case(23, 7, 9, points, monomials(7, (0, 2, 4, 6))) == 26880,
          "equal-fiber step equality")
    print("PASS: four actual carriers, full locator quotients and exact contraction counts")
    for j, expected in ((10000, 475414689222665798), (25000, 291592148613630038)):
        outside, a = 67481, j-10
        upper = prod(outside-i for i in range(10))*(67471+11*a)
        quotient = prod(1048576+j-i for i in range(12))//(12*upper)+134944
        check(quotient == expected > 2130706433**6//2**128, "uniform-charge method boundary")
    print("PASS: two coarse-resource method boundaries, not unsafe rows")
    print("Small controls do not certify the universal contraction/concavity theorem")


if __name__ == "__main__":
    main()
