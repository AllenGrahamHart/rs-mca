#!/usr/bin/env python3
"""Verifier for the cyclic full-fiber collision lemma.

The proof is algebraic and lives in the roadmap note.  This script checks the
coefficient identity on representative 2-power rows and writes a compact
certificate: every full fiber of x -> x^h on mu_n has locator X^h - a, hence
zero top-(h-1) elementary-symmetric signature and cyclic-paid collisions.
"""

from __future__ import annotations

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
    "cyclic-fiber-collision-lemma",
    "cyclic_fiber_collision_lemma.json",
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


def locator_coeffs(roots: list[int], p: int) -> list[int]:
    poly = [1]
    for root in roots:
        poly = poly_mul_linear(poly, root, p)
    return poly


def analyze(n: int, h: int) -> dict[str, Any]:
    assert n % h == 0
    p = first_prime_1_mod_n_after(n, n * n)
    domain = h1.mu_domain(p, n)
    step = n // h
    coset_count = step
    zero_top_signature_cosets = 0
    expected_constants: list[int] = []

    for r in range(step):
        exponents = [r + step * k for k in range(h)]
        roots = [domain[e] for e in exponents]
        coeffs = locator_coeffs(roots, p)
        expected = [0] * (h + 1)
        expected[0] = (-pow(domain[r], h, p)) % p
        expected[h] = 1
        ok = coeffs == expected
        check(
            f"n={n}, h={h}, coset={r}: locator is X^h - zeta^(rh)",
            ok,
            f"p={p}",
        )
        if ok and all(c == 0 for c in coeffs[1:h]):
            zero_top_signature_cosets += 1
        expected_constants.append(expected[0])

    distinct_constants = len(set(expected_constants))
    check(
        f"n={n}, h={h}: coset constants are distinct",
        distinct_constants == coset_count,
        f"distinct={distinct_constants}, cosets={coset_count}",
    )

    return {
        "n": n,
        "h": h,
        "p": p,
        "coset_count": coset_count,
        "zero_top_signature_cosets": zero_top_signature_cosets,
        "anchored_partner_pairs": coset_count - 1,
        "ordered_paid_pairs": coset_count * (coset_count - 1),
        "cyclic_map": f"x^{h}",
    }


def build_certificate() -> dict[str, Any]:
    cases = []
    for n in (8, 16, 32, 64):
        h = 2
        while h < n:
            if n % h == 0:
                cases.append(analyze(n, h))
            h *= 2

    check("sample includes the X19 case n=32,h=8", any(c["n"] == 32 and c["h"] == 8 for c in cases))
    check("every sampled coset has zero top signature", all(c["zero_top_signature_cosets"] == c["coset_count"] for c in cases))

    return {
        "task": "cyclic fiber collision lemma",
        "node": "cyclic_fiber_collision_lemma",
        "status": "PROVED algebraic lemma; verifier sanity-checks representative rows",
        "statement": (
            "If h is a proper divisor of n and H=mu_n, the full fibers of x -> x^h "
            "on H have locators X^h-a. Therefore their top h-1 elementary "
            "symmetric sums vanish, all fiber pairs are same-top-(h-1) collisions, "
            "and all such collisions are cyclic-pullback paid."
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
    print(f"\nPASS: {NCHECK} cyclic-fiber collision lemma checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
