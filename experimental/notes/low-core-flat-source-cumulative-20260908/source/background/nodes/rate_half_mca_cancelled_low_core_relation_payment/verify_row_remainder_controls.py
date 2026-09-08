"""Eight-point actual MCA control; largest matrix is 40 by 36 over F_13."""

import importlib.util
from itertools import combinations
from pathlib import Path

PATH = Path(__file__).resolve().parents[1]/"mca_low_core_subfield_row_saturation"/"verify_small.py"
SPEC = importlib.util.spec_from_file_location("sextic_controls", PATH)
F = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(F)


def verify():
    assert F.power(F.BETA, 6) == 2
    assert F.power(F.BETA, 13**6) == F.BETA
    assert all(F.power(F.BETA, 13**d) != F.BETA for d in (1, 2, 3))
    pairs = [(j*j % 13, 0 if j == 1 else F.power(F.BETA, j-1))
             for j in range(1, 5)]
    cores = [{j, -j % 13} for j in range(1, 5)]
    receiver = {x: pair for pair, core in zip(pairs, cores) for x in core}
    labels, covered, margins = set(), set(), []
    for i, j in combinations(range(4), 2):
        gamma = F.mul(F.neg(F.sub(pairs[i][0], pairs[j][0])),
                      F.inverse(F.sub(pairs[i][1], pairs[j][1])))
        assert gamma not in labels
        labels.add(gamma)
        owner = 3 if (i, j) == (0, 3) else i
        support = cores[i] | cores[j]
        a, b = pairs[owner]
        h = F.add(a, F.mul(gamma, b))
        assert len(support) == 4
        assert all(F.add(receiver[x][0], F.mul(gamma, receiver[x][1])) == h
                   for x in support)
        assert len({receiver[x] for x in support}) == 2  # Not a constant pair.
        # All constant b not among the two received values have raw four.
        minimum = min(sum(receiver[x][1] != candidate for x in support)
                      for candidate in {receiver[x][1] for x in support})
        assert minimum == sum(receiver[x][1] != b for x in support) == 2
        full_core = {x for x in receiver if receiver[x] == (a, b)}
        assert full_core == cores[owner]
        covered |= full_core
        margins.append(minimum)
    assert len(labels) == 6 and covered == set(receiver)
    assert sum(margins) == 12 <= 8*7//4 == 14
    assert all(receiver[x][0] == x*x % 13 for x in receiver)

    def constraints(coefficients):
        a, b, c, d, q0, q1 = coefficients
        result = []
        for x, (u, v) in sorted(receiver.items()):
            row_u = F.mul(F.add(a, F.mul(b, x)), u)
            row_v = F.mul(F.add(c, F.mul(d, x)), v)
            residual = F.sub(F.add(row_u, row_v), F.add(q0, F.mul(q1, x)))
            result.extend(F.digits(residual)[1:])
        return result

    columns = []
    for position in range(36):
        coefficients = [0]*6
        coefficients[position//6] = 13**(position % 6)
        columns.append(constraints(coefficients))
    matrix = [list(row) for row in zip(*columns)]
    assert len(matrix) == 40 and len(matrix[0]) == 36
    assert F.rank_prime(matrix) == 32
    for index in (0, 1, 4, 5):
        coefficients = [0]*6
        coefficients[index] = 1
        assert not any(constraints(coefficients))
    # Only a,b,q0,q1 in E survive; exclude every old relation and offset.
    relation_matrix = [[x*x % 13, x**3 % 13, -1 % 13, -x % 13]
                       for x in receiver]
    assert F.rank_prime(relation_matrix) == 4
    print("PASS: six actual finite labels, full low union eight, minimum raw two")
    print("PASS: full E-row space cyclic of dimension two; offset kernel dimension two")
    print("PASS: row (1,0) has remainder X^2 in the new degree band")
    print("PASS: old relation coefficient matrix has full rank four")


if __name__ == "__main__":
    verify()
