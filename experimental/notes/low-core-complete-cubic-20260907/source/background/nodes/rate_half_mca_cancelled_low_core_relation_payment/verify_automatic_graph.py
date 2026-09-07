"""Exact small parallel-fiber ledger and interpolation dimension checks."""

from fractions import Fraction

import verify as base
from verify_polynomial_graph import verify as verify_graph


def graph_dimension(j):
    a = j+66972
    return 66973+sum(max(a-i*(j-1), 0) for i in range(8))


def plane_dimension(j):
    a = j+66972
    return sum((i+1)*max(a-i*(j-1), 0) for i in range(8))


def verify():
    verify_graph()
    best, where, steps, intervals = Fraction(0), None, 0, 0
    for left, right, rows in base.rectangles():
        if right < 524289:
            continue
        gain, previous = Fraction(1), 0
        intervals += 1
        for depth, cap, trace in rows:
            assert base.R-left-base.D+depth > 0
            gain += right*cap*Fraction(depth-previous, (previous+1)*(depth+1))*Fraction(
                base.R+4801-left, base.D+4801-depth)
            previous = depth
            steps += len(trace)
        assert previous == 500
        if gain > best:
            best, where = gain, (left, right)
    peak = base.ceil(best)
    assert peak == 895247541220804 and where == (520000, 529999)
    assert intervals == 47 and steps == 12220
    total = 255637082864553899+6*peak
    assert total == 261008568111878723
    assert base.BUDGET-total == 13972159999516364
    assert base.R+169999 < peak
    assert (base.R+2)//2 == 524289
    for j in (4801, 9000, 10000, 10244, 10245):
        assert j+66972-7*(j-1) > 0
        assert graph_dimension(j) == 602777-20*j
        assert plane_dimension(j) == 2411160-132*j
    assert graph_dimension(4801) == 506757
    assert graph_dimension(9000)-(9000+413000) == 777 > 0
    assert graph_dimension(169999) == 370917
    assert plane_dimension(10244) > base.R+10244
    assert plane_dimension(10245) <= base.R+10245
    print("PASS: seven parallel fibers", total, "reserve", base.BUDGET-total)
    print("PASS:", intervals, "tail rectangles;", steps, "LIST transitions")
    print("PASS: strict graph and plane interpolation dimensions; no matrix allocated")


if __name__ == "__main__":
    verify()
