"""Tiny exhaustive controls for the bad-evaluation dual-flat argument."""

from collections import Counter
from itertools import combinations, product

P = 5


def need(ok, message):
    if not ok:
        raise ValueError(message)


def rank2(columns):
    if not any(a or b for a, b in columns):
        return 0
    if any((a*d-b*c) % P for (a, b), (c, d) in combinations(columns, 2)):
        return 2
    return 1


def kernel(c):
    pivot = next(i for i, value in enumerate(c) if value)
    need(c[pivot] == 1, "normalized annihilator")
    basis = []
    for j in range(4):
        if j != pivot:
            v = [0]*4
            v[j], v[pivot] = 1, -c[j] % P
            need(sum(a*b for a, b in zip(c, v)) % P == 0, "kernel direction")
            basis.append(v)
    return basis


def evaluate(w, ell):
    return [((v[0]*ell[0]+v[1]*ell[1]) % P,
             (v[2]*ell[0]+v[3]*ell[1]) % P) for v in w]


def main():
    hyperplanes = [c for c in product(range(P), repeat=4)
                   if any(c) and next(v for v in c if v) == 1]
    need(len(hyperplanes) == 156, "complete projective dual space")
    for shifted, degree, expected in ((False, 2, {0: 126, 1: 30}),
                                      (True, 3, {1: 132, 2: 24})):
        counts = Counter()
        for c in hyperplanes:
            w = kernel(c)
            evaluations = [(x, x*x % P) if shifted else (1, x) for x in range(P)]
            bad = [ell for ell in evaluations if rank2(evaluate(w, ell)) < 2]
            need(rank2(bad) <= 1, "dual flat dimension <=2s-r=1")
            need(len(bad) <= degree-1, "root bound K+s-r")
            counts[len(bad)] += 1
        need(dict(counts) == expected, "complete bad-set census")
        print("PASS", len(hyperplanes), "shared-carrier hyperplanes; K", degree, "bad-set counts", dict(counts))
    sharp = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, -1 % P, 1)]
    bad = [x for x in range(P) if rank2(evaluate(sharp, (x, x*x % P))) < 2]
    need(bad == [0, 1], "common zero plus an additional bad anchor is sharp")
    equality = [(1, 0, 0, 0), (0, 1, 0, 0)]
    bad = [x for x in range(P) if rank2(evaluate(equality, (1, x))) < 2]
    need(len(bad) == 5 > 2, "r=s does not imply the improved root bound")
    print("PASS sharp common-zero control; r=s shortcut rejected")
    print("Arbitrary-field tensor independence and pencil rigidity require the hand proof")


if __name__ == "__main__":
    main()
