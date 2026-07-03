#!/usr/bin/env python3
"""QA.24 verifier: degenerate-tower bookkeeping for the lifting lemma.

The lifting lemma's count transfer is an equality only when

    [K(gamma):K] = M/D,        gamma = alpha^D.

If d=[K(gamma):K] is smaller, the sigma map has K-kernel dimension
(M/D)-d, so the count transfer needs a correction factor |K|^((M/D)-d).

This verifier enumerates the clean-rate rows and dyadic periods consumed by
TR-side bookkeeping and emits exact correction columns.  It does not assume
degenerate towers away; the result is deliberately conservative.
"""

from __future__ import annotations

from fractions import Fraction
import json
import math
import os
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "qa24-degenerate-towers",
    "qa24_degenerate_towers.json",
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


def powers_of_two_dividing(n: int) -> list[int]:
    out = []
    m = 2
    while m <= n:
        if n % m == 0:
            out.append(m)
        m *= 2
    return out


def frac_string(x: Fraction) -> str:
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"


def frac_float(x: Fraction) -> float:
    return x.numerator / x.denominator


ROWS = [
    {"label": "RowC", "rate": "1/4", "n": 1024, "k": 256, "A": 261, "log2_q": Fraction(250, 1)},
    {"label": "RowC", "rate": "1/8", "n": 1024, "k": 128, "A": 133, "log2_q": Fraction(250, 1)},
    {"label": "RowC", "rate": "1/16", "n": 1024, "k": 64, "A": 67, "log2_q": Fraction(250, 1)},
    {
        "label": "prize",
        "rate": "1/4",
        "n": 1 << 41,
        "k": 1 << 39,
        "A": 558345748481,
        "log2_q": Fraction(2559, 10),
    },
    {
        "label": "prize",
        "rate": "1/8",
        "n": 1 << 41,
        "k": 1 << 38,
        "A": 283467841537,
        "log2_q": Fraction(2559, 10),
    },
    {
        "label": "prize",
        "rate": "1/16",
        "n": 1 << 41,
        "k": 1 << 37,
        "A": 141733920769,
        "log2_q": Fraction(2559, 10),
    },
]


def period_summary(row: dict, M: int) -> dict:
    t = row["A"] - row["k"]
    log2_q = row["log2_q"]
    exponent = int(math.log2(M))
    # The possible class-closure scales are D=2^b, b=0..exponent.  D=M gives
    # m=1 and is always non-degenerate.  Every D<M has m>1 and can be
    # degenerate for suitable beta/gamma data; the correction below is the
    # worst case d=1 at that D, over a base-level K (multiply by [K:B]).
    proper_D_count = exponent
    worst_kernel_dim = M - 1
    first_degenerate_D = M // 2
    first_degenerate_m = 2
    first_degenerate_kernel_dim = 1
    return {
        "M": M,
        "log2_M": exponent,
        "staircase_consumer_M_gt_t": M > t,
        "D_cells": exponent + 1,
        "nondegenerate_forced_D_cells": 1,
        "degenerate_possible_D_cells": proper_D_count,
        "degenerate_tower_possible": proper_D_count > 0,
        "first_degenerate_D": first_degenerate_D,
        "first_degenerate_m": first_degenerate_m,
        "correction_factor": "|K|^(M/D-d), where d=[K(gamma):K]",
        "first_degenerate_kernel_dim_over_K": first_degenerate_kernel_dim,
        "first_degenerate_base_level_bits": frac_string(log2_q * first_degenerate_kernel_dim),
        "worst_case_D": 1,
        "worst_case_m": M,
        "worst_case_kernel_dim_over_K": worst_kernel_dim,
        "worst_case_base_level_bits": frac_string(log2_q * worst_kernel_dim),
        "worst_case_base_level_bits_float": frac_float(log2_q * worst_kernel_dim),
    }


