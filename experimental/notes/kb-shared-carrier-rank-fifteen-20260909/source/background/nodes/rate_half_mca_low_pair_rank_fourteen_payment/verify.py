"""Generate or replay eleven bounded height-band certificates and the price."""

import argparse
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

NODE = Path(__file__).resolve().parent
CERT = NODE/"height_caps.json"
R, D, E, NEAR = 1048576, 67472, 21499, 134944


def need(ok, message):
    if not ok:
        raise ValueError(message)


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def certificate(compiler):
    bands = []
    for lo in range(1, E, 2000):
        hi = min(lo+1999, E-1)
        e, a = 272000+9*(21498-hi), 67471-hi
        need(1 <= a-E <= e-E and 2130706433**6 >= e, "shared-carrier padding gates")
        cap, trace = compiler.compile_cap(e-E, a-E, E, 11)
        bands.append({"h_min": lo, "h_max": hi, "e": e, "A": a,
                      "K_max": E, "dimension": 11, "cap": cap,
                      "trace": [list(step) for step in trace]})
    return {"schema": "rank-fourteen-height-band-outside-list-v1", "bands": bands}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    compiler = module("credited_height_compiler", NODE.parent/"list_padded_johnson_dimension_descent/compiler.py")
    expected = certificate(compiler)
    if args.write:
        need(not CERT.exists(), "refuse overwriting a frozen certificate")
        CERT.write_text(json.dumps(expected, indent=2)+"\n")
    data = json.loads(CERT.read_bytes())
    need(data == expected and len(data["bands"]) == 11, "exact complete height profile")
    maximum, pmax, owners = 0, [F(1), F(1)], [None, None]
    for row in data["bands"]:
        maximum = max(maximum, 228260637755610995+981106*row["cap"])
        for t in (1, 2):
            need(R-row["e"] > D+1-t, "height monotonicity")
            p = F(R-row["e"]+row["h_min"], D+1-t+row["h_min"])
            if p > pmax[t-1]:
                pmax[t-1], owners[t-1] = p, (row["h_min"], row["h_max"])
    need(maximum == 272840087674756199 < 274138707278280353, "whole-source band prices")
    need(owners == [(18001, 20000)]*2, "worst hereditary height band")
    supplier = module("credited_basis_for_height", NODE.parent/"rate_half_mca_low_pair_pencil_payment/verify.py")
    w3 = int(supplier.basis())
    need(w3 == 613022127444579907, "unrefunded integer source mass")
    value, floors = F(w3, 3), []
    for t in (1, 2):
        c, p, h = F(548576, 67473-t), F(781095, 85474-t), F(1027079, 45975-t)
        need(pmax[t-1] == p and 1 <= c <= p, "uniform hereditary pencil cap")
        need(h <= p*p and h*p**6 <= c**8, "both terminal child ranks are paid")
        q = F(1)
        for pair_rank, shared, excess in ((14, 11, 3), (12, 10, 2), (10, 9, 1)):
            need(pair_rank-shared == excess and pair_rank > shared, "each rank gate")
            need(D-t+excess > 0, "each original-domain denominator")
            q *= F(R+excess, D-t+excess)
        bound = q*c**8
        floors.append(int(bound))
        value += F(R-D+t, t*(t+1))*bound
    branch = int(value)+NEAR
    need(floors == [71666785024, 71678469894], "pair floors")
    need(branch == 251217725856263117, "all-raw branch price")
    total = max(branch, maximum, 274138707278280353)
    need(total == 274138707278280353 and 274980728111395087-total == 842020833114734,
         "whole-source maximum and strict reserve")
    need(14 <= 2*11 and (14-6, 11-3) == (8, 8), "auxiliary embedding and final ranks")
    print("PASS eleven complete height bands; 121 LIST transitions; max band price", maximum)
    print("PASS hereditary caps", pmax, "and three rank-gated anchors; pair floors", floors)
    print("RANK<=14 PAY", total, "RESERVE", 274980728111395087-total, "BRANCH", branch)
    print("No entire degree interval or higher original error rank is paid")


if __name__ == "__main__":
    main()
