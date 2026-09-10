"""Independent actual-span/prefix audit; no new primary or selector imports."""
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path

NODE=Path(__file__).resolve().parent
NODES=NODE.parent
PIN="4299012381d17abfed946572f3fc44fafbe37f2bc54dc3d5acf02365e7c823b1"
AUDIT_PIN="59b9ad4918ced72f90938f3ac5817f5c504aa7a1daa11818d3fcf560dff01d2f"
PARENT_PIN="432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
GATES_PIN="7b58ecc95009ca1a680784343b7121c25feca5ed238c3e9797daa381cc637d51"
R,D,E=1048576,67472,21499
RANGES=[(9965,10964),(10965,11964),(11965,12964),(12965,13364),(13365,13964),
        (13965,14964),(14965,15964),(15965,16964),(16965,17964),(17965,18964),
        (18965,19964),(19965,20964),(20965,21499)]


def need(ok,why):
    if not ok:
        raise ValueError(why)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def rational(data):
    need(type(data) is list and len(data)==2 and all(type(x) is str for x in data),"rational type")
    x=Q(int(data[0]),int(data[1]))
    need(data==[str(x.numerator),str(x.denominator)],"canonical rational")
    return x


def scope(data):
    expected=dict(schema="regular-terminal-actual-span-v1",J=[9965,21499],actual_pair_rank=19,
                  anchors=8,enclosure_dimension=3,proper_actual_dimension_max=2,
                  whole_constant_prefix=[9965,14964],parent_index_sha256=PARENT_PIN,
                  all_height_gates_sha256=GATES_PIN,
                  compiler_sha256="bac33f24d1f34760518406185fcc9850d4fc61f5441486f94237e13b99eb8ca8",
                  unchanged_template_maximum=272127061148955779,
                  original_rank19_closed=False,whole_J_closed=False,prize_closed=False,constant_LIST_steps=1164)
    need(set(data)==set(expected)|{"profiles"},"schema")
    for key,value in expected.items():
        need(type(data[key]) is type(value) and data[key]==value,"exact scope: "+key)
    need(len(data["profiles"])==13 and [tuple(p["J"]) for p in data["profiles"]]==RANGES,
         "complete source degree ranges")


def scalar_box(box,t,g,hi,expected,check):
    need(set(box)=={"e","trace","weight"} and box["e"]==list(expected),"complete complement box")
    a,b=expected
    need(g+1<=a<=b<=R-D+t and all(type(x) is int for x in box["e"]),"legal complement")
    cap=check(box["trace"],R-a,D-t,hi-8,3)
    weight=t+b*cap
    need(type(box["weight"]) is int and box["weight"]==weight,"one preferred charge and original outside weight")
    return weight


def profile(row,parent,pencil,check):
    need(set(row)=={"J","parent_sha256","constant_gate","cutoffs"},"profile schema")
    need(row["J"]==parent["J"] and set(row["cutoffs"])=={"1","2"},"profile/cutoff identity")
    lo,hi=row["J"]
    g=row["constant_gate"]
    need(type(g) is int and g==parent["heights"][0]["gate"] and 3*(g+1)>R+1,"constant gate and monotonicity")
    steps=0
    for t in (1,2):
        record=row["cutoffs"][str(t)]
        expected_keys={"allowance","proper_cases"}|({"constant_boxes","constant_max"} if hi<=14964 else set())
        need(set(record)==expected_keys,"prefix-only claim")
        bound=rational(record["allowance"])
        need(bound==rational(parent["terminals"][t-1]),"unchanged prior allowance")
        need(g+1<=R-D+t<R+1 and R-g>=D+1-t,"populated constant ratio")
        # The original determinant bad count is 2J-a-2 with a=8.
        j=E
        bad=2*j-10
        need(8<=bad<D+j-t and D+j-t<=R+j,"original determinant guard")
        determinant=Q((R+j)-bad,(D+j-t)-bad)*(R-D+t)
        values=dict(one_pair=Q(R-D+t),
                    constant_plane=Q(t)+Q((g+1)*(R-g)**2,(D+1-t)**2),
                    nonconstant_line=pencil[t,1],rank_two_plane=determinant)
        need(set(record["proper_cases"])==set(values),"complete proper-span numerical cases")
        for key,x in values.items():
            need(rational(record["proper_cases"][key])==x<=bound,"proper-span case: "+key)
        if hi<=14964:
            wanted=[(a,min(a+9999,R-D+t)) for a in range(g+1,R-D+t+1,10000)]
            need(len(record["constant_boxes"])==len(wanted),"exhaustive complement count")
            maximum=0
            for box,ends in zip(record["constant_boxes"],wanted):
                maximum=max(maximum,scalar_box(box,t,g,hi,ends,check))
                steps+=3
            need(type(record["constant_max"]) is int and record["constant_max"]==maximum<=bound,
                 "whole constant3 fits unchanged allowance")
    return steps


