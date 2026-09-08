"""Independent binomial and integer-only interval audit; no primary import."""

from math import comb


def verify():
    r, d, budget = 1048576, 67472, 274980728111395087
    assert budget == divmod(2130706433**6, 2**128)[0]
    largest = (0, 0, 0)
    seen = 0
    for index in range(85):
        left, right = 170000+1000*index, 170999+1000*index
        upper = 0
        for dimension in range(1, 10):
            assert d >= dimension*(dimension+1)
            for k in (dimension, right-2):
                numerator = dimension*(d+dimension)*comb(r+k, dimension+1)
                denominator = d*(d+k)*comb(d+dimension-1, dimension-1)
                upper = max(upper, numerator//denominator)
        m = d+left
        bal_num, bal_den = (r+left)*(2*r+left+9), m*(2*d+left+9)
        spike_num = (r+10)*(m*(m-1)+(r-d)*(d+10))
        spike_den = (d+10)*m*(m-1)
        if bal_num*spike_den >= spike_num*bal_den:
            count = upper*bal_num//bal_den
        else:
            count = upper*spike_num//spike_den
        total = count+r+2*d
        assert total <= 270992495272115150 < budget
        largest = max(largest, (total, left, right))
        seen += right-left+1
    assert seen == 85000 and largest == (270992495272115150, 170000, 170999)
    assert largest[0] > 270992495272115149  # Reject a one-unit smaller claimed cap.
    assert 85*1000 != 85001  # The certificate cannot silently include J=169999.
    print("PASS: independent binomial/integer audit of", seen, "covered degrees")
    print("PASS: peak", largest, "; smaller cap and uncovered-endpoint claims rejected")


if __name__ == "__main__":
    verify()
