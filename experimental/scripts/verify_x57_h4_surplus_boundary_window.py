#!/usr/bin/env python3
"""X57 h=4 surplus boundary-window census.

X51 checked the max-shell threshold on full boundary windows.  X55/X56 sharpen
the target to the aggregate h=2 surplus:

    A_anchor_surplus < 4*C(T(n)+1,2).

This verifier recomputes the same complete prime windows as X51 and checks
that stronger surplus barrier row-by-row.
"""

from __future__ import annotations

from collections import Counter
import json
import math
import os
import sys
from typing import Any

import verify_h1_u1_toy_harness as h1
import verify_x50_h4_centered_threshold as x50
import verify_x51_h4_quotient_shell_window as x51


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x57-h4-surplus-boundary-window",
    "x57_h4_surplus_boundary_window.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")
X51_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x51-h4-quotient-shell-window",
    "x51_h4_quotient_shell_window.json",
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


def load_json(path: str) -> Any:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def check_dependency_nodes() -> dict[str, str]:
    dag = load_json(DAG)
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    needed = {
        "x51_h4_quotient_shell_window": "TEST",
        "x55_h4_surplus_threshold_bridge": "PROVED",
        "x56_h2_anchored_surplus_currency": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def shell_surplus_stats(n: int, p: int) -> dict[str, Any]:
    domain = h1.mu_domain(p, n)
    ratio_counts = Counter(
        pow((1 + r) % p, n, p)
        for r in domain
        if r != 1 and (1 + r) % p != 0
    )
    shell_sizes = [count // 2 for count in ratio_counts.values()]
    odd_buckets = sum(1 for count in ratio_counts.values() if count % 2)
    quotient_quadratic = sum(math.comb(m, 2) for m in shell_sizes if m >= 2)
    anchored_surplus = 4 * quotient_quadratic
    unanchored_surplus = n * quotient_quadratic
    return {
        "p": p,
        "ratio_mass": sum(ratio_counts.values()),
        "odd_ratio_buckets": odd_buckets,
        "hit_cosets": len(ratio_counts),
        "max_shell_size": max(shell_sizes, default=0),
        "quotient_quadratic_surplus": quotient_quadratic,
        "anchored_surplus": anchored_surplus,
        "unanchored_surplus": unanchored_surplus,
    }


def window_report(x51_window: dict[str, Any]) -> dict[str, Any]:
    n = int(x51_window["n"])
    threshold = x50.exact_threshold(n)
    anchored_barrier = 4 * math.comb(threshold + 1, 2)
    unanchored_barrier = n * math.comb(threshold + 1, 2)
    prime_count = 0
    mass_failures: list[dict[str, Any]] = []
    odd_bucket_failures: list[dict[str, Any]] = []
    surplus_violations: list[dict[str, Any]] = []
    max_anchor = -1
    max_unanchored = -1
    max_anchor_rows: list[int] = []
    max_shell = 0
    surplus_hist: Counter[int] = Counter()

    for p in x51.prime_window(n):
        prime_count += 1
        row = shell_surplus_stats(n, p)
        if row["ratio_mass"] != n - 2:
            mass_failures.append(row)
        if row["odd_ratio_buckets"] != 0:
            odd_bucket_failures.append(row)
        if row["anchored_surplus"] >= anchored_barrier:
            surplus_violations.append(row)

        anchored = row["anchored_surplus"]
        surplus_hist[anchored] += 1
        max_shell = max(max_shell, int(row["max_shell_size"]))
        if anchored > max_anchor:
            max_anchor = anchored
            max_unanchored = int(row["unanchored_surplus"])
            max_anchor_rows = [p]
        elif anchored == max_anchor:
            max_anchor_rows.append(p)
            max_unanchored = max(max_unanchored, int(row["unanchored_surplus"]))

    check(f"n={n}: prime window count matches X51", prime_count == int(x51_window["prime_count"]))
    check(f"n={n}: max shell matches X51", max_shell == int(x51_window["max_shell_size"]))
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
        f"n={n}: every row satisfies X56 anchored surplus barrier",
        not surplus_violations,
        f"violations={len(surplus_violations)}",
    )
    check(
        f"n={n}: max anchored surplus has positive margin",
        0 <= max_anchor < anchored_barrier,
        f"max={max_anchor}, barrier={anchored_barrier}",
    )

    return {
        "n": n,
        "prime_count": prime_count,
        "p_range": x51_window["p_range"],
        "exact_threshold": threshold,
        "anchored_x56_barrier": anchored_barrier,
        "unanchored_x55_barrier": unanchored_barrier,
        "max_anchored_surplus": max_anchor,
        "max_unanchored_surplus": max_unanchored,
        "max_anchored_surplus_rows": max_anchor_rows,
        "max_anchored_surplus_row_count": len(max_anchor_rows),
        "anchored_barrier_margin": anchored_barrier - max_anchor,
        "max_shell_size": max_shell,
        "surplus_value_histogram": {str(k): v for k, v in sorted(surplus_hist.items())},
        "mass_failures": mass_failures,
        "odd_bucket_failures": odd_bucket_failures,
        "surplus_violations": surplus_violations,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x51_cert = load_json(X51_CERT)
    check("X51 certificate has windows", bool(x51_cert.get("windows")))
    windows = [window_report(row) for row in x51_cert["windows"]]
    check("all surplus windows have no violations", all(not row["surplus_violations"] for row in windows))
    check("census reaches n=512", windows[-1]["n"] == 512)
    check("observed anchored surplus remains below 320", max(row["max_anchored_surplus"] for row in windows) < 320)
    return {
        "task": "X57 h=4 surplus boundary-window census",
        "node": "active_core_count_bound",
        "status": "EXACT TEST: X56 SURPLUS BARRIER ON FULL BOUNDARY WINDOWS THROUGH n=512",
        "method": (
            "For every prime p == 1 mod n with n^2 < p <= n^3, reuse the X51 "
            "coset invariant (1+r)^n.  If bucket sizes are 2*m_C, compute "
            "A_anchor_surplus = 4*sum_C C(m_C,2) and check the X56 barrier "
            "A_anchor_surplus < 4*C(T(n)+1,2)."
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

    print("\nsurplus boundary windows:")
    for row in cert["windows"]:
        print(
            f"n={row['n']}: primes={row['prime_count']} "
            f"Amax={row['max_anchored_surplus']} "
            f"barrier={row['anchored_x56_barrier']} "
            f"margin={row['anchored_barrier_margin']} "
            f"rows={row['max_anchored_surplus_rows'][:8]}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X57 h4 surplus-window checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
