#!/usr/bin/env python3
"""X-12 h=3 active-core census.

This verifier replicates the h=3 active-core signal recorded in the terminal
node.  For h=3, two completely split fibers of the same locator pencil have
the same first two elementary symmetric sums:

    e1(P) = e1(Q),    e2(P) = e2(Q).

The scan groups every 3-subset of mu_n by (e1,e2), then counts anchored cores
P with 1 in P that have at least one disjoint partner Q in the same group.
The cyclic/dihedral strip is checked with the SP-CENSUS classifier; in the
rows where active cores occur, all recorded partners remain non-toral under
that classifier.
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


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x12-h3-active-core-census",
    "x12_h3_active_core_census.json",
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
class H3Row:
    label: str
    n: int
    scale_exponent: int


ROWS = (
    H3Row("n32_q_n2_plus", 32, 2),
    H3Row("n64_q_n2_plus", 64, 2),
    H3Row("n128_q_n2_plus", 128, 2),
    H3Row("n256_q_n2_plus", 256, 2),
    H3Row("n32_q_n3_plus", 32, 3),
    H3Row("n64_q_n3_plus", 64, 3),
    H3Row("n128_q_n3_plus", 128, 3),
    H3Row("n256_q_n3_plus", 256, 3),
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


def first_prime_gt_power_congruent_one(n: int, exponent: int) -> int:
    x = n**exponent + 1
    residue = x % n
    if residue != 1:
        x += (1 - residue) % n
    while not is_prime(x):
        x += n
    return x


def triple_code(i: int, j: int, k: int) -> int:
    return i | (j << 8) | (k << 16)


def decode_triple(code: int) -> tuple[int, int, int]:
    return code & 255, (code >> 8) & 255, (code >> 16) & 255


def mask_from_triple(code: int) -> int:
    i, j, k = decode_triple(code)
    return (1 << i) | (1 << j) | (1 << k)


def exps_from_mask(mask: int, n: int) -> list[int]:
    return [i for i in range(n) if (mask >> i) & 1]


def signature_arrays(p: int, n: int, domain: list[int]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    keys = array("Q")
    triples = array("I")
    for i, j, k in combinations(range(n), 3):
        x, y, z = domain[i], domain[j], domain[k]
        e1 = (x + y + z) % p
        e2 = (x * y + x * z + y * z) % p
        keys.append(e1 + p * e2)
        triples.append(triple_code(i, j, k))
    key_arr = np.frombuffer(keys, dtype=np.uint64).copy()
    triple_arr = np.frombuffer(triples, dtype=np.uint32).copy()
    order = np.argsort(key_arr, kind="stable")
    return key_arr, triple_arr, order


def analyze_row(row: H3Row) -> dict[str, Any]:
    p = first_prime_gt_power_congruent_one(row.n, row.scale_exponent)
    threshold = row.n**row.scale_exponent
    check(f"{row.label}: p is prime", is_prime(p), f"p={p}")
    check(f"{row.label}: p > n^{row.scale_exponent}", p > threshold, f"p={p}, threshold={threshold}")
    check(f"{row.label}: n divides p-1", (p - 1) % row.n == 0)

    domain = h1.mu_domain(p, row.n)
    key_arr, triple_arr, order = signature_arrays(p, row.n, domain)
    partitions = sp.charged_partitions(sp.SplitRow(row.label, p, row.n, 2))

    collision_groups = 0
    collision_triples = 0
    max_group_size = 1
    group_size_hist = Counter()
    raw_active_cores = 0
    nontoral_active_cores = 0
    raw_anchored_partners = 0
    nontoral_anchored_partners = 0
    charged_partners = 0
    charged_reasons = Counter()
    multiplicity_hist = Counter()
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
            masks = [mask_from_triple(int(triple_arr[order[i]])) for i in range(start, end)]
            for p_mask in masks:
                if not (p_mask & 1):
                    continue
                raw_partners_here = 0
                nontoral_partners_here = 0
                for q_mask in masks:
                    if q_mask == p_mask or (q_mask & p_mask):
                        continue
                    raw_partners_here += 1
                    reason = sp.charged_reason(q_mask, p_mask, partitions)
                    if reason is None:
                        nontoral_partners_here += 1
                        if len(examples) < 12:
                            examples.append(
                                {
                                    "signature_code": int(code),
                                    "P_exponents": exps_from_mask(p_mask, row.n),
                                    "Q_exponents": exps_from_mask(q_mask, row.n),
                                }
                            )
                    else:
                        charged_partners += 1
                        charged_reasons[reason] += 1
                if raw_partners_here:
                    raw_active_cores += 1
                    raw_anchored_partners += raw_partners_here
                if nontoral_partners_here:
                    nontoral_active_cores += 1
                    nontoral_anchored_partners += nontoral_partners_here
                    multiplicity_hist[nontoral_partners_here] += 1
        start = end

    check(
        f"{row.label}: partner accounting is nonnegative",
        raw_anchored_partners == nontoral_anchored_partners + charged_partners,
        f"raw={raw_anchored_partners}, nontoral={nontoral_anchored_partners}, charged={charged_partners}",
    )

    return {
        "label": row.label,
        "n": row.n,
        "h": 3,
        "t": 2,
        "scale": f"first prime p > n^{row.scale_exponent}, p == 1 mod n",
        "scale_exponent": row.scale_exponent,
        "p": p,
        "p_over_n_power": f"{p}/{threshold}",
        "triple_count": math.comb(row.n, 3),
        "signature_collision_groups": collision_groups,
        "signature_collision_triples": collision_triples,
        "max_signature_group_size": max_group_size,
        "signature_group_size_histogram": {str(k): v for k, v in sorted(group_size_hist.items())},
        "raw_active_cores": raw_active_cores,
        "raw_anchored_partner_pairs": raw_anchored_partners,
        "nontoral_active_cores": nontoral_active_cores,
        "nontoral_anchored_partner_pairs": nontoral_anchored_partners,
        "charged_partner_pairs": charged_partners,
        "charged_reasons": dict(sorted(charged_reasons.items())),
        "nontoral_partner_multiplicity_histogram": {
            str(k): v for k, v in sorted(multiplicity_hist.items())
        },
        "examples": examples,
    }


def build_certificate() -> dict[str, Any]:
    rows = [analyze_row(row) for row in ROWS]
    n2_rows = [row for row in rows if row["scale_exponent"] == 2]
    n3_rows = [row for row in rows if row["scale_exponent"] == 3]

    expected_n2_counts = {
        "n32_q_n2_plus": 0,
        "n64_q_n2_plus": 0,
        "n128_q_n2_plus": 18,
        "n256_q_n2_plus": 129,
    }
    check(
        "q~n^2 rows reproduce the X-12 h=3 active-core counts",
        {row["label"]: row["nontoral_active_cores"] for row in n2_rows} == expected_n2_counts,
        str({row["label"]: row["nontoral_active_cores"] for row in n2_rows}),
    )
    check(
        "q~n^3 rows have zero h=3 active cores through n=256",
        all(row["nontoral_active_cores"] == 0 for row in n3_rows),
    )
    check(
        "all q~n^2 active partners remain non-toral under cyclic/dihedral strip",
        sum(row["charged_partner_pairs"] for row in n2_rows) == 0,
    )
    check(
        "every active q~n^2 core has one disjoint partner in these rows",
        all(
            row["nontoral_partner_multiplicity_histogram"] in ({}, {"1": row["nontoral_active_cores"]})
            for row in n2_rows
        ),
    )

    return {
        "node": "active_core_count_bound",
        "task": "X12-H3 active-core census replication",
        "status": "EVIDENCE: h=3 q~n^2 boundary counts reproduced; q~n^3 vanishing verified through n=256",
        "scope": "anchored h=3 cores P subset mu_n with a disjoint same-(e1,e2) H-split partner Q",
        "rows": rows,
        "summary": {
            "q_n2_active_core_counts": {
                row["label"]: row["nontoral_active_cores"] for row in n2_rows
            },
            "q_n3_active_core_counts": {
                row["label"]: row["nontoral_active_cores"] for row in n3_rows
            },
            "max_q_n2_active_cores": max(row["nontoral_active_cores"] for row in n2_rows),
            "max_q_n3_active_cores": max(row["nontoral_active_cores"] for row in n3_rows),
            "rows_with_active_cores": [
                row["label"] for row in rows if row["nontoral_active_cores"]
            ],
        },
        "checks": NCHECK,
    }


def main() -> int:
    write = "--write-certificate" in sys.argv
    result = build_certificate()

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
        check("certificate matches recomputed census", result == expected)

    print("\nrow summary:")
    for row in result["rows"]:
        print(
            f"{row['label']:18s} n={row['n']:<3d} p={row['p']:<9d} "
            f"groups={row['signature_collision_groups']:<5d} "
            f"C3_nt={row['nontoral_active_cores']:<4d} "
            f"pairs={row['nontoral_anchored_partner_pairs']:<4d}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        print("\nsummary:")
        print(json.dumps(result["summary"], indent=2, sort_keys=True))
        return 1

    print(f"\nPASS: {NCHECK} X-12 h=3 active-core checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
