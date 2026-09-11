"""Independent full-nu, band-first audit of the paid-normalization-ceiling source proof."""
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path

NODE=Path(__file__).resolve().parent
NODES=NODE.parent
PIN="c8adce1a573f9cb167705dce1234a75be2ca5b41f59f6e4479bdcc5cbc54d6bc"
PRIOR_PIN="37e1f226deb4ba670373090103ebe7d666200d3186542870c46595bf05797aae"
PARENT_PIN="432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
GEOMETRY_PIN="398b9ea9b246bb017e434efd4104ec897dac9e2e4ac38cbe4554d42f5d9747b7"
PRIOR_AUDIT_PIN="fc557d535bfd573b9affbefcc39211b55daf0e0483e441fc9481e6286f55961a"
TRACE_PIN="59b9ad4918ced72f90938f3ac5817f5c504aa7a1daa11818d3fcf560dff01d2f"
GATE_PIN="7b58ecc95009ca1a680784343b7121c25feca5ed238c3e9797daa381cc637d51"
R,D,BUDGET=1048576,67472,274980728111395087
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
COUNTS=dict(degree_bands=254,geometry_rows=1016,nu_candidates=900184,quotient_boxes=160107,
            low_recurrence_identities=2032,inherited_recurrence_identities=19304,
            source_bytes=423598,regular_prefix_maximum=249682145677014171,
            whole_prefix_rank_le19_bound=274462040894062110,
            whole_gap_rank_le19_bound=274839785069298661)
PRICES=[249604027270088959,243591486993244111,245976215664433629,241134325029679811,249682145677014171]


def need(ok,why):
    if not ok:raise ValueError(why)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def rational(x):
    need(type(x) is list and len(x)==2 and all(type(y) is str for y in x),"rational format")
    q=Q(*map(int,x));need(x==[str(q.numerator),str(q.denominator)],"canonical rational");return q


def encode(x):
    x=Q(x);return [str(x.numerator),str(x.denominator)]


def module(name,path,pin):
    need(sha(path.read_bytes())==pin,"inherited checker pin")
    spec=importlib.util.spec_from_file_location(name,path)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result);return result


def scope(index):
    need(set(index)==set(SCOPE)|set(COUNTS)|{"profiles"},"index schema")
    for key,value in dict(SCOPE,**COUNTS).items():
        need(type(index[key]) is type(value) and index[key]==value,"scope/count: "+key)
    need(len(index["profiles"])==5,"whole new prefix")


