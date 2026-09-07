"""Small canonical high-height pencil, full row-space audit and cover guard."""

import importlib.util
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PATH = ROOT/"background/nodes/mca_low_core_subfield_row_saturation/verify_small.py"
SPEC = importlib.util.spec_from_file_location("rational_line_field", PATH)
F = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(F)
# This private helper instance has no cached field tables; other tests stay at F_13.
F.P, F.ORDER, F.BETA = 19, 19**6, 19


def polynomial_value(coefficients, x):
    value = 0
    for coefficient in reversed(coefficients):
        value = F.add(F.mul(value, x), coefficient)
    return value


def row_product(row):
    result = [0]*6
    for i in range(3):
        result[i] = F.add(result[i], row[i+3])
        result[i+1] = F.add(result[i+1], F.mul(F.BETA, row[i]))
        result[i+3] = F.add(result[i+3], row[i])
    return result


def verify():
    assert F.power(F.BETA, 6) == 2
    assert F.power(F.BETA, 19) == F.mul(8, F.BETA)
    assert F.power(F.BETA, 19**6) == F.BETA
    assert all(F.power(F.BETA, 19**e) != F.BETA for e in (1, 2, 3))
    values = [polynomial_value([0, F.BETA, 0, 1], x) for x in range(18)]
    assert len(set(values)) == 18
    constants = [0, 1, F.BETA]
    receiver = [(F.mul(constants[x//6], values[x]), constants[x//6]) for x in range(18)]
    cores = [{x for x in range(18) if receiver[x] == (F.mul(c, values[x]), c)} for c in constants]
    assert cores == [set(range(6)), set(range(6, 12)), set(range(12, 18))]
    inverses = {(x, y): F.inverse(F.sub(values[y], values[x]))
                for x, y in combinations(range(18), 2)}
    labels, assigned = set(), set()
    for root, value in enumerate(values):
        gamma = F.neg(value)
        labels.add(gamma)
        received = [F.add(u, F.mul(gamma, v)) for u, v in receiver]
        pieces = {(c, F.mul(c, gamma)) for c in constants}
        candidates = set()
        for (x, y), inverse in inverses.items():
            alpha = F.mul(F.sub(received[y], received[x]), inverse)
            eta = F.sub(received[x], F.mul(alpha, values[x]))
            candidates.add((alpha, eta))
        accepted = []
        for alpha, eta in candidates:
            agreement = {x for x in range(18) if F.add(F.mul(alpha, values[x]), eta) == received[x]}
            if (alpha, eta) in pieces:
                assert len(agreement) in (6, 7)
            else:
                assert len(agreement) <= 3
            if len(agreement) >= 7:
                accepted.append(agreement)
        assert len(accepted) == 2
        owner = (root//6+1) % 3
        assigned.add(owner)
        support = cores[owner] | {root}
        assert support in accepted and len(support) == 7
        assert sum(receiver[x][1] != constants[owner] for x in support) == 1
        assert len(cores[owner]) >= 4 and 2*1 < 3
    assert len(labels) == 18 and assigned == {0, 1, 2}
    columns = []
    for position in range(36):
        row = [0]*6
        row[position//6] = 19**(position % 6)
        w = row_product(row)
        columns.append([coefficient for poly in (w, [F.mul(F.BETA, v) for v in w])
                        for value in poly for coefficient in F.digits(value)[1:]])
    matrix = [list(row) for row in zip(*columns)]
    assert (len(matrix), len(matrix[0])) == (60, 36)
    assert F.rank_prime(matrix) == 36
    for a, b, c in combinations(range(1, 28), 3):
        determinant = ((b-a)*(c*c-a*a)-(c-a)*(b*b-a*a)) % 101
        assert determinant != 0
    assert all((a+b) % 101 for a, b in combinations(range(1, 28), 2))
    assert (27+1)//2 == 14 > 13
    print("PASS: exactly 18 canonical raw-one labels; all are preferred rational directions")
    print("PASS: height three >ell two, full bounded E-row space ZERO (60x36 rank36)")
    print("PASS: common-carrier dimension two does not force a thirteen-pencil cover")


if __name__ == "__main__":
    verify()
