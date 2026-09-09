"""Exact whole-interval certificates for the cutoff-fifty cubic assembly."""

from fractions import Fraction as F
from math import prod

LO, HI, E, X = 9941, 9964, 10000, 5000
R, GAP, D = 1048576, 67472, 66972
COVER, KAPPA, NEAR, EXCEPTIONS = 50, 51, 134944, 256
W = 646273487661620022
TOTAL = 274861473951141154
BUDGET = 274980728111395087


def need(ok, message):
    if not ok:
        raise ValueError(message)


def ladder():
    c = F(1, 2*(D+2))
    a, b = D*(2*D+1)*c, (3*D+1)*c
    for rank in range(4, 12):
        need(b >= D*c >= 0, "input contraction gate")
        alpha, delta, H = F(rank-2, rank-1), F(1, rank-1), D+rank-1
        f = a+b*(rank-1)+c*(rank-1)**2
        s1, s0 = b-2*c+f/H, a-b+c-(rank-1)*f/H
        u3 = c*alpha*alpha/H
        u2 = (b*alpha+2*c*alpha*delta+D*c*alpha*alpha)/H
        u1 = (a+b*delta+c*delta*delta+D*(b*alpha+2*c*alpha*delta))/H
        u0 = D*(a+b*delta+c*delta*delta)/H
        need(u2 >= c and u3 >= 0, "nonnegative squared remainder")
        t1 = u1+2*(u2-c)*X+3*u3*X*X
        t0 = u0-(u2-c)*X*X-2*u3*X**3
        eta = max(F(0), t0+t1*rank-s0-s1*rank, t0+t1*E-s0-s1*E)
        a, b = t0-eta, t1
        need(min(a, b, c) > 0 and b >= D*c, "positive next coefficients")
        need(all(s0+s1*k >= a+b*k for k in (rank, E)), "whole spike interval")
    return a, b, c


def phi(d, w):
    ell = (d-1)//w
    return d*(ell+1)*(ell+2)//2-w*ell*(ell+1)*(ell+2)//3


