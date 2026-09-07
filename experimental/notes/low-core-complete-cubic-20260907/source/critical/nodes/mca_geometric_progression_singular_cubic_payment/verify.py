"""Exact two-interval list budgets and the complete d=10 payment."""

from fractions import Fraction


def verify():
    budget = 2130706433**6 // 2**128
    resource, near, labels = 23067643444721720934, 134944, 981604
    intervals = ((7117, 7999), (8000, 8655))
    expected = ((414383356, 151782359340, 366),
                (122548519, 153351446699, 1251))
    caps = []
    previous, covered = 7116, 0
    for (lo, hi), row in zip(intervals, expected):
        assert lo == previous+1 and lo <= hi
        h, n, a = (hi-1)//10, 1048576+hi, 66972+lo
        slots, collision = 2*n+5*h, 3*h
        den, num = a*a-slots*collision, slots*(a-collision)
        assert den > 0 and a > collision
        cap = int(Fraction(num, den))
        assert (den, num, cap) == row
        caps.append(cap)
        covered += hi-lo+1
        previous = hi
        print(lo, hi, h, n, a, slots, collision, den, num, cap)
    assert previous == 8655 and covered == 1539
    base = resource//5500+near
    assert base == 4194116990084347
    pairs = max(caps)+1+64
    assert pairs == 1316
    maximal = base+labels*pairs
    assert maximal == 4194118281875211
    assert budget-maximal == 270786609829519876
    smaller_cap = int(2**10*3**9*Fraction(1047712, 66108)**3)
    assert smaller_cap == 80233354159
    smaller = base+labels*(smaller_cap+64)
    assert smaller == 82951498428798039
    assert budget-smaller == 192029229682597048
    assert maximal < smaller < 274979661292365251 < budget
    assert budget-274979661292365251 == 1066819029836
    residual_cap = (budget-base)//labels-64
    assert residual_cap == 275861356574
    assert base+labels*(residual_cap+64) <= budget
    assert base+labels*(residual_cap+65) > budget
    print("PASS: whole d=10 paid; dim-four nonsingular pair cap 1251")
    print("This check pays d=10; the later d=7 component-list payment is separate")


if __name__ == "__main__":
    verify()
