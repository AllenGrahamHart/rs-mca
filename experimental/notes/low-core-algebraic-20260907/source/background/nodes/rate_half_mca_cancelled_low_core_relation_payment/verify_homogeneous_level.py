"""Exact dimension-one group ledger and mixed degree-seven payments."""

from fractions import Fraction

import verify as base


def unit_gain():
    return sum((Fraction((981104+t)*1048577, (67473-t)*t*(t+1))
                for t in range(1, 501)), Fraction(0))


def verify():
    gain = unit_gain()
    g2, g3 = (base.ceil(e**21*gain) for e in (2, 3))
    assert (g2, g3) == (31914462418027, 159185671413625180)
    resource = base.ceil(max(base.resource(j) for j in (4801, 169999)))
    assert resource == 23067643444721720934
    fixed = resource//501+134944
    assert fixed+g2 == 46075114951019479
    assert fixed+g3 == 205228871902226632
    w, q = 17200000000000000, Fraction(63, 4)
    assert Fraction(1048577, 66973) < q and g2 < 2*w
    for degree in range(2, 8):
        rank = 6 if degree == 2 else 5
        cost = degree**(11-rank)*q**rank*981604
        assert cost < degree*w
    assert 7**5*q**5*981604 < w
    assert fixed+7*w == 166443200488601452
    assert fixed+g3+4*w == 274028871902226632
    assert base.BUDGET-fixed-g3-4*w == 951856209168455
    for raw in (1, 2, 7, 499, 500):
        assert sum((Fraction(raw, t*(t+1)) for t in range(raw, 501)), Fraction(0)) == 1-Fraction(raw, 501)
    assert fixed+2*g3 > base.BUDGET
    assert fixed+base.ceil(4**21*gain) > base.BUDGET
    print("PASS: homogeneous quadratic/cubic gains", g2, g3)
    print("PASS: cubic mixed cover", fixed+g3+4*w, "reserve", base.BUDGET-fixed-g3-4*w)
    print("Controls: telescoping endpoints; two-cubic and quartic recipes NOT certified")


if __name__ == "__main__":
    verify()
