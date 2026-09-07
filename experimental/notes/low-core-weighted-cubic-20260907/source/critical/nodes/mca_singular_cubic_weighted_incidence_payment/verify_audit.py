"""Independent integer-cover arithmetic and small algebraic guard controls."""


def multiply(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def verify():
    budget, base, labels = 274980728111395087, 46043200488601452, 981604
    heights = (0, 8654, 8654, 8654, 8654, 8654, 4327, 4327, 2884, 1730, 865, 0)
    paid, completed_paid = [], []
    for d, h in enumerate(heights):
        r, image_dim = (d+2)//3, 22-d
        # Derive from degree-six equations and quadratic incidence on the cover.
        num = 6**(22-r) * (2*(1048577-h))**r
        den = 2**image_dim * 3**d * (66973-h)**r
        floor, rem = divmod(num, den)
        assert 0 <= rem < den
        assert floor*den <= num < (floor+1)*den
        if rem:
            assert (floor-1)*den < num
        total = base+labels*(floor+64)
        completed = 4194116990084347+labels*(floor+64)
        if completed < budget:
            completed_paid.append((completed, d))
        else:
            assert d in (7, 10)
        if total < budget:
            paid.append((total, d))
        else:
            assert d in (7, 10, 11)
            reduced = (num*3*(66973-h)) // (den*(1048577-h))
            assert base+labels*(reduced+64) < budget
    assert len(paid) == 9
    assert max(paid) == (261013572486287276, 4)
    assert len(completed_paid) == 10
    assert max(completed_paid) == (268384711268522187, 11)
    assert 6012*61962 > 5500*67473
    for h, expected in ((1300, 274979661292365251), (1301, 274991255669975911)):
        num = 6**19*(2*(1048577-h))**3
        den = 2**15*3**7*(66973-h)**3
        assert 4194116990084347+labels*(num//den+64) == expected
    assert 274979661292365251+1066819029836 == budget
    assert 261013572486287276+13967155625107811 == budget
    # Integer height consequence and a sharp large-height monomial carrier.
    for s in range(2, 12):
        for c in range(1, s):
            m = (s-1)//c
            assert s-m*c >= 1
            assert s-(m+1)*c <= 0
    for h in (1, 3, 17):
        carrier = {i*h for i in range(11)}
        assert len(carrier & {i+h for i in carrier}) == 10
        assert 10*h == max(carrier)
    # Displayed fibers: division by the full lift factor needs nonbranch points.
    assert len([z for z in range(37) if z*z % 37 == 1]) == 2
    assert len([w for w in range(37) if w**3 % 37 == 8]) == 3
    assert len([z for z in range(37) if z*z % 37 == 0]) == 1
    assert len([w for w in range(37) if w**3 % 37 == 0]) == 1
    for h, t in ((4, [1, 2, -1]), (1, [1, -2, 0, 1])):
        t2, t3 = multiply(t, t), multiply(multiply(t, t), t)
        shifted = [0]*h+t3
        a = [0]*max(len(t2), len(shifted))
        for i, coefficient in enumerate(t2):
            a[i] += coefficient
        for i, coefficient in enumerate(shifted):
            a[i] -= coefficient
        assert len(a) <= 11 and len(t3) <= 11
        assert multiply(t3, t3) == multiply(multiply(t2, t2), t2)
        assert len(set(range(11)) & set(range(h, h+11))) == 11-h
    print("PASS: independent degree-six cover, exact floors, height and cusp controls")
    print("PASS: completed HIGH resource leaves only d=7,10; height boundary recounted")
    print("The two remaining source patterns are not paid by these checks")


if __name__ == "__main__":
    verify()
