"""Exact small certificate for degree-free rational-pencil cover costs."""

from fractions import Fraction

import verify as base

PRICE = 17200000000000000
CURRENT_KMAX = 169999
NEAR = 134944


def certificate():
    peak, where, last_right, transitions = Fraction(0), None, -1, 0
    for left, right, rows in base.rectangles():
        assert left == last_right + 1
        last_right = right
        gain = Fraction(base.R + base.KMAX)
        previous = 0
        for depth, cap, trace in rows:
            assert previous < depth <= 500
            gain += right * cap * Fraction(depth - previous,
                                           (previous + 1) * (depth + 1))
            previous = depth
            transitions += len(trace)
        assert previous == 500
        if gain > peak:
            peak, where = gain, (left, right)
    assert last_right == base.R - base.D and transitions == 25740
    return peak, where


def verify():
    assert (base.R, base.D, base.S, base.T) == (1048576, 67472, 11, 500)
    assert (base.KMIN, base.KMAX) == (4801, 254999)
    assert base.BUDGET == 274980728111395087
    peak, where = certificate()
    assert base.ceil(peak) == 17111519376310956
    assert where == (90000, 99999) and peak < PRICE
    current = max(base.resource(4801), base.resource(CURRENT_KMAX))
    ceiling = base.ceil(current)
    assert ceiling == 23067643444721720934
    thirteen = ceiling // 501 + 13 * PRICE + NEAR
    mixed = 255637082864553899 + PRICE
    assert thirteen == 269643200488601452
    assert mixed == 272837082864553899
    assert base.BUDGET - thirteen == 5337527622793635
    assert base.BUDGET - mixed == 2143645246841188
    assert base.R + base.KMAX < PRICE
    assert base.R + base.KMAX + ceiling // 501 + NEAR < 255637082864553899
    print("Nonconstant group:", base.ceil(peak), "at", where, "rounded price", PRICE)
    print("Thirteen nonconstant pencils:", thirteen, "reserve", base.BUDGET - thirteen)
    print("Constant plus nonconstant:", mixed, "reserve", base.BUDGET - mixed)
    print("PASS: 25740 ordinary LIST transitions supplied; no row-height gate")


if __name__ == "__main__":
    verify()
