"""Tiny exact profile trimming and actual complete-core basis controls."""
from itertools import combinations,product

def need(ok,why):
    if not ok:raise ValueError(why)

def trim(weights,M,cost):
    left=M;value=0
    for w in sorted(weights,reverse=True):
        take=min(left,w);value+=take*cost(w);left-=take
        if not left:return value
    raise ValueError("insufficient coordinate mass")

def main():
    checks=cores=tails=0
    for weights in ((2,1,1,1,1),(4,3,2,1),(3,3,2,2),(5,2,2,1,1)):
        K=max(weights)+1
        for M in range(K,sum(weights)+1):
            for power in (1,2,3):
                F=lambda k:k**power+1
                cost=lambda w:F(K-w)
                want=trim(weights,M,cost)
                exact=min(sum(x*cost(w) for x,w in zip(xs,weights))
                          for xs in product(*(range(w+1) for w in weights)) if sum(xs)==M)
                need(want==exact,"largest-first coordinate allocation");checks+=1
                for bits in product((0,1),repeat=len(weights)):
                    if sum(b*w for b,w in zip(bits,weights))>=M:
                        need(want<=sum(b*w*cost(w) for b,w in zip(bits,weights)),"complete class core relaxation")
                        cores+=1
                for cutoff in range(1,max(weights)+1):
                    E=max(cutoff,sum(w for w in weights if w>cutoff))
                    if E<=K-1:
                        bound=(M-E)*F(K-cutoff)+E*F(K-E)
                        need(want>=bound,"heavy coordinate mass, not number of classes");tails+=1
    weights=(5,1,1,1,1,1);K=6;M=6;F=lambda k:k*k+1
    need(trim(weights,M,lambda w:F(K-w))==36<6*F(5),"class-count substitution is false")
    p=17;fibres={}
    for x in range(1,p):fibres.setdefault(x*x%p,[]).append(x)
    core={xs[0] for xs in fibres.values()};core.add(next(iter(fibres.values()))[1])
    colour_sizes=[]
    for xs in fibres.values():
        groups={}
        for x in xs:groups.setdefault((0,0) if x in core else (1,1),[]).append(x)
        colour_sizes.extend(map(len,groups.values()))
    need(sorted(colour_sizes)==[1]*14+[2] and len(core)==9,"actual receiver colours")
    bases=0
    for x,y,z in combinations(sorted(core),3):
        a,b,c=x*x%p,y*y%p,z*z%p
        det=(b*c*c-c*b*b)-(a*c*c-c*a*a)+(a*b*b-b*a*a)
        bases+=6*bool(det%p)
    D=4;F=lambda k:(D+k)*(D+1)
    lower=trim(colour_sizes,9,lambda w:F(5-w))
    need(bases==462 and lower==350>9*F(3)==315,"actual complete-core improvement")
    print("PASS",checks,"exact allocations;",cores,"complete-core controls;",tails,"tail-mass bounds")
    print("PASS F17 core:462 actual bases >=350 trimmed bound >315 maximum-only bound")
    print("Class units and full-core contraction have hand proofs; no Prize-source enumeration")

if __name__=="__main__":
    main()
