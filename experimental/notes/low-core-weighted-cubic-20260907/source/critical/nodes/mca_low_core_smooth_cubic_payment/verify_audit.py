"""Independent integer and small polynomial controls; no geometry certification."""

from math import comb, lcm


def multiply(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def verify():
    denoms = [(67473-t)*t*(t+1) for t in range(1, 501)]
    common = lcm(*denoms)
    numerator = sum((981104+t)*1048577*(common//denom)
                    for t, denom in enumerate(denoms, 1))*3**21
    quotient, remainder = divmod(numerator, common)
    ceiling = quotient+bool(remainder)
    assert ceiling == 159185671413625180
    assert numerator <= ceiling*common
    assert numerator > (ceiling-1)*common
    c = 23067643444721720934
    for j in (4801, 169999):
        assert comb(1048576+j, 12)*67472*67483 <= c*(67472+j)*comb(67483, 12)
    rigid = 31381059609*981604
    assert rigid == 30803773636432836 < 51600000000000000
    assert rigid > (31381059609-1)*981604
    base = 46043200488601452
    assert base+ceiling+rigid+17200000000000000 == 253232645538659468
    assert base+2*rigid+17200000000000000 == 124850747761467124

    # The singular cusp admits an arbitrary cubic polynomial parameter.
    h = [2, -1, 3, 1]
    a = multiply(h, h)
    b = multiply(a, h)
    assert multiply(b, b) == multiply(multiply(a, a), a)
    assert len(a) == 7 and len(b) == 10

    # Coefficients of b^2-a^3-X*a-1 for linear a,b.
    def coefficients(alpha, beta, gamma, delta):
        return [delta**2-beta**3-1,
                2*gamma*delta-3*alpha*beta**2-beta,
                gamma**2-3*alpha**2*beta-alpha,
                -alpha**3]

    for delta in (1, -1):
        assert coefficients(0, 0, 0, delta) == [0, 0, 0, 0]
    assert coefficients(1, 0, 0, 1)[3] != 0
    assert coefficients(0, 0, 1, 1)[2] != 0
    assert coefficients(0, 1, 0, 1)[1] != 0
    assert coefficients(0, 0, 0, 0)[0] != 0
    print("PASS: independent common-denominator gain and binomial resource")
    print("PASS: insufficient ceiling rejected; cusp and moving-j coefficient controls")
    print("Geometry dimensions still require the hand proof")


if __name__ == "__main__":
    verify()
