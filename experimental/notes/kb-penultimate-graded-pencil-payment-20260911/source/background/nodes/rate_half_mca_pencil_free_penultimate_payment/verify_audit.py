"""Independent child-bound and graded-price audit; no primary/helper imports."""
import copy
from collections import Counter
from fractions import Fraction as Q
import hashlib
import json
from math import comb
from pathlib import Path

NODE = Path(__file__).resolve().parent
PIN = "9715d8e88875c346a1e60df6fc58918812bdb5ceb5673a9172746dfea5901f57"
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


def same(a,b):
    return json.dumps(a,sort_keys=True)==json.dumps(b,sort_keys=True)


def encode(data):
    return (json.dumps(data,indent=2)+"\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def frac(value):
    value = Q(value)
    return [str(value.numerator),str(value.denominator)]


def integer(x):
    need(Q(x).denominator==1,"integer coefficient")
    return int(x)


def parents():
    raw = (PARENT/"index.json").read_bytes()
    need(sha(raw)==PARENT_PIN,"source index custody")
    refs = json.loads(raw)["profiles"]
    need(len(refs)==13,"source profile coverage")
    result,next_j,maximum = [],9965,0
    for ref in refs:
        need(ref["path"]==str(next_j)+".json","ordered source paths")
        raw = (PARENT/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"],"source shard custody")
        p = json.loads(raw)
        need(p["J"][0]==next_j,"source interval")
        next_j = p["J"][1]+1
        total = Q(p["mass_floor"],3)
        for t,den in ((1,2),(2,6)):
            factor = Q(1)
            for j in range(1,9):
                factor *= Q(R+j,D-t+j)
            total += factor*Q(*map(int,p["terminals"][t-1]))/den
        value = total.numerator//total.denominator+134944
        need(value==p["weighted_envelope"]<=272127061148955779,"original weighted resource")
        maximum = max(maximum,value)
        result.append((ref,p))
    need(next_j==21500 and maximum==272127061148955779,"whole original gap")
    return result


def child(eta,limit,m,bar,t,rec):
    need(all(type(x) is int for x in (eta,limit,m,bar,t)) and
         eta>=2 and limit>=1 and m>=2 and bar>=1 and t in (1,2),"child parameters")
    base = dict(eta=eta,nu=[1,limit],M=m)
    mode = rec["mode"]
    if mode=="interpolation":
        ell = rec["ell"]
        need(type(ell) is int and ell>=m-1,"interpolation monotonicity")
        rank = comb(ell+2,2)-(comb(ell-eta+2,2) if ell>=eta else 0)
        need(rank>comb(m,2),"nonzero restricted interpolation")
        degree = eta*limit
        gap = 2*m*(D+degree+1-t)-3*bar*degree-2*(R+degree+1)-2*degree*ell
        need(gap>0,"strict interpolation gate")
        expected = dict(base,mode=mode,ell=ell,gap_twice=gap)
    elif mode=="energy":
        def values(nu,v):
            degree = eta*nu
            n,a = R+degree+1+v,D+degree+1-t+v
            z = 2*m*a-3*bar*degree-n
            return z,z*z-(n+nu*(eta-1)*(eta-2))*(n+4*nu*m*(m-1))
        f0,f1,f2 = [values(n,0)[1] for n in (0,1,2)]
        a = Q(f2-2*f1+f0,2)
        b,c = f1-f0-a,f0
        ends = [values(n,0)[1] for n in (1,limit)]
        positive = [values(n,0)[0] for n in (1,limit)]
        need(min(ends)>0 and min(positive)>0,"strict energy and unsquared sign")
        vertex = None
        if a>0 and 1<=-b/(2*a)<=limit:
            need(values(-b/(2*a),0)[1]>0,"interior energy minimum")
            vertex = integer(4*a*c-b*b)
        derivatives,v2s = [],[]
        for n in (1,limit):
            g0,g1,g2 = [values(n,v)[1] for v in (0,1,2)]
            derivatives.append(integer(Q(4*g1-3*g0-g2,2)))
            v2s.append(integer(Q(g2-2*g1+g0,2)))
        need(min(derivatives)>=0 and v2s==[4*m*(m-1)]*2,"all-slack energy")
        expected = dict(base,mode=mode,coefficients=list(map(integer,(c,b,a))),
                        endpoints=ends,vertex_discriminant=vertex,positive_Z=positive,
                        v_derivatives=derivatives,v2=v2s[0])
    elif mode=="plane_occupancy":
        cap = bar*(R+eta+1)//(D+eta+1-t)
        need(m>cap,"plane occupancy gate")
        expected = dict(base,mode=mode,qbar=bar,cap=cap)
    else:
        raise ValueError("unproved child mode")
    need(same(rec,expected),"child certificate fields/types")
    return mode


def price(p,t,rec):
    k,h = p["J"][1]-8,(p["J"][1]-1)//10
    bar = (R-k+2)//(D-k+2-t)
    q1 = (R-p["heights"][0]["gate"])//(D+1-t)
    need(D-k+2-t>0 and 2*q1<=bar,"old spectral/plane capacities")
    need((R+1)//(D+1-t)<=bar,"line occupancy covered by plane cap")
    b0 = rec["ordinary_cap"]
    need(type(b0) is int and b0>=2,"ordinary count")
    m,ell = b0+1,b0
    need(comb(ell+2,2)-1>comb(m,2),"high-image restricted rank")
    high = 2*m*(D+k-t)-3*bar*(k-1)-2*(R+k)-2*(k-1)*ell
    need(high>0,"all-high-image interpolation")
    ordinary,extra = rec["ordinary_checks"],rec["all_normalization_checks"]
    need([x["eta"] for x in ordinary]==[x["eta"] for x in extra]==list(range(2,b0)),
         "all low-image child coverage")
    modes = Counter()
    for eta,row in zip(range(2,b0),ordinary):
        modes[child(eta,min(h,k//(eta+1)),m,bar,t,row)] += 1
    theta = 0
    for eta,row in zip(range(2,b0),extra):
        cap = row["cap"]
        need(type(cap) is int and cap>=1,"arbitrary child count")
        modes[child(eta,(k-1)//eta,cap+1,bar,t,row["proof"])] += 1
        cost = (eta-1)*max(cap-b0,0)
        need(same(row,dict(eta=eta,cap=cap,excess_price=cost,proof=row["proof"])),
             "graded image cost, not branch-only or unweighted cost")
        theta = max(theta,cost)
    allowance = Q(*map(int,p["terminals"][t-1]))
    weight = R-D+t
    numerator = weight*((R+1)*b0+k*theta)
    gap = (R+1)*allowance-numerator
    need(gap>0,"original penultimate allowance")
    expected = dict(t=t,K=k,H=h,q1=q1,qbar=bar,original_pair_weight=weight,
                    allowance=p["terminals"][t-1],ordinary_cap=b0,
                    high_image_cutoff=b0,high_image_gap_twice=high,
                    ordinary_checks=ordinary,all_normalization_checks=extra,
                    excess_theta=theta,penultimate_bound=frac(Q(numerator,D+1-t)),
                    parent_allowance=frac(Q(R+1,D+1-t)*allowance),comparison_gap=frac(gap))
    need(same(rec,expected),"original owners/allowance and graded arithmetic")
    return gap,modes


def validate(index,shards,source):
    need(len(shards)==len(source)==13,"profile inventory")
    entries,minimum,modes = [],None,Counter()
    for shard,(ref,p) in zip(shards,source):
        need(len(shard["cutoffs"])==2,"both original cutoffs")
        for t,rec in zip((1,2),shard["cutoffs"]):
            gap,counts = price(p,t,rec)
            minimum = gap if minimum is None else min(minimum,gap)
            modes.update(counts)
        expected = dict(schema="pencil-free-penultimate-profile-v1",J=p["J"],
                        parent_profile_sha256=ref["sha256"],cutoffs=shard["cutoffs"])
        need(same(shard,expected),"profile identity")
        entries.append(dict(path=str(p["J"][0])+".json",sha256=sha(encode(shard)),J=p["J"],
                            ordinary_caps=[x["ordinary_cap"] for x in shard["cutoffs"]],
                            excess_theta=[x["excess_theta"] for x in shard["cutoffs"]]))
    expected = dict(schema="pencil-free-penultimate-payment-v1",scope=SCOPE,
                    parent_index_sha256=PARENT_PIN,profiles=entries,profile_count=13,
                    raw_prices=26,child_certificates=sum(modes.values()),
                    minimum_comparison_gap=frac(minimum))
    need(same(index,expected) and sum(modes.values())==1208,"complete index/scope and 1208 child prices")
    return minimum,modes


def mutations(index,shards,source):
    count = 0
    def reject(edit):
        nonlocal count
        idx,parts = copy.deepcopy(index),copy.deepcopy(shards)
        edit(idx,parts)
        # Rehash every changed shard so a semantic test cannot stop at custody.
        for ref,p in zip(idx["profiles"],parts):
            ref["sha256"] = sha(encode(p))
        try:
            validate(idx,parts,source)
        except (ValueError,KeyError,TypeError):
            count += 1
            return
        raise ValueError("accepted corrupted certificate")
    for key in SCOPE:
        reject(lambda i,s,key=key: i["scope"].__setitem__(key,None))
    for key in ("t","K","H","q1","qbar","original_pair_weight","ordinary_cap",
                "high_image_cutoff","high_image_gap_twice","excess_theta"):
        reject(lambda i,s,key=key: s[0]["cutoffs"][0].__setitem__(key,
               s[0]["cutoffs"][0][key]+1))
    for key in ("allowance","penultimate_bound","parent_allowance","comparison_gap"):
        reject(lambda i,s,key=key: s[0]["cutoffs"][0].__setitem__(key,["0","1"]))
    reject(lambda i,s: s[0]["cutoffs"][0]["ordinary_checks"].pop())
    reject(lambda i,s: s[0]["cutoffs"][0]["all_normalization_checks"].pop())
    reject(lambda i,s: s[0]["cutoffs"][0]["ordinary_checks"][0].__setitem__("nu",[1,1]))
    reject(lambda i,s: s[0]["cutoffs"][0]["all_normalization_checks"][0].__setitem__("excess_price",0))
    located = {}
    for pi,p in enumerate(shards):
        for ti,rec in enumerate(p["cutoffs"]):
            for ri,row in enumerate(rec["all_normalization_checks"]):
                located.setdefault(row["proof"]["mode"],(pi,ti,ri))
    for mode,keys in (("interpolation",("ell","gap_twice")),
                      ("energy",("coefficients","endpoints","positive_Z","v_derivatives","v2")),
                      ("plane_occupancy",("qbar","cap"))):
        pi,ti,ri = located[mode]
        for key in keys:
            reject(lambda i,s,pi=pi,ti=ti,ri=ri,key=key:
                   s[pi]["cutoffs"][ti]["all_normalization_checks"][ri]["proof"].__setitem__(key,None))
    # Recompute the first birational interpolation price at unrestricted nu.
    rec = shards[0]["cutoffs"][0]
    eta,limit,m,bar,t = 2,(rec["K"]-1)//2,rec["ordinary_cap"]+1,rec["qbar"],1
    ell = rec["ordinary_checks"][0]["ell"]
    degree = eta*limit
    gap = 2*m*(D+degree+1-t)-3*bar*degree-2*(R+degree+1)-2*degree*ell
    bad = dict(eta=eta,nu=[1,limit],M=m,mode="interpolation",ell=ell,gap_twice=gap)
    try:
        child(eta,limit,m,bar,t,bad)
    except ValueError as error:
        need(str(error)=="strict interpolation gate" and gap<0,"recomputed ceiling failure")
    else:
        raise ValueError("accepted recomputed unrestricted ceiling")
    return count,limit,gap


def main():
    source = parents()
    folder = NODE/"certificates"
    raw = (folder/"index.json").read_bytes()
    need(sha(raw)==PIN,"new index custody")
    index = json.loads(raw)
    names = {str(p["J"][0])+".json" for _,p in source}|{"index.json"}
    need({p.name for p in folder.iterdir() if p.is_file()}==names,"certificate inventory")
    shards = []
    for ref in index["profiles"]:
        raw = (folder/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"],"new shard custody")
        shards.append(json.loads(raw))
    minimum,modes = validate(index,shards,source)
    count,limit,gap = mutations(index,shards,source)
    need([a for a in range(5) if a*(a*a-2)%5==0]==[0],"single field eigenvalue")
    # Exterior coefficients X^2,2X,2X^2-X^4 in the basis X,X^2,X^4.
    matrix = ((0,2,0),(1,0,2),(0,0,-1))
    a,b,c = matrix
    determinant = a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
    need(determinant%5==2,"pencil-free exterior map")
    need(len({(a,b) for a in range(5) for b in range(5)})==25>5,"off-mask affine plane")
    print("PASS26 original prices and1208 independently checked child certificates",dict(modes))
    print("MIN COMPARISON GAP",frac(minimum),"original eight-anchor resource unchanged")
    print("PASS",count,"rehashed mutations; recomputed ceiling",limit,"fails with gap",gap)
    print("PASS F5 off-eigen-mask rank-one plane control; not an official MCA source")
    print("Pencil-free penultimate enclosures with inherited nu are paid; other enclosures and Prizes remain open")


if __name__=="__main__":
    main()
