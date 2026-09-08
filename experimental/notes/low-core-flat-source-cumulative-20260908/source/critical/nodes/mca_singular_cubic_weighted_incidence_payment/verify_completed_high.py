"""Exact HIGH-weight improvement; no search or geometry computation."""

from fractions import Fraction
from math import prod


def verify():
    excess, c = 67472, 23067643444721720934
    b501 = Fraction(6012*(excess+11-501), excess+11)
    b501 *= prod(Fraction(excess-501+i, excess+i) for i in range(1, 11))
    bernoulli = 6012*(1-Fraction(5511, 67473))
    assert b501 >= bernoulli > 5500
    assert 12*5500 < 67473
    assert 6012*(67473-5511)-5500*67473 == 1414044
    base, labels, budget = c//5500+134944, 981604, 2130706433**6//2**128
    assert base == 4194116990084347
    constant_cap = int(2**11*3**7*Fraction(1048577,66973)**4)
    assert constant_cap == 269141725396
    assert base+labels*(constant_cap+64) == 268384711268522187
    assert base+labels*constant_cap == 268384711205699531
    assert budget-base-labels*(constant_cap+64) == 6596016842872900
    totals = []
    for h in (1300, 1301):
        cap = int(2**7*3**12*Fraction(1048577-h,66973-h)**3)
        totals.append(base+labels*(cap+64))
    assert totals == [274979661292365251, 274991255669975911]
    assert totals[0] < budget < totals[1]
    assert budget-totals[0] == 1066819029836
    print("PASS: HIGH weight 5500; all constant-direction cubics paid")
    print("PASS: d=7 height 1300 paid; next recipe value fails, not an unsafe source")


if __name__ == "__main__":
    verify()
