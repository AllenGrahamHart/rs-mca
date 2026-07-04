#!/usr/bin/env python3
"""X37 h=4 quartic-fiber form.

For h=4, equality of the top three locator coefficients is equivalent to
two completely split fibers of one monic quartic:

    L_P(x)=0 for x in P,    L_P(y)=c for y in Q.

The nonzero constant c is e4(P)-e4(Q).  This packet is a small proof reduction
and examples, tying the signed moment residue to the pullback/fiber taxonomy.
"""

from __future__ import annotations

from itertools import combinations
import json
import os
import sys
from typing import Any

import verify_h1_u1_toy_harness as h1
import verify_x33_h4_common_gcd_gate as x33


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x37-h4-quartic-fiber-form",
    "x37_h4_quartic_fiber_form.json",
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
        "x35_h4_power_sum_gate": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        check(f"DAG node {node} has expected status", statuses.get(node) == expected, statuses.get(node, "missing"))
    return {node: statuses.get(node, "missing") for node in needed}


def elementary_all(domain: list[int], p: int, support: tuple[int, ...]) -> tuple[int, int, int, int]:
    e = [0, 0, 0, 0, 0]
    e[0] = 1
    for exponent in support:
        x = domain[exponent]
        for r in range(4, 0, -1):
            e[r] = (e[r] + x * e[r - 1]) % p
    return e[1], e[2], e[3], e[4]


def locator_value_from_e(e: tuple[int, int, int, int], x: int, p: int) -> int:
    e1, e2, e3, e4 = e
    return (pow(x, 4, p) - e1 * pow(x, 3, p) + e2 * x * x - e3 * x + e4) % p


def support_values(domain: list[int], support: tuple[int, ...]) -> list[int]:
    return [domain[i] for i in support]


def analyze_pair(n: int, p: int, p_set: tuple[int, ...], q_set: tuple[int, ...], label: str) -> dict[str, Any]:
    domain = h1.mu_domain(p, n)
    p_e = elementary_all(domain, p, p_set)
    q_e = elementary_all(domain, p, q_set)
    same_top_three = p_e[:3] == q_e[:3]
    fiber_constant = (p_e[3] - q_e[3]) % p

    p_values = [locator_value_from_e(p_e, x, p) for x in support_values(domain, p_set)]
    q_values = [locator_value_from_e(p_e, x, p) for x in support_values(domain, q_set)]
    p_is_zero_fiber = all(value == 0 for value in p_values)
    q_is_constant_fiber = len(set(q_values)) == 1 and q_values[0] == fiber_constant
    disjoint = not (set(p_set) & set(q_set))

    check(f"{label}: P is the zero fiber of L_P", p_is_zero_fiber)
    check(
        f"{label}: quartic fiber criterion matches top-three equality",
        same_top_three == (q_is_constant_fiber and disjoint),
        f"same_top_three={same_top_three}, q_values={q_values}, c={fiber_constant}",
    )
    if same_top_three:
        check(f"{label}: nontrivial disjoint trade has nonzero fiber separation", fiber_constant != 0)

    return {
        "label": label,
        "n": n,
        "p": p,
        "P": list(p_set),
        "Q": list(q_set),
        "P_elementary": list(p_e),
        "Q_elementary": list(q_e),
        "same_top_three": same_top_three,
        "fiber_constant_e4P_minus_e4Q": fiber_constant,
        "P_locator_values_on_P": p_values,
        "P_locator_values_on_Q": q_values,
        "quartic_fiber_criterion_holds": q_is_constant_fiber and disjoint,
    }


def check_tiny_exhaustion() -> dict[str, Any]:
    n = 16
    p = 257
    domain = h1.mu_domain(p, n)
    checked = 0
    mismatches: list[dict[str, Any]] = []
    subsets = list(combinations(range(n), 4))
    for i, p_set in enumerate(subsets):
        p_e = elementary_all(domain, p, p_set)
        p_mask = x33.support_mask(p_set)
        for q_set in subsets[i + 1 :]:
            q_mask = x33.support_mask(q_set)
            if p_mask & q_mask:
                continue
            checked += 1
            q_e = elementary_all(domain, p, q_set)
            same_top_three = p_e[:3] == q_e[:3]
            c = (p_e[3] - q_e[3]) % p
            q_values = [locator_value_from_e(p_e, x, p) for x in support_values(domain, q_set)]
            fiber = len(set(q_values)) == 1 and q_values[0] == c
            if same_top_three != fiber and len(mismatches) < 5:
                mismatches.append({"P": list(p_set), "Q": list(q_set), "same_top_three": same_top_three, "fiber": fiber})
    check("n=16: quartic-fiber criterion matches all disjoint 4-pairs", not mismatches)
    return {
        "n": n,
        "p": p,
        "checked_disjoint_pairs": checked,
        "mismatches": mismatches,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    examples = [
        analyze_pair(32, 4993, (0, 8, 16, 24), (1, 9, 17, 25), "mu4 baseline"),
        analyze_pair(64, 4993, (0, 2, 32, 34), (8, 21, 40, 53), "antipodal quotient extra"),
        analyze_pair(32, 4993, (0, 1, 2, 17), (3, 8, 19, 21), "top-level first-sum only nontrade"),
    ]
    tiny = check_tiny_exhaustion()
    return {
        "task": "X37 h=4 quartic-fiber form",
        "node": "active_core_count_bound",
        "status": (
            "PROVED REDUCTION: h=4 top-three trades are exactly two split "
            "fibers of a monic quartic locator"
        ),
        "theorem": (
            "For disjoint 4-subsets P,Q over a field, e1,e2,e3 agree iff "
            "L_Q(X)=L_P(X)-c with c=e4(P)-e4(Q).  Equivalently, P is the "
            "zero fiber of the monic quartic L_P and Q is the c-fiber.  If "
            "P and Q are disjoint and top-three equal then c is nonzero."
        ),
        "dependency_statuses": deps,
        "examples": examples,
        "tiny_exhaustion": tiny,
        "consequence": (
            "The signed h=4 moment residue is also a degree-4 two-fiber "
            "problem.  Paid cyclic/dihedral cases are quartic pullbacks; any "
            "remaining branch is a primitive quartic with two split mu_n fibers."
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

    print("\nexamples:")
    for row in cert["examples"]:
        print(
            f"{row['label']}: same_top_three={row['same_top_three']} "
            f"c={row['fiber_constant_e4P_minus_e4Q']} "
            f"Q-values={row['P_locator_values_on_Q']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X37 quartic-fiber checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
