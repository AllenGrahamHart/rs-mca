"""Exact finite quadratic-graph payment, with no field or polynomial scan."""

from fractions import Fraction

import verify as base


def verify():
    s, r, delta = 11, 6, 32
    assert r == (s+1)//2 and delta == 2**(s-r)
    qlist = Fraction(1048577, 66973)
    assert qlist < 16 and 16*66973-1048577 == 22991
    pairs = delta*16**r
    assert pairs == 536870912 and delta*qlist**r < pairs
    low = pairs*(1048576-67472+500)
    assert low == 526994634702848
    resource = base.ceil(max(base.resource(k) for k in (4801, 169999)))
    assert resource == 23067643444721720934
    total = resource//501 + low + 134944
    assert total == 46570195123304300
    assert base.BUDGET-total == 228410532988090787
    assert 2130706433 % 2 == 1
    print("PASS: at most", pairs, "LOW pairs and", low, "original LOW labels")
    print("PASS: whole original total", total, "reserve", base.BUDGET-total)


if __name__ == "__main__":
    verify()
