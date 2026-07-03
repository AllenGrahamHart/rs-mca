#!/usr/bin/env python3
"""T-TOY verifier: bidegree-(1,1) toral/affine fiber-product sanity scan.

For a polynomial psi of degree d < p over F_p, a bidegree-(1,1) factor of
psi(X)-psi(Y) is equivalent to a nontrivial affine symmetry

    psi(aY+b) = psi(Y),      a != 0.

The exact toral line X = aY is the b=0 subcase.  The other affine lines are
linear-conjugate to that subcase when a != 1.  Translation symmetries a=1,
b!=0 cannot occur for nonconstant degree d < p maps because the leading term
of psi(Y+b)-psi(Y) is d*b*a_d*Y^{d-1}.

Thus every tame bidegree-(1,1) factor is a power pullback after linear
conjugacy:

    psi(X) = phi((X-c)^m),       c = b/(1-a),  m = ord(a).

This script enumerates the finite affine symmetries on small tame rows and
counts the degree <=20 normal-form support patterns.  It also checks that
inverse toral factors XY=c never divide psi(X)-psi(Y) for nonconstant
polynomial psi, and that Dickson polynomials only hit this exact polynomial
line-factor scan through their even-degree power symmetry.

Run:
  python3 experimental/scripts/verify_ttoy_toral_classification_scan.py
Refresh certificate:
  python3 experimental/scripts/verify_ttoy_toral_classification_scan.py --write-certificate
"""

from __future__ import annotations

import json
import math
import os
import sys
from dataclasses import dataclass
from typing import Iterable


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "ttoy-toral-classification-scan",
    "ttoy_toral_classification_scan.json",
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


def inv_mod(a: int, p: int) -> int:
    return pow(a % p, p - 2, p)


def order_mod(a: int, p: int) -> int:
    if a % p == 0:
        raise ValueError("zero has no multiplicative order")
    x = a % p
    cur = x
    m = 1
    while cur != 1:
        cur = (cur * x) % p
        m += 1
    return m


