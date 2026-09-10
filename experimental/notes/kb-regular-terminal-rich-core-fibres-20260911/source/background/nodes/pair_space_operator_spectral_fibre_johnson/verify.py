"""Small algebraic controls, not a universal source enumeration."""
from fractions import Fraction
from itertools import combinations, product

P=101

def need(ok,why):
    if not ok:
        raise ValueError(why)

def mv(t,v):
    return tuple(sum(a*b for a,b in zip(row,v))%P for row in t)

def cross(a,b):
    return ((a[1]*b[2]-a[2]*b[1])%P,
            (a[2]*b[0]-a[0]*b[2])%P,
            (a[0]*b[1]-a[1]*b[0])%P)

def project(v):
    first=next((x for x in v if x%P),None)
    if first is None:
        return None
    inv=pow(first%P,-1,P)
    return tuple(x*inv%P for x in v)

def eigenvectors(t):
    out=[]
    for lam in range(P):
        rows=[tuple((t[i][j]-(lam if i==j else 0))%P for j in range(3))
              for i in range(3)]
        if sum(a*b for a,b in zip(rows[0],cross(rows[1],rows[2])))%P:
            continue
        v=next((cross(a,b) for a,b in combinations(rows,2) if any(cross(a,b))),None)
        need(v is not None,"the control excludes higher-dimensional eigenspaces")
        need(mv(t,v)==tuple(lam*x%P for x in v),"right eigenvector")
        out.append((lam,v))
    return out

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))%P

def ordinary(x):
    return (1,x,x*(x-1)*(x-2)*(x-3)%P)

def kernel_fixture(x):
    v=(x**3-x)%P
    return (1,v,x*v%P)

def geometry(name,t,basis,degree,expected_e,anchors=()):
    evaluations={x:basis(x) for x in range(P)}
    eig=eigenvectors(t)
    need(len(eig)==expected_e,"spectral stratum: "+name)
    removed=set(anchors)
    if eig:
        removed.update(x for x,v in evaluations.items() if any(dot(v,y)==0 for _,y in eig))
    else:
        removed.update(x for x,v in evaluations.items() if project(v) is None)
    b=len(anchors)+(len(eig)*degree if eig else degree-2)
    need(len(removed)<=b,"root budget")
    omega=set(range(P))-removed
    fibres={}
    for x in omega:
        key=project(evaluations[x])
        need(key is not None,"zero evaluation escaped root mask")
        fibres.setdefault(key,[]).append(x)
    h=max(map(len,fibres.values()),default=0)
    checks=0
    for y in product(range(-2,3),repeat=3):
        if not any(y):
            continue
        ty=mv(t,y)
        hits=[x for x in omega if dot(evaluations[x],y)==dot(evaluations[x],ty)==0]
        need(len(hits)<=h,"finite non-eigen intersection cap")
        if project(ty)==project(y) or not any(ty):
            need(not hits,"eigenvector roots must be removed")
        else:
            need(len({project(evaluations[x]) for x in hits})<=1,
                 "non-eigen intersections lie in one projective evaluation fibre")
        checks+=1
    if name=="split3":
        unmasked=[x for x,v in evaluations.items() if dot(v,(0,0,1))==0]
        need(len(unmasked)==4 and h==1,"root-mask necessity control")
    if name=="irreducible_common":
        need({7,8}<=removed and h==1,"common-zero necessity control")
    if name=="mixed1":
        ell=evaluations[0]
        ell_t=tuple(sum(ell[i]*t[i][j] for i in range(3))%P for j in range(3))
        need(0 in omega and any(ell) and not any(cross(ell,ell_t)),
             "joint-rank-one coordinates may remain, including a zero second row")
    if name=="triple_fibre":
        need(h==3 and set(fibres[project((1,0,0))])=={0,1,100},
             "generic-singleton does not mean maximum fibre one")
    return name,len(eig),len(removed),h,checks

def johnson(n,a,h):
    den=a*a-n*h
    need(0<a<=n and den>0,"positive Johnson gate")
    return Fraction(n*(a-h),den)

def main():
    c=next(c for c in range(1,P) if all((x**3+x+c)%P for x in range(P)))
    nonsplit=((0,0,-c),(1,0,-1),(0,1,0))
    split=((1,0,0),(0,2,0),(0,0,3))
    shared=lambda x: tuple((x-7)*(x-8)*v%P for v in ordinary(x))
    models=[
        ("split3",split,ordinary,4,3,()),
        ("split2",((1,1,0),(0,1,0),(0,0,2)),ordinary,4,2,()),
        ("jordan3",((1,1,0),(0,1,1),(0,0,1)),ordinary,4,1,()),
        ("mixed1",((0,0,0),(0,0,-2),(0,1,0)),ordinary,4,1,()),
        ("irreducible3",nonsplit,ordinary,4,0,()),
        ("irreducible_common",nonsplit,shared,6,0,()),
        ("split_common",split,shared,6,3,(90,91)),
        ("triple_fibre",((0,0,1),(1,0,0),(0,1,0)),kernel_fixture,4,1,()),
    ]
    for args in models:
        print("PASS geometry",geometry(*args))
    fano=[{i,(i+1)%7,(i+3)%7} for i in range(7)]
    need(all(len(s)==3 for s in fano) and all(len(a&b)==1 for a,b in combinations(fano,2)),
         "exact intersection family")
    need(johnson(7,3,1)==7,"sharp set-packing control")
    values=[johnson(101-b,30-b,2) for b in range(10)]
    need(values==sorted(values) and johnson(20,20,1)==1,"deletion monotonicity")
    try:
        eigenvectors(((1,0,0),(0,1,0),(0,0,2)))
    except ValueError:
        pass
    else:
        raise ValueError("multidimensional eigenspace accepted")
    print("PASS 992 pair-direction controls; root masks, common zeros, rank-one evaluations and sharp Johnson control")
    print("Universal theorem uses the written proof; no official MCA source or generic-degree replacement")

if __name__=="__main__":
    main()
