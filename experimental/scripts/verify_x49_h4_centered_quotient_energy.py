#!/usr/bin/env python3
"""X49 h=4 centered quotient-energy compression.

X42 gives R_centered <= sum_s C(m_s,4).
X48 proves m_s is constant on multiplicative H-cosets, with

    m_C = 1/2 #{r in H\\{1}: 1+r in C}.

Since each nonzero quotient coset contains n field elements, this gives the
compressed accounting

    R_centered <= n * sum_C C(m_C,4),
    sum_C m_C = (n-2)/2.

The last identity excludes exactly the n/2 zero-sum antipodal pairs, already
paid by the quotient/cyclic ledger.
"""

from __future__ import annotations

from collections import Counter
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
    "x49-h4-centered-quotient-energy",
    "x49_h4_centered_quotient_energy.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")
X48_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x48-h4-centered-coset-shell-param",
    "x48_h4_centered_coset_shell_param.json",
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
        "x42_h4_centered_energy_accounting": "PROVED",
        "x44_h4_centered_max_shell_bound": "PROVED",
        "x48_h4_centered_coset_shell_param": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def expand_histogram(hist: dict[str, int]) -> list[int]:
    out: list[int] = []
    for key, count in hist.items():
        out.extend([int(key)] * count)
    return out


def max_shell_fraction_bound(n: int, max_shell: int) -> Fraction:
    if max_shell < 4:
        return Fraction(0, 1)
    return Fraction(math.comb(max_shell, 4), max_shell) * Fraction(n * (n - 2), 2)


def row_report(row: dict[str, Any]) -> dict[str, Any]:
    n = row["n"]
    values = expand_histogram(row["coset_shell_size_histogram"])
    quotient_mass = sum(values)
    expected_mass = (n - 2) // 2
    quotient_energy = n * sum(math.comb(value, 4) for value in values if value >= 4)
    max_shell = max(values, default=0)
    frac = max_shell_fraction_bound(n, max_shell)
    ceil_bound = (frac.numerator + frac.denominator - 1) // frac.denominator

    check(
        f"{row['label']}: quotient shell mass is (n-2)/2",
        quotient_mass == expected_mass,
        f"mass={quotient_mass}, expected={expected_mass}",
    )
    check(
        f"{row['label']}: quotient max matches X48 direct max",
        max_shell == row["max_direct_shell_size"] == row["max_coset_shell_size"],
    )
    check(
        f"{row['label']}: quotient max-shell bound dominates quotient energy",
        Fraction(quotient_energy, 1) <= frac,
        f"energy={quotient_energy}, bound={frac}",
    )
    check(
        f"{row['label']}: quotient energy fits n^3 in replay row",
        quotient_energy <= n**3,
        f"energy={quotient_energy}, n^3={n**3}",
    )

    return {
        "label": row["label"],
        "kind": row["kind"],
        "n": n,
        "p": row["p"],
        "quotient_cosets": row["quotient_cosets"],
        "quotient_shell_mass": quotient_mass,
        "expected_shell_mass": expected_mass,
        "max_shell_size": max_shell,
        "quotient_energy_bound": quotient_energy,
        "quotient_max_shell_bound_fraction": f"{frac.numerator}/{frac.denominator}",
        "quotient_max_shell_bound_ceiling": ceil_bound,
        "n_cubed": n**3,
        "coset_shell_size_histogram": row["coset_shell_size_histogram"],
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x48 = load_json(X48_CERT)
    check("X48 certificate exists and has rows", bool(x48.get("rows")))
    rows = [row_report(row) for row in x48["rows"]]
    check("all replay rows have quotient shell mass (n-2)/2", all(row["quotient_shell_mass"] == row["expected_shell_mass"] for row in rows))
    check("all replay quotient energies fit n^3", all(row["quotient_energy_bound"] <= row["n_cubed"] for row in rows))
    check("some replay row exercises nonzero quotient energy", any(row["quotient_energy_bound"] > 0 for row in rows))
    return {
        "task": "X49 h=4 centered quotient-energy compression",
        "node": "active_core_count_bound",
        "status": "PROVED QUOTIENT-COMPRESSED CENTERED ENERGY BOUND",
        "theorem": (
            "Let m_C be X48's shell size attached to the quotient coset C=sH. "
            "Since each coset has n values of s and m_s is constant on cosets, "
            "X42 gives R_centered <= n * sum_C C(m_C,4).  The total quotient "
            "mass sum_C m_C equals (n-2)/2, because the only excluded unordered "
            "pairs are the n/2 zero-sum antipodal pairs.  Therefore "
            "R_centered <= (C(M,4)/M) * n(n-2)/2, where M=max_C m_C.  This is "
            "the quotient-compressed form of X44's max-shell criterion."
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

    print("\nquotient-energy rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: mass={row['quotient_shell_mass']} "
            f"M={row['max_shell_size']} energy={row['quotient_energy_bound']} "
            f"max_bound={row['quotient_max_shell_bound_ceiling']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X49 h4 quotient-energy checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
