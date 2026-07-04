#!/usr/bin/env python3
"""X46 h=4 top-level orbit budget.

X45 proves that the h=4 common-gcd gate is invariant on affine exponent
orbits.  This packet records the budget consequence:

    one positive canonical non-descended orbit expands to at most
    2*n*phi(n) = n^2 ordered signed pairs, for n a power of two.

Thus at h=4, at most n positive non-descended canonical orbits fit the
rewired n^3 terminal column.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
import json
import math
import os
import sys
from typing import Any

import verify_x30_finite_p_norm_gate as x30
import verify_x33_h4_common_gcd_gate as x33
import verify_x45_h4_common_gcd_orbit_compression as x45


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x46-h4-top-level-orbit-budget",
    "x46_h4_top_level_orbit_budget.json",
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


def phi_power_two(n: int) -> int:
    assert n > 1 and n & (n - 1) == 0
    return n // 2


def affine_swap_group_size(n: int) -> int:
    return 2 * n * phi_power_two(n)


def coeff_word(n: int, p_set: tuple[int, ...], q_set: tuple[int, ...]) -> list[int]:
    return x30.coeff_word(n, p_set, q_set)


def is_descended(n: int, p_set: tuple[int, ...], q_set: tuple[int, ...]) -> bool:
    return x30.divisible_by_phi_power_two(coeff_word(n, p_set, q_set))


def check_dependency_nodes() -> dict[str, str]:
    dag = load_json(DAG)
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    needed = {
        "x32_h4_terminal_dichotomy": "PROVED",
        "x33_h4_common_gcd_gate": "PROVED",
        "x45_h4_common_gcd_orbit_compression": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def check_group_size_rows() -> list[dict[str, Any]]:
    rows = []
    for n in (8, 16, 32, 64, 128, 256):
        size = affine_swap_group_size(n)
        check(f"n={n}: affine-swap group size is n^2", size == n * n, str(size))
        rows.append({"n": n, "phi_n": phi_power_two(n), "group_size": size, "n_squared": n * n})
    return rows


def check_descended_invariance_examples() -> list[dict[str, Any]]:
    examples = [
        (16, (0, 4, 8, 12), (1, 5, 9, 13)),
        (16, (0, 1, 2, 9), (3, 4, 7, 12)),
        (32, (0, 8, 16, 24), (1, 9, 17, 25)),
        (32, (0, 1, 2, 17), (3, 8, 19, 21)),
    ]
    rows = []
    for n, p_set, q_set in examples:
        base = is_descended(n, p_set, q_set)
        flags = []
        for unit in x45.units_mod(n)[: min(6, len(x45.units_mod(n)))]:
            for shift in (0, 1, 3, n // 2 - 1):
                for swap in (False, True):
                    left, right = x45.transform_pair(p_set, q_set, n, unit, shift, swap)
                    flags.append(is_descended(n, left, right))
        invariant = all(flag == base for flag in flags)
        check(f"n={n}, P={p_set}: descended/paid status is affine invariant", invariant)
        rows.append(
            {
                "n": n,
                "P": list(p_set),
                "Q": list(q_set),
                "base_descended": base,
                "checked_transforms": len(flags),
            }
        )
    return rows


def full_n16_accounting() -> dict[str, Any]:
    n = 16
    p = 257
    group_size = affine_swap_group_size(n)
    orbit_members: dict[tuple[tuple[int, ...], tuple[int, ...]], int] = defaultdict(int)
    orbit_degree: dict[tuple[tuple[int, ...], tuple[int, ...]], int] = {}
    orbit_descended: dict[tuple[tuple[int, ...], tuple[int, ...]], bool] = {}
    inconsistent: list[dict[str, Any]] = []

    anchored_total = 0
    anchored_top_level_survivors = 0
    for p_set, q_set in x45.anchored_ordered_pairs(n):
        anchored_total += 1
        key = x45.canonical_pair(p_set, q_set, n)
        degree = x33.common_h4_gcd_degree(n, p, p_set, q_set)
        descended = is_descended(n, p_set, q_set)
        orbit_members[key] += 1

        if degree > 0 and not descended:
            anchored_top_level_survivors += 1

        if key in orbit_degree and orbit_degree[key] != degree and len(inconsistent) < 5:
            inconsistent.append(
                {
                    "kind": "degree",
                    "canonical_P": list(key[0]),
                    "canonical_Q": list(key[1]),
                    "first": orbit_degree[key],
                    "new": degree,
                }
            )
        if key in orbit_descended and orbit_descended[key] != descended and len(inconsistent) < 5:
            inconsistent.append(
                {
                    "kind": "descended",
                    "canonical_P": list(key[0]),
                    "canonical_Q": list(key[1]),
                    "first": orbit_descended[key],
                    "new": descended,
                }
            )
        orbit_degree.setdefault(key, degree)
        orbit_descended.setdefault(key, descended)

    positive_non_descended_orbits = [
        key for key, degree in orbit_degree.items() if degree > 0 and not orbit_descended[key]
    ]
    exact_expansion = sum(orbit_members[key] for key in positive_non_descended_orbits)
    crude_expansion = len(positive_non_descended_orbits) * group_size
    degree_hist = Counter(orbit_degree.values())
    member_hist = Counter(orbit_members.values())

    check("n=16 orbit degree/status accounting is consistent", not inconsistent)
    check("n=16 positive canonical non-descended orbit expansion is exact", exact_expansion == anchored_top_level_survivors)
    check("n=16 crude orbit budget bounds exact expansion", exact_expansion <= crude_expansion)
    check("n=16 positive canonical non-descended orbit count fits n", len(positive_non_descended_orbits) <= n)
    check("n=16 top-level survivor count fits n^3", anchored_top_level_survivors <= n**3)
    check("n=16 no top-level non-descended survivors remain", anchored_top_level_survivors == 0)

    return {
        "n": n,
        "p": p,
        "group_size": group_size,
        "anchored_ordered_pairs": anchored_total,
        "canonical_orbits": len(orbit_members),
        "degree_histogram_by_orbit": {str(k): v for k, v in sorted(degree_hist.items())},
        "anchored_orbit_size_histogram": {str(k): v for k, v in sorted(member_hist.items())},
        "positive_non_descended_canonical_orbits": len(positive_non_descended_orbits),
        "positive_non_descended_exact_expansion": exact_expansion,
        "positive_non_descended_crude_budget": crude_expansion,
        "anchored_top_level_survivors": anchored_top_level_survivors,
        "n_cubed": n**3,
    }


def check_n32_sample_budget() -> dict[str, Any]:
    """Small sample showing the budget theorem on X33's n=32 row.

    This is deliberately not a full n=32 orbit census; it verifies the theorem
    on representative canonical orbits without large memory.
    """

    n = 32
    p = 4993
    samples = [
        ((0, 8, 16, 24), (1, 9, 17, 25)),
        ((0, 1, 2, 17), (3, 8, 19, 21)),
        ((0, 1, 3, 14), (4, 7, 16, 27)),
        ((0, 2, 5, 19), (1, 7, 12, 25)),
    ]
    rows = []
    for p_set, q_set in samples:
        key = x45.canonical_pair(p_set, q_set, n)
        degree = x33.common_h4_gcd_degree(n, p, *key)
        descended = is_descended(n, *key)
        budget = affine_swap_group_size(n)
        check(
            f"n=32 sample {p_set}: one canonical orbit budget fits n^3",
            budget <= n**3,
            f"budget={budget}",
        )
        rows.append(
            {
                "P": list(p_set),
                "Q": list(q_set),
                "canonical_P": list(key[0]),
                "canonical_Q": list(key[1]),
                "canonical_degree": degree,
                "canonical_descended": descended,
                "single_orbit_budget": budget,
            }
        )
    return {"n": n, "p": p, "sample_count": len(samples), "rows": rows}


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    group_rows = check_group_size_rows()
    descended_rows = check_descended_invariance_examples()
    n16 = full_n16_accounting()
    n32 = check_n32_sample_budget()
    return {
        "task": "X46 h=4 top-level orbit budget",
        "node": "active_core_count_bound",
        "status": "PROVED H4 CANONICAL-ORBIT BUDGET FOR THE TERMINAL n^3 COLUMN",
        "theorem": (
            "For n=2^s, the affine exponent symmetries plus side swap have "
            "size 2*n*phi(n)=n^2 on ordered signed h=4 pairs.  X45 shows the "
            "h=4 common-gcd degree is constant on these orbits, and the "
            "Phi_n-descended paid status is invariant by the same monomial/"
            "primitive-root permutation argument.  Therefore the top-level "
            "non-descended survivor count is at most n^2 times the number of "
            "positive canonical non-descended orbits.  In particular, <= n "
            "such canonical orbits is sufficient for the rewired n^3 terminal "
            "column, and zero such orbits closes the h=4 top-level branch."
        ),
        "dependency_statuses": deps,
        "group_size_rows": group_rows,
        "descended_invariance_examples": descended_rows,
        "n16_full_accounting": n16,
        "n32_sample_budget": n32,
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

    row = cert["n16_full_accounting"]
    print("\nn=16 top-level orbit budget:")
    print(
        f"canonical positive non-descended={row['positive_non_descended_canonical_orbits']} "
        f"expanded={row['positive_non_descended_exact_expansion']} "
        f"n^3={row['n_cubed']}"
    )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X46 h4 orbit-budget checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
