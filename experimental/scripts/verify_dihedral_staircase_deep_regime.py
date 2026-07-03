#!/usr/bin/env python3
"""Verify the dihedral-staircase deep-regime applicability audit.

DAG node: dihedral_staircase.

The companion note proves an exact-support staircase under

    3*j <= n-k   equivalently   t = n-j-k >= 2*j.

This verifier does not mechanize the MDS proof. It freezes the integer
arithmetic around the proof:

* the theorem's overlap inequalities are the advertised ones;
* none of the six QA.21 clean-rate candidates satisfies the hypothesis;
* the Row C "2^174" line has j=957, while 67 is the complementary support
  size, explaining the GPT-Pro j/complement slip;
* when the deep theorem does apply, the n+1 support bound gives the claimed
  Row C suppression scale.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any

PASS: list[str] = []
FAIL: list[str] = []

CERT_PATH = Path(
    "experimental/data/certificates/dihedral-staircase-deep/"
    "dihedral_staircase_deep_regime_certificate.json"
)


def check(label: str, ok: bool, detail: str = "") -> None:
    (PASS if ok else FAIL).append(label)
    tag = "PASS" if ok else "FAIL"
    print(f"{tag}  {label}" + (f"  [{detail}]" if detail else ""))


def log2_big(x: int) -> float:
    if x <= 0:
        raise ValueError("positive integer expected")
    bits = x.bit_length()
    if bits <= 53:
        return math.log2(x)
    return (bits - 53) + math.log2(x >> (bits - 53))


def n_dih_exact(n: int, j: int) -> int:
    """Odd-j inversion-closed support universe from QA.21."""
    if n % 2 != 0 or j % 2 != 1:
        raise ValueError("this packet expects even n and odd j")
    return 2 * math.comb((n - 2) // 2, (j - 1) // 2)


ROWS = [
    {"row": "RowC", "rate": "1/4", "n": 1024, "k": 256, "A": 261},
    {"row": "RowC", "rate": "1/8", "n": 1024, "k": 128, "A": 133},
    {"row": "RowC", "rate": "1/16", "n": 1024, "k": 64, "A": 67},
    {"row": "prize", "rate": "1/4", "n": 1 << 41, "k": 1 << 39, "A": 558345748481},
    {"row": "prize", "rate": "1/8", "n": 1 << 41, "k": 1 << 38, "A": 283467841537},
    {"row": "prize", "rate": "1/16", "n": 1 << 41, "k": 1 << 37, "A": 141733920769},
]


def enrich_row(row: dict[str, Any]) -> dict[str, Any]:
    n, k, a = row["n"], row["k"], row["A"]
    j = n - a
    t = a - k
    deep = k + 3 * j <= n
    same_slope_unique = k + 2 * j <= n
    comp_j = n - j
    comp_deep = k + 3 * comp_j <= n
    out = {
        **row,
        "j": j,
        "t": t,
        "same_slope_unique_condition_k_plus_2j_le_n": same_slope_unique,
        "deep_staircase_condition_k_plus_3j_le_n": deep,
        "condition_defect_k_plus_3j_minus_n": k + 3 * j - n,
        "complement_support_size": comp_j,
        "complement_deep_condition_k_plus_3A_le_n": comp_deep,
    }
    if row["row"] == "RowC":
        ndih = n_dih_exact(n, j)
        ndih_comp = n_dih_exact(n, comp_j)
        out.update(
            {
                "N_dih_exact": ndih,
                "N_dih_log2": round(log2_big(ndih), 12),
                "N_dih_equals_complement_count": ndih == ndih_comp,
                "suppression_if_deep_applied_bits": round(log2_big(ndih) - math.log2(n + 1), 12),
            }
        )
    return out


def build_certificate() -> dict[str, Any]:
    rows = [enrich_row(row) for row in ROWS]
    return {
        "dag_node": "dihedral_staircase",
        "status": "PROVED in the deep regime; not applicable to QA.21 clean-rate candidates",
        "theorem": {
            "hypothesis": "3*j <= n-k, where j is exact disagreement-support size",
            "finite_slope_bound": "at most n+1 aligned exact j-supports of any kind",
            "projective_slope_bound": "at most n+2 if the slope at infinity is included",
        },
        "clean_rate_rows": rows,
        "correction": (
            "The RowC 1/16 crude count near 2^174 occurs at clean candidate A=67, "
            "j=n-A=957. The number 67 is the complementary support size, not the "
            "QA.21 disagreement support j."
        ),
        "outside_regime_obstruction": "Chebyshev quotient RS list problem at quotient excess about t/2",
    }


def verify_certificate(cert: dict[str, Any]) -> None:
    rows = cert["clean_rate_rows"]
    check("six QA.21 clean-rate rows emitted", len(rows) == 6)
    for row in rows:
        tag = f"{row['row']} {row['rate']}"
        n, k, j, t = row["n"], row["k"], row["j"], row["t"]
        check(f"{tag}: t definition matches n-j-k", t == n - j - k)
        check(
            f"{tag}: same-slope uniqueness condition equivalence",
            (t >= j) == (k + 2 * j <= n) == row["same_slope_unique_condition_k_plus_2j_le_n"],
        )
        check(
            f"{tag}: deep staircase condition equivalence",
            (t >= 2 * j) == (k + 3 * j <= n) == row["deep_staircase_condition_k_plus_3j_le_n"],
        )
        check(
            f"{tag}: QA.21 clean candidate is outside the deep-staircase theorem",
            not row["deep_staircase_condition_k_plus_3j_le_n"],
            f"k+3j-n={row['condition_defect_k_plus_3j_minus_n']}",
        )
        if row["row"] == "RowC":
            check(
                f"{tag}: N_dih(j) equals N_dih(complement j)",
                row["N_dih_equals_complement_count"],
                f"log2 N_dih={row['N_dih_log2']}",
            )
            check(
                f"{tag}: if the deep theorem applied, n+1 would give strong suppression",
                row["suppression_if_deep_applied_bits"] > 40,
                f"{row['suppression_if_deep_applied_bits']} bits",
            )

    tight = next(row for row in rows if row["row"] == "RowC" and row["rate"] == "1/16")
    check("tight RowC line has clean candidate j=957", tight["j"] == 957)
    check("tight RowC line has complementary support size 67", tight["complement_support_size"] == 67)
    check("tight RowC target condition fails", tight["condition_defect_k_plus_3j_minus_n"] == 1911)
    check("tight RowC complementary deep row would satisfy the theorem", tight["complement_deep_condition_k_plus_3A_le_n"])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-certificate", action="store_true")
    args = parser.parse_args()

    cert = build_certificate()
    if args.write_certificate:
        CERT_PATH.parent.mkdir(parents=True, exist_ok=True)
        CERT_PATH.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
        print(f"wrote {CERT_PATH}")
    else:
        if CERT_PATH.exists():
            checked = json.loads(CERT_PATH.read_text())
            check("checked-in JSON certificate matches deterministic build", checked == cert)
        else:
            check("checked-in JSON certificate exists", False, str(CERT_PATH))

    verify_certificate(cert)

    print()
    print("row     rate  A              j              t          k+3j-n")
    for row in cert["clean_rate_rows"]:
        print(
            f"{row['row']:<7} {row['rate']:<5} {row['A']:<14} "
            f"{row['j']:<14} {row['t']:<10} {row['condition_defect_k_plus_3j_minus_n']}"
        )
    print()
    print(f"{len(PASS)} PASS, {len(FAIL)} FAIL")
    return 0 if not FAIL else 1


if __name__ == "__main__":
    sys.exit(main())
