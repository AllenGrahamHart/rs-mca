#!/usr/bin/env python3
"""X41 h=4 centered shell norm-gate localization.

X40 reduced the centered affine h=4 residue to pair-product collisions inside
fixed nonzero pair-sum shells.  This packet proves the shell itself is
p-specific: over characteristic-zero roots of unity, a nonzero pair sum
determines the unordered pair.  Therefore every finite-field nonzero shell
with two distinct pairs is a sparse h=2 cyclotomic norm gate.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations
import json
import os
import sys
from typing import Any

import verify_h1_u1_toy_harness as h1
import verify_x30_finite_p_norm_gate as x30
import verify_x31_h2_quotient_norm_criterion as x31


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x41-h4-centered-norm-gate",
    "x41_h4_centered_norm_gate.json",
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
        "x40_h4_centered_pair_shell_reduction": "PROVED",
        "x31_h2_quotient_norm_criterion": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def pair_sum(domain: list[int], p: int, pair: tuple[int, int]) -> int:
    return (domain[pair[0]] + domain[pair[1]]) % p


def first_nonzero_shell_collision(n: int, p: int) -> tuple[int, tuple[int, int], tuple[int, int]] | None:
    domain = h1.mu_domain(p, n)
    shells: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for pair in combinations(range(n), 2):
        shells[pair_sum(domain, p, pair)].append(pair)
    for s, pairs in shells.items():
        if s == 0 or len(pairs) < 2:
            continue
        for left, right in combinations(pairs, 2):
            if set(left).isdisjoint(right):
                return s, left, right
    return None


def check_nonzero_shell_norm_gate(n: int, p: int) -> dict[str, Any]:
    found = first_nonzero_shell_collision(n, p)
    check(f"n={n}, p={p}: nonzero pair shell with two disjoint pairs exists", found is not None)
    if found is None:
        return {"n": n, "p": p, "found": False}

    s, left, right = found
    coeffs = x30.coeff_word(n, left, right)
    phi_descended = x30.divisible_by_phi_power_two(coeffs)
    resultant = x31.sparse_resultant(n, left, right)
    valuation = x31.p_adic_valuation(resultant, p)
    check(f"n={n}, p={p}: selected pair shell is nonzero", s != 0, f"s={s}")
    check(f"n={n}, p={p}: nonzero shell word is not Phi_n-descended", not phi_descended)
    check(
        f"n={n}, p={p}: nonzero shell word is p-norm-gated",
        resultant % p == 0 and valuation > 0,
        f"res={resultant}, v_p={valuation}",
    )
    return {
        "n": n,
        "p": p,
        "found": True,
        "sum_s": s,
        "left_pair": list(left),
        "right_pair": list(right),
        "phi_descended": phi_descended,
        "resultant": resultant,
        "resultant_abs_bits": abs(resultant).bit_length(),
        "p_adic_valuation": valuation,
    }


def check_zero_sum_baseline(n: int, p: int, b: int) -> dict[str, Any]:
    left = (0, n // 2)
    right = (b, b + n // 2)
    domain = h1.mu_domain(p, n)
    s_left = pair_sum(domain, p, left)
    s_right = pair_sum(domain, p, right)
    coeffs = x30.coeff_word(n, left, right)
    descended = x30.divisible_by_phi_power_two(coeffs)
    check(f"n={n}, p={p}: zero shell sums vanish", s_left == 0 and s_right == 0)
    check(f"n={n}, p={p}: zero shell is Phi_n-descended", descended)
    return {
        "n": n,
        "p": p,
        "left_pair": list(left),
        "right_pair": list(right),
        "left_sum": s_left,
        "right_sum": s_right,
        "phi_descended": descended,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    zero_rows = [
        check_zero_sum_baseline(16, 17, 1),
        check_zero_sum_baseline(64, 193, 5),
        check_zero_sum_baseline(128, 17921, 7),
    ]
    norm_rows = [
        check_nonzero_shell_norm_gate(16, 17),
        check_nonzero_shell_norm_gate(64, 193),
        check_nonzero_shell_norm_gate(64, 257),
        check_nonzero_shell_norm_gate(32, 1153),
        check_nonzero_shell_norm_gate(128, 17921),
    ]
    check("all zero-shell examples are descended", all(row["phi_descended"] for row in zero_rows))
    check(
        "all selected nonzero-shell collisions are non-descended norm gates",
        all(row.get("found") and not row["phi_descended"] and row["p_adic_valuation"] > 0 for row in norm_rows),
    )
    return {
        "task": "X41 h=4 centered norm-gate localization",
        "node": "active_core_count_bound",
        "status": "PROVED LOCALIZATION: nonzero centered pair shells are p-specific h=2 norm gates",
        "theorem": (
            "Over characteristic-zero roots of unity, two unordered pairs with "
            "the same nonzero sum are equal: conjugating x+y=u+v=s gives "
            "x^-1+y^-1=u^-1+v^-1, hence s/(xy)=s/(uv), so xy=uv and the "
            "pairs have the same sum and product.  Therefore a finite-field "
            "nonzero pair-sum collision cannot be Phi_n-descended; by X30/X31 "
            "its sparse 2+2 word has p dividing Res(Phi_n,f).  The centered "
            "affine h=4 residue from X40 is consequently p-specific norm-gate "
            "mass at the pair-shell level."
        ),
        "dependency_statuses": deps,
        "zero_sum_baseline_examples": zero_rows,
        "nonzero_norm_gate_examples": norm_rows,
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

    print("\nnonzero norm-gate examples:")
    for row in cert["nonzero_norm_gate_examples"]:
        print(
            f"n={row['n']:<4d} p={row['p']:<8d} s={row['sum_s']:<8d} "
            f"pairs={row['left_pair']}/{row['right_pair']} v_p={row['p_adic_valuation']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X41 centered norm-gate checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
