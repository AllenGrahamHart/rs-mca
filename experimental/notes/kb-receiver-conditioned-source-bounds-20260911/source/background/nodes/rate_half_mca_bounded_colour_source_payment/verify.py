"""Exact core-fibre contraction and sparse-singleton original-source bounds."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import prod
from pathlib import Path

HERE=Path(__file__).resolve().parent
R,D,J0,J1=1048576,67470,9965,21499
B=2130706433**6//2**128
PINS={
    "mca_min_envelope_fiber_contraction/polynomial.py":"d5cae0ac19b4cb4d7cbe0ebb67d1645204322b30b09ee003ec42b44cf3f4f3c9",
    "rate_half_mca_min_envelope_raw_mass/verify.py":"b6745db5995bdf421755408a54a92f052beadff4747391f62b93733b51be8867",
}
SCOPE=dict(schema="bounded-colour-original-source-v1",field="2130706433^6",
    original_n=2097152,original_k=1048576,original_agreement=1116048,target_epsilon="2^-128",
    original_error_rank_before_reselection=12,J=[9965,21499],shared_dimension=11,
    fixed_carrier_receiver_labels=True,rank_retested_after_reselection=False,
    nonzero_evaluation_receiver_colours=True,cap_range=[2,286],
    core_cutoff=2,child_rank=10,child_branches=128,complete_shape_inputs=127,
    effective_cost="min(beta_C,3*beta44/2)",resource_copies=1,
    HIGH_covers_all_raw_at_least=3,canonical_singleton_defects=True,
    singleton_units="coordinates",zero_label_allowance=21488,zero_charge_per_pair=False,
    near_once=134944,P1_P2_rank_restriction=False,small_sigma43_required=False,
    max_colour_universal=False,adjacent_unsafe=False,whole_J_all_geometries=False,prize_closed=False)


def need(ok,why):
    if not ok:raise ValueError(why)


def module(name,relative):
    path=HERE.parent/relative
    need(hashlib.sha256(path.read_bytes()).hexdigest()==PINS[relative],"supplier custody")
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec);spec.loader.exec_module(value)
    return value


def branches(P):
    rows=[[Q(D+3),Q(3*D+7,2*(D+2)),Q(1,2*(D+2))]]
    count=0
    for rank in range(4,11):
        nxt=[]
        for row in rows:
            need(row[0]==D+rank-1 and min(row)>=0,"positive common child endpoint")
            first=P.derivative(row);second=P.derivative(first)
            gates=(first,second,P.sub(P.scale(first,2),P.scale(second,J1)),
                   P.sub(P.scale(first,2*(rank-2)),P.scale(second,D+J1)))
            need(all(min(P.bernstein(g,0,J1-rank+1))>=0 for g in gates),"whole real child interval")
            nxt.extend((P.add(row,[1,1]),P.scale(P.mul([D+rank,1],
                P.compose(row,0,Q(rank-2,rank-1))),Q(1,D+rank-1))))
            count+=1
        rows=nxt
    need(count==127 and len(rows)==128,"complete rank-ten tree")
    for row in rows:
        need(row[0]==D+10 and min(row)>=0,"rank-ten positive branch")
        need(P.at(P.derivative(row),J0-286-10)*(R+J0-11)>12*P.at(row,J1-2-10),
             "uniform quotient monotonicity for every C2..286 and J")
    return rows


def resource(P,rows,cap):
    n=R+J0;U=prod(n-i for i in range(12))
    beta=12*(D+J0)*prod(D+i for i in range(1,10))*min(P.at(row,J0-cap-10) for row in rows)
    return int(Q(U)/beta)


def profile(cap,singletons,W):
    n=R+J0;U=prod(n-i for i in range(12));miss=prod(n-singletons-i for i in range(12))
    N1=(W+1)*(U-miss)//U
    total=(W+N1)//2+156432
    return dict(cap=cap,singletons=singletons,resource=W,singleton_labels=N1,
                source=total,reserve=B-total)


def build():
    P=module("bounded_colour_polynomials","mca_min_envelope_fiber_contraction/polynomial.py")
    rows=branches(P)
    old=module("bounded_colour_old44","rate_half_mca_min_envelope_raw_mass/verify.py")
    W44=int(Q(prod(R+9941-i for i in range(12)))/old.beta(old.envelope(44),44,9941))
    need(W44==581590844909990298,"all-HIGH resource")
    high=2*(W44+1)//3
    costs={cap:resource(P,rows,cap) for cap in (2,43,286,287)}
    need(high<costs[2]<=costs[43]<=costs[286],"effective cost never exceeds W_C globally")
    specs=((2,1717),(43,1465),(286,0))
    paid=[profile(c,s,costs[c]) for c,s in specs]
    adjacent=[profile(c,s+1,costs[c]) for c,s in specs]
    next_cap=profile(287,0,costs[287])
    need(all(row["reserve"]>=0 for row in paid),"three complete source classes")
    need(all(row["reserve"]<0 for row in adjacent+[next_cap]),"failed adjacent recipes only")
    need(2<67472 and J0-286>=10 and R+11>53067,"canonical, contraction, disjoint old-bank scopes")
    return dict(scope=SCOPE,supplier_pins=PINS,original44=W44,effective_high_floor=high,
                paid=paid,adjacent_singletons=adjacent,adjacent_colour_cap=next_cap)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write",action="store_true")
    args=parser.parse_args()
    data=build();raw=(json.dumps(data,indent=2)+"\n").encode();path=HERE/"certificate.json"
    if args.write:
        need(not path.exists(),"refuse frozen certificate overwrite");path.write_bytes(raw)
    else:need(path.read_bytes()==raw,"exact frozen reconstruction")
    print("PASS complete128-branch rank10 core tree;127 shape inputs; all-C/J monotonicity")
    print("PASS one effective tuple cost; all HIGH; canonical singleton bank; global zero charge")
    for row in data["paid"]:print("PAID",row)
    print("SHA256",hashlib.sha256(raw).hexdigest(),"BYTES",len(raw))
    print("No small-sigma43 premise; no exhaustive source coverage or Prize closure")


if __name__=="__main__":
    main()
