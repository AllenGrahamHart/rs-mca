"""Independent integer height profile and price, with malformed-input controls."""

import copy
import hashlib
import json
from math import prod
from pathlib import Path

NODE = Path(__file__).resolve().parent


def need(ok, message):
    if not ok:
        raise ValueError(message)


def profile(data):
    need(data["schema"] == "rank-fourteen-height-band-outside-list-v1", "schema")
    need(len(data["bands"]) == 11, "complete band count")
    maximum, previous = 0, 0
    attained = [False, False]
    for lo, row in zip(range(1, 21499, 2000), data["bands"]):
        hi = min(lo+1999, 21498)
        e, a = 272000+9*(21498-hi), 67471-hi
        need(tuple(row[k] for k in ("h_min", "h_max", "e", "A", "K_max", "dimension"))
             == (lo, hi, e, a, 21499, 11), "opposite height endpoints and exact inputs")
        need(lo == previous+1, "no missing or overlapping heights")
        previous = hi
        r, w, k = e-21499, a-21499, 21499
        need(1 <= w <= r and 2130706433**6 >= e, "LIST padding gates")
        need(len(row["trace"]) == 11, "complete carrier descent")
        upper = 1
        for rank, step in enumerate(row["trace"], 1):
            need(len(step) == 3 and all(type(v) is int for v in step), "integer step")
            s, degree, value = step
            need(s == rank and 0 <= degree <= k, "transition identity")
            if degree == 0:
                bound = (r+s)*upper//(w+s)
            else:
                denominator = (w+degree)**2-(r+degree)*(degree-1)
                need(denominator > 0, "positive Johnson gate")
                bound = (r+degree)*(w+1)//denominator
                if degree < k:
                    bound = max(bound, (r+degree+1)*upper//(w+degree+1))
            need(value == bound, "legal exact transition")
            upper = value
        need(upper == row["cap"], "final pair cap")
        maximum = max(maximum, 228260637755610995+981106*upper)
        for t in (1, 2):
            need(1048576-e > 67473-t, "decreasing height ratio")
            left = (1048576-e+lo)*(85474-t)
            right = 781095*(67473-t+lo)
            need(left <= right, "uniform hereditary ratio")
            attained[t-1] |= left == right
    need(previous == 21498 and all(attained), "exhaustive height interval and attained maxima")
    need(maximum == 272840087674756199, "maximum original-source band price")
    return maximum


def mutations(data):
    cases = []
    for key, value in (("h_min", 2), ("h_max", 1999), ("e", 447483),
                       ("A", 67471), ("K_max", 21500), ("dimension", 12), ("cap", 0)):
        bad = copy.deepcopy(data)
        bad["bands"][0][key] = value
        cases.append(bad)
    for index, value in ((0, True), (1, 21499), (2, 0)):
        bad = copy.deepcopy(data)
        bad["bands"][0]["trace"][0][index] = value
        cases.append(bad)
    for kind in ("schema", "missing_band", "missing_step"):
        bad = copy.deepcopy(data)
        if kind == "schema":
            bad["schema"] = "wrong"
        elif kind == "missing_band":
            bad["bands"].pop()
        else:
            bad["bands"][0]["trace"].pop()
        cases.append(bad)
    for bad in cases:
        try:
            profile(bad)
        except ValueError:
            continue
        raise ValueError("accepted malformed height profile")
    return len(cases)


def main():
    data = json.loads((NODE/"height_caps.json").read_bytes())
    maximum = profile(data)
    raw = (NODE.parent/"rate_half_mca_low_pair_pencil_payment/certificate/manifest.json").read_bytes()
    need(hashlib.sha256(raw).hexdigest()
         == "d5515bb34f6afa52fe67b616d18967af292fbe16a64b3eecbf032ffa7009b31d", "original resource pin")
    rn, rd = map(int, json.loads(raw)["metadata"]["R0"])
    w3 = rn//rd
    need(w3 == 613022127444579907 and rn % rd != 0, "unrefunded integer mass")
    terms, floors = [], []
    for t in (1, 2):
        cn, cd, pn, pd, hn, hd = 548576, 67473-t, 781095, 85474-t, 1027079, 45975-t
        need(cd > 0 and hd > 0 and cn*pd <= pn*cd, "positive scalar and anchor gates")
        need(hn*pd**2 <= hd*pn**2, "hereditary H<=P squared")
        need(hn*pn**6*cd**8 <= hd*pd**6*cn**8, "rank-two child <=constant child cap")
        numerator = cn**8*prod(1048576+c for c in (1, 2, 3))
        denominator = cd**8*prod(67472-t+c for c in (1, 2, 3))
        floors.append(numerator//denominator)
        terms.append(((981104+t)*numerator, t*(t+1)*denominator))
    (n1, d1), (n2, d2) = terms
    numerator = w3*d1*d2+3*n1*d2+3*n2*d1
    denominator = 3*d1*d2
    branch = numerator//denominator+134944
    need(floors == [71666785024, 71678469894] and branch == 251217725856263117, "joint-pair and all-raw prices")
    total = max(branch, maximum, 274138707278280353)
    need(total == 274138707278280353 and 274980728111395087-total == 842020833114734, "whole-source maximum")
    print("PASS 121 independent LIST transitions and complete height coverage;", mutations(data), "malformed profiles rejected")
    print("PASS three-anchor integer price and both terminal child gates; pair floors", floors)
    print("PAY", total, "RESERVE", 274980728111395087-total, "BRANCH", branch)
    print("No primary/compiler imports; original-source and auxiliary-space proofs remain required")


if __name__ == "__main__":
    main()
