"""Independent first-hit tuple count and unshifted resource audit."""
import copy
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import permutations
import json
from math import prod
from pathlib import Path

HERE=Path(__file__).resolve().parent
PIN="5f36b1890c14b70ac7d3c80fc8df2035b284404f85d757a2cb9ef36115049382"
AUDIT_PIN="4302416fd3e6f357ae05d2074ebd498016be905956980c7a60843e046dc9136b"
SCOPE=dict(schema="small-colour-original-source-v1",field="2130706433^6",
    n=2097152,k=1048576,agreement=1116048,target_epsilon="2^-128",
    original_error_rank_before_fixed_frame_reselection=12,J=[9965,21499],
    shared_dimension=11,canonical_raw_maximized=True,fixed_carrier_receiver_and_labels=True,
    original_rank_retested_after_reselection=False,small_colour_size_max=43,
    small_colour_coordinate_mass_max=53067,nonzero_evaluation_colours_only=True,
    zero_evaluation_label_allowance=21488,zero_charge_per_pair=False,
    tuple_arity=12,tuple_universe="all ordered distinct tuples hitting B43",
    low_beta="original beta44 from m-44 complete-core points and every actual defect",
    resource_cutoff=44,resource_copies=1,P1_rank_restriction=False,P2_rank_restriction=False,
    original_near=134944,whole_source_bound=274978354983575055,reserve=2373127820032,
    next_bank_unsafe_claim=False,all_original_rank12_sources_closed=False,
    active_v4_atom=False,ordinary_LIST_closed=False,adjacent_safe_row_closed=False,prize_closed=False)


def need(ok,why):
    if not ok:raise ValueError(why)


def falling(n,k):
    return prod(range(n-k+1,n+1))


def first_hit(n,b,k):
    return sum(falling(n-b,j)*b*falling(n-j-1,k-j-1) for j in range(k))


def endpoint(sigma,W):
    n=1058541;universe=falling(n,12);hit=first_hit(n,sigma,12)
    need(hit==universe-falling(n-sigma,12),"independent first-hit decomposition")
    for i in range(12):
        a=n-i;b=1070075-i
        need(0<a-sigma and F(a-sigma,a)<=F(b-sigma,b),"whole-J bank-fraction monotonicity")
        need(F(a+1-sigma,a+1)-F(a-sigma,a)==F(sigma,a*(a+1)),"exact factor monotonicity")
    low=int(F((W+1)*hit,universe))
    whole=int(F(W+43*low,44))+156432
    return dict(sigma=sigma,universe=str(universe),miss=str(universe-hit),hit=str(hit),
                low_raw_bound=low,whole=whole,reserve=2130706433**6//2**128-whole)


def expected():
    path=HERE.parent/"rate_half_mca_min_envelope_raw_mass/verify_audit.py"
    need(hashlib.sha256(path.read_bytes()).hexdigest()==AUDIT_PIN,"unshifted resource pin")
    spec=importlib.util.spec_from_file_location("bank_unshifted_mass",path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    branches,_=module.tree(44)
    factor=12*prod(67472-44+i for i in range(1,11))
    denominator=factor*min(module.value(q,9941) for q in branches)
    mass=int(F(falling(1048576+9941,12))/denominator)
    need(mass==581590844909990298,"original44 resource floor")
    pins={
        "rate_half_mca_min_envelope_raw_mass/verify.py":"b6745db5995bdf421755408a54a92f052beadff4747391f62b93733b51be8867",
        "mca_min_envelope_fiber_contraction/polynomial.py":"d5cae0ac19b4cb4d7cbe0ebb67d1645204322b30b09ee003ec42b44cf3f4f3c9",
    }
    for name,pin in pins.items():
        need(hashlib.sha256((HERE.parent/name).read_bytes()).hexdigest()==pin,"custody only; no primary import")
    result=dict(scope=SCOPE,supplier_pins=pins,resource=mass,
                paid=endpoint(53067,mass),adjacent=endpoint(53068,mass))
    need(result["paid"]["reserve"]>=0>result["adjacent"]["reserve"],"named recipe boundary")
    return result


def validate(data,want):
    need(json.dumps(data,sort_keys=True)==json.dumps(want,sort_keys=True),"independent source scope and arithmetic")


def controls():
    tests=0
    for n in range(2,8):
        for k in range(1,min(n,4)+1):
            for b in range(n+1):
                actual=sum(any(x<b for x in row) for row in permutations(range(n),k))
                need(actual==first_hit(n,b,k)==falling(n,k)-falling(n-b,k),"all tiny tuple banks")
                tests+=1
    # A floor of the full rational resource cannot be multiplied by a bank fraction.
    U,beta,hit=20,7,8
    W=U//beta
    need(hit//beta==1 and W*hit//U==0 and (W+1)*hit//U==1,"retain the rational-resource +1")
    for raw in range(1,1001):
        need(F(min(raw,44),44)+(F(43*raw,44) if raw<=43 else 0)>=1,"all HIGH and LOW costs")
    return tests


def main():
    raw=(HERE/"certificate.json").read_bytes();need(hashlib.sha256(raw).hexdigest()==PIN,"certificate custody")
    data=json.loads(raw);want=expected();validate(data,want);count=controls()
    mutations=[]
    for key in SCOPE:
        bad=copy.deepcopy(data);bad["scope"][key]=None;mutations.append(bad)
    for kind in ("no_zero","no_near","linear_bank","omitted_high","raw","universe"):
        bad=copy.deepcopy(data);row=bad["paid"];W=bad["resource"]
        if kind=="linear_bank":
            row["hit"]=str(12*row["sigma"]*falling(1058540,11))
            row["low_raw_bound"]=(W+1)*int(row["hit"])//int(row["universe"])
        elif kind=="raw":row["low_raw_bound"]-=1
        elif kind=="universe":
            row["universe"]=str(int(row["universe"])+1)
        total=(W+43*row["low_raw_bound"])//44+156432
        if kind=="no_zero":total-=21488
        if kind=="no_near":total-=134944
        if kind=="omitted_high":total=(43*row["low_raw_bound"])//44+156432
        row["whole"]=total;row["reserve"]=2130706433**6//2**128-total
        mutations.append(bad)
    for bad in mutations:
        try:validate(bad,want)
        except ValueError:continue
        raise ValueError("accepted altered source ledger")
    print("PASS independent first-hit universe; unshifted256-branch resource; full-J monotonicity")
    print("PASS",count,"exhaustive small tuple banks;1000 cost controls; rational-rounding counterexample")
    print("PASS",len(mutations),"scope/ledger mutations, six with recomputed totals")
    print("SOURCE",data["paid"]["whole"],"RESERVE",data["paid"]["reserve"],"Both Prizes remain OPEN")


if __name__=="__main__":
    main()
