"""Exact cone prices, inherited all-record resource and quadratic root controls."""

from fractions import Fraction as F
import importlib.util
from itertools import product
from math import prod
from pathlib import Path

R, D, E, NEAR, B = 1048576, 67472, 21499, 134944, 274980728111395087
CASES = (
    (3, 9965, 624373932788019251, 151439604546110669, 12765991804643,
     269692335594445840, 7051190022598997),
    (2, 14000, 522680876725222604, 150069040313791513, 12763910835039,
     274290004332197866, 1036085668795833),
)


def need(ok, message):
    if not ok:
        raise ValueError(message)


def low(t, j):
    return F(2*prod(R+j-i for i in range(11)),
             11*(D+j-t)*prod(D-t+i for i in range(1, 10)))


def main():
    path = Path(__file__).resolve().parent.parent/"rate_half_mca_low_raw_rank_filtration/verify.py"
    spec = importlib.util.spec_from_file_location("credited_four_resource", path)
    supplier = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(supplier)
    a, b, c = supplier.ladder()
    q = lambda j: a+b*j+c*j*j
    beta = lambda j: 12*prod(supplier.D+i for i in range(1, 11))*q(j)
    need((b+2*c*9941)*(R+9941-11) > 12*q(E), "credited whole-interval monotonicity")
    need(126*(D+E)*prod(D+i for i in range(1, 11)) >= 4*beta(E), "credited all-HIGH funding")
    for j, expected in ((9941, CASES[0][2]), (14000, CASES[1][2])):
        need(int(F(prod(R+j-i for i in range(12)))/beta(j)) == expected, "credited integer resource")
    for t, lo, W, expected_mass, expected_pairs, expected_price, expected_outside in CASES:
        need(R+E-10-11*(D+E-t) > 0, "whole-J decreasing low quotient")
        for j in (lo, E-1):
            need(low(t, j+1)/low(t, j) == F(R+j+1, R+j-10)*F(D+j-t, D+j+1-t) <= 1,
                 "exact ratio identity")
        mass = int(low(t, lo))
        pairs = int(prod(F(R+i, D-t+i) for i in range(1, 12)))
        exceptions = E-9+2*pairs
        amount = W+t*(mass+exceptions)
        price = amount//(t+1)+NEAR
        outside = ((t+1)*(B-NEAR+1)-amount+t-1)//t
        need((mass, pairs, price, outside) == (expected_mass, expected_pairs, expected_price, expected_outside),
             "exact finite cone payment")
        need((amount+t*(outside-1))//(t+1)+NEAR == B, "last paid outside-label count")
        need((amount+t*outside)//(t+1)+NEAR == B+1, "adjacent sufficient envelope, not true optimum")
        print("PASS T", t, "J", (lo, E), "MASS", mass, "PAIRS", pairs,
              "EXCEPTIONS", exceptions, "PAY", price, "RESERVE", B-price, "OUTSIDE_MIN", outside)
    controls = 0
    for p in (2, 3, 5):
        for a, b, c in product(range(p), repeat=3):
            roots = [z for z in range(p) if (a+b*z+c*z*z) % p == 0]
            need(len(roots) == p if (a, b, c) == (0, 0, 0) else len(roots) <= 2,
                 "noncontained quadratic line root bound")
            controls += 1
    need([z for z in range(5) if (z-z*z) % 5 == 0] == [0, 1], "two exceptions can occur")
    print("PASS", controls, "quadratic restrictions; no single-owner or contained-line shortcut")
    print("Full general low graphs, lower-J quadratic G2, higher ranks and both Prizes remain open")


if __name__ == "__main__":
    main()
