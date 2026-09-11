"""Pay the rank19 prefix by retaining a normalization ceiling and pricing its exits."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path

NODE=Path(__file__).resolve().parent
NODES=NODE.parent
PRIOR=NODES/"rate_half_mca_all_coordinate_rank_nineteen_tail_payment/certificates"
PARENT=NODES/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
PRIOR_PIN="37e1f226deb4ba670373090103ebe7d666200d3186542870c46595bf05797aae"
PARENT_PIN="432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
GEOMETRY_PIN="398b9ea9b246bb017e434efd4104ec897dac9e2e4ac38cbe4554d42f5d9747b7"
R,D,BUDGET=1048576,67472,274980728111395087
STATES=[(s,c) for s in range(12) for c in range(min(3,s)+1)]
SCOPE=dict(
    schema="normalization-ceiling-original-rank19-v1",
    field="2130706433^6",agreement=1116048,target_epsilon="2^-128",
    original_error_rank=12,actual_P2_rank_max=19,J=[9965,21499],
    new_regular_prefix=[9965,13964],previous_paid_tail=[13965,21499],
    initial_shared_dimension=11,codimension=3,ceiling="H=floor((J1-1)/10)",
    degree_excess="kappa=D-(s-1)",degree_band_width=500,shared_stages=list(range(3,12)),
    geometric_stages=list(range(4,12)),branch_weighted=True,centre_count_used=False,
    original_field_and_owners=True,full_gcd_and_slack=True,near=134944,
    geometric_exception_price="untagged full-generic child",
    generic_exception_price="MAX(generic rank1, unrestricted nonregular rank2)",
    exceptional_sets_may_overlap=True,exceptional_coordinates_discarded=False,
    geometric_bad_less_than_core_required=False,
    low_terminal_history="eight actual regular anchors AND nu<=H; source gates first",
    local_antecedent="after proved whole-source pencil alternatives are removed",
    prior_index_sha256=PRIOR_PIN,parent_index_sha256=PARENT_PIN,
    branch_bound_sha256=GEOMETRY_PIN,
    rank20_to22_paid=False,whole_J_closed=False,prize_closed=False,
)


def need(ok,why):
    if not ok:raise ValueError(why)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(x):
    x=Q(x);return [str(x.numerator),str(x.denominator)]


def decode(x):
    return Q(*map(int,x))


def quotient_geometry(degree,s,H,coordinate_bound):
    limit=min(H,degree//(s-1));lo=1;best=0;owner=None;boxes=0
    while lo<=limit:
        image=degree//lo;h=H//lo+1
        hi=min(limit,degree//image,H//(h-1))
        value=coordinate_bound(image,s-1,hi,h)
        if value>best:
            best=value;owner=[hi,image,h,min(image-h*(s-2),max(1,h-2))]
        boxes+=1;lo=hi+1
    return dict(s=s,degree=degree,nu_max=limit,quotient_boxes=boxes,bound=best,argmax=owner)


def inherited_tables(bands,t):
    intervals=[x["kappa"] for x in bands];U={};G={}
    for s,c in STATES:
        uv=[];gv=[]
        for i,(lo,hi) in enumerate(intervals):
            if s==c:
                if c==0:u=g=Q(R-D+t)
                else:
                    base=bands[i]["base"][c-1];u=g=Q(base["constant"])
                    if c>=2:u=max(u,decode(base["ff2"]));g=max(g,decode(base["generic_ff2"]))
            else:
                C=max(U[s-1,c][:i+1]);F=max(U[s-1,c-1][:i+1]) if c else C
                Z=max(U[s-1,c-2][:i+1]) if c>=2 else max(C,F)
                x1=max(Q(0),F-C);x0=max(Q(0),Z-max(C,F))
                u=max(C,*[((R+s+x)*C+(x+c)*x1+(x+c//2)*x0)/(D+s+x-t) for x in (lo,hi)])
                C=max(G[s-1,c][:i+1]);F=max(G[s-1,c-1][:i+1]) if c else C
                T=max(U[s-1,c][:i+1]) if c>=2 else C
                extra=max(Q(0),F-C,T-C)
                g=max(C,*[((R+s+x)*C+(x+c)*extra)/(D+s+x-t) for x in (lo,hi)])
            uv.append(u);gv.append(g)
        U[s,c]=uv;G[s,c]=gv
    for i,row in enumerate(bands):
        need(encode(U[11,3][i])==row["unrestricted"] and encode(G[11,3][i])==row["full_generic"],
             "inherited top tables unchanged")
    return U,G


def build():
    raw=(PRIOR/"index.json").read_bytes();need(sha(raw)==PRIOR_PIN,"prior index")
    refs=json.loads(raw)["profiles"]
    raw=(PARENT/"index.json").read_bytes();need(sha(raw)==PARENT_PIN,"original source index")
    parents=json.loads(raw)["profiles"]
    path=NODES/"rational_curve_inner_projection_branch_budget/bounds.py"
    need(sha(path.read_bytes())==GEOMETRY_PIN,"proved branch-bound implementation")
    spec=importlib.util.spec_from_file_location("ceiling_branch_geometry",path)
    geom=importlib.util.module_from_spec(spec);spec.loader.exec_module(geom)
    entries=[];shards={};counts=dict(degree_bands=0,geometry_rows=0,nu_candidates=0,quotient_boxes=0,
                                   low_recurrence_identities=0,inherited_recurrence_identities=0)
    maximum=0;size=0;next_j=9965
    for ref,parent_ref in zip(refs[:5],parents[:5]):
        raw=(PRIOR/ref["path"]).read_bytes();need(sha(raw)==ref["sha256"],"inherited all-coordinate shard")
        old=[json.loads(x) for x in raw.splitlines()]
        raw=(PARENT/parent_ref["path"]).read_bytes();need(sha(raw)==parent_ref["sha256"],"source profile")
        parent=json.loads(raw);j0,j1=parent["J"];need(j0==next_j,"whole original prefix")
        next_j=j1+1;H=(j1-1)//10
        intervals=[x["kappa"] for x in old if x.get("kind")=="band" and x["t"]==1]
        rows=[dict(kind="profile",J=parent["J"],H=H,prior_sha256=ref["sha256"],parent_sha256=parent_ref["sha256"])]
        geometry=[]
        for lo,hi in intervals:
            stages=[quotient_geometry(s-1+hi,s,H,geom.coordinate_bound) for s in range(4,12)]
            geometry.append(stages);rows.append(dict(kind="geometry",kappa=[lo,hi],stages=stages))
            counts["geometry_rows"]+=8
            counts["nu_candidates"]+=sum(x["nu_max"] for x in stages)
            counts["quotient_boxes"]+=sum(x["quotient_boxes"] for x in stages)
        top=[]
        for t in (1,2):
            bands=[x for x in old if x.get("kind")=="band" and x["t"]==t]
            U,G=inherited_tables(bands,t);L={}
            for s in range(3,12):
                values=[]
                for i,(lo,hi) in enumerate(intervals):
                    if s==3:
                        base=bands[i]["base"][2]
                        price=max(Q(base["constant"]),min(decode(base["ff2"]),decode(parent["terminals"][t-1])))
                    else:
                        C=max(L[s-1][:i+1]);F=max(max(G[s-1,2][:i+1]),max(U[s-1,3][:i+1]))
                        T=max(G[s-1,3][:i+1]);beta=geometry[i][s-4]["bound"]
                        price=max(C,*[((R+s+x)*C+(x+3)*max(F-C,0)+beta*max(T-C,0))/(D+s+x-t)
                                       for x in (lo,hi)])
                        price=min(price,max(G[s,3][:i+1]))
                        counts["low_recurrence_identities"]+=1
                    values.append(price)
                L[s]=values
            for i,interval in enumerate(intervals):
                rows.append(dict(kind="low_band",t=t,kappa=interval,states=[encode(L[s][i]) for s in range(3,12)]))
            counts["degree_bands"]+=len(intervals)
            counts["inherited_recurrence_identities"]+=76*len(intervals)
            top.append(max(L[11]))
        raw_price=Q(parent["mass_floor"],3)+top[0]/2+top[1]/6
        price=raw_price.numerator//raw_price.denominator+134944
        need(price<BUDGET,"whole regular rank19 prefix")
        maximum=max(maximum,price)
        rows.append(dict(kind="source",raw_prices=[encode(x) for x in top],regular_source=price,reserve=BUDGET-price))
        data=("\n".join(json.dumps(row,sort_keys=True,separators=(",",":")) for row in rows)+"\n").encode()
        name=str(j0)+".jsonl";shards[name]=data;size+=len(data)
        entries.append(dict(path=name,sha256=sha(data),J=parent["J"],regular_source=price))
    need(next_j==13965,"entire lower prefix")
    index=dict(SCOPE,**counts,profiles=entries,source_bytes=size,regular_prefix_maximum=maximum,
               whole_prefix_rank_le19_bound=max(maximum,274462040894062110,270000000000000000),
               whole_gap_rank_le19_bound=max(maximum,274462040894062110,274839785069298661))
    need(index["whole_gap_rank_le19_bound"]<BUDGET,"all rank<=19 across original gap")
    return index,shards


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--write",action="store_true");args=parser.parse_args()
    index,shards=build();raw=(json.dumps(index,indent=2)+"\n").encode()
    data={"index.json":raw,**shards};folder=NODE/"certificates"
    if args.write:
        folder.mkdir(exist_ok=True);need(not any(folder.iterdir()),"refuse overwrite")
        for name,content in data.items():(folder/name).write_bytes(content)
    else:
        need({x.name for x in folder.iterdir()}==set(data),"exact certificate inventory")
        for name,content in data.items():need((folder/name).read_bytes()==content,"exact reconstruction: "+name)
    print("PASS",index["degree_bands"],"low degree bands;",index["geometry_rows"],"geometric rows;",
          index["nu_candidates"],"covered nu values;",index["quotient_boxes"],"quotient intervals")
    print("PASS",index["low_recurrence_identities"],"paid-ceiling and",index["inherited_recurrence_identities"],"inherited identities")
    for row in index["profiles"]:print(row["J"],row["regular_source"])
    print("PAID ALL actual P2 rank<=19 J9965..21499:",index["whole_gap_rank_le19_bound"])
    print("INDEX",sha(raw),"SHARD BYTES",index["source_bytes"])
    print("Ranks20..22 and both Prize problems remain OPEN")


if __name__=="__main__":
    main()
