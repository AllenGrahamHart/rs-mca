"""Exact finite branch envelopes and same-source raw-mass gates."""

from fractions import Fraction as F
import importlib.util
from math import prod
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent/"mca_min_envelope_fiber_contraction/polynomial.py"
SPEC = importlib.util.spec_from_file_location("exact_envelope_polynomials", PATH)
P = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(P)
R, GAP, LO, END = 1048576, 67472, 9941, 21499
EXPECTED = {9: (578501226347492453, 469162745598573006),
            44: (581590844909990298, 471656010466926030),
            150: (591058329359405303, 479295814582433859)}


def need(ok, message):
    if not ok:
        raise ValueError(message)


def envelope(cutoff):
    D = GAP-cutoff
    q = [F(D+3), F(3*D+7, 2*(D+2)), F(1, 2*(D+2))]
    branches = [q]
    for rank in range(4, 12):
        children = []
        for q in branches:
            need(min(q) >= 0 and q[0] == D+rank-1, "positive shifted branch and seed")
            first, second = P.derivative(q), P.derivative(P.derivative(q))
            shapes = [first, second, P.sub(P.scale(first, 2), P.scale(second, END)),
                      P.sub(P.scale(first, 2*(rank-2)), P.scale(second, D+END))]
            need(all(min(P.bernstein(g, 0, END-rank+1)) >= 0 for g in shapes), "universal shape gates")
            children.append(P.add(q, [1, 1]))
            children.append(P.scale(P.mul([D+rank, 1], P.compose(q, 0, F(rank-2, rank-1))),
                                    F(1, D+rank-1)))
        branches = children
    need(len(branches) == 256, "complete endpoint tree")
    for q in branches:
        need(min(q) >= 0 and q[0] == D+11, "final positive branch")
        need(P.at(P.derivative(q), LO-11)*(R+LO-11) > 12*P.at(q, END-11),
             "every source quotient decreases on the whole interval")
        need((GAP+11)*q[1] >= q[0], "every beta/m quotient increases")
    return branches


def factor(cutoff):
    return 12*prod(GAP-cutoff+i for i in range(1, 11))


def beta(branches, cutoff, j):
    return factor(cutoff)*min(P.at(q, j-11) for q in branches)


def main():
    families = {cutoff: envelope(cutoff) for cutoff in EXPECTED}
    for cutoff, branches in families.items():
        for j, value in zip((LO, 14000), EXPECTED[cutoff]):
            ratio = F(prod(R+j-i for i in range(12)))/beta(branches, cutoff, j)
            need(value <= ratio < value+1, "exact endpoint floor")
        print("PASS CORE", cutoff, "256 branches; resource floors", EXPECTED[cutoff])
    high = 11*151*(GAP+END)*prod(GAP+i for i in range(1, 11))
    ratio = high/beta(families[150], 150, END)
    need(47 <= ratio < 48, "completed HIGH151 funds47, not48 with this endpoint bound")
    for cutoff in (9, 44):
        for small, large in zip(families[cutoff], families[150]):
            difference = P.sub(P.scale(large, (cutoff+1)*factor(150)),
                               P.scale(small, cutoff*factor(cutoff)))
            need(min(difference) >= 0, "branchwise intermediate-raw transfer")
        need(cutoff+1 <= 47, "HIGH covers same transferred gate")
    need(EXPECTED[44][0] < 624373932788019251 and EXPECTED[44][1] < 522680876725222604,
         "strict improvement of the old HIGH44 resource")
    print("PASS three full endpoint trees; 765 branch shape checks; 512 coefficient transfers")
    print("MASS min(raw,9)<=578501226347492453; min(raw,44)<=581590844909990298")
    print("All original raw ranges covered; no full J, source-rank or Prize closure")


if __name__ == "__main__":
    main()
