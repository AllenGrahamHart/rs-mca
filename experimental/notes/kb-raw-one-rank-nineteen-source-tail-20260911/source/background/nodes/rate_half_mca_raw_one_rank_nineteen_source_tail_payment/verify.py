"""Freeze the original raw-one rank19 enclosure bound and its source-tail composition."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import prod
from pathlib import Path

NODE=Path(__file__).resolve().parent
NODES=NODE.parent
R,D,E,BUDGET=1048576,67472,21499,274980728111395087
PINS={
    "rate_half_mca_all_coordinate_rank_nineteen_tail_payment/certificates/index.json": "37e1f226deb4ba670373090103ebe7d666200d3186542870c46595bf05797aae",
    "rate_half_mca_all_coordinate_rank_nineteen_tail_payment/certificates/20965.jsonl": "d1eab8b31949c355998a9831ee4a022b94ee947a5fd88c326d9795c5161f311a",
    "rate_half_mca_regular_rational_plane_terminal_bounds/certificates/20965.json": "b508835f0104f231a0bba86d38418fe270a2a1e05fa46f4a4a1debd0dd8d9633",
    "rate_half_mca_coupled_pair_rank_frontier/gate_certificate.json": "7b58ecc95009ca1a680784343b7121c25feca5ed238c3e9797daa381cc637d51",
    "rate_half_mca_raw_one_projection_rank_nine_source_tail_payment/certificate.json": "274a1f94ae1c81caabe2c8bc13ba1251756c01273f3e0613792f5259a355f8fc",
    "rate_half_mca_raw_two_quadratic_normal_payment/certificate.json": "3174586f037592a2a0025e7b89ef37bfcff353f7f3450708b3225245b6bee6f5",
    "rate_half_mca_min_envelope_raw_mass/verify.py": "b6745db5995bdf421755408a54a92f052beadff4747391f62b93733b51be8867",
    "mca_min_envelope_fiber_contraction/polynomial.py": "d5cae0ac19b4cb4d7cbe0ebb67d1645204322b30b09ee003ec42b44cf3f4f3c9"
}
SCOPE=dict(
    schema="raw-one-rank19-source-tail-v1",field="2130706433^6",
    n=2097152,k=1048576,agreement=1116048,target_epsilon="2^-128",
    original_error_rank=12,raw_weight_J=[9965,21499],paid_J=[20618,21499],
    actual_family="P1: pairs assigned original raw exactly one",
    actual_P1_pair_affine_rank_max=19,P2_rank_restriction=False,P2_projection_restriction=False,
    residual_antecedent="after paid original whole-source pencil alternatives",
    enclosure_pair_dimension=19,shared_dimension=11,actual_enclosure_occupation_required=False,
    generic_augmentation="one ORIGINAL-field constant vector when generic rank is10 and actual rank<=18",
    proper_carrier_bound=78301130139301820,small_projection_bound=31878195092556089,
    quadratic_contained_mass=89070753921055403,quadratic_moving_labels=21490,
    generic_raw_one_bound=180336660306614524,
    inherited_table_use="t=1 weighted enclosures only; no inherited whole P2 source conclusion",
    lower_J_inherited_in_G=False,upper_degree=21499,normalization_history="eight actual regular ancestors at G33",
    U_nonregular_children_retained=True,original_owners_weights_field=True,extra_anchor_factor=False,
    original_near=134944,source_identity="floor((original min(raw,9) resource+N1)/2)+near",
    source_alternatives="MAXIMUM",whole_source_bound=274978423712566784,reserve=2304398828303,
    J20617_unsafe_claim=False,all_original_rank12_sources_closed=False,
    active_v4_atom=False,ordinary_LIST_closed=False,adjacent_safe_row_closed=False,prize_closed=False,
)


def need(ok,why):
    if not ok:raise ValueError(why)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(relative):
    raw=(NODES/relative).read_bytes();need(sha(raw)==PINS[relative],"inherited bytes")
    return raw


def rational(x):
    return [str(x.numerator),str(x.denominator)]


def build():
    for p in PINS:read(p)
    rows=[json.loads(line) for line in read("rate_half_mca_all_coordinate_rank_nineteen_tail_payment/certificates/20965.jsonl").splitlines()]
    bands=[dict(kappa=r["kappa"],G11=r["full_generic"]) for r in rows if r["kind"]=="band" and r["t"]==1]
    generic=max(Q(*map(int,r["G11"])) for r in bands);cap=int(generic)
    projection=json.loads(read("rate_half_mca_raw_one_projection_rank_nine_source_tail_payment/certificate.json"))["raw_one_bound"]
    quadratic=json.loads(read("rate_half_mca_raw_two_quadratic_normal_payment/certificate.json"))
    proper=int(Q(prod(range(R,R+11)),11*(D+8)*prod(range(D-1,D+8))))
    cases=dict(proper_carrier=proper,small_projection=projection,
               quadratic_normal=quadratic["mass_cap"]+quadratic["moving_zeros"],generic_enclosure=cap)
    need(max(cases.values())==cap==SCOPE["generic_raw_one_bound"],"exhaustive source-class maximum")
    path=NODES/"rate_half_mca_min_envelope_raw_mass/verify.py"
    spec=importlib.util.spec_from_file_location("raw_one_rank19_shifted_mass",path)
    resource=importlib.util.module_from_spec(spec);spec.loader.exec_module(resource)
    tree=resource.envelope(9);endpoints=[]
    for j in (20617,20618):
        value=Q(prod(R+j-i for i in range(12)))/resource.beta(tree,9,j);mass=int(value)
        residual=(mass+cap)//2+2*D
        endpoints.append(dict(J=j,mass_ratio=rational(value),mass_floor=mass,
                              residual=residual,whole=max(residual,270000000000000000),
                              reserve=BUDGET-residual))
    need(endpoints[0]["residual"]>BUDGET>=endpoints[1]["residual"],"this certificate's first paid degree")
    need(endpoints[1]["whole"]==SCOPE["whole_source_bound"],"original source maximum")
    return dict(scope=SCOPE,supplier_pins=PINS,case_raw_one_bounds=cases,
                generic_rational=rational(generic),degree_bands=bands,
                t1_LIST_steps=11051,t1_recurrences=3268,line_height_rows=109,endpoints=endpoints)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--write",action="store_true")
    args=parser.parse_args();data=build();raw=(json.dumps(data,indent=2)+"\n").encode();path=NODE/"certificate.json"
    if args.write:need(not path.exists(),"refuse frozen overwrite");path.write_bytes(raw)
    else:need(path.read_bytes()==raw,"exact reconstruction")
    print("PASS43 inherited raw-one degree bands; maximum",data["case_raw_one_bounds"]["generic_enclosure"])
    print("CASES",data["case_raw_one_bounds"])
    for row in data["endpoints"]:print("J",row["J"],"MASS",row["mass_floor"],"SOURCE",row["residual"],"RESERVE",row["reserve"])
    print("P1 rank<=19 paid on J20618..21499; P2 unrestricted; earlier J not an unsafe witness")
    print("SHA256",sha(raw),"BYTES",len(raw),"Both Prizes remain OPEN")


if __name__=="__main__":
    main()
