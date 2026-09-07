"""Independent rounded valuation-class ledger and existing pencil audit."""

from decimal import Decimal, ROUND_CEILING, localcontext
from math import comb

from verify_rational_pencil_cover_audit import audit as audit_pencils


def audit():
    audit_pencils()
    with localcontext() as context:
        context.prec, context.rounding = 100, ROUND_CEILING
        gains = []
        for e in (2, 3):
            total = Decimal(0)
            for depth in range(500, 0, -1):
                numerator = e**21*(981104+depth)*1048577
                denominator = (67473-depth)*depth*(depth+1)
                total += Decimal(numerator)/Decimal(denominator)
            gains.append(int(total.to_integral_value(rounding=ROUND_CEILING)))
        assert gains == [31914462418027, 159185671413625180]
    c = 23067643444721720934
    for j in (4801, 169999):
        numerator, denominator = 132*comb(1048576+j, 12), (67472+j)*comb(67482, 10)
        assert numerator <= c*denominator
    paid = 46043200488466508
    assert 501*paid <= c < 501*(paid+1)
    w, near, budget = 17200000000000000, 134944, 274980728111395087
    assert 1048577*4 < 63*66973
    assert 2**5*63**6*981604 < 2*w*4**6
    assert 7**5*63**5*981604 < w*4**5
    assert paid+gains[0]+near == 46075114951019479
    assert paid+gains[1]+near == 205228871902226632
    mixed = paid+gains[1]+4*w+near
    assert mixed == 274028871902226632 and budget-mixed == 951856209168455
    assert paid+7*w+near == 166443200488601452
    assert budget*2**128 <= 2130706433**6 < (budget+1)*2**128
    assert paid+2*gains[1]+near > budget
    print("PASS: independent upward-rounded gains, integer graph prices and mixed total")
    print("PASS: existing pencil transition/mutation audits retained; resource charged once")


if __name__ == "__main__":
    audit()
