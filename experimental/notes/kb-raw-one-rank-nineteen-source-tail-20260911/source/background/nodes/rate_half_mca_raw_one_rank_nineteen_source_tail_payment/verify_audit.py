"""Independent P1 rank19 case ledger, weighted enclosure, and source resource audit."""
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import prod
from pathlib import Path

NODE=Path(__file__).resolve().parent
NODES=NODE.parent
R,D,E,BUDGET=1048576,67472,21499,274980728111395087
PIN="73653350ec681ef68a9ed3385d5cddb352d1f1052a873fd5070a9e44bd29cc28"
PINS={
    "rate_half_mca_all_coordinate_rank_nineteen_tail_payment/certificates/index.json": "37e1f226deb4ba670373090103ebe7d666200d3186542870c46595bf05797aae",
    "rate_half_mca_all_coordinate_rank_nineteen_tail_payment/certificates/20965.jsonl": "d1eab8b31949c355998a9831ee4a022b94ee947a5fd88c326d9795c5161f311a",
    "rate_half_mca_regular_rational_plane_terminal_bounds/certificates/20965.json": "b508835f0104f231a0bba86d38418fe270a2a1e05fa46f4a4a1debd0dd8d9633",
    "rate_half_mca_coupled_pair_rank_frontier/gate_certificate.json": "7b58ecc95009ca1a680784343b7121c25feca5ed238c3e9797daa381cc637d51",
    "rate_half_mca_raw_one_projection_rank_nine_source_tail_payment/certificate.json": "274a1f94ae1c81caabe2c8bc13ba1251756c01273f3e0613792f5259a355f8fc",
    "rate_half_mca_raw_two_quadratic_normal_payment/certificate.json": "3174586f037592a2a0025e7b89ef37bfcff353f7f3450708b3225245b6bee6f5",
    "rate_half_mca_min_envelope_raw_mass/verify.py": "b6745db5995bdf421755408a54a92f052beadff4747391f62b93733b51be8867",
    "mca_min_envelope_fiber_contraction/polynomial.py": "d5cae0ac19b4cb4d7cbe0ebb67d1645204322b30b09ee003ec42b44cf3f4f3c9"
}
SCOPE=dict(
    schema="raw-one-rank19-source-tail-v1",field="2130706433^6",
    n=2097152,k=1048576,agreement=1116048,target_epsilon="2^-128",
    original_error_rank=12,raw_weight_J=[9965,21499],paid_J=[20618,21499],
    actual_family="P1: pairs assigned original raw exactly one",
    actual_P1_pair_affine_rank_max=19,P2_rank_restriction=False,P2_projection_restriction=False,
    residual_antecedent="after paid original whole-source pencil alternatives",
    enclosure_pair_dimension=19,shared_dimension=11,actual_enclosure_occupation_required=False,
    generic_augmentation="one ORIGINAL-field constant vector when generic rank is10 and actual rank<=18",
    proper_carrier_bound=78301130139301820,small_projection_bound=31878195092556089,
    quadratic_contained_mass=89070753921055403,quadratic_moving_labels=21490,
    generic_raw_one_bound=180336660306614524,
    inherited_table_use="t=1 weighted enclosures only; no inherited whole P2 source conclusion",
    lower_J_inherited_in_G=False,upper_degree=21499,normalization_history="eight actual regular ancestors at G33",
    U_nonregular_children_retained=True,original_owners_weights_field=True,extra_anchor_factor=False,
    original_near=134944,source_identity="floor((original min(raw,9) resource+N1)/2)+near",
    source_alternatives="MAXIMUM",whole_source_bound=274978423712566784,reserve=2304398828303,
    J20617_unsafe_claim=False,all_original_rank12_sources_closed=False,
    active_v4_atom=False,ordinary_LIST_closed=False,adjacent_safe_row_closed=False,prize_closed=False,
)
KEYS={"scope","supplier_pins","case_raw_one_bounds","generic_rational","degree_bands",
      "t1_LIST_steps","t1_recurrences","line_height_rows","endpoints"}


def need(ok,why):
    if not ok:raise ValueError(why)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def same(a,b):
    return json.dumps(a,sort_keys=True)==json.dumps(b,sort_keys=True)


def encode(value):
    return [str(value.numerator),str(value.denominator)]


def read(relative,pin=None):
    data=(NODES/relative).read_bytes()
    need(sha(data)==(PINS[relative] if pin is None else pin),"source bytes: "+relative)
    return data


