#!/usr/bin/env python3
"""X14 h=4 charged-sweep for the terminal active-core node.

This is the first actual campaign trade size when t=3.  The verifier scans
anchored h=4 trades with equal top-three elementary symmetric sums and checks
that every active partner in the tested rows is charged by the existing
cyclic/dihedral SP-CENSUS strip.  It is exact finite evidence, not a proof of
uniform h=4 emptiness.
"""

from __future__ import annotations

from array import array
from collections import Counter
from dataclasses import dataclass
from itertools import combinations
import json
import math
import os
import sys
from typing import Any

import numpy as np

import verify_h1_u1_toy_harness as h1
import verify_sp_census_split_pairs as sp
import verify_x13_h3_q_sweep as x13
import verify_x12_h3_active_core_census as h3


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x14-h4-charged-sweep",
    "x14_h4_charged_sweep.json",
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
    for n in (32, 64, 128)
    for a, b in ((2, 1), (9, 4), (5, 2), (3, 1))
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


def code4(comb: tuple[int, int, int, int]) -> int:
    i, j, k, ell = comb
    return i | (j << 8) | (k << 16) | (ell << 24)


def exps4(code: int) -> list[int]:
    return [(code >> (8 * s)) & 255 for s in range(4)]


def mask4(code: int) -> int:
    out = 0
    for i in exps4(code):
        out |= 1 << i
    return out


