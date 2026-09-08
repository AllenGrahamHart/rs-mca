"""Small route check of the corrected unrestricted joint-pair recipe.

An over-budget upper rejects only this certificate, not source safety.
"""

from fractions import Fraction as Q

from verify import R, D, S, T, BUDGET, ENDS, compiler, resource, ceil


def envelope(k, outside):
    union, total = R + k - outside, 2 * D + resource(k) / (T + 1)
    previous = 0
    first_term = None
    for depth in ENDS:
        upper, _ = compiler.compile_cap(R - outside, D - depth, k - 1, S - 1)
        pair_count = Q(union * upper, k + D - depth)
        weight = ((R - D) * Q(depth - previous, (previous + 1) * (depth + 1))
                  + Q(depth - previous, T + 1))
        total += pair_count * weight
        if previous == 0:
            first_term = pair_count * weight
        previous = depth
    assert previous == T
    return ceil(total), ceil(first_term)


def verify():
    for k in (4801, 6000, 20000, 100000, 254999):
        upper, first = envelope(k, 0)
        print("J", k, "U=full domain", "upper", upper,
              "first-depth charge", first, "budget", BUDGET,
              "certificate", "pays" if upper <= BUDGET else "over budget")
    assert envelope(4801, 0)[0] < BUDGET
    assert all(envelope(k, 0)[1] > BUDGET for k in (6000, 20000, 100000, 254999))
    print("The first-depth term alone defeats this unfiltered recipe at four tested residual degrees")


if __name__ == "__main__":
    verify()
