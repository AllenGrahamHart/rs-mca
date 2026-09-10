"""Small exact matrix pencils; sampling never substitutes for symbolic rank."""

from itertools import combinations, permutations
from random import Random


def need(ok, message):
    if not ok:
        raise ValueError(message)


def reduce(rows, width, p):
    a, pivots = [[x % p for x in row] for row in rows], []
    for col in range(width):
        r = len(pivots)
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][col], -1, p)
        a[r] = [x*inv % p for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][col]:
                factor = a[i][col]
                a[i] = [(x-factor*y) % p for x, y in zip(a[i], a[r])]
        pivots.append(col)
    return a[:len(pivots)], pivots


def normal(w, s, p):
    for degree in range(s):
        rows, width = [], s*(degree+1)
        for pair in w:
            for k in range(degree+2):
                row = [0]*width
                if k <= degree:
                    row[k*s:(k+1)*s] = pair[:s]
                if k:
                    row[(k-1)*s:k*s] = pair[s:]
                rows.append(row)
        a, pivots = reduce(rows, width, p)
        free = next((i for i in range(width) if i not in pivots), None)
        if free is not None:
            vector = [0]*width
            vector[free] = 1
            for row, pivot in zip(a, pivots):
                vector[pivot] = -row[free] % p
            coefficients = [vector[i*s:(i+1)*s] for i in range(degree+1)]
            need(len(reduce(coefficients, s, p)[1]) == degree+1, "minimal coefficients independent")
            need(degree+2 <= 2*s-len(w), "annihilator degree bound")
            need(all(sum(x*y for x, y in zip(row, vector)) % p == 0 for row in rows), "formal identity")
            return degree
    return None


def symbolic_full(w, s, p):
    for cols in combinations(range(len(w)), s):
        determinant = [0]*(s+1)
        for perm in permutations(range(s)):
            sign = (-1)**sum(perm[i] > perm[j] for i in range(s) for j in range(i+1, s))
            poly = [sign]
            for i, j in enumerate(perm):
                a, b = w[cols[j]][i], w[cols[j]][s+i]
                out = [0]*(len(poly)+1)
                for k, c in enumerate(poly):
                    out[k] += c*a
                    out[k+1] += c*b
                poly = out
            determinant = [(x+y) % p for x, y in zip(determinant, poly)]
        if any(determinant):
            return True
    return False


def main():
    rng, controls = Random(20260910), 0
    for p in (2, 3, 5):
        for requested in range(7):
            for _ in range(4):
                w = reduce([[rng.randrange(p) for _ in range(6)] for _ in range(requested)], 6, p)[0]
                full = symbolic_full(w, 3, p)
                degree = normal(w, 3, p)
                need(full == (degree is None), "symbolic exhaustive dichotomy")
                if full:
                    exceptional = [g for g in range(p) if len(reduce(
                        [[(a+g*b) % p for a, b in zip(row[:3], row[3:])] for row in w], 3, p)[1]) < 3]
                    need(len(exceptional) <= 6-len(w), "finite rank-drop count")
                controls += 1
    for p in (2, 5):
        for e in range(2, 6):
            s, w = 11, []
            for i in range(1, e):
                row = [0]*(2*s)
                row[i], row[s+i-1] = 1, -1 % p
                w.append(row)
            for j in range(e, s):
                for offset in (0, s):
                    row = [0]*(2*s)
                    row[offset+j] = 1
                    w.append(row)
            w = reduce(w, 2*s, p)[0]
            need(len(w) == 2*s-e-1 and normal(w, s, p) == e-1, "sharp full-shared chain degree")
            need(len(reduce([row[:s] for row in w]+[row[s:] for row in w], s, p)[1]) == s,
                 "full component-image sum")
    diagonal = [[(-i if j == i else 0) for j in range(3)]+[int(j == i) for j in range(3)]
                for i in range(3)]
    need(symbolic_full(diagonal, 3, 5) and normal(diagonal, 3, 5) is None, "regular diagonal pencil")
    bad = [g for g in range(5) if len(reduce([[a+g*b for a, b in zip(row[:3], row[3:])]
                                            for row in diagonal], 3, 5)[1]) < 3]
    need(bad == [0, 1, 2], "codimension exception bound can be sharp")
    print("PASS", controls, "symbolic small-pencil controls; eight sharp s11 chain examples; diagonal exceptions", bad)
    print("These are algebra models, not realized over-budget MCA sources; universal proof is separate")


if __name__ == "__main__":
    main()
