#!/usr/bin/env python3
"""X55 h=4 centered surplus-threshold bridge.

X50 closes the centered h=4 branch when the quotient shell maximum M is at
most the exact threshold T(n).  X54 proves that a shell of size M forces
n*C(M,2) h=2 norm-gate surplus collisions.  This verifier records the exact
contrapositive:

    N_surplus < n*C(T(n)+1,2)  =>  M <= T(n).

The condition is sufficient, not necessary.
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
    "x55-h4-surplus-threshold-bridge",
    "x55_h4_surplus_threshold_bridge.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")
X50_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x50-h4-centered-threshold",
    "x50_h4_centered_threshold.json",
)
X54_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x54-h4-shell-surplus-norm-gate-bridge",
    "x54_h4_shell_surplus_norm_gate_bridge.json",
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
        "x50_h4_centered_threshold": "PROVED",
        "x54_h4_shell_surplus_norm_gate_bridge": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def fits_threshold(n: int, m: int) -> bool:
    if m < 4:
        return True
    return (m - 1) * (m - 2) * (m - 3) * (n - 2) <= 48 * n * n


def exact_threshold(n: int) -> int:
    lo = 0
    hi = 4
    while fits_threshold(n, hi):
        lo = hi
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if fits_threshold(n, mid):
            lo = mid
        else:
            hi = mid
    return lo


def surplus_barrier(n: int, threshold: int) -> int:
    return n * math.comb(threshold + 1, 2)


def row_report(row: dict[str, Any]) -> dict[str, Any]:
    n = int(row["n"])
    m = int(row["max_shell_size"])
    surplus = int(row["direct_shell_surplus_pairs"])
    threshold = exact_threshold(n)
    barrier = surplus_barrier(n, threshold)
    forced_from_m = n * math.comb(m, 2) if m >= 2 else 0
    surplus_condition = surplus < barrier
    x50_safe = m <= threshold

    check(
        f"{row['label']}: X54 forced surplus is below total surplus",
        surplus >= forced_from_m,
        f"surplus={surplus}, forced={forced_from_m}",
    )
    check(
        f"{row['label']}: surplus barrier implies X50 max-shell threshold",
        (not surplus_condition) or x50_safe,
        f"surplus={surplus}, barrier={barrier}, M={m}, T={threshold}",
    )
    check(
        f"{row['label']}: over-threshold shell would force barrier",
        m <= threshold or forced_from_m >= barrier,
        f"forced={forced_from_m}, barrier={barrier}",
    )

    return {
        "label": row["label"],
        "kind": row["kind"],
        "n": n,
        "p": row["p"],
        "max_shell_size": m,
        "exact_threshold": threshold,
        "shell_surplus_pairs": surplus,
        "surplus_barrier": barrier,
        "forced_surplus_from_max_shell": forced_from_m,
        "surplus_condition_satisfied": surplus_condition,
        "x50_max_shell_safe": x50_safe,
        "barrier_margin": barrier - surplus,
    }


def scale_report(row: dict[str, Any]) -> dict[str, Any]:
    n = int(row["n"])
    threshold = exact_threshold(n)
    choose_next = math.comb(threshold + 1, 2)
    barrier = surplus_barrier(n, threshold)

    general_h2_scale_fits = 216 * n * n < choose_next**3
    prime_h2_scale_fits = 8 * n * n < choose_next**3
    check(
        f"n={n}: exact threshold agrees with X50 certificate",
        threshold == int(row["exact_threshold"]),
        f"computed={threshold}, cert={row['exact_threshold']}",
    )
    check(
        f"n={n}: 6*n^(5/3) scale lies below surplus barrier",
        general_h2_scale_fits,
        f"216*n^2={216*n*n}, C(T+1,2)^3={choose_next**3}",
    )
    check(
        f"n={n}: 2*n^(5/3) scale lies below surplus barrier",
        prime_h2_scale_fits,
        f"8*n^2={8*n*n}, C(T+1,2)^3={choose_next**3}",
    )

    return {
        "n": n,
        "exact_threshold": threshold,
        "surplus_barrier": barrier,
        "binom_threshold_plus_one_2": choose_next,
        "general_constant_6_scale_check": {
            "inequality": "216*n^2 < C(T+1,2)^3",
            "holds": general_h2_scale_fits,
            "left": 216 * n * n,
            "right": choose_next**3,
        },
        "prime_constant_2_scale_check": {
            "inequality": "8*n^2 < C(T+1,2)^3",
            "holds": prime_h2_scale_fits,
            "left": 8 * n * n,
            "right": choose_next**3,
        },
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x50 = load_json(X50_CERT)
    x54 = load_json(X54_CERT)
    check("X50 certificate has threshold table", bool(x50.get("threshold_table")))
    check("X54 certificate has surplus rows", bool(x54.get("rows")))

    rows = [row_report(row) for row in x54["rows"]]
    scale_table = [scale_report(row) for row in x50["threshold_table"]]

    check(
        "some replay rows satisfy the surplus barrier",
        any(row["surplus_condition_satisfied"] for row in rows),
    )
    check(
        "surplus barrier is not claimed necessary",
        any((not row["surplus_condition_satisfied"]) and row["x50_max_shell_safe"] for row in rows),
    )
    check(
        "all replay rows with satisfied surplus barrier are X50-safe",
        all((not row["surplus_condition_satisfied"]) or row["x50_max_shell_safe"] for row in rows),
    )
    check(
        "all recorded scale rows have constant-6 room",
        all(row["general_constant_6_scale_check"]["holds"] for row in scale_table),
    )

    return {
        "task": "X55 h=4 surplus-threshold bridge",
        "node": "active_core_count_bound",
        "status": "PROVED SUFFICIENT SURPLUS BARRIER FOR X50",
        "theorem": (
            "Let T(n) be the X50 exact shell threshold.  X54 gives "
            "N_surplus >= n*C(M,2) for a quotient shell of size M.  Therefore "
            "N_surplus < n*C(T(n)+1,2) rules out M >= T(n)+1, hence M <= T(n), "
            "and X50 puts the centered h=4 branch inside the n^3 terminal column. "
            "This is a sufficient condition only.  The exact surplus barrier has "
            "room for a total-surplus bound at the 6*n^(5/3) scale on every "
            "recorded threshold row, checked by 216*n^2 < C(T+1,2)^3."
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

    print("\nsurplus-threshold rows:")
    for row in cert["rows"]:
        mark = "pass" if row["surplus_condition_satisfied"] else "no-claim"
        print(
            f"{row['label']}: M={row['max_shell_size']} T={row['exact_threshold']} "
            f"surplus={row['shell_surplus_pairs']} barrier={row['surplus_barrier']} "
            f"{mark}"
        )

    print("\nscale rows:")
    for row in cert["scale_table"]:
        print(
            f"n={row['n']}: T={row['exact_threshold']} "
            f"barrier={row['surplus_barrier']} "
            f"6-scale={row['general_constant_6_scale_check']['holds']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X55 h4 surplus-threshold checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
