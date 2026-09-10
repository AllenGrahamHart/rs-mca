"""Independent integer-fibre and chosen-LIST-step audit; no local code imports."""

import copy
from fractions import Fraction as Q
import hashlib
import json
from math import prod
from pathlib import Path

NODE = Path(__file__).resolve().parent
PARENT = NODE.parent/"rate_half_mca_coupled_pair_rank_frontier"
PIN = "f7157b3e43dc166a00842fd07fcafb0cd00e424d15a89249a060cb597823d582"
GATES = "7b58ecc95009ca1a680784343b7121c25feca5ed238c3e9797daa381cc637d51"
SOURCE = "09a677b5f91a9abca6ace7e07dfbf7ab4f386905cec8e3f3551933007b027f68"
COMPILER = "bac33f24d1f34760518406185fcc9850d4fc61f5441486f94237e13b99eb8ca8"


def need(ok, why):
    if not ok:
        raise ValueError(why)


def read(path, pin):
    raw = path.read_bytes()
    need(hashlib.sha256(raw).hexdigest() == pin, "frozen source")
    return json.loads(raw)


def rational(raw):
    need(type(raw) is list and len(raw) == 2 and all(type(x) is str for x in raw), "rational type")
    value = Q(int(raw[0]), int(raw[1]))
    need(raw == [str(value.numerator), str(value.denominator)], "canonical rational")
    return value


