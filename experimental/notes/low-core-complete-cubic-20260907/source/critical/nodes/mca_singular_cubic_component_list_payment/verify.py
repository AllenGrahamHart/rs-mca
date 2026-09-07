"""Constant-size exact component/list budget; no source enumeration."""

from fractions import Fraction


def verify():
    h_min, h_max, j_max = 1301, 4327, 8655
    ell_max = (j_max-1-h_min)//3
    assert ell_max == 2451
    a0, s0 = 66973+h_min, 2097154+4*h_max
    assert (a0, s0) == (68274, 2114462)
    linear = 6*a0-s0
    assert linear == -1704818 and linear+4*ell_max < 0
    a, slots = a0+3*ell_max, s0+7*ell_max
    den, num = a*a-slots*ell_max, slots*(a-ell_max)
    assert (a, slots, den, num) == (75627, 2131619, 494844960, 155983351944)
    assert den > 0 and int(Fraction(num, den)) == 315
    assert 1896235-2*ell_max+h_min > 0
    components = 3**22 // (3**3*3**3)
    assert components == 43046721
    lower = int(2**7*3**13*Fraction(1044250, 62646)**2)
    assert lower == 56703328989
    top = 315*components
    assert top == 13559717115
    pairs = top+lower+1+64
    assert pairs == 70263046169
    resource, near, labels = 23067643444721720934, 134944, 981604
    total = resource//5500+near+labels*pairs
    budget = 2130706433**6//2**128
    assert total == 73164604161759423
    assert budget-total == 201816123949635664
    strip = max(274979661292365251, total)
    assert strip == 274979661292365251 < budget
    assert budget-strip == 1066819029836
    assert 8655-7117+1 == 1539 and 7116+1 == 7117
    assert 960724-111*8655 > 0 > 960724-111*8656
    print("PASS: 315 per top component, 3^16 components, all lower components paid")
    print("d=7 total", total, "full normalized 7117..8655 total", strip)
    print("Unpaid normalized range starts at 8656; unrestricted row/prizes open")


if __name__ == "__main__":
    verify()
