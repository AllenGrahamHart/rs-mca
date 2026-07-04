#!/usr/bin/env python3
"""X36 h=4 n=64 high-row power-gate check.

Low-memory single-row extension of X33-X35.  It checks the first n=64 row at
q ~= n^3 used elsewhere in the terminal campaign:

    F_262337 / mu_64.

Every non-antipodal first-sum h=4 candidate has zero signed power common-gcd
degree, while the only top-three trades are the paid mu4 baseline.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
import json
import math
import os
import sys
import time
from typing import Any

import verify_h1_u1_toy_harness as h1
import verify_x12_h3_active_core_census as h3
import verify_x20_h4_cyclic_fingerprint as x20
import verify_x30_finite_p_norm_gate as x30
import verify_x33_h4_common_gcd_gate as x33
import verify_x35_h4_power_sum_gate as x35


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x36-h4-n64-highrow-power-gate",
    "x36_h4_n64_highrow_power_gate.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")

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


def load_json(path: str) -> Any:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def check_dependency_nodes() -> dict[str, str]:
    dag = load_json(DAG)
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    needed = {
        "x35_h4_power_sum_gate": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        check(f"DAG node {node} has expected status", statuses.get(node) == expected, statuses.get(node, "missing"))
    return {node: statuses.get(node, "missing") for node in needed}


def analyze_row(n: int = 64, p: int = 262337) -> dict[str, Any]:
    start_time = time.time()
    check("n=64 high-row prime is prime", h3.is_prime(p), f"p={p}")
    check("n=64 high-row prime is 1 mod n", (p - 1) % n == 0)
    check("n=64 high-row prime is above n^3", p > n**3, f"n^3={n**3}")

    domain = h1.mu_domain(p, n)
    e1_groups: dict[int, list[tuple[int, tuple[int, ...], tuple[int, int, int]]]] = defaultdict(list)
    for support in combinations(range(n), 4):
        sig = x33.h4_signature(domain, p, support)
        e1_groups[sig[0]].append((x33.support_mask(support), support, sig))

    counts = Counter()
    power_degree_histogram = Counter()
    examples: dict[str, list[dict[str, Any]]] = {"top_level_first_sum": [], "paid_top_three": []}

    for group in e1_groups.values():
        if len(group) < 2:
            continue
        for p_mask, p_set, p_sig in group:
            if not (p_mask & 1):
                continue
            for q_mask, q_set, q_sig in group:
                if p_mask == q_mask or (p_mask & q_mask):
                    continue
                counts["anchored_e1_pairs"] += 1
                descended = x30.divisible_by_phi_power_two(x30.coeff_word(n, p_set, q_set))
                if descended:
                    counts["antipodal_e1_pairs"] += 1
                else:
                    counts["top_level_e1_pairs"] += 1
                    degree = x35.power_common_gcd_degree(n, p, p_set, q_set)
                    power_degree_histogram[degree] += 1
                    if len(examples["top_level_first_sum"]) < 4:
                        examples["top_level_first_sum"].append(
                            {
                                "P": list(p_set),
                                "Q": list(q_set),
                                "power_common_gcd_degree": degree,
                            }
                        )

                if p_sig == q_sig:
                    counts["anchored_top_three_pairs"] += 1
                    kind = x20.classify_pair(p_mask, q_mask, n, domain, p)
                    counts[f"top_three_{kind}"] += 1
                    if len(examples["paid_top_three"]) < 4:
                        examples["paid_top_three"].append(
                            {
                                "P": list(p_set),
                                "Q": list(q_set),
                                "classification": kind,
                                "descended": descended,
                            }
                        )

    expected_mu4 = n // 4 - 1
    check("n=64 high row has top-level first-sum candidates", counts["top_level_e1_pairs"] > 0)
    check(
        "n=64 high row has zero top-level power-gcd survivors",
        power_degree_histogram == Counter({0: counts["top_level_e1_pairs"]}),
        dict(power_degree_histogram),
    )
    check(
        "n=64 high row top-three pairs are exactly mu4 baseline",
        counts["anchored_top_three_pairs"] == expected_mu4
        and counts["top_three_mu4_full_fiber"] == expected_mu4,
        dict(counts),
    )
    return {
        "n": n,
        "p": p,
        "subset_count": math.comb(n, 4),
        "e1_group_count": len(e1_groups),
        "max_e1_group_size": max(len(group) for group in e1_groups.values()),
        "counts": dict(sorted(counts.items())),
        "top_level_power_common_gcd_degree_histogram": {
            str(k): v for k, v in sorted(power_degree_histogram.items())
        },
        "expected_mu4_baseline": expected_mu4,
        "examples": examples,
        "elapsed_seconds": time.time() - start_time,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    row = analyze_row()
    return {
        "task": "X36 h=4 n64 high-row power gate",
        "node": "active_core_count_bound",
        "status": (
            "EXACT FINITE EVIDENCE: at F_262337/mu_64, signed h=4 top-level "
            "first-sum candidates have zero 3-moment common-gcd survivors"
        ),
        "dependency_statuses": deps,
        "row": row,
        "interpretation": (
            "This extends the X33/X35 signed 4+4 moment-gate evidence from "
            "n=16,32 to the n=64 q~n^3 row without replaying the full "
            "n=64 all-prime support sweep."
        ),
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
        expected = load_json(CERT)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        comparable = dict(cert)
        comparable["row"] = dict(cert["row"])
        comparable["row"]["elapsed_seconds"] = expected["row"].get("elapsed_seconds")
        check("certificate matches recomputed summary", comparable == expected)

    row = cert["row"]
    print(
        "\nsummary:\n"
        f"n={row['n']} p={row['p']} top-level-e1={row['counts']['top_level_e1_pairs']} "
        f"top-three={row['counts']['anchored_top_three_pairs']} "
        f"gcd={row['top_level_power_common_gcd_degree_histogram']}"
    )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X36 h=4 n64 high-row checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
