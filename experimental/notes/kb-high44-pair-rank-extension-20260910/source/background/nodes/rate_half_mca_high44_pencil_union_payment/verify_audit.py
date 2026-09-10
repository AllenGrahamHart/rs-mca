"""Independent polynomial reconstruction and legality audit; no compiler imports."""

import copy
from fractions import Fraction as Q
import hashlib
import json
from math import prod
from pathlib import Path

NODE = Path(__file__).resolve().parent
PIN = "1e699d294491f6c998c0764e111528daeb4e339a6e853323ad2ed05fd422d6ad"
COMPILER = "bac33f24d1f34760518406185fcc9850d4fc61f5441486f94237e13b99eb8ca8"


def need(ok, message):
    if not ok:
        raise ValueError(message)


def add(a, b):
    return [(a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)
            for i in range(max(len(a), len(b)))]


def mul(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def at(a, x):
    value = 0
    for coefficient in reversed(a):
        value = value*x+coefficient
    return value


def substitute(a, linear):
    out, power = [0], [1]
    for coefficient in a:
        out = add(out, [coefficient*x for x in power])
        power = mul(power, linear)
    return out


def resource():
    d, end, x = 67347, 21499, 5000
    q = [v/Q(d+2) for v in mul([d, 1], [d+Q(1, 2), Q(1, 2)])]
    curvature = q[2]
    for rank in range(4, 12):
        h = d+rank-1
        need(q[1] >= d*q[2], "contraction input")
        spike = add(substitute(q, [-1, 1]), [-Q(rank-1, h)*at(q, rank-1), at(q, rank-1)/h])
        equal = [v/h for v in mul([d, 1], substitute(q, [Q(1, rank-1), Q(rank-2, rank-1)]))]
        residual = add(equal, [0, 0, -curvature])
        need(residual[2] >= 0 and residual[3] >= 0, "convex remainder")
        slope = at([i*residual[i] for i in range(1, len(residual))], x)
        tangent = [at(residual, x)-x*slope, slope]
        difference = add(tangent, [-spike[0], -spike[1]])
        shift = max(0, at(difference, rank), at(difference, end))
        q = [tangent[0]-shift, tangent[1], curvature]
        need(min(q) > 0 and q[1] >= d*q[2], "next contraction input")
        expected = add([shift], mul([x*x, -2*x, 1], [residual[2]+2*x*residual[3], residual[3]]))
        need(add(equal, [-v for v in q]) == expected, "squared-remainder identity")
        need(all(at(spike, j) >= at(q, j) for j in (rank, end)), "whole spike interval")
    factor = 12*prod(range(67348, 67358))
    need(67472*q[1] >= q[0], "HIGH ratio monotonicity")
    need(126*(67472+end)*prod(range(67473, 67483)) >= 4*factor*at(q, end), "HIGH126 baseline")
    need((q[1]+2*q[2]*9941)*(1048576+9941-11) > 12*at(q, end), "whole resource interval")
    for j, floor in ((9941, 624373932788019251), (14000, 522680876725222604)):
        value = Q(prod(1048576+j-i for i in range(12)))/(factor*at(q, j))
        need(floor <= value < floor+1, "inherited endpoint floor")
    return Q(prod(1058541-i for i in range(12)))/(factor*at(q, 9965))


def cap(trace, r, w, end, dimension):
    need(1 <= w <= r and dimension <= end and 2130706433**6 >= r+end, "LIST domain and field")
    need(isinstance(trace, list) and len(trace) == dimension, "LIST trace length")
    old = 1
    for rank, row in enumerate(trace, 1):
        need(isinstance(row, list) and len(row) == 3 and all(type(x) is int for x in row), "integer trace")
        actual, degree, bound = row
        need(actual == rank and bound >= 1, "rank and positive cap")
        if degree == 0:
            expected = (r+rank)*old//(w+rank)
        else:
            need(1 <= degree <= end, "degree gate")
            denominator = (w+degree)**2-(r+degree)*(degree-1)
            need(denominator > 0, "Johnson gate")
            expected = (r+degree)*(w+1)//denominator
            if degree < end:
                expected = max(expected, (r+degree+1)*old//(w+degree+1))
        need(bound == expected, "legal exact LIST step")
        old = bound
    return old


def ceil(value):
    return -(-value.numerator//value.denominator)


def validate(data, ratio):
    need(data["schema"] == "high44-pencil-union-v1" and data["compiler_sha256"] == COMPILER, "identity")
    need(data["parameters"] == dict(R=1048576, d=67472, J_min=9965, J_max=21499,
         source_cutoff=125, mass_truncation=44, pair_cutoff=43, constant_gate=567500,
         constant_width=25000, height_width=2000), "original source pins")
    need(data["resource_at_9965"] == [str(ratio.numerator), str(ratio.denominator)], "unfloored resource")
    need(ratio.denominator > 1 and int(ratio) == 623622665753560212, "strict fractional resource")
    boxes, bands = data["constant"], data["nonconstant"]
    need(len(boxes) == 23 and len(bands) == 11, "complete coverage")
    universe, prices, steps = prod(range(1058530, 1058542)), [], 0
    for i, row in enumerate(boxes):
        need(set(row) == {"a", "b", "on", "off", "ceiling"}, "box schema")
        a, b = 25000*i, min(25000*i+24999, 567500)
        need(row["a"] == a and row["b"] == b and b < 981104, "constant coverage and anchor gate")
        on = cap(row["on"], 1048576-a, 67429, 21498, 10)
        if b < 67430:
            need(row["off"] == [], "no off-pair fits")
            off = 0
        else:
            off = cap(row["off"], b-21499, 45931, 21499, 11)
        internal = prod(range(1058541-b-11, 1058541-b+1))
        value = 134945+ratio*(universe-internal)/(44*universe)
        value += Q(43*b*(1058541-a)*on, 44*77394)+Q(43*981147*off, 44)
        need(row["ceiling"] == ceil(value), "original refunded price")
        prices.append(ceil(value))
        steps += len(row["on"])+len(row["off"])
    need(max(prices) == 261996525491320703 and prices[-1] == max(prices), "constant maximum")
    base = Q(624373932788019251, 44)+1205019+Q(43*1048577**11*10**10, 44*11**11*67430**10)
    need(data["nonconstant_base_ceiling"] == ceil(base) == 43891123512334720, "preferred labels and analytic peak")
    prices = []
    for i, row in enumerate(bands):
        need(set(row) == {"low", "high", "gate", "off", "ceiling"}, "height schema")
        low, high = 1+2000*i, min(2000*(i+1), 21498)
        gate = 441382-8*low
        need((row["low"], row["high"], row["gate"]) == (low, high, gate), "complete height bands")
        off = cap(row["off"], gate-21499, 45931-high, 21499, 11)
        value = base+Q(43*981147*off, 44)
        need(row["ceiling"] == ceil(value), "nonconstant whole-source price")
        prices.append(ceil(value))
        steps += len(row["off"])
        for t in (7, 23):
            P = max(Q(9), Q(607203, 67474-t))
            need(Q(1048576-gate+low, 67473-t+low) <= P, "hereditary endpoint")
    need(max(prices) == 110665369786278512 and steps == data["list_steps"] == 582, "nonconstant maximum/inventory")
    need(data["maximum"] == 261996525491320703 and data["reserve"] == 12984202620074384,
         "alternative maximum and reserve")
    need(data["maximum"]+data["reserve"] == 274980728111395087, "original budget")
    need(481076 <= 9*67430, "uniform C_t <= 9 <= P_t on t1..43")


def main():
    raw = (NODE/"certificate.json").read_bytes()
    need(hashlib.sha256(raw).hexdigest() == PIN, "frozen certificate")
    data, ratio = json.loads(raw), resource()
    validate(data, ratio)
    cases = []
    for kind in range(10):
        bad = copy.deepcopy(data)
        if kind == 0: bad["constant"].pop()
        elif kind == 1: bad["nonconstant"].pop()
        elif kind == 2: bad["parameters"]["mass_truncation"] = 43
        elif kind == 3: bad["constant"][0]["b"] += 1
        elif kind == 4: bad["nonconstant"][-1]["high"] += 1
        elif kind == 5: bad["constant"][0]["on"][0][1] = 21499
        elif kind == 6: bad["constant"][2]["off"][-1][2] -= 1
        elif kind == 7: bad["nonconstant"][0]["gate"] += 1
        elif kind == 8: bad["constant"][-1]["ceiling"] -= 1
        else: bad["resource_at_9965"] = [str(int(ratio)), "1"]
        cases.append(bad)
    for bad in cases:
        try:
            validate(bad, ratio)
        except (ValueError, KeyError):
            continue
        raise ValueError("accepted an invalid certificate")
    print("PASS independent eight source-basis identities and 582 chosen LIST steps")
    print("PASS exhaustive 23-box/11-band prices; 10 arithmetic/scope mutations rejected")
    print("No primary/compiler imports; original ownership and universal theorems remain hand-proof inputs")


if __name__ == "__main__":
    main()
