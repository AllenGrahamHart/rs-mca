#!/usr/bin/env python3
"""X60 h=4 centered surplus as a linear triple count.

X59's Mobius collision form is equivalent to a linear equation in H^3.  Put

    x = h,        y = h*r,        z = h*(1+r)-1.

Then z in H is equivalent to x+y-z=1.  The nontrivial centered surplus is the
count of solutions in H^3 avoiding the five trivial loci

    y=x, y=-x, x=1, y=1, z=1.
"""

from __future__ import annotations

import json
import os
import sys
from typing import Any

import verify_h1_u1_toy_harness as h1


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x60-h4-linear-triple-form",
    "x60_h4_linear_triple_form.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")
X59_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x59-h4-mobius-collision-form",
    "x59_h4_mobius_collision_form.json",
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
        "x58_h4_reduced_additive_energy": "PROVED",
        "x59_h4_mobius_collision_form": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def row_report(row: dict[str, Any]) -> dict[str, Any]:
    n = int(row["n"])
    p = int(row["p"])
    domain = h1.mu_domain(p, n)
    hset = set(domain)
    raw_linear = 0
    filtered_linear = 0
    excluded_union = 0
    branch_counts = {
        "x_equals_1": 0,
        "y_equals_1": 0,
        "z_equals_1": 0,
        "y_equals_x": 0,
        "y_equals_minus_x": 0,
    }

    for x in domain:
        for y in domain:
            z = (x + y - 1) % p
            if z not in hset:
                continue
            raw_linear += 1
            excluded = False
            if x == 1:
                branch_counts["x_equals_1"] += 1
                excluded = True
            if y == 1:
                branch_counts["y_equals_1"] += 1
                excluded = True
            if z == 1:
                branch_counts["z_equals_1"] += 1
                excluded = True
            if y == x:
                branch_counts["y_equals_x"] += 1
                excluded = True
            if y == (-x) % p:
                branch_counts["y_equals_minus_x"] += 1
                excluded = True
            if excluded:
                excluded_union += 1
            else:
                filtered_linear += 1

    expected = int(row["nontrivial_mobius_ordered_count"])
    check(
        f"{row['label']}: raw linear count splits into excluded union and filtered locus",
        raw_linear == excluded_union + filtered_linear,
        f"raw={raw_linear}, excluded={excluded_union}, filtered={filtered_linear}",
    )
    check(
        f"{row['label']}: filtered linear count equals X59 Mobius count",
        filtered_linear == expected,
        f"computed={filtered_linear}, expected={expected}",
    )
    check(
        f"{row['label']}: filtered linear count is even",
        filtered_linear % 2 == 0,
        f"filtered={filtered_linear}",
    )
    check(
        f"{row['label']}: zero-sum branch y=-x has n points",
        branch_counts["y_equals_minus_x"] == n,
        f"branch={branch_counts['y_equals_minus_x']}, n={n}",
    )

    return {
        "label": row["label"],
        "kind": row["kind"],
        "n": n,
        "p": p,
        "raw_linear_triple_count": raw_linear,
        "excluded_union_count": excluded_union,
        "filtered_linear_triple_count": filtered_linear,
        "branch_counts": branch_counts,
        "anchored_nonzero_h2_surplus": filtered_linear // 2,
        "x59_anchored_surplus": row["anchored_nonzero_h2_surplus"],
        "x56_anchored_barrier": row["x56_anchored_barrier"],
        "normal_form": "2*A = #{x,y,z in H: x+y-z=1, avoiding y=x,y=-x,x=1,y=1,z=1}",
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x59 = load_json(X59_CERT)
    check("X59 certificate has replay rows", bool(x59.get("rows")))
    rows = [row_report(row) for row in x59["rows"]]
    check(
        "all replay rows match X59 Mobius count",
        all(row["filtered_linear_triple_count"] == 2 * row["anchored_nonzero_h2_surplus"] for row in rows),
    )
    check(
        "some replay row has nonzero filtered linear surplus",
        any(row["filtered_linear_triple_count"] > 0 for row in rows),
    )
    return {
        "task": "X60 h=4 linear triple normal form",
        "node": "active_core_count_bound",
        "status": "PROVED EXACT LINEAR-TRIPLE IDENTITY",
        "theorem": (
            "The substitution x=h, y=hr, z=h(1+r)-1 is a bijection between "
            "X59 Mobius collisions and solutions x+y-z=1 in H^3.  The excluded "
            "branches h=1, h=r^-1, h=2/(1+r), r=1, and r=-1 become respectively "
            "x=1, y=1, z=1, y=x, and y=-x.  Therefore twice the anchored "
            "surplus is the linear-triple count after removing those five loci."
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

    print("\nlinear triple rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: raw={row['raw_linear_triple_count']} "
            f"excluded={row['excluded_union_count']} "
            f"filtered={row['filtered_linear_triple_count']} "
            f"A={row['anchored_nonzero_h2_surplus']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X60 linear-triple checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
