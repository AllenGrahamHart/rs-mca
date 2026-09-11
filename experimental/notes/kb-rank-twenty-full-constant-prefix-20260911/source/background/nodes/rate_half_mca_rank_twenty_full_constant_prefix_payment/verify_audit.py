"""Independent source packing and legal-trace audit; imports no new primary or selector."""
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import prod
from pathlib import Path

NODE=Path(__file__).resolve().parent
NODES=NODE.parent
PARENT=NODES/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
PIN="1a53e3bf7d6b3b88a73d2f16360e191a74489833139779e5fb34b5af7e681b87"
PARENT_PIN="432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
COMPILER_PIN="bac33f24d1f34760518406185fcc9850d4fc61f5441486f94237e13b99eb8ca8"
TRACE_PIN="59b9ad4918ced72f90938f3ac5817f5c504aa7a1daa11818d3fcf560dff01d2f"
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
COUNTS=dict(mass_boxes=3166,LIST_transitions=9498,source_bytes=361476,
            whole_source_bound=270378604704109625,reserve=4602123407285462)
PRICES=[246551605079024985,244822875909897379,249898649334152558,
        250563989103155372,270378604704109625]


def need(ok,why):
    if not ok:raise ValueError(why)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(x):
    x=Q(x);return [str(x.numerator),str(x.denominator)]


def rational(x):
    need(type(x) is list and len(x)==2 and all(type(y) is str for y in x),"rational type")
    q=Q(*map(int,x));need(x==encode(q),"canonical rational");return q


