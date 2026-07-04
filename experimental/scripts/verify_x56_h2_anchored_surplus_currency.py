#!/usr/bin/env python3
"""X56 h=2 anchored surplus currency.

X54 counts the centered h=4 shell surplus in unanchored shell-pair currency:

    N_surplus = n * sum_C C(m_C,2).

The h=2 rung is normally stated in anchored currency.  This verifier records
the exact conversion for the nonzero pair-sum surplus:

    A_anchor_surplus = 4 * sum_C C(m_C,2),
    N_surplus = (n/4) * A_anchor_surplus.

Thus X55's unanchored surplus barrier is equivalent to the anchored target
A_anchor_surplus < 4*C(T(n)+1,2).
"""

from __future__ import annotations

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
    "x56-h2-anchored-surplus-currency",
    "x56_h2_anchored_surplus_currency.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")
X48_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x48-h4-centered-coset-shell-param",
    "x48_h4_centered_coset_shell_param.json",
)
X54_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x54-h4-shell-surplus-norm-gate-bridge",
    "x54_h4_shell_surplus_norm_gate_bridge.json",
)
X55_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x55-h4-surplus-threshold-bridge",
    "x55_h4_surplus_threshold_bridge.json",
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
        "pte_h2_rung": "PROVED",
        "x48_h4_centered_coset_shell_param": "PROVED",
        "x54_h4_shell_surplus_norm_gate_bridge": "PROVED",
        "x55_h4_surplus_threshold_bridge": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def expand_histogram(hist: dict[str, int]) -> list[int]:
    out: list[int] = []
    for value, count in hist.items():
        out.extend([int(value)] * int(count))
    return out


def quadratic_surplus(values: list[int]) -> int:
    return sum(math.comb(value, 2) for value in values if value >= 2)


