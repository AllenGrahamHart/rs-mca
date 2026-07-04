#!/usr/bin/env python3
"""X77 h=5 first-level norm-gate reduction.

X24 removes characteristic-zero h=5 trades.  X30 says any finite-p odd-h trade
cannot enter the antipodal descent branch and must instead trigger the
top-level sparse norm gate.  This verifier records that specialization and
replays the landed h=5 no-collision windows.
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
    "x77-h5-norm-gate-reduction",
    "x77_h5_norm_gate_reduction.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")
X15_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x15-h5-empty-sweep",
    "x15_h5_empty_sweep.json",
)
X25_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x25-h5-prime-window",
    "x25_h5_prime_window.json",
)
X30_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x30-finite-p-norm-gate",
    "x30_finite_p_norm_gate.json",
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
        "x24_char0_dyadic_descent": "PROVED",
        "x30_finite_p_norm_gate": "PROVED",
        "x25_h5_prime_window": "TEST",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x15 = load_json(X15_CERT)
    x25 = load_json(X25_CERT)
    x30 = load_json(X30_CERT)
    odd_h = {int(row["h"]): bool(row["can_be_antipodal_union"]) for row in x30["odd_h_rows"]}

    check("X30 certificate records h=5 as non-antipodal", odd_h.get(5) is False)
    check("X25 h=5 full n=16,32 windows have no collision rows", all(not f["collision_rows"] for f in x25["families"]))
    check("X15 h=5 selected rows have no collision rows", not x15["summary"]["collision_rows"])
    check("X15 selected h=5 rows reach n=64", int(x15["summary"]["max_n"]) >= 64)
    check(
        "X25 h=5 full windows cover n=16 and n=32",
        {int(f["n"]) for f in x25["families"]} == {16, 32},
    )

    full_window_rows = [
        {
            "n": int(family["n"]),
            "prime_count": int(family["prime_count"]),
            "p_min": int(family["p_min"]),
            "p_max": int(family["p_max"]),
            "collision_rows": len(family["collision_rows"]),
            "max_subset_count": int(family["max_subset_count"]),
        }
        for family in x25["families"]
    ]
    selected_rows = [
        {
            "label": row["label"],
            "n": int(row["n"]),
            "p": int(row["first_prime_p_1_mod_n_after_floor_n_alpha"]),
            "exponent": row["exponent"],
            "subset_count": int(row["subset_count"]),
            "collision_groups": int(row["signature_collision_groups"]),
        }
        for row in x15["rows"]
    ]

    return {
        "task": "X77 h=5 norm-gate reduction",
        "node": "active_core_count_bound",
        "status": "PROVED REDUCTION + FINITE EVIDENCE: H5 TRADES ARE FIRST-LEVEL P-SPECIFIC NORM GATES; CHECKED WINDOWS ARE EMPTY",
        "theorem": (
            "For h=5 on a 2-power row, the X30 dyadic descent branch is "
            "impossible because an antipodal union has even size.  X24 also "
            "proves characteristic-zero h=5 trades are empty.  Hence any "
            "finite-field h=5 trade must be a first-level p-specific sparse "
            "norm-gate event for the signed 5+5 first-sum word.  The X25 full "
            "n=16,32 boundary windows and X15 selected n=32,64 rows have no "
            "same-top-four collisions, so no such norm-gated h=5 trades occur "
            "in those checked scopes."
        ),
        "dependency_statuses": deps,
        "x30_odd_h_rows": x30["odd_h_rows"],
        "full_prime_window_rows": full_window_rows,
        "selected_empty_rows": selected_rows,
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

    print("\nh5 norm-gate reduction rows:")
    for row in cert["full_prime_window_rows"]:
        print(
            f"full n={row['n']}: primes={row['prime_count']} "
            f"p=[{row['p_min']},{row['p_max']}] collisions={row['collision_rows']}"
        )
    print(f"selected rows: {len(cert['selected_empty_rows'])}")

    if FAILS:
        print(f"\nFAIL: {len(FAILS)} checks failed: {FAILS}", file=sys.stderr)
        return 1
    print(f"\nPASS: {NCHECK} X77 h5 norm-gate reduction checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
