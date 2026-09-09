"""Eight fixed rational certificates and exact low-raw population endpoints."""

from fractions import Fraction as F
from math import prod

D, E, X = 67347, 21499, 5000
R, GAP, LO, UPPER = 1048576, 67472, 9941, 14000
V9, V10 = 10755802499540570, 156765527508668296
NEAR, BUDGET = 134944, 274980728111395087
W0, W1 = 624373932788019251, 522680876725222604


def need(ok, message):
    if not ok:
        raise ValueError(message)


def ladder(verbose=False):
    c = F(1, 2*(D+2))
    a, b = D*(2*D+1)*c, (3*D+1)*c
    for rank in range(4, 12):
        need(b >= D*c >= 0, "quadratic contraction hypothesis")
        alpha, delta, H = F(rank-2, rank-1), F(1, rank-1), D+rank-1
        f = a+b*(rank-1)+c*(rank-1)**2
        s1, s0 = b-2*c+f/H, a-b+c-(rank-1)*f/H
        u3 = c*alpha**2/H
        u2 = (b*alpha+2*c*alpha*delta+D*c*alpha**2)/H
        u1 = (a+b*delta+c*delta**2+D*(b*alpha+2*c*alpha*delta))/H
        u0 = D*(a+b*delta+c*delta**2)/H
        need(u2 >= c and u3 >= 0, "global convex tangent")
        t1 = u1+2*(u2-c)*X+3*u3*X*X
        t0 = u0-(u2-c)*X*X-2*u3*X**3
        eta = max(F(0), t0+t1*rank-s0-s1*rank, t0+t1*E-s0-s1*E)
        a, b = t0-eta, t1
        need(b >= D*c and min(a, b, c) > 0, "next gate and positivity")
        need(all(a+b*k <= s0+s1*k for k in (rank, E)), "whole spike interval")
        need(a <= t0 and b == t1, "equal-fiber squared remainder")
        if verbose:
            print("RANK", rank, "shift", eta > 0, "A floor", int(a), "B floor", int(b))
    return a, b, c


def ceil_div(a, b):
    return -((-a)//b)


def main():
    need(D == GAP-125 and 11 <= LO <= UPPER <= E <= D, "complete parameter scope")
    need(BUDGET == 2130706433**6//2**128 and NEAR == 2*GAP, "original field and near")
    a, b, c = ladder(True)
    q = lambda j: a+b*j+c*j*j
    P, Pd = prod(D+i for i in range(1, 11)), prod(GAP+i for i in range(1, 11))
    beta = lambda j: 12*P*q(j)
    need(GAP*b >= a and 126*(GAP+E)*Pd >= 4*beta(E), "all-HIGH exact gate")
    need((b+2*c*LO)*(R+LO-11) > 12*q(E), "whole-interval decreasing quotient")
    for j, value in ((LO, W0), (UPPER, W1)):
        ratio = F(prod(R+j-i for i in range(12)))/beta(j)
        need(value <= ratio < value+1, "exact resource floor")
        for wrong in (value-1, value+1):
            need(not wrong <= ratio < wrong+1, "wrong floor rejected")
        print("ENDPOINT", j, value)
    paid = (W0//3+NEAR, (W0+2*V9)//3+NEAR, (W0+3*V10)//4+NEAR)
    need(paid == (208124644262808027, 215295179262501741, 273667628828640978),
         "three original source-class payments")
    need(BUDGET-max(paid) == 1313099282754109, "smallest exact reserve")
    upper_paid = (W1+V9)//2+NEAR
    need(upper_paid < BUDGET, "upper-range raw-one low-rank payment")
    mixed_paid = (W0+V9+V10)//3+NEAR
    need(mixed_paid < BUDGET, "nested mixed-rank payment")
    N = BUDGET-NEAR+1
    mass = (ceil_div(3*N-W0, 2), ceil_div(4*N-W0, 3), 2*N-W1)
    need(mass == (100284125772880591, 158516326552340442, 27280579497297684),
         "three strict over-budget populations")
    need((R-GAP+2)*10**11 < mass[0], "more than 100 billion actual pairs required")
    flag = 3*N-W0
    need(flag == 200568251545761181 and flag-V9 == 189812449046220611
         and flag-V10 == 43802724037092885, "nested low-raw populations")
    need(flag-V9 > V10 and flag-V10 > V9, "mixed-rank exclusion")
    for numerator, denominator, value in ((3*N-W0, 2, mass[0]), (4*N-W0, 3, mass[1])):
        need(denominator*(value-1) < numerator <= denominator*value, "ceiling endpoints")
    exceptions = 1149710068
    need(mass[0]-exceptions > V9 and mass[1]-exceptions > V10
         and mass[2]-exceptions > V9, "surviving selection rank margins")
    need(2*3 < GAP, "canonical complete-core selection guard")
    owner_weights = (3*(R-GAP+1), R-GAP+2, (R-GAP+3)//3)
    census = 4*N-W0-1
    need(owner_weights == (2943315, 981106, 327035) and census == 475548979657021324,
         "source-owned sufficient census with exact integer endpoint")
    need((W0+census)//4+NEAR == BUDGET and (W0+census+1)//4+NEAR == BUDGET+1,
         "adjacent census arithmetic, not true numerator optimality")
    print("PAID", paid, "upper raw-one", upper_paid, "MASS", mass)
    print("MIXED PAID", mixed_paid, "nested mass", flag)
    print("SUFFICIENT CENSUS", owner_weights, "ceiling", census, "NOT yet proved for arbitrary sources")
    print("PASS eight universal certificates, four wrong floors and exact rank/population endpoints")
    print("No full-rank low-defect census or unrestricted endpoint is proved")


if __name__ == "__main__":
    main()
