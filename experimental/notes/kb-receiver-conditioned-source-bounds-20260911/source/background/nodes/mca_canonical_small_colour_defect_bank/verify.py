"""Exhaustive tiny canonical selections, receiver colours and defect-tuple controls."""
from collections import Counter
from itertools import combinations

P=17


def need(ok,why):
    if not ok:raise ValueError(why)


def check(kind):
    zero=kind=="linear_zero";domain=tuple(range(13)) if zero else tuple(range(1,13))
    groups=[(0,0)]*6+[(1,1)]*3+[(2,3),(4,7),(5,9)]
    u={};v={};base={};carrier={}
    for x,(a,b) in zip(range(1,13),groups):
        lam=x if zero else 1
        base[x]=(1+2*x)%P if zero else 0;carrier[x]=lam
        u[x]=(base[x]+lam*a)%P;v[x]=lam*b%P
    if zero:base[0]=1;carrier[0]=0;u[0]=P-1;v[0]=1
    K,m=(2,7) if zero else (1,6)
    need(m-K==5,"canonical guard")
    selected={};support_count=0;pointwise=[]
    for gamma in range(P):
        best=None
        for h in range(P):
            A=tuple(x for x in domain if (u[x]+gamma*v[x]-base[x]-h*carrier[x])%P==0)
            for S in combinations(A,m):
                # Full degree<K containment is checked independently of the carrier.
                if zero:
                    x,y=S[:2];slope=(v[y]-v[x])*pow(y-x,-1,P)%P
                    intercept=(v[x]-slope*x)%P
                    bad=any((intercept+slope*x-v[x])%P for x in S)
                else:bad=len({v[x] for x in S})>1
                scores=[sum((v[x]-b*carrier[x])%P!=0 for x in S) for b in range(P)]
                raw=min(scores);need((raw>0)==bad,"literal full-code badness in this control")
                if not bad:continue
                support_count+=1
                pointwise.append((gamma,h,S,raw))
                record=(raw,h,S,scores.index(raw),A)
                if best is None or record[:3]>best[:3]:best=record
        if best:selected[gamma]=best
    colours={}
    for x in domain:
        if carrier[x]:
            inverse=pow(carrier[x],-1,P)
            colours[x]=((u[x]-base[x])*inverse%P,v[x]*inverse%P)
    counts=Counter(colours.values())
    zero_labels={(- (u[x]-base[x])*pow(v[x],-1,P))%P for x in domain if not carrier[x] and v[x]}
    need(zero_labels==({2} if zero else set()),"zero evaluation labels paid globally")
    low_counts=[]
    for t in (1,2):
        need(2*t<m-K,"strict low guard")
        bank={x for x in colours if counts[colours[x]]<=t}
        need(len(bank)==3,"small receiver colours, not small evaluation fibres")
        owned=set();raw_sum=0;low=0
        for gamma,(raw,h,S,b,A) in selected.items():
            if raw>t or gamma in zero_labels:continue
            defects={x for x in A if (v[x]-b*carrier[x])%P}
            core=set(A)-defects
            need(len(defects)==raw and defects<=set(S) and defects<=bank,"complete canonical defects")
            scores=[sum((v[x]-candidate*carrier[x])%P!=0 for x in A) for candidate in range(P)]
            need(scores.count(min(scores))==1 and scores[b]==raw,"unique full-agreement minimizer")
            H=sorted(core)[:m-t]
            tuples={(x,y) for x in H for y in defects}|{(y,x) for x in H for y in defects}
            need(len(tuples)==2*(m-t)*raw and not owned.intersection(tuples),"disjoint all-defect tuples")
            for x,y in tuples:
                need((v[x]*carrier[y]-v[y]*carrier[x])%P!=0,"independent incidence normals")
                need(x in bank or y in bank,"every tuple hits the small-colour bank")
            owned.update(tuples);raw_sum+=raw;low+=1
        universe=len(domain)*(len(domain)-1)
        misses=(len(domain)-len(bank))*(len(domain)-len(bank)-1)
        need(2*(m-t)*raw_sum<=universe-misses,"restricted universe")
        low_counts.append(low)
    # A nonmaximizing raw-one support uses the three-point colour and fails the bank.
    witnesses=[r for r in pointwise if r[0]==16 and r[3]==1]
    need(witnesses and selected[16][0]==3,"maximizing selection is necessary")
    gamma,h,S,_=witnesses[0]
    scores=[sum((v[x]-b*carrier[x])%P!=0 for x in S) for b in range(P)]
    b=scores.index(1);defects={x for x in S if (v[x]-b*carrier[x])%P}
    need(any(x in colours and counts[colours[x]]==3 for x in defects),"actual noncanonical bank violation")
    return support_count,len(selected),low_counts


def main():
    for kind in ("constant","linear_zero"):
        print("PASS",kind,"bad supports / labels / retained low counts",check(kind))
    for n in range(2,9):
        for size in range(n+1):
            bank=set(range(size));tuples=list(combinations(range(n),2))
            hit=2*sum(bool(bank.intersection(pair)) for pair in tuples)
            need(hit==n*(n-1)-(n-size)*(n-size-1),"all small bank sizes")
    print("PASS canonical scope, unique defects, zero-label peel and restricted tuple universe")
    print("Tiny complete selections are controls; the all-field statement has a hand proof")


if __name__=="__main__":
    main()
