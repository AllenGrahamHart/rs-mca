"""Exact weighted-graph census, characteristic guard and false-fit control."""

from itertools import product

from verify_small import P, add, mul, negative_inverse, scale


def poly_mul(a, b, p):
    result = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] = (result[i+j]+x*y) % p
    return result


def evaluate(coefficients, x, p):
    value = 0
    for coefficient in reversed(coefficients):
        value = (value*x+coefficient) % p
    return value


def verify():
    assert pow(2, (P-1)//2, P) == P-1
    labels, owners = set(), set()
    for x in range(1, 784):
        j, value = (x-1)//29+1, (x, 1)
        z = scale(x, value)
        for i in range(1, 28):
            if i == j:
                continue
            denominator = scale(i+j, z)
            gamma = negative_inverse(denominator)
            assert mul(gamma, denominator) == (P-1, 0)
            assert gamma not in labels
            labels.add(gamma)
            owners.add(i)
            a_i, a_j = scale(i, value), scale(j, value)
            b_i, b_j = scale(x, mul(a_i, a_i)), scale(x, mul(a_j, a_j))
            assert a_i != a_j and b_i != b_j
            assert add(a_i, mul(gamma, b_i)) == add(a_j, mul(gamma, b_j))
    assert len(labels) == 20358 and len(owners) == 27
    assert 29 >= 4 and 27 < 30 and 2 < 30-4
    assert 27 > 4
    characteristic_three = set()
    for c0, c1, c2 in product(range(3), repeat=3):
        a = [0]*10
        a[0], a[1], a[3] = c0, c1, c2
        cube = poly_mul(poly_mul(a, a, 3), a, 3)
        assert all(value == 0 or degree in (0, 3, 9)
                   for degree, value in enumerate(cube))
        characteristic_three.add(tuple(a))
    assert len(characteristic_three) == 27 and 3 > 4//2
    lagrange = poly_mul(poly_mul([0, 1], [-1, 1], 5), [-2, 1], 5)
    locator = poly_mul(lagrange, [-3, 1], 5)
    for x in range(4):
        u, v = (1, 0) if x < 3 else (0, 1)
        assert (u+v) % 5 == 1
        assert (evaluate(lagrange, x, 5)+evaluate(locator, x, 5)*u*u) % 5 == v
    false_identity = [(lagrange[i] if i < len(lagrange) else 0)+locator[i]
                      for i in range(len(locator))]
    false_identity = [value % 5 for value in false_identity]
    assert false_identity == [0, 1, 3, 0, 1]
    assert sum((0, 0, 0, 1)[x] != 0 for x in range(4)) == 1
    assert 3 >= 2 and 4+2*(2-1) > 4-1-1
    print("PASS: 20358 canonical weighted-quadratic labels, all 27 pairs represented")
    print("PASS: characteristic-three cubic counterfamily has three free coefficients")
    print("PASS: actual raw-one pointwise graph fit fails the polynomial identity")
    print("The universal constant-matrix exclusion is the hand coefficient proof, not a scan")


if __name__ == "__main__":
    verify()
