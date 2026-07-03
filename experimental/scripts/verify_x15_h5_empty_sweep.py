#!/usr/bin/env python3
"""X15 h=5 empty-sweep for the terminal active-core node.

This verifier scans anchored h=5/t=4 terminal trades with a two-word
low-memory signature for the top-four elementary-symmetric sums.  In every
checked row the signature map is injective on 5-subsets, so there are no active
partners even before applying the paid strip.
"""

from __future__ import annotations

from array import array
from dataclasses import dataclass
from itertools import combinations
import json
import math
import os
import sys
from typing import Any

import numpy as np

import verify_h1_u1_toy_harness as h1
import verify_x12_h3_active_core_census as h3
import verify_x13_h3_q_sweep as x13


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x15-h5-empty-sweep",
    "x15_h5_empty_sweep.json",
)

FAILS: list[str] = []
NCHECK = 0


@dataclass(frozen=True)
class SweepRow:
    n: int
    exponent_num: int
    exponent_den: int


ROWS = (
    SweepRow(32, 2, 1),
    SweepRow(32, 9, 4),
    SweepRow(32, 5, 2),
    SweepRow(32, 3, 1),
    SweepRow(64, 2, 1),
    SweepRow(64, 9, 4),
    SweepRow(64, 5, 2),
    SweepRow(64, 11, 4),
    SweepRow(64, 3, 1),
)


def check(name: str, cond: bool, detail: str = "") -> None:
    global NCHECK
    NCHECK += 1
    tag = "PASS" if cond else "FAIL"
    line = f"[{tag}] {name}"
    if detail:
        line += f"   ({detail})"
    print(line, flush=True)
    if not cond:
        FAILS.append(name)


def row_label(row: SweepRow) -> str:
    return f"n{row.n}_alpha_{x13.exponent_label(row.exponent_num, row.exponent_den)}"


def first_prime_after_power(row: SweepRow) -> tuple[int, int]:
    floor_threshold = x13.floor_power_fraction(row.n, row.exponent_num, row.exponent_den)
    p = floor_threshold + 1
    p += (1 - p) % row.n
    while not h3.is_prime(p):
        p += row.n
    return p, floor_threshold


def code5(comb: tuple[int, int, int, int, int]) -> int:
    out = 0
    for shift, value in enumerate(comb):
        out |= value << (8 * shift)
    return out


def exps5(code: int) -> list[int]:
    return [(code >> (8 * shift)) & 255 for shift in range(5)]


