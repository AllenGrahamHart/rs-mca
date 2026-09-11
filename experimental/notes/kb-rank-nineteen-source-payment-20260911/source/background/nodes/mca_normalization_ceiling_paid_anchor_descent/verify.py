"""Tiny exact controls for the geometric ceiling envelope and paid-overlap inequality."""
from fractions import Fraction as Q
from functools import lru_cache
from math import comb


def need(ok,why):
    if not ok:raise ValueError(why)


@lru_cache(maxsize=None)
def beta(s,H,nu,image):
    h=H//nu+1;maximum=image-h*(s-2)
    if maximum<1:return 0
    branch=min(maximum,max(1,h-2));genus=comb(image-s+2,2)
    result=nu*(genus*branch//comb(branch+h-1,2))
    brute=max(nu*(genus*b//comb(b+h-1,2)) for b in range(1,maximum+1))
    need(result==brute,"branch-ratio closed form agrees with every allowed tiny branch count")
    return result


def main():
    triples=partitions=0
    for s in range(4,7):
        for H in range(1,11):
            for upper in range(s-1,36):
                limit=min(H,upper//(s-1))
                exact=[]
                for nu in range(1,limit+1):
                    endpoint=beta(s,H,nu,upper//nu)
                    for image in range(s-1,upper//nu+1):
                        need(beta(s,H,nu,image)<=endpoint,"monotone image degree over every physical tiny triple")
                        triples+=1
                    exact.append(endpoint)
                lo=1;covered=[];candidates=[]
                while lo<=limit:
                    image=upper//lo;q=H//lo
                    hi=min(limit,upper//image,H//q)
                    need(all(upper//nu==image and H//nu==q for nu in range(lo,hi+1)),"both constant quotient cells")
                    covered.extend(range(lo,hi+1));candidates.append(beta(s,H,hi,image));lo=hi+1
                need(covered==list(range(1,limit+1)) and max(candidates)==max(exact),"complete quotient endpoint maximum")
                partitions+=1
    overlap=ratios=0
    for C in map(Q,(0,1,5)):
        for F in map(Q,(0,2,7)):
            for T in map(Q,(0,3,9)):
                for e,z in ((0,0),(1,0),(0,1),(1,1)):
                    actual=F if e else T if z else C
                    price=C+e*max(F-C,0)+z*max(T-C,0)
                    need(actual<=price,"overlap needs no disjoint exceptional-set assumption")
                    overlap+=1
                for lo,hi in ((0,2),(3,7)):
                    for geometric in (0,2,99):
                        def price(kappa,v):
                            return ((27+kappa+v)*C+(kappa+3)*max(F-C,0)+geometric*max(T-C,0))/(12+kappa+v)
                        upper=max(C,price(lo,0),price(hi,0))
                        for kappa in range(lo,hi+1):
                            for v in (0,1,100):
                                need(price(kappa,v)<=upper,"all kappa/v and geometric budgets above A")
                                ratios+=1
    print("PASS",triples,"physical tiny degree triples;",partitions,"complete quotient partitions")
    print("PASS",overlap,"overlap cases;",ratios,"exact affine-ratio comparisons")
    print("Includes geometric budgets larger than the core; no discarded-coordinate denominator")
    print("Controls check formulas, not official MCA witnesses; the uniform geometric proof is inherited")


if __name__=="__main__":
    main()
