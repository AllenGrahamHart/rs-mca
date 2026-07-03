#!/usr/bin/env python3
"""SP-CENSUS-2 verifier: in-range anchored non-toral split-pair census.

This is the direct empirical test for the X-10 estimate in its intended
field-size regime q > n^2.  It enumerates anchored split pairs

    1 in P,  P cap Q = empty,  |P| = |Q| = h,
    e_i(P) = e_i(Q), 1 <= i <= t,

and counts the non-toral residue A_h^nt after the same cyclic/dihedral
fiber-union charging used by SP-CENSUS.

Coverage is exact for all disjoint h at n=16 and n=24.  The n=32 falsifier row
is scanned through h=8 in this low-memory PR; the requested disjoint ceiling is
h=16, but h=9 already requires sorting about 28M masks per prime.  The default
run stops after the first in-range falsifier and records the skipped heavier
rows explicitly.
"""

from __future__ import annotations

from array import array
from collections import Counter
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
import verify_sp_census_split_pairs as sp


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "sp-census2-inrange",
    "sp_census2_inrange.json",
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
    print(line, flush=True)
    if not cond:
        FAILS.append(name)


@dataclass(frozen=True)
class InRangeRow:
    name: str
    p: int
    n: int
    t: int
    h_scan_max: int | None = None


ROWS = (
    InRangeRow("F641_mu16_t3", 641, 16, 3),
    InRangeRow("F1153_mu16_t3", 1153, 16, 3),
    InRangeRow("F4289_mu16_t3", 4289, 16, 3),
    InRangeRow("F601_mu24_t3", 601, 24, 3),
    InRangeRow("F1201_mu24_t3", 1201, 24, 3),
    InRangeRow("F1801_mu24_t3", 1801, 24, 3),
    InRangeRow("F1153_mu32_t3_h_le_8", 1153, 32, 3, 8),
)

SKIPPED_AFTER_FALSIFIER = (
    InRangeRow("F2081_mu32_t3_h_le_8", 2081, 32, 3, 8),
    InRangeRow("F4289_mu32_t3_h_le_8", 4289, 32, 3, 8),
)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    step = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += step
        step = 6 - step
    return True


