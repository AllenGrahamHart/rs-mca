#!/usr/bin/env python3
"""OCC-2 verifier: depth-cell residual occupancy audit.

The W2/A2 routing table reduces every partial-tangent pair to a depth cell

    d = r-k,        s = A-r,        d+s=t,

with 1 <= d <= t-2 and 2 <= s <= t-1.  For a fixed anchor support T0 of
size A, the formal number of possible overlap cores at depth d is

    C(A, k+d) = C(A, s).

This verifier certifies the obstruction to the naive occupancy proof: even a
one-per-formal-depth-cell family is already super-linear at every clean-rate
candidate.  Therefore A2 needs an alignment/post-strip incidence theorem
that bounds the active depth-cell shadow, not just a constant emission cap per
cell.

Run:
  python3 experimental/scripts/verify_occ2_depth_cell_occupancy.py
Refresh certificate:
  python3 experimental/scripts/verify_occ2_depth_cell_occupancy.py --write-certificate
"""

from __future__ import annotations

import json
import math
import os
import sys
from dataclasses import dataclass


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "occ2-depth-cell-occupancy",
    "occ2_depth_cell_occupancy.json",
)

FAILS: list[str] = []
NCHECK = 0


def check(name: str, cond: bool, detail: str = "") -> None:
    global NCHECK
    NCHECK += 1
    tag = "PASS" if cond else "FAIL"
    line = f"[{tag}] {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    if not cond:
        FAILS.append(name)


def log2_big(x: int) -> float:
    if x <= 0:
        raise ValueError("log2 input must be positive")
    bits = x.bit_length()
    if bits <= 53:
        return math.log2(x)
    return bits - 53 + math.log2(x >> (bits - 53))


@dataclass(frozen=True)
class CleanRow:
    name: str
    n: int
    k: int
    A: int

    @property
    def t(self) -> int:
        return self.A - self.k


CLEAN_ROWS = [
    CleanRow("RowC_rate_1_4", 2**10, 2**8, 261),
    CleanRow("RowC_rate_1_8", 2**10, 2**7, 133),
    CleanRow("RowC_rate_1_16", 2**10, 2**6, 67),
    CleanRow("prize_rate_1_4", 2**41, 2**39, 2**39 + 2**33 + 1),
    CleanRow("prize_rate_1_8", 2**41, 2**38, 2**38 + 2**33 + 1),
    CleanRow("prize_rate_1_16", 2**41, 2**37, 2**37 + 2**32 + 1),
]


def sampled_s_values(t: int) -> list[int]:
    """Small complementary codimensions s give exact cheap lower bounds."""
    return list(range(2, min(t - 1, 4) + 1))


def row_depth_audit(row: CleanRow) -> dict[str, object]:
    n, k, A, t = row.n, row.k, row.A, row.t
    partial_depths = max(0, t - 2)
    check(
        f"{row.name}: partial tangent band is nonempty",
        partial_depths > 0,
        f"t={t}, partial_depths={partial_depths}",
    )

    samples: list[dict[str, object]] = []
    for s in sampled_s_values(t):
        d = t - s
        cores = math.comb(A, s)
        over_n = log2_big(cores) - math.log2(n)
        check(
            f"{row.name}: depth d=t-{s} has super-linear formal core lattice",
            cores > n,
            f"C(A,{s})={cores}, n={n}",
        )
        check(
            f"{row.name}: sampled depth d=t-{s} is in the W2 partial band",
            1 <= d <= t - 2 and 2 <= s <= t - 1 and d + s == t,
            f"d={d}, s={s}, t={t}",
        )
        samples.append(
            {
                "s": s,
                "d": d,
                "formal_overlap_cores_in_anchor": cores,
                "log2_formal_overlap_cores": log2_big(cores),
                "log2_over_n": over_n,
            }
        )

    blocking = samples[0]
    check(
        f"{row.name}: one-per-cell packing already exceeds linear budget",
        int(blocking["formal_overlap_cores_in_anchor"]) > n,
        f"s={blocking['s']}, count={blocking['formal_overlap_cores_in_anchor']}",
    )

    return {
        "name": row.name,
        "n": n,
        "k": k,
        "A": A,
        "t": t,
        "partial_depth_count": partial_depths,
        "formal_cell_formula": "for fixed anchor T0 and s=A-r=t-d, count C(A,s)",
        "sampled_exact_depths": samples,
        "blocking_depth": {
            "s": blocking["s"],
            "d": blocking["d"],
            "formal_cells": blocking["formal_overlap_cores_in_anchor"],
            "log2_over_n": blocking["log2_over_n"],
        },
    }


def build_result() -> dict[str, object]:
    rows = [row_depth_audit(row) for row in CLEAN_ROWS]
    check(
        "all clean rows have a certified super-linear blocking depth",
        all(row["blocking_depth"]["formal_cells"] > row["n"] for row in rows),
    )
    check(
        "Row-C rows are checked at every partial depth",
        [len(row["sampled_exact_depths"]) for row in rows[:3]] == [3, 3, 1],
    )
    check(
        "prize rows use only small-s exact binomials",
        all({sample["s"] for sample in row["sampled_exact_depths"]} == {2, 3, 4} for row in rows[3:]),
    )

    return {
        "node": "a2_depth_cell_residual_occupancy",
        "task": "OCC-2",
        "status": "CONDITIONAL / RESIDUE: naive depth-cell packing fails",
        "verdict": (
            "A constant per-depth-cell emission cap does not imply the A2 "
            "occupancy bound by summing over the formal cell lattice.  The "
            "formal lattice is already super-linear inside one anchor at every "
            "clean-rate candidate."
        ),
        "named_residue": "a2_depth_cell_active_shadow_bound",
        "required_replacement_statement": (
            "After the unified paid strip, for each fixed anchor support T0 "
            "and depth d, the occupied tangent-depth cells (or their weighted "
            "emissions) form a linear active shadow, unless a positive-density "
            "subfamily is one of the paid tangent, quotient/pullback, "
            "dihedral, extension, or moment/PTE structures."
        ),
        "rows": rows,
        "checks": NCHECK,
    }


def main() -> int:
    write = "--write-certificate" in sys.argv
    result = build_result()

    if write:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, sort_keys=True)
            f.write("\n")
        print(f"[write] {CERT}")

    expected = None
    if os.path.exists(CERT):
        with open(CERT, encoding="utf-8") as f:
            expected = json.load(f)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", result == expected)

    print("\nrow summary:")
    for row in result["rows"]:
        block = row["blocking_depth"]
        print(
            f"{row['name']:16s} t={row['t']:<11d} "
            f"d=t-{block['s']} cells={block['formal_cells']} "
            f"log2(cells/n)={block['log2_over_n']:.4f}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        print("\nrecomputed summary:")
        print(json.dumps(result, indent=2, sort_keys=True))
        return 1

    print(f"\nPASS: {NCHECK} OCC-2 depth-cell occupancy checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
