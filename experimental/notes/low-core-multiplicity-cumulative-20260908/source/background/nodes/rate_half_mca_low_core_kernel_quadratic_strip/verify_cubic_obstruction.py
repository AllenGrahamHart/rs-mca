"""Exact full-kernel, asymmetric Johnson and factor-price certificate."""

from fractions import Fraction


def dimension(j, degree, shift=0):
    a, w = j+66972, j-1
    return sum((i+1)*max(a-(i+shift)*w, 0)
               for i in range(degree+1))


def verify():
    for j in (7117, 8487, 8655, 8656):
        assert dimension(j, 8)-(1048576+j)-dimension(j, 4, 4) == 960724-111*j
    assert 960724-111*8655 == 19
    assert 960724-111*8656 == -92
    k = 8655
    for n, a, cap, expected in (
            (600000, 74089, 132, (296779921, 39261000000)),
            (457230, 66973, 50, (528514309, 26665196370))):
        den, num = a*a-n*(k-1), n*(a-k+1)
        assert (den, num) == expected
        assert num//den == cap and cap*den <= num < (cap+1)*den
    assert 457230 == 1048576+8655-600001
    assert 66973**2-((1048576+8488)//2)*(8488-1) == -268355
    one_pair, w = 981604, 17200000000000000
    assert 132*one_pair == 129571728 < w
    g3 = 159185671413625180
    assert 3*w < g3
    assert 124694999085436416+w < g3
    assert 6*one_pair < g3
    paid = 255637082864553899+50*one_pair
    ordinary = 46043200488601452+g3+64*one_pair
    assert paid == 255637082913634099
    assert ordinary == 205228871965049288 < paid
    assert 2130706433**6//2**128-paid == 19343645197760988
    # Independently retain the already used cubic ceiling in this ledger.
    weighted = sum((Fraction((981104+t)*1048577*3**21,
                             (67473-t)*t*(t+1)) for t in range(1, 501)), Fraction())
    assert g3-1 < weighted <= g3
    print("PASS: degree-three kernel obstruction; asymmetric caps 132 and 50")
    print("PASS: paid branch", paid, "ordinary factors", ordinary)
    print("This check audits the precursor obstruction, not the later full-strip payment")


if __name__ == "__main__":
    verify()
