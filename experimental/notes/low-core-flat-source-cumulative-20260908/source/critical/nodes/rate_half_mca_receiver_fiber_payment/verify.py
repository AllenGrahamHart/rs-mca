"""Exact rational endpoints and analytic gates; no parameter scan."""

from fractions import Fraction as F
from math import isqrt, prod


R, D, H, NEAR = 1048576, 67472, 52999, 134944
BUDGET = 2130706433**6//2**128


def need(ok, message):
    if not ok:
        raise ValueError(message)


def ceil(x):
    return -(-x.numerator//x.denominator)


def ceil_sqrt(x):
    r = isqrt(x.numerator//x.denominator)
    return r+(r*r < x)


def tuple_budget(j):
    return prod(R+j-i for i in range(12))


def basis(j, a, t, cutoff):
    gap = D-cutoff
    return (gap+j-t)*prod(gap+a+10-i-t for i in range(1, 10))*(gap+1+10*t)


def main():
    n, m, degree = R+2000, D+2000, 1999
    need(4*m*m >= 9*n*degree and 4*degree <= n, "full multiplicity-one Johnson gate")
    x = ceil_sqrt(F(9*n*degree, 4))
    y = ceil_sqrt(F(9*n, 4*degree))
    z = max(y, ceil(F(9*n, 12*degree)))
    q_small = 2*x*y*y*z+(n-m+1)*y+z
    need((x, y, z, q_small) == (68741, 35, 395, 66558441820), "fixed padding anchor")
    need(2130706433**6 >= 2*R, "same-field padding room")
    pd = prod(D+i for i in range(1, 11))
    resource = max(ceil(F(tuple_budget(j), (D+j)*pd)) for j in (14000, H))
    need(resource == 13541615650357694642 and R-D-11 > 0, "uniform convex resource")
    need(84*(1-F(77, D+1)) > F(10488, 125) and D+1 > 12*84, "HIGH seven gate")
    need(144*(1-F(132, D+1)) > 143 and D+1 > 12*144, "HIGH twelve gate")
    high = (125*resource//10488, resource//143)
    need(high == (161394160592554522, 94696612939564298), "HIGH exact quotients")
    j = 14000
    need(10*(R+j-11) > 12*(D-6+H), "all-J near-full derivative")
    low = tuple_budget(j)//(12*basis(j, j-2000, 0, 6))
    need(low == 248408193733124448, "near-full LOW floor")
    total_small = 10*(q_small+H)+max(low, high[0])+NEAR
    need(total_small == 248408859318207582 < BUDGET, "near-full total")
    j = 45000
    need(F(H-10, 2) < D-10 and 10*(R+j-11) > 12*(4*(D-11)+3*H),
         "half-size no kink and all-J derivative")
    profiles = ((F(j, 2), F(0)), (F(j, 2), F(j, 4)), (F(j-10), F(j-10, 2)))
    ratios = [F(tuple_budget(j), 12)/basis(j, a, t, 11) for a, t in profiles]
    floors = [v.numerator//v.denominator for v in ratios]
    need(floors == [83217244759090589, 115346523791651123, 24011435147053027],
         "half-size three exact floors")
    q_ten = 156765527508668296
    total_half = q_ten+H+max(*floors, high[1])+NEAR
    need(total_half == 272112051300507362 < BUDGET, "half-size total")
    need(max(total_small, total_half) < 274979661975561635, "original assembly total unchanged")
    print("PASS: full child Johnson", q_small, "and uniform dimension-ten", q_ten)
    print("PASS: NEAR-FULL", total_small, "reserve", BUDGET-total_small)
    print("PASS: HALF", total_half, "reserve", BUDGET-total_half)
    print("Interval and fiber hypotheses are not automatic; full row remains OPEN")


if __name__ == "__main__":
    main()
