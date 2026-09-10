"""Small exact LIST certificates for original HIGH44 pencil-union payments."""

import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from math import prod
from pathlib import Path

NODE = Path(__file__).resolve().parent
R, D, LO, END, W = 1048576, 67472, 9965, 21499, 624373932788019251
BUDGET, NEAR, STOP = 274980728111395087, 134944, 567500
PARAMETERS = dict(R=R, d=D, J_min=LO, J_max=END, source_cutoff=125,
                  mass_truncation=44, pair_cutoff=43, constant_gate=STOP,
                  constant_width=25000, height_width=2000)


def need(ok, message):
    if not ok:
        raise ValueError(message)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def ceiling(value):
    return -(-value.numerator//value.denominator)


def build():
    compiler_path = NODE.parent/"list_padded_johnson_dimension_descent/compiler.py"
    compile_cap = load("pencil_list_compiler", compiler_path).compile_cap
    a, b, c = load("original_filtration", NODE.parent/"rate_half_mca_low_raw_rank_filtration/verify.py").ladder()
    q = lambda j: a+b*j+c*j*j
    beta = lambda j: 12*prod(D-125+i for i in range(1, 11))*q(j)
    n, m = R+LO, D+LO
    universe = prod(n-i for i in range(12))
    ratio = F(universe)/beta(LO)
    need(int(ratio) == 623622665753560212 and ratio.denominator > 1, "unrounded original resource")
    need((b+2*c*LO)*(n-11) > 12*q(END), "whole-J resource monotonicity")
    need(126*(D+END)*prod(D+i for i in range(1, 11)) >= 4*beta(END), "inherited HIGH gate")

    def cap(r, w, k, dim):
        need(1 <= w <= r and dim <= k and 2130706433**6 >= r+k, "LIST scope")
        upper, trace = compile_cap(r, w, k, dim)
        return upper, [list(step) for step in trace]

    boxes = []
    for low in range(0, STOP+1, 25000):
        high = min(low+24999, STOP)
        on, on_trace = cap(R-low, D-43, END-1, 10)
        off, off_trace = (0, []) if high < D-42 else cap(high-END, D-42-END, END, 11)
        value = 1+NEAR+ratio/44*(1-F(prod(n-high-i for i in range(12)), universe))
        value += F(43, 44)*high*(n-low)*on/(m-43)
        value += F(43, 44)*(R-D+43)*off
        boxes.append(dict(a=low, b=high, on=on_trace, off=off_trace, ceiling=ceiling(value)))
    base = F(W, 44)+R+END+NEAR+F(43, 44)*F((R+1)**11*10**10, 11**11*(D-42)**10)
    bands = []
    for low in range(1, END, 2000):
        high, gate = min(low+1999, END-1), 441382-8*low
        off, trace = cap(gate-END, D-42-high-END, END, 11)
        value = base+F(43, 44)*(R-D+43)*off
        bands.append(dict(low=low, high=high, gate=gate, off=trace, ceiling=ceiling(value)))
    constant, nonconstant = max(row["ceiling"] for row in boxes), max(row["ceiling"] for row in bands)
    need(constant == 261996525491320703 and nonconstant == 110665369786278512, "source prices")
    need(max(constant, nonconstant) < BUDGET, "whole-source alternatives below budget")
    need(F(R-STOP, D-42) <= 9, "C_t <= P_t for the entire t1..43 range")
    for t in (7, 23):
        C, P = F(R-STOP, D+1-t), max(F(9), F(607203, 67474-t))
        need(1 <= C <= P, "hereditary scalar ratios")
        for row in bands:
            ell = row["low"]
            need(F(R-row["gate"]+ell, D+1-t+ell) <= P, "height-band endpoint")
    steps = sum(len(row["on"])+len(row["off"]) for row in boxes)+sum(len(row["off"]) for row in bands)
    need((len(boxes), len(bands), steps) == (23, 11, 582), "bounded certificate inventory")
    return dict(schema="high44-pencil-union-v1", parameters=PARAMETERS,
                compiler_sha256=hashlib.sha256(compiler_path.read_bytes()).hexdigest(),
                resource_at_9965=[str(ratio.numerator), str(ratio.denominator)],
                nonconstant_base_ceiling=ceiling(base), constant=boxes, nonconstant=bands,
                maximum=constant, reserve=BUDGET-constant, list_steps=steps)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = build()
    path = NODE/"certificate.json"
    if args.write:
        need(not path.exists(), "refuse to replace a frozen certificate")
        path.write_text(json.dumps(result, indent=2)+"\n")
        print("FROZEN", hashlib.sha256(path.read_bytes()).hexdigest(), "bytes", path.stat().st_size)
    need(json.loads(path.read_text()) == result, "complete independently replayable certificate")
    print("PASS 23 constant boxes; 11 height bands; 582 LIST transitions; exact original refund")
    print("MAXIMUM", result["maximum"], "RESERVE", result["reserve"])
    print("Complete P43 unions and original HIGH44; source ownership remains a hand-proof input")


if __name__ == "__main__":
    main()
