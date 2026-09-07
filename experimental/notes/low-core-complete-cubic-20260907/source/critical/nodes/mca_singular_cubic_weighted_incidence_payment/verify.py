"""Tiny exact weighted-cubic price table; geometry is proved separately."""

from fractions import Fraction


CAPS = (31381059609, 124350118988, 82900079325, 55266719550,
        218999078992, 145999385995, 85054993483, 315063751327,
        196986237004, 124890780289, 423859179691, 269141725396)
HEIGHTS = (None, 8654, 8654, 8654, 8654, 8654,
           4327, 4327, 2884, 1730, 865, 0)


def height(d):
    if d == 0:
        return None
    if d == 11:
        return 0
    return 8654 // (10 // (11-d))


def cap(d, r):
    h = height(d)
    q = Fraction(1048577-(h or 0), 66973-(h or 0))
    assert q >= 3
    return int(2**d * 3**(22-d-r) * q**r)


def verify():
    budget = 2130706433**6 // 2**128
    base = 23067643444721720934 // 501 + 134944
    labels = 981604
    unpaid, paid_totals = [], []
    for d in range(12):
        r = (d+2)//3
        assert height(d) == HEIGHTS[d]
        value = cap(d, r)
        assert value == CAPS[d]
        total = base+labels*(value+64)
        print(d, r, height(d), value, total)
        if total > budget:
            unpaid.append((d, r))
        else:
            paid_totals.append(total)
    assert unpaid == [(7, 3), (10, 4), (11, 4)]
    assert max(paid_totals) == 261013572486287276
    assert budget-max(paid_totals) == 13967155625107811
    assert [base+labels*(cap(d, r-1)+64) for d, r in unpaid] == [
        101703415100342464, 124800581927315144, 96665052831852940]
    assert 255637082913634099 < max(paid_totals) < budget
    print("PASS: baseline raw-resource table; completed-HIGH refinement is checked separately")


if __name__ == "__main__":
    verify()
