#!/usr/bin/env python3
"""B-WRITEUP verifier: band-trade reduction packet consistency.

This is a proof-packet verifier, not a new census.  It replays the structural
inputs that the B write-up is allowed to use:

* P-B census: every toy canonical band trade routes to exits 1/2/3.
* X-10 DAG state: exit 3 is not solved by the old moving-curve route; it is
  conditional on the anchored non-toral PTE bound, including the defect/tails
  wrapper named in that node.

The verifier exits nonzero if the write-up would overclaim the status.
"""

from __future__ import annotations

import json
import os
import sys
from typing import Any


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
PB_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "pb-band-trade-census",
    "pb_band_trade_census.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "b-writeup-band-reduction",
    "b_writeup_band_reduction.json",
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
    print(line)
    if not cond:
        FAILS.append(name)


def load_json(path: str) -> Any:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def node_by_id(dag: dict[str, Any], node_id: str) -> dict[str, Any]:
    for node in dag["nodes"]:
        if node["id"] == node_id:
            return node
    raise KeyError(node_id)


def build_certificate() -> dict[str, Any]:
    pb = load_json(PB_CERT)
    dag = load_json(DAG)
    b_node = node_by_id(dag, "u1_beta_band_trade_reduction")
    pte_node = node_by_id(dag, "anchored_nontoral_pte_bound")

    aggregate = pb["aggregate_exit_counts"]
    routed = sum(aggregate.values())
    total = int(pb["total_canonical_band_trade_orbits"])
    check("P-B census routes every canonical orbit", routed == total, f"routed={routed}, total={total}")
    check("P-B census has no fourth exit", set(aggregate) == {
        "exit1_minimal_subtrade",
        "exit2_v1_pullback",
        "exit3_primitive_moment_pte",
    })
    check("P-B exit 3 is the dominant observed route", aggregate["exit3_primitive_moment_pte"] > aggregate["exit1_minimal_subtrade"] + aggregate["exit2_v1_pullback"])
    check("B node remains open", b_node["status"] == "TARGET", b_node["status"])
    check("B node records moving-curve failure", "moving curves" in b_node["statement"])
    check("anchored non-toral PTE node remains open", pte_node["status"] == "TARGET", pte_node["status"])
    check("X-10 node names defect/tails wrapper", "defect version" in pte_node["statement"] and "tails wrapper" in pte_node["statement"])

    row_summaries = []
    for row in pb["rows"]:
        exits = row["exit_counts"]
        row_total = int(row["canonical_band_trade_orbits"])
        check(
            f"{row['row']}: row exits sum to canonical count",
            sum(exits.values()) == row_total,
            f"sum={sum(exits.values())}, total={row_total}",
        )
        row_summaries.append(
            {
                "row": row["row"],
                "canonical_band_trade_orbits": row_total,
                "exit_counts": exits,
                "large_window_moment_residuals_h_gt_2t_plus_4": row[
                    "large_window_moment_residuals_h_gt_2t_plus_4"
                ],
            }
        )

    return {
        "task": "B-WRITEUP band-trade reduction",
        "node": "u1_beta_band_trade_reduction",
        "status": "CONDITIONAL: exits 1/2 reduce formally; exit 3 is the X-10 anchored non-toral PTE defect/tails bound",
        "pb_total_canonical_band_trade_orbits": total,
        "pb_aggregate_exit_counts": aggregate,
        "named_residue": "anchored_nontoral_pte_bound with defect/tails wrapper",
        "row_summaries": row_summaries,
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
        with open(CERT, encoding="utf-8") as fh:
            expected = json.load(fh)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", cert == expected)

    print("\nsummary:")
    print(json.dumps({
        "exit_counts": cert["pb_aggregate_exit_counts"],
        "named_residue": cert["named_residue"],
        "status": cert["status"],
    }, indent=2, sort_keys=True))

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        print("\nrecomputed summary:")
        print(json.dumps(cert, indent=2, sort_keys=True))
        return 1

    print(f"\nPASS: {NCHECK} B-WRITEUP consistency checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
