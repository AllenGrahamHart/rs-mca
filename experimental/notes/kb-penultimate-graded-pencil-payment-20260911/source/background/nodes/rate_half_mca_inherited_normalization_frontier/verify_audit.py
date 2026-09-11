"""Independent rational-energy audit, without primary or helper imports."""
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

NODE = Path(__file__).resolve().parent
PIN = "b2e0c01a38c1eefd044c697f29f3fddc02015722895973ca05d921970ec67caf"
OLD_PIN = "6d5677e763c53bd135cbf244f75c3e974bf97e21a4cee285a53d3ac561332f4e"
PARENT_PIN = "432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
R,D = 1048576,67472
SCOPE = dict(original_error_rank=12,actual_P2_rank=19,J=[9965,21499],
             original_shared_dimension=11,anchors=8,terminal_dimension=3,
             pencil_free=True,raw_cutoffs=[1,2],image_degrees=[2,3,4,5],spectra=[0,1,2,3],
             normalization_ceiling="floor((J1-1)/10), from the original dimension11 carrier",
             primitive_degree="kappa=eta*nu+1, actual full-gcd degree",
             slack="every v>=0, not assumed saturated",
             spectral_capacity="old full profile degree ceiling, not improved silently",
             original_weights_unchanged=True,remaining_pencil_free_requires_actual_degree_jump=True,
             segre_coordinates="branch weighted; generic centres are not actual anchors",
             anchor_guard_globally_affordable=False,whole_constant_upper_tail_open=True,
             source_maximum=272127061148955779,B_star=274980728111395087,near=134944,
             whole_degree_closed=False,rank19_closed=False,prize_closed=False)


def need(ok,why):
    if not ok:
        raise ValueError(why)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def same(a,b):
    return json.dumps(a,sort_keys=True)==json.dumps(b,sort_keys=True)


