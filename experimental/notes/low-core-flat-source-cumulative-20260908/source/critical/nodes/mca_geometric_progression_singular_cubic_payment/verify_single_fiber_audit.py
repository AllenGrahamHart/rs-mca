"""Independent integer Cauchy exclusion and quadratic-division controls."""


def audit():
    # At 761, the original Cauchy inequality is violated, without division.
    count, agreement, collision, slots = 761, 55636, 2856, 1058102
    assert count*agreement**2 > slots*(agreement+(count-1)*collision)
    assert 760*agreement**2 <= slots*(agreement+759*collision)
    assert 10*952 <= 9526-1 < 10*953
    assert 8656+67472-500-21*952 == agreement
    # Check the exact symbolic remainder coefficients over small rational inputs.
    from fractions import Fraction as Q
    for c, p, u, s in ((1, 0, -1, 0), (2, 3, 5, 7), (-3, 4, -2, 5)):
        t = s*s-Q(p, c)*s+Q(u, c)
        linear = c*(s*s-t)-p*s+u
        assert linear == 0
        singular = (c*s-p)*t
        for z in (-2, 0, 3):
            assert c*z**3+p*z*z+u*z-singular == (c*z+p-c*s)*(z*z+s*z+t)
    lower_num = 2**10*3**9*1047625**3
    lower_den = 66021**3
    cap = 80530893115
    assert cap*lower_den <= lower_num < (cap+1)*lower_den
    assert 4194116990084347+981604*(cap+64) == 83243563858163463
    print("PASS: independent 761-pair exclusion, division identity and finite total")


if __name__ == "__main__":
    audit()
