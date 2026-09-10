"""Eleven nonconstant pencil gates and the original raw-two rank-sixteen price."""

import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from math import prod
from pathlib import Path

NODE = Path(__file__).resolve().parent
R, D, END, NEAR = 1048576, 67472, 21499, 134944
BUDGET, W9, OLD_W = 274980728111395087, 578501226347492453, 624373932788019251
CONSTANT, P = 261996525491320703, F(35, 4)
PARAMETERS = dict(R=R, d=D, J_min=9965, J_max=END, pair_cutoff=2,
                  union_cutoff=43, rank=16, section_ratio=[35, 4],
                  mass_truncation=9, mass_bound=W9, near=NEAR,
                  constant_complement=567500, height_width=2000)


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
    compiler = NODE.parent/"list_padded_johnson_dimension_descent/compiler.py"
    compile_cap = load("raw_two_list", compiler).compile_cap
    resource = load("raw_two_mass", NODE.parent/"rate_half_mca_min_envelope_raw_mass/verify.py")
    beta = resource.beta(resource.envelope(9), 9, 9941)
    need(int(F(prod(R+9941-i for i in range(12)))/beta) == W9, "new source resource")
    base = F(OLD_W, 44)+R+END+NEAR+F(43, 44)*F((R+1)**11*10**10, 11**11*(D-42)**10)
    need(ceiling(base) == 43891123512334720, "inherited unrefunded ON envelope")
    bands = []
    for ell in range(1, END, 2000):
        high = min(ell+1999, END-1)
        gate = ceiling(F(4*R-35*(D-1)-31*ell, 4))
        r, w = gate-END, D-42-high-END
        need(1 <= w <= r and END >= 11 and 2130706433**6 >= r+END, "joint LIST gates")
        cap, trace = compile_cap(r, w, END, 11)
        price = ceiling(base+F(43, 44)*(R-D+43)*cap)
        need(R-gate > D-1 and F(R-gate+ell, D-1+ell) <= P, "uniform hereditary P2 ratio")
        bands.append(dict(low=ell, high=high, gate=gate,
                          off=[list(step) for step in trace], ceiling=price))
    nonconstant = max(row["ceiling"] for row in bands)
    need(len(bands) == 11 and sum(len(row["off"]) for row in bands) == 121,
         "eleven complete height bands")
    need(nonconstant == 220845070943887497 < CONSTANT, "all nonconstant source classes paid")
    C, H = F(R-567500, D-1), F(R-END+2, D-END)
    need(1 <= C <= P and H <= P*P, "hereditary determinant gate")
    need(C**6 > H*P**4, "constant equality terminal dominates")
    for i in range(5):
        r, s = 16-2*i, 11-i
        need(s < r <= 2*s and D-2+r-s > 0, "guarded joint anchor")
    count = C**6*prod(F(R+c, D-2+c) for c in range(1, 6))
    need(int(count) == 119106357701 and (16-10, 11-5) == (6, 6), "pair cap and equality child")
    price = int(F(W9, 3)+F(2, 3)*(R-D+2)*count)+NEAR
    need(price == 270737716902276994 and max(CONSTANT, nonconstant, price) == price,
         "complete original source price")
    need(W9//3+NEAR <= price < BUDGET and 2130706433**6//2**128 == BUDGET,
         "empty family and original field")
    return dict(schema="raw-two-pair-rank-sixteen-v1", parameters=PARAMETERS,
                compiler_sha256=hashlib.sha256(compiler.read_bytes()).hexdigest(),
                bands=bands, nonconstant_max=nonconstant, pair_floor=int(count),
                total=price, reserve=BUDGET-price, list_steps=121)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result, path = build(), NODE/"certificate.json"
    if args.write:
        need(not path.exists(), "refuse certificate replacement")
        path.write_text(json.dumps(result, indent=2)+"\n")
        print("FROZEN", hashlib.sha256(path.read_bytes()).hexdigest(), "bytes", path.stat().st_size)
    need(json.loads(path.read_text()) == result, "full frozen certificate")
    print("PASS 11 height bands, 121 LIST transitions, constant-dominant 6/6 terminal")
    print("P2 RANK16 TOTAL", result["total"], "RESERVE", result["reserve"])
    print("Actual P2 rank>=17 remains; its generic projection is not proved full here")


if __name__ == "__main__":
    main()
