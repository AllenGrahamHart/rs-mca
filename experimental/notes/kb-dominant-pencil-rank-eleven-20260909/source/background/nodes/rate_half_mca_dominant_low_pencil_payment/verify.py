"""Exact grouped-pencil exception prices, using the frozen supplier envelope."""

import hashlib
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

NODE = Path(__file__).resolve().parent
SUPPLIER = NODE.parent/"rate_half_mca_low_pair_pencil_payment"
PIN = "d5515bb34f6afa52fe67b616d18967af292fbe16a64b3eecbf032ffa7009b31d"
A, LO, HI, OWNER = 67471, 9965, 21499, 981106
BUDGET, SMALL, NONCONSTANT = 274980728111395087, 274138707278280353, 254037905932250471
BOX_TOTALS = (254493279590417819, 262886297505008376)


def need(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    spec = importlib.util.spec_from_file_location("credited_pencil_envelope", SUPPLIER/"verify.py")
    supplier = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(supplier)
    r0 = supplier.basis()
    path = SUPPLIER/"certificate/manifest.json"
    data = path.read_bytes()
    need(hashlib.sha256(data).hexdigest() == PIN, "credited manifest pin")
    manifest = json.loads(data)
    need(manifest["complete"] and manifest["metadata"] == supplier.metadata(r0), "complete resource custody")
    e0, top = (A*A-1)//(HI-1), (A*A-1)//(LO-1)
    need((1048576+LO)*(LO-1) > A*A, "empty pencil cannot satisfy the gate")
    need((e0, top) == (211756, 456878), "integer positive-gate endpoints")
    denominator = A*A-e0*(HI-1)
    exception = F(e0*(A-HI+1), denominator)
    need(denominator == 5353 and int(exception) == 1818617, "worst small-complement Johnson floor")
    need(exception.numerator == 9735058588, "printed Johnson numerator")
    need(A*A-(e0+1)*(HI-1) < 0 and A*A-(top+1)*(LO-1) < 0, "strict gate boundaries")
    need(274136923022229951+OWNER*int(exception) == SMALL, "small-complement total")
    off = top*(A-LO+1)
    need(off == 26273683146 and 228260637755610995+OWNER*off == NONCONSTANT,
         "all-height positive-integer-denominator bound")
    need(top < 1048576-67472 and A-HI+1 > 0, "union-size and numerator gates")
    outside = json.loads((NODE/"outside_list_caps.json").read_bytes())
    need(outside["schema"] == "dominant-pencil-outside-list-v1", "outside certificate schema")
    inputs = ((400000, A, 3146811647), (500000, A, 54886611863), (250000, 45973, 14781874200))
    compiler = supplier.module("outside_joint_list", supplier.COMPILER)
    need(len(outside["caps"]) == len(inputs), "three fixed outside certificates")
    for row, (e, agreement, value) in zip(outside["caps"], inputs):
        need((row["e"], row["A"], row["K_max"], row["dimension"], row["cap"])
             == (e, agreement, HI, 11, value), "outside inputs and stated cap")
        need(1 <= agreement-HI <= e-HI and 2130706433**6 >= e, "shared-carrier compiler gates")
        cap, trace = compiler.compile_cap(e-HI, agreement-HI, HI, 11)
        need(cap == value and row["trace"] == [list(step) for step in trace], "outside exact chosen transitions")
    nc_list = 228260637755610995+OWNER*inputs[2][2]
    need(nc_list == 242763223224476195, "any-direction bounded complement price")
    intervals = ((211757, 400000, inputs[0][2]), (400001, 500000, inputs[1][2]))
    maxima, owners, counts = [F(0), F(0)], [None, None], [0, 0]
    rows, size = 0, 0
    for shard in manifest["shards"]:
        block = (path.parent/shard["path"]).read_bytes()
        need(hashlib.sha256(block).hexdigest() == shard["sha256"] and len(block) == shard["bytes"], "shard custody")
        lines = block.splitlines()
        need(len(lines) == shard["records"], "shard row count")
        size += len(block)
        for line in lines:
            row = json.loads(line)
            left, right = row["a"], row["b"]
            need(left == rows*1000 and right == min(left+999, 981104), "complete adjacent boxes")
            rows += 1
            for i, (lower, upper, cap) in enumerate(intervals):
                if right < lower or left > upper:
                    continue
                value = supplier.envelope(row, r0)+OWNER*cap
                counts[i] += 1
                if value > maxima[i]:
                    maxima[i], owners[i] = value, (left, right)
    need((rows, size) == (982, 352246) and counts == [190, 101], "complete inherited and new interval coverage")
    totals = tuple(supplier.ceil(value) for value in maxima)
    need(totals == BOX_TOTALS and owners == [(211000, 211999), (400000, 400999)], "exact larger-complement maxima")
    need(max(SMALL, *totals, NONCONSTANT, nc_list) == SMALL < BUDGET
         and BUDGET-SMALL == 842020833114734, "whole-source alternative maximum")
    roots = tuple(1048576+j-500001 for j in (LO, HI))
    need(roots == (558540, 570074), "constant-pencil survivor ceilings")
    print("PASS positive-gate integer bounds; small Johnson ratio", exception)
    print("PASS 33 shared-carrier LIST transitions and 190/101 inherited-envelope branch boxes", totals)
    print("PAY", SMALL, "RESERVE", BUDGET-SMALL, "NONCONSTANT", NONCONSTANT)
    print("No all-low-pairs-on-pencil premise; J interval and both Prizes remain open")


if __name__ == "__main__":
    main()
