"""Exact finite switching-credit certificate; existing helpers supply generic costs."""

from fractions import Fraction as F
import hashlib
import importlib.util
from math import prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(name, node):
    spec = importlib.util.spec_from_file_location(name, ROOT/node/"verify.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


v = load("previous_weighted_formulas", "rate_half_mca_weighted_collision_interval")
s = load("sharp_switching_credit", "mca_projective_fiber_switching_resource")
D, R, GAP, NEAR = v.D, v.R, v.GAP, v.NEAR
LO, HI, TOTAL = 21500, 21799, 274956328426911303
TRIGGER = 274960000000000000
EXPECTED = "e9087d3555bafce49cba6c75e09c0c6eb45a5025d057f5f20e9b762f48c0fa86"


def need(ok, why):
    if not ok:
        raise ValueError(why)


def main():
    digest = hashlib.sha256()
    rows = [(left, min(left+15, HI)) for left in range(LO, HI+1, 16)]
    v.cover(rows, LO, HI)
    for broken in (rows[1:], rows[:-1], rows+[rows[-1]], rows[:4]+rows[5:]):
        try:
            v.cover(broken, LO, HI)
        except ValueError:
            pass
        else:
            raise ValueError("accepted a broken degree cover")
    need(21000 <= LO <= HI <= 52999 and 266180883463176443 < TOTAL
         < TRIGGER < 2130706433**6//2**128, "source alternative and budget")
    need(84*125*(GAP+1-77) > 10488*(GAP+1) and 22*84 < GAP+1, "all-HIGH weight")
    count, used, floors, peak = 0, 0, 0, (0, None)
    ranks = {t: 0 for t in range(1, 11)}
    for left, right in rows:
        n0, n1 = R+left, R+right
        need(n0 >= 10*(right-10), "whole-box source moment branch")
        Tmax = n1*(right-11)//10
        need(Tmax == v.w.source_cap(n1, right, 11), "exact source collision cap")
        credit = s.coefficient(n1, 12)
        resource = prod(n1-i for i in range(12))
        high = F(10488, 125)*(GAP+left)*prod(GAP+i for i in range(1, 11))
        add = right-11+Tmax//2+NEAR
        digest.update(f"R:{left},{right}:{credit}:{Tmax}:{resource}:{add}\n".encode())
        for t in range(1, 11):
            top = min(right-11+t, right-6001 if t == 1 else right)
            bins = list(v.old.bins(t, top, 1024 if t == 1 else 128))
            v.cover(bins, t, top)
            for a0, a1 in bins:
                lower, bonus, cmin, cmax = v.root_terms(left, right, t, a0, a1, credit, Tmax)
                cost = 12*lower
                if resource//min(cost, high)+add > TRIGGER:
                    cost = max(cost, 12*(v.old_cost(left, right, t, a0, a1)+bonus))
                    used += 1
                cost = min(cost, high)
                ratio = resource/cost
                integer = ratio.numerator//ratio.denominator
                need(integer <= ratio < integer+1, "exact resource floor")
                for wrong in (integer-1, integer+1):
                    need(not wrong <= ratio < wrong+1, "reject adjacent wrong floor")
                    floors += 1
                cap = integer+add
                need(cap <= TOTAL, "all whole-box record types paid")
                digest.update(f"B:{left},{right},{t},{a0},{a1}:{cmin}:{cmax}:{lower}:{bonus}:{cost}:{cap}\n".encode())
                if cap > peak[0]:
                    peak = cap, (left, right, t, a0, a1)
                count += 1
                ranks[t] += 1
        print("BLOCK", left, right, "boxes", count, "maximum", peak[0], flush=True)
    need(len(rows) == 19 and count == 40489 and floors == 80978
         and ranks[1] == 18601 and all(ranks[t] == 2432 for t in range(2, 11))
         and used == 18068,
         "complete fixed cover; no exclusions")
    need(peak == (TOTAL, (21564, 21579, 1, 3633, 3648)), "exact certificate maximum")
    print("CERTIFICATE", peak, "old-used", used, "DIGEST", digest.hexdigest(), flush=True)
    need(digest.hexdigest() == EXPECTED, "frozen every-box digest")
    print("PASS all40489 boxes; sharp source credit; four broken covers rejected")


if __name__ == "__main__":
    main()
