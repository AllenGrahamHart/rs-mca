"""Independent small-integer checks of the cubic obstruction certificate."""

def verify():
    # Count individual (Y,Z) monomials, not total-degree multiplicities.
    def monomials(j, top, shift):
        return sum(max(j+66972-(u+v+shift)*(j-1), 0)
                   for u in range(top+1) for v in range(top+1-u))

    for j in (7117, 8000, 8487, 8655):
        assert monomials(j, 8, 0)-monomials(j, 4, 4)-(1048576+j) > 0
    assert monomials(8656, 8, 0)-monomials(8656, 4, 4)-(1048576+8656) < 0
    # Fixed endpoint rows dominate each actual source, not just a sample.
    for j in (7117, 8000, 8487, 8488, 8655):
        for size, agree, cap in ((600000, j+66972, 132),
                                 (1048576+j-600001, 66973, 50)):
            den = agree**2-size*(j-1)
            num = size*(agree-j+1)
            assert den > 0 and num < (cap+1)*den
    den1, num1 = 74089**2-600000*8654, 600000*(74089-8654)
    den2, num2 = 66973**2-457230*8654, 457230*(66973-8654)
    assert 132*den1 <= num1 < 133*den1
    assert 50*den2 <= num2 < 51*den2
    assert 64 == 8*8
    assert (132+1)*981604 > 129571728
    whole = 255637082864553899+50*981604
    assert whole == 255637082913634099
    assert whole+19343645197760988 == 274980728111395087
    print("PASS: independent monomial, asymmetric row and ledger checks")
    print("PASS: next kernel endpoint and one-unit-small Johnson caps rejected")


if __name__ == "__main__":
    verify()