def main():
    raw=(NODE/"certificate.json").read_bytes()
    need(sha(raw)==PIN,"frozen certificate")
    data=json.loads(raw)
    scope(data)
    ap=NODES/"rate_half_mca_coupled_pair_rank_frontier/verify_audit.py"
    need(sha(ap.read_bytes())==AUDIT_PIN,"independent inherited legality checker")
    spec=importlib.util.spec_from_file_location("inherited_span_legality",ap)
    prior=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prior)
    raw=(NODES/"rate_half_mca_coupled_pair_rank_frontier/gate_certificate.json").read_bytes()
    need(sha(raw)==GATES_PIN,"inherited pencil gates")
    _,pencil=prior.gates(json.loads(raw))
    cp=NODES/"list_padded_johnson_dimension_descent/compiler.py"
    need(sha(cp.read_bytes())==data["compiler_sha256"],"selected-trace provenance")
    root=NODES/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
    raw=(root/"index.json").read_bytes()
    need(sha(raw)==PARENT_PIN,"parent index")
    parent_index=json.loads(raw)
    parents=[]
    steps=0
    for row,ref in zip(data["profiles"],parent_index["profiles"]):
        need(ref["path"]==str(row["J"][0])+".json" and row["parent_sha256"]==ref["sha256"],
             "parent source identity")
        raw=(root/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"],"parent profile hash")
        parent=json.loads(raw)
        parents.append(parent)
        steps+=profile(row,parent,pencil,prior.list_cap)
    need(steps==1164 and parent_index["maximum_envelope"]==data["unchanged_template_maximum"],
         "step count and original envelope")
    rejected=0
    for key in data:
        if key=="profiles":
            continue
        bad=copy.deepcopy(data)
        bad[key]=None
        try:
            scope(bad)
        except (ValueError,TypeError):
            rejected+=1
        else:
            raise ValueError("accepted bad source/span scope")
    for kind in ("anchor-independent-case","allowance","missing-box","weight","trace"):
        bad=copy.deepcopy(data["profiles"][0])
        cut=bad["cutoffs"]["1"]
        if kind=="anchor-independent-case":
            cut["proper_cases"]["rank_two_plane"]=["0","1"]
        elif kind=="allowance":
            cut["allowance"]=["1","1"]
        elif kind=="missing-box":
            cut["constant_boxes"].pop()
        elif kind=="weight":
            cut["constant_boxes"][0]["weight"]-=1
        else:
            cut["constant_boxes"][0]["trace"][-1][-1]-=1
        try:
            profile(bad,parents[0],pencil,prior.list_cap)
        except (ValueError,KeyError):
            rejected+=1
        else:
            raise ValueError("accepted corrupted terminal case")
    print("PASS independent 26 proper-span/cutoff profiles and388 constant3 boxes")
    print("PASS",steps,"frozen scalar LIST transitions; original determinant and constant-plane guards")
    print("PASS",rejected,"scope/weight/trace mutations rejected")
    print("Surviving excess needs actual span3; the lower prefix is pencil-free")
    print("No source enumeration, arbitrary rank19 payment or Prize closure")


if __name__=="__main__":
    main()
