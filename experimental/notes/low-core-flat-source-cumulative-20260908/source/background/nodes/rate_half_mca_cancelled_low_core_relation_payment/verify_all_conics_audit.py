"""Independent integer audit of conic prices and the shared resource."""

from math import comb


def audit():
    q, budget = 2130706433**6, 274980728111395087
    assert budget*2**128 <= q < (budget+1)*2**128
    c = 23067643444721720934
    for j in (4801, 169999):
        numerator = 132*comb(1048576+j, 12)
        denominator = (67472+j)*comb(67482, 10)
        assert numerator <= c*denominator
    assert 4*1048577 < 63*66973
    pairs = 128*63**5
    assert pairs == 127031877504
    assert 2**17*63**5 == pairs*4**5
    low = pairs*(1048576-67472+500)
    paid = 46043200488466508
    assert 501*paid <= c < 501*(paid+1)
    near, w = 2*67472, 17200000000000000
    original = paid+low+near
    mixed = original+5*w
    assert original == 170738199574037868
    assert mixed == 256738199574037868 and budget-mixed == 18242528537357219
    assert 2**5*63**6*981604 < 2*w*4**6
    assert 7**5*63**5*981604 < w*4**5
    assert paid+2*low+3*w+near > budget
    assert 2*3-3//2 == 5 and 2*11-11//2 == 17
    print("PASS: independent integer pair/gain/resource ledger and graph per-degree prices")
    print("The parameter is not used as a LIST coordinate or degree bound")


if __name__ == "__main__":
    audit()
