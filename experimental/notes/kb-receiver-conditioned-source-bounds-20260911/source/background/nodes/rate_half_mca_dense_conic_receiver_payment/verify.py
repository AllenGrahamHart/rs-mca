"""Exact original-source conic/exception payment; no large source enumeration."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import prod
from pathlib import Path

HERE=Path(__file__).resolve().parent
NODES=HERE.parent
R,D,J0,J1,T,E=1048576,67472,9965,21499,43,276035
B=2130706433**6//2**128
PINS={
    "rate_half_mca_min_envelope_raw_mass/verify.py":
        "b6745db5995bdf421755408a54a92f052beadff4747391f62b93733b51be8867",
    "mca_min_envelope_fiber_contraction/polynomial.py":
        "d5cae0ac19b4cb4d7cbe0ebb67d1645204322b30b09ee003ec42b44cf3f4f3c9",
}
SCOPE=dict(schema="dense-conic-original-source-v1",field="2130706433^6",
    n=2097152,k=1048576,agreement=1116048,target_epsilon="2^-128",
    original_error_rank=12,J=[9965,21499],curve="nonsingular projective conic over F(X)",
    curve_coefficients="polynomial in X, all roots retained",weighted_degree_max="2*J",
    receiver_exceptions_max=276035,original_raw_cutoff=43,resource_cutoff=44,
    on_moving_dimension=5,on_moving_degree=131072,off_shared_dimension=11,
    on_pair_hull_rank_required=False,P1_rank_restriction=False,P2_rank_restriction=False,
    same_original_owners=True,raw_reselection=False,resource_reapplied_to_exception_domain=False,
    original_near=134944,whole_source_bound=274980278712737789,reserve=449398657298,
    next_exception_unsafe_claim=False,all_original_rank12_sources_closed=False,
    active_v4_atom=False,ordinary_LIST_closed=False,adjacent_safe_row_closed=False,prize_closed=False)


def need(ok,why):
    if not ok:raise ValueError(why)


def frac(x):return [str(x.numerator),str(x.denominator)]


def resource():
    for name,pin in PINS.items():
        need(hashlib.sha256((NODES/name).read_bytes()).hexdigest()==pin,"inherited source pin")
    spec=importlib.util.spec_from_file_location("conic_shifted_resource",NODES/"rate_half_mca_min_envelope_raw_mass/verify.py")
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return int(Q(prod(R+9941-i for i in range(12)))/module.beta(module.envelope(44),44,9941))


def ledger(e,mass):
    rows=[];gain=Q()
    for t in range(1,T+1):
        q=Q(R+1,D-t+1)
        need(2<=q<=4096,"moving price dominates the other two conic types")
        on=int(2**17*q**5)
        numerator=e-J1+1;denominator=D-t-2*J1+1
        need(denominator>0 and 2*e-D+t-1>0,"entire-J outside quotient monotonicity")
        off=numerator**11//denominator**11
        term=Q((R-D+t)*(on+off),t*(t+1));gain+=term
        rows.append(dict(t=t,on_conic_pairs=on,off_conic_pairs=off,
                         outside_ratio=[numerator,denominator],pair_raw_cap=R-D+t,
                         gain=frac(term)))
    total=Q(mass,44)+gain
    return dict(e=e,rows=rows,gain=frac(gain),total_before_near=frac(total),
                whole=int(total)+2*D,reserve=B-int(total)-2*D)


def build():
    mass=resource();need(mass==581590844909990298,"original all-raw resource")
    current=ledger(E,mass);adjacent=ledger(E+1,mass)
    need(current["whole"]==SCOPE["whole_source_bound"] and current["reserve"]==SCOPE["reserve"],"source payment")
    need(current["whole"]<=B<adjacent["whole"],"exact recipe boundary, not unsafe source")
    return dict(scope=SCOPE,supplier_pins=PINS,resource=mass,paid=current,adjacent=adjacent)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--write",action="store_true")
    args=parser.parse_args();data=build();raw=(json.dumps(data,indent=2)+"\n").encode()
    target=HERE/"certificate.json"
    if args.write:need(not target.exists(),"refuse overwrite");target.write_bytes(raw)
    else:need(target.read_bytes()==raw,"exact certificate reconstruction")
    print("PASS43 conic/exception raw-weight rows, one original44 resource and one near")
    print("EXCEPTIONS",data["paid"]["e"],"SOURCE",data["paid"]["whole"],"RESERVE",data["paid"]["reserve"])
    print("NEXT RECIPE",data["adjacent"]["whole"],"not an unsafe source")
    print("SHA256",hashlib.sha256(raw).hexdigest(),"BYTES",len(raw))
    print("A complete geometric source class is paid; general rank12 and both Prizes remain OPEN")


if __name__=="__main__":
    main()
