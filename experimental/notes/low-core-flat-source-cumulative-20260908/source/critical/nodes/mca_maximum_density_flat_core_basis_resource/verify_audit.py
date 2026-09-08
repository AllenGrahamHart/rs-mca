"""Independent Bareiss census and closed-form inside-extension controls."""

from itertools import combinations
from math import comb, factorial, prod


def require(ok, message):
    if not ok:
        raise ValueError(message)


def determinant(matrix):
    a = [list(row) for row in matrix]
    previous, sign = 1, 1
    for k in range(len(a)-1):
        if a[k][k] == 0:
            swap = next((i for i in range(k+1, len(a)) if a[i][k]), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, len(a)):
            for h in range(k+1, len(a)):
                numerator = pivot*a[i][h]-a[i][k]*a[k][h]
                require(numerator % previous == 0, "exact Bareiss division")
                a[i][h] = numerator//previous
            a[i][k] = 0
        previous = pivot
    return sign*a[-1][-1]


def locator(roots, p):
    coeff = [1]
    for r in roots:
        out = [0]*(len(coeff)+1)
        for i, value in enumerate(coeff):
            out[i] = (out[i]-r*value) % p
            out[i+1] = (out[i+1]+value) % p
        coeff = out
    return coeff


def at(coeff, x, p):
    value = 0
    for c in reversed(coeff):
        value = (value*x+c) % p
    return value


def falling(n, r):
    return prod(range(n-r+1, n+1)) if r <= n else 0


def control(p, dimension, K, flat, a, zeros, inside, outside, expected):
    polynomials = [[0]*i+[1] for i in range(flat-1)]
    polynomials += [locator(range(zeros), p)]
    polynomials += [[0]*i+locator(range(a), p) for i in range(dimension-flat)]
    require(len({len(poly) for poly in polynomials}) == dimension, "independent degrees")
    require(max(map(len, polynomials)) <= K, "degree bound")
    points = inside+outside
    vectors = {x: tuple(at(poly, x, p) for poly in polynomials) for x in points}
    classes = [0]*(flat+1)
    for subset in combinations(points, dimension):
        if determinant([vectors[x] for x in subset]) % p:
            classes[sum(x in inside for x in subset)] += factorial(dimension)
    require(classes == expected, "independent ordered class census")

    # Inside evaluations are a complete Vandermonde system of rank flat-1:
    # a smaller independent span contains exactly its chosen points;
    # a full inside span contains every inside point.
    t, c, ell = len(inside), len(points)-K+1, dimension-flat
    E = [falling(t, b) if b < flat else 0 for b in range(flat+1)]
    y = [t-b if b < flat-1 else 0 for b in range(flat+1)]
    require([E[b]*y[b] for b in range(flat)] == E[1:], "closed extension identity")
    prefix = falling(len(outside), ell)
    for b in range(flat):
        k = flat-b
        extension = prod(c+i-y[b] for i in range(k)) if y[b] < c else 0
        require(comb(dimension, b)*prefix*E[b]*extension <= classes[b],
                "inside-cardinality class lower bound")
    lower = prefix*dimension*prod(range(c, c+flat-1))*t
    require(0 < lower <= sum(classes), "positive deficient-rank coupling")
    print("BAREISS", (p, dimension, K, flat), classes, "coupled lower", lower)


def main():
    control(17, 5, 9, 2, 6, 4, tuple(range(4)), tuple(range(6, 13)),
            [2520, 15840, 0])
    control(13, 7, 11, 3, 7, 5, tuple(range(5)), tuple(range(7, 13)),
            [0, 25200, 302400, 0])
    control(17, 9, 12, 4, 7, 6, tuple(range(6)), tuple(range(7, 15)),
            [0, 2177280, 40642560, 203212800, 0])
    require(12*factorial(22)//factorial(11) == 337903056691200, "dimension-eleven uniform count")
    for c in (12, 67467):
        for j in range(1, 5):
            rising = lambda k: prod(range(c, c+k))
            deriv = lambda k: sum(prod(c+i for i in range(k) if i != v) for v in range(k))
            coefficients = [comb(11, b)*rising(j-b)-comb(11, b-1)*deriv(j-b+1)
                            for b in range(2, j+1)]
            require(all(x >= 0 for x in coefficients), "coupling coefficient signs")
    print("PASS: independent exact determinants, polynomial carriers and inside identities")
    print("Controls do not replace the universal counting and maximum-density proof")


if __name__ == "__main__":
    main()
