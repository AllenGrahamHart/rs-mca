#!/usr/bin/env python3
"""X80 odd-support free scaling orbits.

On a 2-power multiplicative domain, any odd-cardinality support has trivial
cyclic scaling stabilizer.  For h=5 this gives a clean anchored-to-row
conversion for ordered pairs and classifies the only possible unordered
stabilizer as the antipodal swap.
"""

from __future__ import annotations

from itertools import combinations
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
    "x80-odd-support-free-orbits",
    "x80_odd_support_free_orbits.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")

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
        "x78_h5_square_shift_supports": "PROVED",
        "x79_h5_obstruction_norm_gate": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def mask_from_tuple(values: tuple[int, ...]) -> int:
    out = 0
    for value in values:
        out |= 1 << value
    return out


def shift_mask(mask: int, n: int, shift: int) -> int:
    out = 0
    for i in range(n):
        if (mask >> i) & 1:
            out |= 1 << ((i + shift) % n)
    return out


def support_stabilizer(mask: int, n: int) -> list[int]:
    return [shift for shift in range(n) if shift_mask(mask, n, shift) == mask]


def ordered_pair_stabilizer(p_mask: int, q_mask: int, n: int) -> list[int]:
    return [
        shift
        for shift in range(n)
        if shift_mask(p_mask, n, shift) == p_mask and shift_mask(q_mask, n, shift) == q_mask
    ]


def unordered_pair_stabilizer(p_mask: int, q_mask: int, n: int) -> list[int]:
    return [
        shift
        for shift in range(n)
        if (
            shift_mask(p_mask, n, shift) == p_mask
            and shift_mask(q_mask, n, shift) == q_mask
        )
        or (
            shift_mask(p_mask, n, shift) == q_mask
            and shift_mask(q_mask, n, shift) == p_mask
        )
    ]


def exps(mask: int, n: int) -> list[int]:
    return [i for i in range(n) if (mask >> i) & 1]


def check_odd_support_rows() -> list[dict[str, Any]]:
    rows = []
    for n, h in [(16, 1), (16, 3), (16, 5), (32, 3), (32, 5)]:
        max_stabilizer = 0
        bad: list[list[int]] = []
        subset_count = 0
        for subset in combinations(range(n), h):
            subset_count += 1
            mask = mask_from_tuple(subset)
            stab = support_stabilizer(mask, n)
            max_stabilizer = max(max_stabilizer, len(stab))
            if stab != [0] and len(bad) < 5:
                bad.append(list(subset))
        check(
            f"n={n}, h={h}: every odd support has trivial cyclic stabilizer",
            not bad and max_stabilizer == 1,
            f"subsets={subset_count}, max_stabilizer={max_stabilizer}",
        )
        rows.append(
            {
                "n": n,
                "h": h,
                "subset_count": subset_count,
                "max_stabilizer_size": max_stabilizer,
                "bad_examples": bad,
            }
        )
    return rows


def pair_symmetry_checks() -> dict[str, Any]:
    n = 16
    p_mask = mask_from_tuple((0, 1, 2, 3, 4))
    q_mask = shift_mask(p_mask, n, n // 2)
    non_swap_q = mask_from_tuple((5, 6, 7, 8, 9))

    ordered_swap_stab = ordered_pair_stabilizer(p_mask, q_mask, n)
    unordered_swap_stab = unordered_pair_stabilizer(p_mask, q_mask, n)
    unordered_generic_stab = unordered_pair_stabilizer(p_mask, non_swap_q, n)

    check("antipodal h5 pair has trivial ordered stabilizer", ordered_swap_stab == [0])
    check("antipodal h5 pair has unordered stabilizer {0,n/2}", unordered_swap_stab == [0, n // 2])
    check("generic disjoint h5 pair has trivial unordered stabilizer", unordered_generic_stab == [0])

    return {
        "n": n,
        "P": exps(p_mask, n),
        "antipodal_Q": exps(q_mask, n),
        "generic_Q": exps(non_swap_q, n),
        "ordered_antipodal_stabilizer": ordered_swap_stab,
        "unordered_antipodal_stabilizer": unordered_swap_stab,
        "unordered_generic_stabilizer": unordered_generic_stab,
    }


def anchored_conversion_rows() -> list[dict[str, Any]]:
    rows = []
    for n, h in [(16, 5), (32, 5), (64, 5)]:
        full_ordered = math.comb(n, h) * math.comb(n - h, h)
        anchored = math.comb(n - 1, h - 1) * math.comb(n - h, h)
        check(
            f"n={n}, h={h}: full ordered count equals (n/h)*anchored count",
            h * full_ordered == n * anchored,
            f"full={full_ordered}, anchored={anchored}",
        )
        rows.append(
            {
                "n": n,
                "h": h,
                "full_ordered_disjoint_pairs": full_ordered,
                "anchored_ordered_disjoint_pairs": anchored,
                "orbit_size": n,
                "anchored_representatives_per_orbit": h,
                "identity_h_full_equals_n_anchored": h * full_ordered == n * anchored,
            }
        )
    return rows


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    support_rows = check_odd_support_rows()
    pair_checks = pair_symmetry_checks()
    conversion_rows = anchored_conversion_rows()

    check(
        "all checked odd supports have stabilizer one",
        all(row["max_stabilizer_size"] == 1 and not row["bad_examples"] for row in support_rows),
    )
    check(
        "all h5 anchored conversion rows satisfy exact identity",
        all(row["identity_h_full_equals_n_anchored"] for row in conversion_rows),
    )

    return {
        "task": "X80 odd-support free scaling orbits",
        "node": "active_core_count_bound",
        "status": "PROVED H5 ORBIT BOOKKEEPING: ORDERED ODD-SUPPORT PAIRS HAVE FREE SCALING ORBITS",
        "theorem": (
            "If n is a power of two and A is an odd-cardinality subset of "
            "mu_n, then the multiplicative stabilizer of A inside mu_n is "
            "trivial.  Hence ordered h=5 pairs have free scaling orbits.  "
            "Each free ordered-pair orbit has n members and exactly h anchored "
            "representatives with 1 in the first support, so full ordered row "
            "count equals (n/h) times anchored count.  For unordered h=5 pairs, "
            "the only possible nontrivial stabilizer is the antipodal swap "
            "P <-> -P."
        ),
        "dependency_statuses": deps,
        "support_rows": support_rows,
        "pair_symmetry_checks": pair_checks,
        "anchored_conversion_rows": conversion_rows,
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

    print("\nodd-support free-orbit rows:")
    for row in cert["anchored_conversion_rows"]:
        print(
            f"n={row['n']}, h={row['h']}: full={row['full_ordered_disjoint_pairs']} "
            f"anchored={row['anchored_ordered_disjoint_pairs']}"
        )

    if FAILS:
        print(f"\nFAIL: {len(FAILS)} checks failed: {FAILS}", file=sys.stderr)
        return 1
    print(f"\nPASS: {NCHECK} X80 odd-support free-orbit checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
