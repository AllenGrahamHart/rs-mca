"""Small exact controls for all three joint ranks and nonregular rank-two children."""
import importlib.util
from pathlib import Path

P=31
path=Path(__file__).resolve().parent.parent/"pair_space_regular_projection_anchor/verify.py"
spec=importlib.util.spec_from_file_location("all_coordinate_linear_algebra",path)
linear=importlib.util.module_from_spec(spec);spec.loader.exec_module(linear)


def need(ok,why):
    if not ok:raise ValueError(why)


def rank(rows):
    return len(linear.rref(rows,P)[1]) if rows else 0


def multiply(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%P
    return out


def value(row,x):
    return sum(v*pow(x,j,P) for j,v in enumerate(row))%P


def generic(rows,s):
    # Every projected minor has degree at most s in z; s+1 points suffice.
    need(s<P,"exact generic-rank interpolation range")
    return max(rank([[(v[j]+z*v[s+j])%P for j in range(s)] for v in rows])
               for z in range(s+1))


def divide_anchor(poly,x):
    quotient=[0]*(len(poly)-1)
    for j in range(len(quotient)-1,-1,-1):
        quotient[j]=(poly[j+1]+(x*quotient[j+1] if j+1<len(quotient) else 0))%P
    need((poly[0]+x*quotient[0])%P==0,"anchor divides every component difference")
    return quotient


def families(s):
    V=[[int(i==j) for i in range(s)] for j in range(s)];zero=[0]*s
    for c in range(4):
        root=[1]
        for x in range(c):root=multiply(root,[-x,1])
        B=[([0]*j+root+[0]*s)[:s] for j in range(s-c)]
        yield "product"+str(c),c,[v+zero for v in V]+[zero+b for b in B],True
    root=multiply(multiply([0,1],[-1,1]),[-2,1])
    H=[([0]*j+root+[0]*s)[:s] for j in range(s-3)]
    bridges=[V[0]+zero,V[1]+V[0],V[2]+[(-x)%P for x in V[1]]]
    yield "nonregular",3,[v+zero for v in H]+[zero+v for v in H]+bridges,True
    yield "rank0-square",2,[v+zero for v in V[1:]]+[zero+v for v in V[1:]],False
    yield "rank0-nested",3,[v+zero for v in V[1:]]+[zero+v for v in V[2:]],False


def main():
    cases=sections=rank0=rank1=losses=0
    for s in range(4,8):
        for name,c,W,full in families(s):
            need(rank(W)==2*s-c and (generic(W,s)==s)==full,"initial formal scope")
            zero_points=[];low_points=[];bad_generic=[]
            for x in range(P):
                matrix=[[value(v[:s],x) for v in W],[value(v[s:],x) for v in W]]
                q=rank(matrix);section=linear.kernel(matrix,P)
                child=[[sum(a*W[j][k] for j,a in enumerate(coeff))%P for k in range(2*s)]
                       for coeff in section]
                need(rank(child)==2*s-c-q,"actual pair-rank drop")
                normalized=[divide_anchor(v[:s],x)+divide_anchor(v[s:],x) for v in child]
                child_c=c+q-2
                need(0<=child_c<=s-1 and rank(normalized)==2*(s-1)-child_c,"child carrier/codimension")
                need(all(len(v)==2*(s-1) for v in normalized),"shared degree drops by one")
                child_full=generic(normalized,s-1)==s-1
                if q==0:zero_points.append(x);rank0+=1
                if q<=1:low_points.append(x)
                if q==1:rank1+=1
                if full:
                    need(q!=0 and (q!=1 or child_full),"generic rank-one preservation; no rank zero")
                    if not child_full:
                        need(q==2 and c>=2,"only possible nonregular type")
                        bad_generic.append(x);losses+=1
                sections+=1
            need(len(low_points)<=c and len(zero_points)<=c//2,"nested exceptional root bounds")
            need(rank([[pow(x,j,P) for j in range(s)] for x in low_points])<=c,"bad dual-flat dimension")
            if full:need(len(set(low_points)|set(bad_generic))<=c,"one joint generic-exception budget")
            if name=="nonregular":need(bad_generic==[0,1,2],"three real rank-two nonregular children")
            if name.startswith("rank0"):need(zero_points==[0],"proper-component rank-zero control")
            cases+=1
    need((cases,sections,rank0,rank1,losses)==(28,868,8,24,12),"finite control inventory")
    print("PASS",cases,"carriers;",sections,"exact sections;",rank0,"rank-zero;",rank1,"rank-one;",losses,"nonregular rank-two children")
    print("Generic ranks are exact by minor interpolation, not sampled genericity")
    print("Algebraic controls only, not official MCA source witnesses")


if __name__=="__main__":
    main()
