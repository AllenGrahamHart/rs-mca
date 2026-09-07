"""Exact, constant-space checks of the full-kernel strip theorem."""

from fractions import Fraction
from math import prod

R, D, T = 1048576, 67472, 500
LOW, HIGH = 4801, 7116
BUDGET = 2130706433**6 // 2**128
PAIR_LABELS = R - D + T
CONSTANT = 255637082864553899
MIXED = 272837082864553899


def dimensions(j):
    a, w = j + D - T, j - 1
    return (sum((i + 1) * max(a - i * w, 0) for i in range(11)),
            sum((i + 1) * max(a - (i + 3) * w, 0) for i in range(8)))


def verify():
    for j in (LOW, HIGH, HIGH + 1):
        full, multiples = dimensions(j)
        assert j + D - T - 10 * (j - 1) > 0
        assert full - (R + j) - multiples == 960748 - 135 * j
    assert dimensions(HIGH)[0] - (R + HIGH) - dimensions(HIGH)[1] == 88
    assert dimensions(HIGH + 1)[0] - (R + HIGH + 1) - dimensions(HIGH + 1)[1] == -47
    n, a, k = (R + HIGH) // 2, D - T + 1, HIGH
    denominator = a * a - n * (k - 1)
    numerator = n * (a - k + 1)
    assert (denominator, numerator) == (729758439, 31595805868)
    assert numerator // denominator == 43
    assert PAIR_LABELS == 981604
    resource = max(Fraction(prod(R + j - i for i in range(12)),
                            (D + j) * prod(D + i for i in range(1, 11)))
                   for j in (LOW, 169999))
    assert resource <= 23067643444721720934
    base = 23067643444721720934 // 501 + 2 * D
    assert base == 46043200488601452
    assert base + 2 * 17200000000000000 == 80443200488601452
    exceptional = 100 * PAIR_LABELS
    total = MIXED + exceptional
    candidates = (base + exceptional, CONSTANT + exceptional,
                  170738199574037868 + exceptional,
                  base + 101 * PAIR_LABELS,
                  base + 2 * 17200000000000000 + exceptional,
                  261008568111878723 + exceptional,
                  CONSTANT + 144 * PAIR_LABELS)
    assert max(candidates) < total
    assert CONSTANT + 144 * PAIR_LABELS == 255637083005904875
    assert total == 272837082962714299
    assert BUDGET - total == 2143645148680788
    assert HIGH - LOW + 1 == 2316
    print("PASS: 2316 normalized dimensions; upper", total,
          "reserve", BUDGET - total, "next endpoint test", -47)


if __name__ == "__main__":
    verify()
