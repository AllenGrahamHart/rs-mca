"""Tiny exact controls of the mixed-branch identity and actual rank-four bases."""

from fractions import Fraction as Q
from itertools import combinations
from math import factorial

from polynomial import add, at, compose, derivative, mul, scale, sub


def need(ok, message):
    if not ok:
        raise ValueError(message)


def rank(rows, p):
    a = [list(row) for row in rows]
    found = 0
    for column in range(len(a[0])):
        pivot = next((i for i in range(found, len(a)) if a[i][column] % p), None)
        if pivot is None:
            continue
        a[found], a[pivot] = a[pivot], a[found]
        inv = pow(a[found][column] % p, -1, p)
        a[found] = [x*inv % p for x in a[found]]
        for i in range(found+1, len(a)):
            c = a[i][column]
            a[i] = [(x-c*y) % p for x, y in zip(a[i], a[found])]
        found += 1
    return found


def main():
    D, K, r = 10, 6, 4
    t, N = r-2, D+K
    first, second = [Q(2), Q(3), Q(1, 20)], [Q(4), Q(2), Q(1, 30), Q(1, 1000)]
    a, x, y = [K-1, -t], [1, t], [K, -1]
    expression = add(mul(a, compose(first, *x)), mul(sub([N], a), compose(second, *y)))
    left = derivative(derivative(expression))
    right = scale(sub(mul(a, compose(derivative(derivative(first)), *x)),
                      scale(compose(derivative(first), *x), 2)), t*t)
    right = add(right, sub(mul(sub([N], a), compose(derivative(derivative(second)), *y)),
                           scale(compose(derivative(second), *y), 2*t)))
    need(left == right, "mixed-branch second derivative identity")
    F = lambda z: min(2*z, z+1)
    need(F(1) > (F(0)+F(2))/2, "minimum can fail convexity; Jensen not licensed")
    counts = []
    for K in (4, 5, 6):
        D, p, n = 6, 17, 6+K
        for clustered in (False, True):
            rows = []
            for x0 in range(n):
                locator = 1
                for root in range(K-3):
                    locator = locator*(x0-root) % p
                rows.append([1, locator, x0*locator % p, x0*x0*locator % p]
                            if clustered else [pow(x0, j, p) for j in range(4)])
            bases = factorial(4)*sum(rank(points, p) == 4 for points in combinations(rows, 4))
            seed = lambda k: (D+1)*(D+k)*(D+Q(k+1, 2))
            S = (K-3)*seed(3)+(D+3)*seed(K-1)
            U = (D+K)*seed(Q(2*K+1, 3))
            need(bases >= min(S, U), "actual rank-four basis bound")
            counts.append(bases)
    print("PASS mixed-branch identity, nonconvex-minimum control and six actual basis counts", counts)
    print("Universal proof is the concavity argument, not these finite controls")


if __name__ == "__main__":
    main()
