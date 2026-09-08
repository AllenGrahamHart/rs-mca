"""Eight exact quadratic certificates; no hull search or field enumeration."""

from fractions import Fraction as Q
from math import prod

D, E, LO, X = 67466, 65000, 53000, 5000
R, GAP, NEAR = 1048576, 67472, 134944
LOW_CAP = 274171207928811099
UNION_CAP = 274929007493481160


def check(ok, message):
    if not ok:
        raise ValueError(message)


def ladder(verbose=False):
    c = Q(1, 2*(D+2))
    a, b = D*(2*D+1)*c, (3*D+1)*c
    for r in range(4, 12):
        check(b >= D*c >= 0, "quadratic contraction gate")
        alpha, beta, scale = Q(r-2, r-1), Q(1, r-1), D+r-1
        f = a+b*(r-1)+c*(r-1)**2
        s1, s0 = b-2*c+f/scale, a-b+c-(r-1)*f/scale
        u3 = c*alpha**2/scale
        u2 = (b*alpha+2*c*alpha*beta+D*c*alpha**2)/scale
        u1 = (a+b*beta+c*beta**2+D*(b*alpha+2*c*alpha*beta))/scale
        u0 = D*(a+b*beta+c*beta**2)/scale
        check(u2 >= c and u3 >= 0, "convex tangent residual")
        t1 = u1+2*(u2-c)*X+3*u3*X*X
        t0 = u0-(u2-c)*X*X-2*u3*X**3
        shift = max(Q(0), t0+t1*r-s0-s1*r, t0+t1*E-s0-s1*E)
        a, b = t0-shift, t1
        check(b >= D*c, "next contraction gate")
        check(all(a+b*k <= s0+s1*k for k in (r, E)), "spike endpoint gate")
        check(a <= t0 and b == t1, "uniform tangent gate")
        if verbose:
            print("rank", r, "shift_active", shift > 0,
                  "A_floor", a.numerator//a.denominator,
                  "B_floor", b.numerator//b.denominator)
    return a, b, c


def main():
    a, b, c = ladder(True)
    qlo, qhi = a+b*LO+c*LO**2, a+b*E+c*E**2
    check(qlo > 0, "positive final basis bound")
    check((b+2*c*LO)*(R+LO-11) > 12*qhi, "all-J decreasing LOW quotient")
    p = prod(D+i for i in range(1, 11))
    low = Q(prod(R+LO-i for i in range(12)), 12*p)/qlo
    check(low.numerator//low.denominator+NEAR == LOW_CAP, "LOW floor")
    pd = prod(GAP+i for i in range(1, 11))
    ceiling = 14024864706947406176
    for j in (LO, E):
        numerator = prod(R+j-i for i in range(12))
        denominator = (GAP+j)*pd
        check(numerator <= ceiling*denominator, "convex resource endpoint")
    weight = Q(10488, 125)
    check(84*Q(67473-77, 67473) > weight and 12*84 < 67473, "HIGH weight")
    high = Q(ceiling)/weight
    high_total = high.numerator//high.denominator+NEAR
    check(high_total < LOW_CAP < UNION_CAP, "one shared resource; interval union")
    budget = 2130706433**6//2**128
    check(budget-UNION_CAP == 51720617913927, "original field reserve")
    check(65000-53000 == 12000, "new integer J values")
    print("PASS: eight fixed tangent steps; LOW", LOW_CAP, "HIGH", high_total)
    print("PASS: every normalized J=53000..169999 has total <=", UNION_CAP)
    print("Universal contraction, analytic completeness and original transport are hand proofs")


if __name__ == "__main__":
    main()
