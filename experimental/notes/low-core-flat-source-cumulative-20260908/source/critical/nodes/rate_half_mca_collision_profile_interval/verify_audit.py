"""Independent integer-scaled root-moment and collision-resource certificate."""

import hashlib
import importlib.util
from math import gcd,prod
from pathlib import Path


path=Path(__file__).resolve().parents[1]/"rate_half_mca_first_excess_core_interval/verify_audit.py"
spec=importlib.util.spec_from_file_location("independent_signed_counts",path)
old=importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
D,R,GAP,ADD=67466,1048576,67472,134944
LO,HI,COLLISIONS=22500,22999,180000000
TRIGGER=274950000000000000
TOTAL=274938028871508001
EXPECTED="5ace68871be07e08317ea359ac9a73f80c7a9b9a325e5390a0d6e66b9ecdc5a2"


def check(ok,why):
    if not ok:
        raise ValueError(why)


def fraction(n,d=1):
    check(d>0,"positive denominator")
    common=gcd(n,d)
    return n//common,d//common


def less(a,b):
    return a[0]*b[1]<b[0]*a[1]


def minimum(*pairs):
    chosen=pairs[0]
    for pair in pairs[1:]:
        if less(pair,chosen):
            chosen=pair
    return fraction(*chosen)


def maximum(*pairs):
    chosen=pairs[0]
    for pair in pairs[1:]:
        if less(chosen,pair):
            chosen=pair
    return fraction(*chosen)


def coefficients(rank,left,right,hn,hd):
    out={}
    for r in range(3,rank+1):
        contracted=rank-r
        root=(right-rank+1,D+right-rank+r)
        density=((contracted+1)*hn-contracted*hd,hd*(D+left-contracted))
        out[r]=maximum((1,r-1),minimum(root,density))
        check(0<out[r][0]<out[r][1],"hereditary convex coefficient")
    return out


def product(rank,argument,profile):
    xn,xd=argument
    check(xn>=xd>0,"positive real product domain")
    numerator,denominator=D+1,1
    for a in range(2,rank+1):
        contraction_n=prod(profile[r][1]-profile[r][0] for r in range(a+1,rank+1))
        contraction_d=prod(profile[r][1] for r in range(a+1,rank+1))
        numerator*=(D+1)*xd*contraction_d+(xn-xd)*contraction_n
        denominator*=xd*contraction_d
    return fraction(numerator,denominator)


def profile_bound(rank,left,right,hn,hd):
    return product(rank,(left,1),coefficients(rank,left,right,hn,hd))


def root_costs(left,right,t,first,last):
    ell,k=11-t,right-first
    check(k>=ell,"actual quotient dimension")
    mu=coefficients(11,left,right,last,t)
    if ell==1:
        outside=((D+k)**2,1)
    else:
        outside=maximum(((D+k)*(k-1),ell-1),
                        (D+k+(k-ell+1)*(k-ell),1))
    on,od=minimum(outside,((D+k)*last,t))
    split=(last*last*od+t*on,t*od*(D+left))
    common=minimum((last,t),((right-1)*mu[11][0],mu[11][1]),split)
    means=(minimum(common,(D+left+COLLISIONS,D+left)),common)
    result=[]
    for qn,qd in means:
        bn,bd=product(10,(left*qd-qn,qd),mu)
        result.append(fraction(12*(D+left)*bn,bd))
    return result


