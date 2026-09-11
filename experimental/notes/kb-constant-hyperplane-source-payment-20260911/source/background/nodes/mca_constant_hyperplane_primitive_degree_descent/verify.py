"""Exact controls for constant-hyperplane descent, not official-source sampling."""
from fractions import Fraction as Q
import importlib.util
from math import prod
from pathlib import Path

PATH=Path(__file__).resolve().parent.parent/"pair_space_regular_projection_anchor/verify.py"
spec=importlib.util.spec_from_file_location("hyperplane_linear_control",PATH)
linear=importlib.util.module_from_spec(spec);spec.loader.exec_module(linear)
P=97


def need(ok,why):
    if not ok:raise ValueError(why)


def at(poly,x):
    out=0
    for c in reversed(poly):out=(out*x+c)%P
    return out


def rank(rows):
    return len(linear.rref(rows,P)[1])


def combine(vector,basis):
    return [sum(vector[k]*basis[k][i] for k in range(len(basis)))%P
            for i in range(len(basis[0]))]


def main():
    anchors=0
    for s in range(4,12):
        g=[0,2,-3,1]
        degree=s+1;length=degree+1
        pad=lambda x: [(x[i] if i<len(x) else 0)%P for i in range(length)]
        scalar=[pad([0]*j+g) for j in range(s-1)]
        one,zero=pad([1]),pad([])
        pairs=[(x,zero) for x in scalar]+[(one,scalar[0]),(zero,one)]
        pairs += [(zero,scalar[j]) for j in range(1,s-3)]
        need(len(pairs)==2*s-3 and rank(scalar+[one])==s,"full original projection at z0")
        for x in range(P):
            need(at(one,x)!=0,"kernel witness 1-zG cannot vanish identically in z")
            evals=[[at(pair[j],x) for pair in pairs] for j in (0,1)]
            need(rank(evals)==2,"regular joint anchor")
            kernel=linear.kernel(evals,P)
            need(len(kernel)==2*s-5,"child pair dimension")
            child=[(combine(v,[a for a,b in pairs]),combine(v,[b for a,b in pairs])) for v in kernel]
            constant_dimension=len(child)-rank([b for a,b in child])
            exceptional=at(g,x)==0
            need(constant_dimension==(s-1 if exceptional else s-2),"full versus partial constant child")
            if exceptional:
                need(rank([a for a,b in child]+[b for a,b in child]+scalar)==s-1,"shared carrier equals scalar S")
            else:
                k=linear.kernel([[at(v,x) for v in scalar]],P)
                actual=[combine(v,scalar) for v in k]
                expected=[]
                for j in range(s-2):
                    a=[0]*length
                    for i,c in enumerate(g):
                        a[i+j]=(a[i+j]-x*c)%P
                        a[i+j+1]=(a[i+j+1]+c)%P
                    expected.append(a)
                need(rank(actual+expected)==s-2,"primitive scalar degree drops by one")
            anchors+=1
        need(sum(at(g,x)==0 for x in range(P))==degree-(s-2)==3,"exact D-E root count")

    # Full constant11 remains full after a regular contraction, outside the partial hypothesis.
    s=11;basis=[[int(i==j) for i in range(s)] for j in range(s)]
    zero=[0]*s
    pairs=[(a,zero) for a in basis]+[(zero,b) for b in basis[:8]]
    for x in range(P):
        k=linear.kernel([[at(pair[j],x) for pair in pairs] for j in (0,1)],P)
        second=[combine(v,[b for a,b in pairs]) for v in k]
        need(len(k)-rank(second)==10,"full constant11 is not a maximal constant10 source")
    identities=0
    for s in range(5,12):
        r,d,t=1048576,67472,2
        a_prev=prod(Q(r+i,d-t+i) for i in range(1,s-3))
        a4=Q(r+1,d+1-t)
        full_to_four=prod(Q(r+i,d-t+i) for i in range(2,s-3))
        need(full_to_four==a_prev/a4,"full constant normalization telescopes")
        for root in (0,17,21489):
            for ordinary,full in ((Q(3),Q(7)),(Q(7),Q(3)),(Q(0),Q(0))):
                unscaled=((r+s-3)*a_prev*ordinary+root*a_prev*max(full-ordinary,0))/(d+s-3-t)
                a_s=a_prev*Q(r+s-3,d+s-3-t)
                need(unscaled/a_s==ordinary+Q(root,r+s-3)*max(full-ordinary,0),"normalized price identity")
                identities+=1
    print("PASS",anchors,"regular anchor controls, shared dimensions4..11; D-E and primitive degree drop")
    print("PASS97 full constant11 exclusion controls;",identities,"exact normalization identities")
    print("Algebraic fixtures only; universal source/owner statements are written proofs")


if __name__=="__main__":
    main()
