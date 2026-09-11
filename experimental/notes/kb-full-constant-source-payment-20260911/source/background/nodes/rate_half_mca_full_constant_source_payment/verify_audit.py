"""Independent band-first nested-product audit; imports no new primary or selector."""
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path

NODE=Path(__file__).resolve().parent
NODES=NODE.parent
PARENT=NODES/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
PIN="d897c07874c516712d22d4767e6ee8d9b8bae99528a7698302489338d0f0dfb1"
PARENT_PIN="432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
COMPILER_PIN="bac33f24d1f34760518406185fcc9850d4fc61f5441486f94237e13b99eb8ca8"
AUDITOR_PIN="59b9ad4918ced72f90938f3ac5817f5c504aa7a1daa11818d3fcf560dff01d2f"
R,D,BUDGET=1048576,67472,274980728111395087
STATES=[(s,c) for s in range(12) for c in range(min(s,3)+1)]
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
    if not ok:raise ValueError(why)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def rational(raw):
    need(type(raw) is list and len(raw)==2 and all(type(x) is str for x in raw),"rational format")
    value=Q(int(raw[0]),int(raw[1]))
    need(raw==[str(value.numerator),str(value.denominator)],"canonical exact rational")
    return value


def encode(x):
    x=Q(x)
    return [str(x.numerator),str(x.denominator)]


def scope(data):
    extra={"profiles","degree_bands","scalar_LIST_steps","recurrence_identities","state_count",
           "source_bytes","residual_source_maximum","whole_source_bound","combined_large_pencil_bound"}
    need(set(data)==set(SCOPE)|extra,"index schema")
    for key,value in SCOPE.items():
        need(type(data[key]) is type(value) and data[key]==value,"scope: "+key)
    expected=dict(degree_bands=424,scalar_LIST_steps=93384,recurrence_identities=16112,
                  state_count=42,source_bytes=4672377,residual_source_maximum=239161133377346211,
                  whole_source_bound=270000000000000000,combined_large_pencil_bound=272127061148955779)
    for key,value in expected.items():
        need(type(data[key]) is int and data[key]==value,"exact ledger: "+key)
    need(len(data["profiles"])==13,"whole degree coverage")


def scalar(data,t,gate,dimension,degree,check):
    need(set(data)=={"c","degree","boxes","bound"},"whole-pencil schema")
    need(type(data["c"]) is int and data["c"]==dimension
         and type(data["degree"]) is int and data["degree"]==degree,"scalar physical degree plus1")
    intervals=[[a,min(a+9999,R-D+t)] for a in range(gate+1,R-D+t+1,10000)]
    need(len(data["boxes"])==len(intervals),"all union-complement boxes")
    costs=[]
    for row,interval in zip(data["boxes"],intervals):
        need(set(row)=={"e","trace","weight"} and row["e"]==interval,"union-complement partition")
        left,right=interval
        need(1<=D-t<=R-left and dimension<=degree and
             2130706433**6>=R-left+degree,"same-field scalar LIST and padding")
        count=check(row["trace"],R-left,D-t,degree,dimension)
        need(type(row["weight"]) is int and row["weight"]==t+right*count,"one preferred slope and original outside weight")
        costs.append(row["weight"])
    need(type(data["bound"]) is int and data["bound"]==max(costs),"whole-pencil maximum")
    return Q(data["bound"]),dimension*len(costs)


