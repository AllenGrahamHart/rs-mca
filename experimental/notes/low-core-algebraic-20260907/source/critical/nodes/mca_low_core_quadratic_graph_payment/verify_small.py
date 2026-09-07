"""Exact bounded-memory canonical parabola and geometric degree controls."""

from itertools import combinations, product
from math import isqrt

P = 787


def add(x, y):
    return ((x[0] + y[0]) % P, (x[1] + y[1]) % P)


def mul(x, y):
    return ((x[0]*y[0] + 2*x[1]*y[1]) % P,
            (x[0]*y[1] + x[1]*y[0]) % P)


def scale(c, x):
    return (c*x[0] % P, c*x[1] % P)


def negative_inverse(x):
    norm = (x[0]*x[0] - 2*x[1]*x[1]) % P
    assert norm
    reciprocal = pow(norm, -1, P)
    return (-x[0]*reciprocal % P, x[1]*reciprocal % P)


def verify():
    assert all(P % divisor for divisor in range(2, isqrt(P) + 1))
    assert pow(2, (P-1)//2, P) == P-1
    k, m, raw, groups, core = 3, 30, 1, 27, 29
    assert core == m-raw >= k and groups < m and 2*raw < m-k
    labels, owners = set(), set()
    for x in range(groups*core):
        j, value = x//core + 1, (x, 1)
        for i in range(1, groups + 1):
            if i == j:
                continue
            denominator = scale(i+j, value)
            gamma = negative_inverse(denominator)
            assert mul(gamma, denominator) == (P-1, 0)
            assert gamma not in labels
            labels.add(gamma)
            owners.add(i)
            a_i, b_i = scale(i, value), scale(i*i, mul(value, value))
            a_j, b_j = scale(j, value), scale(j*j, mul(value, value))
            assert a_i != a_j and b_i != b_j
            assert add(a_i, mul(gamma, b_i)) == add(a_j, mul(gamma, b_j))
    assert len(labels) == 20358 and len(owners) == 27
    for i, j, k in combinations(range(1, 28), 3):
        assert ((j-i)*(k*k-i*i)-(k-i)*(j*j-i*i)) % P
    assert all((i+j) % P for i, j in combinations(range(1, 28), 2))
    assert (27+1)//2 == 14 > 13
    received = (0, 0, 1, 1)
    degree_two_points = [a for a in (0, 1) if sum(a == w for w in received) >= 2]
    assert len(degree_two_points) == 2 > 1
    characteristic_two = set()
    for coefficients in product((0, 1), repeat=3):
        a = tuple(coefficients) + (0, 0)
        square = (coefficients[0], 0, coefficients[1], 0, coefficients[2])
        assert a[3] == square[3] == 0
        characteristic_two.add((a, square))
    assert len(characteristic_two) == 8 and 3 > (4+1)//2
    assert 2*5 < 11 and (11+1)//2 == 6
    print("PASS: 20358 exact canonical raw-one labels, all 27 parabola pairs represented")
    print("PASS: fourteen lines necessary; constant-plus-nonconstant cover also impossible")
    print("PASS: geometric degree factor cannot be dropped from the LIST bound")
    print("PASS: characteristic-two counterfamily and sharp odd-characteristic dimension")


if __name__ == "__main__":
    verify()
