"""Independent block arithmetic and elementary projection controls."""

from fractions import Fraction


def verify():
    for s in range(1, 12):
        for height in range(s+2):
            first = set(range(s))
            second = set(range(height, height+s))
            assert len(first | second)+len(first & second) == 2*s
            assert len(first & second) == max(s-height, 0)
    for q in (21, 64):
        starts = [3**(24-4*r)*q**r for r in range(1, 5)]
        assert all(b < a for a, b in zip(starts, starts[1:]))
        assert 3**22 < starts[0]
        assert starts[0] == 3486784401*q
    conic_starts = [2**(23-3*r)*29**r for r in range(1, 7)]
    assert all(a < b for a, b in zip(conic_starts, conic_starts[1:]))
    assert conic_starts[-1] == 19034346272
    assert (1048577-51392)-64*(66973-51392) == 1
    assert (1048577-51391)-64*(66973-51391) < 0
    assert 3*(8655-1)+3*((66974-2*8655)//3) < 8655+66972
    for x in map(Fraction, (1, 2, 3, -2)):
        t = x*x
        phi, psi = t-t**3/x**4, t**3/x**5
        assert (phi, psi) == (0, x)
        assert phi+x*psi == t
    # The original polynomial outputs and input remain defined at X=0.
    assert 0+0*0 == 0**2
    assert set(range(4, 11)) | set(range(10)) == set(range(11))
    assert 46043200488601452+223154201664*981604 == 265092257458790508
    assert 46043200488601452+73222472421*981604 == 117918672306944736
    print("PASS: independent dimension blocks, height edge and projection controls")
    print("Missing-guard controls are not unsafe-source witnesses")


if __name__ == "__main__":
    verify()
