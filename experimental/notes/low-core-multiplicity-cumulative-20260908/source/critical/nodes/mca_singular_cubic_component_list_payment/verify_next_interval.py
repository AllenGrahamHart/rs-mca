"""Constant-size coupled-height certificate for the next d=7 interval."""

from fractions import Fraction


def verify():
    ell = (9526-1-1301)//3
    assert ell == 2741 and (9526-1)//2 == 4762
    a, s = 68274+3*ell, 2102358+7*ell
    den, num = a*a-s*ell, s*(a-ell)
    assert (a, s, den, num) == (76497, 2121545, 36636164, 156476673020)
    assert num//den == 4271 and -1692714+4*ell < 0
    assert 1829262-5*ell > 0 and 2*68274 > 4*ell
    assert a*a-(2097154+4*4762+7*ell)*ell < 0
    lower = int(2**7*3**13*Fraction(1043815, 62211)**2)
    assert lower == 57451183984
    top = 4271*3**16
    assert top == 183852545391
    pairs = top+lower+65
    assert pairs == 241303729440
    total = 4194116990084347+981604*pairs
    assert total == 241058823023306107 < 2130706433**6//2**128
    print("PASS: coupled-height envelope, 4271 per component, next d=7 total", total)


if __name__ == "__main__":
    verify()
