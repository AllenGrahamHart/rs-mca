"""Uniform multiplicity-priced penultimate payment at original allowances."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

NODE = Path(__file__).resolve().parent
PARENT = NODE.parent/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
PARENT_PIN = "432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
R,D = 1048576,67472
SCOPE = dict(original_error_rank=12,actual_P2_rank=19,J=[9965,21499],
             field="2130706433^6",agreement=1116048,target="2^-128",
             old_anchors=7,parent_pair_dimension=5,parent_shared_dimension=4,
             parent_pencil_free=True,raw_cutoffs=[1,2],
             normalization_ceiling="nu<=floor((J1-1)/10)",
             prefix_degree="every actual nu*d_image<=J1-8",
             slack="every v>=0; full gcd and original weights retained",
             multiplicity_charge="binom(m+mu-1,2), not just branch count",
             geometric_price="sum extra incidences<=actual D*max_eta((eta-1)*(C_eta-b0)_+)",
             ordinary_child="every birational inner centre, including singular centres",
             occupancy_guard="affine planes at rank-one coordinates, not line-only",
             original_weights_unchanged=True,hereditary_pencil_freeness=True,
             all_parent_enclosures_paid=False,whole_constant_upper_tail_open=True,
             source_maximum=272127061148955779,B_star=274980728111395087,near=134944,
             rank19_closed=False,whole_degree_closed=False,prize_closed=False)


def need(ok,why):
    if not ok:
        raise ValueError(why)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(data):
    return (json.dumps(data,indent=2)+"\n").encode()


def frac(x):
    x = Q(x)
    return [str(x.numerator),str(x.denominator)]


def exclusion(eta,limit,m,qbar,t):
    c2 = 3*qbar
    degree = eta*limit
    n,a0 = R+1,D+1-t
    ell = m-1 if eta>=m-1 else (m*(m-1)+eta*(eta-3))//(2*eta)+1
    interpolation = 2*m*(a0+degree)-c2*degree-2*(n+degree)-2*degree*ell
    head = dict(eta=eta,nu=[1,limit],M=m)
    if interpolation>0:
        return dict(head,mode="interpolation",ell=ell,gap_twice=interpolation)
    z0,z1 = 2*m*a0-n,eta*(2*m-1-c2)
    u,v = eta+(eta-1)*(eta-2),eta+4*m*(m-1)
    c,b,a = z0*z0-n*n,2*z0*z1-n*(u+v),z1*z1-u*v
    ends = [a*x*x+b*x+c for x in (1,limit)]
    vertex = 4*a*c-b*b if a>0 and 2*a<=-b<=2*a*limit else None
    positive = [z0+z1*x for x in (1,limit)]
    derivatives = [2*(2*m-1)*(z0+z1*x)-2*n-(u+v)*x for x in (1,limit)]
    if min(positive)>0 and min(ends)>0 and (vertex is None or vertex>0) and min(derivatives)>=0:
        return dict(head,mode="energy",coefficients=[c,b,a],endpoints=ends,
                    vertex_discriminant=vertex,positive_Z=positive,
                    v_derivatives=derivatives,v2=4*m*(m-1))
    occupancy = qbar*(R+eta+1)//(D+eta+1-t)
    if m>occupancy:
        return dict(head,mode="plane_occupancy",qbar=qbar,cap=occupancy)
    return None


def selected_cap(eta,limit,qbar,t):
    lo,hi = 1,qbar*(R+eta+1)//(D+eta+1-t)+1
    while hi>lo+1:
        mid = (lo+hi)//2
        if exclusion(eta,limit,mid,qbar,t) is not None:
            hi = mid
        else:
            lo = mid
    proof = exclusion(eta,limit,hi,qbar,t)
    need(proof is not None,"selected child certificate")
    return hi-1,proof


def price(p,t):
    k,h = p["J"][1]-8,(p["J"][1]-1)//10
    allowance = Q(*map(int,p["terminals"][t-1]))
    weight = R-D+t
    q1 = (R-p["heights"][0]["gate"])//(D+1-t)
    qbar = (R-k+2)//(D-k+2-t)
    need(2*q1<=qbar and h>=1,"original spectral capacities")
    ordinary = []
    for b0 in range(2,int(allowance/weight)+1):
        m = b0+1
        high_gap = 2*m*(D+k-t)-3*qbar*(k-1)-2*(R+k)-2*(k-1)*b0
        if high_gap<=0:
            continue
        proposed = [exclusion(eta,min(h,k//(eta+1)),m,qbar,t) for eta in range(2,b0)]
        if all(rec is not None for rec in proposed):
            ordinary = proposed
            break
    else:
        raise ValueError("no certified ordinary baseline")
    extra,checks = [],[]
    for eta in range(2,b0):
        cap,proof = selected_cap(eta,(k-1)//eta,qbar,t)
        delta = (eta-1)*max(0,cap-b0)
        checks.append(dict(eta=eta,cap=cap,excess_price=delta,proof=proof))
        extra.append(delta)
    theta = max(extra,default=0)
    numerator = weight*((R+1)*b0+k*theta)
    gap = (R+1)*allowance-numerator
    need(gap>0,"strict whole-prefix original allowance")
    return dict(t=t,K=k,H=h,q1=q1,qbar=qbar,original_pair_weight=weight,
                allowance=p["terminals"][t-1],ordinary_cap=b0,
                high_image_cutoff=b0,high_image_gap_twice=high_gap,
                ordinary_checks=ordinary,all_normalization_checks=checks,
                excess_theta=theta,penultimate_bound=frac(Q(numerator,D+1-t)),
                parent_allowance=frac(Q(R+1,D+1-t)*allowance),
                comparison_gap=frac(gap))


def build():
    raw = (PARENT/"index.json").read_bytes()
    need(sha(raw)==PARENT_PIN,"parent index custody")
    refs = json.loads(raw)["profiles"]
    need(len(refs)==13,"source profile count")
    entries,shards,next_j,minimum = [],{},9965,None
    total_checks = 0
    for ref in refs:
        need(ref["path"]==str(next_j)+".json","ordered source paths")
        raw = (PARENT/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"],"parent profile custody")
        p = json.loads(raw)
        need(p["J"][0]==next_j,"consecutive original degrees")
        next_j = p["J"][1]+1
        cuts = [price(p,t) for t in (1,2)]
        for rec in cuts:
            gap = Q(*map(int,rec["comparison_gap"]))
            minimum = gap if minimum is None else min(minimum,gap)
            total_checks += len(rec["ordinary_checks"])+len(rec["all_normalization_checks"])
        shard = dict(schema="pencil-free-penultimate-profile-v1",J=p["J"],
                     parent_profile_sha256=ref["sha256"],cutoffs=cuts)
        name = str(p["J"][0])+".json"
        shards[name] = encode(shard)
        entries.append(dict(path=name,sha256=sha(shards[name]),J=p["J"],
                            ordinary_caps=[r["ordinary_cap"] for r in cuts],
                            excess_theta=[r["excess_theta"] for r in cuts]))
    need(next_j==21500,"complete original interval")
    index = dict(schema="pencil-free-penultimate-payment-v1",scope=SCOPE,
                 parent_index_sha256=PARENT_PIN,profiles=entries,profile_count=13,
                 raw_prices=26,child_certificates=total_checks,minimum_comparison_gap=frac(minimum))
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
    need((target/"index.json").read_bytes()==encode(index),"stored index")
    for name,data in shards.items():
        need((target/name).read_bytes()==data,"stored shard")
    for row in index["profiles"]:
        print("PAID",row["J"],"ordinary caps",row["ordinary_caps"],"extra theta",row["excess_theta"])
    print("PASS26 whole-degree/all-slack penultimate prices;",index["child_certificates"],"child certificates")
    print("MIN GAP",index["minimum_comparison_gap"],"INDEX",sha(encode(index)))
    print("Pencil-free parent and inherited normalization cap are required; full source and Prizes remain open")


if __name__=="__main__":
    main()
