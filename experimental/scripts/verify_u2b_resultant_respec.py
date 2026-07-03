#!/usr/bin/env python3
"""U2-B-RESPEC verifier: low-memory resultant-route contract.

This does not pretend to close U2-B.  It pins the certifier interface after
U2-A's window split:

* prize rows have empty small-block windows, so no U2-B small-row certificate
  is needed there;
* Row-C-class rows are the only live U2-B rows, but the current budget packet
  treats their prime as unpinned;
* raw pattern enumeration through b<=20 (let alone b<=100) is already too
  large, so the resultant checker must consume a proved finite normal-form
  pattern list, not all subsets;
* the characteristic-zero/resultant divisibility kernel is executable by
  reducing the common syndrome ideal modulo the row prime.

Run:
  python3 experimental/scripts/verify_u2b_resultant_respec.py
Refresh certificate:
  python3 experimental/scripts/verify_u2b_resultant_respec.py --write-certificate
"""

from __future__ import annotations

import json
import math
import os
import sys
from typing import Any


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
U2A_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "u2a-window-split",
    "u2a_window_split.json",
)
XR_BUDGET = os.path.join(
    REPO,
    "experimental",
    "notes",
    "roadmaps",
    "xr_budget_audit.md",
)
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "u2b-resultant-respec",
    "u2b_resultant_respec.json",
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


def load_json(path: str) -> dict[str, Any]:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def bit_length_summary(value: int) -> dict[str, Any]:
    return {
        "bit_length": value.bit_length(),
        "log2_floor": value.bit_length() - 1 if value else None,
        "decimal_digits": len(str(value)),
    }


def subset_count(n: int, b_values: list[int]) -> int:
    return sum(math.comb(n, b) for b in b_values)


def orbit_lower_bound(raw_count: int, n: int) -> int:
    # Dihedral orbits have size at most 2n, so this is a lower bound on the
    # number of normal forms any raw-subset exhaustive pass would still face.
    return (raw_count + 2 * n - 1) // (2 * n)


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_mod_from_exponents(n: int, exponents: list[int], r: int, p: int) -> list[int]:
    coeffs = [0] * n
    for exponent in exponents:
        coeffs[(r * exponent) % n] = (coeffs[(r * exponent) % n] + 1) % p
    return trim(coeffs)


