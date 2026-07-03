#!/usr/bin/env python3
"""X13 h=3 q-sweep for the terminal active-core node.

This verifier reuses the banked X12 h=3 machinery and scans the first prime
row p == 1 mod n above several exact powers n^alpha.  It is finite evidence
for the high-q vanishing route, not a monotonicity theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from collections import Counter
import json
import math
import os
import sys
from typing import Any

import verify_x12_h3_active_core_census as h3


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x13-h3-q-sweep",
    "x13_h3_q_sweep.json",
)

FAILS: list[str] = []
NCHECK = 0


@dataclass(frozen=True)
class SweepRow:
    n: int
    exponent_num: int
    exponent_den: int


ROWS = tuple(
    SweepRow(n, a, b)
    for n in (32, 64, 128, 256)
    for a, b in ((2, 1), (9, 4), (5, 2), (11, 4), (3, 1))
)

EXPECTED_NONTORAL_ACTIVE_CORES = {
    "n32_alpha_2": 0,
    "n32_alpha_9_4": 6,
    "n32_alpha_5_2": 0,
    "n32_alpha_11_4": 0,
    "n32_alpha_3": 0,
    "n64_alpha_2": 0,
    "n64_alpha_9_4": 0,
    "n64_alpha_5_2": 0,
    "n64_alpha_11_4": 0,
    "n64_alpha_3": 0,
    "n128_alpha_2": 18,
    "n128_alpha_9_4": 0,
    "n128_alpha_5_2": 0,
    "n128_alpha_11_4": 0,
    "n128_alpha_3": 0,
    "n256_alpha_2": 129,
    "n256_alpha_9_4": 0,
    "n256_alpha_5_2": 0,
    "n256_alpha_11_4": 0,
    "n256_alpha_3": 0,
}


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


def floor_nth_root(x: int, k: int) -> int:
    if x < 0 or k <= 0:
        raise ValueError("x >= 0 and k > 0 required")
    lo, hi = 0, 1
    while hi**k <= x:
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid**k <= x:
            lo = mid
        else:
            hi = mid
    return lo


def floor_power_fraction(n: int, numerator: int, denominator: int) -> int:
    return floor_nth_root(n**numerator, denominator)


def exponent_label(numerator: int, denominator: int) -> str:
    if denominator == 1:
        return str(numerator)
    return f"{numerator}_{denominator}"


def row_label(row: SweepRow) -> str:
    return f"n{row.n}_alpha_{exponent_label(row.exponent_num, row.exponent_den)}"


def first_prime_after_power(row: SweepRow) -> tuple[int, int]:
    floor_threshold = floor_power_fraction(row.n, row.exponent_num, row.exponent_den)
    p = floor_threshold + 1
    p += (1 - p) % row.n
    while not h3.is_prime(p):
        p += row.n
    return p, floor_threshold


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

    domain = h3.h1.mu_domain(p, row.n)
    key_arr, triple_arr, order = h3.signature_arrays(p, row.n, domain)
    partitions = h3.sp.charged_partitions(h3.sp.SplitRow(label, p, row.n, 2))

    collision_groups = 0
    collision_triples = 0
    max_group_size = 1
    group_size_hist = Counter()
    raw_active_cores = 0
    nontoral_active_cores = 0
    raw_anchored_partners = 0
    nontoral_anchored_partners = 0
    charged_partner_pairs = 0
    charged_reasons = Counter()
    nontoral_multiplicity = Counter()
    examples: list[dict[str, Any]] = []

    start = 0
    while start < len(order):
        end = start + 1
        code = key_arr[order[start]]
        while end < len(order) and key_arr[order[end]] == code:
            end += 1
        group_size = end - start
        if group_size > 1:
            collision_groups += 1
            collision_triples += group_size
            max_group_size = max(max_group_size, group_size)
            group_size_hist[group_size] += 1
            masks = [h3.mask_from_triple(int(triple_arr[order[i]])) for i in range(start, end)]
            for p_mask in masks:
                if not (p_mask & 1):
                    continue
                raw_here = 0
                nontoral_here = 0
                for q_mask in masks:
                    if q_mask == p_mask or (q_mask & p_mask):
                        continue
                    raw_here += 1
                    reason = h3.sp.charged_reason(q_mask, p_mask, partitions)
                    if reason is None:
                        nontoral_here += 1
                        if len(examples) < 8:
                            examples.append(
                                {
                                    "signature_code": int(code),
                                    "P_exponents": h3.exps_from_mask(p_mask, row.n),
                                    "Q_exponents": h3.exps_from_mask(q_mask, row.n),
                                }
                            )
                    else:
                        charged_partner_pairs += 1
                        charged_reasons[reason] += 1
                if raw_here:
                    raw_active_cores += 1
                    raw_anchored_partners += raw_here
                if nontoral_here:
                    nontoral_active_cores += 1
                    nontoral_anchored_partners += nontoral_here
                    nontoral_multiplicity[nontoral_here] += 1
        start = end

    check(
        f"{label}: partner accounting partitions raw partners",
        raw_anchored_partners == nontoral_anchored_partners + charged_partner_pairs,
        f"raw={raw_anchored_partners}, nontoral={nontoral_anchored_partners}, charged={charged_partner_pairs}",
    )
    check(
        f"{label}: active-core count matches pinned sweep value",
        nontoral_active_cores == EXPECTED_NONTORAL_ACTIVE_CORES[label],
        f"got={nontoral_active_cores}, expected={EXPECTED_NONTORAL_ACTIVE_CORES[label]}",
    )

    return {
        "label": label,
        "n": row.n,
        "h": 3,
        "t": 2,
        "exponent": (
            str(row.exponent_num)
            if row.exponent_den == 1
            else f"{row.exponent_num}/{row.exponent_den}"
        ),
        "first_prime_p_1_mod_n_after_floor_n_alpha": p,
        "floor_n_alpha": floor_threshold,
        "p_over_floor_n_alpha": f"{p}/{floor_threshold}",
        "triple_count": math.comb(row.n, 3),
        "signature_collision_groups": collision_groups,
        "signature_collision_triples": collision_triples,
        "max_signature_group_size": max_group_size,
        "signature_group_size_histogram": {str(k): v for k, v in sorted(group_size_hist.items())},
        "raw_active_cores": raw_active_cores,
        "raw_anchored_partner_pairs": raw_anchored_partners,
        "nontoral_active_cores": nontoral_active_cores,
        "nontoral_anchored_partner_pairs": nontoral_anchored_partners,
        "charged_partner_pairs": charged_partner_pairs,
        "charged_reasons": dict(sorted(charged_reasons.items())),
        "nontoral_partner_multiplicity_histogram": {
            str(k): v for k, v in sorted(nontoral_multiplicity.items())
        },
        "examples": examples,
    }


def build_certificate() -> dict[str, Any]:
    rows = [analyze_row(row) for row in ROWS]
    by_label = {row["label"]: row for row in rows}

    check(
        "n=128 and n=256 reproduce X12 q~n^2 counts",
        by_label["n128_alpha_2"]["nontoral_active_cores"] == 18
        and by_label["n256_alpha_2"]["nontoral_active_cores"] == 129,
    )
    check(
        "n=128 and n=256 vanish by the first q>n^(9/4) row",
        by_label["n128_alpha_9_4"]["nontoral_active_cores"] == 0
        and by_label["n256_alpha_9_4"]["nontoral_active_cores"] == 0,
    )
    check(
        "all checked rows vanish by the first q>n^(5/2) row",
        all(
            row["nontoral_active_cores"] == 0
            for row in rows
            if row["exponent"] in {"5/2", "11/4", "3"}
        ),
    )
    check(
        "sweep records non-monotonic finite-prime caution at n=32",
        by_label["n32_alpha_2"]["nontoral_active_cores"] == 0
        and by_label["n32_alpha_9_4"]["nontoral_active_cores"] == 6,
    )

    return {
        "task": "X13 h=3 high-q sweep",
        "node": "active_core_count_bound",
        "status": "EXACT FINITE EVIDENCE: h=3 nontoral active cores vanish by q>n^(5/2) in all checked rows through n=256; n=128 and n=256 vanish already by q>n^(9/4)",
        "scope": "h=3 anchored active-core census at first primes p == 1 mod n above exact n^alpha floors",
        "interpretation": (
            "This is evidence for the high-q vanishing route, not a monotonicity theorem. "
            "The n=32 row is deliberately retained because it shows finite-prime non-monotonicity."
        ),
        "rows": rows,
        "summary": {
            "rows_checked": [row["label"] for row in rows],
            "max_n": max(row["n"] for row in rows),
            "nonzero_rows": [
                row["label"] for row in rows if row["nontoral_active_cores"] > 0
            ],
            "all_alpha_5_2_and_above_zero": all(
                row["nontoral_active_cores"] == 0
                for row in rows
                if row["exponent"] in {"5/2", "11/4", "3"}
            ),
            "n128_n256_alpha_9_4_zero": (
                by_label["n128_alpha_9_4"]["nontoral_active_cores"] == 0
                and by_label["n256_alpha_9_4"]["nontoral_active_cores"] == 0
            ),
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
            f"{row['label']:18s} p={row['first_prime_p_1_mod_n_after_floor_n_alpha']:<9d} "
            f"collisions={row['signature_collision_groups']:<5d} "
            f"C3_nt={row['nontoral_active_cores']:<4d} "
            f"partners={row['nontoral_anchored_partner_pairs']:<4d}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        print("\nrecomputed summary:")
        print(json.dumps(cert["summary"], indent=2, sort_keys=True))
        return 1

    print(f"\nPASS: {NCHECK} X13 h=3 q-sweep checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