def signature_arrays(p: int, n: int, domain: list[int]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return sorted h=4 signature arrays.

    Subsets are stored as four-byte exponent tuples instead of bit masks, so
    the scan remains compact through n=128.
    """
    keys = array("Q")
    codes = array("I")
    p2 = p * p
    check(f"n={n}, p={p}: h=4 signature fits uint64", p2 * (p - 1) + p * (p - 1) + (p - 1) < 2**64)
    for comb in combinations(range(n), 4):
        e = [0, 0, 0, 0]
        e[0] = 1
        for i in comb:
            x = domain[i]
            for r in range(3, 0, -1):
                e[r] = (e[r] + x * e[r - 1]) % p
        keys.append(e[1] + p * e[2] + p2 * e[3])
        codes.append(code4(comb))
    key_arr = np.frombuffer(keys, dtype=np.uint64).copy()
    code_arr = np.frombuffer(codes, dtype=np.uint32).copy()
    order = np.argsort(key_arr, kind="stable")
    return key_arr, code_arr, order


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
    key_arr, code_arr, order = signature_arrays(p, row.n, domain)
    partitions = sp.charged_partitions(sp.SplitRow(label, p, row.n, 3))

    collision_groups = 0
    collision_subsets = 0
    max_group_size = 1
    group_size_hist = Counter()
    raw_active_cores = 0
    raw_anchored_partners = 0
    charged_partner_pairs = 0
    nontoral_active_cores = 0
    nontoral_partner_pairs = 0
    charged_reasons = Counter()
    active_multiplicity_hist = Counter()
    nontoral_examples: list[dict[str, Any]] = []
    charged_examples: list[dict[str, Any]] = []

    start = 0
    while start < len(order):
        end = start + 1
        code = key_arr[order[start]]
        while end < len(order) and key_arr[order[end]] == code:
            end += 1
        size = end - start
        if size > 1:
            collision_groups += 1
            collision_subsets += size
            max_group_size = max(max_group_size, size)
            group_size_hist[size] += 1
            masks = [mask4(int(code_arr[order[i]])) for i in range(start, end)]
            for p_mask in masks:
                if not (p_mask & 1):
                    continue
                raw_here = 0
                nontoral_here = 0
                for q_mask in masks:
                    if q_mask == p_mask or (q_mask & p_mask):
                        continue
                    raw_here += 1
                    reason = sp.charged_reason(q_mask, p_mask, partitions)
                    if reason is None:
                        nontoral_here += 1
                        if len(nontoral_examples) < 8:
                            nontoral_examples.append(
                                {
                                    "signature_code": int(code),
                                    "P_exponents": sp.exps(p_mask, row.n),
                                    "Q_exponents": sp.exps(q_mask, row.n),
                                }
                            )
                    else:
                        charged_partner_pairs += 1
                        charged_reasons[reason] += 1
                        if len(charged_examples) < 8:
                            charged_examples.append(
                                {
                                    "reason": reason,
                                    "signature_code": int(code),
                                    "P_exponents": sp.exps(p_mask, row.n),
                                    "Q_exponents": sp.exps(q_mask, row.n),
                                }
                            )
                if raw_here:
                    raw_active_cores += 1
                    raw_anchored_partners += raw_here
                    active_multiplicity_hist[raw_here] += 1
                if nontoral_here:
                    nontoral_active_cores += 1
                    nontoral_partner_pairs += nontoral_here
        start = end

    check(
        f"{label}: active partner accounting partitions raw partners",
        raw_anchored_partners == charged_partner_pairs + nontoral_partner_pairs,
        f"raw={raw_anchored_partners}, charged={charged_partner_pairs}, nontoral={nontoral_partner_pairs}",
    )
    check(
        f"{label}: no h=4 non-toral active partners after cyclic/dihedral strip",
        nontoral_partner_pairs == 0 and nontoral_active_cores == 0,
        f"active={nontoral_active_cores}, pairs={nontoral_partner_pairs}",
    )
    if raw_anchored_partners:
        check(
            f"{label}: every charged h=4 partner is cyclic",
            all(reason.startswith("cyclic:") for reason in charged_reasons),
            str(dict(charged_reasons)),
        )

    return {
        "label": label,
        "n": row.n,
        "h": 4,
        "t": 3,
        "exponent": (
            str(row.exponent_num)
            if row.exponent_den == 1
            else f"{row.exponent_num}/{row.exponent_den}"
        ),
        "first_prime_p_1_mod_n_after_floor_n_alpha": p,
        "floor_n_alpha": floor_threshold,
        "p_over_floor_n_alpha": f"{p}/{floor_threshold}",
        "subset_count": math.comb(row.n, 4),
        "signature_collision_groups": collision_groups,
        "signature_collision_subsets": collision_subsets,
        "max_signature_group_size": max_group_size,
        "signature_group_size_histogram": {str(k): v for k, v in sorted(group_size_hist.items())},
        "raw_active_cores": raw_active_cores,
        "raw_anchored_partner_pairs": raw_anchored_partners,
        "charged_partner_pairs": charged_partner_pairs,
        "charged_reasons": dict(sorted(charged_reasons.items())),
        "nontoral_active_cores": nontoral_active_cores,
        "nontoral_anchored_partner_pairs": nontoral_partner_pairs,
        "active_partner_multiplicity_histogram": {
            str(k): v for k, v in sorted(active_multiplicity_hist.items())
        },
        "charged_examples": charged_examples,
        "nontoral_examples": nontoral_examples,
    }


def build_certificate() -> dict[str, Any]:
    rows = [analyze_row(row) for row in ROWS]
    check(
        "all checked h=4 rows have zero post-strip non-toral residue",
        all(row["nontoral_anchored_partner_pairs"] == 0 for row in rows),
    )
    check(
        "the sweep includes n=128 at alpha=2",
        any(row["label"] == "n128_alpha_2" for row in rows),
    )
    check(
        "n=128 alpha=2 has nontrivial active h=4 partners before charging",
        next(row for row in rows if row["label"] == "n128_alpha_2")["raw_anchored_partner_pairs"] > 0,
    )
    check(
        "every nonzero active h=4 cell charges through cyclic partitions",
        all(
            all(reason.startswith("cyclic:") for reason in row["charged_reasons"])
            for row in rows
            if row["raw_anchored_partner_pairs"] > 0
        ),
    )

    return {
        "task": "X14 h=4 charged sweep",
        "node": "active_core_count_bound",
        "status": "EXACT FINITE EVIDENCE: h=4 post-cyclic/dihedral non-toral residue is zero in all checked rows through n=128",
        "scope": "anchored h=4 split pairs with e_i(P)=e_i(Q), i=1,2,3, at first p == 1 mod n above n^alpha",
        "interpretation": (
            "This is the first actual campaign trade size for t=3.  The scan is "
            "finite evidence only; it does not prove uniform h=4 emptiness."
        ),
        "rows": rows,
        "summary": {
            "rows_checked": [row["label"] for row in rows],
            "max_n": max(row["n"] for row in rows),
            "nonzero_active_rows_before_charging": [
                row["label"] for row in rows if row["raw_anchored_partner_pairs"] > 0
            ],
            "nonzero_nontoral_rows_after_charging": [
                row["label"] for row in rows if row["nontoral_anchored_partner_pairs"] > 0
            ],
            "all_nonzero_active_rows_cyclic_charged": all(
                all(reason.startswith("cyclic:") for reason in row["charged_reasons"])
                for row in rows
                if row["raw_anchored_partner_pairs"] > 0
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
            f"groups={row['signature_collision_groups']:<4d} "
            f"active_pairs={row['raw_anchored_partner_pairs']:<4d} "
            f"charged={row['charged_partner_pairs']:<4d} "
            f"nontoral={row['nontoral_anchored_partner_pairs']:<4d}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        print("\nrecomputed summary:")
        print(json.dumps(cert["summary"], indent=2, sort_keys=True))
        return 1

    print(f"\nPASS: {NCHECK} X14 h=4 charged-sweep checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
