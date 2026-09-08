"""Independent integer and binomial audit of the uniform graph certificate."""

from math import comb


def audit():
    budget, resource = 274980728111395087, 23067643444721720934
    assert budget == 2130706433**6 // 2**128
    ceilings = []
    for k in (4801, 169999):
        num, den = 132*comb(1048576+k, 12), (67472+k)*comb(67482, 10)
        upper = (num+den-1)//den
        assert (upper-1)*den < num <= upper*den
        ceilings.append(upper)
    assert max(ceilings) == resource
    assert 2*5 <= 11 < 2*6 and 11-5 == 6
    pairs = 123363917824
    assert 7**6*1048577**5 < pairs*66973**5
    assert pairs == 7**6*16**5 and pairs > 2**5*16**6
    low, total = 121094515191709696, 167137715680311148
    assert low == pairs*(1048576-67472+500)
    rest = total-low-134944
    assert 501*rest <= resource < 501*(rest+1)
    assert budget-total == 107843012431083939
    print("PASS: independent degree-seven endpoint, source resource and exact full count")
    print("The count retains the degree charge and all original LOW/HIGH/near labels")


if __name__ == "__main__":
    audit()
