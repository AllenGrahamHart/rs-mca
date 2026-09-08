"""Independent integer/binomial replay; no import of the primary certificate."""

from math import comb


def ceil_div(a, b):
    return -(-a // b)


def verify():
    r, d = 1048576, 67472
    values = [ceil_div(132*comb(r+j, 12), (d+j)*comb(d+10, 10))
              for j in (4801, 169999)]
    assert values == [13195104981505077258, 23067643444721720934]
    c = max(values)
    a_num, a_den, high, near = 12*d, d+11, 501, 134944
    delta = high*a_den-a_num
    numerator = c*a_den+delta*156765527508668296
    denominator = high*a_den
    total = numerator//denominator+near
    assert total == 199054477120667562
    assert (total-near)*denominator <= numerator < (total-near+1)*denominator
    budget = 2130706433**6 // 2**128
    assert budget-total == 75926250990727525
    mass_num = (high*(budget-near+1)-c)*a_den
    low = ceil_div(mass_num, delta)
    assert low == 234554688218295064
    assert (low-1)*delta < mass_num <= low*delta
    # Reject a one-unit stronger floor claim and an insufficient total ceiling.
    assert not low*delta < mass_num
    assert not numerator < (total-near)*denominator
    print("PASS: independent binomial/integer endpoints, total and LOW mass floor")


if __name__ == "__main__":
    verify()
