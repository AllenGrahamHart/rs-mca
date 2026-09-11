"""Exact whole-box certificates for original eigen-root incidence capacities."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

NODE=Path(__file__).resolve().parent
PARENT=NODE.parent/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
INDEX_PIN="432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
R,D=1048576,67472
RANGES=[(9965,10964),(10965,11964),(11965,12964),(12965,13364),(13365,13964),
        (13965,14964),(14965,15964),(15965,16964),(16965,17964),(17965,18964),
        (18965,19964),(19965,20964),(20965,21499)]
GATES=[(2108,1985,1948,1866),(2556,2417,2377,2354),(3041,2897,2856,2832),
       (3176,3034,2992,2968),(3428,3291,3251,3227),(3488,3352,3305,3289),
       (3543,3409,3362,3347),(3543,3409,3362,3347),(3543,3409,3362,3347),
       (3570,3437,3390,3375),(3619,3488,3442,3427),(3619,3488,3434,3427),
       (3619,3488,3434,3427)]
SCOPE=dict(J=[9965,21499],original_error_rank=12,actual_P2_rank=19,anchors=8,
           terminal_dimension=3,pencil_free=True,eigenvalues_field="original F",
           eigenspaces_max_dimension=1,raw_cutoffs=[1,2],
           primitive_degree="kappa=1+actual max degree(U0/G), all 3..J1-8",
           gcd_excess="v=J-8-kappa-distinct nonanchor G roots, includes degree slack, every v>=0",
           root_mask="anchors, domain gcd roots, then primitive F-eigenpolynomial roots",
           capacities="hereditary actual eigenlines and arbitrary affine planes",
           selected_pairs="exactly floor(L_t/(1048576-67472+t))+1",
           natural_intersection_cap="min(H,kappa-2)",energy_gate="S0>=N0 and strict energy",
           original_weights_unchanged=True,actual_core_witness=True,
           original_evaluation_flat_rank=9,automatic_primitive_degree="kappa<=H+2",
           excess_primitive_degree="kappa>=H+3",generic_degree_used=False,
           available_weight_maximum=272127061148955779,B_star=274980728111395087,near=134944,
           whole_constant_upper_tail_open=True,rank19_closed=False,whole_degree_closed=False,
           prize_closed=False)

def need(ok,why):
    if not ok:
        raise ValueError(why)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def encoded(data):
    return (json.dumps(data,indent=2)+"\n").encode()

def ceil(q):
    return -(-q.numerator//q.denominator)

def boxes(kmax,t):
    out=[]
    for q in range((R-1)//(D-1-t),(R-kmax+2)//(D-kmax+2-t)+1):
        lo=max(3,ceil(Q(q*(D+2-t)-(R+2),q-1)))
        hi=min(kmax,ceil(Q((q+1)*(D+2-t)-(R+2),q))-1)
        if lo<=hi:
            out.append((lo,hi,q))
    need(out[0][0]==3 and out[-1][1]==kmax
         and all(a[1]+1==b[0] for a,b in zip(out,out[1:])),"exact floor-box coverage")
    return out

def piece(lo,hi,q2,h,m,q1,e,t,u,w):
    need(q2>=2*q1,"twice-line plane capacity")
    cost=(0,2*q2,2*(q2+q1),3*q2)[e]
    s=2*m-cost
    b=2*m*(D-t)+cost
    coefficients=[b*b-2*R*b-4*R*m*(m-1)*w,
                  2*b*s-2*(b+R*s)-4*m*(m-1)*(R*u+w),
                  s*s-2*s-4*m*(m-1)*u]
    c,b1,a=coefficients
    endpoints=[a*x*x+b1*x+c for x in (lo,hi)]
    margins=[b+s*x-2*(R+x) for x in (lo,hi)]
    vertex=4*a*c-b1*b1 if a>0 and 2*a*lo<=-b1<=2*a*hi else None
    need(min(margins)>=0 and min(endpoints)>0 and (vertex is None or vertex>0),
         "all-gcd whole-box energy")
    return dict(kappa=[lo,hi],q2=q2,H_affine=[u,w],root_cost_twice=cost,
                S_twice=[b,s],energy4=coefficients,S_margin_endpoints=margins,
                energy4_endpoints=endpoints,vertex_discriminant=vertex)

def build():
    raw=(PARENT/"index.json").read_bytes()
    need(sha(raw)==INDEX_PIN,"parent index pin")
    parent_index=json.loads(raw)
    need(len(parent_index["profiles"])==len(RANGES),"parent coverage")
    shards={}
    entries=[]
    total=0
    for ref,ends,gates in zip(parent_index["profiles"],RANGES,GATES):
        raw=(PARENT/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"],"parent profile pin")
        parent=json.loads(raw)
        need(parent["J"]==list(ends),"original profile")
        g=parent["heights"][0]["gate"]
        shard=dict(schema="regular-eigen-capacity-profile-v1",J=list(ends),
                   primitive_degree=[3,ends[1]-8],parent_sha256=ref["sha256"],
                   original_constant_gate=g,spectra=[])
        for e,h in enumerate(gates):
            spectrum=dict(e=e,H=h,cutoffs=[])
            for t in (1,2):
                allowance=parent["terminals"][t-1]
                l=Q(*map(int,allowance))
                weight=R-D+t
                m=int(l/weight)+1
                q1=(R-g)//(D+1-t)
                pieces=[]
                for lo,hi,q2 in boxes(ends[1]-8,t):
                    if lo<=min(hi,h+2):
                        pieces.append(piece(lo,min(hi,h+2),q2,h,m,q1,e,t,1,-2))
                    if max(lo,h+3)<=hi:
                        pieces.append(piece(max(lo,h+3),hi,q2,h,m,q1,e,t,0,h))
                spectrum["cutoffs"].append(dict(t=t,allowance=allowance,original_pair_weight=weight,
                                                M=m,q1=q1,boxes=pieces))
                total+=len(pieces)
            shard["spectra"].append(spectrum)
        path=str(ends[0])+".json"
        shards[path]=encoded(shard)
        entries.append(dict(path=path,sha256=sha(shards[path]),J=list(ends),H=list(gates)))
    index=dict(schema="regular-eigen-capacity-index-v1",parent_index_sha256=INDEX_PIN,
               scope=SCOPE,profiles=entries,uniform_caps=[min(row[e] for row in GATES) for e in range(4)],
               profile_count=13,spectral_gate_count=52,cutoff_count=104,box_count=total)
    return index,shards

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write",action="store_true")
    args=parser.parse_args()
    index,shards=build()
    folder=NODE/"certificates"
    for name,data in dict(shards,**{"index.json":encoded(index)}).items():
        path=folder/name
        if args.write:
            need(not path.exists(),"refuse frozen certificate overwrite")
            folder.mkdir(exist_ok=True)
            path.write_bytes(data)
        need(path.read_bytes()==data,"frozen certificate equality: "+name)
    for row in index["profiles"]:
        print("GATES",row["J"],row["H"])
    print("PASS",index["box_count"],"whole-box energy tests; 104 original cutoff bounds")
    print("UNIFORM",index["uniform_caps"],"INDEX",sha(encoded(index)))
    print("Primitive degree<=H+2 paid; actual rich-core mass and whole original degrees remain open")

if __name__=="__main__":
    main()
