#!/usr/bin/env python3
"""U2-A verifier: exact moment/PTE window split.

This is arithmetic only.  It scopes U2-B by deriving, from QA.22's six
clean-rate rows, the exact block-size windows where a primitive moment/PTE
block can matter under the frozen W3 grammar:

    t < b <= floor(log2 n)^2.

It also emits the transported quotient-row windows used by TR/per-leaf
consumers.  For transported rows, the inherited tail depth `tail_b` is the U2
moment depth; the quotient-local t_q = floor(A/M)-floor(k/M) is recorded but
not used as the moment depth.

Run:
  python3 experimental/scripts/verify_u2a_window_split.py
Refresh certificate:
  python3 experimental/scripts/verify_u2a_window_split.py --write-certificate
"""

from __future__ import annotations

import json
import math
import os
import sys
from dataclasses import dataclass


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
QA22_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "qa22-staircase-budget",
    "qa22_staircase_budget.json",
)
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "u2a-window-split",
    "u2a_window_split.json",
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
    print(line)
    if not cond:
        FAILS.append(name)


def floor_log2_power_of_two(n: int) -> int:
    check(f"{n}: power-of-two row length", n > 0 and n & (n - 1) == 0)
    return n.bit_length() - 1


def b_window(t: int, n: int) -> dict[str, object]:
    logn = floor_log2_power_of_two(n)
    bmax = logn * logn
    start = t + 1
    values = list(range(start, bmax + 1)) if start <= bmax else []
    old_end = min(2 * t + 4, bmax)
    old_values = list(range(start, old_end + 1)) if start <= old_end else []
    beyond_old_start = max(start, 2 * t + 5)
    beyond_old_values = (
        list(range(beyond_old_start, bmax + 1)) if beyond_old_start <= bmax else []
    )
    return {
        "floor_log2_n": logn,
        "grammar_b_max": bmax,
        "window_start": start,
        "window_end": bmax,
        "b_values": values,
        "count": len(values),
        "old_f2_window_end_2t_plus_4": old_end,
        "old_f2_overlap_b_values": old_values,
        "old_f2_overlap_count": len(old_values),
        "beyond_old_f2_b_values": beyond_old_values,
        "beyond_old_f2_count": len(beyond_old_values),
        "empty": len(values) == 0,
    }


def first_power_two_gt(x: int) -> int:
    return 1 << x.bit_length()


