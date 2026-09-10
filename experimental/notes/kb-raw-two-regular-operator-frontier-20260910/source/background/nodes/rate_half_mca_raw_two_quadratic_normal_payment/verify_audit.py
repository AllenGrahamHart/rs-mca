"""Independent integer upper-envelope audit; imports no local proof code."""

import copy
import hashlib
import json
from pathlib import Path

NODE = Path(__file__).resolve().parent


def need(ok, why):
    if not ok:
        raise ValueError(why)


def validate(data):
    parameters = dict(R=1048576, d=67472, J=[9965, 21499], original_rank=12,
                      shared_dimension=11, raw_max=2, basis_raw=7, normal_degree=2,
                      basis_floor5=222676884802638507, resource=578501226347492453,
                      near=134944, B_star=274980728111395087)
    need(data["schema"] == "raw-two-quadratic-normal-v1", "schema")
    need(data["parameters"] == parameters, "unchanged source and raw/basis scopes")
    need(all(type(v) is int for k, v in data["parameters"].items() if k != "J")
         and all(type(v) is int for v in data["parameters"]["J"]), "integer scope, not booleans")
    R, d, J, raw = 1048576, 67472, 21499, 2
    numerator, denominator = 1, 1
    for shared in range(11, 0, -1):
        rank, bad, n, agreements = 2*shared, J-shared, R+J, d+J-raw
        need(shared < rank <= 2*shared and 0 <= bad < agreements, "strict actual-pair anchor")
        numerator *= n-bad
        denominator *= agreements-bad
    pairs = numerator//denominator
    m5 = parameters["basis_floor5"]
    mass = (2*m5+2)//5
    # This uses the proved uniform floor, not coefficients imported from the primary.
    need(5*mass <= 2*(m5+1) < 5*(mass+1), "conservative integer scaling")
    moving, exceptions = J-11+2, J-11+2+2*pairs
    W, near, budget = parameters["resource"], parameters["near"], parameters["B_star"]
    need(2130706433**6//2**128 == budget and near == 2*d, "original budget and add-back")
    amount = W+2*(mass+exceptions)
    graph, lines = divmod(amount, 3)[0]+near, (W+2*(mass+moving))//3+near
    target = 3*(budget-near+1)-amount
    outside = -(-target//2)
    expected = dict(mass_cap=mass, pair_floor=pairs, moving_zeros=moving,
                    inside_exceptions=exceptions, amount=amount, graph=graph,
                    lines=lines, reserve=budget-graph, outside_min=outside)
    need(set(data) == {"schema", "parameters", "basis_primary_sha256", *expected}, "full schema")
    for k, value in expected.items():
        need(type(data[k]) is int and data[k] == value, "exact field: "+k)
    path = NODE.parent/"rate_half_mca_moving_normal_basis_payment/verify.py"
    need(data["basis_primary_sha256"] == hashlib.sha256(path.read_bytes()).hexdigest(), "basis source pin")
    need(pairs*denominator <= numerator < (pairs+1)*denominator, "unrounded pair floor")
    need(lines <= graph < budget and 2*(outside-1) < target <= 2*outside, "whole-source payment")
    need((amount+2*(outside-1))//3+near == budget
         and (amount+2*outside)//3+near == budget+1, "adjacent sufficient envelopes")


def main():
    data = json.loads((NODE/"certificate.json").read_text())
    validate(data)
    cases = []
    for key, value in data.items():
        if type(value) is int:
            bad = copy.deepcopy(data)
            bad[key] -= 1
            cases.append(bad)
    for key in data["parameters"]:
        bad = copy.deepcopy(data)
        if key == "J":
            bad["parameters"][key][0] += 1
        else:
            bad["parameters"][key] += 1
        cases.append(bad)
    for key in ("schema", "basis_primary_sha256"):
        bad = copy.deepcopy(data)
        bad[key] = "wrong"
        cases.append(bad)
    bad = copy.deepcopy(data)
    bad["parameters"]["raw_max"] = True
    cases.append(bad)
    for bad in cases:
        try:
            validate(bad)
        except (ValueError, KeyError):
            continue
        raise ValueError("accepted corrupted scope or arithmetic")
    print("PASS eleven guarded pair stages; independent integer scaling and original source prices")
    print("PASS", len(cases), "scope/exception/price mutations rejected")
    print("Inherited uniform basis floor needs its separate proof and arithmetic replay")


if __name__ == "__main__":
    main()
