"""Independent binomial and integer-bound audit of the quadratic payment."""

from math import comb


def audit():
    q, budget = 2130706433**6, 274980728111395087
    assert budget*2**128 <= q < (budget+1)*2**128
    resource = 23067643444721720934
    ceilings = []
    for k in (4801, 169999):
        numerator = 132*comb(1048576+k, 12)
        denominator = (67472+k)*comb(67482, 10)
        upper = (numerator+denominator-1)//denominator
        assert (upper-1)*denominator < numerator <= upper*denominator
        ceilings.append(upper)
    assert max(ceilings) == resource
    assert 2*6-1 == 11 and 2**(11-6) == 32
    pairs = 536870912
    assert 32*1048577**6 < pairs*66973**6
    assert pairs == 32*16**6
    low, total = 526994634702848, 46570195123304300
    assert low == pairs*981604
    residual = total-low-134944
    assert 501*residual <= resource < 501*(residual+1)
    assert budget-total == 228410532988090787
    assert 32*16**6 > 16**6
    print("PASS: independent field budget, endpoint ceilings and pair-to-label arithmetic")
    print("PASS: full-source total", total, "retains degree=32 and near=134944")


if __name__ == "__main__":
    audit()
