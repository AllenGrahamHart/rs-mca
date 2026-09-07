"""Small exact checks of the smooth-cubic payment, not a geometry prover."""

from fractions import Fraction
from math import prod


def verify():
    p, r, d, tmax = 2130706433, 1048576, 67472, 500
    c, w = 23067643444721720934, 17200000000000000
    budget = p**6 // 2**128
    assert p > 3 and budget == 274980728111395087
    for j in (4801, 169999):
        resource = Fraction(prod(r+j-i for i in range(12)),
                            (d+j)*prod(d+i for i in range(1, 11)))
        assert resource <= c
    z = sum((Fraction((r-d+t)*(r+1), (d+1-t)*t*(t+1))
             for t in range(1, tmax+1)), Fraction())
    weighted = 3**21*z
    g1 = -(-weighted.numerator // weighted.denominator)
    g0 = 3**22*(r-d+tmax)
    assert g1 == 159185671413625180
    assert g0 == 30803773636432836 and g0 < 3*w
    base = c // 501 + 134944
    assert base == 46043200488601452
    assert base+g1 == 205228871902226632
    assert base+g0 == 76846974125034288
    assert budget-base-g0 == 198133753986360799
    totals = {
        "one smooth cubic, four ordinary degrees": base+g1+4*w,
        "one moving conic, five ordinary degrees": base+124694999085436416+5*w,
        "two nonconstant-j cubics, one nonconstant line": base+2*g0+w,
        "smooth cubic, nonconstant-j cubic, nonconstant line": base+g1+g0+w,
    }
    assert totals == {
        "one smooth cubic, four ordinary degrees": 274028871902226632,
        "one moving conic, five ordinary degrees": 256738199574037868,
        "two nonconstant-j cubics, one nonconstant line": 124850747761467124,
        "smooth cubic, nonconstant-j cubic, nonconstant line": 253232645538659468,
    }
    assert max(totals.values()) < budget
    assert base+2*g1 > budget
    assert base+g1+124694999085436416 > budget
    print("PASS: smooth cubic gain", g1, "rigid gain", g0)
    print("PASS: whole-source totals", totals)


if __name__ == "__main__":
    verify()
