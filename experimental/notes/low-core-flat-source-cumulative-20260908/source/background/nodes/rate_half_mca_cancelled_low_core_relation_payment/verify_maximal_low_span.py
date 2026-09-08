"""Constant-size exact product/Fraction certificate for the low-span payment."""

from fractions import Fraction
from math import prod


def ceiling(value):
    return -(-value.numerator // value.denominator)


def verify():
    r, d, s, t = 1048576, 67472, 11, 500
    budget, near = 2130706433**6 // 2**128, 134944
    v10 = 156765527508668296
    assert 2*t < d and d >= s*(s+1)
    assert 2130706433**6 >= 2*r
    endpoints = [ceiling(Fraction(prod(r+j-i for i in range(s+1)),
                                 (d+j)*prod(d+i for i in range(1, s))))
                 for j in (4801, 169999)]
    assert endpoints == [13195104981505077258, 23067643444721720934]
    c = max(endpoints)
    alpha = Fraction((s+1)*d, d+s)
    assert 0 < alpha < t+1
    total_rational = (c+(t+1-alpha)*v10)/(t+1)
    total = total_rational.numerator // total_rational.denominator + near
    assert total == 199054477120667562 < budget
    assert budget-total == 75926250990727525
    low_rational = ((t+1)*(budget-near+1)-c)/(t+1-alpha)
    low_floor = ceiling(low_rational)
    assert low_floor == 234554688218295064 > v10
    assert alpha*(low_floor-1)+(t+1)*(budget-near+1-(low_floor-1)) > c
    assert alpha*low_floor+(t+1)*(budget-near+1-low_floor) <= c
    print("PASS: whole low-rank<=11 source total", total, "reserve", budget-total)
    print("PASS: unpaid source LOW count >=", low_floor, "; LOW rank must be twelve")


if __name__ == "__main__":
    verify()