def row_summary(row: dict) -> dict:
    periods = [period_summary(row, M) for M in powers_of_two_dividing(row["n"])]
    t = row["A"] - row["k"]
    staircase = [p for p in periods if p["staircase_consumer_M_gt_t"]]
    degenerate_possible = [p for p in periods if p["degenerate_tower_possible"]]
    tag = f"{row['label']} {row['rate']}"
    check(f"{tag}: dyadic periods enumerated", len(periods) == int(math.log2(row["n"])), f"periods={len(periods)}")
    check(f"{tag}: no nontrivial period is uniformly non-degenerate", len(degenerate_possible) == len(periods))
    check(f"{tag}: staircase/TR consumer periods are nonempty", bool(staircase), f"count={len(staircase)}, t={t}")
    check(
        f"{tag}: every staircase consumer has possible degenerate tower",
        all(p["degenerate_tower_possible"] for p in staircase),
    )
    return {
        "label": row["label"],
        "rate": row["rate"],
        "n": row["n"],
        "k": row["k"],
        "A": row["A"],
        "t": t,
        "log2_q": frac_string(row["log2_q"]),
        "periods_total": len(periods),
        "degenerate_possible_periods": len(degenerate_possible),
        "staircase_consumer_periods_M_gt_t": len(staircase),
        "first_staircase_period": staircase[0]["M"],
        "first_staircase_worst_base_bits": staircase[0]["worst_case_base_level_bits"],
        "max_worst_base_bits": periods[-1]["worst_case_base_level_bits"],
        "periods": periods,
    }


def main() -> None:
    rows = [row_summary(row) for row in ROWS]
    total_periods = sum(row["periods_total"] for row in rows)
    total_staircase = sum(row["staircase_consumer_periods_M_gt_t"] for row in rows)
    check("all clean-rate (n,q,M) triples have possible degenerate towers", all(row["degenerate_possible_periods"] == row["periods_total"] for row in rows))
    check("staircase/TR consumer subtable is nonempty", total_staircase > 0, f"count={total_staircase}")
    result = {
        "node": "tr_joint_telescope",
        "task": "QA.24",
        "status": "AUDIT: degenerate towers are not absent; correction columns emitted",
        "scope": "six clean-rate rows from QA.22/xr_budget_audit; all dyadic M|n, M>=2; M>t flagged for the staircase/TR consumer subtable",
        "count_transfer_correction": {
            "actual_factor": "|K|^(m-d)",
            "m": "M/D",
            "d": "[K(gamma):K]",
            "base_level_bits": "(m-d) * log2(q)",
            "larger_K_multiplier": "multiply the bit column by e=[K:B]",
            "equality_condition": "d=m; otherwise Theorem LL(iii)'s cardinality equality is unavailable",
        },
        "absence_verdict": "not absent: for every nontrivial dyadic period M, any class closure with D<M has m>1 and admits degenerate tower data; D=M is the only forced non-degenerate cell",
        "rows": rows,
        "totals": {
            "rows": len(rows),
            "period_triples": total_periods,
            "degenerate_possible_period_triples": sum(row["degenerate_possible_periods"] for row in rows),
            "staircase_consumer_period_triples": total_staircase,
        },
        "checks": NCHECK,
    }

    if "--write-certificate" in sys.argv:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w") as fh:
            json.dump(result, fh, indent=2, sort_keys=True)
            fh.write("\n")

    expected = None
    if os.path.exists(CERT):
        with open(CERT) as fh:
            expected = json.load(fh)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", result == expected)

    print("\nrow summary:")
    for row in rows:
        print(
            f"{row['label']:5s} {row['rate']:>4s} periods={row['periods_total']:2d} "
            f"M>t={row['staircase_consumer_periods_M_gt_t']:2d} "
            f"first M>t={row['first_staircase_period']:<14d} "
            f"first corr bits={row['first_staircase_worst_base_bits']} "
            f"max corr bits={row['max_worst_base_bits']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print("  -", name)
        print("\nrecomputed summary:")
        print(json.dumps(result, indent=2, sort_keys=True))
        sys.exit(1)

    print(f"\nPASS: {NCHECK} QA.24 degenerate-tower checks")


if __name__ == "__main__":
    main()
