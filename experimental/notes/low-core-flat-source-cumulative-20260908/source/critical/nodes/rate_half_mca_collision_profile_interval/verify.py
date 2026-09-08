"""Fixed exact collision-profile certificate; universal scope is proved in proof.md."""

import hashlib
import importlib.util
from fractions import Fraction as F
from math import prod
from pathlib import Path


ROOT=Path(__file__).resolve().parents[1]
D,R,GAP,NEAR=67466,1048576,67472,134944
LO,HI,T0=22500,22999,180000000
CALIBRATION=274950000000000000
TOTAL=274938028871508001
EXPECTED="5ace68871be07e08317ea359ac9a73f80c7a9b9a325e5390a0d6e66b9ecdc5a2"


def load(name,node):
    spec=importlib.util.spec_from_file_location(name,ROOT/node/"verify.py")
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


root=load("flat_split_root","mca_flat_split_root_moment_basis")
collision=load("collision_resource","mca_fiber_collision_bonferroni_resource")
old=load("existing_inside_counts","rate_half_mca_first_excess_core_interval")
p=root.p


def need(ok,why):
    if not ok:
        raise ValueError(why)


def cover(rows,low,high):
    need(rows and rows[0][0]==low and rows[-1][1]==high,"cover endpoints")
    need(all(a<=b for a,b in rows),"nonempty cover bins")
    need(all(x[1]+1==y[0] for x,y in zip(rows,rows[1:])),"gap-free disjoint cover")


def previous_cost(J0,J1,t,a0,a1):
    need(1<=t<=5,"signed completion used only at ranks one through five")
    M,h,ell=D+J0,F(a1,t),11-t
    k0,k1=max(ell,J0-a1),J1-a0
    ds=[max(D+1+i,M-(10-i)*a1//t) for i in range(t)]
    caps={i:i*a1//t for i in range(1,t+1)}
    inner=old.inside(ds,a0,a1,caps)
    greedy=(D+k0)*prod(max(D+ell-i,D+k0-i*a1//t) for i in range(1,ell))
    quotient=max(old.quotient(ell,k0,k1,greedy),
                 p.bound(D,k0,k1,ell,min(F(k1-ell+1),h)))
    hybrid=M*prod(max(D+11-r,M-r*a1//t) for r in range(1,11))
    return 12*max(quotient*inner,hybrid,p.bound(D,J0,J1,11,h))


def resources(J0,J1):
    n0,n1,A=R+J0,R+J1,J1-6001
    full=collision.falling(n1,12)
    filtered=collision.box_resource(n0,n1,12,A,T0)
    exceptions=J1-11+n1*(A-1)//2
    need(0<filtered<full and exceptions>=0,"positive resource improvement")
    return full,filtered,exceptions


def controls():
    rows=[(j,min(j+15,HI)) for j in range(LO,HI+1,16)]
    cover(rows,LO,HI)
    for broken in (rows[1:],rows[:-1],rows+[rows[-1]],rows[:4]+rows[5:],
                   [(LO-1,rows[0][1])]+rows[1:]):
        try:
            cover(broken,LO,HI)
        except ValueError:
            pass
        else:
            raise ValueError("accepted broken degree cover")
    sizes=list(old.bins(5,22993,128))
    for broken in (sizes[1:],sizes[:-1],sizes[:7]+sizes[8:]):
        try:
            cover(broken,5,22993)
        except ValueError:
            pass
        else:
            raise ValueError("accepted broken size cover")
    need(84*125*(GAP+1-77)>10488*(GAP+1) and 22*84<GAP+1,"all-HIGH weight")
    need(21000<=LO<=HI<=52999,"proved degree-6000 source gate scope")
    need(266180883463176443<TOTAL<CALIBRATION<2130706433**6//2**128,
         "whole-source alternatives and target ordering")
    return rows


def main():
    digest=hashlib.sha256()
    rows=controls()
    peak,count,mutations,augmented=(0,None),0,0,0
    ranks={t:0 for t in range(1,11)}
    for J0,J1 in rows:
        full,filtered,exceptions=resources(J0,J1)
        high=F(10488,125)*(GAP+J0)*prod(GAP+i for i in range(1,11))
        digest.update(f"R:{J0},{J1}:{full}:{filtered}:{exceptions}\n".encode())
        blockmax=0
        for t in range(1,11):
            top=min(J1-11+t,J1-6001 if t==1 else J1)
            bins=list(old.bins(t,top,128))
            cover(bins,t,top)
            for a0,a1 in bins:
                h=F(a1,t)
                small=12*root.root_lower(D,J0,J1,11,t,a0,a1,h,T0)
                large=12*root.root_lower(D,J0,J1,11,t,a0,a1,h)
                def values():
                    return (full//min(small,high)+NEAR,
                            filtered//min(large,high)+exceptions+NEAR)
                if max(values())>CALIBRATION and t<=5:
                    previous=previous_cost(J0,J1,t,a0,a1)
                    small,large=max(small,previous),max(large,previous)
                    augmented+=1
                for tag,resource,cost,add in (("S",full,min(small,high),NEAR),
                                              ("L",filtered,min(large,high),exceptions+NEAR)):
                    ratio=F(resource)/cost
                    floor=ratio.numerator//ratio.denominator
                    need(floor<=ratio<floor+1,"exact resource floor")
                    for wrong in (floor-1,floor+1):
                        need(not wrong<=ratio<wrong+1,"reject wrong adjacent floor")
                        mutations+=1
                    cap=floor+add
                    need(cap<=TOTAL,"every branch and parameter box paid")
                    digest.update(f"{tag}:{J0},{J1},{t},{a0},{a1}:{cost.numerator}/{cost.denominator}:{cap}\n".encode())
                    if cap>peak[0]:
                        peak=cap,(tag,J0,J1,t,a0,a1)
                    blockmax=max(blockmax,cap)
                count+=1
                ranks[t]+=1
        print("BLOCK",J0,J1,"maximum",blockmax,"boxes",count,flush=True)
    need(len(rows)==32 and count==40960 and mutations==163840,"whole finite inventory")
    need(all(n==4096 for n in ranks.values()),"every maximizing-flat rank covered")
    need(augmented==10955,"fixed signed-completion calibration inventory")
    need(peak==(TOTAL,("S",22628,22643,5,18059,18235)),"exact attained certificate maximum")
    print("CERTIFICATE",peak,"augmented",augmented,"DIGEST",digest.hexdigest(),flush=True)
    need(digest.hexdigest()==EXPECTED,"frozen every-box digest")
    print("PASS all40960 boxes, both source-collision branches, eight broken covers rejected")
    print("Every normalized carrier on22500..22999 paid; original transport is downstream")


if __name__=="__main__":
    main()