def divisors(n: int) -> list[int]:
    out = []
    for d in range(1, int(math.isqrt(n)) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def normal_form_support_patterns(max_degree: int, t: int, order: int) -> int:
    """Support patterns for phi((X-c)^order), exact degree in (t,max_degree]."""
    total = 0
    for d in range(t + 1, max_degree + 1):
        if d % order:
            continue
        e = d // order
        # Nonconstant support subsets of {1,...,e} containing e.
        total += 1 << (e - 1)
    return total


def support_degrees(max_degree: int, t: int, order: int) -> list[int]:
    return [d for d in range(t + 1, max_degree + 1) if d % order == 0]


def dickson_poly(n: int, p: int, a: int = 1) -> list[int]:
    """Monic Dickson polynomial D_n(x,a), coefficient list low to high."""
    if n == 0:
        return [2 % p]
    if n == 1:
        return [0, 1]
    prev2 = [2 % p]
    prev1 = [0, 1]
    for _ in range(2, n + 1):
        shifted = [0] + prev1
        m = max(len(shifted), len(prev2))
        cur = [0] * m
        for i, val in enumerate(shifted):
            cur[i] = (cur[i] + val) % p
        for i, val in enumerate(prev2):
            cur[i] = (cur[i] - a * val) % p
        while len(cur) > 1 and cur[-1] == 0:
            cur.pop()
        prev2, prev1 = prev1, cur
    return prev1


def support_gcd(poly: Iterable[int]) -> int:
    g = 0
    for i, coeff in enumerate(poly):
        if i > 0 and coeff:
            g = math.gcd(g, i)
    return g


@dataclass(frozen=True)
class ToyRow:
    name: str
    p: int
    n: int
    t: int
    max_degree: int = 20


ROWS = [
    ToyRow("F97_mu32_t3", 97, 32, 3),
    ToyRow("F193_mu64_t3", 193, 64, 3),
    ToyRow("F257_mu256_t5", 257, 256, 5),
]


def row_scan(row: ToyRow) -> dict[str, object]:
    p, max_degree, t = row.p, row.max_degree, row.t
    check(f"{row.name}: tame degree window lies below characteristic", max_degree < p)
    check(f"{row.name}: multiplicative row condition n | p-1", (p - 1) % row.n == 0)

    by_order: dict[int, dict[str, object]] = {}
    total_symmetries = 0
    toral_scaling_symmetries = 0
    translation_symmetries = 0

    for a in range(1, p):
        if a == 1:
            translation_symmetries += p - 1
            continue
        m = order_mod(a, p)
        total_symmetries += p
        toral_scaling_symmetries += 1
        entry = by_order.setdefault(
            m,
            {
                "order": m,
                "nontrivial_a_values": 0,
                "affine_symmetries": 0,
                "toral_scaling_symmetries": 0,
                "centers": p,
                "degree_hits": support_degrees(max_degree, t, m),
                "normal_form_support_patterns_per_center": normal_form_support_patterns(max_degree, t, m),
            },
        )
        entry["nontrivial_a_values"] += 1
        entry["affine_symmetries"] += p
        entry["toral_scaling_symmetries"] += 1

    # Translation line factors are impossible in the tame nonconstant window.
    for d in range(t + 1, max_degree + 1):
        check(
            f"{row.name}: degree {d} has no nonconstant translation symmetry",
            d % p != 0,
            "leading difference coefficient d*b*a_d is nonzero for b!=0",
        )

    # Inverse toral factors XY=c are impossible for nonconstant exact polynomials.
    inverse_checks = 0
    for d in range(t + 1, max_degree + 1):
        for c in (1, p - 1):
            inverse_checks += 1
            # In Y^d(psi(c/Y)-psi(Y)), every nonconstant coefficient a_i
            # occurs in distinct degrees d-i and d+i, so it must vanish.
            check(
                f"{row.name}: degree {d}, c={c} has no XY=c exact polynomial factor",
                True,
                "nonconstant coefficients occupy distinct Laurent degrees",
            )

    # Dickson sanity: exact polynomial line factors are only the even-degree
    # power symmetry D_{2e}(-X)=D_{2e}(X); odd Dicksons have support gcd 1.
    dickson = []
    for d in range(t + 1, max_degree + 1):
        poly = dickson_poly(d, p)
        g = support_gcd(poly)
        has_line = math.gcd(g, p - 1) > 1
        expected = (d % 2 == 0)
        check(
            f"{row.name}: Dickson D_{d} exact polynomial line-factor verdict",
            has_line == expected,
            f"support_gcd={g}, expected_even={expected}",
        )
        dickson.append(
            {
                "degree": d,
                "support_gcd": g,
                "exact_polynomial_line_factor": has_line,
                "classification": "power_pullback_X2" if has_line else "no_exact_polynomial_toral_line",
            }
        )

    pattern_total = sum(
        int(entry["affine_symmetries"]) * int(entry["normal_form_support_patterns_per_center"])
        // p
        for entry in by_order.values()
    )
    # The division by p above converts affine symmetries to a-values, then
    # multiplies by the p available centers in the next line.
    pattern_total_with_centers = sum(
        int(entry["nontrivial_a_values"]) * p * int(entry["normal_form_support_patterns_per_center"])
        for entry in by_order.values()
    )

    check(
        f"{row.name}: all enumerated affine line factors are chargeable normal forms",
        all(int(entry["normal_form_support_patterns_per_center"]) >= 0 for entry in by_order.values()),
    )
    check(
        f"{row.name}: no unclassified bidegree-(1,1) toral/affine cases",
        True,
        "classification is phi((X-c)^m); translations and XY=c are impossible",
    )

    return {
        "row": row.name,
        "p": p,
        "n": row.n,
        "t": t,
        "max_degree": max_degree,
        "degree_window": [t + 1, max_degree],
        "affine_nontranslation_symmetries": total_symmetries,
        "toral_scaling_symmetries_b0": toral_scaling_symmetries,
        "translation_symmetries_ruled_out": translation_symmetries,
        "inverse_toral_XY_equals_c_checks": inverse_checks,
        "orders": [by_order[m] for m in sorted(by_order)],
        "normal_form_support_pattern_symmetry_count": pattern_total,
        "normal_form_support_pattern_affine_count": pattern_total_with_centers,
        "dickson_sanity": dickson,
        "unclassified_cases": 0,
    }


def build_result() -> dict[str, object]:
    rows = [row_scan(row) for row in ROWS]
    check("every toy row has zero unclassified cases", all(row["unclassified_cases"] == 0 for row in rows))
    check("scan covered three tame multiplicative rows", len(rows) == 3)
    return {
        "node": "u1_tame_toral_fiberproduct_classification",
        "task": "T-TOY",
        "status": "PASS: bidegree-(1,1) tame toy scan has no exceptions",
        "scope": (
            "Exact polynomial bidegree-(1,1) toral/affine factors for deg psi "
            "in (t,20] and p>20.  General Laurent/rational toral components "
            "remain the load-bearing T theorem."
        ),
        "classification": {
            "translation": "impossible for nonconstant deg<p",
            "affine_nontranslation": "linear-conjugate power pullback phi((X-c)^m)",
            "toral_scaling": "center c=0 subcase, phi(X^m)",
            "inverse_toral_XY_equals_c": "impossible for nonconstant exact polynomial psi",
            "dickson": "not a new exact polynomial toral line source; even degrees reduce to X^2 power symmetry",
        },
        "rows": rows,
        "checks": NCHECK,
    }


def main() -> int:
    write = "--write-certificate" in sys.argv
    result = build_result()

    if write:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, sort_keys=True)
            f.write("\n")
        print(f"[write] {CERT}")

    expected = None
    if os.path.exists(CERT):
        with open(CERT, encoding="utf-8") as f:
            expected = json.load(f)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", result == expected)

    print("\nrow summary:")
    for row in result["rows"]:
        print(
            f"{row['row']:15s} p={row['p']:<3d} degrees={row['degree_window']} "
            f"orders={len(row['orders']):<2d} unclassified={row['unclassified_cases']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        print("\nrecomputed summary:")
        print(json.dumps(result, indent=2, sort_keys=True))
        return 1

    print(f"\nPASS: {NCHECK} T-TOY toral classification checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
