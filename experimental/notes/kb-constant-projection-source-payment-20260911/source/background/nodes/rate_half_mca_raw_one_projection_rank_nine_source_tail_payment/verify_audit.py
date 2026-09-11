"""Independent raw-one source census and unshifted polynomial-resource audit."""
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import prod
from pathlib import Path

NODE=Path(__file__).resolve().parent
NODES=NODE.parent
R,D,E,G,BUDGET=1048576,67472,21499,569050,274980728111395087
CERT_PIN="274a1f94ae1c81caabe2c8bc13ba1251756c01273f3e0613792f5259a355f8fc"
PINS={
    "list_padded_johnson_dimension_descent/compiler.py":"bac33f24d1f34760518406185fcc9850d4fc61f5441486f94237e13b99eb8ca8",
    "rate_half_mca_min_envelope_raw_mass/verify.py":"b6745db5995bdf421755408a54a92f052beadff4747391f62b93733b51be8867",
    "mca_min_envelope_fiber_contraction/polynomial.py":"d5cae0ac19b4cb4d7cbe0ebb67d1645204322b30b09ee003ec42b44cf3f4f3c9",
    "rate_half_mca_regular_rational_plane_terminal_bounds/certificates/index.json":"432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba",
}
SCOPE=dict(
    schema="raw-one-projection-source-tail-v1",field="2130706433^6",
    n=2097152,k=1048576,agreement=1116048,target_epsilon="2^-128",
    original_error_rank=12,J=[11925,21499],original_near=134944,
    projected_family="ACTUAL original raw-exactly-one pairs P1",
    projection_affine_dimension_max=9,
    projection_row="one fixed nonzero ORIGINAL-field constant row",
    P2_rank_restriction=False,P2_projection_restriction=False,
    pair_scalar_carrier_dimension=11,anchors=0,raw_cutoff=1,
    original_weights_and_complete_unions=True,global_inside_charge=1,
    constant_gate=569050,heavy_complement_max=913633,box_width=10000,
    projected_dimension=9,on_dimension=11,
    source_identity="floor((original min(raw,9) resource + original raw-one count)/2)+near",
    higher_raw_covered=True,source_alternatives="MAXIMUM",
    boundary_11924="this upper recipe exceeds budget; NOT an unsafe witness",
    whole_source_bound=274976274292770934,reserve=4453818624153,
    all_original_rank12_sources_closed=False,active_v4_atom=False,
    ordinary_LIST_closed=False,adjacent_safe_row_closed=False,prize_closed=False,
)
ROOT_KEYS={"scope","supplier_pins","gate_profiles","base_count","base_trace","bins","rich_weight",
           "raw_one_bound","endpoints","heavy_boxes","LIST_steps"}


