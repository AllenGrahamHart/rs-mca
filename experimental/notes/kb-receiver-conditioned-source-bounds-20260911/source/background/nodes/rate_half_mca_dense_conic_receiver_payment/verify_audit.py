"""Independent on/off conic ledger, source identity and degree-one lift controls."""
import copy
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from math import prod
from pathlib import Path

HERE=Path(__file__).resolve().parent
PIN="47fa0cf46238c8647c89a7980dd53f7266e51dfa948124b9aa726c377300c834"
RESOURCE_PIN="4302416fd3e6f357ae05d2074ebd498016be905956980c7a60843e046dc9136b"
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


def enc(x):return [str(x.numerator),str(x.denominator)]


def reprice(rows,mass):
    gain=sum((F(*map(int,row["gain"])) for row in rows),F(0))
    total=F(mass,44)+gain
    return dict(gain=enc(gain),total_before_near=enc(total),whole=int(total)+134944,
                reserve=2130706433**6//2**128-int(total)-134944)


def independent_ledger(e,mass):
    rows=[]
    for t in range(1,44):
        q=F(1048577,67473-t)
        moving=(q*q*q*q*q)*131072
        need(moving>=32*q**6 and moving>=2097152*q,"all nonsingular conic types priced")
        numerator=e-21498;denominator=24475-t
        power=F(1)
        for _ in range(11):power*=F(numerator,denominator)
        shared=prod(F(e-21499+i,67472-t-42998+i) for i in range(1,12))
        need(shared<=power and denominator>1,"shared-carrier dimension descent")
        # This positive exact numerator proves monotonicity for every J, not samples.
        need(2*e-67472+t-1>0,"whole-J ratio monotonicity")
        need(F(e-9965+1,67472-t-2*9965+1)<=F(numerator,denominator),"endpoint control")
        on,off=int(moving),int(power)
        term=F((981104+t)*(on+off),t*(t+1))
        rows.append(dict(t=t,on_conic_pairs=on,off_conic_pairs=off,
                         outside_ratio=[numerator,denominator],pair_raw_cap=981104+t,gain=enc(term)))
    return dict(e=e,rows=rows,**reprice(rows,mass))


def expected():
    path=HERE.parent/"rate_half_mca_min_envelope_raw_mass/verify_audit.py"
    need(hashlib.sha256(path.read_bytes()).hexdigest()==RESOURCE_PIN,"independent resource custody")
    spec=importlib.util.spec_from_file_location("conic_unshifted_resource",path)
    resource=importlib.util.module_from_spec(spec);spec.loader.exec_module(resource)
    branches,_=resource.tree(44)
    beta=12*prod(67472-44+i for i in range(1,11))*min(resource.value(q,9941) for q in branches)
    mass=int(F(prod(1048576+9941-i for i in range(12)))/beta)
    need(mass==581590844909990298,"original all-raw44 floor")
    pins={
        "rate_half_mca_min_envelope_raw_mass/verify.py":"b6745db5995bdf421755408a54a92f052beadff4747391f62b93733b51be8867",
        "mca_min_envelope_fiber_contraction/polynomial.py":"d5cae0ac19b4cb4d7cbe0ebb67d1645204322b30b09ee003ec42b44cf3f4f3c9",
    }
    for name,pin in pins.items():
        need(hashlib.sha256((HERE.parent/name).read_bytes()).hexdigest()==pin,"custody only, no primary import")
    result=dict(scope=SCOPE,supplier_pins=pins,resource=mass,
                paid=independent_ledger(276035,mass),adjacent=independent_ledger(276036,mass))
    need(result["paid"]["reserve"]>=0>result["adjacent"]["reserve"],"recipe crossing, not an unsafe source")
    return result


def norm(a):
    a=[c%101 for c in a]
    while len(a)>1 and not a[-1]:a.pop()
    return a


def add(a,b):return norm([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def neg(a):return norm([-c for c in a])
def sub(a,b):return add(a,neg(b))


def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return norm(c)


def scale(a,c):return norm([c*x for x in a])


def geometry():
    p0=([1],[0,1]);p1=([0,1],[1,1])
    determinant=sub(mul(p0[0],p1[1]),mul(p1[0],p0[1]))
    factor=[1,0,1];base=([3,2,0,1],[4,0,1])
    last=mul(factor,determinant)
    controls=0
    for kind in range(3):
        for t in range(1,6):
            if kind==0:a,b=t*t%101,t
            elif kind==1:a,b=t,pow(t,-1,101)
            else:
                denominator=pow(1+t*t,-1,101);a=(1-t*t)*denominator%101;b=2*t*denominator%101
            f=[add(base[i],mul(factor,add(scale(p0[i],a),scale(p1[i],b)))) for i in range(2)]
            v=[sub(f[i],base[i]) for i in range(2)]
            first=sub(mul(p1[1],v[0]),mul(p1[0],v[1]))
            second=sub(mul(p0[0],v[1]),mul(p0[1],v[0]))
            need(first==scale(last,a) and second==scale(last,b),"adjugate lift without division at roots")
            if kind==0:q=sub(mul(first,last),mul(second,second))
            elif kind==1:q=sub(mul(first,second),mul(last,last))
            else:q=sub(add(mul(first,first),mul(second,second)),mul(last,last))
            need(q==[0] and max(map(len,(first,second,last)))<=6,"lifted conic identity and degree")
            controls+=1
    roots=[x for x in range(101) if sum(c*pow(x,i,101) for i,c in enumerate(last))%101==0]
    need(roots and all(sum(c*pow(x,i,101) for i,c in enumerate(mul(last,last)))%101==0 for x in roots),"content/determinant roots retained")
    return controls,len(roots)


def validate(data,want):
    need(json.dumps(data,sort_keys=True)==json.dumps(want,sort_keys=True),"independent source ledger and scope")


def main():
    raw=(HERE/"certificate.json").read_bytes();need(hashlib.sha256(raw).hexdigest()==PIN,"certificate pin")
    data=json.loads(raw);want=expected();validate(data,want)
    for tau in range(1,1001):
        identity=F(min(tau,44),44)+sum((F(tau,t*(t+1)) for t in range(tau,44)),F(0))
        need(identity==1,"all original raw cases")
    controls,roots=geometry()
    mutations=[]
    for key in SCOPE:
        bad=copy.deepcopy(data);bad["scope"][key]=None;mutations.append(bad)
    for kind in ("on","off","exponent","raw","high","near","omit"):
        bad=copy.deepcopy(data);rows=bad["paid"]["rows"]
        if kind=="omit":rows.pop()
        else:
            for row in rows:
                t=row["t"]
                if kind=="on":row["on_conic_pairs"]=0
                if kind=="off":row["off_conic_pairs"]=0
                if kind=="exponent":
                    a,b=row["outside_ratio"];row["off_conic_pairs"]=a**10//b**10
                if kind=="raw":row["pair_raw_cap"]-=t
                row["gain"]=enc(F(row["pair_raw_cap"]*(row["on_conic_pairs"]+row["off_conic_pairs"]),t*(t+1)))
        bad["paid"].update(reprice(rows,0 if kind=="high" else bad["resource"]))
        if kind=="near":bad["paid"]["whole"]-=134944;bad["paid"]["reserve"]+=134944
        mutations.append(bad)
    for bad in mutations:
        try:validate(bad,want)
        except ValueError:continue
        raise ValueError("accepted changed source ledger")
    print("PASS independent43 on/off rows at both e endpoints; shared11 (not pair22); all conic types")
    print("PASS unshifted256-branch original44 resource;1000 raw identities;",controls,"polynomial lifts;",roots,"retained roots")
    print("PASS",len(mutations),"mutations, including seven recomputed bad source ledgers")
    print("SOURCE",data["paid"]["whole"],"RESERVE",data["paid"]["reserve"],"other source geometries and both Prizes OPEN")


if __name__=="__main__":
    main()
