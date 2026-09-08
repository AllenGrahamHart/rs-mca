"""Exact endpoint arithmetic for the analytic all-carrier high interval."""

from fractions import Fraction as Q
from math import prod

R, D, C = 1048576, 67466, 67467
LO, HI, NEAR = 65000, 169999, 134944
RESOURCE = 23067643444721720934
TARGET = 274929007493481160


def check(ok, message):
    if not ok:
        raise ValueError(message)


def rising(x, k):
    return prod(x+i for i in range(k))


def source_cap(J, j, a, t):
    h, ell, M = a/j, 11-j, J+D
    e = J-a-ell
    outside = (M-t)*prod(M-t-min(e+i,i*h) for i in range(1,ell))
    tail = rising(C-t,j) if t<=C else 0
    coupled = tail+11*rising(C,j-1)*t
    check(outside>0 and coupled>0, "positive flat count")
    ratio = Q(prod(R+J-i for i in range(12)),12)/(outside*coupled)
    return ratio.numerator//ratio.denominator+NEAR


def cases():
    for j in range(1,5):
        for r in range(j,6):
            crossing = 11+r*(Q(C,j)-1)
            points = {Q(LO),Q(HI)}
            if LO<=crossing<=HI:
                points.add(crossing)
            for J in sorted(points):
                a=j*(1+(J-11)/r)
                ts={Q(0),a}
                if C<=a:
                    ts.add(Q(C))
                for t in sorted(ts):
                    yield j,r,J,a,t
        # Constant-a=c pieces have their internal boundaries above.
        for J in (Q(LO),Q(HI)):
            if j*(1+(J-11)/5)<=C<=J-11+j:
                for t in (Q(0),Q(C)):
                    yield j,0,J,Q(C),t


def main():
    l0=R+LO-11
    check(7*l0>12*(HI+5*D+50), "t=0 branches decrease")
    check(7*l0>12*(HI+50), "t=c branches decrease")
    check(l0*l0>12*(HI+D)**2, "constant-a=c branches log-convex")
    check(l0*l0>12*HI*HI, "a>=c branches log-convex")
    check(14*l0>60*(D+HI), "low-density hybrid decreases")
    curvature=[]
    for j in range(1,5):
        prev=rising(C,j-1)
        factors=[C+i for i in range(j)]
        a0=prod(factors)
        first=sum(prod(factors[k] for k in range(j) if k!=i) for i in range(j))
        second=2*sum(prod(factors[k] for k in range(j) if k not in (i,h))
                     for i in range(j) for h in range(i+1,j))
        n=120-21*j
        check((11*prev-first)**2-a0*second>=n*prev*prev, "initial log curvature")
        bound=Q(5,j)*(C+j-1)+11*(min(Q(HI),6+Q(5*C,j))-6)
        check(n*l0*l0>12*bound*bound, "all a<c curvature certificate")
        curvature.append(str(bound))
    expected_curvature=['2207258','4048025/2','4048030/3','4048035/4']
    check(curvature==expected_curvature, "curvature denominator list")
    h5=Q(LO-6,5)
    hybrid=(LO+D)*prod(LO+D-min(i*h5,LO-11+i) for i in range(1,11))
    low=int(Q(prod(R+LO-i for i in range(12)),12)/hybrid)+NEAR
    maxima={j:0 for j in range(1,5)}
    witnesses={}
    count=0
    for j,r,J,a,t in cases():
        value=source_cap(J,j,a,t)
        check(value<TARGET, "unpaid endpoint: "+str((j,r,J,a,t,value)))
        if value>maxima[j]:
            maxima[j]=value
            witnesses[j]=tuple(map(str,(r,J,a,t)))
        count+=1
    print("LOW-DENSITY",low)
    check(low==253456757626524982, "printed low-density bound")
    check(count==91, "complete indexed endpoint count")
    check(maxima=={1:266533517899145497,2:244377164689337849,
                   3:244401081788492566,4:244417756062852746}, "printed endpoint maxima")
    print("DENSE-FLAT MAXIMA",maxima)
    print("WITNESSES",witnesses,"ENDPOINT COUNT",count)
    for J in (LO,HI):
        f=Q(prod(R+J-i for i in range(12)),
            (67472+J)*prod(67472+i for i in range(1,11)))
        check(f<=RESOURCE, "convex resource endpoints")
        print("RESOURCE CEILING",J,-(-f.numerator//f.denominator))
    check(84*Q(67473-77,67473)>Q(10488,125), "HIGH floor")
    check(12*84<67473, "HIGH monotonicity")
    check(125*RESOURCE//10488+NEAR==TARGET, "one source resource")
    check(2130706433**6//2**128-TARGET==51720617913927, "original field reserve")
    check(max(low,*maxima.values())<TARGET, "whole-source maximum")
    print("PASS: finite arithmetic; universal source/interval arguments are hand proofs")


if __name__ == "__main__":
    main()
