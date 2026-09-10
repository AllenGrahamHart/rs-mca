"""Reconstruct the same-source HIGH gate and bounded integer controls."""

from fractions import Fraction as F
import importlib.util
from itertools import product
from math import prod
from pathlib import Path


def need(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    path = Path(__file__).resolve().parent.parent/"rate_half_mca_low_raw_rank_filtration/verify.py"
    spec = importlib.util.spec_from_file_location("original_filtration", path)
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    a, b, c = source.ladder()
    d, E, R = 67472, 21499, 1048576
    q = lambda j: a+b*j+c*j*j
    beta = lambda j: 12*prod(source.D+i for i in range(1, 11))*q(j)
    Pd = prod(d+i for i in range(1, 11))
    need(d*b >= a and 126*(d+E)*Pd >= 4*beta(E), "inherited interval-wide HIGH")
    need(1386*(d+E)*Pd >= 44*beta(E), "same-resource completed HIGH")
    need(1386*(d+E)*Pd < 45*beta(E), "this uniform gate does not fund45")
    need((b+2*c*9941)*(R+9941-11) > 12*q(E), "inherited decreasing ratio")
    for j, W, tail in ((9941, 624373932788019251, 14190316654273164),
                       (14000, 522680876725222604, 11879110834664150)):
        need(int(F(prod(R+j-i for i in range(12)))/beta(j)) == W, "same integer resource")
        need(W//44 == tail, "original-label HIGH tail")
    for raw in list(range(1, 601))+[67472, 67473, 1000000]:
        funded = raw if raw <= 125 else 44
        need(funded >= min(raw, 44), "complete raw case split")
        if raw >= 126:
            need(11*min(raw, 500) >= 1386, "completed all-HIGH weight")
    cases = 0
    for values in product((1, 2, 8, 43, 44, 125, 126, 501), repeat=3):
        mass = sum(min(r, 44) for r in values)
        for T in (1, 2, 7, 8, 42, 43):
            clipped = sum(min(r, T+1) for r in values)
            deficit = sum(T+1-r for r in values if r <= T)
            nested = sum(sum(r <= t for r in values) for t in range(1, T+1))
            need(clipped+deficit == (T+1)*len(values) and deficit == nested,
                 "exact original cumulative identity")
            need(clipped <= mass, "funded truncation")
            cases += 1
    print("PASS HIGH44 on unchanged beta; W0/W1 and tail floors;", cases, "integer ledgers")
    print("No maximal truncation, auxiliary HIGH resource or full Prize payment is claimed")


if __name__ == "__main__":
    main()
