#!/usr/bin/env python3
"""X53 h=4 centered standard-line-bound gap.

The h=2 rung imports subgroup-points-on-lines bounds of size n^(2/3).
X50 needs the centered shell maximum M to be O(n^(1/3)).  This verifier records
the exact arithmetic comparison, so the centered h=4 branch does not silently
reuse a line-bound that is one exponent too weak.
"""

from __future__ import annotations

from fractions import Fraction
import json
import math
import os
import sys
from typing import Any

import verify_x50_h4_centered_threshold as x50


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x53-h4-centered-line-bound-gap",
    "x53_h4_centered_line_bound_gap.json",
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
        "pte_h2_rung": "PROVED",
        "x50_h4_centered_threshold": "PROVED",
        "x52_h4_centered_field_uniformity": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def line_bound_fits_threshold(n: int, constant: int, threshold: int) -> bool:
    """Return whether constant*n^(2/3) <= threshold, using integer arithmetic."""
    return constant**3 * n * n <= threshold**3


def energy_bound_from_line_constant(n: int, constant: int) -> Fraction:
    """X49 max-shell bound after substituting M <= constant*n^(2/3)."""
    return Fraction(constant**3 * n * n, 48) * n * (n - 2)


def row_report(n: int) -> dict[str, Any]:
    threshold = x50.exact_threshold(n)
    cube_safe = x50.integer_cube_root_floor(48 * n)
    general_constant = 6
    prime_constant = 2
    general_fits = line_bound_fits_threshold(n, general_constant, threshold)
    prime_fits = line_bound_fits_threshold(n, prime_constant, threshold)
    general_energy = energy_bound_from_line_constant(n, general_constant)
    prime_energy = energy_bound_from_line_constant(n, prime_constant)

    if n >= 16:
        check(
            f"n={n}: general 6*n^(2/3) line bound does not imply X50",
            not general_fits,
            f"T={threshold}",
        )
        check(
            f"n={n}: prime-field 2*n^(2/3) line bound does not imply X50",
            not prime_fits,
            f"T={threshold}",
        )
    else:
        check(f"n={n}: general line-bound comparison evaluated", isinstance(general_fits, bool))

    check(
        f"n={n}: cube-root X50 threshold is strictly smaller than general line exponent",
        threshold**3 < general_constant**3 * n * n,
    )
    return {
        "n": n,
        "exact_threshold": threshold,
        "cube_root_sufficient_threshold_floor_48n": cube_safe,
        "general_line_constant": general_constant,
        "prime_line_constant": prime_constant,
        "general_line_bound_fits_threshold": general_fits,
        "prime_line_bound_fits_threshold": prime_fits,
        "general_line_energy_bound_fraction": f"{general_energy.numerator}/{general_energy.denominator}",
        "prime_line_energy_bound_fraction": f"{prime_energy.numerator}/{prime_energy.denominator}",
        "n_cubed": n**3,
        "general_line_energy_over_n3_fraction": f"{general_energy.numerator}/{general_energy.denominator * n**3}",
        "prime_line_energy_over_n3_fraction": f"{prime_energy.numerator}/{prime_energy.denominator * n**3}",
        "general_shell_gap_bits": math.log2(general_constant) + 2 * math.log2(n) / 3 - math.log2(threshold),
        "prime_shell_gap_bits": math.log2(prime_constant) + 2 * math.log2(n) / 3 - math.log2(threshold),
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    rows = [row_report(n) for n in (16, 32, 64, 128, 256, 512, 1024, 2**20, 2**41)]
    check("general line-bound route fails every recorded row", all(not row["general_line_bound_fits_threshold"] for row in rows))
    check("prime-field line-bound route fails every recorded row", all(not row["prime_line_bound_fits_threshold"] for row in rows))
    check("official-scale row included", rows[-1]["n"] == 2**41)
    return {
        "task": "X53 h=4 centered standard-line-bound gap",
        "node": "active_core_count_bound",
        "status": "PROVED COMPARISON: N^(2/3) LINE BOUNDS DO NOT CLOSE X50",
        "theorem": (
            "The h=2 subgroup-point input gives a fixed-line shell bound of order "
            "n^(2/3): M <= 6 n^(2/3) generally, and M <= 2 n^(2/3) in the prime-field "
            "Garcia-Voloch variant recorded in pte_h2_rung.  X50 requires "
            "M <= T(n) ~ (48n)^(1/3).  Exact integer comparison shows both "
            "n^(2/3) line bounds are too weak from n=16 onward, including the "
            "official-scale n=2^41 row.  The centered branch therefore needs "
            "dyadic/norm-gate rigidity, a fourth-moment distribution theorem, or "
            "another input genuinely at exponent <= 1/3."
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

    print("\nline-bound gap rows:")
    for row in cert["rows"]:
        print(
            f"n={row['n']}: T={row['exact_threshold']} "
            f"general_gap_bits={row['general_shell_gap_bits']:.3f} "
            f"prime_gap_bits={row['prime_shell_gap_bits']:.3f}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X53 h4 centered line-bound-gap checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
