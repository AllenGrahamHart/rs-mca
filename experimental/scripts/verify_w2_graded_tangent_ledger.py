#!/usr/bin/env python3
"""Verifier for the W2 graded tangent ledger design.

This is an arithmetic/design verifier, not a proof of the final ledger bound.
It checks the cell partition forced by the proved 2b map:

  A = k+t, r = k+d, s = A-r = t-d.

Partial-forcing cells have 1 <= d <= t-2, equivalently 2 <= s <= t-1.
The cascade boundary is d >= t-1, and d=0 is the rank/spread boundary.

It also checks the heavy-triangle boundary combinatorics: if
r12+r13+r23-trip > 2k and no pair has r_ij >= k+1, then at least two pairwise
overlaps are deep links (> k/2), so the generic heavy case is rationed by the
deep-link staircase rather than by a new fourth object.

Stdlib only.
Run: python3 experimental/scripts/verify_w2_graded_tangent_ledger.py
To refresh the pinned certificate:
  python3 experimental/scripts/verify_w2_graded_tangent_ledger.py --write-certificate
"""

from __future__ import annotations

import json
import os
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "w2-graded-tangent-ledger",
    "w2_graded_tangent_ledger.json",
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


def quiet_check(name: str, cond: bool, detail: str = "") -> None:
    global NCHECK
    NCHECK += 1
    if not cond:
        line = name
        if detail:
            line += f" ({detail})"
        FAILS.append(line)


def cell_table(k: int, t: int) -> dict:
    A = k + t
    partial = []
    for d in range(1, max(t - 1, 1)):
        if d > t - 2:
            continue
        r = k + d
        s = A - r
        partial.append(
            {
                "d": d,
                "r": r,
                "s": s,
                "qx13_fresh_codim": s,
                "identity": d + s,
            }
        )
    for cell in partial:
        check(
            f"t={t} depth d={cell['d']} lies in partial band",
            1 <= cell["d"] <= t - 2 and k + 1 <= cell["r"] <= A - 2,
            f"r={cell['r']}, A={A}",
        )
        check(
            f"t={t} depth d={cell['d']} has d+s=t",
            cell["identity"] == t and 2 <= cell["s"] <= t - 1,
            f"s={cell['s']}",
        )
    check(
        f"t={t} partial cell count",
        len(partial) == max(0, t - 2),
        f"cells={len(partial)}, expected={max(0, t - 2)}",
    )
    return {
        "k": k,
        "t": t,
        "A": A,
        "partial_depths": partial,
        "residual_boundary": {"d": 0, "r": k, "s": t},
        "cascade_boundary": {"d_min": max(t - 1, 0), "r_min": A - 1, "s_max": 1},
    }


def heavy_triangle_summary(k_max: int = 18) -> dict:
    checked = 0
    heavy = 0
    direct_2b = 0
    deep_link_only = 0
    worst_margin = 0
    for k in range(2, k_max + 1):
        for r12 in range(k + 3):
            for r13 in range(k + 3):
                for r23 in range(k + 3):
                    for trip in range(min(r12, r13, r23) + 1):
                        checked += 1
                        budget = r12 + r13 + r23 - trip
                        if budget <= 2 * k:
                            continue
                        heavy += 1
                        overlaps = sorted((r12, r13, r23), reverse=True)
                        if overlaps[0] >= k + 1:
                            direct_2b += 1
                            continue
                        deep_links = sum(2 * r > k for r in overlaps)
                        margin = budget - 2 * k
                        worst_margin = max(worst_margin, margin)
                        quiet_check(
                            f"k={k} heavy triangle without 2b has two deep links",
                            deep_links >= 2,
                            f"overlaps={overlaps}, trip={trip}, budget={budget}",
                        )
                        deep_link_only += 1
    return {
        "k_max": k_max,
        "profiles_checked": checked,
        "heavy_profiles": heavy,
        "direct_2b_profiles": direct_2b,
        "deep_link_only_profiles": deep_link_only,
        "max_budget_margin_seen": worst_margin,
    }


def main() -> None:
    tables = [cell_table(k=8, t=t) for t in range(1, 9)]
    heavy = heavy_triangle_summary()
    result = {
        "node": "xr_partial_tangent_band / xr_heavy_triangle_charge",
        "task": "W2",
        "checks": NCHECK,
        "cell_tables": tables,
        "heavy_triangle_boundary": heavy,
        "status": "design arithmetic only; no status promotion",
    }

    if "--write-certificate" in sys.argv:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w") as fh:
            json.dump(result, fh, indent=2, sort_keys=True)
            fh.write("\n")

    expected = None
    if os.path.exists(CERT):
        with open(CERT) as fh:
            expected = json.load(fh)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", result == expected)

    if FAILS:
        print("\nrecomputed summary:")
        print(json.dumps(result, indent=2, sort_keys=True))
        print("\nFAIL:")
        for name in FAILS[:25]:
            print("  -", name)
        if len(FAILS) > 25:
            print(f"  ... {len(FAILS) - 25} more")
        sys.exit(1)

    print("\nsummary:")
    print(json.dumps(result, indent=2, sort_keys=True))
    print(f"\nPASS: {NCHECK} W2 graded tangent ledger checks")


if __name__ == "__main__":
    main()
