"""Tiny exact fiber/envelope controls; the general inequality is hand-proved."""

from fractions import Fraction as F


def branches(r, d, k, s):
    n, m, h = r + k, d + k, k - s + 2
    return (F(n * (2 * n - h), m * (2 * m - h)),
            F(r + s - 1, d + s - 1)
            + F((r + s - 1) * (r - d), m * (m - 1)))


def partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    for first in range(min(n, maximum or n), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def projective(row, p):
    pivot = next(value for value in row if value)
    return tuple(value * pow(pivot, -1, p) % p for value in row)


def main():
    fiber_checks = 0
    p, domain, k, s = 13, list(range(1, 13)), 5, 3
    for shape in ('square', 'spike'):
        rows = {}
        for x in domain:
            if shape == 'square':
                row = (1, x*x % p, x**4 % p)
            else:
                value = (x-1)*(x-2)*(x-3) % p
                row = (1, value, x*value % p)
            rows[x] = row
        fibers = {}
        for x in domain:
            fibers.setdefault(projective(rows[x], p), []).append(x)
        weights = sorted((len(fiber) for fiber in fibers.values()), reverse=True)
        assert weights[0] <= k-s+1 and weights[0]+weights[1] <= k-s+2
        assert weights == ([2]*6 if shape == 'square' else [3]+[1]*9)
        for x in domain:
            row = rows[x]
            j = next(i for i, value in enumerate(row) if value)
            child_zeros = []
            for y in domain:
                if y == x:
                    continue
                values = [(rows[y][i] - row[i]*pow(row[j], -1, p)*rows[y][j])
                          * pow((y-x) % p, -1, p) % p for i in range(s) if i != j]
                if not any(values):
                    child_zeros.append(y)
            assert child_zeros == [y for y in fibers[projective(row, p)] if y != x]
            fiber_checks += 1
    controls = 0
    for n in range(4, 13):
        for weights in partitions(n):
            if len(weights) < 2:
                continue
            for k in range(3, n):
                for s in range(3, k+1):
                    if weights[0]+weights[1] > k-s+2:
                        continue
                    for m in range(k+1, n+1):
                        actual = sum(F(w*(n-w), m-w) for w in weights)
                        assert actual <= m*max(branches(n-k, m-k, k, s))
                        controls += 1
    # Independent worst fibers violate the polynomial common-kernel constraint.
    assert sum(F(w*(20-w), 11-w) for w in (8, 8, 4)) == F(512, 7)
    assert F(512, 7) > 11*max(branches(10, 1, 10, 3)) == F(274, 5)
    # Keeping only the spike endpoint would fail even for a valid size profile.
    balanced, spike = branches(15, 1, 5, 3)
    assert 6*balanced == 90 > 6*spike == F(408, 5)
    comparisons = 0
    for r in range(1, 9):
        for d in range(1, r+1):
            for k in range(3, 9):
                for s in range(3, k+1):
                    for z in range(k-s+1):
                        for g in range(z+1):
                            if d+z-g > r:
                                continue
                            actual = branches(r, d+z-g, k-z, s)
                            base = branches(r, d, k-g, s)
                            assert all(a <= b for a, b in zip(actual, base))
                            comparisons += 1
    print(f'PASS: {fiber_checks} actual projective-fiber child zero sets; '
          f'{controls} partition envelopes; {comparisons} normalized-row comparisons; '
          'independent-fiber and missing-balanced-branch mutations rejected')


if __name__ == '__main__':
    main()
