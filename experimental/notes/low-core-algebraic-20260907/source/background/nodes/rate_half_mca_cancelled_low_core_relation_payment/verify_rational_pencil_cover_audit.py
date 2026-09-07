"""Independent transition checks and upward-rounded group-cost audit."""

from decimal import Decimal, ROUND_CEILING, localcontext
from math import comb

import verify as base
from verify_audit import audit as audit_constant, check_trace


def audit():
    audit_constant()
    peak, last_right, count, first = 0, -1, 0, None
    with localcontext() as context:
        context.prec, context.rounding = 100, ROUND_CEILING
        resource = max(Decimal(132 * comb(1048576 + k, 12))
                       / Decimal((67472 + k) * comb(67482, 10))
                       for k in (4801, 169999))
        resource_ceiling = int(resource.to_integral_value(rounding=ROUND_CEILING))
        assert resource_ceiling == 23067643444721720934
        for left, right, rows in base.rectangles():
            assert left == last_right + 1 and left <= right <= 981104
            last_right, count = right, count + 1
            cost, previous = Decimal(1303575), 0
            for depth, cap, trace in rows:
                assert previous < depth <= 500
                assert cap == check_trace(1048576 - left, 67472 - depth, trace)
                first = first or trace
                cost += Decimal(right * cap * (depth - previous)) / Decimal(
                    (previous + 1) * (depth + 1))
                previous = depth
            assert previous == 500
            peak = max(peak, int(cost.to_integral_value(rounding=ROUND_CEILING)))
        assert count == 99 and last_right == 981104
        assert peak == 17111519376310956 < 17200000000000000
    q, budget, near, price = 2130706433**6, 274980728111395087, 134944, 17200000000000000
    assert budget * 2**128 <= q < (budget + 1) * 2**128
    thirteen, mixed = 269643200488601452, 272837082864553899
    paid_resource = thirteen - 13 * price - near
    assert 501 * paid_resource <= resource_ceiling < 501 * (paid_resource + 1)
    assert mixed - price == 255637082864553899
    assert budget - thirteen == 5337527622793635
    assert budget - mixed == 2143645246841188
    assert 14 * price + resource_ceiling // 501 + near > budget
    bad = list(first)
    rank, degree, cap = bad[-1]
    bad[-1] = rank, degree, cap - 1
    try:
        check_trace(1048576, 67471, bad)
    except AssertionError:
        pass
    else:
        raise AssertionError("Underpriced LIST certificate accepted")
    print("PASS: independent rounded group cost", peak, "and both full-source totals")
    print("Controls: underpriced trace rejected; fourteen-line recipe NOT certified")


if __name__ == "__main__":
    audit()
