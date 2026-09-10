"""Seven exact rank-ten basis certificates and original-source prices."""

from fractions import Fraction as F
from math import prod

R, GAP, T, D, LO, HI, X = 1048576, 67472, 7, 67465, 9965, 21499, 5000
W, NEAR, B = 624373932788019251, 134944, 274980728111395087


def need(ok, message):
    if not ok:
        raise ValueError(message)


def ladder():
    c = F(1, 2*(D+2))
    a, b = D*(2*D+1)*c, (3*D+1)*c
    for rank in range(4, 11):
        need(b >= D*c >= 0, "contraction input gate")
        H, alpha, delta = D+rank-1, F(rank-2, rank-1), F(1, rank-1)
        f = a+b*(rank-1)+c*(rank-1)**2
        s1, s0 = b-2*c+f/H, a-b+c-(rank-1)*f/H
        u3 = c*alpha**2/H
        u2 = (b*alpha+2*c*alpha*delta+D*c*alpha**2)/H
        u1 = (a+b*delta+c*delta**2+D*(b*alpha+2*c*alpha*delta))/H
        u0 = D*(a+b*delta+c*delta**2)/H
        need(u2 >= c and u3 >= 0, "nonnegative squared remainder")
        t1 = u1+2*(u2-c)*X+3*u3*X*X
        t0 = u0-(u2-c)*X*X-2*u3*X**3
        eta = max(F(0), t0+t1*rank-s0-s1*rank, t0+t1*HI-s0-s1*HI)
        a, b = t0-eta, t1
        need(min(a, b, c) > 0 and b >= D*c, "positive next gate")
        need(all(a+b*k <= s0+s1*k for k in (rank, HI)), "whole spike interval")
    return a, b, c


def main():
    a, b, c = ladder()
    q = lambda j: a+b*j+c*j*j
    need(10 <= LO <= HI <= D == GAP-T, "actual degree and gap scope")
    need((b+2*c*LO)*(R+LO-10) > 11*q(HI), "whole-J decreasing mass")
    ratio = F(5*prod(R+LO-i for i in range(11)), 11*prod(D+i for i in range(1, 10)))/q(LO)
    mass = int(ratio)
    pairs = int(prod(F(R+j, D+j) for j in range(1, 12)))
    need((mass, pairs) == (222676884802638507, 12774319384974), "exact low mass and pair floors")
    for wrong in (mass-1, mass+1):
        need(not wrong <= ratio < wrong+1, "wrong low floor rejected")
    exceptions = HI-11+5+5*pairs
    amount = W+T*(mass+exceptions)
    graph, lines = amount//8+NEAR, (W+T*(mass+HI-11+5))//8+NEAR
    need((exceptions, amount) == (63871596946363, 2183559227585113341), "all label exceptions")
    need((graph, lines) == (272944903448274111, 272889015800964850), "whole-source totals")
    need(B == 2130706433**6//2**128 and NEAR == 2*GAP, "original denominator and near")
    outside = (8*(B-NEAR+1)-amount+6)//7
    need(outside == 2326656757852545, "every-normal outside-label bound")
    need((amount+7*(outside-1))//8+NEAR == B, "last paid sufficient envelope")
    need((amount+7*outside)//8+NEAR == B+1, "adjacent envelope, not a true unsafe witness")
    print("PASS seven universal rank-ten certificates; MASS", mass, "PAIR", pairs)
    print("GRAPH", graph, "RESERVE", B-graph, "LINES", lines, "OUTSIDE_MIN", outside)
    print("Improved local bases, not an added global resource; source coverage is a separate theorem")


if __name__ == "__main__":
    main()
