"""Independent polynomial and integer replay of every pencil certificate row."""

import copy
import hashlib
import json
from fractions import Fraction as Q
from math import gcd, lcm, prod
from pathlib import Path

NODE = Path(__file__).resolve().parent
PIN = "d5515bb34f6afa52fe67b616d18967af292fbe16a64b3eecbf032ffa7009b31d"
COMPILER_PIN = "bac33f24d1f34760518406185fcc9850d4fc61f5441486f94237e13b99eb8ca8"


def need(ok, message):
    if not ok:
        raise ValueError(message)


def add(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]


def mul(a,b):
    out = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return out


def at(a,x):
    value = 0
    for coefficient in reversed(a):
        value = value*x+coefficient
    return value


def substitute(a,linear):
    out,power = [0],[1]
    for coefficient in a:
        out = add(out,[coefficient*x for x in power])
        power = mul(power,linear)
    return out


def source_ratio():
    d,end,x = 67456,21499,5000
    q = [v/Q(d+2) for v in mul([d,1],[d+Q(1,2),Q(1,2)])]
    curvature = q[2]
    for rank in range(4,12):
        h = d+rank-1
        need(q[1] >= d*q[2], "input contraction gate")
        spike = add(substitute(q,[-1,1]),[-Q(rank-1,h)*at(q,rank-1),at(q,rank-1)/h])
        equal = [v/h for v in mul([d,1],substitute(q,[Q(1,rank-1),Q(rank-2,rank-1)]))]
        residual = add(equal,[0,0,-curvature])
        need(residual[2] >= 0 and residual[3] >= 0, "convex residual")
        slope = at([i*residual[i] for i in range(1,len(residual))],x)
        tangent = [at(residual,x)-x*slope,slope]
        difference = add(tangent,[-spike[0],-spike[1]])
        shift = max(0,at(difference,rank),at(difference,end))
        q = [tangent[0]-shift,tangent[1],curvature]
        need(min(q) > 0 and q[1] >= d*q[2], "positive next polynomial")
        actual = add(equal,[-v for v in q])
        expected = add([shift],mul([x*x,-2*x,1],[residual[2]+2*x*residual[3],residual[3]]))
        need(actual == expected, "exact squared-remainder polynomial identity")
        need(at(spike,rank) >= at(q,rank) and at(spike,end) >= at(q,end), "whole spike interval")
    scale = lcm(*(v.denominator for v in q))
    polynomial = [int(v*scale) for v in q]
    a,b,c = polynomial
    p,pd = prod(range(67457,67467)),prod(range(67473,67483))
    need(67472*b >= a, "q/(d+J) increasing")
    need((b+2*c*9965)*(1058541-11) > 12*at(polynomial,21499), "whole-J ratio decreasing")
    high = 12*p*at(polynomial,21499)
    need(187*(67472+21499)*pd*scale >= 3*high, "completed HIGH funds every raw at least17")
    need(17*(67472+21499)*pd*scale < 3*high, "baseline HIGH fails this application")
    numerator = prod(range(1058541-11,1058541+1))*scale
    denominator = 12*p*at(polynomial,9965)
    common = gcd(numerator,denominator)
    numerator,denominator = numerator//common,denominator//common
    need(numerator//denominator == 613022127444579907 and denominator > 1, "exact R0")
    return numerator,denominator


def list_cap(trace,r,w):
    need(isinstance(trace,list) and len(trace) == 10, "ten LIST transitions")
    old = 1
    for rank,step in enumerate(trace,1):
        need(isinstance(step,list) and len(step) == 3 and all(type(x) is int for x in step), "integer step")
        actual_rank,degree,claimed = step
        need(actual_rank == rank and claimed >= 1, "rank/cap identity")
        if degree == 0:
            correct = ((r+rank)*old)//(w+rank)
        else:
            need(1 <= degree <= 21498, "padded degree gate")
            denominator = (w+degree)**2-(r+degree)*(degree-1)
            need(denominator > 0, "Johnson denominator")
            correct = (r+degree)*(w+1)//denominator
            if degree < 21498:
                correct = max(correct,(r+degree+1)*old//(w+degree+1))
        need(claimed == correct, "certified transition value")
        old = claimed
    return old


def box(row,index):
    need(set(row) == {"a","b","caps"}, "row schema")
    a,b = row["a"],row["b"]
    need(type(a) is int and type(b) is int and a == 1000*index and b == min(a+999,981104),
         "gap-free exact e interval")
    need(isinstance(row["caps"],list) and len(row["caps"]) == 2, "two exact depths")
    values = []
    for t,entry in enumerate(row["caps"],1):
        need(set(entry) == {"t","trace"} and type(entry["t"]) is int and entry["t"] == t,
             "depth identity")
        need(1 <= 67472-t <= 1048576-a and 2130706433**6 >= 1048576-a+21498,
             "uniform LIST field/corridor gate")
        values.append(list_cap(entry["trace"],1048576-a,67472-t))
    return a,b,values


def mutations(first):
    cases = []
    for key in ("a","b"):
        bad = copy.deepcopy(first)
        bad[key] += 1
        cases.append(bad)
    bad = copy.deepcopy(first)
    bad["caps"].pop()
    cases.append(bad)
    bad = copy.deepcopy(first)
    bad["caps"][0]["t"] = 2
    cases.append(bad)
    bad = copy.deepcopy(first)
    bad["caps"][0]["trace"].pop()
    cases.append(bad)
    for position,value in ((0,11),(1,21499),(2,0)):
        bad = copy.deepcopy(first)
        bad["caps"][0]["trace"][0][position] = value
        cases.append(bad)
    bad = copy.deepcopy(first)
    bad["caps"][1]["trace"][-1][2] -= 1
    cases.append(bad)
    for bad in cases:
        try:
            box(bad,0)
        except (ValueError,KeyError):
            continue
        raise ValueError("accepted a corrupted integer certificate")
    return len(cases)


def main():
    path = NODE/"certificate/manifest.json"
    raw = path.read_bytes()
    need(hashlib.sha256(raw).hexdigest() == PIN, "immutable manifest pin")
    manifest = json.loads(raw)
    need(manifest["schema"] == "prize-sharded-result-v1" and manifest["format"] == "jsonl"
         and manifest["complete"] is True, "complete structured result required")
    rn,rd = source_ratio()
    meta = manifest["metadata"]
    need(meta["R0"] == [str(rn),str(rd)] and meta["compiler_sha256"] == COMPILER_PIN,
         "exact source ratio and selection provenance")
    need(meta["kind"] == "low-pair-pencil-tuple-refund-v1" and meta["claimed_ceiling"] == 274136923022229951,
         "certificate theorem identity")
    need(meta["parameters"] == {"R":1048576,"d":67472,"J_min":9965,"J_max":21499,
         "core_cutoff":16,"mass_truncation":3,"pair_cutoff":2,"width":1000,"dimension":10},
         "exact source parameters")
    need(manifest["total_records"] == 982 and len(manifest["shards"]) == 8, "complete row inventory")
    n,m,near = 1058541,77437,134944
    universe = prod(range(n-11,n+1))
    denominators = (3*rd*universe,2*(m-1),6*(m-2))
    common = lcm(*denominators)
    multipliers = [common//d for d in denominators]
    index,total_bytes,maximum,where,first = 0,0,-1,None,None
    for shard_index,entry in enumerate(manifest["shards"]):
        relative = f"shards/part-{shard_index:05d}.jsonl"
        need(entry["path"] == relative, "canonical ordered shard path")
        shard = path.parent/relative
        need(not shard.is_symlink() and shard.resolve().is_relative_to(path.parent.resolve()), "shard custody")
        digest,count,size = hashlib.sha256(),0,0
        with shard.open("rb") as handle:
            for line in handle:
                digest.update(line)
                size += len(line)
                row = json.loads(line)
                if first is None:
                    first = copy.deepcopy(row)
                a,b,caps = box(row,index)
                inside = prod(range(n-b-11,n-b+1))
                value = (1+near)*common+rn*(universe-inside)*multipliers[0]
                value += b*(n-a)*(caps[0]*multipliers[1]+caps[1]*multipliers[2])
                need(value < 274980728111395087*common, "every refunded box below original budget")
                if value > maximum:
                    maximum,where = value,(a,b)
                index += 1
                count += 1
        need(count == (128 if shard_index < 7 else 86) == entry["records"]
             and size == entry["bytes"] and digest.hexdigest() == entry["sha256"], "shard bytes/hash/count")
        total_bytes += size
    ceiling = -(-maximum//common)
    need(index == 982 and total_bytes == manifest["total_bytes"] == 352246, "entire finite coverage")
    need(ceiling == 274136923022229951 and where == (103000,103999), "independent exact maximum")
    need((ceiling-1)*common < maximum <= ceiling*common, "exact ceiling endpoint")
    need(274980728111395087-ceiling == 843805089165136, "original reserve")
    small = -(-(rn+3*rd*(981106+near))//(3*rd))
    need(small == 204340709149309353 < ceiling and 228260637755610995 < ceiling,
         "small-union and inherited nonconstant cases")
    print("PASS independent eight polynomial identities;19640 legal LIST transitions;982 complete boxes")
    print("PASS eight shard hashes; unrounded resource; maximum",ceiling,"at",where,"SMALL",small)
    print("PASS",mutations(first),"corrupted row/transition mutations rejected; no primary or compiler import")
    print("Universal tuple exclusion, source normalization and ownership still require the hand proofs")


if __name__ == "__main__":
    main()
