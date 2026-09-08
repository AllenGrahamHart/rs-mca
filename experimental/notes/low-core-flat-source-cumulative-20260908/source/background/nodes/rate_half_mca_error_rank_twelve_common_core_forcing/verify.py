"""Exact rational small-core payment and all 4799 large-core Johnson rows."""

from fractions import Fraction as F
from math import isqrt


R, D_SLACK = 1048576, 67472
BUDGET = 2130706433**6 // 2**128
JOHNSON_CAP = 10**17


def ceil_sqrt_ratio(num, den):
    root = isqrt(num // den)
    return root + (den*root*root < num)


def johnson_certificate(k):
    n, a, degree = R+k, D_SLACK+k, k-1
    assert 2 <= k <= 4800 and 2 <= k < n and 0 <= a <= n
    assert a*a > n*degree
    low, high = 0, 1
    def gate(t):
        return 4*t*t*a*a >= (2*t+1)**2*n*degree
    while not gate(high):
        high *= 2
    while high-low > 1:
        mid = (high+low)//2
        if gate(mid):
            high = mid
        else:
            low = mid
    t = high
    assert gate(t) and (t == 1 or not gate(t-1))
    sigma = 2*t+1
    ell = ceil_sqrt_ratio(sigma*sigma*n*degree, 4)
    y = ceil_sqrt_ratio(sigma*sigma*n, 4*degree)
    z = max(y, (sigma*sigma*n + 12*degree - 1)//(12*degree))
    bound = 2*ell*y*y*z + (n-a+1)*y + z
    assert bound <= JOHNSON_CAP
    return bound


def main():
    assert BUDGET == 274980728111395087
    s, k, u = 11, 255000, 10755802499540570
    n, m, h = R+k, D_SLACK+k, k-s+2
    balanced = F(n*(2*n-h), m*(2*m-h))
    spike = F(R+s-1, D_SLACK+s-1) + F((R+s-1)*(R-D_SLACK), m*(m-1))
    assert balanced == F(383277578467, 15718615477)
    assert spike == F(11153988094749115, 438581833089399) > balanced
    value = u*spike
    bound = value.numerator//value.denominator
    assert bound == 273540953997732057
    total = bound + R + 2*D_SLACK
    assert total == 273540953998915577 < BUDGET
    assert BUDGET-total == 1439774112479510
    assert R-k == 793576 and R-4800 == 1043776
    count = 0
    for child_k in range(2, 4801):
        johnson_certificate(child_k)
        count += 1
    assert count == 4799
    assert 4070947 < JOHNSON_CAP and R-D_SLACK+1 < JOHNSON_CAP
    assert JOHNSON_CAP + 2*D_SLACK == 100000000000134944 < BUDGET
    assert R-793577 == 254999 and R-1043775 == 4801
    assert johnson_certificate(4800) == 70921548248995035
    print(f'PASS: exact small-core total {total}, slack {BUDGET-total}; '
          f'all {count} large-core rows have valid Johnson certificates <=10^17; '
          'intermediate core range and ranks >=13 remain unproved')


if __name__ == '__main__':
    main()