def giant_parameters(row: dict[str, object]) -> dict[str, object]:
    n = int(row["n"])
    t = int(row["t"])
    first_m = first_power_two_gt(t)
    admissible_m = []
    m = first_m
    while m <= n:
        if n % m == 0:
            admissible_m.append(m)
        m *= 2
    return {
        "b_min": t + 1,
        "complement_reduced_b_max": n // 2,
        "max_disjoint_t_plus_1_blocks": n // (t + 1),
        "first_charged_coset_M": first_m if n % first_m == 0 else None,
        "first_charged_scale_n_over_M": n // first_m if n % first_m == 0 else None,
        "admissible_charged_coset_M": admissible_m,
        "admissible_charged_scales_n_over_M": [n // m for m in admissible_m],
    }


def row_id(row: dict[str, object]) -> str:
    return f"{row['label']}_rate_{str(row['rate']).replace('/', '_')}"


def load_qa22() -> dict[str, object]:
    with open(QA22_CERT, encoding="utf-8") as f:
        return json.load(f)


def transported_windows(row: dict[str, object]) -> list[dict[str, object]]:
    out = []
    for term in row["transported_quotient_row_table"]:
        inherited_t = int(term["tail_b"])
        n_q = int(term["scale_n_over_M"])
        local_t = int(term["quotient_A_floor"]) - int(term["quotient_k_floor"])
        inherited = b_window(inherited_t, n_q)
        local = b_window(local_t, n_q)
        out.append(
            {
                "M": int(term["M"]),
                "scale_n_over_M": n_q,
                "quotient_k_floor": int(term["quotient_k_floor"]),
                "quotient_A_floor": int(term["quotient_A_floor"]),
                "quotient_local_t": local_t,
                "inherited_tail_t": inherited_t,
                "inherited_tail_window": inherited,
                "quotient_local_window_recorded_not_used_for_U2": local,
            }
        )
    return out


def build_certificate() -> dict[str, object]:
    qa22 = load_qa22()
    rows = []
    rowc_live_cells = []
    prize_rows = []
    transported_live_cells = []

    check("QA.22 source has six rows", len(qa22["rows"]) == 6)
    for row in qa22["rows"]:
        rid = row_id(row)
        base_window = b_window(int(row["t"]), int(row["n"]))
        transported = transported_windows(row)
        is_rowc = row["label"] == "RowC"
        is_prize = row["label"] == "prize"

        if is_rowc:
            rowc_live_cells.append(
                {
                    "row_id": rid,
                    "n": int(row["n"]),
                    "t": int(row["t"]),
                    "b_values": base_window["b_values"],
                    "count": base_window["count"],
                    "old_f2_overlap_b_values": base_window["old_f2_overlap_b_values"],
                    "beyond_old_f2_b_values": base_window["beyond_old_f2_b_values"],
                }
            )
            check(f"{rid}: Row-C base small window nonempty", not base_window["empty"])
            check(
                f"{rid}: Row-C full grammar extends old F2 window",
                base_window["beyond_old_f2_count"] > 0,
                f"beyond={base_window['beyond_old_f2_count']}",
            )
        if is_prize:
            prize_rows.append(rid)
            gp = giant_parameters(row)
            check(
                f"{rid}: prize base small window empty",
                base_window["empty"],
                f"t={row['t']}, bmax={base_window['grammar_b_max']}",
            )
            check(
                f"{rid}: prize giant regime has bounded disjoint capacity",
                gp["max_disjoint_t_plus_1_blocks"] <= 512,
                f"capacity={gp['max_disjoint_t_plus_1_blocks']}",
            )
        else:
            gp = None

        for tw in transported:
            check(f"{rid} M={tw['M']}: transported scale divides n", int(row["n"]) % tw["M"] == 0)
            inherited = tw["inherited_tail_window"]
            if not inherited["empty"]:
                transported_live_cells.append(
                    {
                        "row_id": rid,
                        "M": tw["M"],
                        "scale_n_over_M": tw["scale_n_over_M"],
                        "inherited_tail_t": tw["inherited_tail_t"],
                        "b_values": inherited["b_values"],
                        "count": inherited["count"],
                    }
                )

        rows.append(
            {
                "row_id": rid,
                "label": row["label"],
                "rate": row["rate"],
                "n": int(row["n"]),
                "k": int(row["k"]),
                "A": int(row["A"]),
                "t": int(row["t"]),
                "base_window": base_window,
                "giant_parameters": gp,
                "transported_quotient_row_windows": transported,
            }
        )

    check("U2-A identifies exactly three Row-C small-window rows", len(rowc_live_cells) == 3)
    check("U2-A identifies exactly three prize rows", len(prize_rows) == 3)
    check(
        "U2-A transported prize inherited windows empty",
        all(
            tw["inherited_tail_window"]["empty"]
            for row in rows
            if row["label"] == "prize"
            for tw in row["transported_quotient_row_windows"]
        ),
    )

    return {
        "task": "U2-A window split",
        "node": "x4b_moment_trade_exclusion / u2_per_row_certifier",
        "source": "qa22_staircase_budget.json",
        "grammar": "w3 v1: t < b <= floor(log2 n)^2",
        "rows": rows,
        "u2b_base_row_live_cells": rowc_live_cells,
        "tr_transported_quotient_live_cells": transported_live_cells,
        "prize_rows_with_empty_small_window": prize_rows,
        "checks": NCHECK,
        "status": "PASS: exact U2-A windows derived; prize small windows empty",
    }


def main() -> int:
    write = "--write-certificate" in sys.argv
    cert = build_certificate()
    if write:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w", encoding="utf-8") as f:
            json.dump(cert, f, indent=2, sort_keys=True)
            f.write("\n")
        print(f"[write] {CERT}")
    expected = None
    if os.path.exists(CERT):
        with open(CERT, encoding="utf-8") as f:
            expected = json.load(f)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", cert == expected)
    if FAILS:
        print("\nrecomputed summary:")
        print(json.dumps(cert, indent=2, sort_keys=True))
        print("\nFAIL:")
        for name in FAILS:
            print("  -", name)
        return 1
    print("\nsummary:")
    print(
        json.dumps(
            {
                "base_live_cells": cert["u2b_base_row_live_cells"],
                "transported_live_cell_count": len(cert["tr_transported_quotient_live_cells"]),
                "prize_empty": cert["prize_rows_with_empty_small_window"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    print(f"\nAll {NCHECK} checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
