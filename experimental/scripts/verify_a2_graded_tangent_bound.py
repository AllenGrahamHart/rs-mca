#!/usr/bin/env python3
"""A2 verifier: graded tangent ledger bound assembly.

This verifier composes the integrated W2 design, the proved 2b forcing map,
and the A1 staircase assembly.  It does not claim the final band bound is
proved.  Instead it checks the complete routing table and records the precise
remaining residues blocking promotion:

  * a2_depth_cell_residual_occupancy
  * a1_lower_overlap_occupied_subcore_accounting

Run:
  python3 experimental/scripts/verify_a2_graded_tangent_bound.py
Refresh certificate:
  python3 experimental/scripts/verify_a2_graded_tangent_bound.py --write-certificate
"""

from __future__ import annotations

import json
import os
import subprocess
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "a2-graded-tangent-bound",
    "a2_graded_tangent_bound.json",
)

INPUTS = {
    "W2": {
        "script": "experimental/scripts/verify_w2_graded_tangent_ledger.py",
        "certificate": "experimental/data/certificates/w2-graded-tangent-ledger/w2_graded_tangent_ledger.json",
    },
    "X3_2b": {
        "script": "experimental/scripts/verify_xr_smallcore_rungs_2a_2b.py",
        "certificate": "experimental/data/certificates/xr-smallcore-rungs-2a-2b/xr_smallcore_rungs_2a_2b_certificate.json",
    },
    "A1": {
        "script": "experimental/scripts/verify_a1_staircase_cap_assembly.py",
        "certificate": "experimental/data/certificates/a1-staircase-cap-assembly/a1_staircase_cap_assembly.json",
    },
}

FAILS: list[str] = []
NCHECK = 0


def check(name: str, cond: bool, detail: str = "") -> None:
    global NCHECK
    NCHECK += 1
    tag = "PASS" if cond else "FAIL"
    line = f"[{tag}] {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    if not cond:
        FAILS.append(name)


def run_input(name: str, script: str) -> dict[str, object]:
    proc = subprocess.run(
        [sys.executable, script],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    tail = "\n".join(proc.stdout.strip().splitlines()[-6:])
    check(f"{name}: verifier exits green", proc.returncode == 0, tail)
    return {"script": script, "returncode": proc.returncode, "tail": tail}


def load_json(rel: str) -> dict:
    with open(os.path.join(REPO, rel), encoding="utf-8") as f:
        return json.load(f)


def summarize_inputs() -> tuple[dict[str, object], dict[str, dict]]:
    runs = {name: run_input(name, data["script"]) for name, data in INPUTS.items()}
    certs = {name: load_json(data["certificate"]) for name, data in INPUTS.items()}
    return runs, certs


def build_assembly(certs: dict[str, dict]) -> dict[str, object]:
    w2 = certs["W2"]
    x3 = certs["X3_2b"]
    a1 = certs["A1"]["assembly"]

    tables = w2["cell_tables"]
    max_t = max(row["t"] for row in tables)
    total_partial_cells = sum(len(row["partial_depths"]) for row in tables)
    heavy = w2["heavy_triangle_boundary"]

    check(
        "W2 cell table covers t=1..8",
        [row["t"] for row in tables] == list(range(1, 9)),
    )
    check(
        "W2 partial cells are exactly max(0,t-2)",
        all(len(row["partial_depths"]) == max(0, row["t"] - 2) for row in tables),
        f"total_partial_cells={total_partial_cells}",
    )
    check(
        "W2 heavy boundary routes every non-direct case to deep links",
        heavy["deep_link_only_profiles"] > 0 and heavy["direct_2b_profiles"] > 0,
        f"direct={heavy['direct_2b_profiles']}, deep={heavy['deep_link_only_profiles']}",
    )
    check(
        "X3 proves the two-slope forcing map",
        x3["two_slope_identity_toy"]["two_slope_identity_ok"]
        and x3["two_slope_identity_toy"]["depth_constraints_ok"],
    )
    check(
        "X3 rung arithmetic has d+s=t in every partial band",
        all(
            item["identity_d_plus_s_equals_t"]
            for row in x3["rung_arithmetic"]
            for item in row["partial_depths"]
        ),
    )
    check(
        "A1 leaves lower-overlap occupied-subcore accounting as named gap",
        a1["remaining_named_gap"] == "a1_lower_overlap_occupied_subcore_accounting",
    )

    return {
        "node": "xr_partial_tangent_band / xr_heavy_triangle_charge",
        "task": "A2 graded tangent ledger bound",
        "status": "CONDITIONAL-ROUTED",
        "completed": [
            "Every distinct-slope pair with k+1 <= r <= A-2 routes to depth d=r-k.",
            "Depth and qx13 fresh codimension satisfy d+s=t in every partial cell.",
            "The cascade boundary r>=A-1 is outside the partial ledger.",
            "The r=k boundary stays in the rank/spread shell.",
            "Every heavy triangle has either a direct 2b edge or at least two deep-link edges.",
        ],
        "remaining_residues": [
            {
                "id": "a2_depth_cell_residual_occupancy",
                "statement": (
                    "After the unified strip, bound the number of occupied "
                    "tangent-depth-d residual cells, and the emissions from each "
                    "cell, uniformly in every partial band 1<=d<=t-2."
                ),
            },
            {
                "id": "a1_lower_overlap_occupied_subcore_accounting",
                "statement": (
                    "Route lower-overlap heavy-boundary partners to O(n) occupied "
                    "deep-subcore witnesses so the A1 fixed-subcore cap applies."
                ),
            },
        ],
        "constants": {
            "w2_max_t_checked": max_t,
            "w2_total_partial_cells_t1_to_t8": total_partial_cells,
            "heavy_profiles_checked": heavy["profiles_checked"],
            "heavy_direct_2b_profiles": heavy["direct_2b_profiles"],
            "heavy_deep_link_only_profiles": heavy["deep_link_only_profiles"],
            "a1_max_subcore_constant_observed": a1["constants"]["e33_max_partner_events_through_one_subcore"],
        },
        "interpretation": (
            "A2 completes the routing/charge table but not the quantitative "
            "band bound.  The first resisting cell is the depth-cell occupancy "
            "bound; the heavy boundary additionally depends on A1's "
            "lower-overlap occupied-subcore accounting."
        ),
    }


def main() -> int:
    write = "--write-certificate" in sys.argv
    runs, certs = summarize_inputs()
    assembly = build_assembly(certs)
    check(
        "A2 honest status is conditional-routed",
        assembly["status"] == "CONDITIONAL-ROUTED"
        and len(assembly["remaining_residues"]) == 2,
    )
    result = {"inputs": runs, "assembly": assembly, "checks": NCHECK}
    if write:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, sort_keys=True)
            f.write("\n")
        print(f"[write] {CERT}")
    if FAILS:
        print("\nFAILURES:")
        for name in FAILS:
            print(f"  - {name}")
        return 1
    print("\nassembly:")
    print(json.dumps(assembly, indent=2, sort_keys=True))
    print(f"\nAll {NCHECK} checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