def profile(rows,parent,pin,check):
    need(rows[0]==dict(kind="profile",J=parent["J"],parent_sha256=pin,
                       constant_gate=parent["heights"][0]["gate"]),"original source and constant gate")
    j1=parent["J"][1];gate=rows[0]["constant_gate"]
    intervals=[[a,min(a+999,j1-11)] for a in range(0,j1-10,1000)]
    need(gate+1<=R-D+1 and len(rows)==2+2*len(intervals),"whole kappa/cutoff coverage")
    offset=1;steps=identities=0;top=[]
    for t in (1,2):
        prefix={state:Q(0) for state in STATES}
        for lo,hi in intervals:
            row=rows[offset];offset+=1
            need(set(row)=={"kind","t","kappa","base","states"} and row["kind"]=="band"
                 and type(row["t"]) is int and row["t"]==t
                 and row["kappa"]==[lo,hi],"canonical degree band")
            need(len(row["base"])==3 and len(row["states"])==42,"all terminal costs and branch states")
            bases=[]
            for c in (1,2,3):
                value,count=scalar(row["base"][c-1],t,gate,c,c+hi,check)
                bases.append(value);steps+=count
            for pos,(s,c) in enumerate(STATES):
                if s==c:
                    price=Q(R-D+t) if c==0 else bases[c-1]
                else:
                    ordinary=prefix[s-1,c]
                    difference=max(Q(0),prefix[s-1,c-1]-ordinary) if c else Q(0)
                    endpoints=[ordinary+((R-D+t)*ordinary+(x+c)*difference)/(D+s+x-t)
                               for x in (lo,hi)]
                    price=max(ordinary,*endpoints)
                    identities+=1
                need(rational(row["states"][pos])==price>=0,"band-first all-coordinate recurrence")
                prefix[s,c]=max(prefix[s,c],price)
        top.append(prefix[11,3])
    footer=rows[offset]
    need(set(footer)=={"kind","raw_prices","whole_source","reserve"} and footer["kind"]=="source","source footer")
    need([rational(x) for x in footer["raw_prices"]]==top,"all original low-raw weight, no extra anchor factor")
    raw=Q(parent["mass_floor"],3)+top[0]/2+top[1]/6
    cost=raw.numerator//raw.denominator+134944
    need(type(footer["whole_source"]) is int and footer["whole_source"]==cost
         and cost<=239161133377346211<BUDGET,"original source floor, higher raw and near once")
    need(footer["reserve"]==BUDGET-cost,"source reserve")
    return cost,steps,identities,2*len(intervals)


def reprice_without_roots(rows,parent):
    # A self-consistent but mathematically forbidden recipe, for a negative control.
    top=[]
    for t in (1,2):
        prefix={state:Q(0) for state in STATES}
        for row in rows:
            if row.get("kind")!="band" or row["t"]!=t:continue
            lo,hi=row["kappa"];row["states"]=[]
            for s,c in STATES:
                if s==c:
                    price=Q(R-D+t) if c==0 else Q(row["base"][c-1]["bound"])
                else:
                    ordinary=prefix[s-1,c]
                    price=max(ordinary,*[(R+s+x)*ordinary/(D+s+x-t) for x in (lo,hi)])
                row["states"].append(encode(price));prefix[s,c]=max(prefix[s,c],price)
        top.append(prefix[11,3])
    total=Q(parent["mass_floor"],3)+top[0]/2+top[1]/6
    cost=total.numerator//total.denominator+134944
    rows[-1]=dict(kind="source",raw_prices=[encode(x) for x in top],whole_source=cost,reserve=BUDGET-cost)


def reject(action):
    try:action()
    except (ValueError,KeyError,TypeError,IndexError,ZeroDivisionError):return
    raise ValueError("accepted semantic corruption")


