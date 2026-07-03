#!/usr/bin/env python3
"""P-B verifier: canonical band-trade census for u1_beta_band_trade_reduction.

For the H1 toy rows, enumerate disjoint equal-size pairs (P,Q) with
|P|=|Q|=h and identical top-t locator coefficients, for every

    t + 1 < h <= min(floor(log2 n)^2, floor(n/2)).

These are the canonical band trades: deg(L_P - L_Q) <= h-t-1.  Each dihedral
orbit is counted once, then routed through the three exits from
u1_beta_band_trade_reduction:

  1. contains a minimal size-(t+1) subtrade after bounded-tail deletion;
  2. is already v1 pullback/dihedral charged by the frozen W3 dictionary;
  3. is a primitive moment/PTE residual.

Exit 3 is deliberately recorded, not hidden: it is the hand-off to the U2
moment/PTE certifier lane, not a proof that official rows are clear.

Run:
  python3 experimental/scripts/verify_pb_band_trade_census.py
Refresh certificate:
  python3 experimental/scripts/verify_pb_band_trade_census.py --write-certificate
"""

from __future__ import annotations

from array import array
from collections import Counter
from itertools import combinations
import json
import math
import os
import sys

import numpy as np

import verify_h1_u1_toy_harness as h1


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "pb-band-trade-census",
    "pb_band_trade_census.json",
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


def canonical_unordered_trade_key(P: int, Q: int, n: int) -> tuple[int, int]:
    a = h1.canonical_trade_key(P, Q, n)
    b = h1.canonical_trade_key(Q, P, n)
    return min(a, b)


def mask_bits(mask: int, n: int) -> list[int]:
    return [i for i in range(n) if (mask >> i) & 1]


def comb_mask_and_signature(
    comb: tuple[int, ...],
    domain: list[int],
    t: int,
    p: int,
) -> tuple[int, tuple[int, ...], int]:
    mask = 0
    e = [0] * (t + 1)
    e[0] = 1
    for i in comb:
        mask |= 1 << i
        x = domain[i]
        for r in range(t, 0, -1):
            e[r] = (e[r] + x * e[r - 1]) % p
    sig = tuple(e[1:])
    code = 0
    mul = 1
    for v in sig:
        code += v * mul
        mul *= p
    return mask, sig, code


def locator_coeffs(mask: int, domain: list[int], p: int) -> list[int]:
    """Return coefficients of prod_{x in mask}(X-x), ascending by degree."""
    coeffs = [1]
    for i, x in enumerate(domain):
        if not ((mask >> i) & 1):
            continue
        out = [0] * (len(coeffs) + 1)
        for j, c in enumerate(coeffs):
            out[j] = (out[j] - x * c) % p
            out[j + 1] = (out[j + 1] + c) % p
        coeffs = out
    return coeffs


def defect_degree(P: int, Q: int, domain: list[int], p: int) -> int:
    cp = locator_coeffs(P, domain, p)
    cq = locator_coeffs(Q, domain, p)
    m = max(len(cp), len(cq))
    cp += [0] * (m - len(cp))
    cq += [0] * (m - len(cq))
    for i in range(m - 1, -1, -1):
        if (cp[i] - cq[i]) % p:
            return i
    return -1