def signature_arrays(
    p: int, n: int, domain: list[int]
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return sorted h=5/top-4 signature arrays."""
    h = 5
    t = 4
    max_half_key = p**2 - 1
    check(
        f"n={n}, p={p}: h=5 two-word signature halves fit uint64",
        max_half_key < 2**64,
        f"p^2={p**2}",
    )

    key_lo = array("Q")
    key_hi = array("Q")
    codes = array("Q")
    for comb in combinations(range(n), h):
        e = [0] * (t + 1)
        e[0] = 1
        for i in comb:
            x = domain[i]
            for r in range(t, 0, -1):
                e[r] = (e[r] + x * e[r - 1]) % p
        key_lo.append(e[1] + p * e[2])
        key_hi.append(e[3] + p * e[4])
        codes.append(code5(comb))

    key_lo_arr = np.frombuffer(key_lo, dtype=np.uint64).copy()
    key_hi_arr = np.frombuffer(key_hi, dtype=np.uint64).copy()
    code_arr = np.frombuffer(codes, dtype=np.uint64).copy()
    order = np.lexsort((key_lo_arr, key_hi_arr))
    return key_lo_arr, key_hi_arr, code_arr, order


def analyze_row(row: SweepRow) -> dict[str, Any]:
    label = row_label(row)
    p, floor_threshold = first_prime_after_power(row)
    check(f"{label}: p is prime", h3.is_prime(p), f"p={p}")
    check(f"{label}: p == 1 mod n", (p - 1) % row.n == 0)
    check(
        f"{label}: p exceeds floor(n^alpha)",
        p > floor_threshold,
        f"p={p}, floor={floor_threshold}",
    )

    domain = h1.mu_domain(p, row.n)
    key_lo_arr, key_hi_arr, code_arr, order = signature_arrays(p, row.n, domain)

    collision_groups = 0
    collision_subsets = 0
    max_group_size = 1
    collision_examples: list[dict[str, Any]] = []

    start = 0
    while start < len(order):
        end = start + 1
        key_lo = key_lo_arr[order[start]]
        key_hi = key_hi_arr[order[start]]
        while (
            end < len(order)
            and key_lo_arr[order[end]] == key_lo
            and key_hi_arr[order[end]] == key_hi
        ):
            end += 1
        size = end - start
        if size > 1:
            collision_groups += 1
            collision_subsets += size
            max_group_size = max(max_group_size, size)
            if len(collision_examples) < 5:
                collision_examples.append(
                    {
                        "signature_low": int(key_lo),
                        "signature_high": int(key_hi),
                        "subsets": [exps5(int(code_arr[order[i]])) for i in range(start, end)],
                    }
                )
        start = end

    check(
        f"{label}: no h=5 top-four signature collisions",
        collision_groups == 0,
        f"collision_groups={collision_groups}",
    )

    return {
        "label": label,
        "n": row.n,
        "h": 5,
        "t": 4,
        "exponent": (
            str(row.exponent_num)
            if row.exponent_den == 1
            else f"{row.exponent_num}/{row.exponent_den}"
        ),
        "first_prime_p_1_mod_n_after_floor_n_alpha": p,
        "floor_n_alpha": floor_threshold,
        "p_over_floor_n_alpha": f"{p}/{floor_threshold}",
        "subset_count": math.comb(row.n, 5),
        "signature_collision_groups": collision_groups,
        "signature_collision_subsets": collision_subsets,
        "max_signature_group_size": max_group_size,
        "raw_active_cores": 0,
        "raw_anchored_partner_pairs": 0,
        "nontoral_active_cores": 0,
        "nontoral_anchored_partner_pairs": 0,
        "collision_examples": collision_examples,
    }


def build_certificate() -> dict[str, Any]:
    rows = [analyze_row(row) for row in ROWS]
    check(
        "all checked h=5 rows have injective top-four signatures",
        all(row["signature_collision_groups"] == 0 for row in rows),
    )
    check(
        "sweep includes n=64 through alpha=3",
        any(row["label"] == "n64_alpha_3" for row in rows),
    )
    check(
        "sweep includes n=32 through alpha=3",
        any(row["label"] == "n32_alpha_3" for row in rows),
    )

    return {
        "task": "X15 h=5 empty sweep",
        "node": "active_core_count_bound",
        "status": "EXACT FINITE EVIDENCE: h=5 has no active partners before stripping in every checked row",
        "scope": (
            "anchored h=5/t=4 split pairs; since the top-four signature is "
            "injective on all checked 5-subsets, no active-core partners exist"
        ),
        "coverage_note": (
            "top-four signatures are stored as two base-p uint64 words "
            "(e1+p*e2, e3+p*e4), extending n=64 through alpha=3 while keeping "
            "the exact low-memory sort"
        ),
        "rows": rows,
        "summary": {
            "rows_checked": [row["label"] for row in rows],
            "max_n": max(row["n"] for row in rows),
            "max_subset_count": max(row["subset_count"] for row in rows),
            "collision_rows": [
                row["label"] for row in rows if row["signature_collision_groups"] > 0
            ],
        },
        "checks": NCHECK,
    }


def main() -> int:
    write = "--write-certificate" in sys.argv
    cert = build_certificate()
    if write:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w", encoding="utf-8") as fh:
            json.dump(cert, fh, indent=2, sort_keys=True)
            fh.write("\n")
        print(f"[write] {CERT}")

    expected = None
    if os.path.exists(CERT):
        with open(CERT, encoding="utf-8") as fh:
            expected = json.load(fh)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", cert == expected)

    print("\nrow summary:")
    for row in cert["rows"]:
        print(
            f"{row['label']:18s} p={row['first_prime_p_1_mod_n_after_floor_n_alpha']:<8d} "
            f"subsets={row['subset_count']:<8d} collisions={row['signature_collision_groups']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        print("\nrecomputed summary:")
        print(json.dumps(cert["summary"], indent=2, sort_keys=True))
        return 1

    print(f"\nPASS: {NCHECK} X15 h=5 empty-sweep checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
