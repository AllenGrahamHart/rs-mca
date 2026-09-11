"""Independent rational branch-energy audit; no primary or helper imports."""
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

NODE = Path(__file__).resolve().parent
PIN = "9d9a01c5e9ac131cf6e3f7485dfc1c91595acd26521797544fc339771f437893"
OLD_PIN = "6d5677e763c53bd135cbf244f75c3e974bf97e21a4cee285a53d3ac561332f4e"
PARENT_PIN = "432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
R, D = 1048576, 67472
SCOPE = dict(original_error_rank=12, actual_P2_rank=19, J=[9965,21499],
             anchors=8, terminal_dimension=3, pencil_free=True,
             eigenvalues_field="original F", raw_cutoffs=[1,2],
             primitive_degree="actual degree of U0/G, all eta+1<=kappa<=J1-8",
             degree_slack="every v>=0; original full gcd and unused degree retained",
             normalization_degree="nu=(kappa-1)/eta; finite flat normalization map",
             finite_fibre_bound="nu times geometric branch count, not nu alone",
             branch_budget="sum binom(b_p,2)<=binom(eta-1,2), from planarity",
             pair_budget="disjoint chosen actual groups, C<=binom(M,2)",
             squared_gate="Z>0 and Z^2>(N+2nu*g)(N+8nu*P)",
             coverage="new eta range up to old eta0-1; inherited payment above",
             original_weights_unchanged=True, whole_constant_upper_tail_open=True,
             available_weight_maximum=272127061148955779,
             B_star=274980728111395087, near=134944,
             rank19_closed=False, whole_degree_closed=False, prize_closed=False)