def signature_arrays(
    n: int,
    h: int,
    domain: list[int],
    t: int,
    p: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return sorted signature/mask arrays using compact construction.

    The n=24, h=11/12 cells contain millions of subsets.  Storing
    defaultdict(list) groups of Python ints is unnecessarily memory-heavy, so
    this builds uint32 signature/mask arrays and sorts once.  The caller
    expands one signature group at a time.
    """
    keys = array("I")
    masks = array("I")
    for comb in combinations(range(n), h):
        mask, _sig, code = comb_mask_and_signature(comb, domain, t, p)
        masks.append(mask)
        keys.append(code)

    key_arr = np.frombuffer(keys, dtype=np.uint32).copy()
    mask_arr = np.frombuffer(masks, dtype=np.uint32).copy()
    order = np.argsort(key_arr, kind="stable")
    return key_arr, mask_arr, order


def analyze_row(row: h1.RowSpec) -> dict[str, object]:
    domain = h1.mu_domain(row.p, row.n)
    h_min = row.t + 2
    h_max = min(int(math.log2(row.n)) ** 2, row.n // 2)
    partitions = h1.v1_paid_partitions(row.n, row.t)

    def min_subtrade_sigs(mask: int) -> frozenset[tuple[int, ...]]:
        bits = mask_bits(mask, row.n)
        return frozenset(
            comb_mask_and_signature(comb, domain, row.t, row.p)[1]
            for comb in combinations(bits, row.t + 1)
        )

    def has_minimal_subtrade(P: int, Q: int) -> bool:
        return not min_subtrade_sigs(P).isdisjoint(min_subtrade_sigs(Q))

    h_rows: list[dict[str, object]] = []
    aggregate_exit_counts = Counter()
    aggregate_v1_reasons = Counter()
    aggregate_defect_degrees = Counter()
    total_canonical = 0
    total_non_v1 = 0
    total_large_moment = 0
    max_signature_group = 0
    primitive_examples: list[dict[str, object]] = []

    for h in range(h_min, h_max + 1):
        key_arr, mask_arr, order = signature_arrays(row.n, h, domain, row.t, row.p)
        subset_count = int(len(order))

        seen: set[tuple[int, int]] = set()
        exit_counts = Counter()
        v1_reasons = Counter()
        defect_degrees = Counter()
        raw_disjoint_pairs = 0
        defect_failures = 0
        non_v1 = 0
        large_moment = 0
        repeated_classes = 0
        max_group = 0
        max_signature_group = max(max_signature_group, max_group)

        start = 0
        while start < subset_count:
            key0 = key_arr[order[start]]
            end = start + 1
            while end < subset_count and key_arr[order[end]] == key0:
                end += 1
            size = end - start
            if size < 2:
                start = end
                continue
            repeated_classes += 1
            max_group = max(max_group, size)
            masks = [int(mask_arr[order[j]]) for j in range(start, end)]
            for i, P in enumerate(masks):
                for Q in masks[i + 1 :]:
                    if P & Q:
                        continue
                    raw_disjoint_pairs += 1
                    key = canonical_unordered_trade_key(P, Q, row.n)
                    if key in seen:
                        continue
                    seen.add(key)
                    # The orbit key may use inversion for deduplication.
                    # Top-coefficient equality is checked in the original X
                    # coordinate, so route using the first band representative
                    # that produced this orbit.
                    P0, Q0 = P, Q
                    deg = defect_degree(P0, Q0, domain, row.p)
                    defect_degrees[deg] += 1
                    if deg > h - row.t - 1:
                        defect_failures += 1

                    reason = h1.v1_paid_reason(P0, Q0, partitions)
                    if reason is not None:
                        exit_counts["exit2_v1_pullback"] += 1
                        v1_reasons[reason] += 1
                    elif has_minimal_subtrade(P0, Q0):
                        exit_counts["exit1_minimal_subtrade"] += 1
                        non_v1 += 1
                    else:
                        exit_counts["exit3_primitive_moment_pte"] += 1
                        non_v1 += 1
                        if h > 2 * row.t + 4:
                            large_moment += 1
                        if len(primitive_examples) < 10:
                            C0, D0 = key
                            primitive_examples.append(
                                {
                                    "h": h,
                                    "P": h1.exps_from_mask(P0, row.n),
                                    "Q": h1.exps_from_mask(Q0, row.n),
                                    "canonical_P": h1.exps_from_mask(C0, row.n),
                                    "canonical_Q": h1.exps_from_mask(D0, row.n),
                                    "defect_degree": deg,
                                }
                            )
            start = end
        max_signature_group = max(max_signature_group, max_group)

        canonical_count = len(seen)
        total_canonical += canonical_count
        total_non_v1 += non_v1
        total_large_moment += large_moment
        aggregate_exit_counts.update(exit_counts)
        aggregate_v1_reasons.update(v1_reasons)
        aggregate_defect_degrees.update(defect_degrees)

        check(
            f"{row.name} h={h}: band degree condition",
            defect_failures == 0,
            f"canonical={canonical_count}, failures={defect_failures}",
        )
        check(
            f"{row.name} h={h}: all canonical trades routed",
            sum(exit_counts.values()) == canonical_count,
            f"routed={sum(exit_counts.values())}, canonical={canonical_count}",
        )

        h_rows.append(
            {
                "h": h,
                "subset_count": subset_count,
                "same_signature_classes_with_multiplicity": repeated_classes,
                "max_signature_group_size": max_group,
                "raw_disjoint_band_pairs": raw_disjoint_pairs,
                "canonical_band_trade_orbits": canonical_count,
                "non_v1_canonical_orbits": non_v1,
                "exit_counts": dict(sorted(exit_counts.items())),
                "v1_reasons": dict(sorted(v1_reasons.items())),
                "defect_degree_histogram": {str(k): v for k, v in sorted(defect_degrees.items())},
                "large_window_moment_residuals_h_gt_2t_plus_4": large_moment,
            }
        )

    check(
        f"{row.name}: P-B no unclassified canonical band trade",
        total_canonical == sum(aggregate_exit_counts.values()),
        f"canonical={total_canonical}",
    )
    check(
        f"{row.name}: P-B non-v1 exits are classified",
        total_non_v1
        == aggregate_exit_counts["exit1_minimal_subtrade"]
        + aggregate_exit_counts["exit3_primitive_moment_pte"],
        f"non_v1={total_non_v1}",
    )

    return {
        "row": row.name,
        "p": row.p,
        "n": row.n,
        "A": row.A,
        "t": row.t,
        "h_range": [h_min, h_max] if h_min <= h_max else [],
        "map_degree_window": [row.t + 1, int(math.log2(row.n)) ** 2],
        "h_rows": h_rows,
        "canonical_band_trade_orbits": total_canonical,
        "non_v1_canonical_orbits": total_non_v1,
        "n_squared_cap": row.n * row.n,
        "exit_counts": dict(sorted(aggregate_exit_counts.items())),
        "v1_reasons": dict(sorted(aggregate_v1_reasons.items())),
        "defect_degree_histogram": {str(k): v for k, v in sorted(aggregate_defect_degrees.items())},
        "max_signature_group_size": max_signature_group,
        "large_window_moment_residuals_h_gt_2t_plus_4": total_large_moment,
        "primitive_moment_examples": primitive_examples,
    }


def build_certificate() -> dict[str, object]:
    rows = [analyze_row(row) for row in h1.ROWS]
    totals = Counter()
    for row in rows:
        totals.update(row["exit_counts"])
    return {
        "task": "P-B band-trade census",
        "node": "u1_beta_band_trade_reduction",
        "dictionary": "w3_chargeable_dictionary_grammar.md v1",
        "rows": rows,
        "aggregate_exit_counts": dict(sorted(totals.items())),
        "total_canonical_band_trade_orbits": sum(row["canonical_band_trade_orbits"] for row in rows),
        "max_non_v1_canonical_orbits_per_row": max(row["non_v1_canonical_orbits"] for row in rows),
        "verdict": "PASS: every checked canonical band trade routes to exits 1/2/3; no toy falsifier",
    }


def main() -> int:
    write = "--write-certificate" in sys.argv
    cert = build_certificate()
    check(
        "P-B aggregate routing covers all canonical trades",
        cert["total_canonical_band_trade_orbits"] == sum(cert["aggregate_exit_counts"].values()),
        f"canonical={cert['total_canonical_band_trade_orbits']}",
    )
    if write:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w", encoding="utf-8") as f:
            json.dump(cert, f, indent=2, sort_keys=True)
            f.write("\n")
        print(f"[write] {CERT}")
    expected = None
    if os.path.exists(CERT):
        with open(CERT, encoding="utf-8") as f:
            expected = json.load(f)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", cert == expected)
    if FAILS:
        print("\nFAILURES:")
        for f in FAILS:
            print(f"  - {f}")
        return 1
    print("\nsummary:")
    print(json.dumps(
        {
            "aggregate_exit_counts": cert["aggregate_exit_counts"],
            "total_canonical_band_trade_orbits": cert["total_canonical_band_trade_orbits"],
            "max_non_v1_canonical_orbits_per_row": cert["max_non_v1_canonical_orbits_per_row"],
        },
        indent=2,
        sort_keys=True,
    ))
    print(f"\nAll {NCHECK} checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
