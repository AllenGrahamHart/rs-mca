"""Independent integer-scaled product and corner audit; no primary/Fraction import."""

import hashlib
import importlib.util
from math import gcd, prod
from pathlib import Path

path = Path(__file__).resolve().parents[1]/"rate_half_mca_first_excess_core_interval/verify_audit.py"
spec = importlib.util.spec_from_file_location("previous_independent",path)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
D,R,GAP,ADD = 67466,1048576,67472,134944
LOW,HIGH = 26500,27999
TOTAL = 272896493994028693
EXPECTED = "42390ea68dfb9360ab741636c071e3a88523c371bf013fc0857016faa8d1eab0"


def check(ok,why):
    if not ok:
        raise ValueError(why)


def reduce_pair(n,d):
    check(n >= 0 and d > 0,"nonnegative rational count")
    g = gcd(n,d)
    return n//g,d//g


def maximum(*pairs):
    best = (0,1)
    for n,d in pairs:
        if n*best[1] > best[0]*d:
            best = (n,d)
    return best


def quantitative(rank,k,hn,hd):
    p,q = (rank*rank//4)*hn,hd*(D+k)
    if p > 2*q:
        return 0,1
    p,q = reduce_pair(max(p,q),q)
    numerator,denominator = D+1,1
    for a in range(2,rank+1):
        an = prod(j*q-p for j in range(a,rank))
        ad = prod(j*q for j in range(a,rank))
        check(an >= 0 and ad > 0,"positive unrolled product factors")
        numerator *= (D+1)*ad+(k-1)*an
        denominator *= ad
    return reduce_pair(numerator,denominator)


def corners(left,right,t,k,r):
    return min(max(D+11-r,D+J-r*(J-k)//t) for J in (left,right))


def cost(left,right,t,k0,k1):
    ell = 11-t
    first,last = left-k1,right-k0
    factors = [corners(left,right,t,k0,r) for r in range(10,ell-1,-1)]
    caps = [i*last//t for i in range(1,t)]
    greedy = (D+k0)*prod(max(D+ell-i,D+k0-i*last//t) for i in range(1,ell))
    hn,hd = (k1-ell+1,1) if t*(k1-ell+1) <= last else (last,t)
    qn,qd = maximum(old.quotient(ell,k0,k1,greedy),quantitative(ell,k0,hn,hd))
    inner = old.inner(factors,first,last,caps)
    hybrid = (D+left)*prod(corners(left,right,t,k0,r) for r in range(1,11))
    n,d = maximum((qn*inner,qd),(hybrid,1),quantitative(11,left,last,t))
    return reduce_pair(12*n,d)


def main():
    digest = hashlib.sha256()
    peak,blocks,count,mutations = 246756107210901806,0,0,0
    left = LOW
    while left <= HIGH:
        right = min(left+31,HIGH)
        resource = prod(range(R+right-11,R+right+1))
        ln,ld = quantitative(11,left,right-4,7)
        check(ln > 0,"low-density whole-box gate")
        ln *= 12
        hn,hd = 10488*(GAP+left)*prod(range(GAP+1,GAP+11)),125
        if hn*ld < ln*hd:
            ln,ld = hn,hd
        bn,bd = reduce_pair(resource*ld,ln)
        digest.update(f"B:{left},{right}:{bn}/{bd}\n".encode())
        peak = max(peak,bn//bd+ADD)
        for t in range(1,7):
            ell = 11-t
            f = ell*ell//4
            start = 4701 if t==1 else ell
            end = right-t*(right-4)//7-1
            extra = [(D+f*(ell-1))//(f-1)+1]
            for k0,k1 in old.partition(start,end,64,extra):
                cn,cd = cost(left,right,t,k0,k1)
                n,d = resource*cd,cn
                floor = n//d
                check(floor*d <= n < (floor+1)*d,"exact floor")
                for wrong in (floor-1,floor+1):
                    check(not wrong*d <= n < (wrong+1)*d,"incorrect adjacent floor")
                    mutations += 1
                cap = floor+ADD
                check(cap <= TOTAL,"every original record box paid")
                digest.update(f"C:{left},{right},{t},{k0},{k1}:{cn}/{cd}:{cap}\n".encode())
                count += 1
                peak = max(peak,cap)
        left = right+1
        blocks += 1
    check(left == HIGH+1 and peak == TOTAL,"exact endpoints and maximum")
    check(blocks==47 and count==18189 and mutations==36378,"entire independent inventory")
    check(digest.hexdigest() == EXPECTED,"all independent cost values")
    check(2130706433**6//2**128-TOTAL==2084234117366394,"original reserve")
    print("PASS independent",blocks,"blocks",count,"boxes",mutations,"wrong floors")
    print("MAX",peak,"DIGEST",digest.hexdigest())
    print("Unrolled quantitative products and both J corners; full tangent vectors retained")
    print("PASS every carrier on26500..27999; not an unrestricted row proof")


if __name__ == "__main__":
    main()
