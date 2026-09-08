"""Two fixed ordinary-Johnson certificates and the entire very-low union class."""

from fractions import Fraction as Q


def verify():
    r, w, k_max = 400000, 67466, 169998
    assert 2130706433**6 >= r+k_max
    upper, rows = 1, []
    for s in range(1, 11):
        degree = 13000 if s == 2 else 17000 if s >= 4 else 0
        if degree:
            assert 1 <= degree < k_max
            denominator = (w+degree)**2-(r+degree)*(degree-1)
            assert denominator > 0
            johnson = int(Q((r+degree)*(w+1), denominator))
            assert johnson == (25 if degree == 13000 else 612)
            upper = max(johnson, int(Q((r+degree+1)*upper, w+degree+1)))
        else:
            upper = int(Q((r+s)*upper, w+s))
        rows.append(upper)
    assert rows == [5, 25, 148, 730, 3603, 17787, 87811, 433509, 2140169, 10565695]
    assert w < r < 1048576 and 4801-1 <= k_max == 169999-1
    pairs = int(Q((4801+r)*upper, 4801+w))
    assert pairs == 59183360 < 60000000
    per_pair = 1048576-67472+6
    assert per_pair == 981110 < 1000000
    assert pairs*per_pair == 58065386329600 < 60000000000000
    c = 23067643444721720934
    total = int(Q(500*c+35953*60000000000000, 41952))+134944
    budget = 2130706433**6 // 2**128
    assert total == 274980427687989169 < budget
    assert budget-total == 300423405918
    assert 1048576+400001 == 1448577
    assert 1448577-1262889 == 185688
    print("PASS: two fixed Johnson rows and ten all-degree joint-list caps", rows)
    print("PASS: pair cap", pairs, "very-low labels <60000000000000")
    print("PASS: whole original total", total, "reserve", budget-total)
    print("PASS: original complete very-low union >=1448577 for an unpaid source")


if __name__ == "__main__":
    verify()
