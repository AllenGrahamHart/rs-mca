"""Tiny sharpness and endpoint controls for the integer-mass envelope."""

from itertools import combinations_with_replacement
from fractions import Fraction as Q


def need(ok, why):
    if not ok:
        raise ValueError(why)


def main():
    S, T, H, alpha, beta = 11, 3, 2, Q(2), Q(7)
    count = 0
    for size in range(5):
        for masses in combinations_with_replacement(range(2, 10), size):
            if sum(masses) > S:
                continue
            large = sum(x > T for x in masses)
            weight = sum(alpha*x+(beta if x > T else 0) for x in masses)
            need(large <= H and weight <= alpha*S+H*beta, "universal integer-envelope instance")
            count += 1
    need((H+1)*(T+1) > S and sum((4, 4, 3)) == S, "two large fibres can be necessary")
    need(3*349526 == 1048578 > 1048577, "official strict integer threshold")
    need(3*(349524+1) <= 1048577, "one smaller threshold does not prove at most two")
    print("PASS", count, "small mass multisets and official integer threshold")
    print("Universal proof is summation plus the integer cardinality bound, not this fixture")


if __name__ == "__main__":
    main()
