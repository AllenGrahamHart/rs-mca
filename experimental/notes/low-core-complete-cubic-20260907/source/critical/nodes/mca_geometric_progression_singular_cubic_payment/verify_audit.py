"""Independent integer inequalities and tiny projective-fiber controls."""

from collections import Counter


def verify():
    for n, a, h, cap in ((1056575, 74089, 799, 366),
                         (1057231, 74972, 865, 1251)):
        s, c = 2*n+5*h, 3*h
        den = a*a-s*c
        assert den > 0
        # Check the Cauchy inequality directly at successive list sizes.
        assert cap*a*a <= s*(a+(cap-1)*c)
        assert (cap+1)*a*a > s*(a+cap*c)
    assert 74089**2 < (2*1057231+5*865)*(3*865)
    low_num, low_den = 1024*19683*1047712**3, 66108**3
    cap = low_num//low_den
    assert cap*low_den <= low_num < (cap+1)*low_den
    base = 4194116990084347
    assert base+981604*(cap+64) == 82951498428798039
    assert base+981604*(1251+1+64) == 4194118281875211
    assert base*5500 <= 23067643444721720934+134944*5500
    assert (base+1)*5500 > 23067643444721720934+134944*5500

    for valuations, dimension in (((0,), 4), ((3, -3), 4),
                                  ((1, -1), 3), ((2, -2), 3),
                                  ((1, 1, -2), 3), ((1, 1, 1, -3), 3)):
        assert sum(valuations) == 0
        degree = 3+sum(a//3 for a in valuations)
        residues = sum(a%3 for a in valuations)
        assert 3*degree == 9-residues
        assert max(degree+1, 0) == dimension
    # A nodal model has genuine double finite fibers and triple infinity fibers.
    for t in range(7):
        pairs = Counter()
        for z in range(7):
            p = (z*z-1)*(z-t) % 7
            q = ((z*z-1)-t*p) % 7
            pairs[p, q] += 1
        assert max(pairs.values()) == 2 and pairs[0, 0] == 2
    infinity = Counter((0, -z**3 % 7) for z in range(7))
    assert max(infinity.values()) == 3
    roots = [x for x in range(17) if (x-x**3) % 17 == 0]
    assert roots == [0, 1, 16]
    # Three nonzero square fibers under X^2 attain the 3h collision budget.
    collision_roots = [x for x in range(17)
                       if (x*x-1)*(x*x-4)*(x*x-9) % 17 == 0]
    assert len(collision_roots) == 6
    print("PASS: integer Cauchy boundaries, negative valuations and projective fibers")
    print("Geometry and original-source transport require the separate hand proofs")


if __name__ == "__main__":
    verify()
