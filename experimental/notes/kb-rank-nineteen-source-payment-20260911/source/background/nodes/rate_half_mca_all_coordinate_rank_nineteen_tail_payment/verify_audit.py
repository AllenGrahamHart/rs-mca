"""Independent band-first all-coordinate audit; no new primary or selector import."""
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path

NODE=Path(__file__).resolve().parent
NODES=NODE.parent
PIN="37e1f226deb4ba670373090103ebe7d666200d3186542870c46595bf05797aae"
PARENT_PIN="432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
GATE_PIN="7b58ecc95009ca1a680784343b7121c25feca5ed238c3e9797daa381cc637d51"
COMPILER_PIN="bac33f24d1f34760518406185fcc9850d4fc61f5441486f94237e13b99eb8ca8"
AUDITOR_PIN="59b9ad4918ced72f90938f3ac5817f5c504aa7a1daa11818d3fcf560dff01d2f"
R,D,BUDGET=1048576,67472,274980728111395087
STATES=[(s,c) for s in range(12) for c in range(min(s,3)+1)]
SCOPE=dict(
    schema="all-coordinate-rank19-source-v1",field="2130706433^6",
    agreement=1116048,target_epsilon="2^-128",J=[9965,21499],
    paid_J=[13965,21499],original_error_rank=12,actual_P2_rank_max_on_paid_tail=19,
    new_regular_rank=19,shared_dimension=11,degree_band_width=500,
    complement_box_width=10000,degree_excess="kappa=D-(s-1)",
    tables=["unrestricted","full_generic"],joint_rank_types=[0,1,2],
    regular_exception_types=["rank1 generic","rank2 possibly nonregular"],
    rank0_bound="kappa+floor(c/2)",rank_le1_and_regular_bad_bound="kappa+c",
    shared_carrier_joint_LIST=True,field_extension_used=False,
    nonconstant_line_inside_charge="one coordinate globally, not t per coordinate",
    local_antecedent="after proved whole-source pencil alternatives are removed",
    G33_small_degree_allowance="only eight-regular-anchor history and D<2*(H+1)",
    original_weights=True,full_gcd_and_slack=True,near=134944,
    parent_index_sha256=PARENT_PIN,gate_index_sha256=GATE_PIN,compiler_sha256=COMPILER_PIN,
    unrestricted_rank19_all_J_paid=False,whole_J_closed=False,prize_closed=False,
)
COUNTS=dict(degree_bands=844,scalar_and_joint_LIST_steps=190088,recurrence_identities=64144,
            state_count_per_table=42,line_height_rows=1068,source_bytes=7648432,
            tail_regular_maximum=274839785069298661,all_regular_recipe_maximum=301343079910801930,
            combined_rank_le19_tail_bound=274839785069298661)
PRICES=[301343079910801930,298009161723159553,289619735724568996,281614409409587412,
        279132689723371234,274839785069298661,268216554549981924,262440067098698970,
        257081312254413222,256266170922774208,253605855460093996,245895886741509191,
        242164119085401614]


def need(ok,why):
    if not ok:raise ValueError(why)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def rational(raw):
    need(type(raw) is list and len(raw)==2 and all(type(x) is str for x in raw),"rational schema")
    value=Q(int(raw[0]),int(raw[1]))
    need(raw==[str(value.numerator),str(value.denominator)],"canonical rational")
    return value


def encode(x):
    return [str(x.numerator),str(x.denominator)]


def scope(index):
    need(set(index)==set(SCOPE)|set(COUNTS)|{"profiles"},"index schema")
    for key,value in dict(SCOPE,**COUNTS).items():
        need(type(index[key]) is type(value) and index[key]==value,"scope/count: "+key)
    need(len(index["profiles"])==13,"all original profiles")


def integer_line(height,gate,t,j1):
    den=D+1-t+height;ct=R-D+t
    need(den>0 and gate+1<=ct and 33*den>R+1+height-gate-1,"finite exhaustive integer corridor")
    cases=[]
    for population in range(1,33):
        end=min(ct,R+1+height-population*den)
        if end<gate+1:continue
        inside=t if height==0 else R+j1-end
        cost=min(population*ct,inside+population*end)
        cases.append([population,end,cost])
    need(bool(cases),"nonempty upper line envelope")
    return dict(cases=cases,bound=max(x[2] for x in cases))


