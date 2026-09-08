"""Exact endpoint consequence of the projective jet dimension theorem."""

from fractions import Fraction
from math import prod


def verify():
    s, p, kmax = 11, 2130706433, 169999
    assert p >= kmax
    q = Fraction(1048577, 66973)
    assert q < Fraction(63, 4)
    ceilings = {2: 488464861, 3: 134577053, 5: 1526165771, 9: 96104495052}
    for e, bound in ceilings.items():
        r = (s + e - 1) // e
        value = e**(s-r) * Fraction(63, 4)**r
        assert int(value) == bound
    for e in range(2, 10):
        r = (s + e - 1) // e
        endpoint = 2 if e == 2 else 3 if e == 3 else 5 if e <= 5 else 9
        assert (s + endpoint - 1) // endpoint == r
        assert e**(s-r) <= endpoint**(s-r)
    c = 23067643444721720934
    for k in (4801, kmax):
        resource = Fraction(prod(1048576+k-i for i in range(12)),
                            (67472+k)*prod(67472+i for i in range(1, 11)))
        assert resource <= c
    cap = max(ceilings.values())
    total = c // 501 + 981604 * cap + 134944
    assert total == 140379757249624860
    assert p**6 // 2**128 - total == 134600970861770227
    print("PASS: endpoint caps", ceilings, "total", total,
          "reserve", p**6 // 2**128 - total)


if __name__ == "__main__":
    verify()
