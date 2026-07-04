#!/usr/bin/env python3
"""X42 h=4 centered energy accounting.

X40 reduced centered h=4 trades to pair-product two-sum collisions inside
fixed nonzero pair-sum shells.  This packet packages the exact count and a
uniform shell-size upper bound:

    centered_trades = sum_s additive-pair-collisions(U_s)
    centered_trades <= sum_s C(|U_s|,4),

where U_s is the distinct product set of unordered H-pairs with x+y=s.
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


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x42-h4-centered-energy-accounting",
    "x42_h4_centered_energy_accounting.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")

FAILS: list[str] = []
NCHECK = 0


@dataclass(frozen=True)
class Row:
    label: str
    n: int
    p: int
    kind: str


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
        "x40_h4_centered_pair_shell_reduction": "PROVED",
        "x41_h4_centered_norm_gate": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def first_prime_after_power(n: int, exponent_num: int, exponent_den: int) -> tuple[int, int]:
    floor_threshold = x13.floor_power_fraction(n, exponent_num, exponent_den)
    p = floor_threshold + 1
    p += (1 - p) % n
    while not h3.is_prime(p):
        p += n
    return p, floor_threshold


def campaign_rows() -> list[Row]:
    out = [
        Row("low_n16_p17_nonempty", 16, 17, "low_characteristic_stress"),
        Row("low_n64_p193_nonempty", 64, 193, "low_characteristic_stress"),
    ]
    for n, a, b in ((32, 2, 1), (64, 2, 1), (128, 2, 1), (128, 3, 1), (256, 2, 1)):
        p, _ = first_prime_after_power(n, a, b)
        label = f"n{n}_alpha_{x13.exponent_label(a, b)}"
        out.append(Row(label, n, p, "campaign_boundary"))
    return out


def pair_sum(domain: list[int], p: int, pair: tuple[int, int]) -> int:
    return (domain[pair[0]] + domain[pair[1]]) % p


def pair_product(domain: list[int], p: int, pair: tuple[int, int]) -> int:
    return (domain[pair[0]] * domain[pair[1]]) % p


def shell_energy_report(row: Row) -> dict[str, Any]:
    check(f"{row.label}: p is prime", h3.is_prime(row.p), f"p={row.p}")
    check(f"{row.label}: p == 1 mod n", (row.p - 1) % row.n == 0)
    domain = h1.mu_domain(row.p, row.n)
    shells: dict[int, list[tuple[tuple[int, int], int]]] = defaultdict(list)
    for pair in combinations(range(row.n), 2):
        s = pair_sum(domain, row.p, pair)
        if s == 0:
            continue
        shells[s].append((pair, pair_product(domain, row.p, pair)))

    duplicate_products: list[dict[str, Any]] = []
    centered_supports = 0
    centered_trades = 0
    binom4_bound = 0
    nonzero_shells = 0
    max_shell_size = 0
    max_pair_sum_bucket = 0
    shell_size_hist = Counter()
    trade_examples: list[dict[str, Any]] = []

    for s, entries in shells.items():
        m = len(entries)
        shell_size_hist[m] += 1
        max_shell_size = max(max_shell_size, m)
        if m < 2:
            continue
        nonzero_shells += 1
        centered_supports += math.comb(m, 2)
        if m >= 4:
            binom4_bound += math.comb(m, 4)
        product_to_pair: dict[int, tuple[int, int]] = {}
        for pair, product in entries:
            if product in product_to_pair and len(duplicate_products) < 5:
                duplicate_products.append(
                    {
                        "sum_s": s,
                        "product": product,
                        "left_pair": list(product_to_pair[product]),
                        "right_pair": list(pair),
                    }
                )
            product_to_pair[product] = pair

        buckets: dict[int, list[tuple[int, int, tuple[int, int], tuple[int, int]]]] = defaultdict(list)
        for i, (left_pair, left_product) in enumerate(entries):
            for j in range(i + 1, len(entries)):
                right_pair, right_product = entries[j]
                buckets[(left_product + right_product) % row.p].append(
                    (i, j, left_pair, right_pair)
                )
        if buckets:
            max_pair_sum_bucket = max(max_pair_sum_bucket, max(len(v) for v in buckets.values()))
        for key, items in buckets.items():
            if len(items) < 2:
                continue
            for left, right in combinations(items, 2):
                left_indices = {left[0], left[1]}
                right_indices = {right[0], right[1]}
                if left_indices & right_indices:
                    continue
                centered_trades += 1
                if len(trade_examples) < 5:
                    trade_examples.append(
                        {
                            "sum_s": s,
                            "product_sum": key,
                            "P_pairs": [list(left[2]), list(left[3])],
                            "Q_pairs": [list(right[2]), list(right[3])],
                        }
                    )

    check(f"{row.label}: products are distinct inside each nonzero shell", not duplicate_products)
    check(
        f"{row.label}: centered trade count is bounded by sum C(m_s,4)",
        centered_trades <= binom4_bound,
        f"trades={centered_trades}, bound={binom4_bound}",
    )
    if row.kind == "campaign_boundary":
        check(
            f"{row.label}: centered energy bound fits n^3",
            binom4_bound <= row.n**3,
            f"bound={binom4_bound}, n^3={row.n**3}",
        )

    return {
        "label": row.label,
        "kind": row.kind,
        "n": row.n,
        "p": row.p,
        "nonzero_pair_sum_shells": len(shells),
        "nonzero_shells_with_at_least_two_pairs": nonzero_shells,
        "shell_size_histogram": {str(k): v for k, v in sorted(shell_size_hist.items())},
        "max_shell_size": max_shell_size,
        "centered_supports": centered_supports,
        "max_pair_product_sum_bucket": max_pair_sum_bucket,
        "centered_trade_count_exact": centered_trades,
        "binom4_shell_bound": binom4_bound,
        "n_cubed": row.n**3,
        "bound_fits_n_cubed": binom4_bound <= row.n**3,
        "duplicate_products": duplicate_products,
        "trade_examples": trade_examples,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    rows = [shell_energy_report(row) for row in campaign_rows()]
    stress = [row for row in rows if row["kind"] == "low_characteristic_stress"]
    campaign = [row for row in rows if row["kind"] == "campaign_boundary"]
    check(
        "stress rows include a nonempty centered residue",
        any(row["centered_trade_count_exact"] > 0 for row in stress),
    )
    check(
        "campaign rows have zero centered trades in this audit",
        all(row["centered_trade_count_exact"] == 0 for row in campaign),
    )
    check(
        "campaign shell C(m,4) bounds fit n^3",
        all(row["bound_fits_n_cubed"] for row in campaign),
    )
    return {
        "task": "X42 h=4 centered energy accounting",
        "node": "active_core_count_bound",
        "status": "PROVED ACCOUNTING + FINITE EVIDENCE: centered residue counted by pair-product energy per shell",
        "theorem": (
            "For each nonzero pair-sum shell s, pair products are distinct.  "
            "Centered h=4 trades in that shell are exactly two-sum collisions "
            "among unordered pairs of these products with disjoint indices.  "
            "Because the characteristic is odd and products are distinct, any "
            "four shell products support at most one equal-sum partition, so "
            "the shell contributes at most C(m_s,4), where m_s is the shell size."
        ),
        "dependency_statuses": deps,
        "rows": rows,
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

    print("\ncentered energy rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: max_m={row['max_shell_size']} "
            f"support_pairs={row['centered_supports']} "
            f"trades={row['centered_trade_count_exact']} "
            f"bound={row['binom4_shell_bound']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X42 centered energy-accounting checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
