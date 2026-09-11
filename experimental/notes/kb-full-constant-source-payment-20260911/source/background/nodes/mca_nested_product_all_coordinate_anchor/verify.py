"""Small exact nested-product anchor and affine-ratio controls."""
from fractions import Fraction as Q
import importlib.util
from pathlib import Path

PATH=Path(__file__).resolve().parent.parent/"pair_space_regular_projection_anchor/verify.py"
spec=importlib.util.spec_from_file_location("product_anchor_linear_algebra",PATH)
linear=importlib.util.module_from_spec(spec);spec.loader.exec_module(linear)
P=97


def need(ok,why):
    if not ok:raise ValueError(why)


def trim(a):
    a=[x%P for x in a]
    while a and not a[-1]:a.pop()
    return a


def product(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%P
    return trim(out)


def divide(a,b):
    a=trim(a);b=trim(b);need(bool(b),"nonzero divisor")
    q=[0]*max(0,len(a)-len(b)+1)
    while len(a)>=len(b):
        pos=len(a)-len(b);v=a[-1]*pow(b[-1],-1,P)%P;q[pos]=v
        for i,x in enumerate(b):a[pos+i]=(a[pos+i]-v*x)%P
        a=trim(a)
    return trim(q),a


def gcd(a,b):
    a=trim(a);b=trim(b)
    while b:a,b=b,divide(a,b)[1]
    return [x*pow(a[-1],-1,P)%P for x in a] if a else []


def at(a,x):
    y=0
    for value in reversed(a):y=(y*x+value)%P
    return y


def rank(rows):
    if not rows:return 0
    length=max(map(len,rows))
    return len(linear.rref([v+[0]*(length-len(v)) for v in rows],P)[1])


def combine(v,basis):
    return [sum(v[j]*basis[j][i] for j in range(len(basis)))%P for i in range(len(basis[0]))]


def main():
    anchors=roots=cases=0
    for s in range(1,12):
        for c in range(min(3,s-1)+1):
            b=s-c
            for kappa in ((0,3) if c else (0,)):
                degree=s-1+kappa;length=degree+1
                pad=lambda v:v+[0]*(length-len(v))
                common=[1]
                for x in range(kappa+c):common=product(common,[-x,1])
                B=[pad([0]*j+common) for j in range(b)]
                V=B+[pad([0]*j+[1]) for j in range(c)]
                need(rank(V)==s and rank(B)==b,"nested carrier dimensions")
                full=V[0]
                for v in V[1:]:full=gcd(full,v)
                need(trim(full)==[1],"primitive shared carrier")
                observed=0
                for x in range(P):
                    is_root=not any(at(v,x) for v in B)
                    vk=linear.kernel([[at(v,x) for v in V]],P)
                    bk=linear.kernel([[at(v,x) for v in B]],P)
                    child_v=[combine(v,V) for v in vk]
                    child_b=[combine(v,B) for v in bk]
                    need(len(child_v)==s-1 and len(child_b)==b-int(not is_root),"rank-one/two child split")
                    need(rank(child_v+child_b)==s-1,"child B remains in shared V")
                    zero=[0]*length
                    pairs=[v+zero for v in V]+[zero+v for v in B]
                    matrix=[[at(v[:length],x) for v in pairs],[at(v[length:],x) for v in pairs]]
                    pk=linear.kernel(matrix,P)
                    actual=[combine(v,pairs) for v in pk]
                    expected=[v+zero for v in child_v]+[zero+v for v in child_b]
                    child_dimension=2*s-c-(1 if is_root else 2)
                    need(len(actual)==child_dimension and rank(actual+expected)==child_dimension,"exact product agreement section")
                    new_c=(s-1)-len(child_b)
                    need(new_c==c-int(is_root),"root codimension drops by one")
                    if child_v:
                        full=child_v[0]
                        for v in child_v[1:]:full=gcd(full,v)
                        need(at(full,x)==0,"full shared gcd includes the anchor")
                        normalized=[]
                        for v in child_v+child_b:
                            quotient,remainder=divide(v,full)
                            need(not remainder,"divide only polynomial differences by shared full gcd")
                            normalized.append(quotient)
                        d1=max(len(trim(v))-1 for v in normalized)
                        need(d1<=degree-1 and 0<=d1-(s-2)<=kappa,"primitive degree excess cannot increase")
                        need(rank(normalized[:s-1])==s-1,"normalization is injective")
                    else:
                        need(s==1 and b==1 and c==0 and not child_b,"single-pair terminal")
                    anchors+=1;observed+=is_root
                need(observed==(kappa+c if c else 0),"exact common-root bound including large shared degree")
                roots+=observed;cases+=1
    identities=0
    for c in (1,2,3):
        s=c+1
        for C in map(Q,range(4)):
            for F in map(Q,range(5)):
                for lo,hi in ((0,2),(3,7)):
                    extra=max(Q(0),F-C)
                    bound=max(C,*[((23+s+x)*C+(x+c)*extra)/(9+s+x-1) for x in (lo,hi)])
                    for x in range(lo,hi+1):
                        for v in (0,1,99):
                            value=((23+s+x+v)*C+(x+c)*extra)/(9+s+x-1+v)
                            need(value<=bound,"affine-ratio endpoints and unused-degree limit")
                            identities+=1
    print("PASS",cases,"nested product carriers;",anchors,"exact anchor sections;",roots,"rank-one root sections")
    print("PASS full-gcd degree transport and",identities,"exact affine-ratio controls")
    print("Root pair rank drops by ONE, not two. Fixtures are not official MCA source witnesses.")


if __name__=="__main__":
    main()
