#!/usr/bin/env python3
"""X43 h=4 centered shell-size closure criterion.

X42 gives R_centered <= sum_s C(m_s,4), where m_s is the nonzero pair-sum
shell size.  This packet records the small-shell closure:

  * max m_s <= 3  => centered branch is empty;
  * max m_s <= 4  => R_centered <= (sum_s m_s)/4 < n^2.

The verifier replays the X42 certificate and checks the criterion on the
campaign rows already audited there.
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
    "x43-h4-centered-shell-size-closure",
    "x43_h4_centered_shell_size_closure.json",
)
X42_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x42-h4-centered-energy-accounting",
    "x42_h4_centered_energy_accounting.json",
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
        "x42_h4_centered_energy_accounting": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def small_shell_bound(total_pairs: int, max_shell_size: int) -> int:
    if max_shell_size <= 3:
        return 0
    if max_shell_size <= 4:
        return total_pairs // 4
    raise ValueError("small-shell closure only covers max_shell_size <= 4")


def check_x42_rows() -> list[dict[str, Any]]:
    x42 = load_json(X42_CERT)
    rows = []
    for row in x42["rows"]:
        total_pairs = row["n"] * (row["n"] - 1) // 2
        max_m = row["max_shell_size"]
        criterion_applies = max_m <= 4
        closure_bound = small_shell_bound(total_pairs, max_m) if criterion_applies else None
        if criterion_applies:
            check(
                f"{row['label']}: X43 small-shell bound dominates exact centered count",
                row["centered_trade_count_exact"] <= closure_bound,
                f"exact={row['centered_trade_count_exact']}, bound={closure_bound}",
            )
            check(
                f"{row['label']}: X43 small-shell bound fits n^2",
                closure_bound < row["n"] ** 2,
                f"bound={closure_bound}, n^2={row['n'] ** 2}",
            )
        elif row["kind"] == "campaign_boundary":
            check(f"{row['label']}: campaign row satisfies small-shell criterion", False, f"max_m={max_m}")
        rows.append(
            {
                "label": row["label"],
                "kind": row["kind"],
                "n": row["n"],
                "p": row["p"],
                "max_shell_size": max_m,
                "total_unordered_pairs": total_pairs,
                "criterion_applies": criterion_applies,
                "x43_small_shell_bound": closure_bound,
                "exact_centered_trade_count": row["centered_trade_count_exact"],
                "x42_binom4_bound": row["binom4_shell_bound"],
            }
        )
    return rows


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    rows = check_x42_rows()
    campaign = [row for row in rows if row["kind"] == "campaign_boundary"]
    stress = [row for row in rows if row["kind"] == "low_characteristic_stress"]
    check(
        "all X42 campaign rows satisfy max shell size <= 4",
        all(row["criterion_applies"] for row in campaign),
    )
    check(
        "all X42 campaign rows have X43 bound below n^2",
        all(row["x43_small_shell_bound"] is not None and row["x43_small_shell_bound"] < row["n"] ** 2 for row in campaign),
    )
    check(
        "stress rows show the criterion is not vacuous",
        any(not row["criterion_applies"] and row["exact_centered_trade_count"] > 0 for row in stress),
    )
    return {
        "task": "X43 h=4 centered shell-size closure",
        "node": "active_core_count_bound",
        "status": "PROVED CRITERION + CERTIFICATE REPLAY: max nonzero pair-shell size <=4 closes the centered branch below n^2",
        "theorem": (
            "Let m_s be nonzero pair-sum shell sizes.  X42 gives "
            "R_centered <= sum_s C(m_s,4).  If max_s m_s <=3 then every term "
            "vanishes.  If max_s m_s <=4, then C(m_s,4) is 1 only at m_s=4, "
            "so C(m_s,4) <= m_s/4 and R_centered <= (sum_s m_s)/4 < n^2.  "
            "Thus the centered affine branch is safely below the rewired n^3 "
            "terminal column under this one-number shell-size condition."
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

    print("\nX42 row replay:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: max_m={row['max_shell_size']} "
            f"x43={row['x43_small_shell_bound']} exact={row['exact_centered_trade_count']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X43 centered shell-size checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
