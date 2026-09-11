"""Exact all-coordinate nested-product source certificate; bounded JSONL shards."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path

NODE=Path(__file__).resolve().parent
NODES=NODE.parent
PARENT=NODES/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
PARENT_PIN="432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
COMPILER_PIN="bac33f24d1f34760518406185fcc9850d4fc61f5441486f94237e13b99eb8ca8"
R,D,BUDGET=1048576,67472,274980728111395087
STATES=[(s,c) for s in range(12) for c in range(min(3,s)+1)]
SCOPE=dict(
    schema="nested-product-full-constant-source-v1",field="2130706433^6",
    agreement=1116048,target_epsilon="2^-128",J=[9965,21499],
    original_error_rank=12,actual_P2_rank=19,shared_dimension=11,
    full_constant_dimension=11,second_component_dimension=8,
    local_antecedent="after proved whole-source pencil alternatives are removed",
    degree_excess="kappa=D-(s-1)",degree_band_width=1000,complement_box_width=10000,
    shared_stages=list(range(12)),codimensions=[0,1,2,3],
    all_coordinates=True,root_child_codimension_drop=1,root_child_pair_rank_drop=1,
    ordinary_child_pair_rank_drop=2,root_count_bound="kappa+c",
    original_weights=True,full_gcd_and_slack=True,normalization_cap_required=False,
    near=134944,parent_index_sha256=PARENT_PIN,compiler_sha256=COMPILER_PIN,
    whole_constant_terminal_tail_paid=False,unrestricted_rank19_paid=False,prize_closed=False,
)


def need(ok,why):
    if not ok:
        raise ValueError(why)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def pair(x):
    x=Q(x)
    return [str(x.numerator),str(x.denominator)]


def index_bytes(data):
    return (json.dumps(data,indent=2)+"\n").encode()


def shard_bytes(rows):
    return ("\n".join(json.dumps(r,sort_keys=True,separators=(",",":")) for r in rows)+"\n").encode()


def build():
    raw=(PARENT/"index.json").read_bytes()
    need(sha(raw)==PARENT_PIN,"original source index")
    refs=json.loads(raw)["profiles"]
    need(len(refs)==13,"all degree profiles")
    cp=NODES/"list_padded_johnson_dimension_descent/compiler.py"
    need(sha(cp.read_bytes())==COMPILER_PIN,"scalar selector pin")
    spec=importlib.util.spec_from_file_location("product_scalar_selector",cp)
    compiler=importlib.util.module_from_spec(spec);spec.loader.exec_module(compiler)
    shards,entries={},[]
    steps=bands_count=identities=size=0
    maximum=0;next_j=9965
    for ref in refs:
        need(ref["path"]==str(next_j)+".json","source profile path")
        raw=(PARENT/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"],"source profile pin")
        old=json.loads(raw);j0,j1=old["J"]
        need(j0==next_j,"complete degree coverage");next_j=j1+1
        gate=old["heights"][0]["gate"]
        need(gate+1<=R-D+1 and j1>=11,"nonempty scalar corridor")
        intervals=[(a,min(a+999,j1-11)) for a in range(0,j1-10,1000)]
        rows=[dict(kind="profile",J=old["J"],parent_sha256=ref["sha256"],constant_gate=gate)]
        top=[]
        for t in (1,2):
            bands=[]
            for lo,hi in intervals:
                base=[]
                for c in (1,2,3):
                    boxes=[]
                    degree=c+hi
                    for a in range(gate+1,R-D+t+1,10000):
                        b=min(a+9999,R-D+t)
                        need(1<=D-t<=R-a and c<=degree and
                             2130706433**6>=R-a+degree,"same-field uniform scalar degree")
                        count,trace=compiler.compile_cap(R-a,D-t,degree,c)
                        boxes.append(dict(e=[a,b],trace=[list(x) for x in trace],
                                          weight=t+b*count))
                        steps+=c
                    base.append(dict(c=c,degree=degree,boxes=boxes,
                                     bound=max(x["weight"] for x in boxes)))
                bands.append(dict(kind="band",t=t,kappa=[lo,hi],base=base,states=[]))
                bands_count+=1
            table={}
            for s,c in STATES:
                values=[]
                for i,(lo,hi) in enumerate(intervals):
                    if s==c:
                        value=Q(R-D+t) if c==0 else Q(bands[i]["base"][c-1]["bound"])
                    else:
                        ordinary=max(table[s-1,c][:i+1])
                        root=max(table[s-1,c-1][:i+1]) if c else ordinary
                        excess=max(Q(0),root-ordinary)
                        candidates=[ordinary]+[
                            ((R+s+x)*ordinary+(x+c)*excess)/(D+s+x-t)
                            for x in (lo,hi)]
                        value=max(candidates)
                        identities+=1
                    need(value>=0,"nonnegative child price")
                    values.append(value)
                    bands[i]["states"].append(pair(value))
                table[s,c]=values
            top.append(max(table[11,3]))
            rows.extend(bands)
        total=Q(old["mass_floor"],3)+top[0]/2+top[1]/6
        source=total.numerator//total.denominator+134944
        need(source<=239161133377346211<BUDGET,"original source class")
        maximum=max(maximum,source)
        rows.append(dict(kind="source",raw_prices=[pair(x) for x in top],
                         whole_source=source,reserve=BUDGET-source))
        data=shard_bytes(rows);path=str(j0)+".jsonl";shards[path]=data;size+=len(data)
        entries.append(dict(path=path,sha256=sha(data),J=old["J"]))
    need(next_j==21500 and maximum==239161133377346211,"exact covered maximum")
    result=dict(SCOPE,profiles=entries,degree_bands=bands_count,scalar_LIST_steps=steps,
                recurrence_identities=identities,state_count=len(STATES),source_bytes=size,
                residual_source_maximum=maximum,whole_source_bound=270000000000000000,
                combined_large_pencil_bound=272127061148955779)
    return result,shards


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write",action="store_true")
    args=parser.parse_args()
    index,shards=build()
    target=NODE/"certificates"
    expected={"index.json":index_bytes(index),**shards}
    if args.write:
        target.mkdir(exist_ok=True)
        need(not any(target.iterdir()),"refuse overwrite of frozen certificate")
        for name,data in expected.items():
            (target/name).write_bytes(data)
    else:
        need({p.name for p in target.iterdir()}==set(expected),"exact certificate inventory")
        for name,data in expected.items():
            need((target/name).read_bytes()==data,"exact reconstruction: "+name)
    print("PASS",index["degree_bands"],"degree bands;",index["scalar_LIST_steps"],"LIST steps;",
          index["recurrence_identities"],"all-coordinate recurrence identities")
    print("RESIDUAL MAX",index["residual_source_maximum"],"WITH ALTERNATIVES",index["whole_source_bound"])
    print("INDEX",sha(expected["index.json"]),"SHARD BYTES",index["source_bytes"])
    print("Full constant11 source class paid; maximum pencil dimensions8/9 and both Prizes open")


if __name__=="__main__":
    main()
