"""Uniform exact degree endpoint for polynomial-coefficient graph payments."""

from fractions import Fraction

import verify as base


def verify():
    qlist = Fraction(1048577, 66973)
    assert qlist < 16
    quadratic = 2**5*16**6
    higher = 7**6*16**5
    assert quadratic == 536870912 < higher == 123363917824
    assert 7 < 2130706433
    assert all(7**6 >= e**6 for e in range(3, 8))
    low = higher*981604
    resource = base.ceil(max(base.resource(k) for k in (4801, 169999)))
    assert resource == 23067643444721720934
    total = resource//501+low+134944
    assert low == 121094515191709696
    assert total == 167137715680311148
    assert base.BUDGET-total == 107843012431083939
    degree_eight = resource//501+8**6*16**5*981604+134944
    assert degree_eight == 315864453456459628 > base.BUDGET
    print("PASS: one dimension/degree theorem covers graph degrees 2 through 7")
    print("PASS: whole original total", total, "reserve", base.BUDGET-total)
    print("Degree-eight rounded recipe is NOT certified:", degree_eight)


if __name__ == "__main__":
    verify()
