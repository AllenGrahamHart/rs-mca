"""Independent monomial counting, integer gates and hostile controls."""


def reject(call):
    try:
        call()
    except AssertionError:
        return
    raise AssertionError("invalid mutation accepted")


def gap(j, degree=10, divisor_degree=3):
    full = multiple = 0
    for y in range(degree + 1):
        for z in range(degree + 1 - y):
            full += max(0, j + 66972 - (y + z) * (j - 1))
    for y in range(degree - divisor_degree + 1):
        for z in range(degree - divisor_degree + 1 - y):
            multiple += max(0, j + 66972 - (y + z + divisor_degree) * (j - 1))
    return full - multiple - (1048576 + j)


def strip_gate(endpoint):
    assert 4801 <= endpoint and gap(endpoint) > 0


def list_gate(cap):
    a, n, pair_overlap = 66973, 527846, 7115
    den, num = a * a - n * pair_overlap, n * (a - pair_overlap)
    assert den > 0 and cap * den <= num < (cap + 1) * den


def bound_gate(bound, exceptions):
    assert exceptions >= 100
    assert bound >= 272837082864553899 + exceptions * 981604
    assert bound <= pow(2130706433, 6) // pow(2, 128)


def audit():
    assert gap(4801) == 312613 and gap(7116) == 88
    assert gap(7117) == -47 and gap(4802) - gap(4801) == -135
    strip_gate(7116)
    list_gate(43)
    bound_gate(272837082962714299, 100)
    reject(lambda: strip_gate(7117))
    reject(lambda: list_gate(42))
    reject(lambda: bound_gate(272837082962714298, 100))
    reject(lambda: bound_gate(272837082962714299, 99))
    assert 255637082864553899 + 144 * 981604 == 255637083005904875
    assert 274980728111395087 - 272837082962714299 == 2143645148680788
    print("PASS: independent monomial and integer audit; four mutations rejected")


if __name__ == "__main__":
    audit()
