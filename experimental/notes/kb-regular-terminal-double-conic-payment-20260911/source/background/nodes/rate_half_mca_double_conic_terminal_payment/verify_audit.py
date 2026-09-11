"""Independent integer/hypergeometric audit; no primary or helper imports."""
import copy
from fractions import Fraction as Q
import hashlib
import json
from math import comb
from pathlib import Path

NODE = Path(__file__).resolve().parent
PARENT = NODE.parent/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
PIN = "ce10f247ab67af0312fa7cb9c08dce1c8338391bce2cb82893c4aa4a4db723f8"
PARENT_PIN = "432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
R,D = 1048576,67472
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


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def frac(x):
    x = Q(x)
    return [str(x.numerator),str(x.denominator)]


def rat(x):
    return Q(*map(int,x))


def choose(n,k):
    return comb(n,k) if 0<=k<=n else 0


def graph_bound(s):
    if s<=5:
        return s*s//4
    def phi(d):
        numerator = d**3-9*d*d+(6*s-4)*d
        need(numerator % 6==0,"integer degree polynomial")
        return numerator//6
    answer = 0
    for edges in range(s*s//4+1):
        degree,rem = divmod(2*edges,s)
        lhs = (s-4)*2*edges if 2*edges<=5*s else s*phi(degree)+rem*(phi(degree+1)-phi(degree))
        if lhs<=s*(s-1)*(s-2)//3:
            answer = edges
    return answer


def cost(m,s,r):
    # Reconstruct the expectation from the distribution, not its complement formula.
    numerator = sum((j-1)*choose(r,j)*choose(m-r,s-j) for j in range(2,min(r,s)+1))
    return Q(numerator,comb(m,s))


def record(p,t,s,a,b):
    j0,j1 = p["J"]
    allowance = rat(p["terminals"][t-1])
    weight = R-D+t
    m = allowance.numerator//(allowance.denominator*weight)+1
    need(2<=s<=m and a>=1 and b>=0,"admissible subset prices")
    n,agreement = R+j1,D+j1-t
    heights,checks,next_h = [],0,0
    limit = (j1-9)//2
    for line in p["heights"]:
        lo,hi = line["height"]
        need(lo==next_h and hi>=lo,"ordered height bins")
        next_h = hi+1
        e = line["gate"]+1
        for h in (lo,hi):
            common_zeros = j1-1-h
            denominator = agreement-common_zeros
            need(denominator>0,"original pencil denominator")
            heights.append((n-e-common_zeros)//denominator)
            if h:
                checks += 1
    need(next_h==limit+1,"complete conic normalization heights")
    q1,qcap = heights[0],max(heights)
    need(1<=q1<=qcap<=7,"source count bound")
    k = graph_bound(s)
    dual = []
    for r in range(qcap+1):
        f = cost(m,s,r)
        slack = a+b*f-r
        need(slack>=0,"actual occupancy dual")
        dual.append(dict(r=r,cost=frac(f),slack=frac(slack)))
    def gap(nu,v=0):
        length,core = R+2*nu+1+v,D+2*nu+1-t+v
        return m*core-30*nu-a*length-b*nu*k
    gaps = [gap(x) for x in (1,limit)]
    need(min(gaps)>0,"strict all-nu source price")
    slope = gap(1,1)-gap(1)
    need(slope>0 and slope==m-a,"all-v price")
    plane_gap = 16*(D+2-t)-(R+14)
    need(plane_gap>0,"rank-one plane15")
    need((m-1)*weight<=allowance<m*weight,"first unaffordable count")
    return dict(t=t,allowance=p["terminals"][t-1],original_pair_weight=weight,
                M=m,q1=q1,qcap=qcap,height_endpoint_checks=checks,
                subset_s=s,K_s=k,a=frac(a),b=frac(b),occupancy_dual=dual,
                nu=[1,limit],gap_nu_endpoints=[frac(x) for x in gaps],
                v_slope=frac(slope),plane_16_gap_min=plane_gap,
                paid_terminal_weight=(m-1)*weight)


def validate(index,shards,parents,refs):
    need(index["schema"]=="double-conic-payment-v1","schema")
    need(json.dumps(index["scope"],sort_keys=True)==json.dumps(SCOPE,sort_keys=True),"scope and types")
    need(index["parent_index_sha256"]==PARENT_PIN,"parent pin")
    helper = NODE.parent/"conic_direction_subset_forest_bound/bounds.py"
    need(index["graph_helper_sha256"]==sha(helper.read_bytes()),"graph helper custody")
    need(index["profile_count"]==13 and index["raw_price_count"]==26
         and len(index["profiles"])==len(shards)==len(parents)==len(refs)==13,"full inventory")
    need(index["whole_source_degrees_closed"]==0 and index["double_conic_class_paid"] is True,
         "class versus source scope")
    next_j,slacks,maximum = 9965,[],0
    for ref,shard,p,source in zip(index["profiles"],shards,parents,refs):
        need(ref["path"]==source["path"]==str(next_j)+".json"
             and ref["J"]==shard["J"]==p["J"],"ordered complete source profiles")
        next_j = p["J"][1]+1
        need(shard["schema"]=="double-conic-payment-profile-v1"
             and shard["parent_profile_sha256"]==source["sha256"],"source-bound profile")
        need(len(shard["cutoffs"])==2,"both original raw cutoffs")
        envelope = Q(p["mass_floor"],3)
        for t,rec in enumerate(shard["cutoffs"],1):
            expected = record(p,t,rec["subset_s"],rat(rec["a"]),rat(rec["b"]))
            need(rec==expected,"independent record identity")
            slacks.extend(map(rat,rec["gap_nu_endpoints"]))
            factor = Q(1)
            for j in range(1,9):
                factor *= Q(R+j,D-t+j)
            envelope += factor*rat(p["terminals"][t-1])/(2 if t==1 else 6)
        total = envelope.numerator//envelope.denominator+134944
        need(total==p["weighted_envelope"]==shard["weighted_envelope"]<=272127061148955779,
             "unchanged original weighted-anchor template")
        maximum = max(maximum,total)
        need(ref["qcap"]==[x["qcap"] for x in shard["cutoffs"]]
             and ref["M"]==[x["M"] for x in shard["cutoffs"]],"index profile summary")
    need(next_j==21500 and maximum==272127061148955779,"whole interval and unchanged maximum")
    need(index["minimum_gap"]==frac(min(slacks)),"minimum strict margin")


def main():
    raw = (PARENT/"index.json").read_bytes()
    need(sha(raw)==PARENT_PIN,"source custody")
    refs = json.loads(raw)["profiles"]
    parents = []
    for ref in refs:
        raw = (PARENT/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"],"source shard custody")
        parents.append(json.loads(raw))
    raw = (NODE/"certificates/index.json").read_bytes()
    need(sha(raw)==PIN,"index custody")
    index,shards = json.loads(raw),[]
    for ref in index["profiles"]:
        need(ref["path"] in {x["path"] for x in refs},"listed shard path")
        raw = (NODE/"certificates"/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"],"new shard custody")
        shards.append(json.loads(raw))
    validate(index,shards,parents,refs)
    cases = []
    for key in SCOPE:
        bad = copy.deepcopy(index)
        bad["scope"][key] = None
        cases.append((bad,shards))
    for field in ("M","q1","qcap","K_s","subset_s","paid_terminal_weight","plane_16_gap_min"):
        bad = copy.deepcopy(shards)
        bad[-1]["cutoffs"][-1][field] += 1
        cases.append((index,bad))
    for field in ("a","b","v_slope"):
        bad = copy.deepcopy(shards)
        bad[-1]["cutoffs"][-1][field][0] = "0"
        cases.append((index,bad))
    for mode in ("raw","gap","cost","height","source","coverage"):
        bad = copy.deepcopy(shards)
        if mode=="raw":
            bad[-1]["cutoffs"].pop()
        elif mode=="gap":
            bad[-1]["cutoffs"][-1]["gap_nu_endpoints"][1][0] = "0"
        elif mode=="cost":
            bad[-1]["cutoffs"][-1]["occupancy_dual"][-1]["cost"][0] = "0"
        elif mode=="height":
            bad[-1]["cutoffs"][-1]["nu"][1] -= 1
        elif mode=="source":
            bad[-1]["parent_profile_sha256"] = "0"*64
        else:
            bad.pop()
        cases.append((index,bad))
    for idx,parts in cases:
        try:
            validate(idx,parts,parents,refs)
        except (ValueError,TypeError,KeyError,ZeroDivisionError):
            continue
        raise ValueError("accepted corrupted source price")
    m = shards[-1]["cutoffs"][-1]["M"]
    try:
        record(parents[-1],2,m,Q(1),Q(1))
    except ValueError as error:
        need(str(error)=="strict all-nu source price","wrong bare-forest failure reason")
    else:
        raise ValueError("bare forest unexpectedly pays the upper profile")
    print("PASS independent26 all-nu/all-v source prices; original height bins and template")
    print("PASS",len(cases),"mutations plus fully recomputed bare-forest price failure")
    print("MIN GAP",index["minimum_gap"],"double-conic class paid; full source and Prizes remain open")


if __name__ == "__main__":
    main()
