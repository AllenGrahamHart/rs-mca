"""Exact flat-split moment formula and tiny actual-polynomial controls."""

from fractions import Fraction as F
import importlib.util
from itertools import combinations
from pathlib import Path


ROOT=Path(__file__).resolve().parents[1]


def load(name,node):
    spec=importlib.util.spec_from_file_location(name,ROOT/node/"verify.py")
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


p=load("original_rank_profile","mca_rank_profile_density_basis_product")


def need(ok,why):
    if not ok:
        raise ValueError(why)


def moment(n,k,r):
    need(n>k>=r>=1,"actual quotient moment parameters")
    if r==1:
        return F(n*n)
    return max(F(n*(k-1),r-1),F(n+(k-r+1)*(k-r)))


def root_lower(D,K0,K1,s,t,a0,a1,h,C=None):
    need(D>=1 and 3<=s<=K0<=K1 and 1<=t<s and t<=a0<=a1<=K1-s+t
         and h>=1 and (C is None or C>=0),"root-moment degree/flat/density box")
    h=F(h)
    N0,k1,ell=D+K0,K1-a0,s-t
    mu=p.profile(D,K0,K1,s,h)
    q=min(F(h),(K1-1)*mu[s],
          (a1*h+min((D+k1)*h,moment(D+k1,k1,ell)))/N0)
    if C is not None:
        q=min(q,1+F(C,N0))
    if K0-q<1:
        return F(0)
    return N0*p.product(D,K0-q,s-1,mu)


def main():
    b=load("balanced_actual_geometry","mca_balanced_basis_under_flat_density")
    mono=lambda k,powers: [tuple(int(i==v) for i in range(k)) for v in powers]
    locator=b.c.locator(range(10),17)
    big=[[1]+[0]*11,locator+[0],[0]+locator]
    sources=[(17,4,list(range(9)),mono(4,range(4))),
             (23,7,[x%23 for x in range(-8,9) if x],mono(7,(0,2,4,6))),
             (17,12,list(range(13)),big),
             (17,12,list(range(13)),[big[0],[0,1]+[0]*10,big[1],big[2]])]
    count,nonmax=0,0
    for field,K,points,polys in sources:
        rows=b.c.rows_for(polys,points,field)
        N,s=len(rows),len(polys)
        need(N>K>=s and b.rank(rows,field)==s and all(any(row) for row in rows),
             "actual polynomial core")
        flats={}
        for t in range(1,s):
            for indices in combinations(range(N),t):
                basis=[rows[i] for i in indices]
                if b.rank(basis,field)!=t:
                    continue
                closed=tuple(i for i,row in enumerate(rows) if b.rank(basis+[row],field)==t)
                flats.setdefault((t,closed),indices)
        h=max(F(len(A),t) for t,A in flats)
        fibers=[A for t,A in flats if t==1]
        S2=sum(len(A)**2 for A in fibers)
        bases=b.c.basis_count(rows,field,s)
        for (t,A),indices in flats.items():
            a=len(A)
            ell,k=s-t,K-a
            split=a*h+min((N-a)*h,moment(N-a,k,ell))
            need(S2<=split and S2<=N*h,"actual split original moment")
            lower=root_lower(N-K,K,K,s,t,a,a,h)
            collision=root_lower(N-K,K,K,s,t,a,a,h,S2-N)
            need(0<lower<=collision<=bases,"actual root-product lower bounds")
            a0,a1=max(t,a-1),min(K+1-ell,a+1)
            wide=root_lower(N-K,max(s,K-1),K+1,s,t,a0,a1,max(h,F(a1,t)),S2-N)
            need(0<=wide<=bases,"whole-box actual-source control")
            nonmax+=F(a,t)<h
            count+=1
        print("ACTUAL",field,K,N,s,"density",h,"moment",S2,"bases",bases,
              "complete flats",len(flats),flush=True)
    need(count>0 and nonmax>0,"nonmaximizing flats actually tested")
    for C in (None,180000000):
        args=(67466,22500,22515,11,5,16000,16250)
        integer=root_lower(*args,3250,C)
        need(isinstance(integer,F) and integer==root_lower(*args,F(3250),C),
             "integral density never introduces floating-point division")
    for bad in ((0,11,11,11,6,6,6,F(1)),
                (3,11,10,11,6,6,6,F(1)),
                (3,11,11,11,11,11,11,F(1)),
                (3,11,11,11,6,5,6,F(1))):
        try:
            root_lower(*bad)
        except ValueError:
            pass
        else:
            raise ValueError("accepted invalid moment box")
    print("PASS",count,"actual flat controls;",nonmax,"nonmaximizers; four invalid boxes rejected")


if __name__=="__main__":
    main()
