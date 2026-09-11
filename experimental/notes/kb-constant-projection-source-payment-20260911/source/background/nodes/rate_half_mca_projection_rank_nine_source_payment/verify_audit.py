"""Independent constant-projection source census audit; no new primary/selector import."""
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path

NODE=Path(__file__).resolve().parent
NODES=NODE.parent
PARENT=NODES/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
PIN="6620e091aa9d04802701fcbfaaa21de1535da8d2c14b1699c6e00542b88d59ec"
PARENT_PIN="432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
COMPILER_PIN="bac33f24d1f34760518406185fcc9850d4fc61f5441486f94237e13b99eb8ca8"
MASS_PIN="b6745db5995bdf421755408a54a92f052beadff4747391f62b93733b51be8867"
TRACE_PIN="59b9ad4918ced72f90938f3ac5817f5c504aa7a1daa11818d3fcf560dff01d2f"
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
COUNTS=dict(heavy_boxes=70,LIST_transitions=1418,path="weights.jsonl",
            source_bytes=28319,residual_source_bound=214086393235061966,
            whole_source_bound=270000000000000000,reserve=4980728111395087)


def need(ok,why):
    if not ok:raise ValueError(why)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def scope(index):
    need(set(index)==set(SCOPE)|set(COUNTS)|{"sha256","gate_profiles"},"index schema")
    for key,value in dict(SCOPE,**COUNTS).items():
        need(json.dumps(index[key],sort_keys=True)==json.dumps(value,sort_keys=True),"scope/count: "+key)
    need(len(index["gate_profiles"])==13,"thirteen source profiles")
    need(2130706433**6//2**128==BUDGET and 2*D==134944,"original budget/near")


def inherited():
    path=NODES/"rate_half_mca_coupled_pair_rank_frontier/verify_audit.py"
    need(sha(path.read_bytes())==TRACE_PIN,"old independent legality checker")
    need(sha((NODES/"rate_half_mca_min_envelope_raw_mass/verify.py").read_bytes())==MASS_PIN,
         "original mass supplier, not a sampled replacement")
    spec=importlib.util.spec_from_file_location("projection_LIST_legality",path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def source_gate(parent,prior):
    j0,j1=parent["J"];row=parent["heights"][0];gate=row["gate"]
    need(row["height"]==[0,0] and 567500<gate<R-D and gate>=G,"constant source gate")
    on=prior.list_cap(parent["on_trace"],R-567501,D-43,j1,11)
    off=prior.list_cap(row["off_trace"],gate-j1,D-42-j1,j1,11)
    price=Q(581590844909990298+43*gate*on+43*981147*off,44)+134945
    cap=-(-price.numerator//price.denominator)
    need(cap==row["price"]<=270000000000000000,"whole original source alternative")
    return gate


def summary(rows,write=False,omit_singleton=False,omit_tail=False,omit_inside=False):
    weights=[]
    for t in (1,2):
        header=next(r for r in rows if r["kind"]=="cutoff" and r["t"]==t)
        heavy=0
        for row in rows:
            if row["kind"]=="heavy_box" and row["t"]==t:
                value=row["e"][1]*row["on_count"]*(1 if omit_tail else row["projection_count"])
                if write:row["weight"]=value
                else:need(row["weight"]==value,"heavy fibres need projected multiplicity")
                heavy+=value
        single=0 if omit_singleton else (R-D+t)*header["base_count"]
        weight=(0 if omit_inside else t)+single+heavy;weights.append(weight)
        expected=dict(kind="weight",t=t,heavy_weight=heavy,raw_weight=weight)
        pos=next(i for i,r in enumerate(rows) if r["kind"]=="weight" and r["t"]==t)
        if write:rows[pos]=expected
        else:need(rows[pos]==expected,"original singleton weight and single global inside charge")
    numerator=2*MASS+3*weights[0]+weights[1]
    residual=numerator//6+2*D
    whole=max(residual,270000000000000000)
    expected=dict(kind="source",residual_bound=residual,whole_source_bound=whole,reserve=BUDGET-whole)
    if write:rows[-1]=expected
    else:need(rows[-1]==expected and residual==COUNTS["residual_source_bound"],"original raw identity/MAX/near")
    return residual


def census(rows,prior):
    position=boxes=steps=0
    for t in (1,2):
        header=rows[position];position+=1
        # n-2A+K-1, using ORIGINAL degree K=J, cancels J exactly.
        ends={(R+j)-2*(D+j-t)+j-1 for j in (9965,13964,21499)}
        need(len(ends)==1,"same threshold on every original profile")
        end=ends.pop()
        need(set(header)=={"kind","t","heavy_max","base_count","base_trace"}
             and header["kind"]=="cutoff" and type(header["t"]) is int
             and header["t"]==t and header["heavy_max"]==end,"original cutoff/two-core threshold")
        base=prior.list_cap(header["base_trace"],R,D-t,J,9);steps+=9
        need(type(header["base_count"]) is int and header["base_count"]==base,"all projected singletons")
        next_e=G+1
        while next_e<=end:
            last=min(next_e+9999,end);row=rows[position];position+=1
            need(set(row)=={"kind","t","e","on_count","projection_count","on_trace","projection_trace","weight"},
                 "heavy box schema")
            need(row["kind"]=="heavy_box" and type(row["t"]) is int and row["t"]==t
                 and row["e"]==[next_e,last] and all(type(x) is int for x in row["e"]),
                 "no omitted complement/gate")
            on=prior.list_cap(row["on_trace"],R-next_e,D-t,J,11)
            projected=prior.list_cap(row["projection_trace"],R,R-last,J,9)
            need(type(row["on_count"]) is int and row["on_count"]==on,"pair scalar dimension ELEVEN")
            need(type(row["projection_count"]) is int and row["projection_count"]==projected,
                 "projected tail dimension NINE")
            need(type(row["weight"]) is int and row["weight"]==last*on*projected,
                 "upper complement times both actual count bounds")
            boxes+=1;steps+=20;next_e=last+1
        need(rows[position]["kind"]=="weight" and rows[position]["t"]==t,"cutoff subtotal")
        position+=1
    need(position==len(rows)-1 and rows[-1]["kind"]=="source","exact row inventory")
    need((boxes,steps)==(70,1418),"complete finite census")
    return summary(rows)


def reject(action):
    try:action()
    except (ValueError,KeyError,TypeError,IndexError,StopIteration,ZeroDivisionError):return
    raise ValueError("accepted malformed proof recipe")


def main():
    raw=(NODE/"certificates/index.json").read_bytes();need(sha(raw)==PIN,"new certificate index")
    index=json.loads(raw);scope(index)
    raw=(PARENT/"index.json").read_bytes();need(sha(raw)==PARENT_PIN,"original source index")
    refs=json.loads(raw)["profiles"];need(len(refs)==13,"parent profile inventory")
    prior=inherited();next_j=9965;gates=[]
    for ref,pin in zip(refs,index["gate_profiles"]):
        raw=(PARENT/ref["path"]).read_bytes();need(sha(raw)==ref["sha256"],"original profile hash")
        parent=json.loads(raw);need(parent["J"][0]==next_j,"original degree coverage")
        next_j=parent["J"][1]+1
        need(pin==dict(path=ref["path"],sha256=ref["sha256"],J=parent["J"]),"source gate provenance")
        gates.append(source_gate(parent,prior))
    need(next_j==21500 and min(gates)==G,"uniform residual gate from all thirteen source alternatives")
    raw=(NODE/"certificates/weights.jsonl").read_bytes()
    need(len(raw)==COUNTS["source_bytes"] and sha(raw)==index["sha256"],"new payload hash/count")
    need({p.name for p in (NODE/"certificates").iterdir()}=={"index.json","weights.jsonl"},"exact inventory")
    rows=[json.loads(line) for line in raw.splitlines()];census(rows,prior)
    mutations=0
    for key in dict(SCOPE,**COUNTS):
        bad=copy.deepcopy(index);bad[key]=None;reject(lambda:scope(bad));mutations+=1
    for mode in ("missing","duplicate"):
        bad=copy.deepcopy(index)
        if mode=="missing":bad["gate_profiles"].pop()
        else:bad["gate_profiles"].append(bad["gate_profiles"][0])
        reject(lambda:scope(bad));mutations+=1
    for mode in ("drop","gap","endpoints","count","trace","threshold","cutoff","inside","near","sum"):
        bad=copy.deepcopy(rows)
        if mode=="drop":bad.pop(1)
        elif mode=="gap":bad[1]["e"][0]+=1
        elif mode=="endpoints":bad[1]["e"].reverse()
        elif mode=="count":bad[1]["projection_count"]-=1
        elif mode=="trace":bad[1]["on_trace"][-1][-1]-=1
        elif mode=="threshold":bad[0]["heavy_max"]+=1
        elif mode=="cutoff":bad[1]["t"]=2
        elif mode=="inside":summary(bad,write=True,omit_inside=True)
        elif mode=="near":bad[-1]["residual_bound"]-=2*D
        else:bad[-1]["whole_source_bound"]+=270000000000000000
        reject(lambda:census(bad,prior));mutations+=1
    # Reprice each complete cheaper ledger; rejection must not rely on the outer hash.
    for mode in ("no-tail-multiplicity","dimension-nine-pairs","no-singletons"):
        bad=copy.deepcopy(rows)
        if mode=="dimension-nine-pairs":
            for row in bad:
                if row["kind"]=="heavy_box":
                    row["on_trace"]=row["on_trace"][:9];row["on_count"]=row["on_trace"][-1][-1]
        result=summary(bad,write=True,omit_tail=mode=="no-tail-multiplicity",
                       omit_singleton=mode=="no-singletons")
        need(result<rows[-1]["residual_bound"],"repriced mutation must change the residual")
        reject(lambda:census(bad,prior));mutations+=1
    print("PASS independent 70 heavy boxes; 1418 legal LIST steps; 13 original whole-source gates")
    print("PASS",mutations,"semantic mutations, including three fully repriced cheaper ledgers")
    print("RESIDUAL",rows[-1]["residual_bound"],"SOURCE",rows[-1]["whole_source_bound"],
          "RESERVE",rows[-1]["reserve"])
    print("Original projection rank<=9 paid; other rank20 classes, ranks21/22 and both Prizes OPEN")


if __name__=="__main__":
    main()
