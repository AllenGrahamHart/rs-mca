"""Tiny guard controls and exact canonical sextic-field families."""

import importlib.util
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PATH = ROOT/"background/nodes/mca_low_core_subfield_row_saturation/verify_small.py"
SPEC = importlib.util.spec_from_file_location("sextic", PATH)
F = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(F)


def small_guards():
    def maxima(values, m):
        margins = []
        for support in combinations(range(len(values)), m):
            if len({values[x] for x in support}) > 1:
                margins.append(min(sum(values[x] != b for x in support) for b in range(5)))
        return max(margins), min(sum(value != b for value in values) for b in range(5))
    assert maxima([0, 0, 0, 1, 1], 4) == (2, 2)
    assert min(sum(value != b for value in [0, 0, 0, 1]) for b in range(5)) == 1
    assert maxima([0, 0, 1, 1], 3) == (1, 2)
    assert maxima([0, 0, 0, 0, 1], 4) == (1, 1)
    print("PASS: omitted maximality and 2T=d are false; contained neighbors handled")


def fit(values, x, y):
    slope = F.mul(F.sub(values[y], values[x]), pow((y-x) % 13, -1, 13))
    return (F.sub(values[x], F.mul(slope, x)), slope)


def product_coefficients(row, pair):
    result = [0]*4
    for component in range(2):
        for i, coefficient in enumerate(row[3*component:3*component+3]):
            for j, value in enumerate(pair[component]):
                result[i+j] = F.add(result[i+j], F.mul(coefficient, value))
    return result


def audit_case(name, pairs, expected_dimension):
    receiver = [tuple(F.evaluate(poly, x) for poly in pairs[x//4]) for x in range(12)]
    cores = [{x for x in range(12) if receiver[x] == tuple(F.evaluate(poly, x) for poly in pair)}
             for pair in pairs]
    assert cores == [set(range(4)), set(range(4, 8)), set(range(8, 12))]
    for pair1, pair2 in combinations(pairs, 2):
        a = [F.sub(x, y) for x, y in zip(pair1[0], pair2[0])]
        b = [F.sub(x, y) for x, y in zip(pair1[1], pair2[1])]
        assert F.sub(F.mul(a[0], b[1]), F.mul(a[1], b[0]))
    labels = set()
    for owner, pair in enumerate(pairs):
        for x in set(range(12))-cores[owner]:
            du, dv = [F.sub(receiver[x][i], F.evaluate(pair[i], x)) for i in range(2)]
            if dv:
                labels.add(F.mul(F.neg(du), F.inverse(dv)))
    assert len(labels) == 23
    assert set().union(*cores) == set(range(12))
    assert len(labels) <= sum(len(receiver)-len(core) for core in cores) == 24
    # An outside-union-only count would be zero, although all 23 labels are bad.
    assert len(labels) > len(cores)*(len(receiver)-len(set().union(*cores)))
    for gamma in labels:
        values = [F.add(u, F.mul(gamma, v)) for u, v in receiver]
        candidates = {fit(values, x, y) for x, y in combinations(range(12), 2)}
        pieces = {tuple(F.add(pair[0][i], F.mul(gamma, pair[1][i])) for i in range(2))
                  for pair in pairs}
        assert len(pieces) == 3
        accepted = []
        for h in candidates:
            agreement = {x for x in range(12) if F.evaluate(h, x) == values[x]}
            if len(agreement) >= 5:
                assert h in pieces and len(agreement) == 5
                accepted.append(agreement)
            elif h not in pieces:
                assert len(agreement) <= 3
        assert len(accepted) == 1
        support = accepted[0]
        b_values = [value[1] for value in receiver]
        second_candidates = {fit(b_values, x, y) for x, y in combinations(sorted(support), 2)}
        minima = [(sum(F.evaluate(b, x) != b_values[x] for x in support), b)
                  for b in second_candidates]
        assert min(raw for raw, _ in minima) == 1
        best = [b for raw, b in minima if raw == 1]
        assert len(best) == 1
        # All other affine second polynomials match at most one point, hence raw>=4.
        assert sum(F.evaluate(best[0], x) != b_values[x] for x in support) == 1
    columns = []
    for position in range(36):
        row = [0]*6
        row[position//6] = 13**(position % 6)
        columns.append([c for pair in pairs[1:] for value in product_coefficients(row, pair)
                        for c in F.digits(value)[1:]])
    matrix = [list(row) for row in zip(*columns)]
    assert (len(matrix), len(matrix[0])) == (40, 36)
    assert 36-F.rank_prime(matrix) == expected_dimension
    if expected_dimension:
        for position in range(3):
            row = [0]*6
            row[position] = 1
            assert all(value < 13 for pair in pairs for value in product_coefficients(row, pair))
    print(name, "PASS: exactly 23 globally maximal-raw-one labels, rank-two crosses, row dimension",
          expected_dimension)


def verify():
    small_guards()
    assert F.power(F.BETA, 6) == 2 and F.power(F.BETA, 13) == F.mul(4, F.BETA)
    assert F.power(F.BETA, 13**6) == F.BETA
    assert all(F.power(F.BETA, 13**d) != F.BETA for d in (1, 2, 3))
    beta2, beta3 = F.power(F.BETA, 2), F.power(F.BETA, 3)
    audit_case("ZERO", [([0, 0], [0, 0]), ([F.BETA, 0], [0, 1]),
                        ([0, beta2], [beta3, 0])], 0)
    audit_case("CYCLIC", [([0, 0], [0, 0]), ([1, 0], [0, F.BETA]),
                          ([0, 1], [beta2, 0])], 3)


if __name__ == "__main__":
    verify()
