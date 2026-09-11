"""Original KoalaBear source payment from the canonical small-colour defect bank."""
import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from math import prod
from pathlib import Path

HERE=Path(__file__).resolve().parent
NODES=HERE.parent
R,D,J0,J1,T,S=1048576,67472,9965,21499,43,53067
B=2130706433**6//2**128
PINS={
    "rate_half_mca_min_envelope_raw_mass/verify.py":"b6745db5995bdf421755408a54a92f052beadff4747391f62b93733b51be8867",
    "mca_min_envelope_fiber_contraction/polynomial.py":"d5cae0ac19b4cb4d7cbe0ebb67d1645204322b30b09ee003ec42b44cf3f4f3c9",
}
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


def resource():
    for name,pin in PINS.items():
        need(hashlib.sha256((NODES/name).read_bytes()).hexdigest()==pin,"resource custody")
    spec=importlib.util.spec_from_file_location("colour_shifted_resource",NODES/"rate_half_mca_min_envelope_raw_mass/verify.py")
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return int(Q(prod(R+9941-i for i in range(12)))/module.beta(module.envelope(44),44,9941))


def endpoint(sigma,W):
    n=R+J0;universe=prod(n-i for i in range(12))
    miss=prod(n-sigma-i for i in range(12));hit=universe-miss
    low=(W+1)*hit//universe
    whole=(W+T*low)//44+2*D+J1-11
    return dict(sigma=sigma,universe=str(universe),miss=str(miss),hit=str(hit),
                low_raw_bound=low,whole=whole,reserve=B-whole)


def build():
    W=resource();need(W==581590844909990298,"one original44 resource")
    need(2*T<D and J0>=11 and R+J0-S>12,"canonical and tuple guards")
    paid=endpoint(S,W);next_row=endpoint(S+1,W)
    need(paid["whole"]==SCOPE["whole_source_bound"] and paid["reserve"]==SCOPE["reserve"],"complete source class")
    need(paid["whole"]<=B<next_row["whole"],"named recipe boundary only")
    return dict(scope=SCOPE,supplier_pins=PINS,resource=W,paid=paid,adjacent=next_row)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--write",action="store_true")
    args=parser.parse_args();data=build();raw=(json.dumps(data,indent=2)+"\n").encode();path=HERE/"certificate.json"
    if args.write:need(not path.exists(),"refuse frozen overwrite");path.write_bytes(raw)
    else:need(path.read_bytes()==raw,"exact reconstruction")
    print("PASS small-colour bank at53067; global zero-label charge; one original44 resource")
    print("SOURCE",data["paid"]["whole"],"RESERVE",data["paid"]["reserve"],"NEXT RECIPE",data["adjacent"]["whole"])
    print("SHA256",hashlib.sha256(raw).hexdigest(),"BYTES",len(raw))
    print("Fixed-frame source class paid; no rank retest, universal bank hypothesis or Prize closure")


if __name__=="__main__":
    main()
