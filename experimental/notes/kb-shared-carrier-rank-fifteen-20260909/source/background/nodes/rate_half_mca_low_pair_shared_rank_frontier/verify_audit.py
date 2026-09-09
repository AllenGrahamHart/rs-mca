"""Independent integer source prices, with no primary or compiler imports."""

import hashlib
import json
from math import prod
from pathlib import Path


def need(ok, message):
    if not ok:
        raise ValueError(message)


def price(w3, steps, terminal_power):
    terms, floors = [], []
    for t in (1, 2):
        numerator = prod(1048576+c for c in range(1, steps+1))
        denominator = prod(67472-t+c for c in range(1, steps+1))
        if terminal_power:
            cn, cd, pn, pd, hn, hd = 528576, 67473-t, 781095, 85474-t, 1027079, 45975-t
            need(cd > 0 and hd > 0 and cn*pd <= pn*cd, "positive scalar gates")
            need(hn*pd**2 <= hd*pn**2, "hereditary H<=P squared")
            need(hn*pn*cd**3 <= hd*pd*cn**3, "rank-two child <=constant cubic cap")
            numerator *= cn**terminal_power
            denominator *= cd**terminal_power
        floors.append(numerator//denominator)
        terms.append(((981104+t)*numerator, t*(t+1)*denominator))
    (n1, d1), (n2, d2) = terms
    total = (w3*d1*d2+3*n1*d2+3*n2*d1)//(3*d1*d2)+134944
    return floors, total


def main():
    node = Path(__file__).resolve().parent
    raw = (node.parent/"rate_half_mca_low_pair_pencil_payment/certificate/manifest.json").read_bytes()
    need(hashlib.sha256(raw).hexdigest()
         == "d5515bb34f6afa52fe67b616d18967af292fbe16a64b3eecbf032ffa7009b31d", "inherited resource custody")
    rn, rd = map(int, json.loads(raw)["metadata"]["R0"])
    w3 = rn//rd
    need(w3 == 613022127444579907 and rn % rd != 0, "unrefunded integer source mass")
    nine = price(w3, 9, 0)
    ten = price(w3, 7, 3)
    need(nine == ([52853517316, 52860567481], 238911770855075395), "direct full-pair carrier-nine count")
    need(ten == ([105235509453, 105251107155], 273174666855895812), "carrier-ten pair-seventeen branch")
    whole = max(ten[1], 274138707278280353)
    need(whole == 274138707278280353 and 274980728111395087-whole == 842020833114734, "retained whole-source alternatives")
    need(274980728111395087-nine[1] == 36068957256319692, "direct carrier-nine reserve")
    for s, r, steps, end in ((9, 18, 9, 0), (10, 17, 7, 3)):
        need(all(r-2*i > s-i > 0 for i in range(steps)), "each strict shared-rank gate")
        need(r-2*steps == s-steps == end, "point versus rank-three terminal")
    print("PASS independent nine-anchor point count", nine)
    print("PASS independent seven-anchor child split", ten, "WHOLE", whole)
    print("No primary/compiler imports; neither counts nor auxiliary ranks replace the source")


if __name__ == "__main__":
    main()
