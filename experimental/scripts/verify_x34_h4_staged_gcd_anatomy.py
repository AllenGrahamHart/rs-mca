#!/usr/bin/env python3
"""X34 h=4 staged common-gcd anatomy.

X33 proves the all-at-once h=4 common-gcd certifier.  This packet records the
staged filter:

    G1   = gcd(Phi_n, E1)
    G12  = gcd(G1, E2)
    G123 = gcd(G12, E3)

on small boundary rows.  It is evidence/anatomy rather than a new closure
theorem: E2 kills almost all top-level first-sum gates, and E3 kills the small
tail.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
import json
import os
import sys
from typing import Any

import verify_h1_u1_toy_harness as h1
import verify_x30_finite_p_norm_gate as x30
import verify_x33_h4_common_gcd_gate as x33


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x34-h4-staged-gcd-anatomy",
    "x34_h4_staged_gcd_anatomy.json",
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
        "x33_h4_common_gcd_gate": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        check(f"DAG node {node} has expected status", statuses.get(node) == expected, statuses.get(node, "missing"))
    return {node: statuses.get(node, "missing") for node in needed}


def staged_degrees(n: int, p: int, p_set: tuple[int, ...], q_set: tuple[int, ...]) -> tuple[int, int, int]:
    g = x33.cyclotomic_2power_mod(n)
    g = x33.poly_gcd_mod(g, x33.elementary_diff_poly(n, p_set, q_set, 1, p), p)
    d1 = len(g) - 1
    g = x33.poly_gcd_mod(g, x33.elementary_diff_poly(n, p_set, q_set, 2, p), p)
    d12 = len(g) - 1
    g = x33.poly_gcd_mod(g, x33.elementary_diff_poly(n, p_set, q_set, 3, p), p)
    d123 = len(g) - 1
    return d1, d12, d123


def analyze_row(n: int, p: int) -> dict[str, Any]:
    domain = h1.mu_domain(p, n)
    e1_groups: dict[int, list[tuple[int, tuple[int, ...]]]] = defaultdict(list)
    for support in combinations(range(n), 4):
        sig = x33.h4_signature(domain, p, support)
        e1_groups[sig[0]].append((x33.support_mask(support), support))

    hist_g1 = Counter()
    hist_g12 = Counter()
    hist_g123 = Counter()
    killed_by_e2 = 0
    killed_by_e3 = 0
    e2_tail_examples: list[dict[str, Any]] = []

    for group in e1_groups.values():
        for p_mask, p_set in group:
            if not (p_mask & 1):
                continue
            for q_mask, q_set in group:
                if p_mask == q_mask or (p_mask & q_mask):
                    continue
                if x30.divisible_by_phi_power_two(x30.coeff_word(n, p_set, q_set)):
                    continue

                d1, d12, d123 = staged_degrees(n, p, p_set, q_set)
                hist_g1[d1] += 1
                hist_g12[d12] += 1
                hist_g123[d123] += 1
                if d1 > 0 and d12 == 0:
                    killed_by_e2 += 1
                if d12 > 0 and d123 == 0:
                    killed_by_e3 += 1
                    if len(e2_tail_examples) < 6:
                        e2_tail_examples.append(
                            {
                                "P": list(p_set),
                                "Q": list(q_set),
                                "degree_after_E1": d1,
                                "degree_after_E2": d12,
                                "degree_after_E3": d123,
                            }
                        )

    total = sum(hist_g1.values())
    check(f"n={n}, p={p}: top-level first-sum gate has positive support", total > 0)
    check(f"n={n}, p={p}: G1 is positive for every selected top-level first-sum pair", sum(v for k, v in hist_g1.items() if k > 0) == total)
    check(f"n={n}, p={p}: E2 kills most top-level first-sum gates", killed_by_e2 * 10 > 9 * total)
    check(f"n={n}, p={p}: E3 kills the entire E2 survivor tail", hist_g123 == Counter({0: total}), dict(hist_g123))

    return {
        "n": n,
        "p": p,
        "top_level_first_sum_pairs": total,
        "degree_after_E1": {str(k): v for k, v in sorted(hist_g1.items())},
        "degree_after_E1_E2": {str(k): v for k, v in sorted(hist_g12.items())},
        "degree_after_E1_E2_E3": {str(k): v for k, v in sorted(hist_g123.items())},
        "killed_by_E2": killed_by_e2,
        "killed_by_E3": killed_by_e3,
        "E2_survivor_examples_killed_by_E3": e2_tail_examples,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    rows = [analyze_row(16, 257), analyze_row(32, 4993)]
    check("all staged rows have zero final survivors", all(row["degree_after_E1_E2_E3"] == {"0": row["top_level_first_sum_pairs"]} for row in rows))
    return {
        "task": "X34 h=4 staged common-gcd anatomy",
        "node": "active_core_count_bound",
        "status": (
            "FINITE EVIDENCE: in representative boundary rows, E2 kills almost "
            "all non-antipodal first-sum norm gates and E3 kills the remaining tail"
        ),
        "dependency_statuses": deps,
        "theorem_fragment": (
            "For any h=4 pattern, degree(G12)=0 already rules out the pattern "
            "and all Galois scalings before the E3 equation is used; degree(G123)=0 "
            "is exactly the X33 exclusion.  This packet measures the staged degrees."
        ),
        "rows": rows,
        "open_residue": (
            "Prove a general E2-kill theorem for non-antipodal top-level gates, "
            "then classify or eliminate the small G12-positive tail with E3."
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
        check("certificate matches recomputed summary", cert == expected)

    print("\nstaged rows:")
    for row in cert["rows"]:
        print(
            f"n={row['n']:<3d} p={row['p']:<6d} total={row['top_level_first_sum_pairs']:<6d} "
            f"G1={row['degree_after_E1']} G12={row['degree_after_E1_E2']} "
            f"G123={row['degree_after_E1_E2_E3']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X34 staged-gcd checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
