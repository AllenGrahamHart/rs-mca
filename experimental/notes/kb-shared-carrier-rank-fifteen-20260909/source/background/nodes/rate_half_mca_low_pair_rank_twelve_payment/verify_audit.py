"""Independent integer reconstruction; no primary or compiler imports."""

import copy
import hashlib
import json
from pathlib import Path

NODE = Path(__file__).resolve().parent


def need(ok, message):
    if not ok:
        raise ValueError(message)


def outside_certificate(data):
    need(data["schema"] == "rank-twelve-nonconstant-pencil-outside-list-v1", "schema")
    need(tuple(data[key] for key in ("e", "A", "K_max", "dimension", "cap"))
         == (272000, 45973, 21499, 11, 45437954634), "fixed scope")
    r, w, k = 250501, 24474, 21499
    need(1 <= w <= r and 11 <= k and 2130706433**6 >= r+k, "LIST gates")
    need(len(data["trace"]) == 11, "complete trace")
    upper = 1
    for rank, step in enumerate(data["trace"], 1):
        need(len(step) == 3 and all(type(x) is int for x in step), "integer step")
        s, degree, value = step
        need(s == rank and 0 <= degree <= k, "transition identity")
        if degree == 0:
            expected = (r+s)*upper//(w+s)
        else:
            divisor = (w+degree)**2-(r+degree)*(degree-1)
            need(divisor > 0, "positive Johnson gate")
            expected = (r+degree)*(w+1)//divisor
            if degree < k:
                expected = max(expected, (r+degree+1)*upper//(w+degree+1))
        need(value == expected, "exact legal transition")
        upper = value
    need(upper == data["cap"], "final cap")
    return upper


def mutation_controls(data):
    cases = []
    for key, value in (("schema", "wrong"), ("e", 272001), ("A", 45972),
                       ("K_max", 21500), ("dimension", 10), ("cap", 0)):
        bad = copy.deepcopy(data)
        bad[key] = value
        cases.append(bad)
    for index, value in ((0, 0), (1, 21499), (2, 0)):
        bad = copy.deepcopy(data)
        bad["trace"][0][index] = value
        cases.append(bad)
    for mutation in ("missing", "duplicate", "boolean"):
        bad = copy.deepcopy(data)
        if mutation == "missing":
            bad["trace"].pop()
        elif mutation == "duplicate":
            bad["trace"].append(bad["trace"][-1])
        else:
            bad["trace"][0][0] = True
        cases.append(bad)
    for bad in cases:
        try:
            outside_certificate(bad)
        except ValueError:
            continue
        raise ValueError("accepted malformed certificate")
    return len(cases)


def main():
    data = json.loads((NODE/"outside_list_cap.json").read_bytes())
    off = outside_certificate(data)
    extension = 228260637755610995+981106*off
    need(extension == 272840087674756199, "off-pencil original-label projection")
    old = NODE.parent/"rate_half_mca_low_pair_pencil_payment/certificate/manifest.json"
    raw = old.read_bytes()
    need(hashlib.sha256(raw).hexdigest()
         == "d5515bb34f6afa52fe67b616d18967af292fbe16a64b3eecbf032ffa7009b31d", "inherited resource pin")
    rn, rd = map(int, json.loads(raw)["metadata"]["R0"])
    w3 = rn//rd
    need(w3 == 613022127444579907 and rn % rd != 0, "integer mass, not a floored refund")
    terms, floors = [], []
    for t in (1, 2):
        cn, cd, pn, pd = 548576, 67473-t, 776577, 67474-t
        hn, hd, qn, qd = 1027079, 45975-t, 1048577, 67473-t
        need(1 <= cd <= cn and cn*pd <= pn*cd and 776576 > cd, "scalar and height gates")
        need(hd > 0 and qd > 0 and 981104+t > 0, "uniform denominator monotonicity")
        need(hn*pd**2 <= hd*pn**2, "H<=P squared")
        need(cn**10*hd*pd**8 <= hn*pn**8*cd**10, "constant child <=rank-two child cap")
        pair_num, pair_den = qn*hn*pn**8, qd*hd*pd**8
        floors.append(pair_num//pair_den)
        terms.append(((981104+t)*pair_num, t*(t+1)*pair_den))
    (n1, d1), (n2, d2) = terms
    denominator = 3*d1*d2
    numerator = w3*d1*d2+3*n1*d2+3*n2*d1
    branch = numerator//denominator+134944
    need(floors == [106906553861, 106923140583], "pair floors")
    need(branch == 274267808872348771 and numerator % denominator != 0, "single-denominator price")
    total = max(branch, extension, 274138707278280353)
    need(total == branch and 274980728111395087-total == 712919239046316, "whole-source maximum and reserve")
    print("PASS eleven independently reconstructed LIST steps;", mutation_controls(data), "corrupted certificates rejected")
    print("PASS integer hereditary child gates and original-label denominator; pair floors", floors)
    print("PAY", total, "RESERVE", 274980728111395087-total, "EXTENSION", extension)
    print("No primary/compiler imports; shared-rank and source theorems require their hand proofs")


if __name__ == "__main__":
    main()