def main():
    raw=(NODE/"certificates/index.json").read_bytes()
    need(sha(raw)==PIN,"frozen index")
    index=json.loads(raw);scope(index)
    ap=NODES/"rate_half_mca_coupled_pair_rank_frontier/verify_audit.py"
    need(sha(ap.read_bytes())==AUDITOR_PIN,"inherited independent LIST legality checker")
    spec=importlib.util.spec_from_file_location("nested_product_LIST_legality",ap)
    prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)
    need(sha((NODES/"list_padded_johnson_dimension_descent/compiler.py").read_bytes())==COMPILER_PIN,
         "selector provenance only, not imported")
    raw=(PARENT/"index.json").read_bytes()
    need(sha(raw)==PARENT_PIN,"original source index")
    refs=json.loads(raw)["profiles"];need(len(refs)==13,"parent coverage")
    maximum=steps=identities=bands=size=0;next_j=9965;sample=None
    for entry,ref in zip(index["profiles"],refs):
        need(set(entry)=={"path","sha256","J"} and entry["path"]==str(next_j)+".jsonl"
             and ref["path"]==str(next_j)+".json","canonical profile paths")
        raw=(PARENT/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"],"source profile pin")
        parent=json.loads(raw)
        need(entry["J"]==parent["J"] and parent["J"][0]==next_j,"no omitted original degree")
        next_j=parent["J"][1]+1
        raw=(NODE/"certificates"/entry["path"]).read_bytes();size+=len(raw)
        need(sha(raw)==entry["sha256"],"frozen shard pin")
        rows=[json.loads(line) for line in raw.splitlines()]
        cost,count,ids,num=profile(rows,parent,ref["sha256"],prior.list_cap)
        maximum=max(maximum,cost);steps+=count;identities+=ids;bands+=num
        sample=rows,parent,ref["sha256"]
    need(next_j==21500 and (maximum,steps,identities,bands,size)==
         (239161133377346211,93384,16112,424,4672377),"whole original finite ledger")
    need(max(maximum,270000000000000000)==index["whole_source_bound"]<BUDGET,"whole-source alternatives by MAX")
    need(max(index["whole_source_bound"],272127061148955779)==index["combined_large_pencil_bound"],
         "all maximum pencil dimensions at least10")
    need({p.name for p in (NODE/"certificates").iterdir()}==
         {"index.json",*(r["path"] for r in index["profiles"])},"no extra certificate")
    rejected=0
    for key in SCOPE:
        bad=copy.deepcopy(index);bad[key]=None
        reject(lambda:scope(bad));rejected+=1
    rows,parent,pin=sample
    for mode in ("missing","band","degree","box","trace","weight","base","state","root-state",
                 "point","source","near","extra-factor","gate"):
        bad=copy.deepcopy(rows);row=bad[1]
        if mode=="missing":bad.pop(1)
        elif mode=="band":row["kappa"][0]+=1
        elif mode=="degree":row["base"][2]["degree"]-=1
        elif mode=="box":row["base"][0]["boxes"][0]["e"][0]+=1
        elif mode=="trace":row["base"][2]["boxes"][0]["trace"][-1][-1]-=1
        elif mode=="weight":row["base"][1]["boxes"][0]["weight"]-=1
        elif mode=="base":row["base"][2]["bound"]-=1
        elif mode=="state":row["states"].pop()
        elif mode=="root-state":row["states"][STATES.index((4,2))]=["0","1"]
        elif mode=="point":row["states"][0]=["0","1"]
        elif mode=="source":bad[-1]["whole_source"]-=1
        elif mode=="near":bad[-1]["whole_source"]-=134944
        elif mode=="extra-factor":bad[-1]["raw_prices"][0]=encode(rational(bad[-1]["raw_prices"][0])*15)
        else:bad[0]["constant_gate"]+=1
        reject(lambda:profile(bad,parent,pin,prior.list_cap));rejected+=1
    bad=copy.deepcopy(rows);reprice_without_roots(bad,parent)
    reject(lambda:profile(bad,parent,pin,prior.list_cap));rejected+=1
    print("PASS independent",bands,"degree bands;",steps,"LIST transitions;",identities,"recurrence identities")
    print("SOURCE MAX",maximum,"WITH ALTERNATIVES",index["whole_source_bound"])
    print("PASS",rejected,"semantic mutations, including fully repriced omission of rank-one roots")
    print("All original source weights retained; maximum pencil dimensions8/9 and both Prizes open")


if __name__=="__main__":
    main()
