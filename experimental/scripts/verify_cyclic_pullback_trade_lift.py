#!/usr/bin/env python3
"""Verifier for the cyclic pullback trade-lift lemma.

The lemma says that if a support is a union of fibers of the cyclic quotient
mu_n -> mu_{n/g}, then its locator is the quotient locator evaluated at X^g.
Thus same-top split-pair collisions lift and descend exactly through the
cyclic quotient.  The roadmap note contains the proof; this verifier checks
representative 2-power cases, including the X14 boundary shape g=2,s=2.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
import json
import os
import sys
from typing import Any

import verify_h1_u1_toy_harness as h1
import verify_x12_h3_active_core_census as h3


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "cyclic-pullback-trade-lift",
    "cyclic_pullback_trade_lift.json",
)

FAILS: list[str] = []
NCHECK = 0


@dataclass(frozen=True)
class Case:
    n: int
    g: int
    s: int


CASES = (
    Case(16, 4, 1),
    Case(32, 8, 1),
    Case(32, 4, 2),
    Case(64, 4, 2),
    Case(64, 2, 3),
    Case(128, 2, 2),
)


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


def quiet_check(name: str, cond: bool, detail: str = "") -> None:
    global NCHECK
    NCHECK += 1
    if not cond:
        line = name
        if detail:
            line += f" ({detail})"
        FAILS.append(line)


def first_prime_1_mod_n_after(n: int, floor: int) -> int:
    p = floor + 1
    p += (1 - p) % n
    while not h3.is_prime(p):
        p += n
    return p


def poly_mul_linear(poly: list[int], root: int, p: int) -> list[int]:
    out = [0] * (len(poly) + 1)
    for i, c in enumerate(poly):
        out[i] = (out[i] - c * root) % p
        out[i + 1] = (out[i + 1] + c) % p
    return out


def locator_from_values(values: list[int], p: int) -> list[int]:
    poly = [1]
    for value in values:
        poly = poly_mul_linear(poly, value, p)
    return poly


def compose_xg(poly: list[int], g: int) -> list[int]:
    out = [0] * (g * (len(poly) - 1) + 1)
    for i, c in enumerate(poly):
        out[g * i] = c
    return out


def top_signature(poly: list[int], degree: int) -> tuple[int, ...]:
    # poly is in increasing powers.  Monic degree-d locator has top symmetric
    # data in coefficients degree d-1 down to 1.
    return tuple(poly[degree - i] for i in range(1, degree))


def fiber_exponents(n: int, g: int, residue: int) -> list[int]:
    step = n // g
    return [residue + step * j for j in range(g)]


def analyze_case(case: Case) -> dict[str, Any]:
    n, g, s = case.n, case.g, case.s
    assert n % g == 0
    quotient_n = n // g
    p = first_prime_1_mod_n_after(n, n * n)
    domain = h1.mu_domain(p, n)

    quotient_values = [pow(domain[r], g, p) for r in range(quotient_n)]
    quotient_signatures: dict[tuple[int, ...], int] = {}
    full_signatures: dict[tuple[int, ...], int] = {}
    checked_subsets = 0
    zero_gap_coefficients = 0

    for residues in combinations(range(quotient_n), s):
        quotient_roots = [quotient_values[r] for r in residues]
        quotient_locator = locator_from_values(quotient_roots, p)

        full_roots = []
        for r in residues:
            full_roots.extend(domain[e] for e in fiber_exponents(n, g, r))
        full_locator = locator_from_values(full_roots, p)
        lifted_locator = compose_xg(quotient_locator, g)

        checked_subsets += 1
        quiet_check(
            f"n={n}, g={g}, s={s}, subset={checked_subsets}: L_full = L_quot(X^g)",
            full_locator == lifted_locator,
        )

        for degree, coeff in enumerate(full_locator):
            if degree % g != 0 and coeff == 0:
                zero_gap_coefficients += 1

        q_sig = top_signature(quotient_locator, s)
        f_sig = top_signature(full_locator, g * s)
        quotient_signatures[q_sig] = quotient_signatures.get(q_sig, 0) + 1
        full_signatures[f_sig] = full_signatures.get(f_sig, 0) + 1

    quotient_hist = sorted(quotient_signatures.values())
    full_hist = sorted(full_signatures.values())
    check(
        f"n={n}, g={g}, s={s}: same-top groups lift bijectively",
        quotient_hist == full_hist,
        f"groups={len(full_hist)}",
    )
    check(
        f"n={n}, g={g}, s={s}: sampled quotient has expected size",
        len(quotient_values) == quotient_n and len(set(quotient_values)) == quotient_n,
        f"quotient_n={quotient_n}",
    )

    return {
        "n": n,
        "g": g,
        "s": s,
        "h": g * s,
        "quotient_n": quotient_n,
        "p": p,
        "subsets_checked": checked_subsets,
        "quotient_signature_groups": len(quotient_hist),
        "full_signature_groups": len(full_hist),
        "max_group_size": max(full_hist) if full_hist else 0,
        "zero_gap_coefficients_seen": zero_gap_coefficients,
    }


def build_certificate() -> dict[str, Any]:
    cases = [analyze_case(case) for case in CASES]
    check("certificate includes full-fiber X19 shape n=32,g=8,s=1", any(c["n"] == 32 and c["g"] == 8 and c["s"] == 1 for c in cases))
    check("certificate includes X14 boundary shape n=128,g=2,s=2", any(c["n"] == 128 and c["g"] == 2 and c["s"] == 2 for c in cases))
    return {
        "task": "cyclic pullback trade-lift lemma",
        "node": "cyclic_pullback_trade_lift",
        "status": "PROVED algebraic lemma; verifier sanity-checks representative rows",
        "statement": (
            "For H=mu_n and g|n, any support that is a union of g-point cyclic "
            "fibers has locator L_C(X^g), where C is the quotient support in "
            "mu_{n/g}. Therefore same-top split-pair collisions lift and descend "
            "exactly through the cyclic quotient and are cyclic-pullback paid."
        ),
        "cases": cases,
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
        for fail in FAILS:
            print(f"  - {fail}")
        return 1
    print(f"\nPASS: {NCHECK} cyclic-pullback trade-lift checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
