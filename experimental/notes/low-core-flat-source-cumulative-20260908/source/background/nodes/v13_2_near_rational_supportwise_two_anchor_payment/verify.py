#!/usr/bin/env python3
"""Tiny checks for the two-anchor payment and the repaired +1 regression."""

import json
from pathlib import Path


P = 17
D = tuple(range(1, P))  # F_17^* = mu_16
K = 8
W = 2
M = K + W
GAMMAS = (3, 5)
ERROR_INDICES = (0, 1)


def solve_polynomial(word, support):
    matrix = []
    for index in support[:K]:
        x = D[index]
        matrix.append([pow(x, degree, P) for degree in range(K)] + [word[index]])

    for column in range(K):
        pivot = next(row for row in range(column, K) if matrix[row][column] % P)
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        inverse = pow(matrix[column][column], P - 2, P)
        matrix[column] = [(inverse * value) % P for value in matrix[column]]
        for row in range(K):
            if row == column:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                (left - factor * right) % P
                for left, right in zip(matrix[row], matrix[column])
            ]

    coefficients = tuple(matrix[row][K] for row in range(K))
    for index in support:
        value = sum(
            coefficient * pow(D[index], degree, P)
            for degree, coefficient in enumerate(coefficients)
        ) % P
        if value != word[index]:
            return None
    return coefficients


u = [0] * len(D)
v = [0] * len(D)
for index, gamma in zip(ERROR_INDICES, GAMMAS):
    u[index] = -gamma % P
    v[index] = 1


def line_word(z):
    return tuple((left + z * right) % P for left, right in zip(u, v))


assert W >= 1
assert 3 * W <= len(D) - K

# Every slope is W-near the zero codeword and has a size-M zero support.
for z in range(P):
    word = line_word(z)
    assert sum(value != 0 for value in word) <= W
    assert sum(value == 0 for value in word) >= M

# The two selected slopes are support-wise bad on their own supports.
root_indices = tuple(range(2, 2 + M - 1))
for index, gamma in zip(ERROR_INDICES, GAMMAS):
    support = root_indices + (index,)
    assert len(support) == M
    assert all(line_word(gamma)[point] == 0 for point in support)
    assert solve_polynomial(tuple(v), support) is None

# Check the abstract two-anchor support and ratio identities on the fixture.
z0, z1 = GAMMAS
eta0 = line_word(z0)
eta1 = line_word(z1)
inverse = pow(z1 - z0, P - 2, P)
e_v = tuple((right - left) * inverse % P for left, right in zip(eta0, eta1))
e_u = tuple((left - z0 * right) % P for left, right in zip(eta0, e_v))
joint_support = {
    index for index, pair in enumerate(zip(e_u, e_v)) if pair != (0, 0)
}
assert joint_support == set(ERROR_INDICES)
assert len(joint_support) <= 2 * W
ratios = {
    (-e_u[index] * pow(e_v[index], P - 2, P)) % P
    for index in joint_support
    if e_v[index]
}
assert ratios == set(GAMMAS)

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes["v13_2_near_rational_supportwise_payment"]["status"] == "REFUTED"
assert nodes["v13_2_near_rational_supportwise_two_anchor_payment"]["status"] == "PROVED"

print("V13_2_NEAR_RATIONAL_TWO_ANCHOR_PAYMENT_OK", sorted(ratios))
