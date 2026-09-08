"""Independent scaled fibers, unnormalized quadratic and combined cost audit."""

from fractions import Fraction as F
import hashlib
import importlib.util
from math import prod
from pathlib import Path

path=Path(__file__).resolve().parents[1]/"rate_half_mca_fiber_contraction_interval/verify_audit.py"
spec=importlib.util.spec_from_file_location("independent_polynomials",path)
old=importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
D,R,d,H,ADD=67466,1048576,67472,52999,134944
Q=156765527508668296
EXPECTED="5d958551756ddbc6abb9cd787ed8f3f887bc06087c9583fe335564df76f02804"


def check(ok,why):
    if not ok:
        raise ValueError(why)


def quadratic():
    polynomial=old.scale(old.mul([D,1],[F(2*D+1,2),F(1,2)]),D+1)
    for rank in range(4,12):
        check(polynomial[1]>=D*polynomial[2]>=0,"child moment gate")
        spike=old.add(old.scale([-(rank-1),1],old.value(polynomial,rank-1)),
                      old.scale(old.compose(polynomial,[-1,1]),D+rank-1))
        equal=old.mul([D,1],old.compose(polynomial,[F(1,rank-1),F(rank-2,rank-1)]))
        curvature=(D+rank-1)*polynomial[2]
        residual=old.add(equal,[0,0,-curvature])
        check(residual[2]>=0 and residual[3]>=0,"convex tangent")
        slope=old.value(old.derivative(residual),5000)
        intercept=old.value(residual,5000)-5000*slope
        raw=[intercept,slope,curvature]
        shift=max(F(0),*(old.value(raw,k)-old.value(spike,k) for k in (rank,65000)))
        polynomial=[intercept-shift,slope,curvature]
        check(polynomial[1]>=D*polynomial[2],"next moment")
        check(all(old.value(polynomial,k)<=old.value(spike,k) for k in (rank,65000)),
              "whole affine spike difference")
    check(all(c>=0 for c in polynomial),"increasing quadratic")
    return polynomial


def fiber(J,a,p,q):
    factors=[q*(D+J)-p*a]
    factors.extend(q*(D+a+10-i)-p*a for i in range(1,10))
    factors.append(q*(D+1)+10*p*a)
    check(all(x>0 for x in factors),"positive scaled basis factors")
    return F(prod(factors),q**11)


def main():
    polynomial=quadratic()
    digest=hashlib.sha256()
    count=mutations=0
    peaks=[]
    check(H<D+1 and 9*D-10*H+199>0,"no kink and entire a range")
    for start,L in ((21000,6000),(23000,8000)):
        first=start
        peak=(F(0),None)
        while first<=H:
            last=min(first+499,H)
            a=first-L
            check(10<=L<first<=last<=H,"degree and actual fiber guards")
            universal=12*old.value(polynomial,first)
            high=F((d+first)*prod(range(d+1,d+11))*10488,125)
            resource=prod(range(R+last-11,R+last+1))
            for i,p in enumerate(range(16,32)):
                low=min(high,max(universal,12*min(fiber(first,a,0,1),
                                                  fiber(first,a,32-p,32))))
                heavy=min(high,max(universal,12*min(fiber(first,a,p,32),
                                                    fiber(first,a,p+1,32))))
                hmax=Q+F((32-p)*(last-10),32)
                surplus=max(F(0),low-heavy)
                total=(resource+surplus*hmax)/low+ADD
                floor=total.numerator//total.denominator
                check(floor*total.denominator<=total.numerator<(floor+1)*total.denominator,
                      "integer total floor")
                for wrong in (floor-1,floor+1):
                    check(not wrong*total.denominator<=total.numerator<(wrong+1)*total.denominator,
                          "wrong adjacent floor")
                    mutations+=1
                check(floor<2130706433**6//2**128,"complete source gate")
                digest.update(f"{start},{L},{first},{last},{i}:{low.numerator}/{low.denominator}:{heavy.numerator}/{heavy.denominator}:{total.numerator}/{total.denominator}\n".encode())
                if total>peak[0]:
                    peak=total,(first,last,i)
                count+=1
            first=last+1
        check(first==H+1,"all integer degrees covered")
        peaks.append((start,L,peak[0].__floor__(),peak[1]))
    check(peaks==[(21000,6000,266180883463176443,(21000,21499,15)),
                  (23000,8000,265879110627611677,(23000,23499,15))],"independent maxima")
    check(count==1984 and mutations==3968,"complete inventory")
    check(digest.hexdigest()==EXPECTED,"all independent exact costs")
    print("PASS independent source gates",peaks)
    print("BOXES",count,"WRONG FLOORS",mutations,"DIGEST",digest.hexdigest())


if __name__=="__main__":
    main()
