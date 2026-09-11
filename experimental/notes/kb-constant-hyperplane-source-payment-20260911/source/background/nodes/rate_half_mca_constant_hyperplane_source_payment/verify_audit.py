"""Independent band-first recurrence and exact LIST audit; no new primary imports."""
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
PIN="6de686c86dab4b99ffc858df59744e8a3c480e959a4587d25bd95573d3c9cec3"
PARENT_PIN="432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
COMPILER_PIN="bac33f24d1f34760518406185fcc9850d4fc61f5441486f94237e13b99eb8ca8"
AUDITOR_PIN="59b9ad4918ced72f90938f3ac5817f5c504aa7a1daa11818d3fcf560dff01d2f"
R,D,S,BUDGET=1048576,67472,1048577,274980728111395087
SCOPE=dict(
    schema="constant-hyperplane-source-v1",field="2130706433^6",
    agreement=1116048,target_epsilon="2^-128",J=[9965,21499],
    original_error_rank=12,actual_P2_rank=19,shared_dimension=11,
    constant_dimension=10,constant_dimension11_excluded=True,
    normalization_cap_required=False,
    local_antecedent="after proved whole-source pencil alternatives are removed",
    degree_excess="zeta=E-(s-2)",shared_stages=[4,5,6,7,8,9,10,11],
    degree_band_width=2000,mass_box_width=5000,complement_box_width=10000,
    large_mass_threshold=349525,large_mass_count_max=2,
    original_weights=True,full_gcd_and_slack=True,near=134944,
    parent_index_sha256=PARENT_PIN,compiler_sha256=COMPILER_PIN,
    whole_constant4_penultimate_paid=False,unrestricted_rank19_paid=False,prize_closed=False,
)


def need(ok,why):
    if not ok:
        raise ValueError(why)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def q(raw):
    need(type(raw) is list and len(raw)==2 and all(type(x) is str for x in raw),"rational type")
    value=Q(int(raw[0]),int(raw[1]))
    need(raw==[str(value.numerator),str(value.denominator)],"canonical rational")
    return value


def scope(data):
    extra={"profiles","degree_bands","scalar_LIST_steps","residual_source_maximum",
           "whole_source_bound","combined_maximum_pencil10_bound","source_bytes"}
    need(set(data)==set(SCOPE)|extra,"index schema")
    for key,value in SCOPE.items():
        need(type(data[key]) is type(value) and data[key]==value,"scope: "+key)
    need(len(data["profiles"])==13 and data["degree_bands"]==218
         and data["scalar_LIST_steps"]==119988 and data["source_bytes"]==2788463,"source inventory")
    need(data["residual_source_maximum"]==266908096047530929
         and data["whole_source_bound"]==270000000000000000
         and data["combined_maximum_pencil10_bound"]==272127061148955779,"source-class bounds")


def compression(data,t,gate,degree,dimension,check):
    need(set(data)=={"degree","dimension","boxes","alpha","beta","bound"},"compression schema")
    need(type(data["degree"]) is int and data["degree"]==degree
         and data["dimension"]==dimension,"primitive scalar degree plus1")
    intervals=[]
    for low,high in ((D+1-t,349525),(349526,S-gate-1)):
        intervals.extend([a,min(a+4999,high)] for a in range(low,high+1,5000))
    need(len(data["boxes"])==len(intervals),"all shifted masses")
    values=[]
    for row,ends in zip(data["boxes"],intervals):
        need(set(row)=={"x","trace"} and row["x"]==ends,"integer mass partition")
        a,b=ends
        count=check(row["trace"],b-1,D-t,degree,dimension)
        values.append((a,b,(S-a)*count))
    alpha=max(Q(cost,a) for a,b,cost in values if b<=349525)
    beta=max([Q(0)]+[cost-alpha*a for a,b,cost in values if a>=349526])
    bound=t+S*alpha+2*beta
    need(q(data["alpha"])==alpha>=0 and q(data["beta"])==beta>=0,"two-large-fibre dual prices")
    need(q(data["bound"])==bound,"one inside charge and shared mass")
    return bound,len(values)*dimension


