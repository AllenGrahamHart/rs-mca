"""Exact raw-two quadratic price using the inherited rank-ten basis lemma."""

import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import prod
from pathlib import Path

NODE = Path(__file__).resolve().parent


def need(ok, why):
    if not ok:
        raise ValueError(why)


def build():
    path = NODE.parent/"rate_half_mca_moving_normal_basis_payment/verify.py"
    spec = importlib.util.spec_from_file_location("inherited_normal_basis", path)
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    a, b, c = source.ladder()
    R, d, low, high, raw, basis_raw = 1048576, 67472, 9965, 21499, 2, 7
    q = lambda j: a+b*j+c*j*j
    need((b+2*c*low)*(R+low-10) > 11*q(high), "uniform decreasing basis quotient")
    ratio5 = Q(5*prod(R+low-i for i in range(11)),
               11*prod(d-basis_raw+i for i in range(1, 10)))/q(low)
    m5 = int(ratio5)
    need(m5 == 222676884802638507, "inherited degree-five floor")
    mass = 2*(m5+1)//5
    need(int(Q(2, 5)*ratio5) <= mass == 89070753921055403, "safe degree-two mass cap")
    pairs = int(prod(Q(R+i, d-raw+i) for i in range(1, 12)))
    need(pairs == 12763910835039, "actual pair floor at raw cutoff TWO")
    moving = high-11+2
    exceptions = moving+2*pairs
    W, near, budget = 578501226347492453, 134944, 274980728111395087
    need(2130706433**6//2**128 == budget and near == 2*d, "original field budget and near")
    amount = W+2*(mass+exceptions)
    graph, lines = amount//3+near, (W+2*(mass+moving))//3+near
    outside = (3*(budget-near+1)-amount+1)//2
    need((amount, graph, lines, outside) == (756693789832986395,
         252231263277797075, 252214244730017023, 34124197250397019), "original source prices")
    need((amount+2*(outside-1))//3+near == budget, "last paid sufficient envelope")
    need((amount+2*outside)//3+near == budget+1, "adjacent envelope, not unsafe witness")
    return dict(schema="raw-two-quadratic-normal-v1",
                parameters=dict(R=R, d=d, J=[low, high], original_rank=12,
                                shared_dimension=11, raw_max=raw, basis_raw=basis_raw,
                                normal_degree=2, basis_floor5=m5, resource=W, near=near,
                                B_star=budget),
                basis_primary_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                mass_cap=mass, pair_floor=pairs, moving_zeros=moving,
                inside_exceptions=exceptions, amount=amount, graph=graph, lines=lines,
                reserve=budget-graph, outside_min=outside)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    data = build()
    path = NODE/"certificate.json"
    if args.write:
        need(not path.exists(), "refuse certificate replacement")
        path.write_text(json.dumps(data, indent=2)+"\n")
    need(json.loads(path.read_text()) == data, "frozen certificate")
    print("PASS raw2/basis7 separation; MASS", data["mass_cap"], "PAIRS", data["pair_floor"])
    print("GRAPH", data["graph"], "LINES", data["lines"], "OUTSIDE", data["outside_min"])
    print("CERTIFICATE", hashlib.sha256(path.read_bytes()).hexdigest())
    print("Universal basis and original tuple ownership require the printed hand proofs")


if __name__ == "__main__":
    main()
