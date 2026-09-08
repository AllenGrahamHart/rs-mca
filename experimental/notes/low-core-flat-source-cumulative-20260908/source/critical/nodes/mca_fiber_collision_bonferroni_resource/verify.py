"""Exact collision resource and small histogram/multiplicity controls."""

from itertools import product
from math import comb,factorial,prod


def need(ok,why):
    if not ok:
        raise ValueError(why)


def falling(n,r):
    return prod(n-i for i in range(r))


def resource(n,r,A,T):
    need(n>=r>=4 and A>=2 and 0<=T<=n*(A-1),"source collision resource scope")
    return (falling(n,r)-comb(r,2)*T*falling(n-2,r-2)
            +3*comb(r,3)*(A-2)*T*falling(n-3,r-3)
            +3*comb(r,4)*T*T*falling(n-4,r-4))


def box_resource(n0,n1,r,A,T0):
    need(n1>=n0>=r>=4 and A>=2 and 0<=T0<=n1*(A-1),"whole source-resource box")
    need(comb(r,2)*(n0-2)*(n0-3)>=3*comb(r,3)*(A-2)*(n1-3)
         +6*comb(r,4)*n1*(A-1),"whole-T monotonicity coefficient")
    return (falling(n1,r)-comb(r,2)*T0*falling(n0-2,r-2)
            +3*comb(r,3)*(A-2)*T0*falling(n1-3,r-3)
            +3*comb(r,4)*T0*T0*falling(n1-4,r-4))


def symmetric(weights,r):
    values=[1]+[0]*r
    for a in weights:
        for j in range(r,0,-1):
            values[j]+=a*values[j-1]
    return factorial(r)*values[r]


def main():
    count=0
    for length in range(1,7):
        for weights in product(range(1,4),repeat=length):
            T=sum(a*(a-1) for a in weights)
            A=max(2,max(weights))
            for z in (0,1,2):
                n=sum(weights)+z
                for r in (4,5):
                    if n<r:
                        continue
                    exact=symmetric(weights,r)
                    padded=symmetric((*weights,*([1]*z)),r)
                    upper=resource(n,r,A,T)
                    need(exact<=padded<=upper,"exact resource, singleton padding and envelope")
                    pairs=sum(a*(a-1) for a in weights)
                    triple=sum(a*(a-1)*(a-2) for a in weights)
                    disjoint=sum(a*(a-1)*(a-2)*(a-3) for a in weights)
                    disjoint+=sum(a*(a-1)*b*(b-1) for i,a in enumerate(weights)
                                  for j,b in enumerate(weights) if i!=j)
                    need(triple<=(A-2)*T and disjoint<=pairs*pairs,"both overlap upper bounds")
                    count+=1
    for weights,drop in (((2,2,1,1),"disjoint"),((3,1,1,1),"triple")):
        n,r,A=sum(weights),4,max(weights)
        T=sum(a*(a-1) for a in weights)
        wrong=resource(n,r,A,T)
        wrong-= (3*comb(r,4)*T*T*falling(n-4,r-4) if drop=="disjoint"
                 else 3*comb(r,3)*(A-2)*T*falling(n-3,r-3))
        need(wrong<symmetric(weights,r),"omitted overlap term gives a false upper bound")
    for n0,n1 in ((1000,1000),(1000,1010)):
        ceiling=box_resource(n0,n1,5,3,10)
        for n in (n0,n1):
            for T in (10,20,n*2):
                need(resource(n,5,3,T)<=ceiling,"whole-box monotone envelope")
    try:
        box_resource(12,12,12,12,0)
    except ValueError:
        pass
    else:
        raise ValueError("accepted false monotonicity guard")
    print("PASS",count,"exact histogram controls; both overlap omissions fail; bad monotonicity rejected")
    print("The secant supplier owns actual receiver/label transport; no new near allowance")


if __name__=="__main__":
    main()