def whole(data,t,gate,degree,check):
    need(set(data)=={"degree","boxes","bound"} and data["degree"]==degree,"whole scalar3 degree")
    ends=[[a,min(a+9999,R-D+t)] for a in range(gate+1,R-D+t+1,10000)]
    need(len(data["boxes"])==len(ends),"all core union complements")
    values=[]
    for row,interval in zip(data["boxes"],ends):
        need(set(row)=={"e","trace","weight"} and row["e"]==interval,"complement partition")
        a,b=interval;count=check(row["trace"],R-a,D-t,degree,3)
        need(type(row["weight"]) is int and row["weight"]==t+b*count,"original weighted whole pencil")
        values.append(row["weight"])
    need(type(data["bound"]) is int and data["bound"]==max(values),"whole pencil maximum")
    return Q(max(values)),3*len(values)


def profile(rows,parent,pin,check):
    head=rows[0]
    need(head==dict(kind="profile",J=parent["J"],parent_sha256=pin,
                    constant_gate=parent["heights"][0]["gate"]),"original source profile")
    j1=parent["J"][1];gate=head["constant_gate"]
    need(349525<S-gate-1<S and 3*349526>S and D+1<=R-gate,"integer-fibre and field corridor")
    intervals=[[a,min(a+1999,j1-10)] for a in range(0,j1-9,2000)]
    need(len(rows)==2+2*len(intervals),"no missing or extra degree-band record")
    total=Q(parent["mass_floor"],3);offset=1;steps=0;maxima={}
    for t,den in ((1,2),(2,6)):
        prefix=[Q(0)]*8
        for lo,hi in intervals:
            data=rows[offset];offset+=1
            need(set(data)=={"kind","t","zeta","root_count","C2","U3","C4","prices"},"band schema")
            need(data["kind"]=="band" and type(data["t"]) is int and data["t"]==t
                 and data["zeta"]==[lo,hi],"complete cutoff/degree-excess band")
            root=j1-10-lo
            need(type(data["root_count"]) is int and data["root_count"]==root,"D-E at lower degree")
            c2,n=compression(data["C2"],t,gate,hi+2,2,check);steps+=n
            u3,n=whole(data["U3"],t,gate,hi+3,check);steps+=n
            c4,n=compression(data["C4"],t,gate,hi+4,4,check);steps+=n
            need(len(data["prices"])==8,"every shared dimension4..11")
            current=c2+Q(root,S)*max(Q(0),u3-c2)
            need(q(data["prices"][0])==current,"base partial-constant price")
            prefix[0]=max(prefix[0],current)
            for position,s in enumerate(range(5,12),1):
                ordinary=prefix[position-1]
                full=Q(D+1-t,S)*c4
                current=ordinary+Q(root,R+s-3)*max(Q(0),full-ordinary)
                need(q(data["prices"][position])==current,"band-first ancestor recurrence and prefix max")
                prefix[position]=max(prefix[position],current)
        maxima[str(t)]=prefix
        factor=prod(Q(R+i,D-t+i) for i in range(1,9))
        total+=factor*prefix[-1]/den
    tail=rows[offset]
    need(set(tail)=={"kind","stage_maxima","normalized","whole_source","reserve"}
         and tail["kind"]=="source" and set(tail["stage_maxima"])=={"1","2"},"source footer")
    for t in (1,2):
        need([q(x) for x in tail["stage_maxima"][str(t)]]==maxima[str(t)],"whole-stage maxima")
    need([q(x) for x in tail["normalized"]]==[maxima[str(t)][-1] for t in (1,2)],"original normalized raw prices")
    price=total.numerator//total.denominator+134944
    need(type(tail["whole_source"]) is int and tail["whole_source"]==price
         and price<=266908096047530929<BUDGET,"whole original source with higher raw and near once")
    need(tail["reserve"]==BUDGET-price,"exact source reserve")
    return price,steps,len(intervals)*2


def reject(action):
    try:action()
    except (ValueError,TypeError,KeyError,IndexError,ZeroDivisionError):return
    raise ValueError("accepted semantic corruption")


