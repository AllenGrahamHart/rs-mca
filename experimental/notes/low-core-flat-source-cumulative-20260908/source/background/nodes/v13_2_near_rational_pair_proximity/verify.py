#!/usr/bin/env python3
"""Replay the near-rational pair-proximity algebra on a complete toy grid."""

import json
from itertools import product
from pathlib import Path


def inv(x, p):
    return pow(x, p - 2, p)


def add(a, b, p):
    return tuple((x + y) % p for x, y in zip(a, b))


def scale(s, a, p):
    return tuple((s * x) % p for x in a)


def sub(a, b, p):
    return add(a, scale(-1, b, p), p)


def support(a):
    return {i for i, x in enumerate(a) if x}


p = 3
n = 4
w = 1
zero = (0,) * n
errors = [zero]
for i in range(n):
    for value in range(1, p):
        error = [0] * n
        error[i] = value
        errors.append(tuple(error))

checked = 0
for z1, z2 in product(range(p), repeat=2):
    if z1 == z2:
        continue
    denominator_inv = inv((z1 - z2) % p, p)
    for a1, a2, eta1, eta2 in product(range(p), range(p), errors, errors):
        c1 = (a1,) * n
        c2 = (a2,) * n
        cv = scale(denominator_inv, sub(c1, c2, p), p)
        epsilon_v = scale(denominator_inv, sub(eta1, eta2, p), p)
        v = add(cv, epsilon_v, p)
        cu = sub(c1, scale(z1, cv, p), p)
        epsilon_u = sub(eta1, scale(z1, epsilon_v, p), p)
        u = add(cu, epsilon_u, p)

        assert add(u, scale(z1, v, p), p) == add(c1, eta1, p)
        assert add(u, scale(z2, v, p), p) == add(c2, eta2, p)
        joint_support = support(epsilon_u) | support(epsilon_v)
        input_support = support(eta1) | support(eta2)
        assert joint_support <= input_support
        assert len(joint_support) <= 2 * w
        checked += 1

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes["v13_2_near_rational_pair_proximity"]["status"] == "PROVED"
assert nodes["v13_2_near_rational_supportwise_payment"]["status"] == "REFUTED"
assert checked == 4_374

print("V13_2_NEAR_RATIONAL_PAIR_PROXIMITY_PASS", checked)