def indexed_by_label(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {str(row["label"]): row for row in rows}


def row_report(
    x48_row: dict[str, Any],
    x54_row: dict[str, Any],
    x55_row: dict[str, Any],
) -> dict[str, Any]:
    label = str(x48_row["label"])
    n = int(x48_row["n"])
    coset_values = expand_histogram(x48_row["coset_shell_size_histogram"])
    quotient_quadratic = quadratic_surplus(coset_values)
    anchored_surplus = 4 * quotient_quadratic
    unanchored_surplus = int(x54_row["direct_shell_surplus_pairs"])
    threshold = int(x55_row["exact_threshold"])
    anchored_barrier = 4 * math.comb(threshold + 1, 2)
    unanchored_barrier = int(x55_row["surplus_barrier"])

    check(
        f"{label}: X54 unanchored surplus converts from anchored currency",
        4 * unanchored_surplus == n * anchored_surplus,
        f"4N={4*unanchored_surplus}, nA={n*anchored_surplus}",
    )
    check(
        f"{label}: X55 barriers convert between currencies",
        4 * unanchored_barrier == n * anchored_barrier,
        f"4B_un={4*unanchored_barrier}, nB_an={n*anchored_barrier}",
    )
    check(
        f"{label}: surplus condition is currency-invariant",
        (unanchored_surplus < unanchored_barrier)
        == (anchored_surplus < anchored_barrier),
    )
    check(
        f"{label}: anchored surplus is a multiple of four",
        anchored_surplus % 4 == 0,
        f"A={anchored_surplus}",
    )

    return {
        "label": label,
        "kind": x48_row["kind"],
        "n": n,
        "p": x48_row["p"],
        "max_shell_size": x54_row["max_shell_size"],
        "quotient_quadratic_surplus": quotient_quadratic,
        "anchored_nonzero_h2_surplus": anchored_surplus,
        "unanchored_shell_surplus": unanchored_surplus,
        "exact_threshold": threshold,
        "anchored_x55_barrier": anchored_barrier,
        "unanchored_x55_barrier": unanchored_barrier,
        "anchored_barrier_margin": anchored_barrier - anchored_surplus,
        "currency_identity": "4*N_surplus = n*A_anchor_surplus",
    }


def scale_report(row: dict[str, Any]) -> dict[str, Any]:
    n = int(row["n"])
    threshold = int(row["exact_threshold"])
    anchored_barrier = 4 * math.comb(threshold + 1, 2)
    general_h2_too_weak = 216 * n**5 > anchored_barrier**3
    prime_h2_too_weak = 8 * n**5 > anchored_barrier**3
    check(
        f"n={n}: anchored target is below 6*n^(5/3) line-bound scale",
        general_h2_too_weak,
        f"216*n^5={216*n**5}, target^3={anchored_barrier**3}",
    )
    check(
        f"n={n}: prime-line scale comparison is recorded",
        n == 16 or prime_h2_too_weak,
        f"8*n^5={8*n**5}, target^3={anchored_barrier**3}",
    )
    return {
        "n": n,
        "exact_threshold": threshold,
        "anchored_x55_barrier": anchored_barrier,
        "general_h2_bound_comparison": {
            "comparison": "6*n^(5/3) > 4*C(T+1,2)",
            "holds": general_h2_too_weak,
            "cubed_left": 216 * n**5,
            "cubed_right": anchored_barrier**3,
        },
        "prime_h2_bound_comparison": {
            "comparison": "2*n^(5/3) > 4*C(T+1,2)",
            "holds": prime_h2_too_weak,
            "cubed_left": 8 * n**5,
            "cubed_right": anchored_barrier**3,
        },
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x48 = load_json(X48_CERT)
    x54 = indexed_by_label(load_json(X54_CERT)["rows"])
    x55 = load_json(X55_CERT)
    x55_rows = indexed_by_label(x55["rows"])
    check("X48 certificate has rows", bool(x48.get("rows")))
    check("X54 labels cover X48 rows", all(row["label"] in x54 for row in x48["rows"]))
    check("X55 labels cover X48 rows", all(row["label"] in x55_rows for row in x48["rows"]))

    rows = [row_report(row, x54[row["label"]], x55_rows[row["label"]]) for row in x48["rows"]]
    scale_table = [scale_report(row) for row in x55["scale_table"]]

    check(
        "all replay rows satisfy the currency identity",
        all(4 * row["unanchored_shell_surplus"] == row["n"] * row["anchored_nonzero_h2_surplus"] for row in rows),
    )
    check(
        "some replay row is barrier-passing in anchored currency",
        any(row["anchored_nonzero_h2_surplus"] < row["anchored_x55_barrier"] for row in rows),
    )
    check(
        "some replay row records sufficiency-not-necessity in anchored currency",
        any(row["anchored_nonzero_h2_surplus"] >= row["anchored_x55_barrier"] for row in rows),
    )
    check(
        "all scale rows show the general h2 line-bound total is too weak for X55 target",
        all(row["general_h2_bound_comparison"]["holds"] for row in scale_table),
    )
    check(
        "all scale rows n>=32 show the prime h2 line-bound total is too weak",
        all(row["n"] < 32 or row["prime_h2_bound_comparison"]["holds"] for row in scale_table),
    )

    return {
        "task": "X56 h=2 anchored surplus currency",
        "node": "active_core_count_bound",
        "status": "PROVED EXACT CURRENCY CONVERSION",
        "theorem": (
            "For each anchored nonzero h=2 source pair {1,a}, the number of "
            "disjoint target pairs is m_{1+a}-1.  X48 gives exactly 2*m_C "
            "ratios a with 1+a in a quotient coset C, so the anchored surplus "
            "is sum_C 2*m_C*(m_C-1) = 4*sum_C C(m_C,2).  X54 gives "
            "N_surplus = n*sum_C C(m_C,2), hence 4*N_surplus = "
            "n*A_anchor_surplus.  Therefore X55 is equivalent in anchored "
            "currency to A_anchor_surplus < 4*C(T(n)+1,2)."
        ),
        "dependency_statuses": deps,
        "rows": rows,
        "scale_table": scale_table,
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

    print("\nanchored surplus rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: A={row['anchored_nonzero_h2_surplus']} "
            f"barrier={row['anchored_x55_barrier']} "
            f"N={row['unanchored_shell_surplus']} "
            f"identity=4N/n={4*row['unanchored_shell_surplus']//row['n']}"
        )

    print("\nscale rows:")
    for row in cert["scale_table"]:
        print(
            f"n={row['n']}: anchored_barrier={row['anchored_x55_barrier']} "
            f"h2_general_too_weak={row['general_h2_bound_comparison']['holds']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X56 h2 anchored-surplus currency checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