def old_cost(left,right,t,first,last):
    ell=11-t
    k0,k1=max(ell,left-last),right-first
    factors=[max(D+11-r,D+left-r*last//t) for r in range(10,ell-1,-1)]
    caps=[i*last//t for i in range(1,t)]
    inner=old.inner(factors,first,last,caps)
    greedy=(D+k0)*prod(max(D+ell-i,D+k0-i*last//t) for i in range(1,ell))
    hn,hd=minimum((k1-ell+1,1),(last,t))
    qn,qd=maximum(old.quotient(ell,k0,k1,greedy),profile_bound(ell,k0,k1,hn,hd))
    hybrid=(D+left)*prod(max(D+11-r,D+left-r*last//t) for r in range(1,11))
    bn,bd=maximum((qn*inner,qd),(hybrid,1),profile_bound(11,left,right,last,t))
    return fraction(12*bn,bd)


def resources(left,right):
    small,large,A=R+left,R+right,right-6001
    check(66*(small-2)*(small-3)>=660*(A-2)*(large-3)+2970*large*(A-1),
          "entire source-collision range has negative derivative")
    full=prod(range(large-11,large+1))
    filtered=full-66*COLLISIONS*prod(range(small-11,small-1))
    filtered+=660*(A-2)*COLLISIONS*prod(range(large-11,large-2))
    filtered+=1485*COLLISIONS**2*prod(range(large-11,large-3))
    check(0<filtered<full,"strict resource decrease")
    exceptions=right-11+large*(A-1)//2
    return full,filtered,exceptions


def main():
    digest=hashlib.sha256()
    left,blocks,count,floors,augmented=LO,0,0,0,0
    peak,where=0,None
    rankcounts={t:0 for t in range(1,11)}
    while left<=HI:
        right=min(left+15,HI)
        full,filtered,exception=resources(left,right)
        high=(10488*(GAP+left)*prod(range(GAP+1,GAP+11)),125)
        digest.update(f"R:{left},{right}:{full}:{filtered}:{exception}\n".encode())
        for t in range(1,11):
            top=right-11+t
            if t==1:
                top=min(top,right-6001)
            width=max(1,(top-t+128)//128)
            first=t
            while first<=top:
                last=min(first+width-1,top)
                small,large=root_costs(left,right,t,first,last)
                def ceilings():
                    sn,sd=minimum(small,high)
                    ln,ld=minimum(large,high)
                    return full*sd//sn+ADD,filtered*ld//ln+exception+ADD
                if t<=5 and max(ceilings())>TRIGGER:
                    prior=old_cost(left,right,t,first,last)
                    small,large=maximum(small,prior),maximum(large,prior)
                    augmented+=1
                for tag,resource,cost,add in (("S",full,minimum(small,high),ADD),
                                              ("L",filtered,minimum(large,high),exception+ADD)):
                    cn,cd=fraction(*cost)
                    num,den=resource*cd,cn
                    quotient,remainder=divmod(num,den)
                    check(den>0 and 0<=remainder<den,"Euclidean floor certificate")
                    for wrong in (quotient-1,quotient+1):
                        check(not wrong*den<=num<(wrong+1)*den,"adjacent floor rejected")
                        floors+=1
                    cap=quotient+add
                    check(cap<=TOTAL,"all fixed boxes paid")
                    digest.update(f"{tag}:{left},{right},{t},{first},{last}:{cn}/{cd}:{cap}\n".encode())
                    if cap>peak:
                        peak,where=cap,(tag,left,right,t,first,last)
                count+=1
                rankcounts[t]+=1
                first=last+1
            check(first==top+1,"whole integer size interval traversed exactly")
        print("BLOCK",left,right,"boxes",count,"peak",peak,flush=True)
        left=right+1
        blocks+=1
    check(left==HI+1 and blocks==32 and count==40960 and floors==163840,"full coverage")
    check(all(v==4096 for v in rankcounts.values()),"all ten flat ranks")
    check(augmented==10955,"independent calibration inventory")
    check((peak,where)==(TOTAL,("S",22628,22643,5,18059,18235)),"independent maximum")
    print("CERTIFICATE",(peak,where),"augmented",augmented,"DIGEST",digest.hexdigest(),flush=True)
    check(digest.hexdigest()==EXPECTED,"all independently reconstructed costs")
    print("PASS independent integer audit; no primary or Fraction import")
    print("Exact tangent vectors reused from the earlier independent audit, not its finite interval claim")


if __name__=="__main__":
    main()
