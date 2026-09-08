"""Independent integer certificate using the preceding independent cost formulas."""

import hashlib
import importlib.util
from math import prod
from pathlib import Path


path = Path(__file__).resolve().parents[1]/"rate_half_mca_weighted_collision_interval/verify_audit.py"
spec = importlib.util.spec_from_file_location("independent_weighted_costs", path)
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
D, R, GAP, NEAR = 67466, 1048576, 67472, 134944
LO, HI, TOTAL = 21500, 21799, 274956328426911303
TRIGGER = 274960000000000000
EXPECTED = "e9087d3555bafce49cba6c75e09c0c6eb45a5025d057f5f20e9b762f48c0fa86"


def check(ok, why):
    if not ok:
        raise ValueError(why)


def main():
    digest = hashlib.sha256()
    left, blocks, count, used, floors = LO, 0, 0, 0, 0
    ranks, peak = [0]*10, (0, None)
    while left <= HI:
        right = min(left+15, HI)
        n0, n1 = R+left, R+right
        check(n0 > 12 and n0 >= 10*(right-10), "source length and first moment branch")
        Tmax = n1*(right-11)//10
        credit = b.frac(11, 2*(n1-12))
        resource = prod(range(n1-11, n1+1))
        high = b.frac(10488*(GAP+left)*prod(range(GAP+1, GAP+11)), 125)
        addback = right-11+Tmax//2+NEAR
        digest.update(f"R:{left},{right}:{b.printed(credit)}:{Tmax}:{resource}:{addback}\n".encode())
        for t in range(1, 11):
            top = min(right-11+t, right-6001 if t == 1 else right)
            parts = 1024 if t == 1 else 128
            width = (top-t+parts)//parts
            first = t
            while first <= top:
                last = min(first+width-1, top)
                lower, bonus, cmin, cmax = b.root_costs(left, right, t, first, last, credit, Tmax)
                cost = b.mul((12, 1), lower)
                preliminary = b.minimum(cost, high)
                if resource*preliminary[1]//preliminary[0]+addback > TRIGGER:
                    cost = b.maximum(cost, b.mul((12, 1),
                                     b.add(b.old_cost(left, right, t, first, last), bonus)))
                    used += 1
                cost = b.minimum(cost, high)
                quotient, remainder = divmod(resource*cost[1], cost[0])
                check(0 <= remainder < cost[0], "exact Euclidean division")
                for wrong in (quotient-1, quotient+1):
                    check(not 0 <= resource*cost[1]-wrong*cost[0] < cost[0],
                          "reject adjacent wrong resource floor")
                    floors += 1
                cap = quotient+addback
                check(cap <= TOTAL, "all core and source parameters in box paid")
                digest.update(f"B:{left},{right},{t},{first},{last}:{b.printed(cmin)}:{b.printed(cmax)}:{b.printed(lower)}:{b.printed(bonus)}:{b.printed(cost)}:{cap}\n".encode())
                if cap > peak[0]:
                    peak = cap, (left, right, t, first, last)
                count += 1
                ranks[t-1] += 1
                first = last+1
            check(first == top+1, "complete exact size cover")
        print("AUDIT BLOCK", left, right, "boxes", count, "maximum", peak[0], flush=True)
        blocks += 1
        left = right+1
    check(left == HI+1 and blocks == 19 and count == 40489 and floors == 80978
          and ranks[0] == 18601 and set(ranks[1:]) == {2432} and used == 18068,
          "full integer certificate inventory")
    check(peak == (TOTAL, (21564, 21579, 1, 3633, 3648)), "exact attained certificate maximum")
    print("CERTIFICATE", peak, "old-used", used, "DIGEST", digest.hexdigest(), flush=True)
    check(digest.hexdigest() == EXPECTED, "every certificate entry agrees")
    print("PASS independent integer certificate; no primary or Fraction import")


if __name__ == "__main__":
    main()