def full_nu_geometry(degree,s,H):
    limit=min(H,degree//(s-1));maximum=0;owner=None;boxes=0;previous=None
    need(4<=s<=11 and s-1<=degree<2130706433 and H>=1,"low-degree geometric scope")
    for nu in range(1,limit+1):
        image=degree//nu;h=H//nu+1
        if (image,h)!=previous:boxes+=1;previous=(image,h)
        branch=min(image-h*(s-2),max(1,h-2))
        value=0 if branch<1 else nu*(comb(image-s+2,2)*branch//comb(branch+h-1,2))
        if value>maximum:maximum=value;owner=[nu,image,h,branch]
    return dict(s=s,degree=degree,nu_max=limit,quotient_boxes=boxes,bound=maximum,argmax=owner)


def geometry(rows,intervals,H):
    need(len(rows)==len(intervals),"all geometric degree bands")
    candidates=boxes=0
    for row,interval in zip(rows,intervals):
        need(set(row)=={"kind","kappa","stages"} and row["kind"]=="geometry"
             and row["kappa"]==interval and len(row["stages"])==8,"geometry stage coverage")
        for stage,s in zip(row["stages"],range(4,12)):
            expected=full_nu_geometry(interval[1]+s-1,s,H)
            need(stage==expected,"ALL nu values and branch-weighted geometric ceiling")
            candidates+=expected["nu_max"];boxes+=expected["quotient_boxes"]
    return candidates,boxes


def prices(rows,old,parent,prior,check,reprice=False):
    intervals=[x["kappa"] for x in old if x.get("kind")=="band" and x["t"]==1]
    length=len(intervals);geo=rows[1:1+length];pos=1+length
    low_top=[];ledger=old[1]
    for t in (1,2):
        pu={state:Q(0) for state in prior.STATES};pg=dict(pu)
        low={s:Q(0) for s in range(3,12)}
        bands=[x for x in old if x.get("kind")=="band" and x["t"]==t]
        for i,(lo,hi) in enumerate(intervals):
            base_u,base_g,_=prior.bases(bands[i],parent,ledger,check)
            prior.advance(pu,pg,base_u,base_g,lo,hi,t)
            base=bands[i]["base"][2]
            current=max(Q(base["constant"]),min(rational(base["ff2"]),rational(parent["terminals"][t-1])))
            values=[current];low[3]=max(low[3],current)
            for s in range(4,12):
                ordinary=low[s-1];generic_exit=max(pg[s-1,2],pu[s-1,3])
                ceiling_exit=pg[s-1,3];beta=geo[i]["stages"][s-4]["bound"]
                increment_generic=max(Q(0),generic_exit-ordinary)
                increment_ceiling=max(Q(0),ceiling_exit-ordinary)
                values0=[ordinary]
                for kappa in (lo,hi):
                    numerator=(R+s+kappa)*ordinary+(kappa+3)*increment_generic+beta*increment_ceiling
                    values0.append(numerator/(D+s+kappa-t))
                current=min(pg[s,3],max(values0))
                values.append(current);low[s]=max(low[s],current)
            expected=dict(kind="low_band",t=t,kappa=[lo,hi],states=[encode(x) for x in values])
            if reprice:rows[pos]=expected
            else:need(rows[pos]==expected,"band-first paid exit recurrence, including all lower-degree prefixes")
            pos+=1
        low_top.append(low[11])
    value=Q(parent["mass_floor"],3)+low_top[0]/2+low_top[1]/6
    source=value.numerator//value.denominator+134944
    need(source<BUDGET,"whole original regular-rank19 prefix")
    expected=dict(kind="source",raw_prices=[encode(x) for x in low_top],regular_source=source,reserve=BUDGET-source)
    if reprice:rows[pos]=expected
    else:need(rows[pos]==expected,"original floor/higher raw/near, no extra anchor factor")
    return source


def profile(rows,old,parent,old_pin,parent_pin,prior,check,gates):
    j0,j1=parent["J"];H=(j1-1)//10
    need(rows[0]==dict(kind="profile",J=parent["J"],H=H,prior_sha256=old_pin,parent_sha256=parent_pin),
         "original profile and normalization ceiling")
    intervals=[x["kappa"] for x in old if x.get("kind")=="band" and x["t"]==1]
    need(len(rows)==2+3*len(intervals),"full geometry/two-cutoff coverage")
    prior.profile(old,parent,parent_pin,gates,check)
    candidates,boxes=geometry(rows[1:1+len(intervals)],intervals,H)
    price=prices(rows,old,parent,prior,check)
    return price,candidates,boxes,len(intervals)


def reject(action):
    try:action()
    except (ValueError,KeyError,TypeError,IndexError,ZeroDivisionError):return
    raise ValueError("accepted semantic corruption")


def main():
    raw=(NODE/"certificates/index.json").read_bytes();need(sha(raw)==PIN,"new frozen index")
    index=json.loads(raw);scope(index)
    prior=module("paid_ceiling_prior_audit",NODES/"rate_half_mca_all_coordinate_rank_nineteen_tail_payment/verify_audit.py",PRIOR_AUDIT_PIN)
    check=module("paid_ceiling_legal_trace",NODES/"rate_half_mca_coupled_pair_rank_frontier/verify_audit.py",TRACE_PIN).list_cap
    need(sha((NODES/"rational_curve_inner_projection_branch_budget/bounds.py").read_bytes())==GEOMETRY_PIN,
         "geometry provenance; not imported")
    old_dir=NODES/"rate_half_mca_all_coordinate_rank_nineteen_tail_payment/certificates"
    raw=(old_dir/"index.json").read_bytes();need(sha(raw)==PRIOR_PIN,"old table index")
    old_index=json.loads(raw);prior.scope(old_index)
    parent_dir=NODES/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
    raw=(parent_dir/"index.json").read_bytes();need(sha(raw)==PARENT_PIN,"source index")
    parents=json.loads(raw)["profiles"]
    raw=(NODES/"rate_half_mca_coupled_pair_rank_frontier/gate_certificate.json").read_bytes()
    need(sha(raw)==GATE_PIN,"inherited source gates");gates=json.loads(raw)
    need({x.name for x in (NODE/"certificates").iterdir()}=={"index.json"}|{str(x["J"][0])+".jsonl" for x in index["profiles"]},
         "exact shard inventory")
    costs=[];size=candidates=boxes=bands=0;sample=None;next_j=9965
    for entry,old_ref,parent_ref in zip(index["profiles"],old_index["profiles"],parents):
        need(set(entry)=={"path","sha256","J","regular_source"} and entry["path"]==str(next_j)+".jsonl"
             and old_ref["path"]==entry["path"] and parent_ref["path"]==str(next_j)+".json","canonical original profiles")
        raw=(old_dir/old_ref["path"]).read_bytes();need(sha(raw)==old_ref["sha256"],"old shard")
        old=[json.loads(x) for x in raw.splitlines()]
        raw=(parent_dir/parent_ref["path"]).read_bytes();need(sha(raw)==parent_ref["sha256"],"source shard")
        parent=json.loads(raw);need(entry["J"]==parent["J"] and parent["J"][0]==next_j,"complete prefix degrees")
        next_j=parent["J"][1]+1
        raw=(NODE/"certificates"/entry["path"]).read_bytes();size+=len(raw)
        need(sha(raw)==entry["sha256"],"new shard")
        rows=[json.loads(x) for x in raw.splitlines()]
        args=(old,parent,old_ref["sha256"],parent_ref["sha256"],prior,check,gates)
        price,n,b,m=profile(rows,*args)
        need(entry["regular_source"]==price,"index source price")
        costs.append(price);candidates+=n;boxes+=b;bands+=2*m
        if sample is None:sample=(rows,args)
    need(next_j==13965 and costs==PRICES,"all five original-source prices")
    need((size,candidates,boxes,bands)==(423598,900184,160107,254),"independent completeness totals")
    need(4*bands==1016 and 8*bands==2032 and 76*bands==19304,"geometry and recurrence coverage")
    prefix=max(max(costs),274462040894062110,270000000000000000)
    full=max(prefix,old_index["combined_rank_le19_tail_bound"])
    need(prefix==274462040894062110 and full==274839785069298661<BUDGET,"all source alternatives by MAXIMUM")
    mutations=0
    for key in set(SCOPE)|set(COUNTS):
        bad=copy.deepcopy(index);bad[key]=None;reject(lambda:scope(bad));mutations+=1
    rows,args=sample
    first_low=next(i for i,x in enumerate(rows) if x["kind"]=="low_band")
    positive=next(i for i,x in enumerate(rows) if x["kind"]=="geometry" and any(s["bound"] for s in x["stages"]))
    changes=[
        lambda x:x[0].__setitem__("H",x[0]["H"]+1),
        lambda x:x.pop(2),
        lambda x:x[1]["kappa"].__setitem__(0,1),
        lambda x:x[positive]["stages"][0].__setitem__("bound",0),
        lambda x:x[positive]["stages"][0].__setitem__("nu_max",1),
        lambda x:x[positive]["stages"][0].__setitem__("quotient_boxes",0),
        lambda x:x[positive]["stages"][0].__setitem__("argmax",None),
        lambda x:x[first_low].__setitem__("t",2),
        lambda x:x[first_low]["states"].__setitem__(0,["0","1"]),
        lambda x:x[first_low]["states"].__setitem__(1,["0","1"]),
        lambda x:x[-1]["raw_prices"].__setitem__(0,["1","1"]),
        lambda x:x[-1].__setitem__("regular_source",0),
        lambda x:x[-1].__setitem__("reserve",BUDGET),
    ]
    for change in changes:
        bad=copy.deepcopy(rows);change(bad)
        reject(lambda:profile(bad,*args));mutations+=1
    bad=copy.deepcopy(rows)
    for row in bad:
        if row["kind"]=="geometry":
            for stage in row["stages"]:stage["bound"]=0;stage["argmax"]=None
    wrong=prices(bad,args[0],args[1],prior,check,reprice=True)
    need(wrong<rows[-1]["regular_source"],"genuine fully repriced free-jump corruption")
    reject(lambda:profile(bad,*args));mutations+=1
    print("PASS independent full-nu scan:",candidates,"values;",boxes,"quotient intervals;",bands,"low bands")
    print("PASS",8*bands,"paid-ceiling and",76*bands,"inherited recurrence identities")
    print("PASS",mutations,"semantic mutations including fully repriced free normalization jumps")
    print("PAID ALL actual P2 rank<=19 J9965..21499:",full,"RESERVE",BUDGET-full)
    print("Lower-prefix regular maximum",max(costs),"with original alternatives",prefix)
    print("Pair ranks20..22, higher original ranks and both Prizes remain OPEN")


if __name__=="__main__":
    main()
