"""Exact prices for low-pair affine rank at most ten on the remaining gap."""

from fractions import Fraction as F
from itertools import product

R, D, LO, HI = 1048576, 67472, 9965, 21499
W, NEAR, BUDGET = 624373932788019251, 134944, 274980728111395087
TWO, PENCIL = 257846243054097181, 228260637755610995


def need(ok, message):
    if not ok:
        raise ValueError(message)


def pair_cap(j, t, rank=10):
    need(LO <= j <= HI and t in (1, 2) and 2 <= rank, "pair-cap scope")
    n, k, a = R+j, j, D+j-t
    need(a > 2*k-2 and a >= k, "both positive incidence denominators")
    return F(n-2*k+2, a-2*k+2)*F(n-k+1, a-k+1)**(rank-2)


def main():
    need(BUDGET == 2130706433**6//2**128 and NEAR == 2*D, "original row")
    need(HI-LO+1 == 11535 and 1048576-HI == 1027077
         and 1048576-LO == 1038611, "unchanged whole-degree gap")
    for t in (1, 2):
        need(D-HI+2-t >= 45973 and R-D+t > 0, "whole-interval derivative and denominator")
        need(pair_cap(LO, t) <= pair_cap(HI, t), "endpoint incidence envelope")
    need(tuple(int(pair_cap(HI, t)) for t in (1, 2)) == (76016086692, 76026754036),
         "separate pair floors")
    two = F(W, 3)+sum((F(R-D+t, t*(t+1))*pair_cap(HI, t) for t in (1, 2)), F(0))
    need(int(two)+NEAR == TWO and BUDGET-TWO == 17134485057297906, "rank-two total")
    wrong_rank = F(W, 3)+sum((F(R-D+t, t*(t+1))*pair_cap(HI, t, 11)
                              for t in (1, 2)), F(0))
    need(int(wrong_rank)+NEAR > BUDGET, "this recipe does not pay pair rank eleven")

    z, nmax, emax = R+1, R+HI, R-D+2
    need(0 < emax < z and z-emax == D-1, "union may have size m-2")
    peak = F(z**11*10**10, 11**11)
    pencil = F(W, 3)+nmax+peak*(F(1, 2*D**10)+F(1, 6*(D-1)**10))
    need(int(pencil)+NEAR == PENCIL and BUDGET-PENCIL == 46720090355784092,
         "charged rational-pencil total")
    singleton = W//3+nmax+NEAR
    need(singleton == 208124644263878102 < PENCIL < TWO < BUDGET, "exhaustive branch maximum")
    need(PENCIL+TWO > BUDGET, "whole-source alternatives are not additive charges")

    flags = 0
    for raws in product(range(1, 8), repeat=4):
        s1, s2 = (sum(r for r in raws if r <= t) for t in (1, 2))
        mass3, mass4 = (sum(min(r, t) for r in raws) for t in (3, 4))
        need(6*len(raws) == 2*mass3+3*s1+s2, "all-raw telescoping identity")
        need(mass3 <= mass4, "credited resource still covers raw at least three")
        flags += 1
    owners = 0
    for c in (1, 2):
        for raws in product(range(c, 3), repeat=4):
            for spare in range(4):
                e = sum(raws)+spare
                need(sum(F(3-r, 3) for r in raws) <= e*(F(1, c)-F(1, 3)),
                     "same-pair nonpreferred gain")
                owners += 1
    print("PAIR RANK<=10", TWO, "RESERVE", BUDGET-TWO)
    print("PENCIL", PENCIL, "SINGLETON", singleton)
    print("PASS", flags, "complete raw ledgers and", owners, "same-owner gain controls")
    print("PASS both whole-interval prices; actual pair dimension differs from graph dimension")
    print("No universal low-pair rank cap, whole J interval or Prize closure is inferred")


if __name__ == "__main__":
    main()
