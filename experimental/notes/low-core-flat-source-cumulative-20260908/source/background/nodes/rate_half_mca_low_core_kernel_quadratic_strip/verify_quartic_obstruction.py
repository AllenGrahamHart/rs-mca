"""Exact small kernel/line/cubic/factor ledger for 8656..9526."""

from fractions import Fraction as Q


def verify():
    budget = 2130706433**6//2**128
    base, labels = 23067643444721720934//5500+134944, 981604
    for j in (8656, 9526, 9527):
        a, w, n = j+66972, j-1, 1048576+j
        full = sum((i+1)*(a-i*w) for i in range(9))
        multiples = sum((i+1)*(a-(i+5)*w) for i in range(4))
        assert full-multiples-n == 1295614-136*j
    assert 1295614-136*9526 == 78
    assert 1295614-136*9527 == -58
    assert 66980-7*9526 == 298 and 9526-8656+1 == 871
    for h in (0, 952, 4762, 9525):
        on_n, on_a, on_c = 592000+16*h, 75628, 9525-h
        off_n, off_a, off_c = 466101-16*h, 66973-h, 9525
        assert on_a**2-on_n*on_c == 80794384+439600*h+16*h*h
        assert off_a**2-off_n*off_c == 45770704+18454*h+h*h
        assert off_n > off_a > off_c >= 0 and on_a > on_c >= 0
    assert (744400*75628)//80794384 == 696
    assert 26776570248//45770704 == 585
    large_line = 255637082864553899+585*labels
    assert large_line == 255637083438792239

    c3 = 274979661292365251
    other_totals = []
    for d in range(12):
        if d in (7, 10):
            continue
        h = 0 if d in (0, 11) else 9525//(10//(11-d))
        r = (d+2)//3
        cap = int(2**d*3**(22-d-r)*Q(1048577-h, 66973-h)**r)
        other_totals.append(base+labels*(cap+64))
    assert max(other_totals) == 268384711268522187 < c3
    low_h = int(2**7*3**12*Q(1047277, 65673)**3)
    assert base+labels*(low_h+64) == c3
    assert 241058823023306107 < c3 and 83243563858163463 < c3
    smooth = int(3**21*Q(1048577, 66973))
    assert smooth == 163774741769
    assert base+labels*(smooth+64) == 164956058672324479 < c3
    assert (66974-2*8656)//3 <= 17580
    assert Q(1048577-17580, 66973-17580) < 21
    assert max(3**(22-d-(d+2)//3)*21**((d+2)//3)
               for d in range(12)) == 73222472421
    assert base+labels*(73222472421+64) < c3

    m2 = 2**17*Q(63, 4)**5
    assert m2 == 127031877504
    ratio = Q(1048577, 66973)
    assert int(2**5*ratio**6) == 471360758 < m2
    assert int(2**21*ratio) == 32834505 < m2
    prices = [large_line, base+labels*(4*696+64),
              base+labels*(m2+2*696+64), base+labels*(2*m2+64),
              c3+696*labels, base+labels*(12+64)]
    assert prices[1:5] == [4194119785692539, 128889117504736187,
                            253584115223779835, 274979661975561635]
    assert max(prices) == 274979661975561635 < budget
    assert budget-max(prices) == 1066135833452
    print("PASS: all degree<=4 factor patterns except one geometrically integral quartic")
    print("Paid alternative", int(max(prices)), "reserve", int(budget-max(prices)))
    print("871 J-values narrowed, not closed; unrestricted row/prizes OPEN")


if __name__ == "__main__":
    verify()
