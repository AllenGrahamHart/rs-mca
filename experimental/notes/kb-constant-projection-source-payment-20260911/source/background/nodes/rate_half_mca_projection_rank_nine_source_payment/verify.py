"""Original-source payment from a constant projection of affine rank at most nine."""
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
MASS_PIN="b6745db5995bdf421755408a54a92f052beadff4747391f62b93733b51be8867"
R,D,J,G,BUDGET=1048576,67472,21499,569050,274980728111395087
MASS=578501226347492453
SCOPE=dict(
    schema="constant-projection-rank-nine-source-v1",field="2130706433^6",
    n=2097152,k=1048576,agreement=1116048,target_epsilon="2^-128",
    original_error_rank=12,J=[9965,21499],projection_affine_dimension_max=9,
    projection_row="one fixed nonzero ORIGINAL-field constant row",
    pair_scalar_carrier_dimension=11,raw_cutoffs=[1,2],anchors=0,
    original_labels_and_weights=True,original_complete_unions=True,
    inside_weight="one global t",singleton_pair_weight="R-d+t",
    heavy_complement_max="R-2*d-1+2*t",constant_gate=G,
    on_scalar_dimension=11,projected_scalar_dimension=9,
    complement_box_width=10000,projection_tails_counted=True,
    base_may_overcount_heavy_fibres=True,local_antecedent="after paid original constant-pencil alternatives",
    original_min_raw9_mass=MASS,near=134944,whole_source_alternatives="MAXIMUM",
    normalization_cap_required=False,actual_pencil_occupation_assumed=False,
    rank19_terminal_allowance_used=False,parent_index_sha256=PARENT_PIN,
    compiler_sha256=COMPILER_PIN,mass_verifier_sha256=MASS_PIN,
    full_constant_rank20_paid=True,other_rank20_paid=False,rank21_to22_paid=False,
    active_v4_atom=False,ordinary_LIST_row_paid=False,prize_closed=False,
)


def need(ok,why):
    if not ok:raise ValueError(why)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(q):
    q=Q(q);return [str(q.numerator),str(q.denominator)]


def build():
    raw=(PARENT/"index.json").read_bytes();need(sha(raw)==PARENT_PIN,"source gate index")
    refs=json.loads(raw)["profiles"];gate_refs=[];next_j=9965
    for ref in refs:
        raw=(PARENT/ref["path"]).read_bytes();need(sha(raw)==ref["sha256"],"parent profile")
        row=json.loads(raw);need(row["J"][0]==next_j and row["heights"][0]["gate"]>=G,"whole uniform gate")
        next_j=row["J"][1]+1
        gate_refs.append(dict(path=ref["path"],sha256=ref["sha256"],J=row["J"]))
    need(next_j==21500,"all source degrees")
    path=NODES/"list_padded_johnson_dimension_descent/compiler.py"
    need(sha(path.read_bytes())==COMPILER_PIN,"selector pin")
    need(sha((NODES/"rate_half_mca_min_envelope_raw_mass/verify.py").read_bytes())==MASS_PIN,"uniform raw-resource pin")
    spec=importlib.util.spec_from_file_location("projection_scalar_selector",path)
    compiler=importlib.util.module_from_spec(spec);spec.loader.exec_module(compiler)
    rows=[];weights=[];boxes=steps=0
    for t in (1,2):
        base,trace=compiler.compile_cap(R,D-t,J,9);steps+=9
        end=R-2*D-1+2*t
        rows.append(dict(kind="cutoff",t=t,heavy_max=end,base_count=base,base_trace=[list(x) for x in trace]))
        heavy=0
        for low in range(G+1,end+1,10000):
            high=min(low+9999,end)
            on,on_trace=compiler.compile_cap(R-low,D-t,J,11)
            projected,q_trace=compiler.compile_cap(R,R-high,J,9)
            weight=high*on*projected;heavy+=weight;boxes+=1;steps+=20
            rows.append(dict(kind="heavy_box",t=t,e=[low,high],on_count=on,projection_count=projected,
                             on_trace=[list(x) for x in on_trace],projection_trace=[list(x) for x in q_trace],
                             weight=weight))
        weight=t+(R-D+t)*base+heavy;weights.append(weight)
        rows.append(dict(kind="weight",t=t,heavy_weight=heavy,raw_weight=weight))
    price=Q(MASS,3)+Q(weights[0],2)+Q(weights[1],6)
    residual=price.numerator//price.denominator+134944
    whole=max(residual,270000000000000000)
    need(residual==214086393235061966 and whole<BUDGET,"entire original source class")
    rows.append(dict(kind="source",residual_bound=residual,whole_source_bound=whole,reserve=BUDGET-whole))
    data=("\n".join(json.dumps(r,sort_keys=True,separators=(",",":")) for r in rows)+"\n").encode()
    index=dict(SCOPE,gate_profiles=gate_refs,heavy_boxes=boxes,LIST_transitions=steps,
               path="weights.jsonl",sha256=sha(data),source_bytes=len(data),
               residual_source_bound=residual,whole_source_bound=whole,reserve=BUDGET-whole)
    return index,data


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--write",action="store_true");args=parser.parse_args()
    index,data=build();raw=(json.dumps(index,indent=2)+"\n").encode()
    expected={"index.json":raw,"weights.jsonl":data};folder=NODE/"certificates"
    if args.write:
        folder.mkdir(exist_ok=True);need(not any(folder.iterdir()),"refuse frozen replacement")
        for name,content in expected.items():(folder/name).write_bytes(content)
    else:
        need({p.name for p in folder.iterdir()}==set(expected),"exact inventory")
        for name,content in expected.items():need((folder/name).read_bytes()==content,"exact reconstruction")
    print("PASS",index["heavy_boxes"],"heavy-fibre boxes;",index["LIST_transitions"],"legal scalar LIST steps")
    print("RESIDUAL",index["residual_source_bound"],"SOURCE",index["whole_source_bound"],"RESERVE",index["reserve"])
    print("INDEX",sha(raw),"SHARD BYTES",len(data))
    print("Full constant rank20 paid throughout J9965..21499; other rank20 classes and both Prizes open")


if __name__=="__main__":
    main()
