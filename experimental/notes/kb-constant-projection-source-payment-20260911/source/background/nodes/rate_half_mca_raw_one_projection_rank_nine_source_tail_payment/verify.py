"""Exact original-source tail from a rank-nine projection of raw-one owners alone."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import prod
from pathlib import Path

NODE=Path(__file__).resolve().parent
NODES=NODE.parent
R,D,E,G,BUDGET=1048576,67472,21499,569050,274980728111395087
PINS={
    "list_padded_johnson_dimension_descent/compiler.py":"bac33f24d1f34760518406185fcc9850d4fc61f5441486f94237e13b99eb8ca8",
    "rate_half_mca_min_envelope_raw_mass/verify.py":"b6745db5995bdf421755408a54a92f052beadff4747391f62b93733b51be8867",
    "mca_min_envelope_fiber_contraction/polynomial.py":"d5cae0ac19b4cb4d7cbe0ebb67d1645204322b30b09ee003ec42b44cf3f4f3c9",
    "rate_half_mca_regular_rational_plane_terminal_bounds/certificates/index.json":"432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba",
}
SCOPE=dict(
    schema="raw-one-projection-source-tail-v1",field="2130706433^6",
    n=2097152,k=1048576,agreement=1116048,target_epsilon="2^-128",
    original_error_rank=12,J=[11925,21499],original_near=134944,
    projected_family="ACTUAL original raw-exactly-one pairs P1",
    projection_affine_dimension_max=9,
    projection_row="one fixed nonzero ORIGINAL-field constant row",
    P2_rank_restriction=False,P2_projection_restriction=False,
    pair_scalar_carrier_dimension=11,anchors=0,raw_cutoff=1,
    original_weights_and_complete_unions=True,global_inside_charge=1,
    constant_gate=569050,heavy_complement_max=913633,box_width=10000,
    projected_dimension=9,on_dimension=11,
    source_identity="floor((original min(raw,9) resource + original raw-one count)/2)+near",
    higher_raw_covered=True,source_alternatives="MAXIMUM",
    boundary_11924="this upper recipe exceeds budget; NOT an unsafe witness",
    whole_source_bound=274976274292770934,reserve=4453818624153,
    all_original_rank12_sources_closed=False,active_v4_atom=False,
    ordinary_LIST_closed=False,adjacent_safe_row_closed=False,prize_closed=False,
)


def need(ok,why):
    if not ok:raise ValueError(why)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def load(name,relative):
    path=NODES/relative;need(sha(path.read_bytes())==PINS[relative],"pinned supplier")
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def build():
    for path,pin in PINS.items():need(sha((NODES/path).read_bytes())==pin,"supplier bytes")
    compiler=load("raw_one_LIST","list_padded_johnson_dimension_descent/compiler.py")
    resource=load("raw_one_mass","rate_half_mca_min_envelope_raw_mass/verify.py")
    parent=NODES/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
    gates=[];next_j=9965
    for ref in json.loads((parent/"index.json").read_text())["profiles"]:
        raw=(parent/ref["path"]).read_bytes();need(sha(raw)==ref["sha256"],"gate profile pin")
        old=json.loads(raw);need(old["J"][0]==next_j and old["heights"][0]["gate"]>=G,"gate coverage")
        next_j=old["J"][1]+1
        gates.append(dict(path=ref["path"],sha256=ref["sha256"],J=old["J"]))
    need(next_j==21500 and len(gates)==13,"all original gates")
    base,base_trace=compiler.compile_cap(R,D-1,E,9);bins=[]
    for low in range(G+1,R-2*D+2,10000):
        high=min(low+9999,R-2*D+1)
        on,ot=compiler.compile_cap(R-low,D-1,E,11)
        tail,qt=compiler.compile_cap(R,R-high,E,9)
        bins.append(dict(e=[low,high],on=on,tail=tail,
                         on_trace=[list(x) for x in ot],tail_trace=[list(x) for x in qt],
                         weight=high*on*tail))
    rich=sum(row["weight"] for row in bins)
    raw_one=1+(R-D+1)*base+rich
    need(raw_one==31878195092556089,"original raw-one bound")
    branches=resource.envelope(9);endpoints=[]
    for j in (11924,11925):
        quotient=Q(prod(R+j-i for i in range(12)))/resource.beta(branches,9,j)
        mass=quotient.numerator//quotient.denominator
        residual=(mass+raw_one)//2+2*D
        endpoints.append(dict(J=j,mass_ratio=[str(quotient.numerator),str(quotient.denominator)],
                              mass_floor=mass,residual=residual,
                              whole=max(residual,270000000000000000),reserve=BUDGET-residual))
    need(endpoints[0]["residual"]>BUDGET>=endpoints[1]["residual"],"certified recipe threshold, not unsafe witness")
    need(endpoints[1]["whole"]==SCOPE["whole_source_bound"],"whole source maximum")
    return dict(scope=SCOPE,supplier_pins=PINS,gate_profiles=gates,base_count=base,
                base_trace=[list(x) for x in base_trace],bins=bins,rich_weight=rich,
                raw_one_bound=raw_one,endpoints=endpoints,heavy_boxes=len(bins),LIST_steps=9+20*len(bins))


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--write",action="store_true")
    args=parser.parse_args();data=build();raw=(json.dumps(data,indent=2)+"\n").encode()
    path=NODE/"certificate.json"
    if args.write:need(not path.exists(),"refuse frozen replacement");path.write_bytes(raw)
    else:need(path.read_bytes()==raw,"exact frozen reconstruction")
    print("PASS raw-one-only source census;",data["heavy_boxes"],"boxes;",data["LIST_steps"],"LIST steps")
    for row in data["endpoints"]:print("J",row["J"],"mass",row["mass_floor"],"recipe",row["residual"],"reserve",row["reserve"])
    print("P2 UNRESTRICTED; original rank12 J11925..21499 paid at the printed P1 projection scope")
    print("SHA256",sha(raw),"BYTES",len(raw))
    print("Previous J is not certified unsafe; whole row and both Prizes remain OPEN")


if __name__=="__main__":
    main()
