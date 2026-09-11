"""Tiny exact original-label controls for the constant-projection fibre census."""
from collections import defaultdict


def need(ok,why):
    if not ok:raise ValueError(why)


P=101


def polynomial(coefficients,x):
    value=0
    for c in reversed(coefficients):value=(value*x+c)%P
    return value


def census_control(values,receiver,projection,labels,A,K,t,sharp=False):
    n=len(receiver)
    need(len(values)==len(projection) and len(labels)==len(set(labels)),"actual pairs/unique labels")
    cores=[{x for x in range(n) if pair[x]==receiver[x]} for pair in values]
    need(all(len(core)>=A for core in cores),"complete original cores")
    fibres=defaultdict(list)
    for i,q in enumerate(projection):fibres[q].append(i)
    unions={q:set().union(*(cores[i] for i in ids)) for q,ids in fibres.items()}
    raw=inside=outside=0;by_pair=defaultdict(set)
    rho=(1,3) if sharp or projection[0][0]=="finite" else (0,1)
    for gamma,(owner,support) in labels.items():
        need(len(support)==A+t and support<=set(range(n)),"selected original support")
        defects=support-cores[owner]
        need(len(defects)==t and 0<t,"positive original raw")
        for x in support:
            a,b=values[owner][x];u,v=receiver[x]
            need((u-a+gamma*(v-b))%P==0,"literal original scalar agreement")
        need(not by_pair[owner].intersection(defects),"same-pair defects disjoint over labels")
        by_pair[owner].update(defects)
        own_union=unions[projection[owner]]
        for x in defects & own_union:
            u,v=receiver[x];a,b=values[owner][x]
            need((rho[0]*(u-a)+rho[1]*(v-b))%P==0,"own-union compatibility")
            need(rho[0]!=0 and gamma==rho[1]*pow(rho[0],-1,P)%P,"one preferred finite label")
        raw+=t;inside+=len(defects & own_union);outside+=len(defects-own_union)
    need(raw==inside+outside and inside<=t,"global inside bound across fibres")
    if rho[0]==0:need(inside==0,"infinite preferred direction adds no finite label")
    for selected in by_pair.values():need(len(selected)<=n-A,"one-pair original weight cap")
    heavy=[q for q,ids in fibres.items() if len(ids)>=2]
    threshold=n-2*A+K-1
    for q in heavy:
        need(n-len(unions[q])<=threshold,"two-pair complete-core threshold")
        ids=fibres[q]
        for a in ids:
            for b in ids:
                if a!=b:need(len(cores[a]&cores[b])<=K-1,"distinct polynomial intersection")
    if sharp:need(len(heavy)==1 and n-len(unions[heavy[0]])==threshold,"sharp threshold attained")
    # Count represented projected polynomials exactly; these are tiny fixture Q caps,
    # not universal ordinary-LIST bounds for the full Reed--Solomon code.
    q_agreements={}
    for q,ids in fibres.items():
        pair=values[ids[0]]
        q_agreements[q]=sum((rho[0]*(receiver[x][0]-pair[x][0])+
                              rho[1]*(receiver[x][1]-pair[x][1]))%P==0 for x in range(n))
    def q_cap(e):return sum(a>=n-e for a in q_agreements.values())
    base=(n-A)*q_cap(n-A)
    rich=0
    for e in range(max(0,threshold)+1):
        ids=[q for q in heavy if n-len(unions[q])==e]
        scalar_cap=max([0]+[len(fibres[q]) for q in ids])
        rich+=e*scalar_cap*q_cap(e)
    need(raw<=t+base+rich,"singleton plus represented projected tails census")
    return len(labels),inside,len(heavy)


def sharp_fixture(t):
    n,K,m=21,3,9;A=m-t
    delta=(-3,1)
    values=[[(0,0) for x in range(n)],
            [tuple(c*x*(x-1)%P for c in delta) for x in range(n)]]
    h0=set(range(A));h1={0,1}|set(range(A,2*A-2))
    union=h0|h1
    receiver=[]
    for x in range(n):
        if x in h0:receiver.append(values[0][x])
        elif x in h1:receiver.append(values[1][x])
        else:receiver.append((1,0))
    chosen=set(sorted(set(range(n))-union)[:t])
    for x in chosen:
        a,b=values[1][x];receiver[x]=((a-4)%P,(b+1)%P)
    labels={3:(0,h0|set(sorted(h1-h0)[:t])),4:(1,h1|chosen)}
    # Each selected support contains >=K core points and a genuine defect.
    # A degree<K joint polynomial pair agreeing on it would equal its owner
    # on those K points and then contradict that defect.
    result=census_control(values,receiver,[("finite",0),("finite",0)],labels,A,K,t,sharp=True)
    need(result==(2,t,1),"sharp fixture exercises original inside/outside ownership")
    return result


def several_fibres(t,infinity):
    n,K,A=61,3,12
    cs=[(0,),(0,),(0,1),(0,1),(1,0,1)]
    hs=[(0,),(1,),(0,1),(1,1),(0,2)]
    values=[]
    for c,h in zip(cs,hs):
        pair=[]
        for x in range(n):
            q,z=polynomial(c,x),polynomial(h,x)
            pair.append((z,q) if infinity else ((q-3*z)%P,z))
        values.append(pair)
    receiver=[values[min(x//12,4)][x] for x in range(n)]
    cores=[{x for x in range(n) if values[i][x]==receiver[x]} for i in range(5)]
    labels={}
    for gamma in range(P):
        for i,pair in enumerate(values):
            defects=[x for x in range(n) if x not in cores[i]
                     and (receiver[x][0]-pair[x][0]+gamma*(receiver[x][1]-pair[x][1]))%P==0]
            if len(defects)>=t:
                labels[gamma]=(i,set(sorted(cores[i])[:A])|set(defects[:t]))
                break
    projection=[("infinite" if infinity else "finite",c) for c in cs]
    result=census_control(values,receiver,projection,labels,A,K,t)
    need(result[0]>0 and result[2]==2,"two rich and one singleton actual fibres")
    if not infinity:need(result[1]==t and 3 in labels,"global finite preferred label attained")
    # The two projected differences X and X^2+1 are independent:
    # the actual projected affine dimension is TWO, not a quotient line.
    need(cs[2]==(0,1) and cs[4]==(1,0,1),"multidimensional projection fixture")
    return result


def main():
    reports=[sharp_fixture(t) for t in (1,2)]
    reports += [several_fibres(t,infinity) for t in (1,2) for infinity in (False,True)]
    need(sum(x[1] for x in reports)==6,"inside charges tracked separately by fixture")
    print("PASS six exact original-label fixtures:",reports)
    print("PASS sharp two-core threshold; multidimensional quotient; singleton/rich fibres; infinity")
    print("Finite fixtures test the owner identities, not the official row or universal LIST theorem")


if __name__=="__main__":
    main()
