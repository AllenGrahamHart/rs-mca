"""One-source LOW improvement from sparse heavy receiver colours."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import prod
from pathlib import Path

HERE=Path(__file__).resolve().parent
PARENT_PIN="43794017e927909b4e5c93c74a4d607cfa9ca6ea275b01ca1f82e98e8bb319e1"
R,D,J0,J1=1048576,67470,9965,21499
B=2130706433**6//2**128
SCOPE=dict(schema="sparse-heavy-colour-source-v1",field="2130706433^6",
    original_n=2097152,original_k=1048576,original_agreement=1116048,target_epsilon="2^-128",
    original_error_rank_before_reselection=12,J=[9965,21499],shared_dimension=11,
    fixed_carrier_receiver_labels=True,rank_retested_after_reselection=False,
    light_colour_size_max=43,heavy_units="coordinates in classes larger than43",
    heavy_bound_range=[43,4639],child_rank=10,core_cutoff=2,
    tail_cost="(M-E)*F10(J-43)+E*F10(J-E)",effective_cost="min(beta_E,3*beta44/2)",
    one_tuple_resource=True,all_HIGH_retained=True,canonical_singletons=True,
    zero_labels_global=21488,near_once=134944,P1_P2_rank_guard=False,
    small_sigma43_required=False,universal_tail_bound=False,adjacent_unsafe=False,prize_closed=False)

def need(ok,why):
    if not ok:raise ValueError(why)

def setup():
    path=HERE.parent/"rate_half_mca_bounded_colour_source_payment/verify.py"
    need(hashlib.sha256(path.read_bytes()).hexdigest()==PARENT_PIN,"bounded-colour tree custody")
    spec=importlib.util.spec_from_file_location("heavy_colour_parent",path)
    a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
    P=a.module("heavy_colour_polynomials","mca_min_envelope_fiber_contraction/polynomial.py")
    rows=a.branches(P)
    for q in rows:
        need(P.at(P.derivative(q),0)*(R+J0-11)>12*P.at(q,J1-10),"strong entire-J/E gate")
    factor=prod(D+i for i in range(1,10))
    F=lambda k:factor*min(P.at(q,k-10) for q in rows)
    old=a.module("heavy_colour_44","rate_half_mca_min_envelope_raw_mass/verify.py")
    W44=int(Q(prod(R+9941-i for i in range(12)))/old.beta(old.envelope(44),44,9941))
    return F,W44

def source(F,E,sigma):
    n=R+J0;M=D+J0;U=prod(n-i for i in range(12))
    cost=12*((M-E)*F(J0-43)+E*F(J0-E))
    W=int(Q(U)/cost)
    N1=(W+1)*(U-prod(n-sigma-i for i in range(12)))//U
    whole=(W+N1)//2+156432
    return dict(heavy_coordinates=E,singletons=sigma,resource=W,singleton_labels=N1,
                source=whole,reserve=B-whole)

def build():
    F,W44=setup()
    need(W44==581590844909990298,"original all-HIGH resource")
    base=source(F,43,0);high=2*(W44+1)//3
    need(base["resource"]==541038523546369464 and high<base["resource"],"one effective raw-two cost")
    paid=[source(F,3000,824),source(F,4639,0)]
    adjacent=[source(F,3000,825),source(F,4639,1),source(F,4640,0)]
    need(all(x["reserve"]>=0 for x in paid),"two whole-source classes")
    need(all(x["reserve"]<0 for x in adjacent),"failed adjacent recipes only")
    return dict(scope=SCOPE,parent_pin=PARENT_PIN,original44=W44,effective_high_floor=high,
                base_resource=base["resource"],paid=paid,adjacent=adjacent)

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--write",action="store_true");args=p.parse_args()
    data=build();raw=(json.dumps(data,indent=2)+"\n").encode();path=HERE/"certificate.json"
    if args.write:
        need(not path.exists(),"refuse frozen overwrite");path.write_bytes(raw)
    else:need(path.read_bytes()==raw,"exact reconstruction")
    print("PASS sparse heavy-coordinate mass; entire-J/E branch gate; one original LOW/HIGH resource")
    for row in data["paid"]:print("PAID",row)
    print("SHA256",hashlib.sha256(raw).hexdigest(),"BYTES",len(raw))
    print("No universal profile payment, unsafe adjacent source or Prize closure")

if __name__=="__main__":
    main()
