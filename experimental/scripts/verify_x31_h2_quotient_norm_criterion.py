#!/usr/bin/env python3
"""X31 h=2 quotient norm criterion.

Specializes X30 to the quotient h=2 sum-collision layer used by X26-X29.

For m=2^s and an anchored quotient pair collision

    1 + zeta^a = zeta^b + zeta^c,

the zero-sum branch is exactly a Phi_m-descended word.  Every extra collision
has a nonzero sparse resultant Res(Phi_m, 1+X^a-X^b-X^c) divisible by the row
prime.  This verifier computes exact integer resultants for representative
extra rows from the h=4 quotient ledger.
"""

from __future__ import annotations

from collections import Counter
import json
import os
import sys
from typing import Any

import sympy as sp

import verify_h1_u1_toy_harness as h1
import verify_x30_finite_p_norm_gate as x30


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x31-h2-quotient-norm-criterion",
    "x31_h2_quotient_norm_criterion.json",
)

X = sp.symbols("X")
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


def quotient_extra_pairs(p: int, m: int) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    domain = h1.mu_domain(p, m)
    out: list[tuple[tuple[int, int], tuple[int, int]]] = []
    for a in range(1, m):
        p_pair = (0, a)
        target = (domain[0] + domain[a]) % p
        for b in range(m):
            if b in p_pair:
                continue
            for c in range(b + 1, m):
                if c in p_pair:
                    continue
                if (domain[b] + domain[c]) % p != target:
                    continue
                zero_sum = a == m // 2 and (c - b) % m == m // 2
                if not zero_sum:
                    out.append((p_pair, (b, c)))
    return out


def sparse_resultant(m: int, pos: tuple[int, int], neg: tuple[int, int]) -> int:
    f = sum(X**i for i in pos) - sum(X**i for i in neg)
    phi = X ** (m // 2) + 1
    return int(sp.resultant(phi, f, X))


def p_adic_valuation(value: int, p: int) -> int:
    value = abs(value)
    out = 0
    while value and value % p == 0:
        out += 1
        value //= p
    return out


def check_zero_sum_branch(m: int) -> dict[str, Any]:
    baseline = m // 2 - 1
    rows = []
    for b in range(1, m // 2):
        pos = (0, m // 2)
        neg = (b, b + m // 2)
        coeffs = x30.coeff_word(m, pos, neg)
        descended = x30.divisible_by_phi_power_two(coeffs)
        rows.append(descended)
    check(f"m={m}: zero-sum baseline count", len(rows) == baseline)
    check(f"m={m}: every zero-sum baseline word is Phi-descended", all(rows))
    return {
        "m": m,
        "zero_sum_baseline": baseline,
        "all_zero_sum_words_phi_descended": all(rows),
    }


def check_extra_row(p: int, m: int) -> dict[str, Any]:
    pairs = quotient_extra_pairs(p, m)
    bit_lengths: list[int] = []
    valuations = Counter()
    examples: list[dict[str, Any]] = []
    bad: list[dict[str, Any]] = []

    for pos, neg in pairs:
        coeffs = x30.coeff_word(m, pos, neg)
        phi_divisible = x30.divisible_by_phi_power_two(coeffs)
        resultant = sparse_resultant(m, pos, neg)
        divides = resultant % p == 0
        valuation = p_adic_valuation(resultant, p)
        bit_lengths.append(abs(resultant).bit_length())
        valuations[valuation] += 1
        if phi_divisible or not divides:
            bad.append(
                {
                    "P": list(pos),
                    "Q": list(neg),
                    "phi_divisible": phi_divisible,
                    "resultant_mod_p": resultant % p,
                }
            )
        if len(examples) < 8:
            examples.append(
                {
                    "P": list(pos),
                    "Q": list(neg),
                    "resultant": resultant,
                    "resultant_abs_bits": abs(resultant).bit_length(),
                    "p_adic_valuation": valuation,
                }
            )

    check(f"m={m}, p={p}: row has extra quotient collisions", bool(pairs))
    check(f"m={m}, p={p}: every extra word is non-descended and p-norm-gated", not bad)
    return {
        "m": m,
        "p": p,
        "extra_pair_count": len(pairs),
        "resultant_abs_bit_min": min(bit_lengths) if bit_lengths else 0,
        "resultant_abs_bit_max": max(bit_lengths) if bit_lengths else 0,
        "p_adic_valuation_histogram": {str(k): v for k, v in sorted(valuations.items())},
        "examples": examples,
        "bad_examples": bad,
    }


def build_certificate() -> dict[str, Any]:
    zero_sum_rows = [check_zero_sum_branch(m) for m in (8, 16, 32, 64, 128)]
    extra_rows = [
        check_extra_row(4993, 32),
        check_extra_row(65537, 64),
        check_extra_row(65537, 128),
    ]
    check("all zero-sum branches descend", all(row["all_zero_sum_words_phi_descended"] for row in zero_sum_rows))
    check("all extra rows are p-norm-gated", all(not row["bad_examples"] for row in extra_rows))
    return {
        "task": "X31 h=2 quotient norm criterion",
        "node": "active_core_count_bound",
        "status": (
            "PROVED SPECIALIZATION: quotient h=2 extra collisions are sparse "
            "cyclotomic norm gates; zero-sum collisions are the descended baseline"
        ),
        "theorem": (
            "For m=2^s, an anchored quotient h=2 collision "
            "1+zeta^a=zeta^b+zeta^c is either the zero-sum Phi_m-descended "
            "baseline a=m/2, c=b+m/2, or the nonzero sparse resultant "
            "Res(Phi_m,1+X^a-X^b-X^c) is divisible by the characteristic. "
            "Conversely, resultant divisibility gives such a collision after "
            "a Galois exponent scaling of the pattern."
        ),
        "zero_sum_rows": zero_sum_rows,
        "extra_rows": extra_rows,
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

    print("\nextra rows:")
    for row in cert["extra_rows"]:
        print(
            f"m={row['m']:<4d} p={row['p']:<8d} extras={row['extra_pair_count']:<4d} "
            f"bits={row['resultant_abs_bit_min']}..{row['resultant_abs_bit_max']} "
            f"vp={row['p_adic_valuation_histogram']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X31 h=2 quotient norm-criterion checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
