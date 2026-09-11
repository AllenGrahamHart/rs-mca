"""Exact shared-fibre budget for the rank20 full-constant source prefix."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import prod
from pathlib import Path

NODE=Path(__file__).resolve().parent
NODES=NODE.parent
PARENT=NODES/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
PARENT_PIN="432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
COMPILER_PIN="bac33f24d1f34760518406185fcc9850d4fc61f5441486f94237e13b99eb8ca8"
R,D,S,BUDGET=1048576,67472,1048577,274980728111395087
SCOPE=dict(
    schema="rank20-full-constant-prefix-v1",field="2130706433^6",
    n=2097152,k=1048576,agreement=1116048,target_epsilon="2^-128",
    original_error_rank=12,actual_P2_rank=20,J=[9965,13964],
    shared_dimension=11,full_constant_dimension=11,initial_quotient_dimension=9,
    anchors=8,terminal_pair_dimension=4,terminal_shared_dimension=3,
    terminal_pencil_dimension=3,terminal_quotient_dimension=1,
    factor_indices=list(range(2,10)),scalar_dimension=3,
    original_weights=True,original_field=True,original_union_complements=True,
    same_P2_enclosure_for_both_cutoffs=True,raw_cutoffs=[1,2],
    packing_budget=S,threshold=S//3,large_fibres_max=2,mass_box_width=1000,
    inside_weight="one global t",local_antecedent="after paid whole-source constant-pencil alternatives",
    normalization_cap_required=False,actual_pencil_occupation_assumed=False,
    whole_source_alternatives="MAXIMUM",near=134944,
    parent_index_sha256=PARENT_PIN,compiler_sha256=COMPILER_PIN,
    all_rank20_paid=False,full_constant_tail_paid=False,rank21_to22_paid=False,
    active_v4_atom=False,ordinary_LIST_row_paid=False,prize_closed=False,
)


def need(ok,why):
    if not ok:raise ValueError(why)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(x):
    x=Q(x);return [str(x.numerator),str(x.denominator)]


def build():
    raw=(PARENT/"index.json").read_bytes();need(sha(raw)==PARENT_PIN,"parent index")
    parents=json.loads(raw)["profiles"][:5]
    path=NODES/"list_padded_johnson_dimension_descent/compiler.py"
    need(sha(path.read_bytes())==COMPILER_PIN,"selector pin")
    spec=importlib.util.spec_from_file_location("rank20_scalar_selector",path)
    compiler=importlib.util.module_from_spec(spec);spec.loader.exec_module(compiler)
    entries=[];shards={};boxes=steps=0;maximum=0;next_j=9965
    for ref in parents:
        raw=(PARENT/ref["path"]).read_bytes();need(sha(raw)==ref["sha256"],"original profile pin")
        parent=json.loads(raw);j0,j1=parent["J"];need(j0==next_j,"degree coverage");next_j=j1+1
        gate=parent["heights"][0]["gate"]
        rows=[dict(kind="profile",J=parent["J"],parent_sha256=ref["sha256"],constant_gate=gate)]
        weights=[]
        for t in (1,2):
            low,high=D+1-t,S-gate-1;threshold=S//3
            need(0<low<=threshold<high<S and 3*(threshold+1)>S,"mass corridor")
            families={"small":[],"large":[]}
            for first,last,kind in ((low,threshold,"small"),(threshold+1,high,"large")):
                for lo in range(first,last+1,1000):
                    hi=min(lo+999,last)
                    need(1<=D-t<=hi-1 and 3<=j1-8 and 2130706433**6>=hi-1+j1-8,"same-field scalar corridor")
                    count,trace=compiler.compile_cap(hi-1,D-t,j1-8,3)
                    entry=dict(kind="box",t=t,size_class=kind,x=[lo,hi],count=count,
                               trace=[list(x) for x in trace])
                    families[kind].append(entry);rows.append(entry);boxes+=1;steps+=3
            alpha=max([Q(0)]+[Q((S-e["x"][0])*e["count"],e["x"][0]) for e in families["small"]])
            beta=max([Q(0)]+[(S-e["x"][0])*e["count"]-alpha*e["x"][0] for e in families["large"]])
            terminal=t+S*alpha+2*beta
            factor=prod(Q(R+j,D-t+j) for j in range(2,10))
            weights.append(terminal*factor)
            rows.append(dict(kind="cutoff",t=t,alpha=encode(alpha),beta=encode(beta),
                             terminal=encode(terminal),factor=encode(factor),raw_weight=encode(weights[-1])))
        price=Q(parent["mass_floor"],3)+weights[0]/2+weights[1]/6
        residual=price.numerator//price.denominator+134944
        whole=max(residual,270000000000000000)
        need(whole<BUDGET,"original full-constant rank20 source")
        rows.append(dict(kind="source",residual_bound=residual,whole_source_bound=whole,reserve=BUDGET-whole))
        maximum=max(maximum,whole)
        data=("\n".join(json.dumps(row,sort_keys=True,separators=(",",":")) for row in rows)+"\n").encode()
        name=str(j0)+".jsonl";shards[name]=data
        entries.append(dict(path=name,sha256=sha(data),J=parent["J"],residual_bound=residual,whole_source_bound=whole))
    need(next_j==13965 and maximum==270378604704109625,"exact full prefix maximum")
    index=dict(SCOPE,profiles=entries,mass_boxes=boxes,LIST_transitions=steps,
               source_bytes=sum(map(len,shards.values())),whole_source_bound=maximum,reserve=BUDGET-maximum)
    return index,shards


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--write",action="store_true");args=parser.parse_args()
    index,shards=build();raw=(json.dumps(index,indent=2)+"\n").encode()
    expected={"index.json":raw,**shards};folder=NODE/"certificates"
    if args.write:
        folder.mkdir(exist_ok=True);need(not any(folder.iterdir()),"refuse frozen certificate overwrite")
        for name,data in expected.items():(folder/name).write_bytes(data)
    else:
        need({p.name for p in folder.iterdir()}==set(expected),"exact certificate inventory")
        for name,data in expected.items():need((folder/name).read_bytes()==data,"exact replay: "+name)
    print("PASS",index["mass_boxes"],"mass boxes;",index["LIST_transitions"],"dimension-three LIST transitions")
    for row in index["profiles"]:print(row["J"],row["residual_bound"],row["whole_source_bound"])
    print("PAID rank20 full constant11 J9965..13964:",index["whole_source_bound"],"RESERVE",index["reserve"])
    print("INDEX",sha(raw),"SHARD BYTES",index["source_bytes"])
    print("Other rank20 sources, full-constant tail, ranks21..22 and both Prizes remain OPEN")


if __name__=="__main__":
    main()
