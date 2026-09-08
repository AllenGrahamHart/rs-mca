"""85 interval certificates, at most nine small integer products per endpoint."""

from fractions import Fraction as Q
from math import prod

R, D = 1048576, 67472
BUDGET = 2130706433**6 // 2**128


def resource(s, k):
    return Q(prod(R+k-i for i in range(s+1)),
             (D+k)*prod(D+i for i in range(1, s)))


def child_cap(upper):
    assert upper >= 9
    caps = []
    for s in range(1, 10):
        assert D >= s*(s+1)
        bound = max(resource(s, s), resource(s, upper))*Q(D+s, (s+1)*D)
        caps.append(bound.numerator//bound.denominator)
    assert max(caps) >= R-D+1
    return max(caps)


def factors(j):
    m = D+j
    return (Q((R+j)*(2*R+j+9), m*(2*D+j+9)),
            Q(R+10, D+10)+Q((R+10)*(R-D), m*(m-1)))


def verify():
    rows = []
    previous = 169999
    for left in range(170000, 255000, 1000):
        right = left+999
        assert left == previous+1
        previous = right
        upper = child_cap(right-2)*max(factors(left))
        total = upper.numerator//upper.denominator+R+2*D
        assert total < BUDGET
        rows.append((total, left, right))
    assert len(rows) == 85 and previous == 254999
    assert max(rows) == (270992495272115150, 170000, 170999)
    assert BUDGET-max(rows)[0] == 3988232839279937
    assert R-170000 == 878576 and R-169999 == 878577
    assert 254999-169999 == 85000
    print("PASS:", len(rows), "covering intervals; maximum", max(rows))
    print("PASS: original reserve", BUDGET-max(rows)[0], "; residual J=4801..169999")


if __name__ == "__main__":
    verify()