def need(ok, why):
    if not ok:
        raise ValueError(why)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def inputs():
    raw = (NODE.parent/"rate_half_mca_regular_terminal_low_image_degree_frontier/certificate.json").read_bytes()
    need(sha(raw)==OLD_PIN, "old image certificate custody")
    old = json.loads(raw)
    folder = NODE.parent/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
    raw = (folder/"index.json").read_bytes()
    need(sha(raw)==PARENT_PIN, "parent allowance custody")
    refs = json.loads(raw)["profiles"]
    parents, maximum = [], 0
    for ref, before in zip(refs, old["profiles"]):
        raw = (folder/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"], "parent profile custody")
        p = json.loads(raw)
        need(p["J"]==before["J"] and p["heights"][0]["gate"]==before["original_constant_gate"],
             "source profile identity")
        total = Q(p["mass_floor"],3)
        for t, den in ((1,2),(2,6)):
            factor = Q(1)
            for j in range(1,9):
                factor *= Q(R+j,D-t+j)
            total += factor*Q(*map(int,p["terminals"][t-1]))/den
        value = int(total)+134944
        need(value==p["weighted_envelope"]<=272127061148955779, "original eight-anchor template")
        maximum = max(maximum,value)
        parents.append(p)
    need(len(parents)==len(old["profiles"])==len(refs)==13 and maximum==272127061148955779,
         "complete unchanged source allowance profiles")
    return parents, old


def independent(eta, e, t, p):
    k = p["J"][1]-8
    allowance = p["terminals"][t-1]
    weight = R-D+t
    m = int(Q(*map(int,allowance))/weight)+1
    pairs, g = m*(m-1)//2, (eta-1)*(eta-2)//2
    q1 = (R-p["heights"][0]["gate"])//(D+1-t)
    qbar = (R-k+2)//(D-k+2-t)
    cost = (Q(0),Q(qbar),Q(qbar+q1),Q(3*qbar,2))[e]

    def values(x, v=0):
        n, nu = R+x+v, Q(x-1,eta)
        z = 2*(m*(D+x-t+v)-cost*(x-1))-n
        return z, eta*eta*(z*z-(n+2*nu*g)*(n+8*nu*pairs))

    f0, f1, f2 = [values(x)[1] for x in (0,1,2)]
    a = (f2-2*f1+f0)/2
    b, c = f1-f0-a, f0
    need(all(x.denominator==1 for x in (a,b,c)), "integer energy polynomial")
    lo, hi = eta+1, k
    vertex = 4*a*c-b*b if a>0 and lo<=-b/(2*a)<=hi else None
    square_v = 4*eta*eta*m*(m-1)
    rec = dict(eta=eta,t=t,kappa=[lo,hi],allowance=allowance,
               original_pair_weight=weight,M=m,P=pairs,q1=q1,qbar=qbar,
               root_cost_twice=int(2*cost),branch_budget=g,
               energy_coefficients=[int(c),int(b),int(a)],
               energy_endpoints=[int(values(x)[1]) for x in (lo,hi)],
               vertex_discriminant=None if vertex is None else int(vertex),
               positive_Z_endpoints=[int(values(x)[0]) for x in (lo,hi)],
               v_derivative_endpoints=[int(values(x,1)[1]-values(x)[1]-square_v) for x in (lo,hi)],
               v2=square_v,paid_terminal_weight=(m-1)*weight)
    return rec, values, (a,b,c)


def check(rec, eta, e, t, p):
    expected, values, (a,b,c) = independent(eta,e,t,p)
    need(rec==expected, "independent field/arithmetic identity")
    lo, hi = rec["kappa"]
    xs = [Q(lo),Q(hi)]
    if a>0 and lo<-b/(2*a)<hi:
        xs.append(-b/(2*a))
    need(all(values(x)[0]>0 for x in (lo,hi)), "positive Z before squaring")
    need(all(values(x)[1]>0 for x in xs), "strict whole-kappa branch energy")
    need(min(rec["v_derivative_endpoints"])>=0 and rec["v2"]>0, "all-v extension")
    need(rec["qbar"]>=2*rec["q1"], "capacity hypotheses")
    need(rec["paid_terminal_weight"]<=Q(*map(int,rec["allowance"])), "original weight conversion")


def validate(index, shards, parents, old):
    need(index["schema"]=="regular-branch-energy-frontier-v1", "schema")
    need(json.dumps(index["scope"],sort_keys=True)==json.dumps(SCOPE,sort_keys=True), "scope and types")
    need(index["old_certificate_sha256"]==OLD_PIN and index["profile_count"]==13
         and index["spectral_gate_count"]==52, "supplier and inventory")
    need(len(index["profiles"])==len(shards)==13, "shard coverage")
    expected_J = 9965
    count = improvements = 0
    uniform = [0]*4
    for ref, shard, p, before in zip(index["profiles"],shards,parents,old["profiles"]):
        need(ref["path"]==str(expected_J)+".json" and ref["J"]==p["J"]==shard["J"],
             "ordered complete degree profiles")
        expected_J = p["J"][1]+1
        need(shard["schema"]=="regular-branch-energy-profile-v1"
             and shard["old_certificate_sha256"]==OLD_PIN
             and shard["original_constant_gate"]==p["heights"][0]["gate"], "shard source scope")
        need(len(ref["eta0"])==len(shard["spectra"])==4, "spectral coverage")
        for e, spectrum in enumerate(shard["spectra"]):
            first, last = spectrum["eta0"], before["spectra"][e]["eta0"]
            need(spectrum["e"]==e and spectrum["inherited_eta0"]==last
                 and first==ref["eta0"][e] and 2<=first<=last, "source-bound combined gate")
            expected = [(eta,t) for eta in range(first,last) for t in (1,2)]
            need([(r["eta"],r["t"]) for r in spectrum["checks"]]==expected, "no omitted eta or raw cutoff")
            for record in spectrum["checks"]:
                check(record,record["eta"],e,record["t"],p)
            count += len(expected)
            improvements += int(first<last)
            uniform[e] = max(uniform[e],first)
    need(expected_J==21500, "full original gap")
    need(count==index["new_strict_prices"]==328 and improvements==index["improved_spectral_gates"]==46,
         "strict price inventory")
    need(uniform==index["uniform_image_thresholds"]==[4,5,6,6]
         and index["maximum_surviving_image_degree"]==5, "surviving class")


def mutations(index, shards, parents, old):
    cases = []
    for key in SCOPE:
        bad = copy.deepcopy(index)
        bad["scope"][key] = None
        cases.append((bad,shards))
    for key, value in (("schema","wrong"),("profiles",[]),("new_strict_prices",0),
                       ("uniform_image_thresholds",[2,2,2,2]),("old_certificate_sha256","0"*64)):
        bad = copy.deepcopy(index)
        bad[key] = value
        cases.append((bad,shards))
    for mode in ("omit","duplicate","coefficient","weight","Z","branch","degree","v"):
        bad = copy.deepcopy(shards)
        records = bad[1]["spectra"][0]["checks"]
        if mode=="omit":
            records.pop()
        elif mode=="duplicate":
            records.append(copy.deepcopy(records[0]))
        else:
            row = records[0]
            if mode=="coefficient":
                row["energy_coefficients"][0] += 1
            elif mode=="weight":
                row["original_pair_weight"] -= 1
            elif mode=="Z":
                row["positive_Z_endpoints"][0] *= -1
            elif mode=="branch":
                row["branch_budget"] = 0
            elif mode=="degree":
                row["kappa"][0] += 1
            else:
                row["v_derivative_endpoints"][0] = -1
        cases.append((index,bad))
    for a,b in cases:
        try:
            validate(a,b,parents,old)
        except (ValueError,KeyError,TypeError,IndexError):
            continue
        raise ValueError("accepted malformed certificate")
    # Recompute EVERY dependent field for a lower gate, then test its mathematics.
    bad,_,_ = independent(3,0,1,parents[0])
    try:
        check(bad,3,0,1,parents[0])
    except ValueError as error:
        need(str(error)=="strict whole-kappa branch energy", "counterfactual must fail the actual price")
    else:
        raise ValueError("unaffordable lower gate accepted")
    return len(cases)+1


def main():
    folder = NODE/"certificates"
    raw = (folder/"index.json").read_bytes()
    need(sha(raw)==PIN, "index custody")
    index = json.loads(raw)
    shards = []
    for ref in index["profiles"]:
        need(Path(ref["path"]).name==ref["path"] and ref["path"].endswith(".json"), "shard path")
        raw = (folder/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"], "shard custody")
        shards.append(json.loads(raw))
    parents, old = inputs()
    validate(index,shards,parents,old)
    print("PASS independent 328 whole-kappa/all-v prices; 46 improved gates; unchanged source allowances")
    print("PASS", mutations(index,shards,parents,old), "mutations including fully recomputed lower-gate failure")
    print("UNIFORM [4,5,6,6]; remaining image degrees2..5; no rank19 or Prize closure")


if __name__ == "__main__":
    main()
