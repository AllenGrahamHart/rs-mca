"""Small exact moving-conic and original mixed-cover arithmetic."""

from fractions import Fraction

import verify as base


def verify():
    assert 2130706433 % 2 == 1
    assert Fraction(1048577, 66973) < Fraction(63, 4)
    pairs = 2**17*Fraction(63, 4)**5
    assert pairs.denominator == 1 and pairs == 127031877504
    gain = int(pairs)*981604
    assert gain == 124694999085436416
    c = base.ceil(max(base.resource(j) for j in (4801, 169999)))
    assert c == 23067643444721720934
    fixed, w = c//501+134944, 17200000000000000
    assert fixed+gain == 170738199574037868
    assert base.BUDGET-fixed-gain == 104242528537357219
    assert 46075114951019479 < 46570195123304300 < fixed+gain
    assert 981604 < 2*w
    assert fixed+gain+5*w == 256738199574037868
    assert base.BUDGET-fixed-gain-5*w == 18242528537357219
    assert fixed+2*gain+3*w > base.BUDGET
    assert fixed+gain+159185671413625180 > base.BUDGET
    print("PASS: all individual nonsingular conics", fixed+gain)
    print("PASS: moving conic plus five ordinary degrees", fixed+gain+5*w)
    print("Controls: two-moving and moving-plus-cubic recipes NOT certified")


if __name__ == "__main__":
    verify()
