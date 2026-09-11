"""Independent LIST-trace and degree-sensitive price audit; no primary imports."""
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path

NODE = Path(__file__).resolve().parent
NODES = NODE.parent
PARENT = NODES/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
PIN = "a587923b30d6e319c57e7bd9e78c85111b3447b37dc3a47e1c79df53874e55f8"
PARENT_PIN = "432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
COMPILER_PIN = "bac33f24d1f34760518406185fcc9850d4fc61f5441486f94237e13b99eb8ca8"
AUDITOR_PIN = "59b9ad4918ced72f90938f3ac5817f5c504aa7a1daa11818d3fcf560dff01d2f"
R, D0 = 1048576, 67472
SCOPE = dict(
    schema="constant-three-penultimate-v1", J=[9965,21499],
    field="2130706433^6", agreement=1116048, target_epsilon="2^-128",
    original_error_rank=12, actual_P2_rank=19, anchors=7, pair_shared=[5,4],
    constant_pencil_dimension=3, constant_pencil_dimension4_excluded=True,
    normalization_cap_required=False,
    local_allowance_antecedent="after proved whole-source pencil alternatives are removed",
    primitive_shared_degree_max="J-8", scalar_primitive_degree="E>=2",
    exceptional_coordinates="at most D-E, not D",
    ordinary_children="rank-two3/3 with constant plane; use height-zero C_t",
    degree_cut=12000, complement_box_width=10000,
    original_weights=True, full_gcd_and_slack=True,
    whole_constant_terminal_tail_paid=False, all_rank19_sources_paid=False, prize_closed=False,
    parent_index_sha256=PARENT_PIN, compiler_sha256=COMPILER_PIN,
)


def need(ok, why):
    if not ok:
        raise ValueError(why)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def rational(raw):
    need(type(raw) is list and len(raw)==2 and all(type(x) is str for x in raw), "rational types")
    value = Q(int(raw[0]),int(raw[1]))
    need(raw==[str(value.numerator),str(value.denominator)], "canonical rational")
    return value


def scope(data):
    keys = {"profiles","profile_prices","degree_bands","scalar_LIST_steps","minimum_gap"}
    need(set(data)==set(SCOPE)|keys, "index schema")
    for key,value in SCOPE.items():
        need(type(data[key]) is type(value) and data[key]==value, "exact scope: "+key)
    need(data["profile_prices"]==26 and data["degree_bands"]==48
         and data["scalar_LIST_steps"]==5238, "complete arithmetic inventory")
    need(len(data["profiles"])==13, "original profile count")
    need(rational(data["minimum_gap"])==Q(2464185717588779767135,12274496849), "frozen minimum")


def profile(data, original, original_hash, check):
    need(set(data)=={"J","parent_sha256","constant_gate","cutoffs"}, "profile schema")
    need(data["J"]==original["J"] and data["parent_sha256"]==original_hash, "source identity")
    need(set(data["cutoffs"])=={"1","2"}, "both original raw cutoffs")
    k = original["J"][1]-8
    gate = original["heights"][0]["gate"]
    need(type(data["constant_gate"]) is int and data["constant_gate"]==gate, "hereditary constant gate")
    cuts = [[2,min(k,11999)]]+([[12000,k]] if k>=12000 else [])
    steps, gaps, coarse = 0, [], []
    for t in (1,2):
        row = data["cutoffs"][str(t)]
        need(set(row)=={"constant_plane_price","allowance","bands"}, "cutoff schema")
        c = rational(row["constant_plane_price"])
        l = rational(row["allowance"])
        need(c==rational(original["heights"][0]["cutoffs"][str(t)]["terminal"]),
             "height-zero ordinary-child price, not all-height ceiling")
        need(l==rational(original["terminals"][t-1]) and 0<=c<=l, "unchanged allowance")
        need(gate+1<=R-D0+t and 1<=D0-t<=R-gate-1, "populated complement corridor")
        need(len(row["bands"])==len(cuts), "exhaustive primitive degree bands")
        largest_upper = 0
        for band, ends in zip(row["bands"], cuts):
            need(set(band)=={"E","boxes","whole_constant_weight","exceptional_excess","gap"}, "band schema")
            need(band["E"]==ends and all(type(x) is int for x in band["E"]), "exact whole degree interval")
            e0,e1 = ends
            expected = [[a,min(a+9999,R-D0+t)] for a in range(gate+1,R-D0+t+1,10000)]
            need(len(band["boxes"])==len(expected), "all union complement boxes")
            values = []
            for box, interval in zip(band["boxes"], expected):
                need(set(box)=={"e","trace","weight"} and box["e"]==interval, "complete integer complement partition")
                a,b = interval
                answer = check(box["trace"], R-a, D0-t, e1+1, 3)
                need(type(box["weight"]) is int and box["weight"]==t+b*answer,
                     "single preferred charge and original outside weight")
                values.append(box["weight"])
                steps += 3
            upper = max(values)
            need(type(band["whole_constant_weight"]) is int and band["whole_constant_weight"]==upper,
                 "whole-constant child upper maximum")
            extra = (k-e0)*max(Q(0),upper-c)
            gap = (R+1)*(l-c)-extra
            need(rational(band["exceptional_excess"])==extra, "degree-credit factor at LOW primitive degree")
            need(rational(band["gap"])==gap and gap>0, "strict original-source price")
            # Increasing full-gcd slack is harmless once C<=L and d0+1-t<=R+1.
            need(D0+1-t<=R+1 and k<D0+1-t, "all-slack positive denominator")
            gaps.append(gap)
            largest_upper = max(largest_upper, upper)
        coarse.append((R+1)*(l-c)-k*max(Q(0),largest_upper-c))
    return steps,gaps,coarse


