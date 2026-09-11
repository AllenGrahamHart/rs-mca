"""Small actual-collision and product-rank controls, not a source census."""
from itertools import combinations
from math import comb

def need(ok,why):
    if not ok:
        raise ValueError(why)

def hilbert(eta,ell):
    return comb(ell+2,2)-(comb(ell-eta+2,2) if ell>=eta else 0)

def rank(rows,p):
    a=[list(row) for row in rows]
    r=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][j]%p),None)
        if pivot is None:
            continue
        a[r],a[pivot]=a[pivot],a[r]
        inverse=pow(a[r][j]%p,-1,p)
        a[r]=[v*inverse%p for v in a[r]]
        for i in range(len(a)):
            if i!=r:
                scale=a[i][j]
                a[i]=[(x-scale*y)%p for x,y in zip(a[i],a[r])]
        r+=1
    return r

def collisions(p,s,roots,scalars):
    # Coefficients of scalar*(Z-root)^2; T is differentiation in Z, not X.
    family=[(0,0,0)]+[(c*u*u%p,-2*c*u%p,c) for u in roots for c in scalars]
    best={}
    excess=0
    fibre_sizes={}
    for x in range(p):
        z=pow(x,s,p)
        key=(1,z,z*z%p)
        fibre_sizes[key]=fibre_sizes.get(key,0)+1
        hits=[i for i,(a,b,c) in enumerate(family)
              if (a+b*z+c*z*z)%p==0 and (b+2*c*z)%p==0]
        excess+=max(len(hits)-1,0)
        if len(hits)>=2 and len(hits)>len(best.get(key,())):
            best[key]=hits
    used=set()
    conditions=0
    for hits in best.values():
        pairs=set(combinations(hits,2))
        need(not pairs&used,"actual unordered-pair ownership")
        used.update(pairs)
        conditions+=comb(len(hits),2)
    need(conditions<=comb(len(family),2),"fat-jet condition budget")
    return len(family),conditions,excess,max(fibre_sizes.values())

def main():
    checks=0
    for eta in range(2,11):
        for s in (1,2,3):
            for ell in range(21):
                exponents={s*(i+eta*j) for i in range(ell+1) for j in range(ell-i+1)}
                need(len(exponents)==hilbert(eta,ell),"exact monomial product rank")
                checks+=1
    need(collisions(101,1,range(5),(1,))==(6,5,5,1),"five actual conic collisions")
    rows=[(1,u,u*u,u*u,u**3,u**4) for u in range(5)]
    need(rank(rows,101)==5 and comb(4,2)==6>5==hilbert(2,2),
         "full ternary dimension is not pullback rank")
    # The only quadratic through these five conic points is the image equation.
    need(all(row[2]-row[3]==0 for row in rows),"zero-pullback kernel equation")
    weighted=collisions(101,1,range(4),(1,2))
    need(weighted==(9,12,8,1) and hilbert(2,6)>12 and 8<=2*6,
         "weighted jets cost binom(r,2), not r-1")
    composed=collisions(97,3,(1,),(1,2))
    need(composed==(3,3,6,3) and hilbert(2,2)>3 and 6<=6*2,
         "finite compositional fibres retained")
    need(sum(pow(x,3,97)==1 for x in range(97))==3,
         "image degree two is not finite fibre maximum three")
    print("PASS",checks,"formal product-rank controls; no evaluation-rank aliasing")
    print("PASS actual pair ownership, weighted collision jets and repeated finite fibres")
    print("PASS five-point conic rejects the full-form-dimension shortcut")
    print("Written universal proof required; no official MCA source or Prize witness")

if __name__=="__main__":
    main()
