"""Exact rank-twelve price, with one bounded shared-carrier LIST certificate."""

import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

NODE = Path(__file__).resolve().parent
R, D, LO, HI, NEAR = 1048576, 67472, 9965, 21499, 134944
BUDGET, TOTAL, OLD = 274980728111395087, 274267808872348771, 274138707278280353


def need(ok, message):
    if not ok:
        raise ValueError(message)


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def main():
    data = json.loads((NODE/"outside_list_cap.json").read_bytes())
    need(data["schema"] == "rank-twelve-nonconstant-pencil-outside-list-v1", "certificate identity")
    need(tuple(data[key] for key in ("e", "A", "K_max", "dimension", "cap"))
         == (272000, 45973, HI, 11, 45437954634), "exact joint-LIST input")
    need(1 <= 45973-HI <= 272000-HI and 2130706433**6 >= 272000, "padding gates")
    compiler = module("credited_joint_compiler", NODE.parent/"list_padded_johnson_dimension_descent/compiler.py")
    cap, trace = compiler.compile_cap(272000-HI, 45973-HI, HI, 11)
    need(cap == data["cap"] and [list(row) for row in trace] == data["trace"], "all chosen transitions")
    extension = 228260637755610995+981106*cap
    need(extension == 272840087674756199 < OLD, "groupwise extension price")
    supplier = module("credited_all_raw_basis", NODE.parent/"rate_half_mca_low_pair_pencil_payment/verify.py")
    r0 = supplier.basis()
    w3 = int(r0)
    need(w3 == 613022127444579907 and r0.denominator > 1, "unrefunded integer mass")
    value, floors = F(w3, 3), []
    for t in (1, 2):
        c, p = F(548576, D+1-t), F(776577, D+2-t)
        h, q = F(R-HI+2, D-HI+2-t), F(R+1, D+1-t)
        need(1 <= c <= p and R-272000 > D+1-t, "hereditary scalar and height gates")
        need(D-HI+2-t > 0 and D+1-t > 0, "both anchor denominators")
        need(F(R-LO+2, D-LO+2-t) <= h and R-D+t > 0, "whole-J monotonicity")
        need(h <= p*p and c**10 <= h*p**8, "rank-two and constant child domination")
        bound = q*h*p**8
        floors.append(int(bound))
        value += F(R-D+t, t*(t+1))*bound
    branch = int(value)+NEAR
    need(floors == [106906553861, 106923140583], "separate pair floors")
    need(branch == TOTAL and max(branch, extension, OLD) == TOTAL, "whole-source maximum")
    need(BUDGET-TOTAL == 712919239046316 > 0, "strict finite reserve")
    need(12 > 11 and 2*11-12 == 10 and 12-2 == 11-1 == 10, "pair/shared-rank bookkeeping")
    print("PASS eleven exact shared-carrier LIST steps; nonconstant extension", extension)
    print("PASS whole-J and hereditary child gates; pair floors", floors)
    print("RANK<=12 PAY", TOTAL, "RESERVE", BUDGET-TOTAL)
    print("Pair dimension>=13 and original error rank>=13 remain separate open obligations")


if __name__ == "__main__":
    main()
