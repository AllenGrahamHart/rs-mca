#!/usr/bin/env python3
"""X19 h=8/t=7 exact signature sweep for the terminal active-core node.

This verifier tests the largest n=32 minimal terminal size that is still
comfortable on a low-memory machine.  It scans all 8-subsets of mu_32 at the
standard alpha rows and groups them by the top seven elementary-symmetric sums.
The global signature map is not injective at h=8: the unique collision is the
cyclic partition into four cosets modulo 4.  That collision is paid by the
cyclic pullback strip, so the post-strip non-toral residue is still zero.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
import gc
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
    "x19-h8-n32-sweep",
    "x19_h8_n32_sweep.json",
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
    SweepRow(32, 11, 4),
    SweepRow(32, 3, 1),
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


def signature_tuple_for_comb(comb: tuple[int, ...], p: int, domain: list[int]) -> tuple[int, int, int, int]:
    t = 7
    e = [0] * (t + 1)
    e[0] = 1
    for i in comb:
        x = domain[i]
        for r in range(t, 0, -1):
            e[r] = (e[r] + x * e[r - 1]) % p
    return (e[1] + p * e[2], e[3] + p * e[4], e[5] + p * e[6], e[7])


def expected_cyclic_cosets(n: int) -> list[list[int]]:
    return [[r + 4 * k for k in range(n // 4)] for r in range(4)]


def signature_arrays(
    p: int, n: int, domain: list[int]
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return h=8/top-7 signature arrays sorted by four key words."""
    h = 8
    subset_count = math.comb(n, h)
    max_pair_key = p**2 - 1
    check(
        f"n={n}, p={p}: paired h=8 signature words fit uint64",
        max_pair_key < 2**64,
        f"p^2={p**2}",
    )

    key_12 = np.empty(subset_count, dtype=np.uint64)
    key_34 = np.empty(subset_count, dtype=np.uint64)
    key_56 = np.empty(subset_count, dtype=np.uint64)
    key_7 = np.empty(subset_count, dtype=np.uint64)

    for idx, comb in enumerate(combinations(range(n), h)):
        k12, k34, k56, k7 = signature_tuple_for_comb(comb, p, domain)
        key_12[idx] = k12
        key_34[idx] = k34
        key_56[idx] = k56
        key_7[idx] = k7
    return key_12, key_34, key_56, key_7


def expected_collision_examples(
    p: int,
    n: int,
    domain: list[int],
) -> list[dict[str, Any]]:
    subsets = expected_cyclic_cosets(n)
    signatures = [signature_tuple_for_comb(tuple(subset), p, domain) for subset in subsets]
    return [
        {
            "signature_12": int(signatures[0][0]),
            "signature_34": int(signatures[0][1]),
            "signature_56": int(signatures[0][2]),
            "signature_7": int(signatures[0][3]),
            "subsets": subsets,
            "cyclic_reason": "four cosets of the subgroup <zeta^4>; locator polynomials X^8 - zeta^(8r)",
        }
    ]


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
    key_12, key_34, key_56, key_7 = signature_arrays(p, row.n, domain)
    order = np.lexsort((key_12, key_34, key_56, key_7))

    collision_groups = 0
    collision_subsets = 0
    max_group_size = 1
    collision_signatures: list[tuple[int, int, int, int]] = []

    start = 0
    while start < len(order):
        end = start + 1
        k12 = key_12[order[start]]
        k34 = key_34[order[start]]
        k56 = key_56[order[start]]
        k7 = key_7[order[start]]
        while (
            end < len(order)
            and key_12[order[end]] == k12
            and key_34[order[end]] == k34
            and key_56[order[end]] == k56
            and key_7[order[end]] == k7
        ):
            end += 1
        size = end - start
        if size > 1:
            collision_groups += 1
            collision_subsets += size
            max_group_size = max(max_group_size, size)
            if len(collision_signatures) < 5:
                collision_signatures.append((int(k12), int(k34), int(k56), int(k7)))
        start = end

    del order, key_12, key_34, key_56, key_7
    gc.collect()

    expected_examples = expected_collision_examples(p, row.n, domain)
    expected_signature = (
        expected_examples[0]["signature_12"],
        expected_examples[0]["signature_34"],
        expected_examples[0]["signature_56"],
        expected_examples[0]["signature_7"],
    )
    expected_paid_collision = (
        collision_groups == 1
        and collision_subsets == 4
        and max_group_size == 4
        and collision_signatures == [expected_signature]
        and expected_signature == (0, 0, 0, 0)
    )

    check(
        f"{label}: unique h=8 collision is the cyclic mod-4 coset group",
        expected_paid_collision,
        f"groups={collision_groups}, subsets={collision_subsets}, signature={collision_signatures[:1]}",
    )

    return {
        "label": label,
        "n": row.n,
        "h": 8,
        "t": 7,
        "exponent": (
            str(row.exponent_num)
            if row.exponent_den == 1
            else f"{row.exponent_num}/{row.exponent_den}"
        ),
        "first_prime_p_1_mod_n_after_floor_n_alpha": p,
        "floor_n_alpha": floor_threshold,
        "p_over_floor_n_alpha": f"{p}/{floor_threshold}",
        "subset_count": math.comb(row.n, 8),
        "signature_collision_groups": collision_groups,
        "signature_collision_subsets": collision_subsets,
        "max_signature_group_size": max_group_size,
        "global_signature_injective": collision_groups == 0,
        "cyclic_paid_collision_groups": 1 if expected_paid_collision else 0,
        "raw_active_cores": 1 if expected_paid_collision else None,
        "raw_anchored_partner_pairs": 3 if expected_paid_collision else None,
        "cyclic_charged_partner_pairs": 3 if expected_paid_collision else None,
        "nontoral_active_cores": 0 if expected_paid_collision else None,
        "nontoral_anchored_partner_pairs": 0 if expected_paid_collision else None,
        "collision_examples": expected_examples if expected_paid_collision else [],
    }


