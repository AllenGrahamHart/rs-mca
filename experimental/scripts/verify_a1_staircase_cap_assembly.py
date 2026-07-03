#!/usr/bin/env python3
"""A1 verifier: assemble the staircase-cap packet.

This is a proof-assembly verifier, not a new search.  It replays the three
integrated gates used by A1:

  * P1: fixed-subcore reduction to affine rich points.
  * F3: affine-net rich points charge to mixed b=2 degree-1 pullbacks.
  * E33: toy constants for the near-k link population.

The verifier records the honest conclusion: the fixed-(k-1)-subcore rich-line
residue is closed after the unified strip, while the full deep-link staircase
still needs the lower-overlap / occupied-subcore accounting step already named
in the P1 packet.

Run:
  python3 experimental/scripts/verify_a1_staircase_cap_assembly.py
Refresh certificate:
  python3 experimental/scripts/verify_a1_staircase_cap_assembly.py --write-certificate
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
    "a1-staircase-cap-assembly",
    "a1_staircase_cap_assembly.json",
)

INPUTS = {
    "P1": {
        "script": "experimental/scripts/verify_p1_deep_link_staircase_conditional.py",
        "certificate": "experimental/data/certificates/p1-deep-link-staircase-conditional/p1_deep_link_staircase_conditional.json",
    },
    "F3": {
        "script": "experimental/scripts/verify_f3_net_absorption.py",
        "certificate": "experimental/data/certificates/f3-net-absorption/f3_net_absorption.json",
    },
    "E33": {
        "script": "experimental/scripts/verify_e33_deep_link_staircase.py",
        "certificate": "experimental/data/certificates/e33-deep-link-staircase/e33_deep_link_staircase.json",
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
    return {
        "script": script,
        "returncode": proc.returncode,
        "tail": tail,
    }


def load_json(rel: str) -> dict:
    path = os.path.join(REPO, rel)
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def summarize_inputs() -> tuple[dict[str, object], dict[str, object]]:
    runs = {name: run_input(name, data["script"]) for name, data in INPUTS.items()}
    certs = {name: load_json(data["certificate"]) for name, data in INPUTS.items()}
    return runs, certs


def build_assembly(certs: dict[str, dict]) -> dict[str, object]:
    p1 = certs["P1"]
    f3 = certs["F3"]
    e33 = certs["E33"]

    p1_rich = p1["rich_line_reduction_fixture"]
    original_f3 = next(
        row for row in f3["cases"] if row["name"] == "p3_original_three_direction_net"
    )
    e33_rows = e33["rows"]
    max_e33_anchor = max(row["max_partner_events_per_anchor"] for row in e33_rows)
    max_e33_subcore = max(row["max_partner_events_through_one_subcore"] for row in e33_rows)
    max_e33_ratio = max(
        row["max_partner_events_per_anchor"] / row["n"] for row in e33_rows
    )

    check(
        "P1 exposes the pre-strip rich-line obstruction",
        p1_rich["rich_parameters"] > p1_rich["n"],
        f"rich={p1_rich['rich_parameters']}, n={p1_rich['n']}",
    )
    check(
        "F3 charges the original P3 affine-net obstruction",
        original_f3["rich_points"] == 65 and f3["total_rich_points"] == 342,
        f"original={original_f3['rich_points']}, total={f3['total_rich_points']}",
    )
    check(
        "F3 uses only mixed b=2 pair trades",
        f3["total_pair_trades"] == 726 and f3["local_assertions"] == 4314,
        f"pair_trades={f3['total_pair_trades']}, identities={f3['local_assertions']}",
    )
    check(
        "E33 fixed-subcore toy cap is <= 5",
        max_e33_subcore <= 5,
        f"max_subcore={max_e33_subcore}",
    )
    check(
        "E33 anchor population remains linear",
        max_e33_anchor <= 5 * max(row["n"] for row in e33_rows),
        f"max_anchor={max_e33_anchor}, max_ratio={max_e33_ratio:.3f}",
    )

    return {
        "node": "deep_link_staircase",
        "task": "A1 staircase cap assembly",
        "status": "CONDITIONAL-ASSEMBLED",
        "closed_component": "p1 fixed-(k-1)-subcore rich-line residue closes after F3 mixed degree-1 pullback strip",
        "remaining_named_gap": "a1_lower_overlap_occupied_subcore_accounting",
        "proof_chain": [
            "P1 reduces partners through a fixed (k-1)-subcore to rich points of an affine line arrangement in (z,a).",
            "Single-direction rich points are tangent/pencil paid; multi-direction rich points are exactly the affine-net residue isolated by P3.",
            "F3 charges every multi-direction rich point by a spanning tree of mixed b=2 degree-1 pullback cells.",
            "Therefore the P1 fixed-subcore rich-line obstruction is removed by the unified strip.",
            "The full deep-link staircase follows once lower-overlap partners are assigned to O(n) occupied deep-subcore witnesses.",
        ],
        "constants": {
            "e33_max_partner_events_per_anchor": max_e33_anchor,
            "e33_max_partner_events_per_anchor_over_n": max_e33_ratio,
            "e33_max_partner_events_through_one_subcore": max_e33_subcore,
            "f3_total_rich_points_charged": f3["total_rich_points"],
            "f3_total_pair_trades": f3["total_pair_trades"],
            "p1_prestrip_rich_parameters": p1_rich["rich_parameters"],
            "p1_prestrip_fixture_n": p1_rich["n"],
        },
        "interpretation": (
            "A1 closes the rich-line chapter at the fixed-subcore model level. "
            "It does not honestly flip deep_link_staircase to PROVED until the "
            "lower-overlap / occupied-subcore accounting is supplied."
        ),
    }


def main() -> int:
    write = "--write-certificate" in sys.argv
    runs, certs = summarize_inputs()
    assembly = build_assembly(certs)
    result = {
        "inputs": runs,
        "assembly": assembly,
        "checks": NCHECK,
    }
    check(
        "A1 honest status is conditional on occupied-subcore accounting",
        assembly["status"] == "CONDITIONAL-ASSEMBLED"
        and assembly["remaining_named_gap"] == "a1_lower_overlap_occupied_subcore_accounting",
    )
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
