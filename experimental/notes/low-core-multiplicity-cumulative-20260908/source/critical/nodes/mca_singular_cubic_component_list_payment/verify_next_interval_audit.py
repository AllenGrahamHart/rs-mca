"""Independent cross-product exclusions and degree-budget arithmetic."""


def audit():
    count, agreement, collision, slots = 4272, 76497, 2741, 2121545
    assert count*agreement**2 > slots*(agreement+(count-1)*collision)
    assert 4271*agreement**2 <= slots*(agreement+4270*collision)
    assert count*(agreement**2-slots*collision)-slots*(agreement-collision) == 33019588
    components = 3**16
    assert components*27*27 == 3**22
    cap, denominator = 57451183984, 62211**2
    numerator = 2**7*3**13*1043815**2
    assert cap*denominator <= numerator < (cap+1)*denominator
    assert 981604*(4271*components+cap+65)+4194116990084347 == 241058823023306107
    # Derivative numerator at S=4a+b, retaining all common parameters.
    for a, ell in ((68280, 2), (76497, 2741)):
        b = 1829262-5*ell
        n = (4*a+b)*(a-ell)
        d = a*a-(4*a+b)*ell
        derivative = (8*a+b-4*ell)*d-n*(2*a-4*ell)
        expected = -(b+12*ell)*a*a-6*b*ell*a-b*b*ell
        assert derivative == expected < 0 and d > 0
    print("PASS: independent 4272-pair exclusion and coupled derivative identity")


if __name__ == "__main__":
    audit()
