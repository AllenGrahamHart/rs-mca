"""Independent legality and expanded terminal audit; no local imports."""

import copy
from fractions import Fraction as Q
import hashlib
import json
from math import comb, prod
from pathlib import Path

NODE = Path(__file__).resolve().parent
R, D, END, S = 1048576, 67472, 21499, 1048577
BUDGET, NEAR = 274980728111395087, 134944
PINS = {
    "gate_certificate.json": "7b58ecc95009ca1a680784343b7121c25feca5ed238c3e9797daa381cc637d51",
    "compression_certificate.json": "19eb68900549c952bf3ad630d70caaf8ae6b9ee6c9560bd573c1b2d920594b77",
    "source_certificate.json": "09a677b5f91a9abca6ace7e07dfbf7ab4f386905cec8e3f3551933007b027f68",
}


def need(ok, why):
    if not ok:
        raise ValueError(why)


def ceiling(x):
    return -(-x.numerator//x.denominator)


def ratio(raw):
    need(type(raw) is list and len(raw) == 2 and all(type(x) is str for x in raw),
         "exact rational encoding")
    value = Q(int(raw[0]), int(raw[1]))
    need(raw == [str(value.numerator), str(value.denominator)], "canonical rational")
    return value


def list_cap(trace, r, w, degree, dimension):
    need(1 <= w <= r and degree >= dimension and 2130706433**6 >= r+degree,
         "LIST scope and source field")
    need(len(trace) == dimension, "all dimension transitions retained")
    previous = 1
    for rank, row in enumerate(trace, 1):
        need(len(row) == 3 and all(type(x) is int for x in row), "integer LIST transition")
        actual, cutoff, answer = row
        need(actual == rank and 0 <= cutoff <= degree, "legal rank and degree")
        if cutoff == 0:
            expected = (r+rank)*previous//(w+rank)
        else:
            denominator = (w+cutoff)**2-(r+cutoff)*(cutoff-1)
            need(denominator > 0, "positive Johnson denominator")
            expected = (r+cutoff)*(w+1)//denominator
            if cutoff < degree:
                expected = max(expected, (r+cutoff+1)*previous//(w+cutoff+1))
        need(answer == expected and answer > 0, "exact chosen-step upper bound")
        previous = answer
    return previous


def gates(data):
    need(set(data) == {"schema", "source_W44", "budget", "bands", "constants", "nonconstants"},
         "gate schema")
    need((data["schema"], data["source_W44"], data["budget"]) ==
         ("coupled-pencil-gates-v1", 581590844909990298, 270000000000000000), "gate source pins")
    base = Q(581590844909990298, 44)+1070075+NEAR
    base += Q(43*1048577**11*10**10, 44*11**11*67430**10)
    need(len(data["bands"]) == 108, "complete primitive-height bands")
    for i, row in enumerate(data["bands"]):
        low, high = 1+200*i, min(200*(i+1), 21498)
        need(set(row) == {"low", "high", "gate", "trace", "price"}, "height row schema")
        need((row["low"], row["high"]) == (low, high), "no omitted height")
        e = row["gate"]
        need(type(e) is int and 250000 <= e <= 650000, "integer complement gate")
        cap = list_cap(row["trace"], e-END, 45931-high, END, 11)
        price = ceiling(base+Q(43*981147*cap, 44))
        need(row["price"] == price <= data["budget"] < BUDGET, "whole-source pencil price")
    c, p = {}, {}
    keys = {f"{t},{v}" for t in (1, 2) for v in range(1, 6)}
    need(set(data["constants"]) == set(data["nonconstants"]) == keys, "all pencil dimensions")
    for t in (1, 2):
        for v in range(1, 6):
            need(567501*(v+1) >= S and 567501 <= R-D+t, "constant peak interval")
            c[t, v] = t+Q(567501)*Q(481076, 67473-t)**v
            terms = []
            for row in data["bands"]:
                ell, e_min = row["low"], row["gate"]+1
                peak = Q(S+ell, v+1)
                e = peak if peak >= e_min else Q(e_min)
                need(e_min <= e <= R-D+t and R-D+t < S, "nonconstant maximum interval")
                terms.append(t*(R+END-e_min)+e*(Q(S+ell-e, D+1-t+ell))**v)
            p[t, v] = max(terms)
            need(ratio(data["constants"][f"{t},{v}"]) == c[t, v], "constant weight cap")
            need(ratio(data["nonconstants"][f"{t},{v}"]) == p[t, v], "height-resolved weight cap")
    need(max(r["price"] for r in data["bands"]) == 269999966480486592, "chosen gate maximum")
    return c, p


def compression(data):
    need(set(data) == {"schema", "z_max", "rows"} and data["schema"] ==
         "coupled-compression-boxes-v1" and data["z_max"] == 481076, "compression scope")
    wanted = [(17, 6, 1), (17, 6, 2), (18, 5, 1), (18, 5, 2), (18, 4, 1), (18, 4, 2)]
    need(len(data["rows"]) == len(wanted), "six compression cases")
    totals, steps, boxes = {}, 0, 0
    for row, key in zip(data["rows"], wanted):
        rank, dimension, t = key
        need(set(row) == {"rank", "scalar_dimension", "cutoff", "boxes", "terminal"}, "case schema")
        need((row["rank"], row["scalar_dimension"], row["cutoff"]) == key, "actual scalar-span scope")
        starts = list(range(D+1-t, 481077, 10000))
        need(len(row["boxes"]) == len(starts) == 42, "complete shifted-mass coverage")
        values = []
        for box, low in zip(row["boxes"], starts):
            high = min(low+9999, 481076)
            need(set(box) == {"low", "high", "trace", "ratio"} and
                 (box["low"], box["high"]) == (low, high), "shifted-mass box")
            # Proper-span rank18 still has SIX anchors, not seven.
            cap = list_cap(box["trace"], high-1, D-t, END-(rank-12), dimension)
            value = Q((S-low)*cap, low)
            need(ratio(box["ratio"]) == value, "ratio uses LOW endpoint, padded list uses HIGH")
            values.append(value)
            steps += len(box["trace"])
            boxes += 1
        totals[key] = t+S*max(values)
        need(ratio(row["terminal"]) == totals[key], "common preferred slope and PACK used once")
    need(boxes == 252 and steps == 1260, "compression audit inventory")
    return totals


def substitution(q, offset, scale):
    return [sum(q[j]*comb(j, i)*offset**(j-i)*scale**i for j in range(i, len(q)))
            for i in range(len(q))]


def at(q, x):
    total = Q(0)
    for coefficient in reversed(q):
        total = total*x+coefficient
    return total


def resource_floors():
    # Reconstruct in the original degree variable, independently of the primary.
    d = D-9
    level = [[Q(d*(2*d+1), 2*(d+2)), Q(3*d+1, 2*(d+2)), Q(1, 2*(d+2))]]
    for rank in range(4, 12):
        result = []
        for q in level:
            spike = substitution(q, -1, 1)
            spike[0] -= rank-1
            spike[1] += 1
            child = substitution(q, Q(1, rank-1), Q(rank-2, rank-1))
            equal = [Q(0)]*(len(child)+1)
            for i, a in enumerate(child):
                equal[i] += d*a/(d+rank-1)
                equal[i+1] += a/(d+rank-1)
            result.extend((spike, equal))
        level = result
    need(len(level) == 256, "unpruned resource tree")
    factor = 12*prod(range(d+1, d+11))
    values = {j: int(Q(prod(range(R+j-11, R+j+1)), factor)/min(at(q, j) for q in level))
              for j in range(9965, END+1, 200)}
    need(values[9965] == 577632198670483716, "independent first source floor")
    return values


def source(data, c, p, terminals, masses):
    need(set(data) == {"schema", "J", "near", "budget", "boxes", "maxima", "full18_paid_tail"},
         "source schema")
    need((data["schema"], data["J"], data["near"], data["budget"]) ==
         ("coupled-original-source-boxes-v1", [9965, END], NEAR, BUDGET), "original source scope")
    kinds = ("full17", "sparse18", "no_primitive18", "full18")
    need(len(data["boxes"]) == len(masses) == 58, "full original J coverage")

    def h(a, t, j):
        need(D-j+a+2-t > 0 and S > 2*(j-a)-2, "determinant and Pluecker gates")
        return Q(R-j+a+2, D-j+a+2-t)

    def sparse(rank, t, j):
        pencil = {v: max(c[t, v], p[t, v]) for v in range(1, 6)}
        if rank == 17:
            # Five shared anchors, then all rank5 and rank3 exits.
            child = h(6, t, j)*max(pencil[3], h(7, t, j)*pencil[1])
            exceptional, constant = 2*j-12, c[t, 5]
        else:
            # Six shared anchors, then rank4, rank2 AND zero-dimensional exits.
            child = h(7, t, j)*max(pencil[2], h(8, t, j)*(R-D+t))
            exceptional, constant = 2*j-14, c[t, 4]
        return (S*child+exceptional*max(Q(0), constant-child))/(D+1-t)

    expected = []
    for row, low in zip(data["boxes"], masses):
        high = min(low+199, END)
        need(set(row) == {"low", "high", "mass_floor", *kinds}, "source box schema")
        need((row["low"], row["high"], row["mass_floor"]) == (low, high, masses[low]),
             "source interval and independent resource floor")
        prices = {}
        for kind in kinds:
            rank = 17 if kind == "full17" else 18
            parts = []
            for t in (1, 2):
                value = sparse(rank, t, high)
                if kind != "sparse18":
                    span = 4 if kind == "no_primitive18" else 23-rank
                    value = max(value, terminals[rank, span, t])
                count = rank-12
                for i in range(count):
                    r, s = rank-2*i, 11-i
                    need(s < r <= 2*s and D-t+r-s > 0, "each weighted shared-anchor guard")
                need((rank-2*count, 11-count) == (24-rank, 23-rank), "correct equality-plus-one terminal")
                weight = prod(Q(R+offset, D-t+offset) for offset in range(2, rank-10))
                parts.append(weight*value)
            price = (Q(masses[low], 3)+parts[0]/2+parts[1]/6).numerator
            denominator = (Q(masses[low], 3)+parts[0]/2+parts[1]/6).denominator
            prices[kind] = price//denominator+NEAR
            need(row[kind] == prices[kind], "original weighted identity; single floor and near")
        expected.append(dict(low=low, **prices))
    maxima = {key: max(row[key] for row in expected) for key in kinds}
    need(data["maxima"] == maxima == dict(full17=238873511194752109,
         sparse18=274462040894062110, no_primitive18=274462040894062110,
         full18=311022340713143637), "honest paid and unpaid source maxima")
    tail = next(row["low"] for row in expected
                if all(r["full18"] < BUDGET for r in expected if r["low"] >= row["low"]))
    need(data["full18_paid_tail"] == tail == 14165, "certified upper-degree tail")
    tail_max = max(row["full18"] for row in expected if row["low"] >= tail)
    need(tail_max == 273715780528023745 and BUDGET-tail_max == 1264947583371342, "tail cap")
    need(max(maxima["full17"], 270000000000000000, 261996525491320703) ==
         270000000000000000 and BUDGET-270000000000000000 == 4980728111395087, "whole rank17")
    need(BUDGET-maxima["no_primitive18"] == 518687217332977, "sparse/proper-compression reserve")
    for raw in (1, 2, 3, 9, 44, 150, 151, 981147):
        low1, low2 = (raw if raw <= 1 else 0), (raw if raw <= 2 else 0)
        need(Q(min(raw, 3), 3)+Q(low1, 2)+Q(low2, 6) == 1, "original-label identity")


def mutations(data, c, p, totals, masses):
    cases = []
    for name in data:
        bad = copy.deepcopy(data[name])
        bad["schema"] = "wrong"
        cases.append((name, bad))
    for kind in ("missing", "weight", "preferred", "gate", "step"):
        bad = copy.deepcopy(data["gate_certificate.json"])
        if kind == "missing":
            bad["bands"].pop()
        elif kind == "weight":
            bad["source_W44"] -= 1
        elif kind == "preferred":
            bad["constants"]["1,1"][0] = str(int(bad["constants"]["1,1"][0])-1)
        elif kind == "gate":
            bad["bands"][0]["gate"] += 1
        else:
            bad["bands"][0]["trace"][-1][-1] -= 1
        cases.append(("gate_certificate.json", bad))
    for kind in ("missing", "dimension", "cutoff", "ratio", "preferred", "step"):
        bad = copy.deepcopy(data["compression_certificate.json"])
        row = bad["rows"][-1]
        if kind == "missing":
            row["boxes"].pop()
        elif kind == "dimension":
            row["scalar_dimension"] = 3
        elif kind == "cutoff":
            row["cutoff"] = 1
        elif kind == "ratio":
            row["boxes"][0]["ratio"][0] = str(int(row["boxes"][0]["ratio"][0])-1)
        elif kind == "preferred":
            row["terminal"][0] = str(int(row["terminal"][0])-2*int(row["terminal"][1]))
        else:
            row["boxes"][-1]["trace"][-1][-1] -= 1
        cases.append(("compression_certificate.json", bad))
    for kind in ("missing", "mass", "tail", "full17", "sparse18", "no_primitive18", "full18", "near"):
        bad = copy.deepcopy(data["source_certificate.json"])
        if kind == "missing":
            bad["boxes"].pop()
        elif kind == "mass":
            bad["boxes"][0]["mass_floor"] -= 1
        elif kind == "tail":
            bad["full18_paid_tail"] -= 200
        elif kind == "near":
            bad["near"] -= 1
        else:
            bad["boxes"][0][kind] -= 1
        cases.append(("source_certificate.json", bad))
    for name, bad in cases:
        try:
            if name == "gate_certificate.json":
                gates(bad)
            elif name == "compression_certificate.json":
                compression(bad)
            else:
                source(bad, c, p, totals, masses)
        except (ValueError, KeyError):
            continue
        raise ValueError("accepted corrupted certificate")
    return len(cases)


def main():
    data = {}
    for name, pin in PINS.items():
        raw = (NODE/name).read_bytes()
        need(hashlib.sha256(raw).hexdigest() == pin, "frozen certificate identity")
        data[name] = json.loads(raw)
    c, p = gates(data["gate_certificate.json"])
    totals = compression(data["compression_certificate.json"])
    masses = resource_floors()
    source(data["source_certificate.json"], c, p, totals, masses)
    print("PASS independent 108 height bands, 252 compression boxes, 58 source boxes")
    print("PASS all 2448 LIST transitions; expanded rank-two descendants; all paid/unpaid maxima")
    print("PASS", mutations(data, c, p, totals, masses), "scope/coverage/weight/price mutations rejected")
    print("No primary/helper imports; universal geometry and ownership remain hand-proof inputs")


if __name__ == "__main__":
    main()
