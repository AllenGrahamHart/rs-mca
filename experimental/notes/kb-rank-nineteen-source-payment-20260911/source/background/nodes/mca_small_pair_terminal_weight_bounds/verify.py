"""Literal original-label and integer line-price controls over F13."""
P=13
N,J,R,D=13,2,11,3


def need(ok,why):
    if not ok:raise ValueError(why)


def main():
    instances=labels=inside_total=outside_total=0
    for nonconstant in (False,True):
        pairs=[[(c*x%P,c) if nonconstant else (0,c) for x in range(P)] for c in (1,2,3)]
        receiver=[pairs[x//4][x] for x in range(12)]+[(5,7)]
        cores=[{x for x in range(P) if f[x]==receiver[x]} for f in pairs]
        need(all(len(C)==4 for C in cores),"complete actual cores")
        union=set.union(*cores);e=N-len(union);need(e==1,"original core-union complement")
        for rotation in range(3):
            for t in (1,2):
                selected=[]
                for gamma in range(P):
                    for i in [(rotation+j)%3 for j in range(3)]:
                        agreements={x for x in range(P)
                                    if (receiver[x][0]+gamma*receiver[x][1]
                                        -pairs[i][x][0]-gamma*pairs[i][x][1])%P==0}
                        if len(agreements)<D+J:continue
                        raw=D+J-len(cores[i]);need(raw==1<=t,"original raw, not remapped after restriction")
                        defect=min(agreements-cores[i]);selected.append((gamma,i,defect));break
                need(len({gamma for gamma,_,_ in selected})==len(selected),"one owner per original label")
                inside=[x for _,_,x in selected if x in union]
                outside=[(i,x) for _,i,x in selected if x not in union]
                need(len(inside)==len(set(inside)) and len(outside)==len(set(outside)),"global inside and per-pair outside disjointness")
                if not nonconstant:need(len(inside)<=t,"one constant preferred finite label")
                m=len({i for _,i,_ in selected});h=int(nonconstant);ct=R-D+t
                cap=(R+1+h-e)//(D+1-t+h)
                bound=min(m*ct,(t if h==0 else N-e)+m*e)
                need(1<=m<=cap and len(selected)<=bound,"integer population and original weight")
                for i in range(3):need(sum(j==i for _,j,_ in selected)<=ct,"same-pair original weight")
                labels+=len(selected);inside_total+=len(inside);outside_total+=len(outside);instances+=1
    checks=0
    for t in (1,2):
        ct=R-D+t
        for low,high in ((0,0),(1,2),(3,4)):
            for gate in range(ct):
                den=D+1-t+low
                top=(R+1+low-gate-1)//den
                envelope=0
                for m in range(1,top+1):
                    end=min(ct,R+1+low-m*den)
                    envelope=max(envelope,min(m*ct,t+m*end if low==0 else N+(m-1)*end))
                for h in range(low,high+1):
                    for e in range(gate+1,ct+1):
                        for m in range(1,(R+1+h-e)//(D+1-t+h)+1):
                            weight=min(m*ct,t+m*e if h==0 else N+(m-1)*e)
                            need(weight<=envelope,"all integer heights/complements/populations in toy bands")
                            checks+=1
    print("PASS",instances,"literal F13 owner assignments;",labels,"labels;",inside_total,"inside;",outside_total,"outside defects")
    print("PASS",checks,"integer line-envelope comparisons; no large field enumeration")
    print("Controls are not official row witnesses; the uniform statements have separate proofs")


if __name__=="__main__":
    main()
