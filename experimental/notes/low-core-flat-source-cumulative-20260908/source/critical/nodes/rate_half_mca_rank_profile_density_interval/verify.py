"""Exact box certificate; the universal source argument is in proof.md."""

from fractions import Fraction as F
import hashlib
import importlib.util
from math import prod
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name, node):
    spec = importlib.util.spec_from_file_location(name,ROOT/node/"verify.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


v = load("first_excess_counts","rate_half_mca_first_excess_core_interval")
p = load("rank_profile_product","mca_rank_profile_density_basis_product")
D,R,d,NEAR = 67466,1048576,67472,134944
LOW,HIGH = 24000,26499
FIBER_TOTAL = 246756107210901806
TARGET = 273123695048315164
EXPECTED_DIGEST = "2dc6c17b530fa45a8f40864f9910ddb873492217f3785acf875a9946b2441e36"


def need(ok,why):
    if not ok:
        raise ValueError(why)


def profile_bound(rank,k0,k1,h):
    return p.bound(D,k0,k1,rank,h)


def completion(J0,J1,t,k0,r):
    J = J0 if r <= t else J1
    return max(D+11-r,D+J-r*(J-k0)//t)


def cost(J0,J1,t,k0,k1):
    ell = 11-t
    b0,b1 = J0-k1,J1-k0
    ds = [completion(J0,J1,t,k0,10-i) for i in range(t)]
    caps = {i:i*b1//t for i in range(1,t+1)}
    greedy = (D+k0)*prod(max(D+ell-i,D+k0-i*b1//t) for i in range(1,ell))
    quotient = max(v.quotient(ell,k0,k1,greedy),
                   profile_bound(ell,k0,k1,min(F(k1-ell+1),F(b1,t))))
    inside = v.inside(ds,b0,b1,caps)
    hybrid = (D+J0)*prod(completion(J0,J1,t,k0,r) for r in range(1,11))
    full = profile_bound(11,J0,J1,F(b1,t))
    return 12*max(quotient*inside,hybrid,full)


def cover(rows):
    need(rows and rows[0][0] == LOW and rows[-1][1] == HIGH,"degree endpoints")
    need(all(a<=b for a,b in rows) and all(a[1]+1==b[0] for a,b in zip(rows,rows[1:])),
         "full consecutive degree partition")


def main():
    rows = [(a,min(a+31,HIGH)) for a in range(LOW,HIGH+1,32)]
    cover(rows)
    digest = hashlib.sha256()
    peak,count,mutations = (FIBER_TOTAL,("fiber",)),0,0
    for J0,J1 in rows:
        resource = prod(R+J1-i for i in range(12))
        low = 12*profile_bound(11,J0,J1,F(J1-4,7))
        high = F(10488,125)*(d+J0)*prod(d+i for i in range(1,11))
        need(low>0,"low-core quantitative gate")
        basic = F(resource)/min(low,high)
        digest.update(f"B:{J0},{J1}:{basic.numerator}/{basic.denominator}\n".encode())
        local = (int(basic)+NEAR,("low-density/HIGH",))
        for t in range(1,7):
            ell = 11-t
            lower,upper = (4701 if t==1 else ell),J1-t*(J1-4)//7-1
            f = ell*ell//4
            extra = [(D+f*(ell-1))//(f-1)+1]
            for k0,k1 in v.bins(lower,upper,64,extra):
                value = cost(J0,J1,t,k0,k1)
                quotient = F(resource)/value
                floor = int(quotient)
                need(floor<=quotient<floor+1,"exact floor")
                for wrong in (floor-1,floor+1):
                    need(not wrong<=quotient<wrong+1,"reject adjacent wrong floor")
                    mutations += 1
                cap = floor+NEAR
                digest.update(f"C:{J0},{J1},{t},{k0},{k1}:{value.numerator}/{value.denominator}:{cap}\n".encode())
                count += 1
                if cap>local[0]:
                    local=cap,(t,k0,k1)
        if local[0]>peak[0]:
            peak=local[0],(J0,J1,local[1])
        print("BLOCK",J0,J1,local,flush=True)
    need(peak==(TARGET,(24000,24031,(1,4701,4949))),"exact maximum")
    need(len(rows)==79 and count==30565 and mutations==61130,"complete certificate inventory")
    need(digest.hexdigest()==EXPECTED_DIGEST,"every exact cost")
    need(2130706433**6//2**128-TARGET==1857033063079923,"original reserve")
    need(FIBER_TOTAL<peak[0]<274929007493481160,"source alternative and old union")
    broken = [rows[1:],rows[:-1],rows+[rows[-1]],rows[:20]+rows[21:],
              [(LOW-1,rows[0][1])]+rows[1:]]
    for changed in broken:
        try:
            cover(changed)
        except ValueError:
            pass
        else:
            raise ValueError("accepted broken degree cover")
    print("TOTAL",peak,"blocks",len(rows),"boxes",count,"wrong floors",mutations,
          "digest",digest.hexdigest(),flush=True)
    print("PASS all-carrier interval with five rejected covers; unrestricted MCA remains OPEN")


if __name__ == "__main__":
    main()
