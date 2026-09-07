"""Independent direct Cauchy certificate and tiny exceptional-fiber checks."""

from collections import Counter


def verify():
    a0, s0, ell_max, forbidden = 68274, 2114462, 2451, 316
    # Direct Cauchy violation at M=316; independent of the quotient derivative.
    b_max = 1896235+4327
    assert 2*(forbidden-3)*a0-b_max-3*(forbidden-1)*ell_max > 0
    linear = (6*forbidden-7)*a0-(forbidden+2)*s0
    quadratic = 9*forbidden-7*(forbidden+2)
    assert quadratic == 618 and linear+2*quadratic*ell_max < 0
    a, s = a0+3*ell_max, s0+7*ell_max
    assert forbidden*a*a-s*(a+(forbidden-1)*ell_max) == 387655416 > 0
    assert 315*a*a-s*(a+314*ell_max) < 0

    top = 43046721
    assert top*27*27 == 3**22
    num = 6**20*(2*1044250)**2
    den = 2**15*3**7*62646**2
    low, rem = divmod(num, den)
    assert low == 56703328989 and 0 <= rem < den
    total = 4194116990084347+981604*(315*top+low+65)
    assert total == 73164604161759423
    assert total+201816123949635664 == 274980728111395087

    exceptional = Counter((z**3-z) % 7 for z in range(7))
    assert exceptional[0] == 3 and max(exceptional.values()) == 3
    constant = Counter((0, 0) for z in range(7))
    assert constant[0, 0] == 7 > 3
    assert constant[1, 0] == 0
    for x in range(1, 7):
        fibers = Counter()
        for z in range(7):
            p = (z*z-1)*z % 7
            q = x*(z*z-1)-x*p
            fibers[p, q % 7] += 1
        assert max(fibers.values()) <= 2
    print("PASS: direct 316 exclusion, original-degree component budget, lower lift budget")
    print("PASS: real triple and constant fibers; no universal geometry certification")


if __name__ == "__main__":
    verify()
