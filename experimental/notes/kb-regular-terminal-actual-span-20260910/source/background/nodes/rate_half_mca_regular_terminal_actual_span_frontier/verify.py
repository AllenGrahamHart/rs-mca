"""Actual-span and whole-constant-prefix bounds for regular rank19 terminals."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path

NODE=Path(__file__).resolve().parent
NODES=NODE.parent
R,D,E=1048576,67472,21499
PARENT="rate_half_mca_regular_rational_plane_terminal_bounds"
PARENT_PIN="432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
GATES_PIN="7b58ecc95009ca1a680784343b7121c25feca5ed238c3e9797daa381cc637d51"


def need(ok,why):
    if not ok:
        raise ValueError(why)


def ratio(value):
    value=Q(value)
    return [str(value.numerator),str(value.denominator)]


def decode(value):
    return Q(*map(int,value))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def build():
    cp=NODES/"list_padded_johnson_dimension_descent/compiler.py"
    spec=importlib.util.spec_from_file_location("constant_prefix_selector",cp)
    compiler=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(compiler)
    root=NODES/PARENT/"certificates"
    raw=(root/"index.json").read_bytes()
    need(sha(raw)==PARENT_PIN,"parent terminal pin")
    index=json.loads(raw)
    raw=(NODES/"rate_half_mca_coupled_pair_rank_frontier/gate_certificate.json").read_bytes()
    need(sha(raw)==GATES_PIN,"inherited all-height pencil gates")
    gates=json.loads(raw)
    profiles=[]
    steps=0
    for ref in index["profiles"]:
        raw=(root/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"],"parent J profile")
        parent=json.loads(raw)
        lo,hi=parent["J"]
        need(hi<=14964 or lo>=14965,"whole-constant prefix boundary")
        g=parent["heights"][0]["gate"]
        row=dict(J=[lo,hi],parent_sha256=ref["sha256"],constant_gate=g,
                 cutoffs={})
        for t in (1,2):
            allowance=decode(parent["terminals"][t-1])
            need(R+1<3*(g+1) and g+1<=R-D+t,"decreasing constant-plane weight")
            cases=dict(one_pair=Q(R-D+t),
                       constant_plane=t+(g+1)*Q(R-g,D+1-t)**2,
                       nonconstant_line=decode(gates["nonconstants"][str(t)+",1"]),
                       rank_two_plane=Q(R-E+10,D-E+10-t)*(R-D+t))
            need(all(value<=allowance for value in cases.values()),"all proper actual-span cases fit")
            result=dict(allowance=ratio(allowance),proper_cases={k:ratio(v) for k,v in cases.items()})
            if hi<=14964:
                boxes=[]
                for left in range(g+1,R-D+t+1,10000):
                    right=min(left+9999,R-D+t)
                    r,w,k=R-left,D-t,hi-8
                    need(1<=w<=r and 3<=k and 2130706433**6>=r+k,"scalar dimension3 corridor")
                    cap,trace=compiler.compile_cap(r,w,k,3)
                    weight=t+right*cap
                    boxes.append(dict(e=[left,right],trace=[list(x) for x in trace],weight=weight))
                    steps+=len(trace)
                maximum=max(b["weight"] for b in boxes)
                need(maximum<=allowance,"whole constant3 fits unchanged allowance on prefix")
                result.update(constant_boxes=boxes,constant_max=maximum)
            row["cutoffs"][str(t)]=result
        profiles.append(row)
    return dict(schema="regular-terminal-actual-span-v1",J=[9965,21499],actual_pair_rank=19,anchors=8,
                enclosure_dimension=3,proper_actual_dimension_max=2,whole_constant_prefix=[9965,14964],
                parent_index_sha256=PARENT_PIN,all_height_gates_sha256=GATES_PIN,
                compiler_sha256=sha(cp.read_bytes()),unchanged_template_maximum=index["maximum_envelope"],
                original_rank19_closed=False,whole_J_closed=False,prize_closed=False,
                profiles=profiles,constant_LIST_steps=steps)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write",action="store_true")
    args=parser.parse_args()
    data=build()
    encoded=(json.dumps(data,indent=2)+"\n").encode()
    path=NODE/"certificate.json"
    if args.write:
        need(not path.exists(),"refuse frozen certificate replacement")
        path.write_bytes(encoded)
    need(path.read_bytes()==encoded,"exact frozen certificate")
    for p in data["profiles"]:
        if p["J"][1]<=14964:
            print("CONSTANT3",p["J"],[p["cutoffs"][str(t)]["constant_max"] for t in (1,2)])
    print("PASS 26 proper-span cases;",data["constant_LIST_steps"],"constant-prefix LIST steps")
    print("UNCHANGED AVAILABLE-WEIGHT MAXIMUM",data["unchanged_template_maximum"])
    print("CERTIFICATE",sha(encoded),len(encoded),"bytes")
    print("A surviving obstruction has actual terminal span3; prefix constant pencils are paid")
    print("Pencil-free3 and whole constant3 on J14965..21499 remain open")


if __name__=="__main__":
    main()
