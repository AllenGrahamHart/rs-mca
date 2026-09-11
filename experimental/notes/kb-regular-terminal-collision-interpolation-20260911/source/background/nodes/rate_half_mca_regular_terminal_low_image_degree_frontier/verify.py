"""Exact finite interpolation prices for all high-image-degree regular3 terminals."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

NODE=Path(__file__).resolve().parent
PARENT=NODE.parent/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
PARENT_PIN="432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
CAPACITY_PIN="4c8ddb8396ce996e92fba3e12d6d96e87867668161e2cbbe710bf3de2dac501f"
R,D=1048576,67472
RANGES=[(9965,10964),(10965,11964),(11965,12964),(12965,13364),(13365,13964),
        (13965,14964),(14965,15964),(15965,16964),(16965,17964),(17965,18964),
        (18965,19964),(19965,20964),(20965,21499)]
GATES=[(4,5,5,6),(5,5,6,6),(5,6,6,6),(6,6,6,7),(6,7,7,7),(7,7,8,8),
       (7,8,8,8),(8,8,9,9),(8,9,9,9),(8,9,10,10),(9,10,10,10),
       (9,10,11,11),(9,10,11,11)]
SCOPE=dict(original_error_rank=12,actual_P2_rank=19,J=[9965,21499],anchors=8,
           terminal_dimension=3,pencil_free=True,eigenvalues_field="original F",
           raw_cutoffs=[1,2],image_degree="primitive homogeneous equation, not map degree or kappa",
           interpolation_rank="actual degree-ell product space, not all ternary forms",
           collision_cost="sum binom(r_p,2)<=binom(M,2), disjoint actual unordered pairs",
           pullback="nonzero polynomial with every actual multiplicity retained",
           primitive_degree="all 3..J1-8; actual degree and full polynomial gcd",
           degree_slack="every v>=0 retained",original_weights_unchanged=True,
           available_weight_maximum=272127061148955779,B_star=274980728111395087,near=134944,
           generic_fibre_used=False,finite_fibre_cap_assumed=False,
           whole_constant_upper_tail_open=True,rank19_closed=False,whole_degree_closed=False,
           prize_closed=False)

def need(ok,why):
    if not ok:
        raise ValueError(why)

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def build():
    raw=(PARENT/"index.json").read_bytes()
    need(sha(raw)==PARENT_PIN,"parent index custody")
    index=json.loads(raw)
    capacity=NODE.parent/"rate_half_mca_regular_terminal_eigen_capacity_frontier/certificates/index.json"
    need(sha(capacity.read_bytes())==CAPACITY_PIN,"capacity supplier custody")
    need(len(index["profiles"])==13,"parent coverage")
    profiles=[]
    margins=[]
    degrees=[]
    for ref,ends,gates in zip(index["profiles"],RANGES,GATES):
        raw=(PARENT/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"],"parent profile custody")
        p=json.loads(raw)
        need(p["J"]==list(ends),"original degree interval")
        k=ends[1]-8
        g=p["heights"][0]["gate"]
        row=dict(J=list(ends),parent_sha256=ref["sha256"],kappa_max=k,
                 original_constant_gate=g,spectra=[])
        for e,eta in enumerate(gates):
            spectrum=dict(e=e,eta0=eta,cutoffs=[])
            for t in (1,2):
                weight=R-D+t
                allowance=p["terminals"][t-1]
                m=int(Q(*map(int,allowance))/weight)+1
                pairs=m*(m-1)//2
                ell=(pairs-1+(eta-1)*(eta-2)//2)//eta+1
                need(ell>=max(m-1,eta-1),"whole-degree monotonicity and linear Hilbert range")
                rank=eta*ell+1-(eta-1)*(eta-2)//2
                need(rank>pairs,"nonzero pullback rank")
                q1=(R-g)//(D+1-t)
                qbar=(R-k+2)//(D-k+2-t)
                need(2*q1<=qbar,"root capacity hypotheses")
                c2=(0,2*qbar,2*(qbar+q1),3*qbar)[e]
                lhs=2*m*(D+k-t)
                rhs=2*(R+k)+(k-1)*(c2+2*ell)
                gap=lhs-rhs
                need(gap>0,"strict original incidence price")
                record=dict(t=t,allowance=allowance,original_pair_weight=weight,M=m,
                            unordered_pair_budget=pairs,ell=ell,product_rank=rank,q1=q1,qbar=qbar,
                            root_cost_twice=c2,incidence_lower_twice=lhs,incidence_upper_twice=rhs,
                            gap_twice=gap,kappa_slope_twice=2*(m-1-ell)-c2,
                            v_slope_twice=2*(m-1),paid_pair_cap=m-1,
                            paid_terminal_weight=(m-1)*weight)
                spectrum["cutoffs"].append(record)
                margins.append(gap)
                degrees.append(ell)
            row["spectra"].append(spectrum)
        profiles.append(row)
    return dict(schema="regular-low-image-degree-frontier-v1",scope=SCOPE,
                parent_index_sha256=PARENT_PIN,capacity_index_sha256=CAPACITY_PIN,
                profiles=profiles,profile_count=13,spectral_gate_count=52,cutoff_count=104,
                uniform_image_thresholds=[max(row[e] for row in GATES) for e in range(4)],
                maximum_surviving_image_degree=10,minimum_gap_twice=min(margins),
                maximum_interpolant_degree=max(degrees))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write",action="store_true")
    args=parser.parse_args()
    data=build()
    raw=(json.dumps(data,indent=2)+"\n").encode()
    path=NODE/"certificate.json"
    if args.write:
        need(not path.exists(),"refuse overwrite of frozen certificate")
        path.write_bytes(raw)
    need(path.read_bytes()==raw,"frozen certificate equality")
    for row in data["profiles"]:
        print("IMAGE GATES",row["J"],[s["eta0"] for s in row["spectra"]])
    print("PASS 52 image-degree gates; 104 strict incidence prices; all primitive degrees and v>=0")
    print("UNIFORM",data["uniform_image_thresholds"],"MIN GAP2",data["minimum_gap_twice"],
          "MAX ELL",data["maximum_interpolant_degree"])
    print("CERTIFICATE",sha(raw),len(raw),"bytes")
    print("Low image degrees and whole-constant upper tail remain; no whole J or Prize closure")

if __name__=="__main__":
    main()
