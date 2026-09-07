"""Small exact certificate for common-core-cancelled KoalaBear families."""

import importlib.util
from fractions import Fraction
from math import prod
from pathlib import Path

R, D, S, T = 1048576, 67472, 11, 500
KMIN, KMAX = 4801, 254999
BUDGET = 2130706433**6 // 2**128
ENDS = tuple(range(1, 21)) + (50, 100, 200, 300, 400, 500)
path = Path(__file__).resolve().parents[1] / "list_padded_johnson_dimension_descent" / "compiler.py"
spec = importlib.util.spec_from_file_location("list_compiler", path)
compiler = importlib.util.module_from_spec(spec)
spec.loader.exec_module(compiler)


def resource(k):
    return Fraction(prod(R + k - j for j in range(S + 1)),
                    (D + k) * prod(D + j for j in range(1, S)))


def rectangles():
    for left in range(0, R - D + 1, 10000):
        right = min(left + 9999, R - D)
        rows = []
        for depth in ENDS:
            cap, trace = compiler.compile_cap(R - left, D - depth, KMAX, S - 1)
            rows.append((depth, cap, trace))
        yield left, right, rows


def ceil(value):
    return -(-value.numerator // value.denominator)


def verify():
    peaks = {"constant": (Fraction(0), None), "nonconstant": (Fraction(0), None)}
    count, last_right = 0, -1
    for left, right, rows in rectangles():
        assert left == last_right + 1
        last_right = right
        for k in (KMIN, KMAX):
            totals = {
                "constant": 1 + 2 * D + resource(k) / (T + 1),
                "nonconstant": R + KMAX + 2 * D + resource(k) / (T + 1),
            }
            previous = 0
            for depth, cap, trace in rows:
                assert previous < depth <= T
                weight = Fraction(depth - previous, (previous + 1) * (depth + 1))
                totals["constant"] += right * cap * weight * Fraction(R + k - left, D + k - depth)
                totals["nonconstant"] += right * cap * weight
                previous = depth
                if k == KMIN:
                    count += len(trace)
            assert previous == T
            for branch, total in totals.items():
                assert total < BUDGET, (branch, k, left, ceil(total))
                if total > peaks[branch][0]:
                    peaks[branch] = total, (k, left, right)
    assert last_right == R - D
    cmax = max(resource(KMIN), resource(KMAX))
    maximum_low = R - D + T
    small = maximum_low + (cmax - maximum_low) / (T + 1) + 2 * D
    assert small < BUDGET
    assert ceil(peaks["constant"][0]) == 255637082864553899
    assert peaks["constant"][1] == (4801, 80000, 89999)
    assert ceil(peaks["nonconstant"][0]) == 93265404076279452
    assert peaks["nonconstant"][1] == (254999, 90000, 99999)
    assert ceil(small) == 76153884700948142 and count == 25740
    assert BUDGET - ceil(peaks["constant"][0]) == 19343645246841188
    assert 3 * (D - T) + 2 == 200918
    for branch, (value, where) in peaks.items():
        print(branch, ceil(value), "at", where, "slack", BUDGET - ceil(value))
    print("small union", ceil(small), "transitions", count)
    print("resource endpoints", ceil(resource(KMIN)), ceil(resource(KMAX)))
    print("relation-free union offset", 3 * (D - T) + 2)


if __name__ == "__main__":
    verify()
