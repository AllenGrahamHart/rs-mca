"""Exact original-source prices for every double-conic terminal profile."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path

NODE = Path(__file__).resolve().parent
PARENT = NODE.parent/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
PARENT_PIN = "432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
R,D = 1048576,67472
CHOICES = [(27,"1","1"),(32,"1","1"),(40,"1","1"),
           (33,"61/51","12341/8976"),(33,"4670/3327","57575/36597"),
           (26,"386/243","1666/729"),(24,"1387/842","105417/38732"),
           (24,"1387/842","105417/38732"),(24,"1387/842","105417/38732"),
           (22,"2339/1382","31005/9674"),(22,"17601/8998","27189/8998"),
           (19,"5721/2795","10494/2795"),(19,"5721/2795","10494/2795")]
SCOPE = dict(original_error_rank=12,actual_P2_rank=19,J=[9965,21499],
             field="2130706433^6",agreement=1116048,target="2^-128",
             anchors=8,terminal_dimension=3,pencil_free=True,
             evaluation_image_degree=2,kernel_image_degree=2,raw_cutoffs=[1,2],
             primitive_degree="D=2nu=kappa-1, every nu=1..floor((J1-9)/2)",
             degree_slack="every v>=0, full gcd and actual degree retained",
             nonconstant_collision_height="exactly nu in the ORIGINAL pair pencil",
             removed_fibres="only rank-one evaluation fibres, not all eigen roots",
             rank_one_plane_cap=15,rank_one_incidence_per_nu=30,
             subset_resource="exact all-subset forest expectation, not linear thinning",
             source_maximum=272127061148955779,B_star=274980728111395087,near=134944,
             original_weights_unchanged=True,all_conic_images_paid=False,
             whole_constant_upper_tail_open=True,rank19_closed=False,
             whole_degree_closed=False,prize_closed=False)


def need(ok, why):
    if not ok:
        raise ValueError(why)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encode(data):
    return (json.dumps(data,indent=2)+"\n").encode()


def fraction(x):
    x = Q(x)
    return [str(x.numerator),str(x.denominator)]


def build():
    helper = NODE.parent/"conic_direction_subset_forest_bound/bounds.py"
    spec = importlib.util.spec_from_file_location("conic_forest_resource",helper)
    bounds = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bounds)
    raw = (PARENT/"index.json").read_bytes()
    need(sha(raw)==PARENT_PIN,"parent custody")
    refs = json.loads(raw)["profiles"]
    need(len(refs)==len(CHOICES)==13,"complete profile inventory")
    entries,shards = [],{}
    next_j,all_slacks,maximum = 9965,[],0
    for ref,(s,a,b) in zip(refs,CHOICES):
        raw = (PARENT/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"],"parent shard custody")
        p = json.loads(raw)
        j0,j1 = p["J"]
        need(j0==next_j,"consecutive original degree coverage")
        next_j = j1+1
        v_max = (j1-9)//2
        a,b = Q(a),Q(b)
        cuts = []
        envelope = Q(p["mass_floor"],3)
        for t,den in ((1,2),(2,6)):
            allowance = Q(*map(int,p["terminals"][t-1]))
            weight = R-D+t
            m = int(allowance/weight)+1
            q1 = (R-p["heights"][0]["gate"])//(D+1-t)
            qcap,expected_h,checks = q1,1,0
            for line in p["heights"][1:]:
                lo,hi = line["height"]
                need(lo==expected_h and lo<=hi<=v_max,"complete original height bins")
                expected_h = hi+1
                gate = line["gate"]
                for h in (lo,hi):
                    qcap = max(qcap,(R+h-gate)//(D+h+1-t))
                    checks += 1
            need(expected_h==v_max+1 and 1<=q1<=qcap<=7,"original collision-line capacities")
            need(2<=s<=m and a>=1 and b>=0,"subset dual parameters")
            k = bounds.edge_bound(s)
            dual = []
            for r in range(qcap+1):
                cost = bounds.averaging_cost(m,s,r)
                slack = a+b*cost-r
                need(slack>=0,"all occupancy dual inequalities")
                dual.append(dict(r=r,cost=fraction(cost),slack=fraction(slack)))
            def gap(nu):
                return m*(D+2*nu+1-t)-30*nu-a*(R+2*nu+1)-b*nu*k
            slacks = [gap(nu) for nu in (1,v_max)]
            need(min(slacks)>0 and m-a>0,"strict all-nu/all-v price")
            plane_gap = 16*(D+1-t)-(R+1)+3
            need(plane_gap>0,"uniform rank-one plane cap15")
            all_slacks.extend(slacks)
            need((m-1)*weight<=allowance,"original weight conversion")
            factor = Q(1)
            for j in range(1,9):
                factor *= Q(R+j,D-t+j)
            envelope += factor*allowance/den
            cuts.append(dict(t=t,allowance=p["terminals"][t-1],original_pair_weight=weight,
                             M=m,q1=q1,qcap=qcap,height_endpoint_checks=checks,
                             subset_s=s,K_s=k,a=fraction(a),b=fraction(b),
                             occupancy_dual=dual,nu=[1,v_max],
                             gap_nu_endpoints=[fraction(x) for x in slacks],
                             v_slope=fraction(m-a),plane_16_gap_min=plane_gap,
                             paid_terminal_weight=(m-1)*weight))
        total = int(envelope)+134944
        need(total==p["weighted_envelope"]<=272127061148955779,"original source template")
        maximum = max(maximum,total)
        shard = dict(schema="double-conic-payment-profile-v1",J=p["J"],
                     parent_profile_sha256=ref["sha256"],cutoffs=cuts,weighted_envelope=total)
        shards[ref["path"]] = encode(shard)
        entries.append(dict(path=ref["path"],sha256=sha(shards[ref["path"]]),J=p["J"],
                            qcap=[x["qcap"] for x in cuts],M=[x["M"] for x in cuts]))
    need(next_j==21500 and maximum==272127061148955779,"full original interval")
    index = dict(schema="double-conic-payment-v1",scope=SCOPE,parent_index_sha256=PARENT_PIN,
                 graph_helper_sha256=sha(helper.read_bytes()),profiles=entries,
                 profile_count=13,raw_price_count=26,minimum_gap=fraction(min(all_slacks)),
                 whole_source_degrees_closed=0,double_conic_class_paid=True)
    return index,shards


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write",action="store_true")
    args = parser.parse_args()
    index,shards = build()
    target = NODE/"certificates"
    if args.write:
        target.mkdir(exist_ok=True)
        for name,data in shards.items():
            (target/name).write_bytes(data)
        (target/"index.json").write_bytes(encode(index))
    need((target/"index.json").read_bytes()==encode(index),"stored index differs")
    for name,data in shards.items():
        need((target/name).read_bytes()==data,"stored profile differs")
    for row in index["profiles"]:
        print("PAID DOUBLE CONIC",row["J"],"M",row["M"],"line caps",row["qcap"])
    print("PASS 26 original raw prices, all nu and v; minimum gap",index["minimum_gap"])
    print("INDEX",sha(encode(index)))
    print("Eta2 now requires chi3/4 for excess; eta3..5 and constant tail remain open")


if __name__ == "__main__":
    main()
