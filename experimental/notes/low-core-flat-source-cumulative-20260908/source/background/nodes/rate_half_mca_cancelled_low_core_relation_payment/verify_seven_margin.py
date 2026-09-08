"""Exact small certificate for seven-margin and very-low-rank source payments."""

from fractions import Fraction as Q
from math import prod


def ceiling(value):
    return -(-value.numerator // value.denominator)


def verify():
    d, s, near = 67472, 11, 134944
    budget = 2130706433**6 // 2**128
    endpoints = [ceiling(Q(prod(1048576+j-i for i in range(12)),
                           (d+j)*prod(d+i for i in range(1, 11))))
                 for j in (4801, 169999)]
    assert endpoints == [13195104981505077258, 23067643444721720934]
    c = max(endpoints)
    alpha = Q(12*d, d+s)

    def weight(r):
        return 12*r*Q(d+s-r, d+s)*prod(Q(d-r+i, d+i) for i in range(1, 11))

    omega = weight(7)
    assert omega == Q(1359828247211942851691371569952, 16206915841717723963443447881)
    assert 12*84 < d+1 and alpha < omega < 84 <= d+1
    assert all(weight(r) <= weight(r+1) for r in range(7, 84))
    # The derivative proves the whole interval; the old weight covers every r>=84.
    total = int(c/omega)+near
    assert total == 274928364476952114 < budget
    assert budget-total == 52363634442973
    assert int(c/weight(6))+near == 320697470408695467 > budget
    assert (500-7+1, 139-7) == (494, 132)
    v7 = 50371450079970
    rank_total = int((c+(omega-alpha)*v7)/omega)+near
    assert rank_total == 274971532963425180 < budget
    assert budget-rank_total == 9195147969907
    low = ceiling((omega*(budget-near+1)-c)/(omega-alpha))
    assert low == 61100872739557 > v7
    assert alpha*(low-1)+omega*(budget-near+1-(low-1)) > c
    assert alpha*low+omega*(budget-near+1-low) <= c
    print("PASS: raw>=7 total", total, "reserve", budget-total)
    print("PASS: raw<=6 rank<=8 total", rank_total, "reserve", budget-rank_total)
    print("PASS: unpaid raw<=6 mass >=", low, "; 132 more remainder degrees paid")


if __name__ == "__main__":
    verify()
