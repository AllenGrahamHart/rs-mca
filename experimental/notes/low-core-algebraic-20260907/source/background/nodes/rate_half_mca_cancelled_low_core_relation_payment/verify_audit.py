"""Independent integer-transition and directed-rounding certificate audit."""

from decimal import Decimal, ROUND_CEILING, localcontext
from math import comb

import verify as primary


def check_trace(r, w, trace):
    prior = 1
    assert len(trace) == 10
    for expected_rank, (rank, degree, cap) in enumerate(trace, 1):
        assert rank == expected_rank and cap >= 1
        if degree == 0:
            numerator, denominator = (r + rank) * prior, w + rank
            assert cap * denominator <= numerator < (cap + 1) * denominator
        else:
            assert 1 <= degree <= 254999
            denominator = w * w + r - (r - 2 * w - 1) * degree
            assert denominator > 0
            upper = (r + degree) * (w + 1) // denominator
            if degree < 254999:
                upper = max(upper, (r + degree + 1) * prior // (w + degree + 1))
            assert cap == upper
        prior = cap
    return prior


def rejects(call):
    try:
        call()
    except AssertionError:
        return
    raise AssertionError("mutation accepted")


def audit():
    assert (primary.R, primary.D, primary.S, primary.T) == (1048576, 67472, 11, 500)
    assert (primary.KMIN, primary.KMAX) == (4801, 254999)
    peak = [0, 0]
    count, previous_right, first = 0, -1, None
    with localcontext() as context:
        context.prec, context.rounding = 100, ROUND_CEILING
        resources = {}
        for k in (4801, 254999):
            numerator = 132 * comb(1048576 + k, 12)
            denominator = (67472 + k) * comb(67482, 10)
            fraction = primary.resource(k)
            assert numerator * fraction.denominator == denominator * fraction.numerator
            resources[k] = Decimal(numerator) / Decimal(denominator)
        for left, right, rows in primary.rectangles():
            assert left == previous_right + 1 and left <= right <= 981104
            previous_right, count = right, count + 1
            totals = {k: [Decimal(134945) + resources[k] / Decimal(501),
                          Decimal(1303575 + 134944) + resources[k] / Decimal(501)]
                      for k in (4801, 254999)}
            previous = 0
            for depth, cap, trace in rows:
                assert previous < depth <= 500
                assert cap == check_trace(1048576 - left, 67472 - depth, trace)
                first = first or trace
                numerator = right * cap * (depth - previous)
                denominator = (previous + 1) * (depth + 1)
                for k in totals:
                    totals[k][0] += Decimal(numerator * (1048576 + k - left)) / Decimal(denominator * (67472 + k - depth))
                    totals[k][1] += Decimal(numerator) / Decimal(denominator)
                previous = depth
            assert previous == 500
            for values in totals.values():
                for branch, value in enumerate(values):
                    upper = int(value.to_integral_value(rounding=ROUND_CEILING))
                    assert upper < 2130706433**6 // 2**128
                    peak[branch] = max(peak[branch], upper)
        assert count == 99 and previous_right == 981104
        assert peak == [255637082864553899, 93265404076279452]
        small = Decimal(981604 + 134944) + (max(resources.values()) - Decimal(981604)) / Decimal(501)
        assert int(small.to_integral_value(rounding=ROUND_CEILING)) == 76153884700948142
    bad = list(first)
    rank, degree, upper = bad[-1]
    bad[-1] = rank, degree, upper - 1
    rejects(lambda: check_trace(1048576, 67471, bad))
    bad = list(first)
    bad[0] = 1, 254999, 1
    rejects(lambda: check_trace(1048576, 67471, bad))
    print("PASS: independent resource, transitions and rounded envelopes", peak)
    print("Two invalid certificate mutations rejected")


if __name__ == "__main__":
    audit()
