"""Independent source-gate and terminal-envelope audit.

The inherited compiler only proposes two-step traces. The separate inherited
legality checker verifies every proposed inequality before its bound is used.
No module from this new primary proof is imported.
"""
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import prod
from pathlib import Path

NODE=Path(__file__).resolve().parent
NODES=NODE.parent
INDEX_PIN="432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
AUDIT_PIN="59b9ad4918ced72f90938f3ac5817f5c504aa7a1daa11818d3fcf560dff01d2f"
RANGES=[(9965,10964),(10965,11964),(11965,12964),(12965,13364),
        (13365,13964),(13965,14964),(14965,15964),(15965,16964),
        (16965,17964),(17965,18964),(18965,19964),(19965,20964),(20965,21499)]
R,D,S,NEAR,B=1048576,67472,1048577,134944,274980728111395087


def need(ok,why):
    if not ok:
        raise ValueError(why)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rational(data):
    need(type(data) is list and len(data)==2 and all(type(x) is str for x in data),"rational type")
    result=Q(int(data[0]),int(data[1]))
    need(data==[str(result.numerator),str(result.denominator)],"canonical rational")
    return result


def ceiling(x):
    return -(-x.numerator//x.denominator)


def index_scope(data):
    expected=dict(schema="regular-rational-plane-terminals-v1",J=[9965,21499],rank=19,
                  anchors=8,terminal_pair_dimension=3,pencil_plane_dimension=2,raw_cutoffs=[1,2],
                  W44=581590844909990298,B_star=B,near=NEAR,threshold=349525,large_fibres_max=2,
                  source_certificate_sha256="09a677b5f91a9abca6ace7e07dfbf7ab4f386905cec8e3f3551933007b027f68",
                  compiler_sha256="bac33f24d1f34760518406185fcc9850d4fc61f5441486f94237e13b99eb8ca8",
                  all_terminals_covered=False,original_source_closed=False,prize_closed=False,
                  mass_boxes=92042,maximum_envelope=272127061148955779)
    need(set(data)==set(expected)|{"profiles"},"index keys")
    for key,value in expected.items():
        need(type(data[key]) is type(value) and data[key]==value,"fixed scope: "+key)
    need(len(data["profiles"])==len(RANGES),"profile count")
    need(2130706433**6//2**128==B and NEAR==2*D,"original field budget and near")


def height(entry,j1,on,compiler,prior):
    need(set(entry)=={"height","gate","off_trace","price","cutoffs"},"height schema")
    h0,h1=entry["height"]
    need(all(type(x) is int for x in (h0,h1,entry["gate"],entry["price"])),"integer gate")
    need(0<=h0<=h1<=(j1-9)//2 and (h0>0 or h1==0),"normal-form height guard")
    g=entry["gate"]
    need((567500 if h0==0 else 250000)<=g and g+1<R-D+1,"source complement gate")
    off=prior.list_cap(entry["off_trace"],g-j1,D-42-h1-j1,j1,11)
    if h0==0:
        price=Q(581590844909990298+43*g*on+43*981147*off+44*(NEAR+1),44)
    else:
        price=Q(581590844909990298+43*981147*off,44)+R+21499+NEAR
        price+=Q(43*S**11*10**10,44*11**11*(D-42)**10)
    need(entry["price"]==ceiling(price)<=270000000000000000<B,"whole original pencil price")
    need(set(entry["cutoffs"])=={"1","2"},"both original raw cutoffs")
    bounds,boxes=[],0
    for t in (1,2):
        record=entry["cutoffs"][str(t)]
        need(set(record)=={"alpha","beta","terminal","boxes"},"mass-envelope keys")
        budget=S-h0
        lo,hi=D-h1+1-t,budget-g-1
        need(0<lo<=hi<budget and lo<=349525 and 3*349526>budget,"positive degree-corrected packing")
        candidates=[[],[]]
        for side,(left,right) in enumerate(((lo,min(349525,hi)),(349526,hi))):
            for left_box in range(left,right+1,5000):
                right_box=min(right,left_box+4999)
                r,w,k=right_box+2*h1-1,D+h0-t,j1-8-h0
                need(1<=w<=r and 2<=k and 2130706433**6>=r+k,"padded same-field scalar scope")
                proposed,trace=compiler.compile_cap(r,w,k,2)
                checked=prior.list_cap(trace,r,w,k,2)
                need(proposed==checked,"independent legality of proposed mass-box trace")
                candidates[side].append((left_box,checked))
        alpha=max([Q(0)]+[Q((budget-x)*v,x) for x,v in candidates[0]])
        beta=max([Q(0)]+[(budget-x)*v-alpha*x for x,v in candidates[1]])
        terminal=(t if h0==0 else R+j1)+budget*alpha+2*beta
        count=sum(map(len,candidates))
        need(rational(record["alpha"])==alpha and rational(record["beta"])==beta,"independent envelopes")
        need(rational(record["terminal"])==terminal and type(record["boxes"]) is int
             and record["boxes"]==count,"one inside charge, one mass, at most two excesses")
        bounds.append(terminal)
        boxes+=count
    return bounds,boxes


def profile(data,expected_j,masses,compiler,prior):
    need(set(data)=={"schema","J","on_trace","mass_floor","heights","terminals",
                     "weighted_envelope","reserve"},"profile schema")
    need(data["schema"]=="regular-rational-plane-profile-v1" and data["J"]==list(expected_j),"J scope")
    low,high=expected_j
    need(type(data["mass_floor"]) is int and data["mass_floor"]==masses[low],"independent original mass")
    on=prior.list_cap(data["on_trace"],R-567501,D-43,high,11)
    wanted=[(0,0)]+[(h,min(h+199,(high-9)//2)) for h in range(1,(high-9)//2+1,200)]
    need([tuple(x["height"]) for x in data["heights"]]==wanted,"exhaustive height bands")
    totals=[Q(0),Q(0)]
    count=0
    for row in data["heights"]:
        bounds,boxes=height(row,high,on,compiler,prior)
        totals=[max(a,b) for a,b in zip(totals,bounds)]
        count+=boxes
    need([rational(x) for x in data["terminals"]]==totals,"all height maxima")
    q1=Q(prod(range(R+1,R+9)),prod(range(D,D+8)))
    q2=Q(prod(range(R+1,R+9)),prod(range(D-1,D+7)))
    price=int(Q(masses[low],3)+q1*totals[0]/2+q2*totals[1]/6)+NEAR
    need(type(data["weighted_envelope"]) is int and type(data["reserve"]) is int
         and data["weighted_envelope"]==price<B and data["reserve"]==B-price,"exact sufficient weight test")
    return count


def main():
    raw=(NODE/"certificates/index.json").read_bytes()
    need(sha(raw)==INDEX_PIN,"frozen index")
    index=json.loads(raw)
    index_scope(index)
    cp=NODES/"list_padded_johnson_dimension_descent/compiler.py"
    ap=NODES/"rate_half_mca_coupled_pair_rank_frontier/verify_audit.py"
    need(sha(cp.read_bytes())==index["compiler_sha256"] and sha(ap.read_bytes())==AUDIT_PIN,
         "inherited selector and independent checker pins")
    compiler=load("propose_mass_traces",cp)
    prior=load("independent_list_and_resource_audit",ap)
    masses=prior.resource_floors()
    profiles=[]
    boxes=0
    for row,j in zip(index["profiles"],RANGES):
        need(set(row)=={"path","sha256"} and row["path"]==str(j[0])+".json","canonical profile identity")
        path=NODE/"certificates"/row["path"]
        need(not path.is_symlink() and path.stat().st_size<1024*1024,"bounded regular profile")
        raw=path.read_bytes()
        need(sha(raw)==row["sha256"],"profile hash")
        data=json.loads(raw)
        boxes+=profile(data,j,masses,compiler,prior)
        profiles.append(data)
    need(boxes==index["mass_boxes"] and max(p["weighted_envelope"] for p in profiles)
         ==index["maximum_envelope"],"complete profile envelope and census")
    need({p.name for p in (NODE/"certificates").iterdir()}==
         {"index.json",*(row["path"] for row in index["profiles"])},"no unlisted certificate")
    rejected=0
    for key,value in index.items():
        if key=="profiles":
            continue
        bad=copy.deepcopy(index)
        bad[key]=None
        try:
            index_scope(bad)
        except (ValueError,TypeError):
            rejected+=1
        else:
            raise ValueError("accepted wrong scope")
    first=profiles[0]
    on=prior.list_cap(first["on_trace"],R-567501,D-43,first["J"][1],11)
    for key in ("alpha","beta","terminal"):
        bad=copy.deepcopy(first["heights"][0])
        bad["cutoffs"]["1"][key]=["0","1"]
        try:
            height(bad,first["J"][1],on,compiler,prior)
        except ValueError:
            rejected+=1
        else:
            raise ValueError("accepted corrupted envelope")
    for delta in (-1,1):
        trace=copy.deepcopy(first["on_trace"])
        trace[-1][2]+=delta
        try:
            prior.list_cap(trace,R-567501,D-43,first["J"][1],11)
        except ValueError:
            rejected+=1
        else:
            raise ValueError("accepted false LIST step")
    print("PASS independent",boxes,"mass boxes and",2*boxes,"proposed LIST transitions")
    print("PASS 544 degree-adapted source gates; independent original resource and eight-anchor arithmetic")
    print("PASS",rejected,"scope/envelope/LIST mutations rejected")
    print("MAX ENVELOPE",index["maximum_envelope"],"RESERVE",B-index["maximum_envelope"])
    print("An affordable rational-plane class is not an exhaustive regular-terminal cover")


if __name__=="__main__":
    main()
