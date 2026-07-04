#!/usr/bin/env python3
"""X54 h=4 centered shell-surplus norm-gate bridge.

X41 says every nonzero pair-sum shell collision is a sparse h=2 norm gate.
This packet records the exact quadratic accounting:

    shell_surplus = sum_{s != 0} C(m_s,2)
                  = n * sum_C C(m_C,2),

where m_C is the X48 quotient-coset shell size.  Thus high centered shell
concentration is exactly high h=2 norm-gate surplus in the pair-sum layer.
"""

from __future__ import annotations

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
    "x54-h4-shell-surplus-norm-gate-bridge",
    "x54_h4_shell_surplus_norm_gate_bridge.json",
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
        "x31_h2_quotient_norm_criterion": "PROVED",
        "x41_h4_centered_norm_gate": "PROVED",
        "x48_h4_centered_coset_shell_param": "PROVED",
        "x52_h4_centered_field_uniformity": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def expand_histogram(hist: dict[str, int]) -> list[int]:
    out: list[int] = []
    for value, count in hist.items():
        out.extend([int(value)] * int(count))
    return out


def quadratic_surplus(values: list[int]) -> int:
    return sum(math.comb(value, 2) for value in values if value >= 2)


def quartic_energy(values: list[int]) -> int:
    return sum(math.comb(value, 4) for value in values if value >= 4)


def row_report(row: dict[str, Any]) -> dict[str, Any]:
    n = int(row["n"])
    direct_values = expand_histogram(row["direct_shell_size_histogram"])
    coset_values = expand_histogram(row["coset_shell_size_histogram"])
    direct_surplus = quadratic_surplus(direct_values)
    quotient_surplus = n * quadratic_surplus(coset_values)
    direct_energy = quartic_energy(direct_values)
    quotient_energy = n * quartic_energy(coset_values)
    max_shell = max(coset_values, default=0)
    forced_surplus_from_max = n * math.comb(max_shell, 2) if max_shell >= 2 else 0

    check(
        f"{row['label']}: direct surplus equals quotient-compressed surplus",
        direct_surplus == quotient_surplus,
        f"direct={direct_surplus}, quotient={quotient_surplus}",
    )
    check(
        f"{row['label']}: direct quartic energy equals quotient-compressed energy",
        direct_energy == quotient_energy,
        f"direct={direct_energy}, quotient={quotient_energy}",
    )
    check(
        f"{row['label']}: max shell forces its quadratic surplus",
        direct_surplus >= forced_surplus_from_max,
        f"surplus={direct_surplus}, forced={forced_surplus_from_max}",
    )
    check(
        f"{row['label']}: quartic energy implies quadratic surplus",
        direct_energy == 0 or direct_surplus > 0,
        f"energy={direct_energy}, surplus={direct_surplus}",
    )

    return {
        "label": row["label"],
        "kind": row["kind"],
        "n": n,
        "p": row["p"],
        "max_shell_size": max_shell,
        "direct_shell_surplus_pairs": direct_surplus,
        "quotient_shell_surplus_pairs": quotient_surplus,
        "forced_surplus_from_max_shell": forced_surplus_from_max,
        "direct_quartic_energy_bound": direct_energy,
        "quotient_quartic_energy_bound": quotient_energy,
        "direct_shell_size_histogram": row["direct_shell_size_histogram"],
        "coset_shell_size_histogram": row["coset_shell_size_histogram"],
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x48 = load_json(X48_CERT)
    check("X48 certificate exists and has rows", bool(x48.get("rows")))
    rows = [row_report(row) for row in x48["rows"]]
    check("some replay row has nonzero shell surplus", any(row["direct_shell_surplus_pairs"] > 0 for row in rows))
    check("some replay row has quartic centered energy", any(row["direct_quartic_energy_bound"] > 0 for row in rows))
    check("all replay rows satisfy surplus compression", all(row["direct_shell_surplus_pairs"] == row["quotient_shell_surplus_pairs"] for row in rows))
    return {
        "task": "X54 h=4 shell-surplus norm-gate bridge",
        "node": "active_core_count_bound",
        "status": "PROVED ACCOUNTING: CENTERED SHELL SURPLUS IS H2 NORM-GATE SURPLUS",
        "theorem": (
            "For every nonzero pair-sum shell S_s of size m_s, each unordered "
            "choice of two distinct shell pairs gives a nonzero h=2 pair-sum "
            "collision.  Distinct pairs in one shell are automatically disjoint, "
            "and by X41 each such collision is non-Phi-descended and p-norm-gated. "
            "Therefore the h=2 norm-gate surplus in centered shells is exactly "
            "sum_{s != 0} C(m_s,2).  By X48/X52, m_s is constant on H-cosets, so "
            "this equals n * sum_C C(m_C,2)."
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

    print("\nshell-surplus rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: M={row['max_shell_size']} "
            f"surplus={row['direct_shell_surplus_pairs']} "
            f"quartic={row['direct_quartic_energy_bound']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X54 h4 shell-surplus bridge checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
