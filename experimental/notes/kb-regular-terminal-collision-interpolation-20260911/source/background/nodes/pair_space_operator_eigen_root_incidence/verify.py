"""Small exact sharpness and hypothesis controls; not an MCA source census."""
from fractions import Fraction as Q
import hashlib
import importlib.util
from itertools import combinations, product
from pathlib import Path

HELPER=Path(__file__).resolve().parent.parent/"pair_space_operator_spectral_fibre_johnson/verify.py"
PIN="5650d8dc31f603bcb58792b38e3b23aa66ab5748e1d318d7125325880f9180a6"

def need(ok,why):
    if not ok:
        raise ValueError(why)

need(hashlib.sha256(HELPER.read_bytes()).hexdigest()==PIN,"matrix helper custody")
spec=importlib.util.spec_from_file_location("spectral_matrix_helpers",HELPER)
alg=importlib.util.module_from_spec(spec)
spec.loader.exec_module(alg)
P=alg.P
CUBE=list(product((0,1),repeat=3))

def sub(a,b):
    return tuple((x-y)%P for x,y in zip(a,b))

def capacities(eig):
    plane=0
    for a,b,c in combinations(CUBE,3):
        normal=alg.cross(sub(b,a),sub(c,a))
        if any(normal):
            plane=max(plane,sum(alg.dot(normal,sub(y,a))==0 for y in CUBE))
    need(plane==4,"cube affine plane capacity; smaller sections have <=2 points")
    for _,v in eig:
        cosets={}
        for y in CUBE:
            key=alg.cross(v,y)
            cosets[key]=cosets.get(key,0)+1
        need(max(cosets.values())<=2,"actual eigenline capacity")
    return 2,plane

def inspect(t,basis,degree,expected_e,zero_free=True):
    eig=alg.eigenvectors(t)
    need(len(eig)==expected_e,"spectral count")
    q1,q2=capacities(eig)
    evaluations={x:tuple(v%P for v in basis(x)) for x in range(P)}
    # Independent evaluation rows also certify polynomial-basis independence.
    rows=list(evaluations.values())
    first=next(v for v in rows if any(v))
    second=next(v for v in rows if any(alg.cross(first,v)))
    need(any(alg.dot(alg.cross(first,second),v) for v in rows),"three-dimensional carrier")
    if zero_free:
        need(all(any(v) for v in rows),"common-zero guard")
    roots={x for x,v in evaluations.items() if any(alg.dot(v,y)==0 for _,y in eig)}
    incidence=0
    ranks={0:0,1:0,2:0}
    for x in roots:
        ell=evaluations[x]
        ell_t=tuple(sum(ell[i]*t[i][j] for i in range(3))%P for j in range(3))
        rank=0 if not any(ell) else (2 if any(alg.cross(ell,ell_t)) else 1)
        ranks[rank]+=1
        hits=sum(alg.dot(ell,y)==alg.dot(ell_t,y)==0 for y in CUBE)
        incidence+=hits
        if rank==2:
            need(hits<=q1,"root section is an actual eigenline")
        elif rank==1:
            need(hits<=q2,"rank-one section is an actual plane")
    cap=degree*(0,q2,q2+q1,Q(3*q2,2))[expected_e]
    if zero_free:
        need(incidence<=cap,"spectral incidence inequality")
        for a,b in combinations(CUBE,2):
            y=sub(a,b)
            ty=alg.mv(t,y)
            shared=[x for x,ell in evaluations.items() if x not in roots
                    and alg.dot(ell,y)==alg.dot(ell,ty)==0]
            need(len(shared)<=degree-1,"natural degree intersection cap")
    return incidence,cap,ranks

def split_basis(x):
    a,b,c=x*(x-1),(x-2)*(x-3),(x-4)*(x-5)
    return b*c,a*c,a*b

def partial_basis(x):
    g=x*(x-1)*(x-2)
    return g,x*g,(x-3)*(x-4)*(x-5)*(x-6)

def main():
    split=((1,0,0),(0,2,0),(0,0,3))
    partial=((1,1,0),(0,1,0),(0,0,2))
    sharp=inspect(split,split_basis,4,3)
    need(sharp==(24,Q(24),{0:0,1:6,2:0}),"sharp factor3/2 control")
    repeated=inspect(partial,partial_basis,4,2)
    need(repeated==(20,24,{0:0,1:3,2:4}) and repeated[0]>4*4,
         "repeated eigenvalue defeats naive D*q2")
    common=lambda x:tuple((x-9)*v for v in split_basis(x))
    unguarded=inspect(split,common,5,3,False)
    need(unguarded[0]==32>unguarded[1]==30,"common zero defeats unguarded capacity")
    try:
        inspect(split,common,5,3)
    except ValueError as error:
        need(str(error)=="common-zero guard","intended guard rejection")
    else:
        raise ValueError("common zero accepted")
    c=next(c for c in range(1,P) if all((x**3+x+c)%P for x in range(P)))
    models=[("nilpotent",((0,1,0),(0,0,1),(0,0,0)),1),
            ("mixed",((0,0,0),(0,0,-2),(0,1,0)),1),
            ("irreducible",((0,0,-c),(1,0,-1),(0,1,0)),0)]
    for name,t,e in models:
        print("PASS",name,inspect(t,partial_basis,4,e))
    # The Fano set-packing equality must not pass a strict contradiction gate.
    def energy(n,a,m,b,h):
        s=m*a-b
        return s>=n and s*s-n*s>n*m*(m-1)*h
    need(not energy(7,3,7,0,1) and energy(7,3,8,0,1),"strict fixed-M gate")
    print("PASS split sharpness",sharp,"repeated spectrum",repeated)
    print("PASS common-zero countercontrol",unguarded)
    print("Actual cube counts, natural degree cap and strict energy tested; universal proof is written")

if __name__=="__main__":
    main()
