"""Exact weighted exception, inherited-box and rank-fifteen checks."""

import hashlib
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

NODE = Path(__file__).resolve().parent
PIN = "d5515bb34f6afa52fe67b616d18967af292fbe16a64b3eecbf032ffa7009b31d"


def need(ok, message):
    if not ok:
        raise ValueError(message)


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def owner_controls():
    checked = 0
    for gap in range(13):
        for c in (1, 2):
            capacity = gap+c
            for one in range(capacity+1):
                for two in range(capacity//2+1):
                    if one+2*two > capacity or (c == 2 and one):
                        continue
                    need(2*one+two <= 2*(gap+1), "weighted complete-core owner bound")
                    checked += 1
        need(2*(gap+1) > gap+1, "deficit units are not label units")
    need(2*2 > 2*(0+1), "allowing raw1 when c=2 breaks the bound")
    need(2*981105 == 3*654070 and F(981106, 6) < 654070, "two actual core classes")
    return checked


def main():
    supplier = module("credited_pencil", NODE.parent/"rate_half_mca_low_pair_pencil_payment/verify.py")
    compiler = module("credited_list", supplier.COMPILER)
    r0 = supplier.basis()
    raw = supplier.MANIFEST.read_bytes()
    need(hashlib.sha256(raw).hexdigest() == PIN, "unchanged inherited certificate")
    manifest = json.loads(raw)
    need(manifest["complete"] and manifest["metadata"] == supplier.metadata(r0), "complete original resource")
    data = json.loads((NODE/"outside_list_cap.json").read_bytes())
    need(data["schema"] == "rank-fifteen-constant-pencil-outside-list-v1", "schema")
    need(tuple(data[k] for k in ("e", "A", "K_max", "dimension", "cap"))
         == (520000, 67471, 21499, 11, 85934633384), "outside input")
    cap, trace = compiler.compile_cap(498501, 45972, 21499, 11)
    need(cap == data["cap"] and [list(x) for x in trace] == data["trace"], "eleven chosen steps")
    need(1 <= 45972 <= 498501 and 2130706433**6 >= 520000, "padding gates")
    maximum, where, count, rows = F(0), None, 0, 0
    for shard in manifest["shards"]:
        block = (supplier.MANIFEST.parent/shard["path"]).read_bytes()
        need(hashlib.sha256(block).hexdigest() == shard["sha256"] and len(block) == shard["bytes"], "shard custody")
        for line in block.splitlines():
            row = json.loads(line)
            need(row["a"] == rows*1000 and row["b"] == min(rows*1000+999, 981104), "old box coverage")
            rows += 1
            if row["b"] < 500001 or row["a"] > 520000:
                continue
            value = supplier.envelope(row, r0)+654070*cap
            count += 1
            if value > maximum:
                maximum, where = value, (row["a"], row["b"])
    constant = supplier.ceil(maximum)
    need(rows == 982 and count == 21 and where == (500000, 500999), "complete new interval")
    need(constant == 261389606553601974, "weighted constant-pencil branch")
    value, floors = F(int(r0), 3), []
    for t in (1, 2):
        c, p, h = F(528576, 67473-t), F(781095, 85474-t), F(1027079, 45975-t)
        need(1 <= c <= p and h <= p*p and h*p**5 <= c**7, "hereditary and both child gates")
        q = F(1)
        for r, s in ((15, 11), (13, 10), (11, 9), (9, 8)):
            excess = r-s
            need(excess > 0 and 67472-t+excess > 0, "four anchor gates")
            q *= F(1048576+excess, 67472-t+excess)
        bound = q*c**7
        floors.append(int(bound))
        value += F(981104+t, t*(t+1))*bound
    branch = int(value)+134944
    need(floors == [105622838829, 105640059975] and branch == 273428272906977732, "four-anchor price")
    total = max(constant, branch, 274138707278280353)
    need(total == 274138707278280353 and 274980728111395087-total == 842020833114734, "whole-source maximum")
    print("PASS", owner_controls(), "weighted owner controls; eleven LIST steps and 21 inherited boxes")
    print("CONSTANT", constant, "AT", where, "PAIR FLOORS", floors)
    print("RANK<=15 PAY", total, "RESERVE", 274980728111395087-total, "BRANCH", branch)
    print("The charge654070 is a deficit bound, not a label-count bound")


if __name__ == "__main__":
    main()
