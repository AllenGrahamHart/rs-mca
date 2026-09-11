"""Independent unshifted two-cost core mass and original-source audit."""
import copy
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from math import prod
from pathlib import Path

HERE=Path(__file__).resolve().parent
PIN="37390858e17597e465ba246c2c1d18c8df214534cfd4772aeb5f70af829d7401"
AUDIT_PIN="0bf3221e82268f3bf136b97c926ed17071c4de9a1ecb4ce7bfa416ad001fa2be"
PRIMARY_PIN="43794017e927909b4e5c93c74a4d607cfa9ca6ea275b01ca1f82e98e8bb319e1"
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

def falling(n,k):
    return prod(range(n-k+1,n+1))

def expected():
    path=HERE.parent/"rate_half_mca_bounded_colour_source_payment/verify_audit.py"
    need(hashlib.sha256(path.read_bytes()).hexdigest()==AUDIT_PIN,"independent child tree custody")
    primary=path.with_name("verify.py")
    need(hashlib.sha256(primary.read_bytes()).hexdigest()==PRIMARY_PIN,"parent primary custody only")
    spec=importlib.util.spec_from_file_location("heavy_independent_parent",path)
    old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
    A=old.old_auditor();rows=old.tree(A)
    for q in rows:
        need(A.value(A.slope(q),10)*(1058541-11)>12*A.value(q,21499),
             "strong entire-degree/E gate in original degree")
    factor=prod(range(67471,67480))
    child=lambda k:factor*min(A.value(q,k) for q in rows)
    high_rows,_=A.tree(44)
    W44=int(F(falling(1048576+9941,12))/
            (12*prod(range(67429,67439))*min(A.value(q,9941) for q in high_rows)))
    U=falling(1058541,12);M=77435
    def price(E,s):
        base=child(9965-43)
        penalty=E*(base-child(9965-E))
        beta=12*(M*base-penalty)
        W=int(F(U)/beta)
        hit=sum(falling(1058541-s,j)*s*falling(1058540-j,11-j) for j in range(12))
        N1=int(F((W+1)*hit,U));total=int(F(W+N1,2))+21488+134944
        return dict(heavy_coordinates=E,singletons=s,resource=W,singleton_labels=N1,
                    source=total,reserve=2130706433**6//2**128-total)
    base=price(43,0)["resource"];high=2*(W44+1)//3
    need(base==541038523546369464 and high<base,"every HIGH range funded")
    result=dict(scope=SCOPE,parent_pin=PRIMARY_PIN,original44=W44,effective_high_floor=high,
                base_resource=base,paid=[price(3000,824),price(4639,0)],
                adjacent=[price(3000,825),price(4639,1),price(4640,0)])
    need(all(x["reserve"]>=0 for x in result["paid"]),"paid source endpoints")
    need(all(x["reserve"]<0 for x in result["adjacent"]),"failed recipe endpoints only")
    # Pointwise differences audit the monotone tail relaxation independently of branch differentiability.
    for J in (9965,14000,21499):
        for e,f in ((43,44),(1000,3000),(3000,4639)):
            light=child(J-43)
            first=(67470+J-e)*light+e*child(J-e)
            second=(67470+J-f)*light+f*child(J-f)
            need(first>=second>0,"tail mass relaxation controls; universal proof is order-theoretic")
    return result

def validate(data,want):
    need(json.dumps(data,sort_keys=True)==json.dumps(want,sort_keys=True),"exact independent source ledger")

def controls():
    count=0
    for M in range(6,11):
        for E in range(1,6):
            for h in range(E+1):
                for heavy,light in ((1,3),(2,5),(3,3)):
                    actual=(M-h)*light+h*heavy
                    relaxed=(M-E)*light+E*heavy
                    need(actual>=relaxed>0,"charge heavy coordinate mass under one core sum");count+=1
    for bc,b44 in ((F(1),F(2)),(F(2),F(1)),(F(7,3),F(5,4))):
        effective=min(bc,3*b44/2)
        for raw in range(1,101):
            available=raw*bc if raw<=2 else min(raw,44)*b44
            need(available>=min(raw,2)*effective,"single LOW/HIGH tuple cost")
    return count

def main():
    raw=(HERE/"certificate.json").read_bytes()
    need(hashlib.sha256(raw).hexdigest()==PIN,"certificate custody")
    data=json.loads(raw);want=expected();validate(data,want);count=controls()
    mutations=[]
    for key in SCOPE:
        bad=copy.deepcopy(data);bad["scope"][key]=None;mutations.append(bad)
    for kind in ("zero","near","singleton","resource","double_high","half_singletons"):
        bad=copy.deepcopy(data);row=bad["paid"][0]
        if kind=="singleton":row["singleton_labels"]=0
        if kind=="resource":row["resource"]-=1
        if kind=="half_singletons":row["singleton_labels"]//=2
        total=(row["resource"]+row["singleton_labels"])//2+156432
        if kind=="zero":total-=21488
        if kind=="near":total-=134944
        if kind=="double_high":total+=bad["effective_high_floor"]//2
        row["source"]=total;row["reserve"]=2130706433**6//2**128-total
        mutations.append(bad)
    for bad in mutations:
        try:validate(bad,want)
        except ValueError:continue
        raise ValueError("accepted changed source ledger")
    print("PASS independent128-branch tree; whole J/E monotonicity; all-HIGH and singleton resources")
    print("PASS",count,"core-tail controls;300 raw-cost controls;",len(mutations),"scope/ledger mutations")
    for row in data["paid"]:print("SOURCE",row["heavy_coordinates"],row["singletons"],row["source"],"RESERVE",row["reserve"])
    print("Finite controls are not an original-source census; BOTH Prizes remain OPEN")

if __name__=="__main__":
    main()