def must_reject(action):
    try:
        action()
    except (ValueError, TypeError, KeyError, IndexError, ZeroDivisionError):
        return
    raise ValueError("accepted semantic corruption")


def main():
    raw = (NODE/"certificates/index.json").read_bytes()
    need(sha(raw)==PIN, "frozen price index")
    index = json.loads(raw)
    scope(index)
    path = NODES/"rate_half_mca_coupled_pair_rank_frontier/verify_audit.py"
    need(sha(path.read_bytes())==AUDITOR_PIN, "independent inherited LIST legality checker")
    spec = importlib.util.spec_from_file_location("constant_three_independent_LIST", path)
    prior = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prior)
    need(sha((NODES/"list_padded_johnson_dimension_descent/compiler.py").read_bytes())==COMPILER_PIN,
         "selector provenance only; never imported")
    raw = (PARENT/"index.json").read_bytes()
    need(sha(raw)==PARENT_PIN, "source index")
    refs = json.loads(raw)["profiles"]
    prices, gaps, steps, samples, next_j = [], [], 0, [], 9965
    for entry, source_ref in zip(index["profiles"], refs):
        need(set(entry)=={"path","sha256","J"} and entry["path"]==str(next_j)+".json",
             "canonical profile path")
        need(source_ref["path"]==entry["path"], "same original interval")
        raw = (PARENT/source_ref["path"]).read_bytes()
        need(sha(raw)==source_ref["sha256"], "original profile pin")
        original = json.loads(raw)
        need(entry["J"]==original["J"] and original["J"][0]==next_j, "no omitted source J")
        next_j = original["J"][1]+1
        raw = (NODE/"certificates"/entry["path"]).read_bytes()
        need(sha(raw)==entry["sha256"], "price shard hash")
        data = json.loads(raw)
        count, current, coarse = profile(data,original,source_ref["sha256"],prior.list_cap)
        steps += count
        gaps += current
        prices += coarse
        samples.append((data,original,source_ref["sha256"]))
    need(next_j==21500 and steps==5238 and len(gaps)==48, "complete all-profile arithmetic")
    need(min(gaps)==rational(index["minimum_gap"]), "exact minimum comparison gap")
    actual = {p.name for p in (NODE/"certificates").iterdir()}
    need(actual=={"index.json",*(row["path"] for row in index["profiles"])}, "no unlisted certificate")

    rejected = 0
    for key in SCOPE:
        bad = copy.deepcopy(index)
        bad[key] = None
        must_reject(lambda:scope(bad))
        rejected += 1
    source,original,pin = samples[-1]
    for mode in ("allowance","constant","missing-band","wrong-low","wrong-high",
                 "missing-box","wrong-complement","missing-step","list-answer",
                 "whole-weight","extra","gap","gate","owner-weight","parent"):
        bad = copy.deepcopy(source)
        row = bad["cutoffs"]["1"]
        band = row["bands"][-1]
        if mode=="allowance":
            row["allowance"][0]=str(int(row["allowance"][0])+1)
        elif mode=="constant":
            row["constant_plane_price"][0]=str(int(row["constant_plane_price"][0])+1)
        elif mode=="missing-band":
            row["bands"].pop(0)
        elif mode=="wrong-low":
            band["E"][0]+=1
        elif mode=="wrong-high":
            band["E"][1]-=1
        elif mode=="missing-box":
            band["boxes"].pop()
        elif mode=="wrong-complement":
            band["boxes"][0]["e"][0]+=1
        elif mode=="missing-step":
            band["boxes"][0]["trace"].pop()
        elif mode=="list-answer":
            band["boxes"][0]["trace"][-1][-1]-=1
        elif mode=="whole-weight":
            band["whole_constant_weight"]-=1
        elif mode=="extra":
            band["exceptional_excess"]=["0","1"]
        elif mode=="gap":
            band["gap"]=["1","1"]
        elif mode=="gate":
            bad["constant_gate"]+=1
        elif mode=="owner-weight":
            band["boxes"][0]["weight"]-=1
        else:
            bad["parent_sha256"]="0"*64
        must_reject(lambda:profile(bad,original,pin,prior.list_cap))
        rejected += 1
    need(all(value<0 for value in prices[-4:]), "coarse no-degree-credit recipe really fails last2 profiles")
    print("PASS independent26 prices;",len(gaps),"whole degree bands;",steps,"LIST transitions")
    print("MIN GAP",index["minimum_gap"])
    print("PASS",rejected,"semantic mutations with hashes bypassed for content audit")
    print("PASS recomputed no-degree-credit failure on both cutoffs of final2 profiles")
    print("Maximal constant3 parent is paid; individual constant3 tail and constant4 parent remain open")


if __name__ == "__main__":
    main()