def cyclotomic_2power_mod(n: int, p: int) -> list[int]:
    assert n > 1 and n & (n - 1) == 0
    coeffs = [0] * (n // 2 + 1)
    coeffs[0] = 1 % p
    coeffs[n // 2] = 1 % p
    return coeffs


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


def common_syndrome_gcd_degree(n: int, p: int, exponents: list[int], t: int) -> int:
    common = cyclotomic_2power_mod(n, p)
    for r in range(1, t + 1):
        syndrome_poly = poly_mod_from_exponents(n, exponents, r, p)
        common = poly_gcd_mod(common, syndrome_poly, p)
    return len(common) - 1


def resultant_kernel_demo() -> dict[str, Any]:
    exponents = [0, 1, 2, 4, 16, 45, 50, 60]
    p_hit = 193
    p_clean = 641
    return {
        "row": "toy F_193/mu_64 witness pattern",
        "n": 64,
        "t": 3,
        "exponents": exponents,
        "hit_prime": p_hit,
        "hit_common_gcd_degree": common_syndrome_gcd_degree(64, p_hit, exponents, 3),
        "clean_prime": p_clean,
        "clean_common_gcd_degree": common_syndrome_gcd_degree(64, p_clean, exponents, 3),
        "interpretation": (
            "positive common gcd degree means the prime divides the common "
            "resultant/norm obstruction for this pattern; degree zero rules "
            "the pattern out at that prime"
        ),
    }


def row_has_pinned_prime(row: dict[str, Any]) -> bool:
    prime_keys = {"p", "prime", "row_prime", "field_prime", "characteristic"}
    return any(key in row for key in prime_keys)


def build_certificate() -> dict[str, Any]:
    u2a = load_json(U2A_CERT)
    budget_text = open(XR_BUDGET, encoding="utf-8").read().lower()
    rowc_unpinned = "row c prime unpinned" in budget_text or "prime unpinned" in budget_text

    live = list(u2a["u2b_base_row_live_cells"])
    rows_by_id = {row["row_id"]: row for row in u2a["rows"]}
    prize_empty = list(u2a["prize_rows_with_empty_small_window"])

    check("U2-A certificate exists and is consumed", os.path.exists(U2A_CERT), U2A_CERT)
    check("U2-B live base rows are exactly Row-C-class", len(live) == 3)
    check("prize rows have empty U2-B small window", len(prize_empty) == 3)
    check("xr_budget_audit flags Row-C prime as unpinned", rowc_unpinned)

    row_records = []
    for cell in live:
        row_id = cell["row_id"]
        row = rows_by_id[row_id]
        b_values = list(cell["b_values"])
        stage1_values = [b for b in b_values if b <= 20]
        stage2_values = b_values
        stage1_raw = subset_count(int(cell["n"]), stage1_values)
        stage2_raw = subset_count(int(cell["n"]), stage2_values)
        stage1_orbit_lb = orbit_lower_bound(stage1_raw, int(cell["n"]))
        stage2_orbit_lb = orbit_lower_bound(stage2_raw, int(cell["n"]))
        pinned = row_has_pinned_prime(row)
        check(f"{row_id}: no pinned row prime in U2-A row record", not pinned)
        check(
            f"{row_id}: raw stage-1 subset enumeration is not a low-memory route",
            stage1_orbit_lb.bit_length() > 80,
            f"log2 orbit-lb ~= {stage1_orbit_lb.bit_length() - 1}",
        )
        row_records.append(
            {
                "row_id": row_id,
                "n": int(cell["n"]),
                "t": int(row["t"]),
                "base_window": {
                    "start": min(b_values),
                    "end": max(b_values),
                    "count": len(b_values),
                },
                "pinned_prime_available": pinned,
                "row_prime_status": "unpinned_in_current_certificates",
                "stage1_b_le_20": {
                    "b_values": stage1_values,
                    "raw_subset_count": bit_length_summary(stage1_raw),
                    "dihedral_orbit_lower_bound": bit_length_summary(stage1_orbit_lb),
                },
                "stage2_b_le_grammar_max": {
                    "b_values_start": min(stage2_values),
                    "b_values_end": max(stage2_values),
                    "raw_subset_count": bit_length_summary(stage2_raw),
                    "dihedral_orbit_lower_bound": bit_length_summary(stage2_orbit_lb),
                },
                "required_next_input": (
                    "pin the row characteristic/prime and provide a proved finite "
                    "normal-form sparse-relation pattern list; the resultant "
                    "kernel can then check p-divisibility pattern-by-pattern"
                ),
            }
        )

    demo = resultant_kernel_demo()
    check("resultant kernel detects the F193 witness pattern", demo["hit_common_gcd_degree"] > 0)
    check("resultant kernel rejects the same pattern at p=641", demo["clean_common_gcd_degree"] == 0)

    return {
        "task": "U2-B-RESPEC resultant-route contract",
        "node": "u2_per_row_certifier",
        "status": "RESPEC: Row-C live cells identified, but per-row certificates require pinned primes plus compressed pattern generation",
        "source": "u2a_window_split.json + xr_budget_audit.md",
        "prize_small_window": {
            "empty_rows": prize_empty,
            "verdict": "no U2-B small-block certificate needed at prize rows",
        },
        "rowc_prime_status": "unpinned" if rowc_unpinned else "not_detected",
        "rowc_live_rows": row_records,
        "resultant_kernel_demo": demo,
        "certifier_contract": {
            "input": [
                "row characteristic p",
                "n, t",
                "finite normal-form list of exponent patterns E with t < |E| <= floor(log2 n)^2",
                "coverage proof that the list exhausts primitive patterns not already charged",
            ],
            "per_pattern_check": (
                "compute gcd(Phi_n, sum_{e in E} X^{r e}) over F_p for r=1..t; "
                "degree zero rules out that sparse-relation pattern at the row prime"
            ),
            "fail_closed_rule": (
                "without a pinned row prime and an exhaustive compressed pattern "
                "list, U2-B remains TARGET and must not be reported as certified"
            ),
        },
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
        with open(CERT, encoding="utf-8") as fh:
            expected = json.load(fh)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", cert == expected)

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        print("\nrecomputed certificate:")
        print(json.dumps(cert, indent=2, sort_keys=True))
        return 1

    print("\nsummary:")
    print(
        json.dumps(
            {
                "prize_small_window": cert["prize_small_window"],
                "rowc_prime_status": cert["rowc_prime_status"],
                "rowc_live_rows": [
                    {
                        "row_id": row["row_id"],
                        "window": row["base_window"],
                        "stage1_orbit_lb_log2_floor": row["stage1_b_le_20"]["dihedral_orbit_lower_bound"]["log2_floor"],
                        "stage2_orbit_lb_log2_floor": row["stage2_b_le_grammar_max"]["dihedral_orbit_lower_bound"]["log2_floor"],
                    }
                    for row in cert["rowc_live_rows"]
                ],
                "demo": cert["resultant_kernel_demo"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    print(f"\nPASS: {NCHECK} U2-B-RESPEC checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

