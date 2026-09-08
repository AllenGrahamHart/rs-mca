"""Tiny actual-field controls for the union-overlap implication."""

from itertools import product

P = 7
D = tuple(range(4))
POLYNOMIALS = tuple(product(range(P), repeat=2))


def evaluate(poly, x):
    return (poly[0] + poly[1] * x) % P


def inspect(u, v, records):
    cores, pairs = [], []
    for gamma, h, support, b in records:
        assert all((u[x] + gamma * v[x]) % P == evaluate(h, x) for x in support)
        margins = [sum(v[x] != evaluate(poly, x) for x in support) for poly in POLYNOMIALS]
        assert min(margins) == sum(v[x] != evaluate(b, x) for x in support) == 1
        a = tuple((h[j] - gamma * b[j]) % P for j in range(2))
        core = {x for x in D if u[x] == evaluate(a, x) and v[x] == evaluate(b, x)}
        assert len(core) >= 2
        assert not set(support) <= core
        cores.append(core)
        pairs.append((a, b))
    return cores, pairs


def verify():
    zero = (0, 0)
    cores, pairs = inspect([0, 0, 1, 1], [0, 0, 1, 2],
                           [(6, zero, (0, 1, 2), zero), (3, zero, (0, 1, 3), zero)])
    assert len(set.union(*cores)) == 2
    assert pairs[0] == pairs[1]
    assert len(pairs) == len(D) - len(cores[0])
    cores, pairs = inspect([0, 0, 0, 3], [0, 0, 2, 0],
                           [(0, zero, (0, 1, 2), zero), (1, (0, 1), (0, 2, 3), (0, 1))])
    assert len(set.union(*cores)) == 3
    assert len(cores[0] & cores[1]) == 1
    assert pairs[0] != pairs[1]
    print("PASS: complete-pair collapse, saturated outside injection, sharp K-1 overlap control")


if __name__ == "__main__":
    verify()
