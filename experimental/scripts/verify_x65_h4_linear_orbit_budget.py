#!/usr/bin/env python3
"""X65 h=4 linear orbit-budget currency.

X60 states the centered h=4 target as a filtered triple bound

    filtered_triples < 8*C(T(n)+1, 2).

X64 proves that filtered triples form free eightfold chord-pair orbits.
Therefore the same target is exactly

    canonical_orbits < C(T(n)+1, 2).

After X63 strips quotient-descended content, the top-level primitive residue
is the same inequality with primitive content-one canonical orbits.
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
    "x65-h4-linear-orbit-budget",
    "x65_h4_linear_orbit_budget.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")
X50_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x50-h4-centered-threshold",
    "x50_h4_centered_threshold.json",
)
X60_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x60-h4-linear-triple-form",
    "x60_h4_linear_triple_form.json",
)
X64_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x64-h4-linear-orbit-compression",
    "x64_h4_linear_orbit_compression.json",
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
        "x50_h4_centered_threshold": "PROVED",
        "x55_h4_surplus_threshold_bridge": "PROVED",
        "x56_h2_anchored_surplus_currency": "PROVED",
        "x60_h4_linear_triple_form": "PROVED",
        "x63_h4_linear_content_descent": "PROVED",
        "x64_h4_linear_orbit_compression": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def by_label(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}
    for row in rows:
        label = row["label"]
        check(f"label {label} appears once", label not in indexed)
        indexed[label] = row
    return indexed


def row_report(
    x50_row: dict[str, Any],
    x60_row: dict[str, Any],
    x64_row: dict[str, Any],
) -> dict[str, Any]:
    label = x64_row["label"]
    n = int(x64_row["n"])
    threshold = int(x50_row["exact_threshold"])
    orbit_barrier = math.comb(threshold + 1, 2)
    filtered_barrier = 8 * orbit_barrier
    anchored_barrier = 4 * orbit_barrier

    filtered = int(x64_row["filtered_linear_triple_count"])
    canonical_orbits = int(x64_row["canonical_orbit_count"])
    primitive_orbits = int(x64_row["primitive_canonical_orbit_count"])
    primitive_triples = int(x64_row["primitive_content_one_count"])
    quotient_descended_triples = int(x64_row["quotient_descended_count"])
    quotient_descended_orbits = canonical_orbits - primitive_orbits

    check(f"{label}: n agrees across X50/X60/X64", n == int(x50_row["n"]) == int(x60_row["n"]))
    check(f"{label}: p agrees across X50/X60/X64", int(x64_row["p"]) == int(x50_row["p"]) == int(x60_row["p"]))
    check(
        f"{label}: X60 filtered count agrees with X64",
        filtered == int(x60_row["filtered_linear_triple_count"]),
        f"X60={x60_row['filtered_linear_triple_count']}, X64={filtered}",
    )
    check(
        f"{label}: anchored barrier is half the filtered barrier",
        int(x60_row["x56_anchored_barrier"]) == anchored_barrier,
        f"cert={x60_row['x56_anchored_barrier']}, expected={anchored_barrier}",
    )
    check(
        f"{label}: X64 total orbit expansion is exact",
        filtered == 8 * canonical_orbits,
        f"filtered={filtered}, orbits={canonical_orbits}",
    )
    check(
        f"{label}: X64 primitive orbit expansion is exact",
        primitive_triples == 8 * primitive_orbits,
        f"primitive={primitive_triples}, primitive_orbits={primitive_orbits}",
    )
    check(
        f"{label}: quotient-descended count expands by eight orbits",
        quotient_descended_triples == 8 * quotient_descended_orbits,
        f"quotient_triples={quotient_descended_triples}, quotient_orbits={quotient_descended_orbits}",
    )
    check(
        f"{label}: filtered target equals canonical-orbit target",
        (filtered < filtered_barrier) == (canonical_orbits < orbit_barrier),
        f"filtered={filtered}/{filtered_barrier}, orbits={canonical_orbits}/{orbit_barrier}",
    )
    check(
        f"{label}: primitive target is no stronger than total target",
        primitive_orbits <= canonical_orbits,
        f"primitive_orbits={primitive_orbits}, total_orbits={canonical_orbits}",
    )

    return {
        "label": label,
        "kind": x64_row["kind"],
        "n": n,
        "p": int(x64_row["p"]),
        "exact_threshold": threshold,
        "orbit_barrier": orbit_barrier,
        "filtered_barrier": filtered_barrier,
        "anchored_barrier": anchored_barrier,
        "filtered_linear_triple_count": filtered,
        "canonical_orbit_count": canonical_orbits,
        "primitive_canonical_orbit_count": primitive_orbits,
        "quotient_descended_orbit_count": quotient_descended_orbits,
        "filtered_target_passes": filtered < filtered_barrier,
        "canonical_target_passes": canonical_orbits < orbit_barrier,
        "primitive_target_passes_after_quotient_strip": primitive_orbits < orbit_barrier,
        "canonical_margin": orbit_barrier - canonical_orbits,
        "primitive_canonical_margin": orbit_barrier - primitive_orbits,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x50 = load_json(X50_CERT)
    x60 = load_json(X60_CERT)
    x64 = load_json(X64_CERT)
    check("X50 certificate has replay rows", bool(x50.get("rows")))
    check("X60 certificate has replay rows", bool(x60.get("rows")))
    check("X64 certificate has replay rows", bool(x64.get("rows")))

    x50_rows = by_label(x50["rows"])
    x60_rows = by_label(x60["rows"])
    rows = []
    for x64_row in x64["rows"]:
        label = x64_row["label"]
        check(f"{label}: X50 row exists", label in x50_rows)
        check(f"{label}: X60 row exists", label in x60_rows)
        rows.append(row_report(x50_rows[label], x60_rows[label], x64_row))

    check(
        "filtered and canonical pass/fail decisions agree on every replay row",
        all(row["filtered_target_passes"] == row["canonical_target_passes"] for row in rows),
    )
    check(
        "at least one replay row shows quotient descent matters",
        any(
            (not row["canonical_target_passes"])
            and row["primitive_target_passes_after_quotient_strip"]
            for row in rows
        ),
    )
    check(
        "all replay rows pass the primitive post-quotient orbit target",
        all(row["primitive_target_passes_after_quotient_strip"] for row in rows),
    )
    check(
        "all campaign-boundary replay rows pass with primitive margin",
        all(
            row["primitive_target_passes_after_quotient_strip"]
            and row["primitive_canonical_margin"] > 0
            for row in rows
            if row["kind"] == "campaign_boundary"
        ),
    )

    return {
        "task": "X65 h=4 linear orbit-budget currency",
        "node": "active_core_count_bound",
        "status": "PROVED CURRENCY CONVERSION: X60 FILTERED TARGET EQUALS CANONICAL ORBIT TARGET",
        "theorem": (
            "X60 requires filtered_linear_triples < 8*C(T(n)+1,2). "
            "X64 proves filtered_linear_triples = 8*canonical_orbit_count "
            "on the filtered locus, so the target is exactly "
            "canonical_orbit_count < C(T(n)+1,2).  X63 strips "
            "content d>1 into quotient rows; hence the primitive top-level "
            "residue is measured by the same inequality with primitive "
            "content-one canonical orbits."
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

    print("\norbit-budget rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: orbits={row['canonical_orbit_count']}/"
            f"{row['orbit_barrier']} "
            f"primitive={row['primitive_canonical_orbit_count']}/"
            f"{row['orbit_barrier']} "
            f"primitive_margin={row['primitive_canonical_margin']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X65 h4 linear orbit-budget checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
