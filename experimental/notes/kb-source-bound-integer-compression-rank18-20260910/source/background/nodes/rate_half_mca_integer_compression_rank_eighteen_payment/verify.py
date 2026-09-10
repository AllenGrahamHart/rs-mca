"""Two degree ranges and an integer two-large-fibre compression certificate."""

import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import prod
from pathlib import Path

NODE = Path(__file__).resolve().parent
PARENT = NODE.parent/"rate_half_mca_coupled_pair_rank_frontier"
R, D, END, S = 1048576, 67472, 21499, 1048577
NEAR, BUDGET, T = 134944, 274980728111395087, 349525
GATE_PIN = "7b58ecc95009ca1a680784343b7121c25feca5ed238c3e9797daa381cc637d51"
SOURCE_PIN = "09a677b5f91a9abca6ace7e07dfbf7ab4f386905cec8e3f3551933007b027f68"


def need(ok, why):
    if not ok:
        raise ValueError(why)


def read_pinned(name, pin):
    raw = (PARENT/name).read_bytes()
    need(hashlib.sha256(raw).hexdigest() == pin, "inherited certificate pin")
    return json.loads(raw)


def encode(value):
    return [str(value.numerator), str(value.denominator)]


def decode(value):
    return Q(*map(int, value))


def build():
    gates = read_pinned("gate_certificate.json", GATE_PIN)
    source = read_pinned("source_certificate.json", SOURCE_PIN)
    path = NODE.parent/"list_padded_johnson_dimension_descent/compiler.py"
    spec = importlib.util.spec_from_file_location("integer_fibre_list", path)
    compiler = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(compiler)
    need(3*(T+1) == S+1 and S//3 == T, "at most TWO large integer masses")
    cases, bounds = [], {}
    for low_j, high_j in ((9965, 12964), (12965, 14164)):
        degree = high_j-6
        for t in (1, 2):
            small, large = [], []
            for lower, upper, rows in ((D+1-t, T, small), (T+1, 481076, large)):
                for low in range(lower, upper+1, 10000):
                    high = min(low+9999, upper)
                    need(1 <= D-t <= high-1 and degree >= 5 and
                         2130706433**6 >= high-1+degree, "original-field auxiliary LIST")
                    cap, trace = compiler.compile_cap(high-1, D-t, degree, 5)
                    rows.append(dict(low=low, high=high, cap=cap,
                                     trace=[list(step) for step in trace]))
            alpha = max(Q((S-row["low"])*row["cap"], row["low"]) for row in small)
            beta = max([Q(0)]+[Q((S-row["low"])*row["cap"])-alpha*row["low"] for row in large])
            terminal = t+S*alpha+2*beta
            bounds[low_j, t] = terminal
            cases.append(dict(J=[low_j, high_j], cutoff=t, degree_max=degree, scalar_dimension=5,
                              small=small, large=large, alpha=encode(alpha), beta=encode(beta),
                              terminal=encode(terminal)))
    c = {tuple(map(int, key.split(","))): decode(value) for key, value in gates["constants"].items()}
    p = {tuple(map(int, key.split(","))): decode(value) for key, value in gates["nonconstants"].items()}

    def sparse(t, j):
        h = lambda a: Q(R-j+a+2, D-j+a+2-t)
        child = h(7)*max(c[t, 2], p[t, 2], h(8)*(R-D+t))
        return (S*child+(2*j-14)*max(Q(0), c[t, 4]-child))/(D+1-t)

    for t in (1, 2):
        need(bounds[9965, t] <= sparse(t, 9965), "prefix compression dominated by sparse cap")
        need(bounds[12965, t] >= sparse(t, 14164), "middle compression cap dominates all sparse children")
    row = next(row for row in source["boxes"] if row["low"] == 12965)
    masses = [prod(Q(R+c, D-t+c) for c in range(2, 8))*bounds[12965, t] for t in (1, 2)]
    middle = int(Q(row["mass_floor"], 3)+masses[0]/2+masses[1]/6)+NEAR
    prefix = max(row["sparse18"] for row in source["boxes"] if row["high"] <= 12964)
    upper = max(row["full18"] for row in source["boxes"] if row["low"] >= 14165)
    need((prefix, middle, upper) ==
         (274462040894062110, 270702759681887570, 273715780528023745), "three source ranges")
    total = max(270000000000000000, prefix, middle, upper)
    need(total < BUDGET and BUDGET-total == 518687217332977, "entire rank18 source paid")
    rows = sum(len(case["small"])+len(case["large"]) for case in cases)
    steps = sum(len(row["trace"]) for case in cases for side in ("small", "large") for row in case[side])
    need((len(cases), rows, steps) == (4, 172, 860), "bounded compression inventory")
    return dict(schema="integer-compression-rank18-v1",
                parameters=dict(R=R, d=D, source_J=[9965, END], anchors=6, cutoff=[1, 2],
                                x_max=481076, threshold=T, large_count=2, box_width=10000,
                                original_rank=12, pair_rank=18, near=NEAR, B_star=BUDGET),
                inherited_sha256=dict(gates=GATE_PIN, source=SOURCE_PIN),
                compiler_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                cases=cases, middle_mass_floor=row["mass_floor"],
                prefix=prefix, middle=middle, upper=upper, total=total,
                reserve=BUDGET-total, boxes=rows, list_steps=steps)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    data = build()
    path = NODE/"certificate.json"
    if args.write:
        need(not path.exists(), "refuse frozen certificate replacement")
        path.write_text(json.dumps(data, indent=2)+"\n")
    need(json.loads(path.read_text()) == data, "frozen exact certificate")
    print("PASS four degree/cutoff cases;", data["boxes"], "boxes;", data["list_steps"], "LIST transitions")
    print("SOURCE RANGES", data["prefix"], data["middle"], data["upper"], "TOTAL", data["total"])
    print("RESERVE", data["reserve"], "middle original mass floor", data["middle_mass_floor"])
    print("CERTIFICATE", path.stat().st_size, hashlib.sha256(path.read_bytes()).hexdigest())
    print("Arithmetic only; actual fibre packing and original ownership use the hand proof")


if __name__ == "__main__":
    main()