def inputs():
    raw = (NODE.parent/"rate_half_mca_regular_terminal_low_image_degree_frontier/certificate.json").read_bytes()
    need(sha(raw)==OLD_PIN,"old certificate custody")
    old = json.loads(raw)
    folder = NODE.parent/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
    raw = (folder/"index.json").read_bytes()
    need(sha(raw)==PARENT_PIN,"original allowance custody")
    refs = json.loads(raw)["profiles"]
    need(len(refs)==len(old["profiles"])==13,"source inventory")
    parents,maximum,next_j = [],0,9965
    for ref,before in zip(refs,old["profiles"]):
        need(ref["path"]==str(next_j)+".json","original shard path")
        raw = (folder/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"],"original shard custody")
        p = json.loads(raw)
        need(p["J"]==before["J"] and p["J"][0]==next_j,"ordered original profiles")
        next_j = p["J"][1]+1
        need(before["kappa_max"]==p["J"][1]-8
             and p["heights"][0]["gate"]==before["original_constant_gate"],"original capacity ceiling")
        total = Q(p["mass_floor"],3)
        for t,den in ((1,2),(2,6)):
            factor = Q(1)
            for j in range(1,9):
                factor *= Q(R+j,D-t+j)
            total += factor*Q(*map(int,p["terminals"][t-1]))/den
            need(all(s["cutoffs"][t-1]["allowance"]==p["terminals"][t-1]
                     for s in before["spectra"]),"unchanged original allowances")
        value = total.numerator//total.denominator+134944
        need(value==p["weighted_envelope"]<=272127061148955779,"original eight-anchor resource")
        maximum = max(maximum,value)
        parents.append(p)
    need(next_j==21500 and maximum==272127061148955779,"complete gap and source maximum")
    return parents


def independent(p,e,t,eta,ceiling=None):
    k = p["J"][1]-8
    h = (p["J"][1]-1)//10 if ceiling is None else ceiling
    allowance = p["terminals"][t-1]
    weight = R-D+t
    cap = Q(*map(int,allowance))
    m = cap.numerator//(cap.denominator*weight)+1
    q1 = (R-p["heights"][0]["gate"])//(D+1-t)
    qbar = (R-k+2)//(D-k+2-t)
    cost = (Q(0),Q(qbar),Q(qbar+q1),Q(3*qbar,2))[e]
    pairs,g = m*(m-1)//2,(eta-1)*(eta-2)//2

    def values(nu,v=0):
        n = R+eta*nu+1+v
        core = D+eta*nu+1-t+v
        mask = cost*eta*nu
        z = 2*(m*core-mask)-n
        return z,z*z-(n+2*nu*g)*(n+8*nu*pairs)

    f0,f1,f2 = [values(Q(x))[1] for x in (0,1,2)]
    a = (f2-2*f1+f0)/2
    b,c = f1-f0-a,f0
    need(all(x.denominator==1 for x in (a,b,c)),"integral energy polynomial")
    vertex = 4*a*c-b*b if a>0 and 1<=-b/(2*a)<=h else None
    square_v = 4*m*(m-1)
    rec = dict(e=e,t=t,eta=eta,nu=[1,h],M=m,allowance=allowance,
               original_pair_weight=weight,q1=q1,qbar=qbar,root_cost_twice=int(2*cost),
               branch_budget=g,pair_budget=pairs,energy_coefficients=[int(c),int(b),int(a)],
               energy_endpoints=[int(values(x)[1]) for x in (1,h)],
               vertex_discriminant=None if vertex is None else int(vertex),
               positive_Z_endpoints=[int(values(x)[0]) for x in (1,h)],
               v_derivative_endpoints=[int(values(x,1)[1]-values(x)[1]-square_v) for x in (1,h)],
               v2=square_v,paid_terminal_weight=(m-1)*weight)
    xs = [Q(1),Q(h)]
    if a>0 and 1<-b/(2*a)<h:
        xs.append(-b/(2*a))
    minimum = min(values(x)[1] for x in xs)
    need(h>=1 and eta*h+1<=k and 2*q1<=qbar,"degree and inherited spectral envelope")
    need(all(values(x)[0]>0 for x in (1,h)),"positive Z before squaring")
    need(minimum>0,"strict all-normalization energy")
    need(min(rec["v_derivative_endpoints"])>=0 and square_v>0,"all-slack extension")
    need(all(values(x,2)[1]-2*values(x,1)[1]+values(x)[1]==2*square_v
             for x in (1,h)),"slack second difference")
    need((m-1)*weight<=cap<m*weight,"original first-unaffordable weight")
    return rec,minimum


def validate(index,shards,parents):
    need(index["schema"]=="inherited-normalization-frontier-v1","schema")
    need(same(index["scope"],SCOPE),"scope and types")
    need(index["old_certificate_sha256"]==OLD_PIN,"original image supplier")
    need(index["profile_count"]==len(index["profiles"])==len(shards)==len(parents)==13
         and index["exact_prices"]==416,"complete profile/price inventory")
    need(index["all_jump_free_pencil_free_paths_paid"] is True,"jump-free scope")
    count,next_j,minimum = 0,9965,None
    for ref,shard,p in zip(index["profiles"],shards,parents):
        h = (p["J"][1]-1)//10
        need(ref["path"]==str(next_j)+".json" and ref["J"]==shard["J"]==p["J"],"ordered complete profiles")
        next_j = p["J"][1]+1
        need(ref["normalization_ceiling"]==h,"original eleven-dimensional ceiling")
        need(shard["schema"]=="inherited-normalization-profile-v1"
             and shard["old_certificate_sha256"]==OLD_PIN,"shard scope")
        tuples = [(e,t,eta) for e in range(4) for eta in range(2,6) for t in (1,2)]
        need([(r["e"],r["t"],r["eta"]) for r in shard["prices"]]==tuples,"no omitted spectrum/eta/cutoff")
        for rec,(e,t,eta) in zip(shard["prices"],tuples):
            expected,gap = independent(p,e,t,eta)
            need(same(rec,expected),"independent rational identity")
            minimum = gap if minimum is None else min(minimum,gap)
            count += 1
    need(next_j==21500 and count==416,"complete original gap")
    return minimum


def mutations(index,shards,parents):
    count = 0

    def reject(idx,parts):
        nonlocal count
        try:
            validate(idx,parts,parents)
        except (ValueError,TypeError,KeyError,ZeroDivisionError):
            count += 1
            return
        raise ValueError("accepted malformed normalization price")

    for key in SCOPE:
        bad = copy.deepcopy(index)
        bad["scope"][key] = None
        reject(bad,shards)
    for key,value in (("schema","wrong"),("exact_prices",415),("profiles",[]),
                      ("old_certificate_sha256","0"*64),("all_jump_free_pencil_free_paths_paid",False)):
        bad = copy.deepcopy(index)
        bad[key] = value
        reject(bad,shards)
    for key in ("M","q1","qbar","root_cost_twice","branch_budget","pair_budget",
                "paid_terminal_weight","original_pair_weight","v2"):
        bad = copy.deepcopy(shards)
        bad[0]["prices"][0][key] += 1
        reject(index,bad)
    for key in ("energy_coefficients","energy_endpoints","positive_Z_endpoints",
                "v_derivative_endpoints","nu"):
        bad = copy.deepcopy(shards)
        bad[0]["prices"][0][key][0] += 1
        reject(index,bad)
    for mode in ("missing","duplicate","order","profile","source"):
        bad = copy.deepcopy(shards)
        if mode=="missing":
            bad[0]["prices"].pop()
        elif mode=="duplicate":
            bad[0]["prices"].append(copy.deepcopy(bad[0]["prices"][0]))
        elif mode=="order":
            bad[0]["prices"].reverse()
        elif mode=="profile":
            bad[0]["J"][0] += 1
        else:
            bad[0]["old_certificate_sha256"] = "0"*64
        reject(index,bad)
    p = parents[0]
    raised = (p["J"][1]-9)//5
    try:
        independent(p,3,2,5,raised)
    except ValueError as error:
        need(str(error)=="strict all-normalization energy","wrong raised-ceiling failure")
    else:
        raise ValueError("fully recomputed unrestricted ceiling unexpectedly pays")
    return count,raised


def main():
    parents = inputs()
    raw = (NODE/"certificates/index.json").read_bytes()
    need(sha(raw)==PIN,"new index custody")
    index = json.loads(raw)
    names = {str(p["J"][0])+".json" for p in parents}
    shards = []
    for ref in index["profiles"]:
        need(ref["path"] in names,"listed shard path")
        raw = (NODE/"certificates"/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"],"new shard custody")
        shards.append(json.loads(raw))
    minimum = validate(index,shards,parents)
    count,raised = mutations(index,shards,parents)
    print("PASS independent416 all-nu/all-v rational prices and unchanged original eight-anchor resource")
    print("MIN SQUARED GAP",minimum)
    print("PASS",count,"mutations plus fully recomputed raised ceiling failure at",raised)
    print("Excess requires an actual degree jump; global anchor affordability and both Prizes remain open")


if __name__=="__main__":
    main()
