"""Small exact multi-defect counts and exhaustive integer-ledger controls."""

import importlib.util
from itertools import combinations, product
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("credited_rank",
    ROOT/"critical/nodes/mca_fiber_contraction_core_basis_resource/verify.py")
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


def need(ok, why):
    if not ok:
        raise ValueError(why)


def main():
    p, rank, core_size = 17, 3, 7
    for defects in (1, 2, 3):
        m = core_size+defects
        evaluations = [[pow(x, j, p) for j in range(rank)] for x in range(m)]
        values = [0]*core_size+[1]*defects
        normals = [row+[v] for row, v in zip(evaluations, values)]
        bases = [indices for indices in combinations(range(core_size), rank)
                 if c.rank([evaluations[x] for x in indices], p) == rank]
        inserted = {tuple(sorted(indices+(defect,)))
                    for indices in bases for defect in range(core_size, m)}
        need(len(inserted) == defects*len(bases), "recoverable distinct defects")
        need(all(c.rank([normals[x] for x in indices], p) == rank+1 for indices in inserted),
             "all inserted tuples independent")
        need(factorial(rank+1)*len(inserted) == defects*(rank+1)*factorial(rank)*len(bases),
             "ordered insertion factor")
        raw = min(sum(c.evaluate(poly, x, p) != values[x] for x in range(m))
                  for poly in product(range(p), repeat=rank))
        need(raw == defects, "actual minimum over the entire polynomial carrier")
        need(c.rank([row+[value] for row, value in zip(evaluations, values)], p) == rank+1,
             "full-code pair badness of scalar-zero support")
    count = 0
    for raw_values in product(range(1, 7), repeat=4):
        W = sum(min(raw, 4) for raw in raw_values)
        for t in (1, 2, 3):
            low = sum(raw <= t for raw in raw_values)
            nested = sum(sum(raw <= j for raw in raw_values) for j in range(1, t+1))
            need((t+1)*len(raw_values)-nested == sum(min(raw, t+1) for raw in raw_values),
                 "exact cumulative flag identity")
            need((t+1)*len(raw_values)-t*low <= W, "exact weighted ledger")
            count += 1
    need(count == 3888, "complete small ledger inventory")
    owner_cases = 0
    for c_min in (1, 2, 3):
        for raw_values in product(range(c_min, 4), repeat=4):
            used = sum(raw_values)
            for spare in range(4):
                need(sum(4-raw for raw in raw_values) <= (4-c_min)*(used+spare)//c_min,
                     "same-owner weighted deficit")
                owner_cases += 1
    need(4*4 > 4, "dropping multiplicities would fail on four raw-four labels")
    need(owner_cases == 392, "complete small owner inventory")
    print("PASS three actual multi-defect sources,", count, "flag cases and", owner_cases, "owner cases")
    print("Core-basis and high-raw hypotheses remain mathematical inputs, not numerical discoveries")


if __name__ == "__main__":
    main()
