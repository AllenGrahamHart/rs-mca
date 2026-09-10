"""Bounded exact certificates for coupled weighted pair-rank terminals."""

import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from math import prod
from pathlib import Path

NODE = Path(__file__).resolve().parent
R, D, LOW, END = 1048576, 67472, 9965, 21499
S, NEAR, BUDGET = R+1, 134944, 274980728111395087
PENCIL_BUDGET, ZMAX = 270000000000000000, 481076
W44 = 581590844909990298


def need(ok, message):
    if not ok:
        raise ValueError(message)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def ceil(value):
    return -(-value.numerator//value.denominator)


def pair(value):
    value = F(value)
    return [str(value.numerator), str(value.denominator)]


def build():
    compiler = load("coupled_list", NODE.parent/"list_padded_johnson_dimension_descent/compiler.py")
    resource = load("coupled_mass", NODE.parent/"rate_half_mca_min_envelope_raw_mass/verify.py")
    branches = resource.envelope(9)

    def list_cap(r, w, degree, dimension):
        need(1 <= w <= r and 0 <= dimension <= degree and 2130706433**6 >= r+degree,
             "original-field padded LIST gates")
        cap, trace = compiler.compile_cap(r, w, degree, dimension)
        return cap, [list(step) for step in trace]

    base = F(W44, 44)+R+END+NEAR+F(43, 44)*F(S**11*10**10, 11**11*(D-42)**10)
    bands = []
    for low in range(1, END, 200):
        high = min(low+199, END-1)
        left, right = 250000, 650000
        while right-left > 1:
            middle = (left+right)//2
            cap, _ = list_cap(middle-END, D-42-high-END, END, 11)
            if base+F(43, 44)*(R-D+43)*cap <= PENCIL_BUDGET:
                left = middle
            else:
                right = middle
        cap, trace = list_cap(left-END, D-42-high-END, END, 11)
        price = ceil(base+F(43, 44)*(R-D+43)*cap)
        need(price <= PENCIL_BUDGET < BUDGET, "chosen gate is paid; no optimality assertion")
        bands.append(dict(low=low, high=high, gate=left, trace=trace, price=price))
    need(len(bands) == 108, "complete primitive-height coverage")

    constants, nonconstants = {}, {}
    for t in (1, 2):
        for v in range(1, 6):
            e = max(F(567501), F(S, v+1))
            need(e <= R-D+t, "constant maximum in populated-core interval")
            constants[t, v] = t+e*((S-e)/(D+1-t))**v
            values = []
            for row in bands:
                h, emin = row["low"], row["gate"]+1
                e = max(F(emin), F(S+h, v+1))
                need(e <= R-D+t and R-D+t >= emin, "nonconstant peak in allowed interval")
                values.append(t*(R+END-emin)+e*((S+h-e)/(D+1-t+h))**v)
            nonconstants[t, v] = max(values)
    gates = dict(schema="coupled-pencil-gates-v1", source_W44=W44, budget=PENCIL_BUDGET,
                 bands=bands, constants={f"{t},{v}": pair(x) for (t, v), x in constants.items()},
                 nonconstants={f"{t},{v}": pair(x) for (t, v), x in nonconstants.items()})

    compression, terminal = [], {}
    for rank, dimension in ((17, 6), (18, 5), (18, 4)):
        anchors = rank-12
        for t in (1, 2):
            rows, ratios = [], []
            for low in range(D+1-t, ZMAX+1, 10000):
                high = min(low+9999, ZMAX)
                cap, trace = list_cap(high-1, D-t, END-anchors, dimension)
                ratio = F((S-low)*cap, low)
                rows.append(dict(low=low, high=high, trace=trace, ratio=pair(ratio)))
                ratios.append(ratio)
            total = t+S*max(ratios)
            terminal[rank, dimension, t] = total
            compression.append(dict(rank=rank, scalar_dimension=dimension, cutoff=t,
                                    boxes=rows, terminal=pair(total)))
    compression_data = dict(schema="coupled-compression-boxes-v1", z_max=ZMAX, rows=compression)

    def H(anchors, t, j):
        need(D-j+anchors+2-t > 0 and R > D-t, "positive increasing determinant factor")
        return F(R-j+anchors+2, D-j+anchors+2-t)

    def general(v, anchors, t, j):
        if v == 0:
            return F(R-D+t)
        one = max(constants[t, v], nonconstants[t, v])
        if v == 1:
            return one
        return max(one, H(anchors, t, j)*general(v-2, anchors+1, t, j))

    def sparse(rank, t, j):
        anchors, shared = rank-12, 23-rank
        rank_two = H(anchors+1, t, j)*general(shared-3, anchors+2, t, j)
        constant = constants[t, shared-1]
        exceptional = 2*(j-anchors)-2
        need(0 <= exceptional <= S, "sparse good-coordinate cap")
        return (S*rank_two+exceptional*max(0, constant-rank_two))/(D+1-t)

    products = {}
    for rank in (17, 18):
        count = rank-12
        for i in range(count):
            r, s = rank-2*i, 11-i
            need(s < r <= 2*s, "guarded weighted shared-carrier stage")
        need(rank-2*count == 12-count and 11-count == 23-rank, "s+1/s terminal")
        for t in (1, 2):
            products[rank, t] = prod(F(R+c, D-t+c) for c in range(2, rank-10))

    boxes = []
    for low in range(LOW, END+1, 200):
        high = min(low+199, END)
        mass = int(F(prod(R+low-i for i in range(12)))/resource.beta(branches, 9, low))
        record = dict(low=low, high=high, mass_floor=mass)
        for rank, kind in ((17, "full17"), (18, "sparse18"), (18, "no_primitive18"), (18, "full18")):
            parts = []
            for t in (1, 2):
                cap = sparse(rank, t, high)
                if kind != "sparse18":
                    dimension = 4 if kind == "no_primitive18" else 23-rank
                    cap = max(cap, terminal[rank, dimension, t])
                parts.append(products[rank, t]*cap)
            record[kind] = int(F(mass, 3)+parts[0]/2+parts[1]/6)+NEAR
        boxes.append(record)
    maxima = {key: max(row[key] for row in boxes)
              for key in ("full17", "sparse18", "no_primitive18", "full18")}
    need(maxima["full17"] < BUDGET and maxima["no_primitive18"] < BUDGET,
         "complete low-rank and sparse/proper-compression cases are paid")
    paid_tail = next(row["low"] for row in boxes
                     if all(later["full18"] < BUDGET for later in boxes if later["low"] >= row["low"]))
    source = dict(schema="coupled-original-source-boxes-v1", J=[LOW, END], near=NEAR,
                  budget=BUDGET, boxes=boxes, maxima=maxima, full18_paid_tail=paid_tail)
    return {"gate_certificate.json": gates, "compression_certificate.json": compression_data,
            "source_certificate.json": source}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    certificates = build()
    for filename, data in certificates.items():
        path = NODE/filename
        if args.write:
            need(not path.exists(), "refuse certificate replacement")
            path.write_text(json.dumps(data, indent=2)+"\n")
        need(json.loads(path.read_text()) == data, "frozen exact certificate")
        print("PASS", filename, path.stat().st_size, hashlib.sha256(path.read_bytes()).hexdigest())
    print("SOURCE MAXIMA", certificates["source_certificate.json"]["maxima"])
    print("FULL RANK18 PAID TAIL", certificates["source_certificate.json"]["full18_paid_tail"])
    print("Arithmetic only; geometry and original ownership use the listed hand proofs")


if __name__ == "__main__":
    main()
