"""Exact coupled-dimension and projection-height payment certificates."""

from fractions import Fraction


def cap(e, q):
    values = []
    for d in range(12):
        r = (d+e-1)//e
        values.append(e**(22-d-r)*q**r)
    return max(values)


def verify():
    base = 23067643444721720934//501+134944
    labels, budget = 981604, 2130706433**6//2**128
    assert Fraction(1048577-51391, 66973-51391) < 64
    assert Fraction(1048577-51392, 66973-51392) > 64
    cubic = cap(3, 64)
    assert cubic == 3**20*64 == 223154201664
    assert base+labels*cubic == 265092257458790508
    assert budget-base-labels*cubic == 9888470652604579
    assert (66974-2*7117)//3 == 17580
    assert Fraction(1048577-17580, 66973-17580) < 21
    strip = cap(3, 21)
    assert strip == 73222472421
    assert labels*strip == 71875471818343284
    assert base+labels*strip == 117918672306944736
    assert (66973-4801)//2 == 31086
    assert Fraction(1048577-31086, 66973-31086) < 29
    conic = cap(2, 29)
    assert conic == 2**5*29**6 == 19034346272
    assert labels*conic == 18684190437980288 < 34400000000000000
    assert base+labels*conic == 64727390926581740
    assert 117918672306944736+64*labels < 255637082913634099
    print("PASS: moving cubic height 51391, total", base+labels*cubic)
    print("PASS: kernel cubic and conic pair caps", strip, conic)
    print("Affine-singular one-place cubics remain unresolved")


if __name__ == "__main__":
    verify()
