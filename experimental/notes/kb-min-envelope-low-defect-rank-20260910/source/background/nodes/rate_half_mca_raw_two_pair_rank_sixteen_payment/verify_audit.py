"""Independent chosen-step legality and integer-ratio final price; no local imports."""

import copy
from fractions import Fraction as Q
import hashlib
import json
from math import prod
from pathlib import Path

NODE = Path(__file__).resolve().parent
PIN = "bbacb3699165acb3dbf018fc21116d0f19b3ee1e650ea9994100adc038f1973e"
COMPILER = "bac33f24d1f34760518406185fcc9850d4fc61f5441486f94237e13b99eb8ca8"
PRICES = (72265795590617078, 79278043693283795, 83945390348617214,
          89723144344675371, 97521166406982503, 106844085628376811,
          119660010442406346, 136828308086394744, 172912201229402247,
          210774727972621255, 220845070943887497)


def need(ok, message):
    if not ok:
        raise ValueError(message)


def list_cap(trace, n_minus_k, a_minus_k):
    need(1 <= a_minus_k <= n_minus_k and len(trace) == 11, "LIST scope")
    need(2130706433**6 >= n_minus_k+21499, "padding field")
    old = 1
    for rank, row in enumerate(trace, 1):
        need(len(row) == 3 and all(type(x) is int for x in row), "integer trace")
        actual, degree, cap = row
        need(actual == rank and 0 <= degree <= 21499 and cap > 0, "step scope")
        if degree == 0:
            expected = (n_minus_k+rank)*old//(a_minus_k+rank)
        else:
            denominator = (a_minus_k+degree)**2-(n_minus_k+degree)*(degree-1)
            need(denominator > 0, "Johnson denominator")
            expected = (n_minus_k+degree)*(a_minus_k+1)//denominator
            if degree < 21499:
                expected = max(expected, (n_minus_k+degree+1)*old//(a_minus_k+degree+1))
        need(cap == expected, "exact chosen-step legality")
        old = cap
    return old


def validate(data):
    need(set(data) == {"schema", "parameters", "compiler_sha256", "bands", "nonconstant_max",
                       "pair_floor", "total", "reserve", "list_steps"}, "certificate schema")
    need(data["schema"] == "raw-two-pair-rank-sixteen-v1" and data["compiler_sha256"] == COMPILER,
         "source identity")
    need(data["parameters"] == dict(R=1048576, d=67472, J_min=9965, J_max=21499,
         pair_cutoff=2, union_cutoff=43, rank=16, section_ratio=[35, 4], mass_truncation=9,
         mass_bound=578501226347492453, near=134944, constant_complement=567500,
         height_width=2000), "original source parameters")
    base = Q(624373932788019251, 44)+1070075+134944
    base += Q(43*1048577**11*10**10, 44*11**11*67430**10)
    bands = data["bands"]
    need(len(bands) == 11 and data["list_steps"] == 121, "complete band inventory")
    for i, row in enumerate(bands):
        low, high = 1+2000*i, min(2000+2000*i, 21498)
        gate = (4*1048576-35*67471-31*low+3)//4
        need(set(row) == {"low", "high", "gate", "off", "ceiling"}, "band schema")
        need((row["low"], row["high"], row["gate"]) == (low, high, gate), "exact coverage")
        need(4*(1048576-gate+low) <= 35*(67471+low), "ceiling gives hereditary endpoint")
        need(1048576-gate > 67471 and gate > 21499, "height monotonicity and degree corridor")
        cap = list_cap(row["off"], gate-21499, 45931-high)
        price = base+Q(43*981147*cap, 44)
        ceiling = -(-price.numerator//price.denominator)
        need(row["ceiling"] == ceiling == PRICES[i], "independent band price")
    need(data["nonconstant_max"] == max(PRICES) < 261996525491320703, "whole-source alternatives")
    need(4*481076 <= 35*67471 and 16*1027079 <= 35**2*45973, "C<=P and H<=P^2")
    one_n, one_d = 481076**6, 67471**6
    two_n, two_d = 1027079*35**4, 45973*4**4
    need(one_n*two_d > two_n*one_d, "constant terminal dominates rank two")
    numerator = one_n*prod(range(1048577, 1048582))
    denominator = one_d*prod(range(67471, 67476))
    need(numerator//denominator == data["pair_floor"] == 119106357701, "pair floor")
    for i in range(5):
        rank, shared = 16-2*i, 11-i
        need(shared < rank <= 2*shared and 67470+rank-shared > 0, "each guarded stage")
    total = (578501226347492453*denominator+2*981106*numerator)//(3*denominator)+134944
    need(total == data["total"] == 270737716902276994, "single final integer floor")
    need(total > max(PRICES) and total > 261996525491320703, "take maximum, not sum")
    need(data["reserve"] == 274980728111395087-total == 4243011209118093, "reserve")
    need(578501226347492453//3+134944 < total, "empty P2 family")


def main():
    raw = (NODE/"certificate.json").read_bytes()
    need(hashlib.sha256(raw).hexdigest() == PIN, "frozen certificate")
    data = json.loads(raw)
    validate(data)
    variants = []
    for field in ("total", "reserve", "pair_floor", "nonconstant_max", "list_steps"):
        bad = copy.deepcopy(data)
        bad[field] += 1
        variants.append(bad)
    for kind in ("mass", "cutoff", "missing", "gate", "step"):
        bad = copy.deepcopy(data)
        if kind == "mass":
            bad["parameters"]["mass_bound"] -= 1
        elif kind == "cutoff":
            bad["parameters"]["pair_cutoff"] = 7
        elif kind == "missing":
            bad["bands"].pop()
        elif kind == "gate":
            bad["bands"][0]["gate"] += 1
        else:
            bad["bands"][-1]["off"][-1][-1] += 1
        variants.append(bad)
    for bad in variants:
        try:
            validate(bad)
        except ValueError:
            continue
        raise ValueError("accepted a corrupted certificate")
    print("PASS independent 121 LIST steps, rank16 chain and original source price270737716902276994")
    print("PASS", len(variants), "scope/coverage/step/price mutations rejected")
    print("No primary/helper imports; ownership and universal gates remain hand-proof inputs")


if __name__ == "__main__":
    main()