def scope(index):
    need(set(index)==set(SCOPE)|set(COUNTS)|{"profiles"},"index schema")
    for k,v in dict(SCOPE,**COUNTS).items():
        need(json.dumps(index[k],sort_keys=True)==json.dumps(v,sort_keys=True),"scope/count: "+k)
    need(len(index["profiles"])==5,"prefix coverage")
    need(2130706433**6//2**128==BUDGET and 2*D==134944,"field budget/near")


def inherited():
    path=NODES/"rate_half_mca_coupled_pair_rank_frontier/verify_audit.py"
    need(sha(path.read_bytes())==TRACE_PIN,"old legality checker pin")
    spec=importlib.util.spec_from_file_location("rank20_legal_LIST",path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def source_gate(parent,prior,masses):
    j0,j1=parent["J"];need(parent["mass_floor"]==masses[j0],"original mass, independently reconstructed")
    gate=parent["heights"][0];g=gate["gate"]
    need(gate["height"]==[0,0] and 567500<g<R-D,"constant gate scope")
    on=prior.list_cap(parent["on_trace"],R-567501,D-43,j1,11)
    off=prior.list_cap(gate["off_trace"],g-j1,D-42-j1,j1,11)
    raw=Q(581590844909990298+43*g*on+43*981147*off,44)+134945
    price=-(-raw.numerator//raw.denominator)
    need(price==gate["price"]<=270000000000000000,"original constant-pencil alternative")
    return g


def summaries(rows,parent,missing_large=False,write=False):
    # Reconstruct prices from the proposed boxes, independently of their claimed summaries.
    weights=[]
    for t in (1,2):
        small=[x for x in rows if x.get("kind")=="box" and x["t"]==t and x["size_class"]=="small"]
        large=[x for x in rows if x.get("kind")=="box" and x["t"]==t and x["size_class"]=="large"]
        alpha=max([Q(0)]+[Q((S-x["x"][0])*x["count"],x["x"][0]) for x in small])
        beta=max([Q(0)]+[(S-x["x"][0])*x["count"]-alpha*x["x"][0] for x in large])
        terminal=Q(t)+alpha*S+(0 if missing_large else 2*beta)
        factor=Q(1)
        for a in range(8):
            shared,pairs=11-a,20-2*a
            need(shared<pairs<=2*shared and pairs-shared==9-a,"actual anchor dimensions")
            factor*=Q(R+pairs-shared,D-t+pairs-shared)
        weights.append(terminal*factor)
        expected=dict(kind="cutoff",t=t,alpha=encode(alpha),beta=encode(beta),
                      terminal=encode(terminal),factor=encode(factor),raw_weight=encode(weights[-1]))
        position=next(i for i,x in enumerate(rows) if x.get("kind")=="cutoff" and x["t"]==t)
        if write:rows[position]=expected
        else:
            need(rows[position]==expected,"one shared packing budget, two large fibres, actual anchor factors")
            for key in ("alpha","beta","terminal","factor","raw_weight"):rational(rows[position][key])
    value=Q(parent["mass_floor"],3)+weights[0]/2+weights[1]/6
    residual=value.numerator//value.denominator+134944
    whole=max(residual,270000000000000000)
    expected=dict(kind="source",residual_bound=residual,whole_source_bound=whole,reserve=BUDGET-whole)
    if write:rows[-1]=expected
    else:need(rows[-1]==expected and whole<BUDGET,"original floor, alternatives by MAX, near once")
    return residual


def profile(rows,parent,pin,prior,masses):
    gate=source_gate(parent,prior,masses);j0,j1=parent["J"]
    need(rows[0]==dict(kind="profile",J=[j0,j1],parent_sha256=pin,constant_gate=gate),"original source header")
    position=1;boxes=0
    for t in (1,2):
        for lo,hi,kind in ((D+1-t,S//3,"small"),(S//3+1,S-gate-1,"large")):
            next_x=lo
            while next_x<=hi:
                row=rows[position];position+=1
                last=min(next_x+999,hi)
                need(set(row)=={"kind","t","size_class","x","count","trace"},"box schema")
                need(row["kind"]=="box" and type(row["t"]) is int and row["t"]==t
                     and row["size_class"]==kind and row["x"]==[next_x,last]
                     and all(type(x) is int for x in row["x"]),"complete mass partition")
                count=prior.list_cap(row["trace"],last-1,D-t,j1-8,3)
                need(type(row["count"]) is int and row["count"]==count,"dimension-three scalar cap")
                boxes+=1;next_x=last+1
        need(rows[position]["kind"]=="cutoff" and rows[position]["t"]==t,"cutoff boundary")
        position+=1
    need(position==len(rows)-1 and rows[-1]["kind"]=="source","exact row inventory")
    return summaries(rows,parent),boxes


def reject(action):
    try:action()
    except (ValueError,KeyError,TypeError,IndexError,StopIteration,ZeroDivisionError):return
    raise ValueError("accepted semantic mutation")


def controls():
    checked=0
    for total in range(6,31):
        threshold=total//3
        need(3*(threshold+1)>total,"integer large-fibre limit")
        for a in range(1,total):
            for b in range(1,total-a):
                c=total-a-b
                used=sum(Q(7,3)*x+(Q(11,2) if x>threshold else 0) for x in (a,b,c))
                need(used<=Q(7,3)*total+11,"shared-budget envelope")
                checked+=1
    # Two large fibres really can occur; replacing the factor two by one underpays.
    masses=[349526,349526,349525]
    need(sum(masses)==S and sum(x>S//3 for x in masses)==2,"two-large-fibre witness")
    need(sum(Q(7,3)*x+(Q(11,2) if x>S//3 else 0) for x in masses)>Q(7,3)*S+Q(11,2),
         "one-large-fibre shortcut fails")
    for j in (9965,10964,13964):
        for a in range(9):
            shared,second,pairs=11-a,9-a,20-2*a
            need(pairs==shared+second and (j-a)-second==j-9,"full-constant prefix dimensions/root bound")
    return checked


def main():
    raw=(NODE/"certificates/index.json").read_bytes();need(sha(raw)==PIN,"new index")
    index=json.loads(raw);scope(index)
    raw=(PARENT/"index.json").read_bytes();need(sha(raw)==PARENT_PIN,"original source index")
    refs=json.loads(raw)["profiles"][:5];prior=inherited();masses=prior.resource_floors()
    samples=[];total_boxes=size=0;next_j=9965
    for ref,old,expected in zip(index["profiles"],refs,PRICES):
        raw=(PARENT/old["path"]).read_bytes();need(sha(raw)==old["sha256"],"parent source pin")
        parent=json.loads(raw);need(parent["J"][0]==next_j,"contiguous original J");next_j=parent["J"][1]+1
        name=str(parent["J"][0])+".jsonl";need(ref["path"]==name,"shard path")
        raw=(NODE/"certificates"/name).read_bytes();need(sha(raw)==ref["sha256"],"shard pin");size+=len(raw)
        rows=[json.loads(x) for x in raw.splitlines()]
        price,boxes=profile(rows,parent,old["sha256"],prior,masses);total_boxes+=boxes
        need(price==expected and ref["residual_bound"]==price and ref["J"]==parent["J"]
             and ref["whole_source_bound"]==max(price,270000000000000000),"profile source price")
        samples.append((rows,parent,old["sha256"]))
    need(next_j==13965 and total_boxes==3166 and size==361476,"complete source prefix and inventory")
    need({p.name for p in (NODE/"certificates").iterdir()}=={"index.json",*[r["path"] for r in index["profiles"]]},
         "exact frozen inventory")
    mutations=0
    for key in dict(SCOPE,**COUNTS):
        bad=copy.deepcopy(index);bad[key]=None;reject(lambda:scope(bad));mutations+=1
    for which in ("missing","duplicate"):
        bad=copy.deepcopy(index)
        if which=="missing":bad["profiles"].pop()
        else:bad["profiles"].append(bad["profiles"][0])
        reject(lambda:scope(bad));mutations+=1
    rows,parent,pin=samples[-1]
    for mode in ("drop-box","gap","wrong-class","count","trace","gate","parent","factor","near","sum-alternatives","inside"):
        bad=copy.deepcopy(rows)
        if mode=="drop-box":bad.pop(1)
        elif mode=="gap":bad[1]["x"][0]+=1
        elif mode=="wrong-class":bad[1]["size_class"]="large"
        elif mode=="count":bad[1]["count"]-=1
        elif mode=="trace":bad[1]["trace"][-1][-1]-=1
        elif mode=="gate":bad[0]["constant_gate"]+=1
        elif mode=="parent":bad[0]["parent_sha256"]="0"*64
        elif mode=="near":bad[-1]["residual_bound"]-=134944
        elif mode=="sum-alternatives":bad[-1]["whole_source_bound"]+=270000000000000000
        else:
            entry=next(x for x in bad if x.get("kind")=="cutoff")
            entry["factor" if mode=="factor" else "terminal"]=encode(1)
        reject(lambda:profile(bad,parent,pin,prior,masses));mutations+=1
    # Fully reprice the cheaper ledger, not just its final hash or output integer.
    bad=copy.deepcopy(rows);summaries(bad,parent,missing_large=True,write=True)
    need(bad[-1]["residual_bound"]<rows[-1]["residual_bound"],"free-large-fibre mutation changes the price")
    reject(lambda:profile(bad,parent,pin,prior,masses));mutations+=1
    bad=copy.deepcopy(rows)
    for row in bad:
        if row.get("kind")=="box":
            row["trace"]=row["trace"][:2];row["count"]=row["trace"][-1][-1]
    summaries(bad,parent,write=True)
    need(bad[-1]["residual_bound"]<rows[-1]["residual_bound"],"wrong-dimension mutation changes the price")
    reject(lambda:profile(bad,parent,pin,prior,masses));mutations+=1
    print("PASS independent",total_boxes,"mass boxes;",3*total_boxes,"legal dimension-three LIST steps; five original gates")
    print("PASS",mutations,"semantic mutations, including fully repriced free large fibres and dimension2 substitution")
    print("PASS",controls(),"small packing controls and 27 exact prefix-dimension checks; not official witnesses")
    print("PAID original rank20 full constant11 J9965..13964:",COUNTS["whole_source_bound"],"RESERVE",COUNTS["reserve"])
    print("No other rank20 source, full-constant tail, rank21/22 or Prize closure")


if __name__=="__main__":
    main()