def requested_h_max(n: int) -> int:
    return min(int(math.log2(n)) ** 2, n // 2)


def scan_h_max(row: InRangeRow) -> int:
    req = requested_h_max(row.n)
    return min(req, row.h_scan_max) if row.h_scan_max is not None else req


def comb_mask_and_code64(
    comb: tuple[int, ...],
    domain: list[int],
    t: int,
    p: int,
) -> tuple[int, int]:
    mask = 0
    e = [0] * (t + 1)
    e[0] = 1
    for i in comb:
        mask |= 1 << i
        x = domain[i]
        for r in range(t, 0, -1):
            e[r] = (e[r] + x * e[r - 1]) % p
    code = 0
    mul = 1
    for v in e[1:]:
        code += v * mul
        mul *= p
    return mask, code


def signature_arrays64(
    row: InRangeRow,
    h: int,
    domain: list[int],
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    keys = array("Q")
    masks = array("I")
    for comb in combinations(range(row.n), h):
        mask, code = comb_mask_and_code64(comb, domain, row.t, row.p)
        keys.append(code)
        masks.append(mask)
    key_arr = np.frombuffer(keys, dtype=np.uint64).copy()
    mask_arr = np.frombuffer(masks, dtype=np.uint32).copy()
    order = np.argsort(key_arr, kind="stable")
    return key_arr, mask_arr, order


def locator_derivative_coeffs(mask: int, domain: list[int], p: int) -> list[int]:
    coeffs = sp.locator_coeffs(mask, domain, p)
    return [(i * coeffs[i]) % p for i in range(1, len(coeffs))]


def anatomy(
    row: InRangeRow,
    h: int,
    q_mask: int,
    p_mask: int,
    domain: list[int],
    route: int,
    defect_degree: int,
    q_dz: int,
    p_dz: int,
) -> dict[str, Any]:
    return {
        "h": h,
        "Q_mask": q_mask,
        "P_mask": p_mask,
        "Q_exponents": sp.exps(q_mask, row.n),
        "P_exponents": sp.exps(p_mask, row.n),
        "route_code": route,
        "defect_degree": defect_degree,
        "Q_locator_coeffs": sp.locator_coeffs(q_mask, domain, row.p),
        "P_locator_coeffs": sp.locator_coeffs(p_mask, domain, row.p),
        "Q_derivative_coeffs": locator_derivative_coeffs(q_mask, domain, row.p),
        "P_derivative_coeffs": locator_derivative_coeffs(p_mask, domain, row.p),
        "Q_derivative_zero_mask": q_dz,
        "P_derivative_zero_mask": p_dz,
        "Q_derivative_zero_exponents": sp.exps(q_dz, row.n),
        "P_derivative_zero_exponents": sp.exps(p_dz, row.n),
    }


def analyze_row(row: InRangeRow) -> dict[str, Any]:
    check(f"{row.name}: p is prime", is_prime(row.p), f"p={row.p}")
    check(f"{row.name}: q=p is in range q>n^2", row.p > row.n * row.n, f"p={row.p}, n^2={row.n * row.n}")
    check(f"{row.name}: n divides p-1", (row.p - 1) % row.n == 0)

    domain = h1.mu_domain(row.p, row.n)
    sp_row = sp.SplitRow(row.name, row.p, row.n, row.t)
    partitions = sp.charged_partitions(sp_row)
    h0 = row.t + 1
    h1_scan = scan_h_max(row)
    h1_req = requested_h_max(row.n)
    full_h_coverage = h1_scan == h1_req

    min_sig_cache: dict[int, frozenset[int]] = {}
    deriv_cache: dict[int, int] = {}
    defect_cache: dict[tuple[int, int], int] = {}

    def has_minimal_subtrade(q_mask: int, p_mask: int) -> bool:
        if q_mask not in min_sig_cache:
            min_sig_cache[q_mask] = sp.minimal_subtrade_signature_set(q_mask, sp_row, domain)
        if p_mask not in min_sig_cache:
            min_sig_cache[p_mask] = sp.minimal_subtrade_signature_set(p_mask, sp_row, domain)
        return not min_sig_cache[q_mask].isdisjoint(min_sig_cache[p_mask])

    def dz(mask: int) -> int:
        if mask not in deriv_cache:
            deriv_cache[mask] = sp.derivative_zero_mask(mask, domain, row.p)
        return deriv_cache[mask]

    def deg(q_mask: int, p_mask: int) -> int:
        key = (q_mask, p_mask)
        if key not in defect_cache:
            defect_cache[key] = sp.defect_degree(q_mask, p_mask, domain, row.p)
        return defect_cache[key]

    anchored_total = 0
    anchored_charged = 0
    anchored_nontoral = 0
    anchored_by_h = Counter()
    anchored_charged_by_h = Counter()
    anchored_nontoral_by_h = Counter()
    charged_reasons = Counter()
    route_counts = Counter()
    derivative_zero_counts = Counter()
    defect_degrees = Counter()
    max_signature_group = 0
    max_subsets_sorted = 0
    nontoral_anatomy: list[dict[str, Any]] = []
    bad_defect_examples: list[dict[str, int]] = []

    for h in range(h0, h1_scan + 1):
        key_arr, mask_arr, order = signature_arrays64(row, h, domain)
        max_subsets_sorted = max(max_subsets_sorted, len(order))
        start = 0
        while start < len(order):
            code = key_arr[order[start]]
            end = start + 1
            while end < len(order) and key_arr[order[end]] == code:
                end += 1
            size = end - start
            max_signature_group = max(max_signature_group, size)
            if size < 2:
                start = end
                continue
            masks = [int(mask_arr[order[i]]) for i in range(start, end)]
            for q_mask in masks:
                if q_mask & 1:
                    continue
                for p_mask in masks:
                    if not (p_mask & 1):
                        continue
                    if q_mask == p_mask or (q_mask & p_mask):
                        continue
                    anchored_total += 1
                    anchored_by_h[h] += 1
                    reason = sp.charged_reason(q_mask, p_mask, partitions)
                    if reason is not None:
                        anchored_charged += 1
                        anchored_charged_by_h[h] += 1
                        charged_reasons[reason] += 1
                        continue

                    d = deg(q_mask, p_mask)
                    if d > h - row.t - 1:
                        bad_defect_examples.append(
                            {
                                "h": h,
                                "Q_mask": q_mask,
                                "P_mask": p_mask,
                                "degree": d,
                                "bound": h - row.t - 1,
                            }
                        )
                    if h == row.t + 1 or has_minimal_subtrade(q_mask, p_mask):
                        route = sp.ROUTE_MINIMAL_SUBTRADE
                    else:
                        route = sp.ROUTE_PRIMITIVE_MOMENT_PTE
                    q_dz = dz(q_mask)
                    p_dz = dz(p_mask)
                    anchored_nontoral += 1
                    anchored_nontoral_by_h[h] += 1
                    route_counts[route] += 1
                    defect_degrees[d] += 1
                    derivative_zero_counts[(q_dz.bit_count(), p_dz.bit_count())] += 1
                    nontoral_anatomy.append(
                        anatomy(row, h, q_mask, p_mask, domain, route, d, q_dz, p_dz)
                    )
            start = end
        del key_arr, mask_arr, order
        gc.collect()

    target_by_h = {str(h): h * row.n for h in range(h0, h1_scan + 1)}
    nontoral_by_h_json = {str(k): v for k, v in sorted(anchored_nontoral_by_h.items())}
    ratios = {
        h: (anchored_nontoral_by_h[h] / (h * row.n))
        for h in range(h0, h1_scan + 1)
    }
    max_ratio = max(ratios.values()) if ratios else 0.0
    target_hn_holds = all(
        anchored_nontoral_by_h[h] <= h * row.n for h in range(h0, h1_scan + 1)
    )
    violations_by_h = {
        str(h): {
            "A_h_nontoral": anchored_nontoral_by_h[h],
            "target_hn": h * row.n,
            "ratio": anchored_nontoral_by_h[h] / (h * row.n),
        }
        for h in range(h0, h1_scan + 1)
        if anchored_nontoral_by_h[h] > h * row.n
    }
    check(
        f"{row.name}: anchored accounting partitions total",
        anchored_total == anchored_charged + anchored_nontoral,
        f"total={anchored_total}, charged={anchored_charged}, nontoral={anchored_nontoral}",
    )
    check(
        f"{row.name}: defect-degree check holds for every non-toral pair",
        not bad_defect_examples,
        f"bad={len(bad_defect_examples)}, non_toral={anchored_nontoral}",
    )
    check(
        f"{row.name}: target comparison evaluated on scanned h",
        True,
        f"holds={target_hn_holds}, max_ratio={max_ratio:.4f}",
    )
    check(
        f"{row.name}: every non-toral pair has full anatomy",
        len(nontoral_anatomy) == anchored_nontoral,
    )

    return {
        "row": row.name,
        "p": row.p,
        "q": row.p,
        "n": row.n,
        "t": row.t,
        "h_range_requested": [h0, h1_req],
        "h_range_scanned": [h0, h1_scan],
        "full_requested_h_coverage": full_h_coverage,
        "coverage_note": (
            "full requested disjoint h range"
            if full_h_coverage
            else "capped low-memory n=32 scan; h=9 would sort C(32,9)=28048800 masks per prime"
        ),
        "max_subsets_sorted_for_one_h": max_subsets_sorted,
        "subset_signature_max_group": max_signature_group,
        "anchored_split_pairs": anchored_total,
        "anchored_charged_pairs": anchored_charged,
        "anchored_nontoral_pairs": anchored_nontoral,
        "anchored_split_pairs_by_h": {str(k): v for k, v in sorted(anchored_by_h.items())},
        "anchored_charged_by_h": {str(k): v for k, v in sorted(anchored_charged_by_h.items())},
        "A_h_nontoral_by_h": nontoral_by_h_json,
        "target_hn_by_h": target_by_h,
        "target_hn_holds_on_scanned_h": target_hn_holds,
        "target_hn_violations_by_h": violations_by_h,
        "max_A_h_nontoral_over_hn": max_ratio,
        "charged_reasons": dict(sorted(charged_reasons.items())),
        "nontoral_route_counts": {str(k): v for k, v in sorted(route_counts.items())},
        "nontoral_defect_degrees": {str(k): v for k, v in sorted(defect_degrees.items())},
        "nontoral_derivative_zero_count_pairs": {
            f"{a},{b}": v for (a, b), v in sorted(derivative_zero_counts.items())
        },
        "nontoral_pair_anatomy": nontoral_anatomy,
    }


def build_result() -> dict[str, Any]:
    rows = [analyze_row(row) for row in ROWS]
    full_rows = [row["row"] for row in rows if row["full_requested_h_coverage"]]
    capped_rows = [row["row"] for row in rows if not row["full_requested_h_coverage"]]
    violating_rows = [row["row"] for row in rows if not row["target_hn_holds_on_scanned_h"]]
    check("all n=16 and n=24 rows have full requested h coverage", len(full_rows) == 6)
    check("the scanned n=32 falsifier row is explicitly capped", capped_rows == ["F1153_mu32_t3_h_le_8"])
    check(
        "SP-CENSUS-2 reproduces an in-range violation of A_h^nt <= h*n",
        violating_rows == ["F1153_mu32_t3_h_le_8"],
        ", ".join(violating_rows),
    )
    return {
        "node": "anchored_nontoral_pte_bound",
        "task": "SP-CENSUS-2 in-range anchored non-toral split-pair census",
        "status": (
            "FALSIFIER: exact in-range census finds F1153/mu32, h<=8, exceeding "
            "the strict A_h^nt <= h*n target under the SP-CENSUS toral classifier"
        ),
        "scope": "anchored disjoint split pairs with 1 in P, e_i(P)=e_i(Q), 1<=i<=t",
        "charged_classifier": "same SP-CENSUS cyclic/dihedral toral fiber-union classifier",
        "rows": rows,
        "summary": {
            "rows_checked": [row["row"] for row in rows],
            "rows_skipped_after_falsifier": [row.name for row in SKIPPED_AFTER_FALSIFIER],
            "full_requested_h_coverage_rows": full_rows,
            "capped_rows": capped_rows,
            "violating_rows": violating_rows,
            "max_A_h_nontoral_over_hn": max(row["max_A_h_nontoral_over_hn"] for row in rows),
            "total_anchored_nontoral_pairs": sum(row["anchored_nontoral_pairs"] for row in rows),
            "rows_with_anchored_nontoral_pairs": [
                row["row"] for row in rows if row["anchored_nontoral_pairs"]
            ],
        },
        "checks": NCHECK,
    }


def main() -> int:
    write = "--write-certificate" in sys.argv
    result = build_result()

    if write:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w", encoding="utf-8") as fh:
            json.dump(result, fh, indent=2, sort_keys=True)
            fh.write("\n")
        print(f"[write] {CERT}")

    expected = None
    if os.path.exists(CERT):
        with open(CERT, encoding="utf-8") as fh:
            expected = json.load(fh)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", result == expected)

    print("\nrow summary:")
    for row in result["rows"]:
        print(
            f"{row['row']:24s} h={row['h_range_scanned']} "
            f"A_nt={row['anchored_nontoral_pairs']:<5d} "
            f"max(A_h/hn)={row['max_A_h_nontoral_over_hn']:.4f} "
            f"coverage={'full' if row['full_requested_h_coverage'] else 'capped'}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS[:40]:
            print(f"  - {name}")
        if len(FAILS) > 40:
            print(f"  ... {len(FAILS) - 40} more")
        print("\nsummary:")
        print(json.dumps(result["summary"], indent=2, sort_keys=True))
        return 1

    print(f"\nPASS: {NCHECK} SP-CENSUS-2 in-range checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
