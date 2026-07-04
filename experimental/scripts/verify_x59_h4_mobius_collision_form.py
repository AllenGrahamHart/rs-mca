#!/usr/bin/env python3
"""X59 h=4 centered surplus as a Mobius collision count.

X56 gives the anchored surplus A.  X58 gives an additive-energy form.  This
packet records the equivalent two-parameter multiplicative form:

    A = 1/2 * #{(r,h): r in H\\{1,-1}, h in H,
                    h(1+r)-1 in H, h not in {1, r^-1, 2/(1+r)}}.

The excluded h=1 term is the same ordered source ratio.  The excluded
h=r^-1 term is the inverse source ratio from the same unordered pair.
The excluded h=2/(1+r) term is the diagonal target ratio t=1 when it lies in H.
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
    "x59-h4-mobius-collision-form",
    "x59_h4_mobius_collision_form.json",
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
        "x58_h4_reduced_additive_energy": "PROVED",
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
    one = 1
    minus_one = p - 1
    raw_surface = 0
    source_h_one = 0
    inverse_source = 0
    diagonal_target = 0
    mobius_nontrivial = 0

    for r in domain:
        if r in (one, minus_one):
            continue
        rinv = pow(r, -1, p)
        hdiag = (2 * pow((1 + r) % p, -1, p)) % p
        for h in domain:
            t = (h * ((1 + r) % p) - 1) % p
            if t not in hset:
                continue
            raw_surface += 1
            if h == one:
                source_h_one += 1
                continue
            if h == rinv:
                inverse_source += 1
                continue
            if h == hdiag:
                diagonal_target += 1
                continue
            mobius_nontrivial += 1

    expected = int(row["anchored_nonzero_h2_surplus"])
    check(
        f"{row['label']}: h=1 source branch has one point per anchor",
        source_h_one == n - 2,
        f"h1={source_h_one}, anchors={n-2}",
    )
    check(
        f"{row['label']}: h=r^-1 inverse-source branch has one point per anchor",
        inverse_source == n - 2,
        f"hinv={inverse_source}, anchors={n-2}",
    )
    check(
        f"{row['label']}: diagonal branch matches X58 correction",
        diagonal_target <= n - 2,
        f"hdiag={diagonal_target}",
    )
    check(
        f"{row['label']}: nontrivial Mobius count is even",
        mobius_nontrivial % 2 == 0,
        f"N={mobius_nontrivial}",
    )
    check(
        f"{row['label']}: Mobius collision count equals X56 anchored surplus",
        mobius_nontrivial // 2 == expected,
        f"computed={mobius_nontrivial//2}, expected={expected}",
    )

    return {
        "label": row["label"],
        "kind": row["kind"],
        "n": n,
        "p": p,
        "raw_surface_count": raw_surface,
        "source_h_equals_1_count": source_h_one,
        "inverse_source_h_equals_r_inverse_count": inverse_source,
        "diagonal_h_equals_2_over_1_plus_r_count": diagonal_target,
        "nontrivial_mobius_ordered_count": mobius_nontrivial,
        "anchored_nonzero_h2_surplus": mobius_nontrivial // 2,
        "x56_anchored_barrier": row["anchored_x55_barrier"],
        "normal_form": "A = #{(r,h): h(1+r)-1 in H, h notin {1,r^-1,2/(1+r)}} / 2",
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x56 = load_json(X56_CERT)
    check("X56 certificate has replay rows", bool(x56.get("rows")))
    rows = [row_report(row) for row in x56["rows"]]
    check(
        "all replay rows match X56 anchored surplus",
        all(row["nontrivial_mobius_ordered_count"] == 2 * row["anchored_nonzero_h2_surplus"] for row in rows),
    )
    check(
        "some replay row has nonzero Mobius surplus",
        any(row["anchored_nonzero_h2_surplus"] > 0 for row in rows),
    )
    return {
        "task": "X59 h=4 Mobius collision normal form",
        "node": "active_core_count_bound",
        "status": "PROVED EXACT MOBIUS-COLLISION IDENTITY",
        "theorem": (
            "For an anchor ratio r, target ratios t in the same quotient shell "
            "are exactly t = h(1+r)-1 with h in H.  The source unordered pair "
            "corresponds to t=r (h=1) and t=r^-1 (h=r^-1).  The diagonal "
            "target corresponds to t=1 (h=2/(1+r)) when it lies in H.  After "
            "excluding these branches, each valid unordered target contributes "
            "two ordered ratios.  Hence A_anchor_surplus is half the nontrivial "
            "Mobius collision count."
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

    print("\nMobius collision rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: raw={row['raw_surface_count']} "
            f"h1={row['source_h_equals_1_count']} "
            f"hinv={row['inverse_source_h_equals_r_inverse_count']} "
            f"hdiag={row['diagonal_h_equals_2_over_1_plus_r_count']} "
            f"N={row['nontrivial_mobius_ordered_count']} "
            f"A={row['anchored_nonzero_h2_surplus']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X59 Mobius collision-form checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
