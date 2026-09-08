"""Independent upward-rounded ledger and monomial dimension audit."""

from decimal import Decimal, ROUND_CEILING, localcontext

import verify as base
from verify_audit import audit as audit_constant, check_trace


def audit():
    audit_constant()
    peak, last, intervals, first = 0, 519999, 0, None
    with localcontext() as context:
        context.prec, context.rounding = 100, ROUND_CEILING
        for left, right, rows in base.rectangles():
            if right < 524289:
                continue
            assert left == last+1
            last, intervals = right, intervals+1
            gain, previous = Decimal(1), 0
            for depth, cap, trace in rows:
                assert previous < depth <= 500
                assert cap == check_trace(1048576-left, 67472-depth, trace)
                first = first or (left, depth, trace)
                numerator = right*cap*(depth-previous)*(1048576+4801-left)
                denominator = (previous+1)*(depth+1)*(67472+4801-depth)
                gain += Decimal(numerator)/Decimal(denominator)
                previous = depth
            assert previous == 500
            peak = max(peak, int(gain.to_integral_value(rounding=ROUND_CEILING)))
    assert intervals == 47 and last == 981104 and peak == 895247541220804
    assert 261008568111878723-6*peak == 255637082864553899
    assert 274980728111395087-261008568111878723 == 13972159999516364
    left, depth, trace = first
    bad = list(trace)
    rank, degree, cap = bad[-1]
    bad[-1] = rank, degree, cap-1
    try:
        check_trace(1048576-left, 67472-depth, bad)
    except AssertionError:
        pass
    else:
        raise AssertionError("Underpriced tail LIST certificate accepted")
    for j in (4801, 9000, 10000, 10244, 10245, 169999):
        bound = j+66972
        graph = sum(max(bound-a*(j-1)-b*(j-1), 0)
                    for a, b in [(i, 0) for i in range(8)]+[(0, 1)])
        plane = sum(max(bound-(a+b)*(j-1), 0)
                    for a in range(8) for b in range(8-a))
        if j <= 10245:
            assert graph == 602777-20*j and plane == 2411160-132*j
        else:
            assert graph == plane == 370917
        if j == 10244:
            assert plane-(1048576+j) == 132
        if j == 10245:
            assert plane-(1048576+j) == -1
    assert 602777-21*9000-413000 == 777
    # Equal numbers of equations and unknowns need not leave a kernel.
    evaluation = ((1, 0), (1, 1))
    assert evaluation[0][0]*evaluation[1][1]-evaluation[0][1]*evaluation[1][0] == 1
    print("PASS: independent rounded parallel ledger and explicit monomial counts")
    print("Controls: underpriced LIST step rejected; interpolation inequality is strict")


if __name__ == "__main__":
    audit()
