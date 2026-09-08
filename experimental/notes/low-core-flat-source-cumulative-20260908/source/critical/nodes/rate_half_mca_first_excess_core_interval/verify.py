"""Exact finite certificate; the exhaustive source argument is in proof.md."""

import hashlib

from fractions import Fraction as F
import importlib.util
from math import comb, prod
from pathlib import Path

root=Path(__file__).resolve().parents[3]
path=root/"critical/nodes/rate_half_mca_quotient_density_interval/verify.py"
spec=importlib.util.spec_from_file_location("quotient",path)
q=importlib.util.module_from_spec(spec)
spec.loader.exec_module(q)
D,R,d,NEAR=67466,1048576,67472,134944
TARGET=273019482620216244
EXPECTED_DIGEST="a34884087a5dd4e1ddfabb9413b89f4bfa4fc02dd6dc7389ed8e5bea6c5f3dc9"


def need(ok,why):
    if not ok:
        raise ValueError(why)


def degree_cover(rows):
    need(rows and rows[0][0]==28000 and rows[-1][1]==29999,"degree endpoints")
    need(all(a<=b for a,b in rows),"nonempty blocks")
    need(all(x[1]+1==y[0] for x,y in zip(rows,rows[1:])),"exact degree cover")


def bins(a,b,parts,extra=()):
    if a>b:
        return
    step=max(1,(b-a+parts)//parts)
    cuts=sorted({*range(a,b+1,step),b+1,*[x for x in extra if a<x<=b]})
    for x,y in zip(cuts,cuts[1:]):
        yield x,y-1


def product(rank,k):
    return prod(F(D+k)-F(i*(k-1),rank-1) for i in range(rank))


def inside(ds,b0,b1,caps):
    t=len(ds)
    need(t<=b0<=b1,"complete flat size hull")
    if min(ds)<=b1:
        raise ValueError("positive completion")
    value=comb(11,t)
    for i in range(t-1,0,-1):
        lower,upper=max(b0-caps[i],0),b1-i
        need(0<=lower<=upper<=b1<min(ds),"valid integer tangent interval")
        factor=comb(11,i)
        def evaluate(z):
            p,derivative=1,0
            for c in ds[:t-i]:
                p,derivative=p*(c-z),derivative*(c-z)+p
            tail=value-factor*derivative
            return factor*(p+z*derivative)+tail*(lower if tail>=0 else upper),tail
        lo,hi=lower,upper
        if evaluate(lo)[1]>=0:
            hi=lo
        elif evaluate(hi)[1]<=0:
            lo=hi
        else:
            while hi-lo>1:
                mid=(hi+lo)//2
                if evaluate(mid)[1]>=0:
                    hi=mid
                else:
                    lo=mid
        value=max(evaluate(lo)[0],evaluate(hi)[0])
    base=prod(c-b1 for c in ds)
    return max(base,base+value*(b0 if value>=0 else b1))


def quotient(rank,k0,k1,greedy):
    k0=max(rank,k0)
    need(rank<=k0<=k1<=D and greedy>0,"actual quotient hull and greedy positivity")
    lower=F(max(greedy,q.quadratic(rank,D,k1,k0)))
    f=rank*rank//4
    if (f-1)*k1<=D+f*(rank-1):
        lower=max(lower,product(rank,k0))
    return lower


def low(J0,J1,t,b0,b1):
    def cap(J,r):
        value=min(J-11+r,r*(J-5)//6)
        return min(value,(J+D)//(11-r)) if r<t else value
    ds=[J0+D-cap(J0,10-i) for i in range(t)]
    caps={i:cap(J1,i) for i in range(1,t+1)}
    ell=11-t
    greedy=(D+J0-b1)*prod(D+J0-cap(J0,t+i) for i in range(1,ell))
    return 12*quotient(ell,J0-b1,J1-b0,greedy)*inside(ds,b0,b1,caps)


def high(J0,J1,t,k0,k1):
    b0,b1=J0-k1,J1-k0
    ell=11-t
    ds=[max(D+1+i,D+J1-(10-i)*b1//t) for i in range(t)]
    caps={i:i*b1//t for i in range(1,t+1)}
    greedy=(D+k0)*prod(max(D+ell-i,D+k0-i*b1//t) for i in range(1,ell))
    return 12*quotient(ell,k0,k1,greedy)*inside(ds,b0,b1,caps)


def main():
    overall,count=(0,None),0
    digest=hashlib.sha256()
    rows=[(a,min(29999,a+31)) for a in range(28000,30000,32)]
    degree_cover(rows)
    mutations=0
    cases={"L":0,"H":0}
    def record(kind,J0,J1,t,a,b,cost,cap):
        nonlocal mutations
        ratio=F(prod(R+J1-i for i in range(12)))/cost
        need(cap-NEAR<=ratio<cap-NEAR+1,"exact resource floor")
        for false in (cap-NEAR-1,cap-NEAR+1):
            need(not false<=ratio<false+1,"reject adjacent wrong floor")
            mutations+=1
        digest.update(f"{kind}:{J0},{J1},{t},{a},{b}:{cost.numerator}/{cost.denominator}:{cap}\n".encode())
        cases[kind]+=1
    for J0,J1 in rows:
        resource=prod(R+J1-i for i in range(12))
        costs=[12*product(11,J0),F(10488,125)*(d+J0)*prod(d+i for i in range(1,11))]
        basic=F(resource)/min(costs)
        digest.update(f"B:{J0},{J1}:{basic.numerator}/{basic.denominator}\n".encode())
        peak=(int(basic)+NEAR,("basis-rich/HIGH",))
        for t in range(1,8):
            bmin=(J0+D)//(11-t)+1
            bmax=min(J1-11+t,t*(J1-5)//6)
            parts=256 if J0<28256 and t>=6 else 128
            for b0,b1 in bins(bmin,bmax,parts):
                cost=low(J0,J1,t,b0,b1)
                cap=int(F(resource)/cost)+NEAR
                count+=1
                record("L",J0,J1,t,b0,b1,cost,cap)
                if cap>peak[0]:
                    peak=cap,("L",t,b0,b1)
        for t in range(1,6):
            ell=11-t
            kmin=2001 if t==1 else ell
            kmax=J1-t*(J1-5)//6-1
            f=ell*ell//4
            extra=[(D+f*(ell-1))//(f-1)+1]
            if t==1:
                extra+=list(range(2001,2501,32))
            for k0,k1 in bins(kmin,kmax,64,extra):
                cost=high(J0,J1,t,k0,k1)
                cap=int(F(resource)/cost)+NEAR
                count+=1
                record("H",J0,J1,t,k0,k1,cost,cap)
                if cap>peak[0]:
                    peak=cap,("H",t,k0,k1)
        need(peak[0]<=TARGET,"all boxes below total")
        if peak[0]>overall[0]:
            overall=peak[0],(J0,J1,peak[1])
    need(count==63312 and len(rows)==63 and mutations==126624,"entire inventory")
    need(overall==(TARGET,(28000,28031,("H",1,2001,2032))),"maximum certificate")
    need(248408859318207582<TARGET<274929007493481160,"source-fiber and interval union")
    need(2130706433**6//2**128-TARGET==1961245491178843,"original reserve")
    need(cases=={"L":41957,"H":21355},"both exhaustive geometric branches")
    need(digest.hexdigest()==EXPECTED_DIGEST,"every cost")
    broken=[rows[1:],rows[:-1],rows+[rows[-1]],rows[:20]+rows[21:],[(27999,rows[0][1])]+rows[1:]]
    for bad in broken:
        try:
            degree_cover(bad)
        except ValueError:
            pass
        else:
            raise ValueError("accepted broken degree cover")
    print("PASS",count,"boxes; 63 basic comparisons;",mutations,"wrong floors; five cover mutations")
    print("CASES",cases,"MAX",overall,"DIGEST",digest.hexdigest())
    print("Every normalized carrier on J=28000..29999 paid; unrestricted row remains OPEN")


if __name__=="__main__":
    main()
