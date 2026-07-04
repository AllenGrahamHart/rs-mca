#!/usr/bin/env python3
"""X30 finite-p norm gate for dyadic terminal trades.

The terminal finite-p residue can be phrased recursively:

  * if the signed first-sum word is divisible by Phi_{2^s}=X^{2^{s-1}}+1,
    the support is antipodal and descends through x -> x^2;
  * otherwise the characteristic p divides the cyclotomic norm/resultant of
    that sparse word.

This verifier checks the coefficient criterion and representative p-specific
quotient examples from the h=4 ledger.  The roadmap note contains the general
proof.
"""

from __future__ import annotations

import json
import os
import sys
from typing import Any

import verify_h1_u1_toy_harness as h1
import verify_x27_h4_large_quotient_sum as x27


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x30-finite-p-norm-gate",
    "x30_finite_p_norm_gate.json",
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


def coeff_word(n: int, pos: tuple[int, ...], neg: tuple[int, ...]) -> list[int]:
    coeffs = [0] * n
    for i in pos:
        coeffs[i % n] += 1
    for i in neg:
        coeffs[i % n] -= 1
    return coeffs


def divisible_by_phi_power_two(coeffs: list[int]) -> bool:
    n = len(coeffs)
    half = n // 2
    return all(coeffs[i] == coeffs[i + half] for i in range(half))


def support_is_antipodal_union(n: int, support: tuple[int, ...]) -> bool:
    half = n // 2
    support_set = set(support)
    return all((i + half) % n in support_set for i in support_set)


def eval_word_mod(coeffs: list[int], root: int, p: int) -> int:
    acc = 0
    power = 1
    for c in coeffs:
        acc = (acc + c * power) % p
        power = (power * root) % p
    return acc


def first_extra_quotient_row(p: int, m: int) -> dict[str, Any]:
    row = x27.quotient_h2_row(p, m)
    for example in row["examples"]:
        if example["reason"] == "extra_antipodal_quotient_lift":
            return {
                "P": tuple(example["P_quotient_exponents"]),
                "Q": tuple(example["Q_quotient_exponents"]),
                "row": row,
            }
    raise AssertionError(f"no extra quotient example for p={p}, m={m}")


def check_descent_criterion(n: int, pos: tuple[int, ...], neg: tuple[int, ...]) -> dict[str, Any]:
    coeffs = coeff_word(n, pos, neg)
    divisible = divisible_by_phi_power_two(coeffs)
    pos_antipodal = support_is_antipodal_union(n, pos)
    neg_antipodal = support_is_antipodal_union(n, neg)
    check(
        f"n={n}: Phi divisibility matches antipodal support union",
        divisible == (pos_antipodal and neg_antipodal),
        f"divisible={divisible}, pos={pos_antipodal}, neg={neg_antipodal}",
    )
    return {
        "n": n,
        "positive_exponents": list(pos),
        "negative_exponents": list(neg),
        "phi_divisible": divisible,
        "positive_antipodal_union": pos_antipodal,
        "negative_antipodal_union": neg_antipodal,
    }


def check_norm_gate_example(p: int, m: int) -> dict[str, Any]:
    extra = first_extra_quotient_row(p, m)
    pos = extra["P"]
    neg = extra["Q"]
    coeffs = coeff_word(m, pos, neg)
    domain = h1.mu_domain(p, m)
    root = domain[1]
    value = eval_word_mod(coeffs, root, p)
    phi_divisible = divisible_by_phi_power_two(coeffs)
    check(f"m={m}, p={p}: extra quotient word vanishes at primitive root", value == 0)
    check(f"m={m}, p={p}: extra quotient word is not characteristic-zero descended", not phi_divisible)
    check(
        f"m={m}, p={p}: p is a norm-gate prime for the sparse word",
        value == 0 and not phi_divisible,
    )
    return {
        "m": m,
        "p": p,
        "positive_exponents": list(pos),
        "negative_exponents": list(neg),
        "word_value_at_primitive_root_mod_p": value,
        "phi_divisible_over_Z": phi_divisible,
        "extra_count_in_row": extra["row"]["extra_antipodal_quotient_lifts"],
    }


def check_zero_sum_descended_example(m: int) -> dict[str, Any]:
    pos = (0, m // 2)
    neg = (1, 1 + m // 2)
    coeffs = coeff_word(m, pos, neg)
    descended = divisible_by_phi_power_two(coeffs)
    check(f"m={m}: zero-sum quotient word is Phi-divisible", descended)
    return {
        "m": m,
        "positive_exponents": list(pos),
        "negative_exponents": list(neg),
        "phi_divisible_over_Z": descended,
    }


def build_certificate() -> dict[str, Any]:
    descent_rows = [
        check_descent_criterion(16, (0, 8, 3, 11), (1, 9, 4, 12)),
        check_descent_criterion(16, (0, 3, 8, 11), (1, 4, 9, 12)),
        check_descent_criterion(16, (0, 2, 5), (1, 3, 6)),
        check_descent_criterion(32, (0, 16, 7, 23, 8, 24), (2, 18, 11, 27, 12, 28)),
    ]
    odd_h_rows = []
    for h in (3, 5, 7, 9):
        possible = h % 2 == 0
        check(f"h={h}: antipodal descent requires even support size", not possible)
        odd_h_rows.append({"h": h, "can_be_antipodal_union": possible})

    norm_gate_rows = [
        check_norm_gate_example(4993, 32),
        check_norm_gate_example(65537, 64),
        check_norm_gate_example(65537, 128),
    ]
    zero_sum_rows = [check_zero_sum_descended_example(m) for m in (16, 32, 64, 128)]
    check("all norm-gate examples are non-descended", all(not row["phi_divisible_over_Z"] for row in norm_gate_rows))
    check("all zero-sum examples are descended", all(row["phi_divisible_over_Z"] for row in zero_sum_rows))
    return {
        "task": "X30 finite-p norm gate",
        "node": "active_core_count_bound",
        "status": (
            "PROVED REDUCTION: finite-p terminal trades either follow dyadic "
            "descent or trigger a sparse cyclotomic norm prime"
        ),
        "theorem": (
            "Let n=2^s and let f be the signed first-sum word of a finite-field "
            "trade in mu_n.  If Phi_n does not divide f over Z, then the "
            "characteristic divides Res(Phi_n,f).  If Phi_n divides f, the "
            "positive and negative supports are antipodal unions and the trade "
            "descends through x -> x^2.  Iterate until a norm gate triggers or "
            "the characteristic-zero dyadic classification applies."
        ),
        "descent_rows": descent_rows,
        "odd_h_rows": odd_h_rows,
        "norm_gate_rows": norm_gate_rows,
        "zero_sum_rows": zero_sum_rows,
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

    print("\nnorm-gate rows:")
    for row in cert["norm_gate_rows"]:
        print(
            f"m={row['m']:<4d} p={row['p']:<8d} "
            f"P={row['positive_exponents']} Q={row['negative_exponents']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X30 finite-p norm-gate checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
