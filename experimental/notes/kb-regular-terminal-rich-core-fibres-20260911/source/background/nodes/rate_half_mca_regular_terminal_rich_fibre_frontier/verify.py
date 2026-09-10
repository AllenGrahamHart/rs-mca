"""Exact finite Johnson gates for excessive regular3 actual core fibres."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

NODE=Path(__file__).resolve().parent
PARENT=NODE.parent/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
INDEX_PIN="432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
R,D,ANCHORS=1048576,67472,8
BUDGET,MAXIMUM,NEAR=274980728111395087,272127061148955779,134944
RANGES=[(9965,10964),(10965,11964),(11965,12964),(12965,13364),(13365,13964),
        (13965,14964),(14965,15964),(15965,16964),(16965,17964),(17965,18964),
        (18965,19964),(19965,20964),(20965,21499)]

def need(ok,why):
    if not ok:
        raise ValueError(why)

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def root_budget(e,j):
    return j-3 if e==0 else ANCHORS+e*(j-ANCHORS-1)

def ceil(q):
    return -(-q.numerator//q.denominator)

def build():
    raw=(PARENT/"index.json").read_bytes()
    need(sha(raw)==INDEX_PIN,"parent index")
    index=json.loads(raw)
    profiles=[]
    for ref,ends in zip(index["profiles"],RANGES):
        raw=(PARENT/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"],"parent profile")
        parent=json.loads(raw)
        lo,hi=parent["J"]
        need((lo,hi)==ends,"complete degree profiles")
        row=dict(J=[lo,hi],parent_sha256=ref["sha256"],spectra=[])
        for e in range(4):
            b=root_budget(e,hi)
            n=R+hi-b
            candidates=[]
            for t in (1,2):
                allowance=Q(*map(int,parent["terminals"][t-1]))
                count=int(allowance/(R-D+t))
                a=D+hi-t-b
                boundary=Q((count+1)*a*a-n*a,count*n)
                candidates.append(ceil(boundary)-1)
            h=min(candidates)
            need(0<h<lo-9,"nonvacuous finite fibre gate")
            spectrum=dict(e=e,bad_bound=b,max_intersection=h,cutoffs={})
            for t in (1,2):
                a=D+hi-t-b
                numerator=n*(a-h)
                denominator=a*a-n*h
                need(0<a<=n and denominator>0,"positive Johnson corridor")
                count=numerator//denominator
                weight=count*(R-D+t)
                allowance=parent["terminals"][t-1]
                need(weight<=Q(*map(int,allowance)),"unchanged terminal allowance")
                spectrum["cutoffs"][str(t)]=dict(
                    reduced_n=n,reduced_agreement=a,numerator=numerator,denominator=denominator,
                    pair_cap=count,original_pair_weight=R-D+t,
                    terminal_weight=weight,allowance=allowance)
            row["spectra"].append(spectrum)
        profiles.append(row)
    need(len(profiles)==len(index["profiles"])==13,"profile count")
    return dict(schema="regular-terminal-rich-fibre-v1",J=[9965,21499],
                original_error_rank=12,actual_P2_rank=19,anchors=8,terminal_dimension=3,
                eigenvalues_field="original F",eigenspaces_max_dimension=1,
                root_mask="anchors plus F-eigenpolynomial roots; common zeros when e=0",
                intersection_scope="two actual complete joint cores on the remaining domain",
                raw_cutoffs=[1,2],parent_index_sha256=INDEX_PIN,
                unchanged_available_weight_maximum=MAXIMUM,B_star=BUDGET,near=NEAR,
                original_weights_unchanged=True,generic_degree_used=False,
                actual_core_witness=True,original_evaluation_flat_rank=9,
                whole_constant_upper_tail_open=True,rank19_closed=False,prize_closed=False,
                uniform_intersection_caps=[min(p["spectra"][e]["max_intersection"] for p in profiles)
                                           for e in range(4)],
                profiles=profiles)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write",action="store_true")
    args=parser.parse_args()
    data=build()
    encoded=(json.dumps(data,indent=2)+"\n").encode()
    path=NODE/"certificate.json"
    if args.write:
        need(not path.exists(),"refuse replacement of frozen certificate")
        path.write_bytes(encoded)
    need(path.read_bytes()==encoded,"exact frozen certificate")
    for row in data["profiles"]:
        print("GATES",row["J"],[s["max_intersection"] for s in row["spectra"]])
    print("PASS 13 profiles; 52 spectral gates; 104 exact Johnson weight tests")
    print("UNIFORM CAPS",data["uniform_intersection_caps"])
    print("CERTIFICATE",sha(encoded),len(encoded),"bytes")
    print("Excess forces an actual shared-core fibre beyond its gate; not universal terminal coverage")

if __name__=="__main__":
    main()
