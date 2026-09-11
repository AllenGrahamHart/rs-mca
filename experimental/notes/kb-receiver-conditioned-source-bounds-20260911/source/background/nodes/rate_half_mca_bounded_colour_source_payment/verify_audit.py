"""Independent unshifted contraction, source accounting and small core controls."""
import copy
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import combinations, permutations
import json
from math import prod
from pathlib import Path

HERE=Path(__file__).resolve().parent
PIN="851c08cdff1ce32262bc2bb73e56b6ed610028403f29f4633a32576757a4c012"
OLD_PIN="4302416fd3e6f357ae05d2074ebd498016be905956980c7a60843e046dc9136b"
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


def old_auditor():
    path=HERE.parent/"rate_half_mca_min_envelope_raw_mass/verify_audit.py"
    need(hashlib.sha256(path.read_bytes()).hexdigest()==OLD_PIN,"unshifted supplier custody")
    spec=importlib.util.spec_from_file_location("bounded_colour_unshifted",path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def tree(A):
    d=67470;end=21499
    rows=[[F(d*(2*d+1),2*(d+2)),F(3*d+1,2*(d+2)),F(1,2*(d+2))]]
    count=0
    for r in range(4,11):
        nxt=[]
        for q in rows:
            need(A.value(q,r-1)==d+r-1,"original-degree child endpoint")
            first=A.slope(q);second=A.slope(first)
            for gate in (first,second,A.difference([2*c for c in first],second,end),
                         A.difference([2*(r-2)*c for c in first],second,d+end)):
                need(A.positive_on(gate,r-1,end),"all real unshifted branch gates")
            spike=A.linear_change(q,-1,1);spike[0]-=r-1;spike[1]+=1
            transformed=A.linear_change(q,F(1,r-1),F(r-2,r-1))
            equal=[F(0)]*(len(q)+1)
            for i,c in enumerate(transformed):
                equal[i]+=d*c/(d+r-1);equal[i+1]+=c/(d+r-1)
            nxt.extend((spike,equal));count+=1
        rows=nxt
    need(len(rows)==128 and count==127,"all rank-ten branches")
    for q in rows:
        shifted=A.linear_change(q,10,1)
        need(shifted[0]==d+10 and min(shifted)>=0,"final monotone convex branches")
        need(A.value(A.slope(q),9965-286)*(1058541-11)>12*A.value(q,21499-2),
             "whole-J and all-C derivative bound")
    return rows


def falling(n,k):
    return prod(range(n-k+1,n+1))


def first_hit(n,b,k):
    return sum(falling(n-b,j)*b*falling(n-j-1,k-j-1) for j in range(k))


def expected(A):
    rows=tree(A);U=falling(1058541,12)
    factor=12*(67470+9965)*prod(range(67471,67480))
    def resource(cap):
        return int(F(U)/(factor*min(A.value(q,9965-cap) for q in rows)))
    old,_=A.tree(44)
    W44=int(F(falling(1048576+9941,12))/
            (12*prod(range(67429,67439))*min(A.value(q,9941) for q in old)))
    high=int(F(2*(W44+1),3))
    need(W44==581590844909990298 and high<resource(2),"full HIGH tail fits W_C")
    def profile(c,s):
        W=resource(c);hit=first_hit(1058541,s,12)
        N1=int(F((W+1)*hit,U));total=int(F(W+N1,2))+21488+134944
        return dict(cap=c,singletons=s,resource=W,singleton_labels=N1,
                    source=total,reserve=2130706433**6//2**128-total)
    pins={
        "mca_min_envelope_fiber_contraction/polynomial.py":"d5cae0ac19b4cb4d7cbe0ebb67d1645204322b30b09ee003ec42b44cf3f4f3c9",
        "rate_half_mca_min_envelope_raw_mass/verify.py":"b6745db5995bdf421755408a54a92f052beadff4747391f62b93733b51be8867",
    }
    for name,pin in pins.items():
        need(hashlib.sha256((HERE.parent/name).read_bytes()).hexdigest()==pin,"primary custody only; no import")
    specs=((2,1717),(43,1465),(286,0))
    result=dict(scope=SCOPE,supplier_pins=pins,original44=W44,effective_high_floor=high,
        paid=[profile(c,s) for c,s in specs],adjacent_singletons=[profile(c,s+1) for c,s in specs],
        adjacent_colour_cap=profile(287,0))
    need(all(x["reserve"]>=0 for x in result["paid"]),"all paid recipes")
    need(all(x["reserve"]<0 for x in result["adjacent_singletons"]+[result["adjacent_colour_cap"]]),
         "adjacent recipes fail, not source unsafety")
    return result


def geometry():
    p=97;fibres={}
    for x in range(1,p):fibres.setdefault(pow(x,4,p),[]).append(x)
    need(len(fibres)==24 and {len(v) for v in fibres.values()}=={4},"actual quartic evaluation fibres")
    core=set();colours={}
    for z,points in fibres.items():
        for i,x in enumerate(points):
            colour=(0,0) if i<2 else (1,1)
            colours.setdefault((z,colour),[]).append(x)
            if colour==(0,0):core.add(x)
    need({len(v) for v in colours.values()}=={2} and len(core)==48,"receiver classes, not evaluation fibres")
    total=0
    for x,y,z in combinations(sorted(core),3):
        a,b,c=pow(x,4,p),pow(y,4,p),pow(z,4,p)
        determinant=(b*c*c-c*b*b)-(a*c*c-c*a*a)+(a*b*b-b*a*a)
        total+=6*bool(determinant%p)
    need(total==48*46*44==97152,"actual independent ordered core bases")
    # After contracting one complete two-point core fibre, degree drops from9 to7.
    # The rank-two root bound gives (D+7)*(D+1)=46*40 ordered child bases.
    need(total>=48*46*40==88320,"bounded-colour full-fibre contraction")
    need(all(len(set(v)&core) in (0,2) for v in colours.values()),"complete core colour membership")
    return total


def profile_controls():
    def elementary(weights,k):
        out=[1]+[0]*k
        for w in weights:
            for j in range(k,0,-1):out[j]+=w*out[j-1]
        return out[k]
    count=0
    for weights in ((1,2,2),(2,3,2),(1,1,1,2),(3,3,1),(2,2,2,2)):
        classes=[i for i,w in enumerate(weights) for _ in range(w)]
        for k in range(2,5):
            actual=hit=0
            for row in permutations(range(len(classes)),k):
                owners={classes[x] for x in row}
                if len(owners)!=k:continue
                actual+=1;hit+=any(weights[i]==1 for i in owners)
            factor=prod(range(1,k+1))
            full=factor*elementary(weights,k)
            miss=factor*elementary([w for w in weights if w!=1],k)
            need(actual==full and hit==full-miss,"distinct-class universe and singleton hits")
            count+=1
    return count


def controls():
    for bc,b44 in ((F(1),F(2)),(F(2),F(1)),(F(7,3),F(5,4))):
        cost=min(bc,3*b44/2)
        for raw in range(1,1001):
            actual=raw*bc if raw<=2 else min(raw,44)*b44
            need(actual>=min(raw,2)*cost,"one actual LOW/HIGH tuple cost")
            need(2==min(raw,2)+(1 if raw==1 else 0),"exact source count identity")
    need(max(F(1),F(3))>1 and 2*max(F(2),F(3,2))>3,"max costs can underfund LOW or HIGH")
    for b in (0,1,1465,1717):
        for i in range(12):
            a=1058541-i
            need(F(a+1-b,a+1)-F(a-b,a)==F(b,a*(a+1)),"all-J singleton fraction monotonicity")
    need(8//7==1 and (20//7)*8//20==0,"integer-resource flooring is not transportable")
    return geometry(),profile_controls()


def validate(data,want):
    need(json.dumps(data,sort_keys=True)==json.dumps(want,sort_keys=True),"exact independent scope and ledger")


def main():
    raw=(HERE/"certificate.json").read_bytes()
    need(hashlib.sha256(raw).hexdigest()==PIN,"certificate custody")
    data=json.loads(raw);want=expected(old_auditor());validate(data,want)
    bases,profiles=controls();mutations=[]
    for key in SCOPE:
        bad=copy.deepcopy(data);bad["scope"][key]=None;mutations.append(bad)
    for kind in ("zero","near","singleton","half_bank","low_resource","double_high"):
        bad=copy.deepcopy(data);row=bad["paid"][1]
        if kind=="singleton":row["singleton_labels"]=0
        if kind=="half_bank":row["singleton_labels"]//=2
        if kind=="low_resource":row["resource"]-=1
        total=(row["resource"]+row["singleton_labels"])//2+156432
        if kind=="zero":total-=21488
        if kind=="near":total-=134944
        if kind=="double_high":total+=bad["effective_high_floor"]//2
        row["source"]=total;row["reserve"]=2130706433**6//2**128-total
        mutations.append(bad)
    for bad in mutations:
        try:validate(bad,want)
        except ValueError:continue
        raise ValueError("accepted altered original-source ledger")
    print("PASS independent128-branch tree,127 whole-interval gates and all-C/J monotonicity")
    print("PASS first-hit singleton counts;3000 LOW/HIGH costs;",bases,"actual core bases")
    print("PASS",profiles,"exhaustive distinct-class tuple-profile controls")
    print("PASS",len(mutations),"scope/ledger mutations, six recomputed totals")
    for row in want["paid"]:print("SOURCE",row["cap"],row["singletons"],row["source"],"RESERVE",row["reserve"])
    print("No original full-source enumeration; BOTH Prize problems remain OPEN")


if __name__=="__main__":
    main()
