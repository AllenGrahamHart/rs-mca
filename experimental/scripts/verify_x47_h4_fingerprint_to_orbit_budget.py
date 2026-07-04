#!/usr/bin/env python3
"""X47 h=4 fingerprint sweeps in orbit-budget currency.

X20-X22 show that checked h=4 rows have no non-fingerprinted active pairs:
all active pairs are mu_4 fibers or antipodal h=2 quotient lifts, hence paid.
X46 shows that the h=4 top-level branch fits the terminal column if the
positive canonical non-descended orbit count is <= n.

This packet records the bridge: zero non-fingerprinted active pairs imply zero
positive canonical non-descended h=4 orbits.  Therefore the checked windows
close the h=4 top-level branch in the new orbit-budget currency.
"""

from __future__ import annotations

import json
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
    "x47-h4-fingerprint-to-orbit-budget",
    "x47_h4_fingerprint_to_orbit_budget.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")
CERT_DIR = os.path.join(REPO, "experimental", "data", "certificates")

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


def cert_path(*parts: str) -> str:
    return os.path.join(CERT_DIR, *parts)


def check_dependency_nodes() -> dict[str, str]:
    dag = load_json(DAG)
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    needed = {
        "x20_h4_cyclic_fingerprint": "TEST",
        "x21_h4_prime_sweep": "TEST",
        "x22_h4_n64_full_window": "TEST",
        "x32_h4_terminal_dichotomy": "PROVED",
        "x46_h4_top_level_orbit_budget": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def bridge_row(label: str, n: int, prime_count: int, p_min: int, p_max: int, nonfingerprinted_count: int, source: str) -> dict[str, Any]:
    positive_canonical_orbits = 0 if nonfingerprinted_count == 0 else None
    fits = positive_canonical_orbits is not None and positive_canonical_orbits <= n
    expanded_bound = None if positive_canonical_orbits is None else positive_canonical_orbits * n * n
    check(f"{label}: no non-fingerprinted h=4 active pairs", nonfingerprinted_count == 0)
    check(f"{label}: positive canonical non-descended orbit count fits <= n", fits)
    check(f"{label}: expanded orbit budget fits n^3", expanded_bound is not None and expanded_bound <= n**3)
    return {
        "label": label,
        "source": source,
        "n": n,
        "prime_count": prime_count,
        "p_min": p_min,
        "p_max": p_max,
        "nonfingerprinted_count": nonfingerprinted_count,
        "positive_canonical_non_descended_orbits": positive_canonical_orbits,
        "canonical_orbit_target": n,
        "expanded_orbit_bound": expanded_bound,
        "n_cubed": n**3,
        "orbit_budget_fits": fits,
    }


def x21_window_rows(x21: dict[str, Any]) -> list[dict[str, Any]]:
    out = []
    for family in x21["families"]:
        n = family["n"]
        if n not in (16, 32):
            continue
        out.append(
            bridge_row(
                f"X21 full n={n} boundary window",
                n,
                family["prime_count"],
                family["p_min"],
                family["p_max"],
                len(family["nonfingerprinted_rows"]),
                "x21_h4_prime_sweep",
            )
        )
    check("X21 contributes full n=16 and n=32 windows", {row["n"] for row in out} == {16, 32})
    return out


def x22_window_row(x22: dict[str, Any]) -> dict[str, Any]:
    summary = x22["summary"]
    return bridge_row(
        "X22 full n=64 boundary window",
        64,
        summary["prime_count"],
        summary["p_min"],
        summary["p_max"],
        summary["nonfingerprinted_count"],
        "x22_h4_n64_full_window",
    )


def x20_selected_rows(x20: dict[str, Any]) -> list[dict[str, Any]]:
    out = []
    for row in x20["rows"]:
        counts = row["fingerprint_counts"]
        nonfingerprinted_count = counts.get("other", 0)
        out.append(
            bridge_row(
                f"X20 selected {row['label']}",
                row["n"],
                1,
                row["p"],
                row["p"],
                nonfingerprinted_count,
                "x20_h4_cyclic_fingerprint",
            )
        )
    check("X20 selected rows all have zero other fingerprint count", all(row["nonfingerprinted_count"] == 0 for row in out))
    return out


def check_bridge_implication_text() -> dict[str, Any]:
    """Machine-check the bridge's hypotheses in the dependency statements."""

    dag = load_json(DAG)
    nodes = {node["id"]: node for node in dag["nodes"]}
    x32_statement = nodes["x32_h4_terminal_dichotomy"]["statement"]
    x46_statement = nodes["x46_h4_top_level_orbit_budget"]["statement"]
    check("X32 statement names top-level non-descended branch", "not Phi_n-descended" in x32_statement or "not Phi_n" in x32_statement)
    check("X46 statement supplies <= n canonical-orbit target", "<= n such orbits suffices" in x46_statement)
    return {
        "x32_branch": "non-descended h=4 trades are exactly the top-level branch outside paid antipodal quotient",
        "x46_budget": "positive canonical non-descended orbits <= n implies h=4 top-level mass <= n^3",
        "bridge": (
            "If a positive canonical non-descended orbit existed, X33/X45 give "
            "a translated and Galois-scaled anchored h=4 active pair outside "
            "the mu4/antipodal paid fingerprints.  Thus zero non-fingerprinted "
            "active pairs forces zero such canonical orbits."
        ),
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x20 = load_json(cert_path("x20-h4-cyclic-fingerprint", "x20_h4_cyclic_fingerprint.json"))
    x21 = load_json(cert_path("x21-h4-prime-sweep", "x21_h4_prime_sweep.json"))
    x22 = load_json(cert_path("x22-h4-n64-full-window", "x22_h4_n64_full_window.json"))
    x46 = load_json(cert_path("x46-h4-top-level-orbit-budget", "x46_h4_top_level_orbit_budget.json"))

    check("X46 certificate states orbit-budget theorem", "positive canonical non-descended" in x46["theorem"])
    bridge = check_bridge_implication_text()
    exact_windows = x21_window_rows(x21) + [x22_window_row(x22)]
    selected_rows = x20_selected_rows(x20)
    check("all exact windows close the h=4 top-level branch in orbit currency", all(row["orbit_budget_fits"] for row in exact_windows))
    check("all selected rows close the h=4 top-level branch in orbit currency", all(row["orbit_budget_fits"] for row in selected_rows))
    return {
        "task": "X47 h=4 fingerprint sweeps to orbit budget",
        "node": "active_core_count_bound",
        "status": "PROVED BRIDGE + CERTIFICATE REPLAY: checked h=4 rows have zero positive canonical non-descended orbits",
        "theorem": (
            "By X32, a non-descended h=4 trade is outside the paid mu4/"
            "antipodal quotient fingerprints.  By X33 and X45, any positive "
            "canonical non-descended common-gcd orbit has a translated, "
            "Galois-scaled anchored representative in the same top-level "
            "branch.  Therefore zero non-fingerprinted h=4 active pairs in a "
            "row implies zero positive canonical non-descended h=4 orbits.  "
            "X46 then gives zero top-level mass, well inside the n^3 terminal "
            "column."
        ),
        "dependency_statuses": deps,
        "bridge_implication": bridge,
        "exact_window_rows": exact_windows,
        "selected_rows": selected_rows,
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

    print("\nexact h=4 windows in orbit currency:")
    for row in cert["exact_window_rows"]:
        print(
            f"n={row['n']:<3d} primes={row['prime_count']:<4d} "
            f"positive_orbits={row['positive_canonical_non_descended_orbits']} "
            f"bound={row['expanded_orbit_bound']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X47 h4 fingerprint-to-orbit-budget checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
