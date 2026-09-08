"""Exact comparison and forced-mass arithmetic, not an upper census."""

from fractions import Fraction as Q
from math import prod

D,d,R,NEAR,B = 67466,67472,1048576,134944,274980728111395087
PD=prod(d+i for i in range(1,11))
ROWS=((23000,268913508505087358,6933965264351691),
      (25000,241182907136195749,38626081114513530),
      (28000,205624578023526844,79264171528992278),
      (29999,185335366473228672,102451841872190189))


def need(ok,message):
    if not ok:
        raise ValueError(message)


def basis(k):
    return prod(D+k-Q(i*(k-1),10) for i in range(11))


def comparison(k):
    need(23000<=k<=29999,"comparison scope")
    resource=prod(R+k-i for i in range(12))
    q=max(Q(resource,12)/basis(k),Q(125*resource,(d+k)*PD*10488))
    return q.__floor__()+NEAR


def force(g):
    return 8*(B-g)//7+1


def main():
    need(B==2130706433**6//2**128 and NEAR==2*d,"original field and allowance")
    need(8*d*(d+23000)*PD >= (d+11)*basis(29999),"exceptional eighth-cost gate")
    need(11*(R+23000-11)>24*(D+29999),"whole-interval LOW comparison")
    high=Q(125*prod(R+29999-i for i in range(12)),(d+23000)*PD*10488)+NEAR
    need(high<166836445768446335<268913508505087358,"whole-interval HIGH comparison")
    for k,g,mass in ROWS:
        need(comparison(k)==g and force(g)==mass,"exact pointwise comparison and mass")
        need(7*(mass-1)<=8*(B-g)<7*mass,"least forced integer")
        for wrong in (mass-1,mass+1):
            need(not 7*(wrong-1)<=8*(B-g)<7*wrong,"wrong mass endpoint rejected")
        print("PASS",k,"comparison",g,"forced flags",mass)
    for delta in (0,1,6,7,14,100):
        mass=force(B-delta)
        need(7*(mass-1)<=8*delta<7*mass,"strict integer boundary")
    need(force(B-7)==9,"divisible boundary requires final plus one")
    need(1<=Q(1,2)+Q(7,8) and not 1<=0+Q(7,8),"premature floor loses valid integer")
    for t in (8,9):
        need((10-t)*29999<=D+111-11*t,"high flag rank excluded uniformly")
    for k in (23000,29999):
        b=(k+D+18)//4+1
        need(4*(b-1)-18<=k+D<4*b-18,"rank-seven core threshold")
        need(k-b<=5628,"auxiliary quotient degree")
    need(29999-((29999+D+18)//4+1)==5628,"sharp printed degree endpoint")
    print("PASS eight wrong masses, six strictness controls and rank/degree gates")
    print("No density premise, upper flag census or unrestricted row bound is asserted")


if __name__ == "__main__":
    main()
