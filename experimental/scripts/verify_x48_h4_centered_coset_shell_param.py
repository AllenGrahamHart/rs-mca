#!/usr/bin/env python3
"""X48 h=4 centered pair-sum shells as quotient-coset counts.

X44 reduces the centered affine h=4 branch to the maximum nonzero pair-sum
shell size

    m_s = #{{x,y} subset H : x+y=s},  s != 0.

This packet proves the quotient-coset parametrization

    m_s = 1/2 * #{ r in H \\ {1} : 1+r in sH }.

In particular, m_s depends only on the multiplicative coset sH, so X44's
single row statistic is a maximum shifted-subgroup intersection over
F_p^*/H.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import combinations
import json
import os
import sys
from typing import Any

import verify_h1_u1_toy_harness as h1
import verify_x12_h3_active_core_census as h3


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x48-h4-centered-coset-shell-param",
    "x48_h4_centered_coset_shell_param.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")

FAILS: list[str] = []
NCHECK = 0


@dataclass(frozen=True)
class Row:
    label: str
    n: int
    p: int
    kind: str


ROWS = (
    Row("low_n16_p17", 16, 17, "low_characteristic_stress"),
    Row("low_n64_p193", 64, 193, "low_characteristic_stress"),
    Row("boundary_n64_p7937", 64, 7937, "boundary_x43_fails_x44_closes"),
    Row("boundary_n128_p17921", 128, 17921, "campaign_boundary"),
    Row("boundary_n256_p91393", 256, 91393, "campaign_boundary"),
)


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
        "x44_h4_centered_max_shell_bound": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def pair_sum(domain: list[int], p: int, pair: tuple[int, int]) -> int:
    return (domain[pair[0]] + domain[pair[1]]) % p


def coset_key(value: int, h_values: list[int], p: int) -> int:
    assert value % p
    return min((value * h) % p for h in h_values)


def quotient_cosets(h_values: list[int], p: int) -> list[int]:
    seen: set[int] = set()
    reps: list[int] = []
    for value in range(1, p):
        if value in seen:
            continue
        coset = {(value * h) % p for h in h_values}
        seen.update(coset)
        reps.append(min(coset))
    return sorted(reps)


def ratio_count_for_sum(s: int, h_values: list[int], h_set: set[int], p: int) -> int:
    inv_s = pow(s, -1, p)
    count = 0
    for r in h_values:
        if r == 1:
            continue
        if ((1 + r) * inv_s) % p in h_set:
            count += 1
    return count


def shell_report(row: Row) -> dict[str, Any]:
    check(f"{row.label}: p is prime", h3.is_prime(row.p), f"p={row.p}")
    check(f"{row.label}: p == 1 mod n", (row.p - 1) % row.n == 0)
    domain = h1.mu_domain(row.p, row.n)
    h_values = sorted(domain)
    h_set = set(h_values)

    direct_shells: dict[int, int] = defaultdict(int)
    for pair in combinations(range(row.n), 2):
        s = pair_sum(domain, row.p, pair)
        if s:
            direct_shells[s] += 1

    formula_mismatches: list[dict[str, Any]] = []
    coset_sizes_from_shells: dict[int, set[int]] = defaultdict(set)
    for s, direct_size in direct_shells.items():
        ratio_count = ratio_count_for_sum(s, h_values, h_set, row.p)
        if ratio_count != 2 * direct_size and len(formula_mismatches) < 5:
            formula_mismatches.append(
                {"sum": s, "direct_size": direct_size, "ratio_count": ratio_count}
            )
        coset_sizes_from_shells[coset_key(s, h_values, row.p)].add(direct_size)

    cosets = quotient_cosets(h_values, row.p)
    coset_rows = []
    all_even = True
    max_coset_shell = 0
    nonzero_coset_count = 0
    for rep in cosets:
        ratio_count = ratio_count_for_sum(rep, h_values, h_set, row.p)
        all_even &= ratio_count % 2 == 0
        shell_size = ratio_count // 2
        max_coset_shell = max(max_coset_shell, shell_size)
        if shell_size:
            nonzero_coset_count += 1
        if len(coset_rows) < 12 or shell_size == max_coset_shell:
            coset_rows.append(
                {
                    "representative": rep,
                    "ratio_count": ratio_count,
                    "shell_size": shell_size,
                }
            )

    inconsistent_cosets = {
        str(key): sorted(values)
        for key, values in coset_sizes_from_shells.items()
        if len(values) > 1
    }
    direct_max = max(direct_shells.values(), default=0)

    check(f"{row.label}: ratio parametrization matches every direct shell", not formula_mismatches)
    check(f"{row.label}: direct shell size is constant on observed cosets", not inconsistent_cosets)
    check(f"{row.label}: all quotient ratio counts are even", all_even)
    check(f"{row.label}: quotient coset count is (p-1)/n", len(cosets) == (row.p - 1) // row.n)
    check(
        f"{row.label}: max direct shell equals max quotient-coset shell",
        direct_max == max_coset_shell,
        f"direct={direct_max}, quotient={max_coset_shell}",
    )

    return {
        "label": row.label,
        "kind": row.kind,
        "n": row.n,
        "p": row.p,
        "quotient_cosets": len(cosets),
        "nonzero_pair_sum_values": len(direct_shells),
        "nonzero_cosets_with_shells": nonzero_coset_count,
        "max_direct_shell_size": direct_max,
        "max_coset_shell_size": max_coset_shell,
        "direct_shell_size_histogram": {
            str(k): v for k, v in sorted(Counter(direct_shells.values()).items())
        },
        "coset_shell_size_histogram": {
            str(k): v
            for k, v in sorted(
                Counter(ratio_count_for_sum(rep, h_values, h_set, row.p) // 2 for rep in cosets).items()
            )
        },
        "sample_coset_rows": coset_rows,
        "formula_mismatches": formula_mismatches,
        "inconsistent_cosets": inconsistent_cosets,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    rows = [shell_report(row) for row in ROWS]
    check("all rows have exact coset-shell parametrization", all(not row["formula_mismatches"] for row in rows))
    check("all rows have coset-constant shell sizes", all(not row["inconsistent_cosets"] for row in rows))
    check("at least one replay row has max shell size > 4", any(row["max_coset_shell_size"] > 4 for row in rows))
    return {
        "task": "X48 h=4 centered coset shell parametrization",
        "node": "active_core_count_bound",
        "status": "PROVED COSET PARAMETRIZATION FOR CENTERED H4 PAIR-SUM SHELLS",
        "theorem": (
            "For H=mu_n in F_p and s != 0, unordered distinct pairs {x,y} in H "
            "with x+y=s are in two-to-one correspondence with ratios "
            "r=x/y in H\\{1} satisfying 1+r in sH.  Therefore "
            "m_s = 1/2 * #{r in H\\{1}: 1+r in sH}.  In particular m_s "
            "depends only on the quotient coset sH, and X44's max-shell "
            "statistic is the maximum shifted-subgroup intersection over "
            "F_p^*/H."
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

    print("\ncoset-shell rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: cosets={row['quotient_cosets']} "
            f"max_shell={row['max_coset_shell_size']} "
            f"nonzero_cosets={row['nonzero_cosets_with_shells']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X48 h4 coset-shell checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
