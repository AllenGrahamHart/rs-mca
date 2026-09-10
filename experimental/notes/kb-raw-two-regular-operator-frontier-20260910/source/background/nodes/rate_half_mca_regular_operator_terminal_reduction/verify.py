"""Exact stage dimensions and factors for the four regular operator terminals."""

from fractions import Fraction as Q
from math import prod


def need(ok, why):
    if not ok:
        raise ValueError(why)


def main():
    R, d, low, high = 1048576, 67472, 9965, 21499
    rows = []
    for rank in range(19, 23):
        count, codimension = rank-11, 22-rank
        need(2130706433**6 > codimension, "original-field finite chart")
        for t in (1, 2):
            expected = prod(Q(R+j, d-t+j) for j in range(1, count+1))
            for J in (low, high):
                product = Q(1)
                for i in range(count):
                    r, s = rank-2*i, 11-i
                    bad, A, n = J+s-r, d+J-t, R+J
                    need(s < r <= 2*s and 2*s-r == codimension, "regular strict stage")
                    need(i <= bad < A <= n and J-i >= s, "old anchors and positive root-flat corridor")
                    product *= Q(n-bad, A-bad)
                need(product == expected, "identical exact product, no extra history denominator")
        need(rank-2*count == 11-count == codimension and low-count >= codimension,
             "square regular terminal")
        rows.append((rank, count, codimension))
    need(rows == [(19, 8, 3), (20, 9, 2), (21, 10, 1), (22, 11, 0)], "complete frontier")
    need(1048576-67472+1 == 981105 and 1048576-67472+2 == 981106, "original c0 owner caps")
    print("PASS eight rank/cutoff chains; degree endpoints; exact regular terminal rows", rows)
    print("No affordable dimension1/2/3 terminal weights or original-source payment asserted")


if __name__ == "__main__":
    main()