def need(ok,why):
    if not ok:raise ValueError(why)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def load(relative,pin,name):
    path=NODES/relative;need(sha(path.read_bytes())==pin,"independent old helper pin")
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def header(data):
    need(set(data)==ROOT_KEYS,"exact certificate schema")
    need(json.dumps(data["scope"],sort_keys=True)==json.dumps(SCOPE,sort_keys=True),"original P1-only source scope")
    need(data["supplier_pins"]==PINS,"proposed source pins")
    need(data["heavy_boxes"]==35 and data["LIST_steps"]==709 and len(data["bins"])==35,
         "complete raw-one census")
    need(2130706433**6//2**128==BUDGET,"original budget")


def source_gates(data,legal,profiles):
    need(len(data["gate_profiles"])==len(profiles)==13,"complete gate profile inventory")
    next_j=9965
    for claimed,(ref,parent) in zip(data["gate_profiles"],profiles):
        need(claimed==dict(path=ref["path"],sha256=ref["sha256"],J=parent["J"]),"source gate identity")
        j0,j1=parent["J"];need(j0==next_j,"contiguous source interval");next_j=j1+1
        gate=parent["heights"][0];g=gate["gate"]
        need(gate["height"]==[0,0] and 567500<g<R-D and g>=G,"rank-independent constant gate")
        on=legal.list_cap(parent["on_trace"],R-567501,D-43,j1,11)
        off=legal.list_cap(gate["off_trace"],g-j1,D-42-j1,j1,11)
        cost=Q(581590844909990298+43*g*on+43*981147*off,44)+134945
        need(-(-cost.numerator//cost.denominator)==gate["price"]<=270000000000000000,
             "whole original source gate price")
    need(next_j==21500,"gate interval endpoint")


def raw_one(data,legal):
    base=legal.list_cap(data["base_trace"],R,D-1,E,9)
    need(data["base_count"]==base,"base projection count")
    end=(R+E)-2*(D+E-1)+E-1
    next_e=G+1;rich=steps=0
    for row in data["bins"]:
        last=min(next_e+9999,end)
        need(set(row)=={"e","on","tail","on_trace","tail_trace","weight"}
             and row["e"]==[next_e,last],"all two-core complement bins")
        on=legal.list_cap(row["on_trace"],R-next_e,D-1,E,11)
        tail=legal.list_cap(row["tail_trace"],R,R-last,E,9)
        need(row["on"]==on and row["tail"]==tail and row["weight"]==last*on*tail,
             "separate on/projection counts and original outside weights")
        rich+=last*on*tail;steps+=20;next_e=last+1
    need(next_e==end+1 and steps+9==709,"complete bin/trace coverage")
    value=1+(R-D+1)*base+rich
    need(data["rich_weight"]==rich and data["raw_one_bound"]==value==31878195092556089,
         "singleton weights plus one global inside label")
    return value


def endpoints(data,omega,mass,branches):
    need(len(data["endpoints"])==2,"two certificate boundary endpoints")
    factor=12*prod(range(D-8,D+2))
    prices=[]
    for row,j in zip(data["endpoints"],(11924,11925)):
        minimum=min(mass.value(q,j) for q in branches)
        ratio=Q(prod(R+j-i for i in range(12)),factor)/minimum
        floor=ratio.numerator//ratio.denominator
        # For raw=1: 1=(1+1)/2; for raw>=2: 1=min(raw,2)/2.
        residual=(floor+omega)//2+2*D
        expected=dict(J=j,mass_ratio=[str(ratio.numerator),str(ratio.denominator)],
                      mass_floor=floor,residual=residual,
                      whole=max(residual,270000000000000000),reserve=BUDGET-residual)
        need(row==expected,"unshifted complete-tree floor and ORIGINAL two-level raw identity")
        prices.append(residual)
    need(prices[0]>BUDGET>=prices[1] and prices[1]==SCOPE["whole_source_bound"],
         "recipe crossing, not source unsafety")
    return prices


def reprice(data,divisor=2,omit_singletons=False,omit_tail=False,omit_inside=False):
    rich=0
    for row in data["bins"]:
        row["weight"]=row["e"][1]*row["on"]*(1 if omit_tail else row["tail"])
        rich+=row["weight"]
    data["rich_weight"]=rich
    data["raw_one_bound"]=(0 if omit_inside else 1)+rich
    if not omit_singletons:data["raw_one_bound"]+=(R-D+1)*data["base_count"]
    for row in data["endpoints"]:
        value=(row["mass_floor"]+data["raw_one_bound"])//divisor+2*D
        row.update(residual=value,whole=max(value,270000000000000000),reserve=BUDGET-value)


def reject(action):
    try:action()
    except (ValueError,KeyError,TypeError,IndexError,ZeroDivisionError):return
    raise ValueError("accepted malformed proof recipe")


def main():
    raw=(NODE/"certificate.json").read_bytes()
    need(len(raw)==56677 and sha(raw)==CERT_PIN,"frozen certificate bytes")
    data=json.loads(raw)
    legal=load("rate_half_mca_coupled_pair_rank_frontier/verify_audit.py",
               "59b9ad4918ced72f90938f3ac5817f5c504aa7a1daa11818d3fcf560dff01d2f","raw_one_legal")
    mass=load("rate_half_mca_min_envelope_raw_mass/verify_audit.py",
              "4302416fd3e6f357ae05d2074ebd498016be905956980c7a60843e046dc9136b","raw_one_unshifted")
    branches,_=mass.tree(9)
    parent=NODES/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
    raw=(parent/"index.json").read_bytes()
    need(sha(raw)==PINS["rate_half_mca_regular_rational_plane_terminal_bounds/certificates/index.json"],"source index")
    profiles=[]
    for ref in json.loads(raw)["profiles"]:
        raw=(parent/ref["path"]).read_bytes();need(sha(raw)==ref["sha256"],"source profile bytes")
        profiles.append((ref,json.loads(raw)))
    def validate(candidate):
        header(candidate);source_gates(candidate,legal,profiles)
        return endpoints(candidate,raw_one(candidate,legal),mass,branches)
    prices=validate(data);mutations=0
    for key in SCOPE:
        bad=copy.deepcopy(data);bad["scope"][key]=None;reject(lambda:header(bad));mutations+=1
    for mode in ("missing-bin","duplicate-bin","bin-gap","bad-on","bad-tail","missing-gate","source-pin","near"):
        bad=copy.deepcopy(data)
        if mode=="missing-bin":bad["bins"].pop()
        elif mode=="duplicate-bin":bad["bins"].append(bad["bins"][0])
        elif mode=="bin-gap":bad["bins"][0]["e"][0]+=1
        elif mode=="bad-on":bad["bins"][0]["on_trace"][-1][-1]-=1
        elif mode=="bad-tail":bad["bins"][0]["tail_trace"][-1][-1]-=1
        elif mode=="missing-gate":bad["gate_profiles"].pop()
        elif mode=="source-pin":bad["gate_profiles"][0]["sha256"]="0"*64
        else:bad["endpoints"][-1]["residual"]-=134944
        reject(lambda:validate(bad));mutations+=1
    for mode in ("singletons","tail","inside","divide-three","wrong-dimension"):
        bad=copy.deepcopy(data)
        if mode=="wrong-dimension":
            for row in bad["bins"]:
                row["on_trace"]=row["on_trace"][:9];row["on"]=row["on_trace"][-1][-1]
        reprice(bad,divisor=3 if mode=="divide-three" else 2,omit_singletons=mode=="singletons",
                omit_tail=mode=="tail",omit_inside=mode=="inside")
        if mode=="inside":
            need(bad["raw_one_bound"]<data["raw_one_bound"]
                 and bad["endpoints"][-1]["residual"]<=data["endpoints"][-1]["residual"],
                 "inside omission changes raw weight; the final floor may absorb one")
        else:
            need(bad["endpoints"][-1]["residual"]<data["endpoints"][-1]["residual"],"mutation reprices full source")
        reject(lambda:validate(bad));mutations+=1
    bad=copy.deepcopy(data);factor=12*prod(range(D-8,D+2))
    for row in bad["endpoints"]:
        ratio=Q(prod(R+row["J"]-i for i in range(12)),factor)/max(mass.value(q,row["J"]) for q in branches)
        row["mass_ratio"]=[str(ratio.numerator),str(ratio.denominator)];row["mass_floor"]=int(ratio)
    reprice(bad);need(bad["endpoints"][-1]["residual"]<prices[-1],"optimistic branch changes price")
    reject(lambda:validate(bad));mutations+=1
    for raw in range(1,1001):
        need(Q(min(raw,2)+(1 if raw==1 else 0),2)==1,"all positive raw cases")
    need(Q(2,3)<1,"raw-two record refutes the free one-third high-raw charge")
    print("PASS independent 35 boxes; 709 LIST steps; all13 source gates; unshifted256-branch resource")
    print("PASS",mutations,"semantic mutations, including six fully repriced ledgers;1000 raw-identity controls")
    print("RECIPE J11924/J11925",prices,"RESERVE",BUDGET-prices[-1])
    print("P1 projection<=9 pays J11925..21499 with no P2 rank/image restriction")
    print("No unsafe J11924 witness, whole-row or Prize closure")


if __name__=="__main__":
    main()
