#!/usr/bin/env python3
"""X35 h=4 power-sum gate.

For h=4 and char p > 3, equality of e1,e2,e3 is equivalent to equality of
the first three power sums.  Thus X33's common-gcd gate can be checked with
the signed 8-sparse word f:

    f(zeta) = f(zeta^2) = f(zeta^3) = 0.

This puts the h=4 top-level residue in the same sparse moment language as U2.
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
    "x35-h4-power-sum-gate",
    "x35_h4_power_sum_gate.json",
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
        "x34_h4_staged_gcd_anatomy": "TEST",
        "x4b_moment_trade_exclusion": "TARGET",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        check(f"DAG node {node} has expected status", statuses.get(node) == expected, statuses.get(node, "missing"))
    return {node: statuses.get(node, "missing") for node in needed}


def power_sum_diff_poly(n: int, p_set: tuple[int, ...], q_set: tuple[int, ...], r: int, p: int) -> list[int]:
    coeffs = [0] * n
    for support, sign in ((p_set, 1), (q_set, -1)):
        for exponent in support:
            coeffs[(r * exponent) % n] = (coeffs[(r * exponent) % n] + sign) % p
    return x33.trim(coeffs)


def power_common_gcd_degree(n: int, p: int, p_set: tuple[int, ...], q_set: tuple[int, ...]) -> int:
    common = x33.cyclotomic_2power_mod(n)
    for r in (1, 2, 3):
        common = x33.poly_gcd_mod(common, power_sum_diff_poly(n, p_set, q_set, r, p), p)
    return len(common) - 1


def newton_reconstruct_e_from_power(p1: int, p2: int, p3: int, p: int) -> tuple[int, int, int]:
    inv2 = pow(2, -1, p)
    inv3 = pow(3, -1, p)
    e1 = p1 % p
    e2 = ((e1 * p1 - p2) * inv2) % p
    e3 = ((p3 - e1 * p2 + e2 * p1) * inv3) % p
    return e1, e2, e3


def power_signature(domain: list[int], p: int, support: tuple[int, ...]) -> tuple[int, int, int]:
    out = []
    for r in (1, 2, 3):
        out.append(sum(domain[(r * exponent) % (len(domain))] for exponent in support) % p)
    return tuple(out)  # type: ignore[return-value]


def check_newton_examples() -> list[dict[str, Any]]:
    rows = []
    examples = [
        (32, 4993, (0, 8, 16, 24)),
        (32, 4993, (0, 1, 2, 17)),
        (16, 257, (0, 2, 4, 6)),
    ]
    for n, p, support in examples:
        check(f"n={n}, p={p}: char supports Newton denominators", p % 2 and p % 3)
        domain = h1.mu_domain(p, n)
        e_sig = x33.h4_signature(domain, p, support)
        p_sig = power_signature(domain, p, support)
        reconstructed = newton_reconstruct_e_from_power(*p_sig, p)
        check(f"n={n}, support={support}: Newton reconstructs e1,e2,e3", reconstructed == e_sig)
        rows.append(
            {
                "n": n,
                "p": p,
                "support": list(support),
                "elementary_signature": list(e_sig),
                "power_signature": list(p_sig),
                "reconstructed_elementary_signature": list(reconstructed),
            }
        )
    return rows


def compare_gates_on_row(n: int, p: int) -> dict[str, Any]:
    domain = h1.mu_domain(p, n)
    e1_groups: dict[int, list[tuple[int, tuple[int, ...]]]] = defaultdict(list)
    for support in combinations(range(n), 4):
        sig = x33.h4_signature(domain, p, support)
        e1_groups[sig[0]].append((x33.support_mask(support), support))

    degree_pairs = Counter()
    mismatches: list[dict[str, Any]] = []
    checked = 0
    for group in e1_groups.values():
        for p_mask, p_set in group:
            if not (p_mask & 1):
                continue
            for q_mask, q_set in group:
                if p_mask == q_mask or (p_mask & q_mask):
                    continue
                if x30.divisible_by_phi_power_two(x30.coeff_word(n, p_set, q_set)):
                    continue
                e_degree = x33.common_h4_gcd_degree(n, p, p_set, q_set)
                p_degree = power_common_gcd_degree(n, p, p_set, q_set)
                degree_pairs[(e_degree, p_degree)] += 1
                checked += 1
                if e_degree != p_degree and len(mismatches) < 5:
                    mismatches.append(
                        {
                            "P": list(p_set),
                            "Q": list(q_set),
                            "elementary_degree": e_degree,
                            "power_degree": p_degree,
                        }
                    )
    check(f"n={n}, p={p}: compared at least one top-level pattern", checked > 0)
    check(f"n={n}, p={p}: elementary and power-sum gates agree on all checked patterns", not mismatches)
    return {
        "n": n,
        "p": p,
        "checked_top_level_patterns": checked,
        "degree_pair_histogram": {f"{a},{b}": v for (a, b), v in sorted(degree_pairs.items())},
        "mismatches": mismatches,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    newton_rows = check_newton_examples()
    gate_rows = [compare_gates_on_row(16, 257), compare_gates_on_row(32, 4993)]
    check("all gate comparisons have no mismatches", all(not row["mismatches"] for row in gate_rows))
    return {
        "task": "X35 h=4 power-sum gate",
        "node": "active_core_count_bound / x4b_moment_trade_exclusion",
        "status": (
            "PROVED REDUCTION: in characteristic > 3, h=4 top-three trades "
            "are exactly signed 8-sparse words with power sums 1,2,3 vanishing"
        ),
        "theorem": (
            "Newton identities give e1=p1, 2e2=e1*p1-p2, and "
            "3e3=p3-e1*p2+e2*p1.  Since p>3 at the terminal rows, equality "
            "of e1,e2,e3 for two 4-sets is equivalent to equality of p1,p2,p3. "
            "Therefore X33's gcd(Phi_n,E1,E2,E3) gate is equivalent to "
            "gcd(Phi_n,S1,S2,S3), where Sr is the signed power-sum word "
            "sum_{a in P} X^{ra}-sum_{b in Q} X^{rb}."
        ),
        "dependency_statuses": deps,
        "newton_examples": newton_rows,
        "gate_comparison_rows": gate_rows,
        "consequence": (
            "The h=4 top-level residue is a signed 8-sparse, 3-moment-null "
            "block.  It can be handled by the same sparse moment certifier "
            "architecture as x4b_moment_trade_exclusion, with signs and "
            "disjoint 4+4 support."
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

    print("\ngate comparison rows:")
    for row in cert["gate_comparison_rows"]:
        print(
            f"n={row['n']:<3d} p={row['p']:<6d} checked={row['checked_top_level_patterns']:<6d} "
            f"degrees={row['degree_pair_histogram']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X35 h=4 power-sum checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
