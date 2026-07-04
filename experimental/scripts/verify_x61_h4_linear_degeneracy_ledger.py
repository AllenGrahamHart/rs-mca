#!/usr/bin/env python3
"""X61 h=4 linear-triple degeneracy ledger.

X60 filters five loci from the linear equation x+y-z=1 in H^3.  Three are
the genuine S-unit degeneracies of x + y - z - 1 = 0:

    x=1,  y=1,  y=-x.

The other two, y=x and z=1, are diagonal/source-overlap line branches.  This
verifier records their exact count as D+1, where D is the X58 diagonal
correction, and checks that the existing h=2 line-bound scale is below the
X60 barrier on every threshold-table row.
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
    "x61-h4-linear-degeneracy-ledger",
    "x61_h4_linear_degeneracy_ledger.json",
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
X58_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x58-h4-reduced-additive-energy",
    "x58_h4_reduced_additive_energy.json",
)
X60_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x60-h4-linear-triple-form",
    "x60_h4_linear_triple_form.json",
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
        "pte_h2_rung": "PROVED",
        "x50_h4_centered_threshold": "PROVED",
        "x58_h4_reduced_additive_energy": "PROVED",
        "x60_h4_linear_triple_form": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def indexed_by_label(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {str(row["label"]): row for row in rows}


def row_report(x60_row: dict[str, Any], x58_row: dict[str, Any]) -> dict[str, Any]:
    n = int(x60_row["n"])
    branches = x60_row["branch_counts"]
    d = int(x58_row["diagonal_target_count"])
    check(
        f"{x60_row['label']}: x=1 branch has n raw points",
        int(branches["x_equals_1"]) == n,
        f"branch={branches['x_equals_1']}, n={n}",
    )
    check(
        f"{x60_row['label']}: y=1 branch has n raw points",
        int(branches["y_equals_1"]) == n,
        f"branch={branches['y_equals_1']}, n={n}",
    )
    check(
        f"{x60_row['label']}: y=-x branch has n raw points",
        int(branches["y_equals_minus_x"]) == n,
        f"branch={branches['y_equals_minus_x']}, n={n}",
    )
    check(
        f"{x60_row['label']}: y=x branch equals D+1",
        int(branches["y_equals_x"]) == d + 1,
        f"branch={branches['y_equals_x']}, D={d}",
    )
    check(
        f"{x60_row['label']}: z=1 branch equals D+1",
        int(branches["z_equals_1"]) == d + 1,
        f"branch={branches['z_equals_1']}, D={d}",
    )
    return {
        "label": x60_row["label"],
        "kind": x60_row["kind"],
        "n": n,
        "p": x60_row["p"],
        "sunit_degenerate_branches": {
            "x_equals_1": branches["x_equals_1"],
            "y_equals_1": branches["y_equals_1"],
            "y_equals_minus_x": branches["y_equals_minus_x"],
        },
        "diagonal_correction_D": d,
        "source_overlap_branch_y_equals_x": branches["y_equals_x"],
        "diagonal_branch_z_equals_1": branches["z_equals_1"],
        "branch_formula": "y=x count = z=1 count = D+1",
    }


def scale_report(row: dict[str, Any]) -> dict[str, Any]:
    n = int(row["n"])
    threshold = int(row["exact_threshold"])
    linear_barrier = 8 * math.comb(threshold + 1, 2)
    # pte_h2_rung gives a fixed-line bound <= 12*n^(2/3).  The strict
    # comparison below proves 12*n^(2/3)+1 < linear_barrier.
    line_plus_one_fits = 1728 * n * n < (linear_barrier - 1) ** 3
    check(
        f"n={n}: h2 fixed-line scale plus one fits below X60 barrier",
        line_plus_one_fits,
        f"1728*n^2={1728*n*n}, (B-1)^3={(linear_barrier-1)**3}",
    )
    return {
        "n": n,
        "exact_threshold": threshold,
        "x60_linear_barrier": linear_barrier,
        "h2_fixed_line_plus_one_comparison": {
            "inequality": "12*n^(2/3)+1 < 8*C(T+1,2)",
            "holds": line_plus_one_fits,
            "cubed_left_without_plus_one": 1728 * n * n,
            "cubed_right_after_minus_one": (linear_barrier - 1) ** 3,
        },
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x50 = load_json(X50_CERT)
    x58 = indexed_by_label(load_json(X58_CERT)["rows"])
    x60 = load_json(X60_CERT)
    check("X60 certificate has replay rows", bool(x60.get("rows")))
    check("X58 labels cover X60 rows", all(row["label"] in x58 for row in x60["rows"]))
    rows = [row_report(row, x58[row["label"]]) for row in x60["rows"]]
    scale_table = [scale_report(row) for row in x50["threshold_table"]]
    check(
        "all scale rows fit the h2 fixed-line plus-one branch below X60 barrier",
        all(row["h2_fixed_line_plus_one_comparison"]["holds"] for row in scale_table),
    )
    return {
        "task": "X61 h=4 linear degeneracy ledger",
        "node": "active_core_count_bound",
        "status": "PROVED DEGENERACY LEDGER AND DIAGONAL-LINE AFFORDABILITY",
        "theorem": (
            "For x+y-z-1=0, the only proper vanishing subsums on H^3 are "
            "x=1, y=1, and y=-x.  X60's additional excluded loci y=x and z=1 "
            "are source-overlap/diagonal line branches, each of size D+1 where "
            "D is X58's diagonal correction.  The pte_h2_rung fixed-line bound "
            "puts each such branch below 12*n^(2/3)+1, and exact X50 arithmetic "
            "shows this is below the X60 barrier 8*C(T+1,2) on every recorded "
            "threshold row."
        ),
        "dependency_statuses": deps,
        "rows": rows,
        "scale_table": scale_table,
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

    print("\nlinear degeneracy rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: n={row['n']} D={row['diagonal_correction_D']} "
            f"y=x={row['source_overlap_branch_y_equals_x']} "
            f"z=1={row['diagonal_branch_z_equals_1']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X61 linear-degeneracy ledger checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
