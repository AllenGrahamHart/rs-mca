#!/usr/bin/env python3
"""X40 h=4 centered affine residue -> pair-shell h=2 collision.

X39 isolates the only affine-line h=4 residue not already cyclic-paid:
quartics even around a nonzero center c.  This packet proves the exact
combinatorial reduction.  A reflected 4-subset is two unordered H-pairs with
common sum s=2c; two such 4-subsets have the same top-three locator
coefficients iff the sums of their pair products agree.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import combinations
import json
import math
import os
import sys
from typing import Any

import verify_h1_u1_toy_harness as h1
import verify_x12_h3_active_core_census as h3
import verify_x13_h3_q_sweep as x13
import verify_x37_h4_quartic_fiber_form as x37


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x40-h4-centered-pair-shell-reduction",
    "x40_h4_centered_pair_shell_reduction.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")

FAILS: list[str] = []
NCHECK = 0


@dataclass(frozen=True)
class SweepRow:
    n: int
    exponent_num: int
    exponent_den: int


ROWS = (
    SweepRow(32, 2, 1),
    SweepRow(32, 3, 1),
    SweepRow(64, 2, 1),
    SweepRow(64, 3, 1),
    SweepRow(128, 2, 1),
    SweepRow(128, 3, 1),
    SweepRow(256, 2, 1),
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


def load_json(path: str) -> Any:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def check_dependency_nodes() -> dict[str, str]:
    dag = load_json(DAG)
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    needed = {
        "x39_h4_affine_line_normal_form": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def row_label(row: SweepRow) -> str:
    return f"n{row.n}_alpha_{x13.exponent_label(row.exponent_num, row.exponent_den)}"


def first_prime_after_power(row: SweepRow) -> tuple[int, int]:
    floor_threshold = x13.floor_power_fraction(row.n, row.exponent_num, row.exponent_den)
    p = floor_threshold + 1
    p += (1 - p) % row.n
    while not h3.is_prime(p):
        p += row.n
    return p, floor_threshold


def direct_top_three(domain: list[int], p: int, support: tuple[int, int, int, int]) -> tuple[int, int, int]:
    e1, e2, e3, _ = x37.elementary_all(domain, p, tuple(sorted(support)))
    return e1, e2, e3


def formula_top_three(s: int, product_sum: int, p: int) -> tuple[int, int, int]:
    # (X^2 - sX + u)(X^2 - sX + v)
    return (2 * s % p, (s * s + product_sum) % p, s * product_sum % p)


def pair_product(domain: list[int], p: int, pair: tuple[int, int]) -> int:
    return (domain[pair[0]] * domain[pair[1]]) % p


def pair_sum(domain: list[int], p: int, pair: tuple[int, int]) -> int:
    return (domain[pair[0]] + domain[pair[1]]) % p


def support_from_pairpair(pairpair: tuple[tuple[int, int], tuple[int, int]]) -> frozenset[int]:
    return frozenset(pairpair[0] + pairpair[1])


def check_pair_shell_identity() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    examples = [
        (32, 1153, ((0, 1), (22, 29))),
        (64, 4289, ((0, 2), (7, 14))),
        (128, 17921, ((0, 2), (52, 84))),
    ]
    for n, p, pairpair in examples:
        domain = h1.mu_domain(p, n)
        s0 = pair_sum(domain, p, pairpair[0])
        s1 = pair_sum(domain, p, pairpair[1])
        check(f"n={n}: example pairs have common sum", s0 == s1, f"{s0}, {s1}")
        support = tuple(sorted(support_from_pairpair(pairpair)))
        product_sum = (pair_product(domain, p, pairpair[0]) + pair_product(domain, p, pairpair[1])) % p
        direct = direct_top_three(domain, p, support)
        formula = formula_top_three(s0, product_sum, p)
        check(f"n={n}: pair-shell top-three formula matches direct locator", direct == formula)
        rows.append(
            {
                "n": n,
                "p": p,
                "pairs": [list(pairpair[0]), list(pairpair[1])],
                "common_sum_s": s0,
                "product_sum": product_sum,
                "support": list(support),
                "direct_top_three": list(direct),
                "formula_top_three": list(formula),
            }
        )
    return rows


def centered_pair_shell_report(row: SweepRow) -> dict[str, Any]:
    label = row_label(row)
    p, floor_threshold = first_prime_after_power(row)
    check(f"{label}: p is prime", h3.is_prime(p), f"p={p}")
    check(f"{label}: p == 1 mod n", (p - 1) % row.n == 0)
    check(f"{label}: p exceeds floor(n^alpha)", p > floor_threshold, f"floor={floor_threshold}")

    domain = h1.mu_domain(p, row.n)
    by_sum: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for pair in combinations(range(row.n), 2):
        by_sum[pair_sum(domain, p, pair)].append(pair)

    shell_size_hist = Counter(len(pairs) for pairs in by_sum.values())
    nonzero_centered_supports = 0
    centered_trade_pairs = 0
    active_shells = 0
    max_product_sum_bucket = 0
    examples: list[dict[str, Any]] = []

    for s, pairs in by_sum.items():
        if s == 0 or len(pairs) < 2:
            continue
        buckets: dict[int, list[tuple[tuple[int, int], tuple[int, int], frozenset[int]]]] = defaultdict(list)
        for pair1, pair2 in combinations(pairs, 2):
            support = support_from_pairpair((pair1, pair2))
            if len(support) != 4:
                continue
            nonzero_centered_supports += 1
            key = (pair_product(domain, p, pair1) + pair_product(domain, p, pair2)) % p
            buckets[key].append((pair1, pair2, support))
        if buckets:
            max_product_sum_bucket = max(max_product_sum_bucket, max(len(v) for v in buckets.values()))
        shell_trades = 0
        for key, items in buckets.items():
            if len(items) < 2:
                continue
            for left, right in combinations(items, 2):
                if left[2].isdisjoint(right[2]):
                    shell_trades += 1
                    if len(examples) < 3:
                        examples.append(
                            {
                                "sum_s": s,
                                "product_sum": key,
                                "P_pairs": [list(left[0]), list(left[1])],
                                "Q_pairs": [list(right[0]), list(right[1])],
                                "P_support": sorted(left[2]),
                                "Q_support": sorted(right[2]),
                            }
                        )
        if shell_trades:
            active_shells += 1
            centered_trade_pairs += shell_trades

    check(
        f"{label}: no nonzero-centered h=4 pair-shell trades",
        centered_trade_pairs == 0,
        f"trades={centered_trade_pairs}, shells={active_shells}",
    )

    return {
        "label": label,
        "n": row.n,
        "p": p,
        "h": 4,
        "floor_n_alpha": floor_threshold,
        "pair_sum_shell_count": len(by_sum),
        "pair_sum_shell_size_histogram": {str(k): v for k, v in sorted(shell_size_hist.items())},
        "nonzero_centered_supports": nonzero_centered_supports,
        "max_product_sum_bucket_within_shell": max_product_sum_bucket,
        "centered_trade_pairs": centered_trade_pairs,
        "active_center_shells": active_shells,
        "examples": examples,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    identities = check_pair_shell_identity()
    rows = [centered_pair_shell_report(row) for row in ROWS]
    check(
        "all checked rows have zero nonzero-centered pair-shell trades",
        all(row["centered_trade_pairs"] == 0 for row in rows),
    )
    check(
        "finite evidence includes the h=4 boundary row n=128 alpha=2",
        any(row["label"] == "n128_alpha_2" for row in rows),
    )
    check(
        "finite evidence includes n=256 alpha=2 pair-shell audit",
        any(row["label"] == "n256_alpha_2" for row in rows),
    )
    return {
        "task": "X40 h=4 centered pair-shell reduction",
        "node": "active_core_count_bound",
        "status": "PROVED REDUCTION + FINITE EVIDENCE: centered affine h=4 trades reduce to pair-product h=2 collisions; none in checked rows",
        "theorem": (
            "For a nonzero center c with s=2c, any h=4 support even around c "
            "is two unordered H-pairs with common sum s.  If their products "
            "are u and v, then the support has top-three elementary sums "
            "(2s, s^2+u+v, s(u+v)).  Hence two centered supports with the "
            "same nonzero center have equal top-three sums iff their pair-product "
            "sums u+v agree.  The h4_centered_power_affine_residue is therefore "
            "exactly a same-sum collision among pair products inside a fixed "
            "nonzero pair-sum shell."
        ),
        "dependency_statuses": deps,
        "identity_examples": identities,
        "row_evidence": rows,
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

    print("\nrow evidence:")
    for row in cert["row_evidence"]:
        print(
            f"{row['label']}: centered_supports={row['nonzero_centered_supports']} "
            f"max_bucket={row['max_product_sum_bucket_within_shell']} "
            f"trades={row['centered_trade_pairs']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X40 centered pair-shell checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
