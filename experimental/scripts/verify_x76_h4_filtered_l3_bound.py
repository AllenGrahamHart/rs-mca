#!/usr/bin/env python3
"""X76 h=4 filtered-triple L3 bound.

X75 bounds primitive h=4 canonical row orbits by n(n-1).  X65 proves that the
filtered linear-triple count is exactly eight times the canonical orbit count.
This verifier records the row-count consequence: the primitive h=4 filtered
linear-triple mass is < n^3 for every relevant 2-power row.
"""

from __future__ import annotations

import json
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
    "x76-h4-filtered-l3-bound",
    "x76_h4_filtered_l3_bound.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")
X65_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x65-h4-linear-orbit-budget",
    "x65_h4_linear_orbit_budget.json",
)
X75_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x75-h4-witness-injection-bound",
    "x75_h4_witness_injection_bound.json",
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


def by_label(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {row["label"]: row for row in rows}


def check_dependency_nodes() -> dict[str, str]:
    dag = load_json(DAG)
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    needed = {
        "x65_h4_linear_orbit_budget": "PROVED",
        "x75_h4_witness_injection_bound": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def row_report(row65: dict[str, Any], row75: dict[str, Any]) -> dict[str, Any]:
    label = row65["label"]
    n = int(row65["n"])
    primitive_orbits = int(row65["primitive_canonical_orbit_count"])
    primitive_triples = 8 * primitive_orbits
    witness_bound = int(row75["witness_bound_2_phi_n_minus_1"])
    orbit_expanded_bound = 8 * witness_bound
    n_cubed = n**3

    check(
        f"{label}: X65 primitive triples are eight times primitive orbits",
        primitive_triples == 8 * primitive_orbits,
        f"triples={primitive_triples}, orbits={primitive_orbits}",
    )
    check(
        f"{label}: X75 witness bound matches n(n-1)",
        witness_bound == n * (n - 1),
        f"witness={witness_bound}, n(n-1)={n * (n - 1)}",
    )
    check(
        f"{label}: witness-expanded primitive triple bound is below n^3",
        orbit_expanded_bound < n_cubed,
        f"expanded={orbit_expanded_bound}, n^3={n_cubed}",
    )
    check(
        f"{label}: replay primitive triple count is below n^3",
        primitive_triples < n_cubed,
        f"triples={primitive_triples}, n^3={n_cubed}",
    )

    return {
        "label": label,
        "kind": row65["kind"],
        "n": n,
        "p": int(row65["p"]),
        "primitive_canonical_orbit_count": primitive_orbits,
        "primitive_filtered_triple_count": primitive_triples,
        "witness_orbit_bound": witness_bound,
        "filtered_triple_bound_8n_nminus1": orbit_expanded_bound,
        "n_cubed_bound": n_cubed,
        "bound_slack": n_cubed - orbit_expanded_bound,
        "replay_slack": n_cubed - primitive_triples,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x65 = load_json(X65_CERT)
    x75 = load_json(X75_CERT)
    check("X65 certificate has replay rows", bool(x65.get("rows")))
    check("X75 certificate has replay rows", bool(x75.get("rows")))
    rows75 = by_label(x75["rows"])
    rows = []
    for row65 in x65["rows"]:
        label = row65["label"]
        check(f"{label}: X75 row exists", label in rows75)
        rows.append(row_report(row65, rows75[label]))

    check(
        "all replay rows satisfy the h4 filtered-triple L3 bound",
        all(row["filtered_triple_bound_8n_nminus1"] < row["n_cubed_bound"] for row in rows),
    )
    check(
        "all replay primitive filtered-triple counts are below n^3",
        all(row["primitive_filtered_triple_count"] < row["n_cubed_bound"] for row in rows),
    )

    return {
        "task": "X76 h=4 filtered-triple L3 bound",
        "node": "active_core_count_bound",
        "status": "PROVED H4 ROW-COUNT CONSEQUENCE: PRIMITIVE FILTERED TRIPLES ARE < n^3",
        "theorem": (
            "X65 proves primitive filtered h=4 triples equal eight times the "
            "primitive canonical orbit count.  X75 proves the primitive "
            "canonical orbit count is at most n(n-1).  Therefore primitive "
            "filtered h=4 triples are at most 8*n*(n-1), which is < n^3 for "
            "every 2-power row n>=8, the first size where disjoint h=4 "
            "supports exist."
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

    print("\nh4 filtered-triple rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: primitive_triples={row['primitive_filtered_triple_count']} "
            f"bound={row['filtered_triple_bound_8n_nminus1']} n^3={row['n_cubed_bound']}"
        )

    if FAILS:
        print(f"\nFAIL: {len(FAILS)} checks failed: {FAILS}", file=sys.stderr)
        return 1
    print(f"\nPASS: {NCHECK} X76 h4 filtered L3-bound checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