def main():
    need(11 <= LO <= HI <= E <= D == GAP-500, "basis versus cover cutoffs")
    need(KAPPA == COVER+1 and 2*500 < GAP and 2130706433 > E+51391,
         "selection, characteristic and accounting scopes")
    need(BUDGET == 2130706433**6//2**128 and NEAR == 2*GAP, "original field and near")
    a, b, c = ladder()
    q = lambda j: a+b*j+c*j*j
    P, Pd = prod(D+i for i in range(1, 11)), prod(GAP+i for i in range(1, 11))
    beta = lambda j: 12*P*q(j)
    need(GAP*b >= a and 5500*(GAP+E)*Pd >= KAPPA*beta(E), "whole-interval strong HIGH")
    need((b+2*c*LO)*(R+LO-11) > 12*q(E), "whole-interval decreasing quotient")
    ratio = F(prod(R+LO-i for i in range(12)))/beta(LO)
    need(W <= ratio < W+1, "exact raw-mass floor")
    for wrong in (W-1, W+1):
        need(not wrong <= ratio < wrong+1, "wrong mass floor rejected")
    need(501*(GAP+E)*Pd < KAPPA*beta(E), "coarse HIGH cannot fund this application")
    labels, base = R-GAP+COVER, W//KAPPA+NEAR
    need(labels == 981154, "original per-pair labels")
    for j in (LO, HI):
        A, w = j+GAP-COVER, j-1
        need(15*w <= 2*A-1 < 16*w and 11*w <= 2*A-4*w-1 < 12*w,
             "linear endpoint proof of both monomial regimes")
        need(phi(2*A, w)-phi(2*A-4*w, w)-4*(R+j) == 3627124-364*j > 0,
             "strict full-kernel cubic cover")
        need((2*A-1-3*w)//3 <= 41635 < 51391, "actual doubled factor height")
    need(3627124-364*HI == 228 and 3627124-364*(HI+1) == -136,
         "fixed-cutoff adjacent kernel boundary")
    need(15**2 <= EXCEPTIONS and HI-LO+1 == 24, "all off-gcd pairs and whole degrees")
    f = lambda t: (981104+t)*(2**7*3**12*F(1047027, 65923-t)**3+EXCEPTIONS)
    low = int(F(W, KAPPA)+sum((f(t)/F(t*(t+1)) for t in range(1, KAPPA)), F(0)))+NEAR
    need(low == TOTAL and BUDGET-TOTAL == 119254160253933, "binding low-height complete price")

    ell, h0, hmax = (HI-1-1551)//3, 1550, (HI-1)//2
    u0, slots0 = GAP+1-COVER+h0, 2*R+2+4*h0
    u, slots = u0+3*ell, slots0+7*ell
    den = u*u-slots*ell
    need(2*R-1-3*(GAP-COVER)-2*ell > 0 and 2*u0 > 4*ell,
         "component g and height derivative gates")
    need(2*R+2-4*(GAP+1-COVER)-5*ell > 0, "positive height derivative b")
    need(6*u0-slots0+4*ell < 0 and den > 0, "decreasing positive component denominator")
    top = slots*(u-ell)//den
    lower = int(2**7*3**13*F(R+1-hmax, GAP+1-COVER-hmax)**2)
    high = base+labels*(top*3**16+lower+1+EXCEPTIONS)
    need(high == 256464058457221028 < TOTAL, "all high-height components")
    print("D7 HIGH", ell, hmax, u, slots, den, top, lower, "TOTAL", high)

    h, nmax, amin = (HI-1)//10, R+HI, LO+GAP-COVER
    a1, collision = amin-21*h, 3*h
    den = a1*a1-nmax*collision
    need(a1 > collision and den > 0, "GP single-valued original-coordinate count")
    gp_top = nmax*(a1-collision)//den
    gp_lower = int(2**10*3**9*F(R+1-h, GAP+1-COVER-h)**3)
    need((h, a1, collision, den, gp_top, gp_lower) ==
         (996, 56447, 2988, 23346289, 2423, 79053330393), "GP envelope")
    need(base+labels*(max(gp_top+1, gp_lower)+EXCEPTIONS) == 90235520749559576 < TOTAL,
         "whole GP locus, not sum of dimension alternatives")
    ordinary = []
    for kernel in range(12):
        if kernel in (7, 10):
            continue
        r = (kernel+2)//3
        h = 0 if kernel in (0, 11) else (HI-1)//(10//(11-kernel))
        quotient = F(R+1-h, GAP+1-COVER-h)
        need(quotient >= 3, "weighted incidence ratio gate")
        pairs = int(2**kernel*3**(22-kernel-r)*quotient**r)
        ordinary.append(base+labels*(pairs+EXCEPTIONS))
    need(max(ordinary) == 269761880886747862 < TOTAL, "every other projection kernel")
    for pairs in (163774741769, 223154201664, 6):
        need(base+labels*(pairs+EXCEPTIONS) < TOTAL, "smooth, boundary and nongeneric cubics")

    hmax = HI-1
    line_den = amin*amin-590000*hmax
    small = (590000+16*hmax)*amin//line_den
    need(line_den == 106863769 and small == 542 and 590000-16*hmax > 0,
         "small-line whole-height denominator and numerator")
    outside_den = GAP+2-COVER-HI
    need(outside_den == 57460 and outside_den-hmax > 0
         and F(458576, outside_den) < 8 and 458576-16*outside_den < 0,
         "large-line outside-domain envelope")
    need(2**16*8**6 == 2*8**11 and 11*KAPPA > 501, "all complement factors and medium margins")
    primary = 255637082864553899
    need(23067643444721720934//501+17200000000000000+NEAR < primary,
         "nonconstant primary line included")
    large = primary+labels*(2*8**11+EXCEPTIONS)
    need(large == 272493180485087659 < TOTAL, "coupled large-line source")
    need(large+base > BUDGET, "duplicating the source resource is not allowed")
    for pairs in (3*small, 127031877504+small, 0):
        need(base+labels*(pairs+EXCEPTIONS) < TOTAL, "all remaining factor patterns")
    print("RAW MASS", W, "BASE", base, "BOUND", TOTAL, "RESERVE", BUDGET-TOTAL)
    print("PASS eight basis certificates, all original raw margins and every cubic/reducible factor pattern")
    print("PASS exact full-cover interval 9941..9964; no claim beyond its fixed-cutoff kernel boundary")


if __name__ == "__main__":
    main()
