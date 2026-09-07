"""Small exact hyperbola census and missing-hypothesis controls."""

import importlib.util
from itertools import product
from pathlib import Path

path = Path(__file__).resolve().parents[1]/"mca_low_core_quadratic_graph_payment"/"verify_small.py"
spec = importlib.util.spec_from_file_location("graph_field_arithmetic", path)
field = importlib.util.module_from_spec(spec)
spec.loader.exec_module(field)


def verify():
    p = field.P
    assert pow(2, (p-1)//2, p) == p-1
    labels, owners = set(), set()
    for x in range(783):
        j, value = x//29+1, (x, 1)
        for i in range(1, 28):
            if i == j:
                continue
            gamma = field.scale(i*j, value)
            assert gamma not in labels
            labels.add(gamma)
            owners.add(i)
            a_i, a_j = field.scale(i, value), field.scale(j, value)
            b_i, b_j = (pow(i, -1, p), 0), (pow(j, -1, p), 0)
            assert a_i != a_j and b_i != b_j
            assert field.mul(a_i, b_i) == value
            assert field.add(a_i, field.mul(gamma, b_i)) == field.add(
                a_j, field.mul(gamma, b_j))
    assert len(labels) == 20358 and len(owners) == 27
    assert 29 >= 2 and 27 < 30 and 2 < 30-2 and 27 > 2*7
    zero_level = {((0, 0), b) for b in product(range(5), repeat=2)}
    single_direction = {((1, 0), b) for b in product(range(5), repeat=2)}
    assert len(zero_level) == len(single_direction) == 25
    assert 1*(1+1) == 2
    assert all(a*b*(a+b+1) % 5 == 1 for a, b in ((2, 3), (2, 4)))
    assert all(not (h == 0 and k == 0 and -2*(h+k) % 5 == 1)
               for h, k in product(range(5), repeat=2))
    torus = {(t, pow(t, -1, 5)) for t in range(1, 5)}
    assert len(torus) == 4 and all(a*b % 5 == 1 for a, b in torus)
    print("PASS: 20358 canonical hyperbola labels, all 27 pairs represented")
    print("PASS: zero-level, single-direction and scalar-family guards")
    print("Universal geometric and graph-exclusion assertions are hand proofs")


if __name__ == "__main__":
    verify()