def build_certificate() -> dict[str, Any]:
    rows = [analyze_row(row) for row in ROWS]
    all_paid = all(row["cyclic_paid_collision_groups"] == 1 for row in rows)
    all_non_toral_zero = all(row["nontoral_anchored_partner_pairs"] == 0 for row in rows)
    check("all checked h=8 rows have exactly one cyclic-paid collision group", all_paid)
    check("all checked h=8 rows have zero post-strip non-toral partners", all_non_toral_zero)
    check(
        "sweep includes n=32 through alpha=3",
        any(row["label"] == "n32_alpha_3" for row in rows),
    )
    check(
        "h=8 n=32 rows stay below eleven million subsets per row",
        max(row["subset_count"] for row in rows) < 11_000_000,
    )

    return {
        "task": "X19 h=8 n=32 signature sweep",
        "node": "active_core_count_bound",
        "status": (
            "EXACT FINITE EVIDENCE: h=8 has one raw cyclic-paid collision group "
            "and zero post-strip non-toral partners in every checked n=32 row"
        ),
        "scope": (
            "h=8/t=7 split pairs at n=32; the top-seven signature has exactly "
            "one collision group, the cyclic coset partition modulo 4"
        ),
        "coverage_note": (
            "n=32 is checked through alpha=3; this low-memory packet sorts "
            "C(32,8)=10518300 subsets per row using four uint64 key arrays"
        ),
        "signature_encoding": "(e1+p*e2, e3+p*e4, e5+p*e6, e7)",
        "interpretation": (
            "Global signature injectivity is false at h=8, but only by a paid "
            "cyclic pullback family: the four cosets r mod 4 have locator "
            "polynomials X^8 - zeta^(8r)."
        ),
        "rows": rows,
        "summary": {
            "rows_checked": [row["label"] for row in rows],
            "max_n": max(row["n"] for row in rows),
            "max_subset_count": max(row["subset_count"] for row in rows),
            "global_signature_injective_rows": [
                row["label"] for row in rows if row["global_signature_injective"]
            ],
            "collision_rows": [
                row["label"] for row in rows if row["signature_collision_groups"] > 0
            ],
            "post_strip_nontoral_rows": [
                row["label"] for row in rows if row["nontoral_anchored_partner_pairs"]
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
            f"subsets={row['subset_count']:<9d} collisions={row['signature_collision_groups']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        print("\nrecomputed summary:")
        print(json.dumps(cert["summary"], indent=2, sort_keys=True))
        return 1

    print(f"\nPASS: {NCHECK} X19 h=8 n=32 signature-sweep checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
