"""Small exact controls for the residual cubic normal form."""

from fractions import Fraction


def verify():
    assert 117918672306944736+64*981604 == 117918672369767392
    assert 117918672369767392 < 255637082913634099
    assert 64+1 == 65
    for a, b in ((Fraction(2), Fraction(3)), (Fraction(5), Fraction(0))):
        lam = a*b
        for tau in map(Fraction, (0, 1, 2, 4)):
            z = (tau*tau-lam)/a
            y = tau*z
            assert y*y == a*z*z*(z+b)
            if z:
                assert y/z == tau
    # Over F_7, the node of y^2=z^2*(z+3) has no F_7 normalization preimage.
    assert 0**2 == 0**2*(0+3)
    assert 3 not in {t*t % 7 for t in range(7)}
    for x in map(Fraction, (1, 2, 3, -2)):
        tau = 1/x
        assert (x*x*tau*tau, x**3*tau**3) == (1, 1)
    print("PASS: rational (2,3) normal form, extra singular pair and pole control")
    print("The remaining source family is not paid by these identities")


if __name__ == "__main__":
    verify()
