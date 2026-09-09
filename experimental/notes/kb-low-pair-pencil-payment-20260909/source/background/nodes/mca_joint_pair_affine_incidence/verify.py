"""Tiny exact families test two-constraint and bad-anchor hypotheses."""

from fractions import Fraction as Q
from itertools import product


def need(ok, message):
    if not ok:
        raise ValueError(message)


def value(poly, x, p):
    result = 0
    for coefficient in reversed(poly):
        result = (result*x+coefficient) % p
    return result


def rich_pairs(p, directions, receiver, threshold):
    k = len(directions[0][0])
    pairs = set()
    for coefficients in product(range(p), repeat=len(directions)):
        pair = tuple(tuple(sum(c*w[component][j] for c, w in zip(coefficients, directions)) % p
                           for j in range(k)) for component in (0, 1))
        agreements = sum((value(pair[0], x, p), value(pair[1], x, p)) == receiver[x]
                         for x in range(len(receiver)))
        if agreements >= threshold:
            pairs.add(pair)
    return pairs


def bound(n, k, a, r, e):
    need(k <= a <= n and 0 <= e < a and r >= 2, "incidence hypotheses")
    return Q(n-e, a-e)*Q(n-k+1, a-k+1)**(r-2)


def main():
    p = 7
    zero, one, x = (0, 0), (1, 0), (0, 1)
    receiver = [(a, 0) for a in (0, 0, 2, 0, 2, 0, 6)]
    pencil = [(one, zero), (x, zero)]
    pairs = rich_pairs(p, pencil, receiver, 3)
    need(len(pairs) >= 3 and len(pairs) <= Q(6, 2)**2, "affine pencil list")
    need(len(pairs) > bound(7, 2, 3, 2, 0), "rank-one pencil defeats a false two-drop")
    genuine = pencil+[(zero, one)]
    lifted = rich_pairs(p, genuine, receiver, 3)
    need(lifted == pairs and len(lifted) <= bound(7, 2, 3, 3, 0), "genuine rank-two anchor")
    need(len(lifted) <= bound(7, 2, 3, 3, 2), "coarse determinant-root gate")

    directions = [(x, zero), (zero, x)]
    receiver = [(a*a % p, 0) for a in range(p)]
    pairs = rich_pairs(p, directions, receiver, 2)
    need(len(pairs) == 6 == bound(7, 2, 2, 2, 1), "sharp actual bad-anchor example")
    need(len(pairs) > bound(7, 2, 2, 2, 0), "dropping the universal zero is false")
    determinant_roots = [a for a in range(p) if a*a % p == 0]
    need(determinant_roots == [0], "actual determinant-root set")
    try:
        bound(7, 2, 2, 2, 2)
    except ValueError:
        pass
    else:
        raise ValueError("accepted zero agreement denominator")
    cases = 0
    for n in range(3, 12):
        for a in range(2, n+1):
            for e in range(a-1):
                need(Q(n-e, a-e) <= Q(n-e-1, a-e-1), "bad-set monotonicity")
                cases += 1
    print("PASS exact pencil/genuine-pair families; six-pair sharp bad-anchor control")
    print("PASS", cases, "integer monotonicity cases and failed denominator gate")
    print("Only joint LIST pairs counted; no uncharged MCA projection")


if __name__ == "__main__":
    main()