def main():
    raw=(NODE/"certificates/index.json").read_bytes()
    need(sha(raw)==PIN,"frozen index")
    index=json.loads(raw);scope(index)
    ap=NODES/"rate_half_mca_coupled_pair_rank_frontier/verify_audit.py"
    need(sha(ap.read_bytes())==AUDITOR_PIN,"independent inherited legal-trace checker")
    spec=importlib.util.spec_from_file_location("hyperplane_LIST_legality",ap)
    prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)
    need(sha((NODES/"list_padded_johnson_dimension_descent/compiler.py").read_bytes())==COMPILER_PIN,
         "selector provenance; not imported")
    raw=(PARENT/"index.json").read_bytes()
    need(sha(raw)==PARENT_PIN,"parent index")
    refs=json.loads(raw)["profiles"]
    maximum=0;steps=0;bands=0;size=0;next_j=9965;sample=None
    for entry,ref in zip(index["profiles"],refs):
        need(set(entry)=={"path","sha256","J"} and entry["path"]==str(next_j)+".jsonl"
             and ref["path"]==str(next_j)+".json","canonical source paths")
        raw=(PARENT/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"],"source profile hash")
        parent=json.loads(raw)
        need(entry["J"]==parent["J"] and parent["J"][0]==next_j,"whole J coverage")
        next_j=parent["J"][1]+1
        raw=(NODE/"certificates"/entry["path"]).read_bytes()
        need(sha(raw)==entry["sha256"],"degree shard hash");size+=len(raw)
        rows=[json.loads(line) for line in raw.splitlines()]
        value,count,number=profile(rows,parent,ref["sha256"],prior.list_cap)
        maximum=max(maximum,value);steps+=count;bands+=number
        sample=rows,parent,ref["sha256"]
    need(next_j==21500 and maximum==index["residual_source_maximum"]
         and steps==119988 and bands==218 and size==2788463,"entire finite ledger")
    need(max(maximum,270000000000000000)==index["whole_source_bound"]<BUDGET,"alternative caps use MAXIMUM")
    need(max(index["whole_source_bound"],272127061148955779)==index["combined_maximum_pencil10_bound"],
         "constant/nonconstant source alternatives")
    need({p.name for p in (NODE/"certificates").iterdir()}==
         {"index.json",*(r["path"] for r in index["profiles"])},"no unlisted certificate")
    rejected=0
    for key in SCOPE:
        bad=copy.deepcopy(index);bad[key]=None
        reject(lambda:scope(bad));rejected+=1
    rows,parent,pin=sample
    for mode in ("missing","wrong-band","root-count","scalar-degree","mass","trace",
                 "alpha","whole","stage","owner","source","near","gate"):
        bad=copy.deepcopy(rows);band=bad[1]
        if mode=="missing":bad.pop(1)
        elif mode=="wrong-band":band["zeta"][0]+=1
        elif mode=="root-count":band["root_count"]-=1
        elif mode=="scalar-degree":band["C4"]["degree"]-=1
        elif mode=="mass":band["C2"]["boxes"][0]["x"][0]+=1
        elif mode=="trace":band["C4"]["boxes"][0]["trace"][-1][-1]-=1
        elif mode=="alpha":band["C2"]["alpha"]=["0","1"]
        elif mode=="whole":band["U3"]["bound"]-=1
        elif mode=="stage":band["prices"][-1][0]=str(int(band["prices"][-1][0])+1)
        elif mode=="owner":band["U3"]["boxes"][0]["weight"]-=1
        elif mode=="source":bad[-1]["whole_source"]-=1
        elif mode=="near":bad[-1]["whole_source"]-=134944
        else:bad[0]["constant_gate"]+=1
        reject(lambda:profile(bad,parent,pin,prior.list_cap));rejected+=1
    print("PASS independent",bands,"bands;",steps,"LIST steps; eight-stage band-first recurrence")
    print("SOURCE MAX",maximum,"WITH ALTERNATIVES",index["whole_source_bound"])
    print("PASS",rejected,"semantic mutations with outer hashes bypassed")
    print("Some intermediate prices exceed old L_t; whole original resource, not allocated local budget, pays them")
    print("Maximum-pencil10 source class paid; unrestricted rank19 and both Prizes remain open")


if __name__=="__main__":
    main()
