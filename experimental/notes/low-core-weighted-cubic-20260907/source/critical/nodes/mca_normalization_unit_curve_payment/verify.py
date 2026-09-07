"""Tiny exact identity controls and cubic gain; not a dimension prover."""

from fractions import Fraction


def multiply(a, b):
    result = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result


def verify():
    for t in map(Fraction, (1, 2, 3, 5, -2)):
        u = (1+t*t)/(t*(1+t))
        v = (1+t*t)/(1+t)
        w = 1/t
        assert u*v*(u+v) == u*u+v*v
        assert t*t-v*t+1-v == 0
        assert w*w-u*w+1-u == 0
        assert v/u == t
    # A nodal one-boundary cubic has a large polynomial parameter family.
    h = [1, -1, 2, 1]
    a = multiply(h, h)
    a[0] -= 1
    b = multiply(h, a)
    a_plus_one = list(a)
    a_plus_one[0] += 1
    assert multiply(b, b) == multiply(multiply(a, a), a_plus_one)
    assert len(a) == 7 and len(b) == 10
    total = 3**21*sum((Fraction((981104+t)*1048577,
                               (67473-t)*t*(t+1))
                      for t in range(1, 501)), Fraction())
    cap = 159185671413625180
    assert cap-1 < total <= cap
    assert 23067643444721720934//501+134944+cap == 205228871902226632
    print("PASS: normalization-unit identities and nodal one-boundary control")
    print("PASS: cubic weighted ceiling", cap, "; geometry requires the hand proof")


if __name__ == "__main__":
    verify()
