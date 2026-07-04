#!/usr/bin/env python3
"""X74 h=4 normalized-sieve orbit bound.

X73 gives a complete normalized-pair sieve for row-local h=4 norm gates.  This
verifier records the counting consequence in X65 row-count currency: the
primitive h=4 norm-gate canonical-orbit count is < n^3 for every 2-power row.
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
    "x74-h4-sieve-orbit-bound",
    "x74_h4_sieve_orbit_bound.json",
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
X68_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x68-h4-norm-gate-certifier-keys",
    "x68_h4_norm_gate_certifier_keys.json",
)
X73_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x73-h4-normalized-pair-sieve",
    "x73_h4_normalized_pair_sieve.json",
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
        "x68_h4_norm_gate_certifier_keys": "PROVED",
        "x73_h4_normalized_pair_sieve": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def row_report(
    row73: dict[str, Any],
    row65: dict[str, Any],
    row68: dict[str, Any],
) -> dict[str, Any]:
    label = row73["label"]
    n = int(row73["n"])
    phi = n // 2
    survivor_pairs = int(row73["survivor_normalized_pair_count"])
    survivor_keys = int(row73["survivor_key_count"])
    primitive_orbits = int(row65["primitive_canonical_orbit_count"])
    x68_keys = int(row68["certifier_key_count"])

    pair_bound = 2 * phi * (n - 1)
    key_to_orbit_bound = survivor_keys * phi
    normalized_pair_orbit_bound = survivor_pairs * phi
    uniform_orbit_bound = pair_bound * phi
    terminal_bound = n**3

    check(
        f"{label}: X73 and X68 key counts agree",
        survivor_keys == x68_keys,
        f"X73={survivor_keys}, X68={x68_keys}",
    )
    check(
        f"{label}: survivor keys are bounded by survivor normalized pairs",
        survivor_keys <= survivor_pairs,
        f"keys={survivor_keys}, pairs={survivor_pairs}",
    )
    check(
        f"{label}: survivor normalized pairs obey 2 phi(n)(n-1) bound",
        survivor_pairs <= pair_bound,
        f"pairs={survivor_pairs}, bound={pair_bound}",
    )
    check(
        f"{label}: primitive canonical orbits obey key-times-phi bound",
        primitive_orbits <= key_to_orbit_bound,
        f"orbits={primitive_orbits}, key_phi={key_to_orbit_bound}",
    )
    check(
        f"{label}: primitive canonical orbits obey normalized-pair-times-phi bound",
        primitive_orbits <= normalized_pair_orbit_bound,
        f"orbits={primitive_orbits}, pair_phi={normalized_pair_orbit_bound}",
    )
    check(
        f"{label}: uniform h4 orbit bound is below n^3",
        uniform_orbit_bound < terminal_bound,
        f"uniform={uniform_orbit_bound}, n^3={terminal_bound}",
    )
    check(
        f"{label}: replay primitive orbits are below n^3",
        primitive_orbits < terminal_bound,
        f"orbits={primitive_orbits}, n^3={terminal_bound}",
    )

    return {
        "label": label,
        "kind": row73["kind"],
        "n": n,
        "p": int(row73["p"]),
        "phi_n": phi,
        "survivor_normalized_pair_count": survivor_pairs,
        "survivor_key_count": survivor_keys,
        "primitive_canonical_orbit_count": primitive_orbits,
        "normalized_pair_bound_2_phi_n_minus_1": pair_bound,
        "key_to_orbit_bound_phi_per_key": key_to_orbit_bound,
        "normalized_pair_to_orbit_bound": normalized_pair_orbit_bound,
        "uniform_orbit_bound": uniform_orbit_bound,
        "terminal_n_cubed_bound": terminal_bound,
        "uniform_bound_slack": terminal_bound - uniform_orbit_bound,
        "replay_orbit_slack": terminal_bound - primitive_orbits,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x65 = load_json(X65_CERT)
    x68 = load_json(X68_CERT)
    x73 = load_json(X73_CERT)
    check("X65 certificate has replay rows", bool(x65.get("rows")))
    check("X68 certificate has replay rows", bool(x68.get("rows")))
    check("X73 certificate has replay rows", bool(x73.get("rows")))
    rows65 = by_label(x65["rows"])
    rows68 = by_label(x68["rows"])
    rows = []
    for row73 in x73["rows"]:
        label = row73["label"]
        check(f"{label}: X65 row exists", label in rows65)
        check(f"{label}: X68 row exists", label in rows68)
        rows.append(row_report(row73, rows65[label], rows68[label]))

    check(
        "all replay rows satisfy the uniform h4 n^3 orbit bound",
        all(row["uniform_orbit_bound"] < row["terminal_n_cubed_bound"] for row in rows),
    )
    check(
        "all replay primitive orbit counts satisfy the h4 n^3 bound",
        all(row["primitive_canonical_orbit_count"] < row["terminal_n_cubed_bound"] for row in rows),
    )

    return {
        "task": "X74 h=4 normalized-sieve orbit bound",
        "node": "active_core_count_bound",
        "status": "PROVED H4 COUNTING CONSEQUENCE: PRIMITIVE NORM-GATE CANONICAL ORBITS ARE < n^3",
        "theorem": (
            "For n=2^s, X73 survivor normalized pairs are bounded by "
            "2*phi(n)*(n-1): for each primitive root, sign, and interval "
            "length, the interval start is forced if it exists.  X68 classes "
            "contain at most phi(n) X64 canonical row representatives because "
            "unit scaling has phi(n) choices after quotienting by the X64 "
            "eightfold orbit.  Therefore the primitive h=4 norm-gate canonical "
            "orbit count is at most 2*phi(n)^2*(n-1) = n^2*(n-1)/2 < n^3."
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

    print("\nh4 orbit-bound rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: orbits={row['primitive_canonical_orbit_count']} "
            f"uniform_bound={row['uniform_orbit_bound']} "
            f"n^3={row['terminal_n_cubed_bound']}"
        )

    if FAILS:
        print(f"\nFAIL: {len(FAILS)} checks failed: {FAILS}", file=sys.stderr)
        return 1
    print(f"\nPASS: {NCHECK} X74 h4 sieve-orbit bound checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