def module(relative,pin,name):
    read(relative,pin)
    spec=importlib.util.spec_from_file_location(name,NODES/relative)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result)
    return result


def header(data):
    need(set(data)==KEYS and same(data["scope"],SCOPE),"exact P1-only source scope")
    need(data["supplier_pins"]==PINS,"supplier custody")
    need(data["t1_LIST_steps"]==11051 and data["t1_recurrences"]==3268
         and data["line_height_rows"]==109,"weighted coverage")
    need(2130706433**6//2**128==BUDGET,"original field denominator")


def weighted(rows,parent,gates,audit,legal,omission=None):
    ledger=audit.lines(parent,gates)
    need(rows[1]==ledger,"original all-height integer line prices")
    pu={state:Q(0) for state in audit.STATES};pg=dict(pu)
    prices=[];steps=0
    bands=[row for row in rows if row["kind"]=="band" and row["t"]==1]
    intervals=[[lo,min(lo+499,E-11)] for lo in range(0,E-10,500)]
    need([r["kappa"] for r in bands]==intervals,"all raw-one degree bands")
    for row in bands:
        tu,tg,count=audit.bases(row,parent,ledger,legal.list_cap)
        lo,hi=row["kappa"]
        x,y=audit.advance(pu,pg,tu,tg,lo,hi,1,
                          omit_nonregular=omission in ("nonregular","both"),
                          omit_rank1=omission in ("rank1","both"))
        if omission is None:
            need(audit.rational(row["unrestricted"])==x
                 and audit.rational(row["full_generic"])==y,"independent U/G identities")
        prices.append(dict(kappa=[lo,hi],G11=encode(y)));steps+=count
    need((len(prices),steps,76*len(prices),len(ledger["heights"]))==(43,11051,3268,109),
         "complete t1 replay, not the discarded P2 source recipe")
    return prices,max(Q(*map(int,row["G11"])) for row in prices)


def case_prices(projection,quadratic):
    proper=Q(prod(R+i for i in range(11)),
             11*(D+8)*prod(D-2+j for j in range(1,10)))
    need(R+E-10-11*(D+E-2)==91406>0,"whole proper-carrier monotonicity")
    p=quadratic["parameters"]
    need(p["normal_degree"]==2 and p["basis_raw"]==7
         and p["basis_floor5"]==222676884802638507,"uniform basis, not G7 containment")
    contained=2*(p["basis_floor5"]+1)//5
    moving=E-9
    need(contained==quadratic["mass_cap"]==89070753921055403
         and moving==quadratic["moving_zeros"]==21490,"retained mass plus raw-one moving labels")
    return dict(proper_carrier=int(proper),small_projection=projection,
                quadratic_normal=contained+moving)


def endpoints(data,omega,mass,branches):
    need(len(data["endpoints"])==2,"adjacent recipe endpoints")
    factor=12*prod(D-9+i for i in range(1,11))
    result=[]
    for row,j in zip(data["endpoints"],(20617,20618)):
        basis=min(mass.value(p,j) for p in branches)
        ratio=Q(prod(R+j-i for i in range(12)),factor)/basis
        floor=ratio.numerator//ratio.denominator
        value=(floor+omega)//2+2*D
        expected=dict(J=j,mass_ratio=encode(ratio),mass_floor=floor,residual=value,
                      whole=max(value,270000000000000000),reserve=BUDGET-value)
        need(same(row,expected),"unshifted original resource and two-level raw identity")
        result.append(value)
    need(result[0]>BUDGET>=result[1]==274978423712566784
         and BUDGET-result[1]==2304398828303,"recipe boundary, not actual unsafety")
    return result


def validate(data,prices,generic,cases,mass,branches):
    header(data)
    need(same(data["degree_bands"],prices) and data["generic_rational"]==encode(generic),
         "all original-weight enclosure prices")
    expected=dict(cases,generic_enclosure=generic.numerator//generic.denominator)
    need(same(data["case_raw_one_bounds"],expected),"four exhaustive case costs")
    omega=max(expected.values())
    need(omega==180336660306614524,"case MAXIMUM, not addition or minimum")
    return endpoints(data,omega,mass,branches)


def reprice(data,divisor=2,near=134944,maximum=True):
    costs=data["case_raw_one_bounds"].values()
    omega=max(costs) if maximum else min(costs)
    for row in data["endpoints"]:
        value=(row["mass_floor"]+omega)//divisor+near
        row.update(residual=value,whole=max(value,270000000000000000),reserve=BUDGET-value)


def reject(action):
    try:action()
    except (ValueError,KeyError,TypeError,IndexError,ZeroDivisionError):return
    raise ValueError("accepted malformed P1 proof ledger")


def linear_controls():
    def rank(rows):
        a=[[x%101 for x in row] for row in rows];r=0
        for col in range(len(a[0])):
            pivot=next((j for j in range(r,len(a)) if a[j][col]),None)
            if pivot is None:continue
            a[r],a[pivot]=a[pivot],a[r]
            inv=pow(a[r][col],-1,101);a[r]=[x*inv%101 for x in a[r]]
            for j in range(r+1,len(a)):
                factor=a[j][col]
                a[j]=[(x-factor*y)%101 for x,y in zip(a[j],a[r])]
            r+=1
            if r==len(a):break
        return r

    def projection(rows,s):
        # Max minors have degree at most s; s+1 distinct points detect formal rank.
        return max(rank([[a+z*b for a,b in zip(row[:s],row[s:])] for row in rows])
                   for z in range(s+1))

    for s in range(3,12):
        first=[0]*(2*s);first[1]=1;first[s]=-1;rows=[first]
        for i in range(2,s):
            a=[0]*(2*s);a[i]=1
            b=[0]*(2*s);b[s+i]=1
            rows.extend((a,b))
        need(rank(rows)==2*s-3 and projection(rows,s)==s-1,"short normal dimension")
        need(rank([row[:s] for row in rows]+[row[s:] for row in rows])==s,
             "deficient projection despite full component carrier")
        need(all(row[0]==row[s+1]==row[1]+row[s]==0 for row in rows),
             "independent linear normal coefficients")
        short=rows[:-1];extra=[0]*(2*s);extra[0]=1
        need(rank(short)==2*s-4 and projection(short,s)==s-1,"lower-rank deficient family")
        need(rank(short+[extra])==2*s-3 and projection(short+[extra],s)==s,
             "one original-field augmentation fills the generic projection")
    for raw in range(1,1001):
        need(Q(min(raw,2)+(raw==1),2)==1,"all positive raw values")
    return 9


def main():
    raw=(NODE/"certificate.json").read_bytes()
    need(len(raw)==17267 and sha(raw)==PIN,"frozen proposed certificate")
    data=json.loads(raw)
    for relative in PINS:read(relative)
    audit=module("rate_half_mca_all_coordinate_rank_nineteen_tail_payment/verify_audit.py",
                 "fc557d535bfd573b9affbefcc39211b55daf0e0483e441fc9481e6286f55961a","p1_old_UG")
    legal=module("rate_half_mca_coupled_pair_rank_frontier/verify_audit.py",
                 "59b9ad4918ced72f90938f3ac5817f5c504aa7a1daa11818d3fcf560dff01d2f","p1_old_LIST")
    mass=module("rate_half_mca_min_envelope_raw_mass/verify_audit.py",
                "4302416fd3e6f357ae05d2074ebd498016be905956980c7a60843e046dc9136b","p1_old_mass")
    prior=module("rate_half_mca_raw_one_projection_rank_nine_source_tail_payment/verify_audit.py",
                 "906b194ea0de9fc5449909ae6956a7e81effeb9e05322297f183920c806e0b70","p1_projection_census")
    parent=json.loads(read("rate_half_mca_regular_rational_plane_terminal_bounds/certificates/20965.json"))
    gates=json.loads(read("rate_half_mca_coupled_pair_rank_frontier/gate_certificate.json"))
    rows=[json.loads(line) for line in
          read("rate_half_mca_all_coordinate_rank_nineteen_tail_payment/certificates/20965.jsonl").splitlines()]
    prices,generic=weighted(rows,parent,gates,audit,legal)
    # Metadata and the old final mixed-raw composition are deliberately not transplanted.
    for j0 in (9965,20618):
        extended=copy.deepcopy(parent);extended["J"][0]=j0
        altered,value=weighted(rows,extended,gates,audit,legal)
        need(altered==prices and value==generic,"G induction is independent of profile lower J")

    previous=json.loads(read("rate_half_mca_raw_one_projection_rank_nine_source_tail_payment/certificate.json"))
    folder="rate_half_mca_regular_rational_plane_terminal_bounds/certificates/"
    index=json.loads(read(folder+"index.json",
                         "432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"))
    profiles=[(ref,json.loads(read(folder+ref["path"],ref["sha256"]))) for ref in index["profiles"]]
    prior.header(previous);prior.source_gates(previous,legal,profiles)
    projection=prior.raw_one(previous,legal)
    cases=case_prices(projection,json.loads(read("rate_half_mca_raw_two_quadratic_normal_payment/certificate.json")))
    branches,_=mass.tree(9)
    validate(data,prices,generic,cases,mass,branches)
    mutations=repriced=0
    for key in SCOPE:
        bad=copy.deepcopy(data);bad["scope"][key]=None
        reject(lambda:header(bad));mutations+=1
    for mode in ("missing-case","case-cost","missing-band","degree-gap","G-price",
                 "raw-cap","missing-endpoint","mass","supplier","count"):
        bad=copy.deepcopy(data)
        if mode=="missing-case":bad["case_raw_one_bounds"].pop("quadratic_normal")
        elif mode=="case-cost":bad["case_raw_one_bounds"]["proper_carrier"]-=1
        elif mode=="missing-band":bad["degree_bands"].pop()
        elif mode=="degree-gap":bad["degree_bands"][0]["kappa"][0]=1
        elif mode=="G-price":bad["degree_bands"][0]["G11"]=["1","1"]
        elif mode=="raw-cap":bad["generic_rational"]=["1","1"]
        elif mode=="missing-endpoint":bad["endpoints"].pop()
        elif mode=="mass":bad["endpoints"][-1]["mass_floor"]-=1
        elif mode=="supplier":bad["supplier_pins"]={}
        else:bad["t1_LIST_steps"]-=1
        reject(lambda:validate(bad,prices,generic,cases,mass,branches));mutations+=1
    for mode in ("rank1","both"):
        bad=copy.deepcopy(data)
        altered,value=weighted(rows,parent,gates,audit,legal,omission=mode)
        need(altered!=prices,"omitted branch changes the certified recurrence")
        bad["degree_bands"]=altered;bad["generic_rational"]=encode(value)
        bad["case_raw_one_bounds"]["generic_enclosure"]=int(value);reprice(bad)
        reject(lambda:validate(bad,prices,generic,cases,mass,branches));mutations+=1;repriced+=1
    unchanged,value=weighted(rows,parent,gates,audit,legal,omission="nonregular")
    need(unchanged==prices and value==generic,
         "nonregular-only omission is dominated in this frozen root ledger")
    # Such domination does not justify deleting this child type from the theorem.
    need(Q((R+4)+3,D+3)>Q(R+4,D+3),"unrestricted-child excess can matter")
    for mode in ("divide-three","near","minimum","moving","optimistic-branch"):
        bad=copy.deepcopy(data)
        if mode=="moving":bad["case_raw_one_bounds"]["quadratic_normal"]-=21490
        if mode=="optimistic-branch":
            factor=12*prod(D-9+i for i in range(1,11))
            for row in bad["endpoints"]:
                value=Q(prod(R+row["J"]-i for i in range(12)),factor)/max(mass.value(p,row["J"]) for p in branches)
                row["mass_ratio"]=encode(value);row["mass_floor"]=int(value)
        reprice(bad,divisor=3 if mode=="divide-three" else 2,
                near=0 if mode=="near" else 134944,maximum=mode!="minimum")
        reject(lambda:validate(bad,prices,generic,cases,mass,branches));mutations+=1;repriced+=1
    controls=linear_controls()
    print("PASS independent43 raw-one bands;11051 LIST steps;3268 U/G identities;109 height rows")
    print("PASS lower-J independence at9965/20618; four exhaustive algebraic case prices")
    print("PASS previous P1 census709 LIST steps and13 original whole-source gates; unshifted256-branch resource")
    print("PASS",mutations,"semantic mutations;",repriced,"fully repriced ledgers;",
          controls,"linear-algebra controls;1000 raw identities")
    print("RAW ONE",int(generic),"SOURCE",data["endpoints"][-1]["whole"],"RESERVE",data["endpoints"][-1]["reserve"])
    print("P1 rank<=19 pays J20618..21499 with P2 unrestricted; other source classes and both Prizes OPEN")


if __name__=="__main__":
    main()