def list_cap(trace, length_gap, agreement_gap, degree):
    need(1 <= agreement_gap <= length_gap and degree >= 5 and
         2130706433**6 >= length_gap+degree, "LIST source scope")
    need(len(trace) == 5, "all five actual scalar dimensions")
    old = 1
    for rank, row in enumerate(trace, 1):
        need(len(row) == 3 and all(type(v) is int for v in row), "integer transition")
        actual, cut, answer = row
        need(actual == rank and 0 <= cut <= degree, "dimension and allowed degree")
        if cut == 0:
            expected = (length_gap+rank)*old//(agreement_gap+rank)
        else:
            delta = (agreement_gap+cut)**2-(length_gap+cut)*(cut-1)
            need(delta > 0, "Johnson positivity")
            expected = (length_gap+cut)*(agreement_gap+1)//delta
            if cut < degree:
                expected = max(expected, (length_gap+cut+1)*old//(agreement_gap+cut+1))
        need(answer == expected and answer >= 1, "chosen-step legality")
        old = answer
    return old


def validate(data, inherited_gates, inherited_source):
    need(set(data) == {"schema", "parameters", "inherited_sha256", "compiler_sha256",
         "cases", "middle_mass_floor", "prefix", "middle", "upper", "total", "reserve",
         "boxes", "list_steps"}, "certificate schema")
    need(data["schema"] == "integer-compression-rank18-v1" and data["compiler_sha256"] == COMPILER,
         "scope and compiler identity")
    need(data["inherited_sha256"] == dict(gates=GATES, source=SOURCE), "inherited identities")
    need(data["parameters"] == dict(R=1048576, d=67472, source_J=[9965, 21499],
         anchors=6, cutoff=[1, 2], x_max=481076, threshold=349525, large_count=2,
         box_width=10000, original_rank=12, pair_rank=18, near=134944,
         B_star=274980728111395087), "actual original source and integer-packing scope")
    need(3*349526 > 1048577 and 2*349526 <= 1048577, "two large masses, not one or three")
    wanted = [(9965, 12964, 1), (9965, 12964, 2), (12965, 14164, 1), (12965, 14164, 2)]
    need(len(data["cases"]) == 4, "four degree and cutoff cases")
    terminal, boxes, steps = {}, 0, 0
    for case, (low_j, high_j, t) in zip(data["cases"], wanted):
        need(set(case) == {"J", "cutoff", "degree_max", "scalar_dimension", "small", "large",
             "alpha", "beta", "terminal"}, "case schema")
        degree = high_j-6
        need((case["J"], case["cutoff"], case["degree_max"], case["scalar_dimension"]) ==
             ([low_j, high_j], t, degree, 5), "actual degree range and FIVE-dimensional fibres")
        alpha_candidates, large_costs = [], []
        for name, lo, hi in (("small", 67473-t, 349525), ("large", 349526, 481076)):
            starts = list(range(lo, hi+1, 10000))
            need(len(case[name]) == len(starts), "exhaustive integer mass coverage")
            for row, low in zip(case[name], starts):
                high = min(low+9999, hi)
                need(set(row) == {"low", "high", "cap", "trace"} and
                     (row["low"], row["high"]) == (low, high), "exact mass box")
                cap = list_cap(row["trace"], high-1, 67472-t, degree)
                need(cap == row["cap"], "scalar pair cap")
                if name == "small":
                    alpha_candidates.append(Q((1048577-low)*cap, low))
                else:
                    large_costs.append(((1048577-low)*cap, low))
                boxes += 1
                steps += len(row["trace"])
        alpha = max(alpha_candidates)
        beta = max([Q(0)]+[cost-alpha*mass for cost, mass in large_costs])
        need(rational(case["alpha"]) == alpha >= 0 and rational(case["beta"]) == beta >= 0,
             "small linear envelope and large affine excess")
        terminal[low_j, t] = t+1048577*alpha+2*beta
        need(rational(case["terminal"]) == terminal[low_j, t], "one common preferred slope")
    need((boxes, steps, data["boxes"], data["list_steps"]) == (172, 860, 172, 860), "inventory")
    c = {key: rational(value) for key, value in inherited_gates["constants"].items()}
    p = {key: rational(value) for key, value in inherited_gates["nonconstants"].items()}

    def sparse(t, j):
        def determinant(a):
            need(67472-j+a+2-t > 0 and 1048576 > 67472-t, "increasing determinant")
            return Q(1048576-j+a+2, 67472-j+a+2-t)
        rank_two = determinant(7)*max(c[f"{t},2"], p[f"{t},2"], determinant(8)*(981104+t))
        exceptional = 2*j-14
        need(0 <= exceptional <= 1048577, "monotone sparse coefficient")
        return (1048577*rank_two+exceptional*max(Q(0), c[f"{t},4"]-rank_two))/(67473-t)

    for t in (1, 2):
        need(terminal[9965, t] <= sparse(t, 9965), "prefix compression inherits sparse NUMERICAL cap")
        need(terminal[12965, t] >= sparse(t, 14164), "middle covers both terminal types")
    old = inherited_source["boxes"]
    prefix_rows = [row for row in old if row["high"] <= 12964]
    need([(row["low"], row["high"]) for row in prefix_rows] ==
         [(low, low+199) for low in range(9965, 12965, 200)], "inherited prefix coverage")
    prefix = max(row["sparse18"] for row in prefix_rows)
    upper_rows = [row for row in old if row["low"] >= 14165]
    need([(row["low"], row["high"]) for row in upper_rows] ==
         [(low, min(low+199, 21499)) for low in range(14165, 21500, 200)], "inherited upper coverage")
    upper = max(row["full18"] for row in upper_rows)
    mass = next(row["mass_floor"] for row in old if row["low"] == 12965)
    need(mass == data["middle_mass_floor"] == 491840933524792929, "same original resource at12965")
    fractions = []
    for t in (1, 2):
        n = prod(range(1048578, 1048584))*terminal[12965, t].numerator
        d = prod(range(67474-t, 67480-t))*terminal[12965, t].denominator
        fractions.append((n, d))
    (n1, d1), (n2, d2) = fractions
    middle = (2*mass*d1*d2+3*n1*d2+n2*d1)//(6*d1*d2)+134944
    need((data["prefix"], data["middle"], data["upper"]) == (prefix, middle, upper) ==
         (274462040894062110, 270702759681887570, 273715780528023745), "independent three-range totals")
    need(data["total"] == max(270000000000000000, prefix, middle, upper) == 274462040894062110,
         "whole-source MAXIMUM")
    need(data["reserve"] == 274980728111395087-data["total"] == 518687217332977, "reserve")
    need(2130706433**6//2**128 == 274980728111395087, "actual challenge budget")


def mutations(data, gates, source):
    cases = []
    for field in ("anchors", "pair_rank", "original_rank", "large_count", "threshold", "near"):
        bad = copy.deepcopy(data)
        bad["parameters"][field] -= 1
        cases.append(bad)
    for kind in ("missing_case", "missing_small", "missing_large", "cutoff", "dimension",
                 "degree", "step", "alpha", "beta", "preferred", "boundary"):
        bad = copy.deepcopy(data)
        row = bad["cases"][-1]
        if kind == "missing_case":
            bad["cases"].pop()
        elif kind == "missing_small":
            row["small"].pop()
        elif kind == "missing_large":
            row["large"].pop()
        elif kind == "cutoff":
            row["cutoff"] -= 1
        elif kind == "dimension":
            row["scalar_dimension"] -= 1
        elif kind == "degree":
            row["degree_max"] -= 1
        elif kind == "step":
            row["large"][-1]["trace"][-1][-1] -= 1
        elif kind == "boundary":
            row["large"][0]["low"] -= 1
        else:
            key = "terminal" if kind == "preferred" else kind
            row[key][0] = str(int(row[key][0])-int(row[key][1]))
        cases.append(bad)
    for field in ("middle_mass_floor", "prefix", "middle", "upper", "total", "reserve"):
        bad = copy.deepcopy(data)
        bad[field] -= 1
        cases.append(bad)
    for bad in cases:
        try:
            validate(bad, gates, source)
        except (ValueError, KeyError):
            continue
        raise ValueError("accepted a corrupted certificate")
    return len(cases)


def main():
    data = read(NODE/"certificate.json", PIN)
    gates = read(PARENT/"gate_certificate.json", GATES)
    source = read(PARENT/"source_certificate.json", SOURCE)
    validate(data, gates, source)
    print("PASS independent172 integer-mass boxes and860 chosen LIST steps")
    print("PASS six shared anchors, actual scalar dimension5, at most two large fibres")
    print("PASS three original source ranges; whole rank18 total274462040894062110")
    print("PASS", mutations(data, gates, source), "scope/degree/cardinality/coverage/price mutations rejected")
    print("No primary/compiler imports; inherited resource/sparse certificates require their own replay")


if __name__ == "__main__":
    main()
