"""Exact proper-hyperplane prices and small algebraic ownership controls."""

from fractions import Fraction as F
import importlib.util
from itertools import product
from math import prod
from pathlib import Path

R, D, E, NEAR, B = 1048576, 67472, 21499, 134944, 274980728111395087


def need(ok, message):
    if not ok:
        raise ValueError(message)


def low(k):
    return F(prod(range(R+k-10, R+k+1)), 11*(D+k-2)*prod(range(D-1, D+8)))


def main():
    path = Path(__file__).resolve().parent.parent/"rate_half_mca_low_pair_pencil_payment/verify.py"
    spec = importlib.util.spec_from_file_location("credited_original_basis", path)
    supplier = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(supplier)
    W = int(supplier.basis())
    need(W == 613022127444579907, "credited original unrefunded resource")
    need(R+E-10-11*(D+E-2) == 91406 > 0, "whole-corridor decreasing-ratio gate")
    for k in (10, 11, 9965, E-1):
        ratio = F(R+k+1, R+k-10)*F(D+k-2, D+k-1)
        need(low(k+1)/low(k) == ratio <= 1, "exact falling-factorial ratio")
    M = int(low(10))
    pairs = int(prod(F(R+j, D-2+j) for j in range(1, 12)))
    need((M, pairs) == (78301130139301820, 12763910835039), "exact integral low and pair caps")
    carrier, graph = (W+2*M)//3+NEAR, (W+2*M+2*pairs)//3+NEAR
    need((carrier, graph) == (256541462574529459, 256549971848419485), "whole-source prices")
    need(B-graph == 18430756262975602 and B-carrier == 18439265536865628, "strict reserves")
    outside = (3*(B-NEAR+1)-W-2*(M+pairs)+1)//2
    need(outside == 27646134394463404, "integer hyperplane spread")
    need((W+2*(M+pairs)+2*(outside-1))//3+NEAR == B, "last safe exception count")
    need((W+2*(M+pairs)+2*outside)//3+NEAR == B+1, "adjacent recipe count, not a bad source")
    controls = 0
    for e0, c, a, b in product(range(5), repeat=4):
        solutions = [g for g in range(5) if (a-e0+g*(b+c)) % 5 == 0]
        compatible = (a-e0) % 5 == (b+c) % 5 == 0
        need(len(solutions) == 5 if compatible else len(solutions) <= 1, "hyperplane pair partition")
        controls += 1
    for raw in product(range(1, 6), repeat=4):
        mass = sum(min(t, 3) for t in raw)
        deficit = sum(3-t for t in raw if t <= 2)
        need(mass+deficit == 3*len(raw), "same-resource deficit identity")
        need(deficit <= 2*sum(t for t in raw if t <= 2), "compatible-family weighted bound")
    print("PASS original W3; LOW", M, "PAIR", pairs, "CARRIER", carrier, "GRAPH", graph)
    print("PASS", controls, "F5 hyperplane controls; 625 deficit ledgers; OUTSIDE_MIN", outside)
    print("Full low-graph/shared11/pair16..22 remains open; no whole row or Prize closure")


if __name__ == "__main__":
    main()
