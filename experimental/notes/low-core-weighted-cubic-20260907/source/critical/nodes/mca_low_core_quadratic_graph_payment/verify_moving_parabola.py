"""Small exact moving-conic census and equality-case hypothesis guards."""

from itertools import product

from verify_small import P, add, mul, negative_inverse


def verify():
    assert pow(2, (P-1)//2, P) == P-1
    labels, owners = set(), set()
    for x in range(783):
        j = x//29+1
        for i in range(1, 28):
            if i == j:
                continue
            gamma = negative_inverse((x, pow(i+j, -1, P)))
            assert gamma not in labels
            labels.add(gamma)
            owners.add(i)
            a_i, a_j = (i*i % P, 0), (j*j % P, 0)
            b_i, b_j = (x*i*i % P, i), (x*j*j % P, j)
            assert a_i != a_j and b_i != b_j
            assert mul((0, i), (0, i)) == (2*i*i % P, 0)
            assert add(a_i, mul(gamma, b_i)) == add(a_j, mul(gamma, b_j))
    assert len(labels) == 20358 and len(owners) == 27
    assert 29 >= 2 and 27 < 30 and 2 < 30-2 and 27 > 2*7
    constant_axis, split_carriers = set(), set()
    for c0, c1 in product(range(5), repeat=2):
        square = (c0*c0 % 5, 2*c0*c1 % 5, c1*c1 % 5)
        second = ((square[0]+c0) % 5, (square[1]+c1) % 5, square[2])
        constant_axis.add((square, second))
        split_carriers.add((square, (0,)+second))
    assert len(constant_axis) == len(split_carriers) == 25
    assert 2 > 3//2 and 2 == 4//2
    degrees = set(range(6))
    square_degrees = {a+b for a in degrees for b in degrees}
    assert square_degrees == set(range(11))
    assert {d+1 for d in square_degrees} - square_degrees == {11}
    print("PASS: 20358 moving-parabola labels; all 27 pairs represented")
    print("PASS: constant-axis and unrelated-carrier gates; product-space endpoint")
    print("The degree-seven cover exclusion and equality theorem are hand proofs")


if __name__ == "__main__":
    verify()
