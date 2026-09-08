"""Independent printed-certificate audit using integer inequalities only."""

from math import comb


def verify():
    r, w = 400000, 67466
    caps = [1, 5, 25, 148, 730, 3603, 17787, 87811, 433509, 2140169, 10565695]
    for s in range(1, 11):
        l = 13000 if s == 2 else 17000 if s >= 4 else 0
        if l:
            denominator = (w+l)**2-(r+l)*(l-1)
            numerator = (r+l)*(w+1)
            assert denominator > 0 and 1 <= l < 169998
            j = 25 if l == 13000 else 612
            assert j*denominator <= numerator < (j+1)*denominator
            assert j <= caps[s]
            numerator, denominator = (r+l+1)*caps[s-1], w+l+1
        else:
            numerator, denominator = (r+s)*caps[s-1], w+s
        assert caps[s]*denominator <= numerator < (caps[s]+1)*denominator
    assert 404801*caps[-1] < 60000000*72267
    assert 1048576-67472+6 < 1000000
    assert 2130706433**6 >= 569998
    ceilings = []
    for j in (4801, 169999):
        numerator, denominator = 132*comb(1048576+j, 12), (67472+j)*comb(67482, 10)
        ceilings.append(-(-numerator//denominator))
    assert ceilings == [13195104981505077258, 23067643444721720934]
    numerator = 500*max(ceilings)+35953*60000000000000
    paid, near, denominator = 274980427687989169, 134944, 41952
    assert (paid-near)*denominator <= numerator < (paid-near+1)*denominator
    budget = 2130706433**6 // 2**128
    assert numerator < (budget-near)*denominator
    assert budget-paid == 300423405918
    # A one-unit stronger integer ceiling is not certified by this rounded recipe.
    assert not numerator < (paid-near)*denominator
    print("PASS: independent integer Johnson gates, floors, endpoint resource and payment")


if __name__ == "__main__":
    verify()
