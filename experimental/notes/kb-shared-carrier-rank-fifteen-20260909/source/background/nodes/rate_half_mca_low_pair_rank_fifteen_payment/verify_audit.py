"""Independent integer proof-certificate checks, without primary/compiler imports."""

import copy
import hashlib
import json
from math import prod
from pathlib import Path

NODE = Path(__file__).resolve().parent


def need(ok, message):
    if not ok:
        raise ValueError(message)


def outside(data):
    need(data["schema"] == "rank-fifteen-constant-pencil-outside-list-v1", "schema")
    need(tuple(data[k] for k in ("e", "A", "K_max", "dimension", "cap"))
         == (520000, 67471, 21499, 11, 85934633384), "fixed input")
    r, w, k, upper = 498501, 45972, 21499, 1
    need(1 <= w <= r and 2130706433**6 >= r+k, "LIST scope")
    need(len(data["trace"]) == 11, "complete trace")
    for rank, step in enumerate(data["trace"], 1):
        need(len(step) == 3 and all(type(x) is int for x in step), "integer step")
        s, degree, value = step
        need(s == rank and 0 <= degree <= k, "transition identity")
        if degree == 0:
            bound = (r+s)*upper//(w+s)
        else:
            divisor = (w+degree)**2-(r+degree)*(degree-1)
            need(divisor > 0, "positive Johnson gate")
            bound = (r+degree)*(w+1)//divisor
            if degree < k:
                bound = max(bound, (r+degree+1)*upper//(w+degree+1))
        need(value == bound, "legal exact step")
        upper = value
    need(upper == data["cap"], "final cap")
    return upper


def mutations(data):
    cases = []
    for key, value in (("schema", "wrong"), ("e", 520001), ("A", 67470),
                       ("K_max", 21500), ("dimension", 10), ("cap", 0)):
        bad = copy.deepcopy(data)
        bad[key] = value
        cases.append(bad)
    for index, value in ((0, True), (1, 21499), (2, 0)):
        bad = copy.deepcopy(data)
        bad["trace"][0][index] = value
        cases.append(bad)
    bad = copy.deepcopy(data)
    bad["trace"].pop()
    cases.append(bad)
    for bad in cases:
        try:
            outside(bad)
        except ValueError:
            continue
        raise ValueError("accepted malformed certificate")
    return len(cases)


def box_fraction(row, rn, rd):
    a, b = row["a"], row["b"]
    n, m = 1058541, 77437
    falling = prod(n-i for i in range(12))
    d0 = 3*rd*falling
    d1, d2 = 2*(m-1), 6*(m-2)
    v1, v2 = (entry["trace"][-1][2] for entry in row["caps"])
    numerator = (134945*d0*d1*d2
                 +rn*(falling-prod(n-b-i for i in range(12)))*d1*d2
                 +b*(n-a)*v1*d0*d2+b*(n-a)*v2*d0*d1)
    return numerator, d0*d1*d2


def main():
    data = json.loads((NODE/"outside_list_cap.json").read_bytes())
    cap = outside(data)
    need(3*654070 == 2*981105 and 981106 < 6*654070, "both complete-core owner classes")
    cert = NODE.parent/"rate_half_mca_low_pair_pencil_payment/certificate"
    raw = (cert/"manifest.json").read_bytes()
    need(hashlib.sha256(raw).hexdigest()
         == "d5515bb34f6afa52fe67b616d18967af292fbe16a64b3eecbf032ffa7009b31d", "original resource custody")
    manifest = json.loads(raw)
    rn, rd = map(int, manifest["metadata"]["R0"])
    need(rn//rd == 613022127444579907 and rn % rd != 0, "unrounded refund resource")
    best, where, selected, rows = (0, 1), None, [], 0
    for shard in manifest["shards"]:
        block = (cert/shard["path"]).read_bytes()
        need(hashlib.sha256(block).hexdigest() == shard["sha256"] and len(block) == shard["bytes"], "old shard hash")
        for line in block.splitlines():
            row = json.loads(line)
            need((row["a"], row["b"]) == (1000*rows, min(1000*rows+999, 981104)), "old box order")
            rows += 1
            if row["b"] < 500001 or row["a"] > 520000:
                continue
            selected.append(row["a"]//1000)
            num, den = box_fraction(row, rn, rd)
            num += 654070*cap*den
            if num*best[1] > best[0]*den:
                best, where = (num, den), (row["a"], row["b"])
    constant = (best[0]+best[1]-1)//best[1]
    need(rows == 982 and selected == list(range(500, 521)), "new interval coverage")
    need(constant == 261389606553601974 and where == (500000, 500999), "independent constant price")
    terms, floors = [], []
    for t in (1, 2):
        cn, cd, pn, pd, hn, hd = 528576, 67473-t, 781095, 85474-t, 1027079, 45975-t
        need(cd > 0 and hd > 0 and cn*pd <= pn*cd, "scalar and denominator gates")
        need(hn*pd**2 <= hd*pn**2 and hn*pn**5*cd**7 <= hd*pd**5*cn**7, "both child gates")
        num = cn**7*prod(1048576+c for c in (1, 2, 3, 4))
        den = cd**7*prod(67472-t+c for c in (1, 2, 3, 4))
        floors.append(num//den)
        terms.append(((981104+t)*num, t*(t+1)*den))
    (n1, d1), (n2, d2) = terms
    branch = ((rn//rd)*d1*d2+3*n1*d2+3*n2*d1)//(3*d1*d2)+134944
    need(floors == [105622838829, 105640059975] and branch == 273428272906977732, "independent rank-fifteen price")
    total = max(branch, constant, 274138707278280353)
    need(total == 274138707278280353 and 274980728111395087-total == 842020833114734, "whole-source maximum")
    print("PASS eleven independent LIST steps,21 exact refund boxes;", mutations(data), "corrupted certificates rejected")
    print("PASS weighted owner and four-anchor gates; CONSTANT", constant, "BRANCH", branch)
    print("PAY", total, "RESERVE", 274980728111395087-total, "PAIR FLOORS", floors)
    print("No primary/compiler imports; source and ownership proofs remain required")


if __name__ == "__main__":
    main()
