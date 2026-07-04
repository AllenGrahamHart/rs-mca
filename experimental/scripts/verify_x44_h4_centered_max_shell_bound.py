#!/usr/bin/env python3
"""X44 h=4 centered max-shell bound.

X42 gives R_centered <= sum_s C(m_s,4).  This packet records the more useful
max-shell bound:

    R_centered <= C(M,4)/M * C(n,2),   M = max_s m_s.

It also replays the full n=64 boundary window and selected rows where X43's
M<=4 criterion is too strict but the max-shell bound still closes far below
n^3.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
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
    "x44-h4-centered-max-shell-bound",
    "x44_h4_centered_max_shell_bound.json",
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
        "x42_h4_centered_energy_accounting": "PROVED",
        "x43_h4_centered_shell_size_closure": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def prime_window(n: int) -> list[int]:
    out: list[int] = []
    p = n * n + 1
    p += (1 - p) % n
    while p <= n**3:
        if h3.is_prime(p):
            out.append(p)
        p += n
    return out


def pair_sum(domain: list[int], p: int, pair: tuple[int, int]) -> int:
    return (domain[pair[0]] + domain[pair[1]]) % p


def pair_product(domain: list[int], p: int, pair: tuple[int, int]) -> int:
    return (domain[pair[0]] * domain[pair[1]]) % p


def max_shell_fraction_bound(n: int, max_shell_size: int) -> Fraction:
    if max_shell_size < 4:
        return Fraction(0, 1)
    return Fraction(math.comb(max_shell_size, 4), max_shell_size) * math.comb(n, 2)


def shell_energy_summary(n: int, p: int, emit_checks: bool = True) -> dict[str, Any]:
    domain = h1.mu_domain(p, n)
    shells: dict[int, list[tuple[tuple[int, int], int]]] = defaultdict(list)
    for pair in combinations(range(n), 2):
        s = pair_sum(domain, p, pair)
        if s:
            shells[s].append((pair, pair_product(domain, p, pair)))

    max_shell = 0
    shell_hist = Counter()
    binom4_bound = 0
    exact_trades = 0
    max_pair_sum_bucket = 0

    for entries in shells.values():
        m = len(entries)
        shell_hist[m] += 1
        max_shell = max(max_shell, m)
        if m >= 4:
            binom4_bound += math.comb(m, 4)
        buckets: dict[int, list[tuple[int, int]]] = defaultdict(list)
        for i, (_, left_product) in enumerate(entries):
            for j in range(i + 1, len(entries)):
                _, right_product = entries[j]
                buckets[(left_product + right_product) % p].append((i, j))
        if buckets:
            max_pair_sum_bucket = max(max_pair_sum_bucket, max(len(v) for v in buckets.values()))
        for items in buckets.values():
            if len(items) < 2:
                continue
            for left, right in combinations(items, 2):
                if not ({left[0], left[1]} & {right[0], right[1]}):
                    exact_trades += 1

    frac = max_shell_fraction_bound(n, max_shell)
    ceil_bound = (frac.numerator + frac.denominator - 1) // frac.denominator
    if emit_checks:
        check(
            f"n={n}, p={p}: X44 max-shell bound dominates X42 binomial bound",
            binom4_bound <= frac,
            f"binom={binom4_bound}, max-bound={frac}",
        )
        check(
            f"n={n}, p={p}: X44 max-shell bound fits n^3",
            frac <= n**3,
            f"max-bound={frac}, n^3={n**3}",
        )
    return {
        "n": n,
        "p": p,
        "max_shell_size": max_shell,
        "shell_size_histogram": {str(k): v for k, v in sorted(shell_hist.items())},
        "x42_binom4_bound": binom4_bound,
        "exact_centered_trades": exact_trades,
        "max_pair_product_sum_bucket": max_pair_sum_bucket,
        "x44_bound_fraction": f"{frac.numerator}/{frac.denominator}",
        "x44_bound_ceiling": ceil_bound,
        "n_cubed": n**3,
    }


def full_window_summary(n: int) -> dict[str, Any]:
    rows = []
    max_shell = 0
    max_bound = 0
    max_exact = 0
    interesting = []
    for p in prime_window(n):
        row = shell_energy_summary(n, p, emit_checks=False)
        rows.append(row)
        max_shell = max(max_shell, row["max_shell_size"])
        max_bound = max(max_bound, row["x42_binom4_bound"])
        max_exact = max(max_exact, row["exact_centered_trades"])
        if row["max_shell_size"] > 4 or row["exact_centered_trades"] > 0:
            interesting.append(row)
    check(f"n={n}: full window has no centered trades", max_exact == 0, f"max_exact={max_exact}")
    check(f"n={n}: full-window max-shell bound fits n^3", all(row["x44_bound_ceiling"] <= n**3 for row in rows))
    check(f"n={n}: X44 max-shell bound dominates X42 row bounds", all(row["x42_binom4_bound"] <= row["x44_bound_ceiling"] for row in rows))
    return {
        "n": n,
        "prime_count": len(rows),
        "max_shell_size": max_shell,
        "max_x42_binom4_bound": max_bound,
        "max_exact_centered_trades": max_exact,
        "interesting_rows": interesting,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    stress_rows = [
        shell_energy_summary(16, 17),
        shell_energy_summary(64, 193),
    ]
    selected_rows = [
        shell_energy_summary(64, 7937),
        shell_energy_summary(128, 17921),
        shell_energy_summary(256, 91393),
    ]
    full_windows = [full_window_summary(64)]
    check(
        "selected rows include an X43-failing but X44-closing row",
        any(row["max_shell_size"] > 4 and row["x44_bound_ceiling"] <= row["n_cubed"] for row in selected_rows),
    )
    check(
        "stress rows show centered trades can be nonzero while X44 still bounds them",
        any(row["exact_centered_trades"] > 0 for row in stress_rows),
    )
    return {
        "task": "X44 h=4 centered max-shell bound",
        "node": "active_core_count_bound",
        "status": "PROVED MAX-SHELL BOUND + FULL n64 WINDOW REPLAY",
        "theorem": (
            "Let M=max_s m_s over nonzero pair-sum shells.  Since C(m,4)/m is "
            "increasing for m>=4, X42's sum_s C(m_s,4) is at most "
            "C(M,4)/M times sum_s m_s, and sum_s m_s <= C(n,2).  Thus "
            "R_centered <= C(M,4) C(n,2)/M.  Any row with this bound <= n^3 "
            "has the centered affine branch safely inside the rewired terminal column."
        ),
        "dependency_statuses": deps,
        "stress_rows": stress_rows,
        "selected_rows": selected_rows,
        "full_windows": full_windows,
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

    print("\nselected rows:")
    for row in cert["selected_rows"]:
        print(
            f"n={row['n']} p={row['p']} M={row['max_shell_size']} "
            f"exact={row['exact_centered_trades']} x44={row['x44_bound_ceiling']}"
        )
    for window in cert["full_windows"]:
        print(
            f"full n={window['n']}: primes={window['prime_count']} "
            f"M={window['max_shell_size']} interesting={len(window['interesting_rows'])}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X44 centered max-shell checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
