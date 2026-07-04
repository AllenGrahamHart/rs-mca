#!/usr/bin/env python3
"""X51 h=4 quotient-shell boundary-window census.

X48 identifies centered shell sizes with quotient-coset intersections:

    m_C = 1/2 #{r in H\\{1}: 1+r in C}.

This finite census checks the X50 threshold on complete prime windows
n^2 < p <= n^3 for moderate powers of two, using the coset representative
(1+r)^n.  It avoids h=4 support enumeration and large discrete-log tables.
"""

from __future__ import annotations

from collections import Counter
import json
import os
import sys
from typing import Any, Iterable

import verify_h1_u1_toy_harness as h1
import verify_x12_h3_active_core_census as h3
import verify_x50_h4_centered_threshold as x50


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x51-h4-quotient-shell-window",
    "x51_h4_quotient_shell_window.json",
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
        "x48_h4_centered_coset_shell_param": "PROVED",
        "x50_h4_centered_threshold": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def prime_window(n: int) -> Iterable[int]:
    p = n * n + 1
    p += (1 - p) % n
    while p <= n**3:
        if h3.is_prime(p):
            yield p
        p += n


def shell_stats(n: int, p: int) -> dict[str, Any]:
    domain = h1.mu_domain(p, n)
    ratio_counts = Counter(
        pow((1 + r) % p, n, p)
        for r in domain
        if r != 1 and (1 + r) % p != 0
    )
    odd_buckets = sum(1 for count in ratio_counts.values() if count % 2)
    max_ratio_count = max(ratio_counts.values(), default=0)
    return {
        "p": p,
        "hit_cosets": len(ratio_counts),
        "ratio_mass": sum(ratio_counts.values()),
        "odd_ratio_buckets": odd_buckets,
        "max_ratio_count": max_ratio_count,
        "max_shell_size": max_ratio_count // 2,
    }


def window_report(n: int) -> dict[str, Any]:
    threshold = x50.exact_threshold(n)
    cube_safe = x50.integer_cube_root_floor(48 * n)
    max_shell = 0
    max_rows: list[int] = []
    hist: Counter[int] = Counter()
    prime_count = 0
    odd_bucket_total = 0
    mass_failures: list[dict[str, Any]] = []
    odd_bucket_failures: list[dict[str, Any]] = []
    min_hit_cosets: int | None = None
    max_hit_cosets = 0
    hit_coset_sum = 0
    threshold_violations: list[dict[str, Any]] = []

    for p in prime_window(n):
        prime_count += 1
        row = shell_stats(n, p)
        if row["ratio_mass"] != n - 2:
            mass_failures.append(row)
        if row["odd_ratio_buckets"] != 0:
            odd_bucket_failures.append(row)
        if row["max_shell_size"] > threshold:
            threshold_violations.append(row)

        m = row["max_shell_size"]
        hist[m] += 1
        odd_bucket_total += row["odd_ratio_buckets"]
        hit = row["hit_cosets"]
        min_hit_cosets = hit if min_hit_cosets is None else min(min_hit_cosets, hit)
        max_hit_cosets = max(max_hit_cosets, hit)
        hit_coset_sum += hit
        if m > max_shell:
            max_shell = m
            max_rows = [p]
        elif m == max_shell:
            max_rows.append(p)

    check(f"n={n}: prime window is nonempty", prime_count > 0)
    check(
        f"n={n}: every row has quotient ratio mass n-2",
        not mass_failures,
        f"failures={len(mass_failures)}",
    )
    check(
        f"n={n}: every row has even quotient ratio buckets",
        not odd_bucket_failures,
        f"failures={len(odd_bucket_failures)}",
    )
    check(
        f"n={n}: every row satisfies X50 threshold",
        not threshold_violations,
        f"violations={len(threshold_violations)}",
    )
    check(
        f"n={n}: max shell is below cube-root sufficient threshold",
        max_shell <= cube_safe,
        f"M={max_shell}, cube_safe={cube_safe}",
    )
    return {
        "n": n,
        "prime_count": prime_count,
        "p_range": [n * n, n**3],
        "exact_threshold": threshold,
        "cube_root_sufficient_threshold_floor_48n": cube_safe,
        "max_shell_size": max_shell,
        "max_shell_rows": max_rows,
        "max_shell_row_count": len(max_rows),
        "shell_size_histogram": {str(k): v for k, v in sorted(hist.items())},
        "odd_ratio_bucket_total": odd_bucket_total,
        "mass_failures": mass_failures,
        "odd_bucket_failures": odd_bucket_failures,
        "min_hit_cosets": min_hit_cosets or 0,
        "max_hit_cosets": max_hit_cosets,
        "average_hit_cosets_numerator": hit_coset_sum,
        "average_hit_cosets_denominator": prime_count,
        "threshold_violations": threshold_violations,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    windows = [window_report(n) for n in (32, 64, 128, 256, 512)]
    check("all censused windows have no threshold violations", all(not row["threshold_violations"] for row in windows))
    check("census reaches n=512", windows[-1]["n"] == 512)
    check("observed max shell never exceeds 6", max(row["max_shell_size"] for row in windows) <= 6)
    return {
        "task": "X51 h=4 quotient-shell boundary-window census",
        "node": "active_core_count_bound",
        "status": "EXACT TEST: FULL BOUNDARY WINDOWS THROUGH n=512",
        "method": (
            "For each prime p == 1 mod n with n^2 < p <= n^3, compute H=mu_n "
            "and count quotient cosets by the invariant (1+r)^n for r in H, "
            "excluding r=1 and r=-1.  The shell size is half the largest quotient "
            "ratio count.  This is exactly X48's shifted-subgroup shell statistic."
        ),
        "dependency_statuses": deps,
        "windows": windows,
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

    print("\nquotient-shell windows:")
    for row in cert["windows"]:
        avg = row["average_hit_cosets_numerator"] / row["average_hit_cosets_denominator"]
        print(
            f"n={row['n']}: primes={row['prime_count']} "
            f"Mmax={row['max_shell_size']} T={row['exact_threshold']} "
            f"cube_safe={row['cube_root_sufficient_threshold_floor_48n']} "
            f"max_rows={row['max_shell_rows'][:8]} "
            f"hit_cosets=[{row['min_hit_cosets']},{row['max_hit_cosets']}] "
            f"avg_hit={avg:.2f}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X51 h4 quotient-shell window checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
