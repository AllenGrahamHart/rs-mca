#!/usr/bin/env python3
"""X58 h=4 centered surplus as reduced shifted additive energy.

X56 defines the anchored nonzero h=2 surplus:

    A = #{(a,{b,c}) : 1+a=b+c, {b,c} disjoint from {1,a}}.

This verifier records the equivalent shifted-additive-energy form.  Let

    I = #{(a,b,c) in H^3 : a not in {1,-1}, 1+a=b+c}
    D = #{a in H\\{1,-1}: (1+a)/2 in H}.

Then

    A = (I - D - 2(n-2))/2.

The term 2(n-2) is the two ordered copies of the source pair (1,a); D is the
ordered diagonal target b=c.
"""

from __future__ import annotations

from collections import Counter
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
    "x58-h4-reduced-additive-energy",
    "x58_h4_reduced_additive_energy.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")
X56_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x56-h2-anchored-surplus-currency",
    "x56_h2_anchored_surplus_currency.json",
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
        "x56_h2_anchored_surplus_currency": "PROVED",
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
    pair_sum_counts: Counter[int] = Counter()
    for b in domain:
        for c in domain:
            pair_sum_counts[(b + c) % p] += 1

    shifted_incidence = 0
    diagonal_targets = 0
    inv2 = pow(2, -1, p)
    for a in domain:
        if a in (1, p - 1):
            continue
        s = (1 + a) % p
        shifted_incidence += pair_sum_counts[s]
        if (s * inv2) % p in hset:
            diagonal_targets += 1

    source_pair_ordered = 2 * (n - 2)
    reduced_ordered = shifted_incidence - diagonal_targets - source_pair_ordered
    anchored_surplus = reduced_ordered // 2
    expected = int(row["anchored_nonzero_h2_surplus"])

    check(
        f"{row['label']}: reduced ordered incidence is even",
        reduced_ordered % 2 == 0,
        f"reduced={reduced_ordered}",
    )
    check(
        f"{row['label']}: reduced additive energy equals X56 anchored surplus",
        anchored_surplus == expected,
        f"computed={anchored_surplus}, expected={expected}",
    )
    check(
        f"{row['label']}: shifted incidence decomposes into trivial plus surplus",
        shifted_incidence == diagonal_targets + source_pair_ordered + 2 * expected,
        f"I={shifted_incidence}, D={diagonal_targets}, source={source_pair_ordered}, A={expected}",
    )
    check(
        f"{row['label']}: diagonal target count is at most n-2",
        0 <= diagonal_targets <= n - 2,
        f"D={diagonal_targets}",
    )

    return {
        "label": row["label"],
        "kind": row["kind"],
        "n": n,
        "p": p,
        "shifted_ordered_incidence": shifted_incidence,
        "diagonal_target_count": diagonal_targets,
        "source_pair_ordered_trivial_count": source_pair_ordered,
        "reduced_ordered_incidence": reduced_ordered,
        "anchored_nonzero_h2_surplus": anchored_surplus,
        "x56_anchored_barrier": row["anchored_x55_barrier"],
        "x56_barrier_margin": row["anchored_barrier_margin"],
        "normal_form": "A = (I - D - 2(n-2))/2",
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x56 = load_json(X56_CERT)
    check("X56 certificate has replay rows", bool(x56.get("rows")))
    rows = [row_report(row) for row in x56["rows"]]
    check(
        "all replay rows match X56 anchored surplus",
        all(row["anchored_nonzero_h2_surplus"] * 2 == row["reduced_ordered_incidence"] for row in rows),
    )
    check(
        "some replay row has nonzero reduced surplus",
        any(row["anchored_nonzero_h2_surplus"] > 0 for row in rows),
    )
    return {
        "task": "X58 h=4 reduced additive energy normal form",
        "node": "active_core_count_bound",
        "status": "PROVED EXACT REDUCED-ENERGY IDENTITY",
        "theorem": (
            "For H=mu_n and anchored source pair {1,a}, ordered targets "
            "(b,c) with 1+a=b+c split into the two ordered copies of the "
            "source pair, possible diagonal targets b=c, and two ordered "
            "copies of each valid disjoint target pair.  Summing over "
            "a in H\\{1,-1} gives A_anchor_surplus = (I - D - 2(n-2))/2."
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

    print("\nreduced additive-energy rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: I={row['shifted_ordered_incidence']} "
            f"D={row['diagonal_target_count']} "
            f"source={row['source_pair_ordered_trivial_count']} "
            f"A={row['anchored_nonzero_h2_surplus']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X58 reduced additive-energy checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