def lines(parent,gates):
    j1=parent["J"][1];cap=j1-10
    rows=[]
    # Intersect each old interval with the parent regimes, including its tail.
    regions=[(i,x["height"][0],x["height"][1],x["gate"])
             for i,x in enumerate(parent["heights"]) if i]
    regions.append((None,regions[-1][2]+1,cap,0))
    for gi,old in enumerate(gates["bands"]):
        for pi,left,right,parent_gate in regions:
            lo=max(1,left,old["low"]);hi=min(cap,right,old["high"])
            if lo>hi:continue
            gate=max(old["gate"],parent_gate)
            rows.append(dict(height=[lo,hi],old_gate_row=gi,parent_height_row=pi,gate=gate,
                             cutoffs={str(t):integer_line(lo,gate,t,j1) for t in (1,2)}))
    rows.sort(key=lambda x:x["height"])
    next_h=1
    for row in rows:
        need(row["height"][0]==next_h,"all heights with no gaps/overlap")
        next_h=row["height"][1]+1
    need(next_h==cap+1,"complete original height range")
    g=parent["heights"][0]["gate"]
    return dict(kind="lines",constant_gate=g,
                constant={str(t):integer_line(0,g,t,j1) for t in (1,2)},heights=rows)


def bases(row,parent,ledger,check):
    lo,hi=row["kappa"];t=row["t"];gate=ledger["constant_gate"]
    line=max([ledger["constant"][str(t)]["bound"]]+
             [x["cutoffs"][str(t)]["bound"] for x in ledger["heights"] if x["height"][0]<=hi+1])
    need(row["line_cap"]==line,"all child line heights including constants")
    need(len(row["base"])==3,"three positive terminals")
    u={0:Q(R-D+t)};g=dict(u);steps=0
    for c,item in enumerate(row["base"],1):
        keys={"c","degree","boxes","constant"}
        if c>=2:keys|={"joint_trace","determinant","ff2","generic_ff2","small_normalization"}
        need(set(item)==keys and type(item["c"]) is int and item["c"]==c
             and type(item["degree"]) is int and item["degree"]==hi+c,"terminal shared degree")
        degree=c+hi;ct=R-D+t
        expected=[[a,min(a+9999,ct)] for a in range(gate+1,ct+1,10000)]
        need(len(item["boxes"])==len(expected),"all scalar complement boxes")
        costs=[]
        for box,(left,right) in zip(item["boxes"],expected):
            need(set(box)=={"e","trace","weight"} and box["e"]==[left,right],"original union complement")
            need(1<=D-t<=R-left and c<=degree and 2130706433**6>=R-left+degree,"same-field scalar padding")
            count=check(box["trace"],R-left,D-t,degree,c);steps+=c
            need(type(box["weight"]) is int and box["weight"]==t+right*count,"one preferred label and original weight")
            costs.append(box["weight"])
        need(type(item["constant"]) is int and item["constant"]==max(costs),"whole-constant maximum")
        u[c]=g[c]=Q(max(costs))
        if c==1:continue
        actual_degree=degree-1
        need(D-actual_degree+1-t>0 and 2130706433**6>=R+degree,"joint and determinant corridor")
        determinant=Q(R-actual_degree+1,D-actual_degree+1-t)*(ct if c==2 else line)
        count=check(item["joint_trace"],R,D-t,degree,c);steps+=c
        ff2=min(determinant,Q(ct*count))
        small=c==3 and actual_degree<2*((parent["J"][1]-1)//10+1)
        regular=min(ff2,Q(*map(int,parent["terminals"][t-1]))) if small else ff2
        need(rational(item["determinant"])==determinant and rational(item["ff2"])==ff2,
             "determinant/joint-list MINIMUM with original raw multiplier")
        need(type(item["small_normalization"]) is bool and item["small_normalization"]==small
             and rational(item["generic_ff2"])==regular,"G33 history and small-degree guard")
        u[c]=max(u[c],ff2);g[c]=max(g[c],regular)
    return u,g,steps


def advance(prefix_u,prefix_g,terminal_u,terminal_g,lo,hi,t,omit_nonregular=False,omit_rank1=False):
    # Omission switches construct negative controls, never an accepted ledger.
    top_u=top_g=None
    for s,c in STATES:
        if s==c:
            value_u,value_g=terminal_u[c],terminal_g[c]
        else:
            child=prefix_u[s-1,c]
            rank1=max(child,prefix_u[s-1,c-1]) if c else child
            rank0=max(rank1,prefix_u[s-1,c-2]) if c>=2 else rank1
            trial=[child]
            for kappa in (lo,hi):
                numerator=(R+s+kappa)*child+(kappa+c)*(rank1-child)
                numerator+=(kappa+c//2)*(rank0-rank1)
                trial.append(numerator/(D+s+kappa-t))
            value_u=max(trial)
            child=prefix_g[s-1,c];exception=child
            if c and not omit_rank1:exception=max(exception,prefix_g[s-1,c-1])
            if c>=2 and not omit_nonregular:exception=max(exception,prefix_u[s-1,c])
            value_g=max(child,*[((R+s+x)*child+(x+c)*(exception-child))/(D+s+x-t)
                                 for x in (lo,hi)])
        need(value_u>=0 and value_g>=0,"nonnegative prices")
        prefix_u[s,c]=max(prefix_u[s,c],value_u)
        prefix_g[s,c]=max(prefix_g[s,c],value_g)
        top_u,top_g=value_u,value_g
    return top_u,top_g


def profile(rows,parent,pin,gates,check,reprice_omission=False):
    need(rows[0]==dict(kind="profile",J=parent["J"],parent_sha256=pin),"original source pin")
    ledger=lines(parent,gates);need(rows[1]==ledger,"integer line ledger and height-valid source gates")
    j0,j1=parent["J"];intervals=[[a,min(a+499,j1-11)] for a in range(0,j1-10,500)]
    need(len(rows)==3+2*len(intervals),"all degree bands and cutoffs")
    pos=2;steps=0;top=[]
    for t in (1,2):
        pu={state:Q(0) for state in STATES};pg=dict(pu)
        for lo,hi in intervals:
            row=rows[pos];pos+=1
            need(set(row)=={"kind","t","kappa","line_cap","base","unrestricted","full_generic"}
                 and row["kind"]=="band" and type(row["t"]) is int and row["t"]==t
                 and row["kappa"]==[lo,hi],"canonical cutoff/degree band")
            tu,tg,count=bases(row,parent,ledger,check);steps+=count
            u,g=advance(pu,pg,tu,tg,lo,hi,t,reprice_omission,reprice_omission)
            if reprice_omission:
                row["unrestricted"]=encode(u);row["full_generic"]=encode(g)
            else:
                need(rational(row["unrestricted"])==u and rational(row["full_generic"])==g,
                     "independent all-coordinate recurrence with nonregular children")
        top.append(pg[11,3])
    total=Q(parent["mass_floor"],3)+top[0]/2+top[1]/6
    cost=total.numerator//total.denominator+134944;paid=j0>=13965
    expected=dict(kind="source",raw_prices=[encode(x) for x in top],regular_source=cost,
                  paid_profile=paid,reserve=BUDGET-cost)
    if reprice_omission:rows[-1]=expected
    else:need(rows[-1]==expected,"original source floor/higher raw/near once")
    if paid:need(cost<BUDGET,"paid original rank19 tail")
    return cost,steps,2*len(intervals),152*len(intervals),len(ledger["heights"])


def reject(action):
    try:action()
    except (ValueError,KeyError,TypeError,IndexError,ZeroDivisionError):return
    raise ValueError("accepted semantic corruption")


def main():
    raw=(NODE/"certificates/index.json").read_bytes();need(sha(raw)==PIN,"frozen index")
    index=json.loads(raw);scope(index)
    p=NODES/"rate_half_mca_coupled_pair_rank_frontier/verify_audit.py"
    need(sha(p.read_bytes())==AUDITOR_PIN,"independent LIST legality supplier")
    spec=importlib.util.spec_from_file_location("all_coordinate_legal_LIST",p)
    checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)
    check=checker.list_cap
    p=NODES/"list_padded_johnson_dimension_descent/compiler.py"
    need(sha(p.read_bytes())==COMPILER_PIN,"selector custody only; not imported")
    parent_dir=NODES/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
    raw=(parent_dir/"index.json").read_bytes();need(sha(raw)==PARENT_PIN,"parent index")
    refs=json.loads(raw)["profiles"]
    raw=(NODES/"rate_half_mca_coupled_pair_rank_frontier/gate_certificate.json").read_bytes()
    need(sha(raw)==GATE_PIN,"all-height source gates");gates=json.loads(raw)
    need(len(refs)==13,"parent profile count")
    total_steps=total_bands=total_identities=height_rows=size=0;prices=[];sample=None;next_j=9965
    need({p.name for p in (NODE/"certificates").iterdir()}=={"index.json"}|{str(x["J"][0])+".jsonl" for x in index["profiles"]},"complete shard inventory")
    for entry,ref in zip(index["profiles"],refs):
        need(set(entry)=={"path","sha256","J","regular_source"}
             and entry["path"]==str(next_j)+".jsonl" and ref["path"]==str(next_j)+".json","canonical profile paths")
        raw=(parent_dir/ref["path"]).read_bytes();need(sha(raw)==ref["sha256"],"parent profile")
        parent=json.loads(raw);need(entry["J"]==parent["J"] and parent["J"][0]==next_j,"whole J coverage")
        next_j=parent["J"][1]+1
        raw=(NODE/"certificates"/entry["path"]).read_bytes();size+=len(raw)
        need(sha(raw)==entry["sha256"],"shard hash")
        rows=[json.loads(line) for line in raw.splitlines()]
        cost,steps,bands,identities,heights=profile(rows,parent,ref["sha256"],gates,check)
        need(entry["regular_source"]==cost,"index source cost")
        prices.append(cost);total_steps+=steps;total_bands+=bands;total_identities+=identities;height_rows+=heights
        if parent["J"][0]==13965:sample=(rows,parent,ref["sha256"])
    need(next_j==21500 and prices==PRICES,"exact complete source profile results")
    need((total_steps,total_bands,total_identities,height_rows,size)==(190088,844,64144,1068,7648432),"independent coverage totals")
    tail=max(prices[5:]);combined=max(tail,274462040894062110,270000000000000000)
    need(combined==274839785069298661<BUDGET,"whole-source alternatives use MAXIMUM")
    mutations=0
    for key in set(SCOPE)|set(COUNTS):
        bad=copy.deepcopy(index);bad[key]=None;reject(lambda:scope(bad));mutations+=1
    rows,parent,pin=sample
    changes=[
        lambda x:x.pop(3),
        lambda x:x[2]["kappa"].__setitem__(0,1),
        lambda x:x[2].__setitem__("t",2),
        lambda x:x[2].__setitem__("line_cap",x[2]["line_cap"]-1),
        lambda x:x[1]["heights"][0].__setitem__("gate",0),
        lambda x:x[1]["constant"]["1"]["cases"].pop(),
        lambda x:x[2]["base"][0]["boxes"][0]["e"].__setitem__(0,0),
        lambda x:x[2]["base"][0]["boxes"][0].__setitem__("weight",0),
        lambda x:x[2]["base"][0]["boxes"][0]["trace"][0].__setitem__(2,0),
        lambda x:x[2]["base"][1].__setitem__("joint_trace",[]),
        lambda x:x[2]["base"][1].__setitem__("determinant",["1","1"]),
        lambda x:x[2]["base"][2].__setitem__("small_normalization",False),
        lambda x:x[2]["base"][2].__setitem__("generic_ff2",["1","1"]),
        lambda x:x[2].__setitem__("unrestricted",["0","1"]),
        lambda x:x[2].__setitem__("full_generic",["0","1"]),
        lambda x:x[-1].__setitem__("regular_source",0),
        lambda x:x[-1].__setitem__("paid_profile",False),
        lambda x:x[-1]["raw_prices"].__setitem__(0,["1","1"]),
        lambda x:x[-1].__setitem__("reserve",BUDGET),
    ]
    for change in changes:
        bad=copy.deepcopy(rows);change(bad)
        reject(lambda:profile(bad,parent,pin,gates,check));mutations+=1
    bad=copy.deepcopy(rows)
    wrong=profile(bad,parent,pin,gates,check,reprice_omission=True)[0]
    need(bad!=rows and wrong<rows[-1]["regular_source"],"genuine fully repriced cheaper forbidden recipe")
    reject(lambda:profile(bad,parent,pin,gates,check));mutations+=1
    # The nonregular term is dominated on this official sample. Test its
    # independent necessity with unequal synthetic terminal prices instead.
    tu={0:Q(1),1:Q(1),2:Q(1000000),3:Q(1)};tg={c:Q(1) for c in tu}
    pu={state:Q(0) for state in STATES};pg=dict(pu)
    advance(pu,pg,tu,tg,0,2,1)
    qu={state:Q(0) for state in STATES};qg=dict(qu)
    advance(qu,qg,tu,tg,0,2,1,omit_nonregular=True)
    need(pg[3,2]>qg[3,2],"nonregular-child synthetic price control")
    print("PASS independent",total_bands,"bands;",total_steps,"LIST transitions;",total_identities,"two-table identities")
    print("PASS",height_rows,"height atoms;",mutations,"semantic mutations including fully repriced omitted exceptional children")
    print("PASS nonregular-child synthetic price control; that term is dominated in the mutation sample")
    print("PAID actual P2 rank<=19, J13965..21499:",combined,"RESERVE",BUDGET-combined)
    print("Unpaid prefix recipe maximum",max(prices),"is NOT a source counterexample")
    print("Rank19 J9965..13964 and higher pair ranks remain; both Prizes OPEN")


if __name__=="__main__":
    main()
