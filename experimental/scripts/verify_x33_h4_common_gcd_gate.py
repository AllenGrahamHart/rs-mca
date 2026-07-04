#!/usr/bin/env python3
"""X33 h=4 common-gcd gate.

X32 leaves one h=4 obstruction: non-antipodal top-level sparse norm gates.
This verifier packages the exact row-checker for that branch.

For a fixed exponent pattern P,Q, form the three elementary-difference
polynomials E_1,E_2,E_3 in Z[X]/(X^n-1).  At a row p == 1 mod n, the pattern
or one of its Galois scalings is an h=4 top-three trade iff

    gcd(Phi_n, E_1, E_2, E_3) in F_p[X]

has positive degree.

The proof note records the equivalence.  The finite part below shows that in
two small boundary rows, many top-level first-sum norm gates exist, but the
full common-gcd gate kills all non-antipodal h=4 candidates.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
import json
import os
import sys
from typing import Any

import verify_h1_u1_toy_harness as h1
import verify_x20_h4_cyclic_fingerprint as x20
import verify_x30_finite_p_norm_gate as x30


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x33-h4-common-gcd-gate",
    "x33_h4_common_gcd_gate.json",
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


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_divmod_mod(a: list[int], b: list[int], p: int) -> tuple[list[int], list[int]]:
    a = trim([x % p for x in a[:]])
    b = trim([x % p for x in b[:]])
    if b == [0]:
        raise ZeroDivisionError("polynomial division by zero")
    if len(a) < len(b):
        return [0], a
    q = [0] * (len(a) - len(b) + 1)
    inv_lc = pow(b[-1], -1, p)
    while len(a) >= len(b) and a != [0]:
        shift = len(a) - len(b)
        factor = a[-1] * inv_lc % p
        q[shift] = factor
        if factor:
            for i, coeff in enumerate(b):
                a[shift + i] = (a[shift + i] - factor * coeff) % p
        trim(a)
    return trim(q), trim(a)


def poly_gcd_mod(a: list[int], b: list[int], p: int) -> list[int]:
    a = trim([x % p for x in a[:]])
    b = trim([x % p for x in b[:]])
    while b != [0]:
        _, r = poly_divmod_mod(a, b, p)
        a, b = b, r
    if a == [0]:
        return [0]
    inv_lc = pow(a[-1], -1, p)
    return trim([(x * inv_lc) % p for x in a])


def cyclotomic_2power_mod(n: int) -> list[int]:
    assert n > 1 and n & (n - 1) == 0
    return [1] + [0] * (n // 2 - 1) + [1]


def elementary_diff_poly(n: int, p_set: tuple[int, ...], q_set: tuple[int, ...], r: int, p: int) -> list[int]:
    coeffs = [0] * n
    for support, sign in ((p_set, 1), (q_set, -1)):
        for combo in combinations(support, r):
            coeffs[sum(combo) % n] = (coeffs[sum(combo) % n] + sign) % p
    return trim(coeffs)


def common_h4_gcd_degree(n: int, p: int, p_set: tuple[int, ...], q_set: tuple[int, ...]) -> int:
    common = cyclotomic_2power_mod(n)
    for r in (1, 2, 3):
        common = poly_gcd_mod(common, elementary_diff_poly(n, p_set, q_set, r, p), p)
    return len(common) - 1


def h4_signature(domain: list[int], p: int, support: tuple[int, ...]) -> tuple[int, int, int]:
    e = [0, 0, 0, 0]
    e[0] = 1
    for i in support:
        x = domain[i]
        for r in range(3, 0, -1):
            e[r] = (e[r] + x * e[r - 1]) % p
    return e[1], e[2], e[3]


def support_mask(support: tuple[int, ...]) -> int:
    out = 0
    for i in support:
        out |= 1 << i
    return out


def degree_histogram_for_row(n: int, p: int) -> dict[str, Any]:
    domain = h1.mu_domain(p, n)
    e1_groups: dict[int, list[tuple[int, tuple[int, ...], tuple[int, int, int]]]] = defaultdict(list)
    for support in combinations(range(n), 4):
        sig = h4_signature(domain, p, support)
        e1_groups[sig[0]].append((support_mask(support), support, sig))

    counts = Counter()
    top_gcd_degree_histogram = Counter()
    examples: dict[str, list[dict[str, Any]]] = {"top_level_first_sum": [], "top_three_paid": []}

    for group in e1_groups.values():
        for p_mask, p_set, p_sig in group:
            if not (p_mask & 1):
                continue
            for q_mask, q_set, q_sig in group:
                if p_mask == q_mask or (p_mask & q_mask):
                    continue
                counts["anchored_e1_pairs"] += 1
                descended = x30.divisible_by_phi_power_two(x30.coeff_word(n, p_set, q_set))
                if descended:
                    counts["antipodal_e1_pairs"] += 1
                else:
                    counts["top_level_e1_pairs"] += 1
                    degree = common_h4_gcd_degree(n, p, p_set, q_set)
                    top_gcd_degree_histogram[degree] += 1
                    if len(examples["top_level_first_sum"]) < 4:
                        examples["top_level_first_sum"].append(
                            {
                                "P": list(p_set),
                                "Q": list(q_set),
                                "common_h4_gcd_degree": degree,
                                "same_top_three_at_chosen_generator": p_sig == q_sig,
                            }
                        )

                if p_sig == q_sig:
                    counts["anchored_top_three_pairs"] += 1
                    kind = x20.classify_pair(p_mask, q_mask, n, domain, p)
                    counts[f"top_three_{kind}"] += 1
                    if len(examples["top_three_paid"]) < 4:
                        examples["top_three_paid"].append(
                            {
                                "P": list(p_set),
                                "Q": list(q_set),
                                "classification": kind,
                                "descended": descended,
                                "common_h4_gcd_degree": common_h4_gcd_degree(n, p, p_set, q_set),
                            }
                        )

    check(f"n={n}, p={p}: top-level first-sum candidates exist", counts["top_level_e1_pairs"] > 0)
    check(
        f"n={n}, p={p}: no top-level h=4 common-gcd survivors",
        top_gcd_degree_histogram and set(top_gcd_degree_histogram) == {0},
        dict(top_gcd_degree_histogram),
    )
    check(
        f"n={n}, p={p}: every top-three pair is paid mu4 baseline",
        counts["anchored_top_three_pairs"] == counts["top_three_mu4_full_fiber"],
        dict(counts),
    )
    return {
        "n": n,
        "p": p,
        "subset_count": sum(len(group) for group in e1_groups.values()),
        "e1_group_count": len(e1_groups),
        "max_e1_group_size": max(len(group) for group in e1_groups.values()),
        "counts": dict(sorted(counts.items())),
        "top_level_common_gcd_degree_histogram": {str(k): v for k, v in sorted(top_gcd_degree_histogram.items())},
        "examples": examples,
    }


def check_gcd_criterion_examples() -> dict[str, Any]:
    rows = [
        {
            "name": "mu4 baseline",
            "n": 32,
            "p": 4993,
            "P": (0, 8, 16, 24),
            "Q": (1, 9, 17, 25),
            "expected_positive_degree": True,
        },
        {
            "name": "top-level first-sum only",
            "n": 32,
            "p": 4993,
            "P": (0, 1, 2, 17),
            "Q": (3, 8, 19, 21),
            "expected_positive_degree": False,
        },
    ]
    out = []
    for row in rows:
        degree = common_h4_gcd_degree(row["n"], row["p"], row["P"], row["Q"])
        positive = degree > 0
        check(
            f"{row['name']}: common h4 gcd degree has expected sign",
            positive == row["expected_positive_degree"],
            f"degree={degree}",
        )
        item = dict(row)
        item["P"] = list(row["P"])
        item["Q"] = list(row["Q"])
        item["common_h4_gcd_degree"] = degree
        out.append(item)
    return {"examples": out}


def check_dependency_nodes() -> dict[str, str]:
    dag = load_json(DAG)
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    needed = {
        "x32_h4_terminal_dichotomy": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        check(f"DAG node {node} has expected status", statuses.get(node) == expected, statuses.get(node, "missing"))
    return {node: statuses.get(node, "missing") for node in needed}


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    criterion = check_gcd_criterion_examples()
    rows = [
        degree_histogram_for_row(16, 257),
        degree_histogram_for_row(32, 4993),
    ]
    check("representative rows have no top-level h=4 gcd survivors", all(row["top_level_common_gcd_degree_histogram"] == {"0": row["counts"]["top_level_e1_pairs"]} for row in rows))
    return {
        "task": "X33 h=4 common-gcd gate",
        "node": "active_core_count_bound",
        "status": (
            "PROVED CHECKER + FINITE EVIDENCE: h=4 top-level candidates are "
            "exactly common-gcd survivors; representative boundary rows have "
            "many first-sum norm gates but zero top-level h=4 survivors"
        ),
        "theorem": (
            "For a fixed h=4 exponent pattern P,Q and row p == 1 mod n, "
            "some Galois scaling of the pattern is a top-three h=4 trade iff "
            "gcd(Phi_n,E1,E2,E3) has positive degree in F_p[X], where Er is "
            "the r-th elementary-difference polynomial reduced modulo X^n-1. "
            "Degree zero rules out the pattern and all its Galois scalings."
        ),
        "dependency_statuses": deps,
        "criterion_examples": criterion,
        "row_census": rows,
        "open_residue": (
            "Run or prove this common-gcd exclusion for official h=4 rows, or "
            "count positive-degree top-level survivors as a norm-gate column."
        ),
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

    print("\nrow census:")
    for row in cert["row_census"]:
        print(
            f"n={row['n']:<3d} p={row['p']:<6d} "
            f"top-level-e1={row['counts']['top_level_e1_pairs']:<6d} "
            f"top-three={row['counts']['anchored_top_three_pairs']:<4d} "
            f"gcd={row['top_level_common_gcd_degree_histogram']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X33 h=4 common-gcd checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
