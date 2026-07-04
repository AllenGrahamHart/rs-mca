#!/usr/bin/env python3
"""X50 h=4 centered cube-root threshold.

X49 proves

    R_centered <= (C(M,4)/M) * n(n-2)/2,

where M is the maximum quotient-coset shell size.  This verifier records the
exact integer threshold T(n) for which this bound is <= n^3.
"""

from __future__ import annotations

from fractions import Fraction
import json
import math
import os
import sys
from typing import Any


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x50-h4-centered-threshold",
    "x50_h4_centered_threshold.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")
X49_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x49-h4-centered-quotient-energy",
    "x49_h4_centered_quotient_energy.json",
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
        "x49_h4_centered_quotient_energy": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def centered_bound(n: int, m: int) -> Fraction:
    if m < 4:
        return Fraction(0, 1)
    return Fraction(math.comb(m, 4), m) * Fraction(n * (n - 2), 2)


def fits_threshold(n: int, m: int) -> bool:
    if m < 4:
        return True
    return (m - 1) * (m - 2) * (m - 3) * (n - 2) <= 48 * n * n


def exact_threshold(n: int) -> int:
    lo = 0
    hi = 4
    while fits_threshold(n, hi):
        lo = hi
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if fits_threshold(n, mid):
            lo = mid
        else:
            hi = mid
    return lo


def integer_cube_root_floor(value: int) -> int:
    if value < 0:
        raise ValueError("cube root floor expects a nonnegative integer")
    lo = 0
    hi = 1
    while hi**3 <= value:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**3 <= value:
            lo = mid
        else:
            hi = mid
    return lo


def row_report(row: dict[str, Any]) -> dict[str, Any]:
    n = int(row["n"])
    m = int(row["max_shell_size"])
    threshold = exact_threshold(n)
    bound = centered_bound(n, m)
    cube_sufficient = integer_cube_root_floor(48 * n)

    check(
        f"{row['label']}: X49 max-shell threshold fits",
        m <= threshold,
        f"M={m}, T(n)={threshold}",
    )
    check(
        f"{row['label']}: X49 centered bound <= n^3",
        bound <= n**3,
        f"bound={bound}, n^3={n**3}",
    )
    check(
        f"{row['label']}: exact threshold boundary is sharp",
        fits_threshold(n, threshold) and not fits_threshold(n, threshold + 1),
        f"T(n)={threshold}",
    )

    return {
        "label": row["label"],
        "kind": row["kind"],
        "n": n,
        "p": row["p"],
        "max_shell_size": m,
        "exact_threshold": threshold,
        "cube_root_sufficient_threshold_floor_48n": cube_sufficient,
        "centered_bound_fraction": f"{bound.numerator}/{bound.denominator}",
        "centered_bound_ceiling": (bound.numerator + bound.denominator - 1) // bound.denominator,
        "n_cubed": n**3,
        "slack_to_threshold": threshold - m,
    }


def threshold_report(n: int) -> dict[str, Any]:
    threshold = exact_threshold(n)
    next_m = threshold + 1
    check(
        f"n={n}: exact threshold has correct boundary",
        fits_threshold(n, threshold) and not fits_threshold(n, next_m),
        f"T={threshold}, next={next_m}",
    )
    check(
        f"n={n}: exact threshold agrees with Fraction bound",
        centered_bound(n, threshold) <= n**3 and centered_bound(n, next_m) > n**3,
    )
    cube_sufficient = integer_cube_root_floor(48 * n)
    check(
        f"n={n}: cube-root sufficient threshold is safe",
        centered_bound(n, cube_sufficient) <= n**3,
        f"floor((48n)^(1/3))={cube_sufficient}",
    )
    return {
        "n": n,
        "exact_threshold": threshold,
        "first_failing_shell_size": next_m,
        "cube_root_sufficient_threshold_floor_48n": cube_sufficient,
        "threshold_bound_fraction": (
            f"{centered_bound(n, threshold).numerator}/"
            f"{centered_bound(n, threshold).denominator}"
        ),
        "first_failing_bound_fraction": (
            f"{centered_bound(n, next_m).numerator}/"
            f"{centered_bound(n, next_m).denominator}"
        ),
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x49 = load_json(X49_CERT)
    check("X49 certificate exists and has rows", bool(x49.get("rows")))
    rows = [row_report(row) for row in x49["rows"]]
    powers = [16, 32, 64, 128, 256, 1024, 2**20, 2**41]
    threshold_table = [threshold_report(n) for n in powers]
    check("all X49 replay rows fit their exact threshold", all(row["slack_to_threshold"] >= 0 for row in rows))
    check("threshold table includes official-scale n=2^41", threshold_table[-1]["n"] == 2**41)
    return {
        "task": "X50 h=4 centered cube-root threshold",
        "node": "active_core_count_bound",
        "status": "PROVED EXACT THRESHOLD CONSEQUENCE OF X49",
        "theorem": (
            "X49 gives R_centered <= (C(M,4)/M) * n(n-2)/2.  For M>=4, "
            "C(M,4)/M = (M-1)(M-2)(M-3)/24, so this is <= n^3 exactly when "
            "(M-1)(M-2)(M-3)(n-2) <= 48 n^2.  The left side is increasing in "
            "M for M>=4, giving an exact row threshold T(n).  The simpler "
            "sufficient condition M^3 <= 48 n also closes the centered branch."
        ),
        "dependency_statuses": deps,
        "rows": rows,
        "threshold_table": threshold_table,
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

    print("\nthreshold table:")
    for row in cert["threshold_table"]:
        print(
            f"n={row['n']}: T={row['exact_threshold']} "
            f"cube_safe={row['cube_root_sufficient_threshold_floor_48n']} "
            f"first_fail={row['first_failing_shell_size']}"
        )

    print("\nX49 replay rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: M={row['max_shell_size']} "
            f"T={row['exact_threshold']} slack={row['slack_to_threshold']} "
            f"bound={row['centered_bound_ceiling']} n^3={row['n_cubed']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X50 h4 centered-threshold checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
