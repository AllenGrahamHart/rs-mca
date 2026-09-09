"""Independent integer reconstruction; no primary or LIST compiler imports."""

import hashlib
import json
import copy
from math import prod
from pathlib import Path

CERT = Path(__file__).resolve().parent.parent/"rate_half_mca_low_pair_pencil_payment/certificate"
PIN = "d5515bb34f6afa52fe67b616d18967af292fbe16a64b3eecbf032ffa7009b31d"


def need(ok, message):
    if not ok:
        raise ValueError(message)


def johnson(e, k, a):
    need(e >= 0 and k > 0 and a > 0, "scope")
    if a > e:
        return 0
    divisor = a*a-e*(k-1)
    need(divisor > 0, "positive Johnson gate")
    return e*(a-k+1)//divisor


def outside_caps(data):
    need(data["schema"] == "dominant-pencil-outside-list-v1" and len(data["caps"]) == 3, "three outside caps")
    expected = ((400000, 67471, 3146811647), (500000, 67471, 54886611863), (250000, 45973, 14781874200))
    for row, (e, a, cap) in zip(data["caps"], expected):
        need((row["e"], row["A"], row["K_max"], row["dimension"], row["cap"])
             == (e, a, 21499, 11, cap), "fixed shared-carrier input")
        r, w, k = e-21499, a-21499, 21499
        need(1 <= w <= r and 11 <= k and 2130706433**6 >= e, "LIST scope")
        upper = 1
        need(len(row["trace"]) == 11, "eleven transitions")
        for rank, (s, degree, value) in enumerate(row["trace"], 1):
            need(s == rank and type(degree) is int and 0 <= degree <= k, "transition identity")
            if degree == 0:
                bound = (r+s)*upper//(w+s)
            else:
                denominator = (w+degree)**2-(r+degree)*(degree-1)
                need(denominator > 0, "Johnson step gate")
                bound = (r+degree)*(w+1)//denominator
                if degree < k:
                    bound = max(bound, (r+degree+1)*upper//(w+degree+1))
            need(type(value) is int and value == bound, "exact legal transition")
            upper = value
        need(upper == cap, "final outside cap")
    return tuple(row[2] for row in expected)


def main():
    data = (CERT/"manifest.json").read_bytes()
    need(hashlib.sha256(data).hexdigest() == PIN, "supplier manifest identity")
    manifest = json.loads(data)
    need(manifest["complete"] is True and len(manifest["shards"]) == 8, "completed eight-shard certificate")
    rn, rd = map(int, manifest["metadata"]["R0"])
    need(rn//rd == 613022127444579907 and rn % rd != 0, "unrounded resource")
    low_end, high_end = 211756, 456878
    need(67471**2-21498*low_end == 5353
         and 21498*(low_end+1) >= 67471**2, "worst-J endpoint")
    need(9964*high_end < 67471**2 <= 9964*(high_end+1), "minimum-J endpoint")
    count = johnson(low_end, 21499, 67471)
    need(count == 1818617 and 274136923022229951+981106*count == 274138707278280353,
         "small branch")
    need(228260637755610995+981106*456878*57507 == 254037905932250471,
         "nonconstant branch")
    rejected = 0
    for args in ((low_end+1, 21499, 67471), (high_end+1, 9965, 67471), (4, 2, 2)):
        try:
            johnson(*args)
        except ValueError:
            rejected += 1
        else:
            raise ValueError("accepted nonpositive Johnson denominator")
    need(rejected == 3 and johnson(0, 21499, 67471) == 0, "boundary controls")
    outside = json.loads((Path(__file__).resolve().parent/"outside_list_caps.json").read_bytes())
    caps = outside_caps(outside)
    mutations = []
    for key, value in (("e", 400001), ("A", 67470), ("K_max", 21500), ("dimension", 10)):
        bad = copy.deepcopy(outside)
        bad["caps"][0][key] = value
        mutations.append(bad)
    for index, value in ((0, 0), (1, 21500), (2, 0)):
        bad = copy.deepcopy(outside)
        bad["caps"][0]["trace"][0][index] = value
        mutations.append(bad)
    bad = copy.deepcopy(outside)
    bad["caps"][0]["trace"][-1][2] -= 1
    mutations.append(bad)
    bad = copy.deepcopy(outside)
    bad["caps"][0]["trace"].pop()
    mutations.append(bad)
    for bad in mutations:
        try:
            outside_caps(bad)
        except ValueError:
            continue
        raise ValueError("accepted corrupted outside certificate")

    n, m = 1058541, 77437
    full = prod(n-i for i in range(12))
    denominator = 6*rd*full*(m-1)*(m-2)
    maxima, intervals, boxes = [0, 0], [None, None], [0, 0]
    ranges = ((211757, 400000, caps[0]), (400001, 500000, caps[1]))
    seen, byte_count = 0, 0
    for index, shard in enumerate(manifest["shards"]):
        relative = f"shards/part-{index:05d}.jsonl"
        need(shard["path"] == relative, "canonical shard order")
        block = (CERT/relative).read_bytes()
        need(hashlib.sha256(block).hexdigest() == shard["sha256"]
             and len(block) == shard["bytes"], "shard hash and bytes")
        lines = block.splitlines()
        need(len(lines) == shard["records"], "shard count")
        byte_count += len(block)
        for line in lines:
            row = json.loads(line)
            a, b = row["a"], row["b"]
            need(a == seen*1000 and b == min(a+999, 981104), "exhaustive base boxes")
            seen += 1
            need([cap["t"] for cap in row["caps"]] == [1, 2], "two LIST thresholds")
            v1, v2 = (cap["trace"][-1][2] for cap in row["caps"])
            outside = prod(n-b-i for i in range(12))
            numerator = (1+134944)*denominator
            numerator += 2*rn*(full-outside)*(m-1)*(m-2)
            numerator += rd*full*b*(n-a)*(3*(m-2)*v1+(m-1)*v2)
            for i, (low, high, cap) in enumerate(ranges):
                if b < low or a > high:
                    continue
                value = numerator+981106*cap*denominator
                if value > maxima[i]:
                    maxima[i], intervals[i] = value, (a, b)
                boxes[i] += 1
    need((seen, byte_count) == (982, 352246) and boxes == [190, 101], "complete imported and new coverage")
    ceilings = tuple(-(-value//denominator) for value in maxima)
    need(ceilings == (254493279590417819, 262886297505008376)
         and intervals == [(211000, 211999), (400000, 400999)], "independent exact maxima")
    nc_list = 228260637755610995+981106*caps[2]
    need(nc_list == 242763223224476195, "arbitrary-direction bounded complement")
    total = max(*ceilings, 274138707278280353, 254037905932250471, nc_list)
    need(total < 2130706433**6//2**128 and 274980728111395087-total == 842020833114734,
         "original target and reserve")
    print("PASS 33 independently checked shared-carrier LIST transitions; 190/101 branch boxes", ceilings)
    print("PASS eight pinned shards; three invalid Johnson gates and nine corrupted outside certificates rejected")
    print("Groupwise source accounting and the inherited LIST/basis proofs remain required")


if __name__ == "__main__":
    main()
