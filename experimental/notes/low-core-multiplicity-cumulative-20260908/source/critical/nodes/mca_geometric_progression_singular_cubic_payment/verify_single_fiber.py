"""Small exact one-list certificate and projective double-fiber controls."""

from collections import defaultdict
from fractions import Fraction


def verify():
    n, h, a = 1058102, 952, 75628
    reduced, collision = a-21*h, 3*h
    denominator = reduced**2-n*collision
    numerator = n*(reduced-collision)
    assert (reduced, collision, denominator, numerator) == (
        55636, 2856, 73425184, 55846623560)
    assert numerator//denominator == 760
    assert a*a-(2*n+5*h)*collision < 0
    lower = int(2**10*3**9*Fraction(1047625, 66021)**3)
    assert lower == 80530893115
    base, labels = 4194116990084347, 981604
    assert base+labels*(760+65) == 4194117799907647
    assert base+labels*(lower+64) == 83243563858163463
    assert 2130706433**6//2**128 > base+labels*(lower+64)

    prime, saw_double, saw_triple = 7, False, False
    for t in range(prime):
        p, b, u, w = pow(t, 4, prime), 0, pow(t, 7, prime), pow(t, 7, prime)
        e, f = (t*p+b) % prime, (t*u+w) % prime
        fibers = defaultdict(list)
        for z in range(prime):
            output = ((z**3+p*z*z+u*z) % prime,
                      (-t*z**3+b*z*z+w*z) % prime)
            fibers[output].append(z)
        for zs in fibers.values():
            assert len(zs) <= (2 if e else 3)
            saw_triple |= len(zs) == 3
            if e and len(zs) > 1:
                saw_double = True
                for z in zs:
                    assert (e*e*z*z+e*f*z+f*f+e*(u*b-p*w)) % prime == 0

    infinity = defaultdict(list)
    for z in range(prime):
        infinity[((z*z+z) % prime, (-z**3+z) % prime)].append(z)
    assert len(infinity[(0, 0)]) == 2
    for zs in infinity.values():
        assert len(zs) <= 2
        if len(zs) == 2:
            for z in zs:
                assert (z*z+z) % prime == 0
    assert saw_double and saw_triple
    assert max(2*5+2*3, 5+8+3, 2*8, 5+7+4) == 16
    print("PASS: 760 nonsingular GP pairs; d=10 paid through 9526")
    print("Finite and infinity controls pass; not a proof of the generic family")


if __name__ == "__main__":
    verify()
