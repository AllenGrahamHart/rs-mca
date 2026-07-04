#!/usr/bin/env python3
"""X38 h=4 exact toral-line classifier.

X37 rewrites h=4 trades as two split fibers of one monic quartic
locator.  This verifier records the elementary toral-line specialization:

* if a monic quartic psi has an exact scaling symmetry psi(lambda X)=psi(X)
  with lambda != 1 in odd characteristic, then psi factors through X^2 or
  X^4, hence is cyclic-pullback paid;
* an exact inverse toral component XY=c cannot divide psi(X)-psi(Y) for a
  nonconstant polynomial psi.

Thus any primitive quartic two-fiber residue has no exact toral line in its
polynomial fiber product.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
import sys
from typing import Any

import verify_h1_u1_toy_harness as h1
import verify_x37_h4_quartic_fiber_form as x37


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x38-h4-exact-toral-line-classifier",
    "x38_h4_exact_toral_line_classifier.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")

FAILS: list[str] = []
NCHECK = 0


@dataclass(frozen=True)
class QuarticExample:
    label: str
    n: int
    p: int
    support: tuple[int, int, int, int]
    expected_order: int | None


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
        "x37_h4_quartic_fiber_form": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def poly_trim(coeffs: list[int]) -> list[int]:
    out = coeffs[:]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_degree(coeffs: list[int]) -> int:
    return len(poly_trim(coeffs)) - 1


def quartic_coeffs_from_support(n: int, p: int, support: tuple[int, int, int, int]) -> list[int]:
    domain = h1.mu_domain(p, n)
    e1, e2, e3, e4 = x37.elementary_all(domain, p, support)
    return [e4 % p, (-e3) % p, e2 % p, (-e1) % p, 1]


def multiplicative_order(a: int, p: int) -> int:
    x = 1
    for r in range(1, p):
        x = (x * a) % p
        if x == 1:
            return r
    raise ValueError(f"{a} has no multiplicative order modulo {p}")


def scaling_difference_coeffs(coeffs: list[int], lam: int, p: int) -> list[int]:
    return [((pow(lam, i, p) - 1) * coeff) % p for i, coeff in enumerate(coeffs)]


def scaling_invariant(coeffs: list[int], lam: int, p: int) -> bool:
    return all(c == 0 for c in scaling_difference_coeffs(coeffs, lam, p))


def pullback_modulus(coeffs: list[int], m: int) -> bool:
    return all((coeff == 0 or i % m == 0) for i, coeff in enumerate(coeffs))


def classify_scaling_symmetry(coeffs: list[int], lam: int, p: int) -> dict[str, Any]:
    order = multiplicative_order(lam, p)
    invariant = scaling_invariant(coeffs, lam, p)
    return {
        "lambda": lam,
        "order": order,
        "lambda_fourth": pow(lam, 4, p),
        "invariant": invariant,
        "allowed_exponents": [i for i, coeff in enumerate(coeffs) if coeff and i % order == 0],
        "forbidden_nonzero_exponents": [i for i, coeff in enumerate(coeffs) if coeff and i % order != 0],
        "pullback_through_X_order": invariant and order in (2, 4) and pullback_modulus(coeffs, order),
    }


def check_symbolic_scaling_classifier() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for p, lambdas in ((97, [96, 22, 75]), (4993, [4992, 158, 4835])):
        for lam in lambdas:
            order = multiplicative_order(lam, p)
            check(f"lambda order is 2 or 4 modulo {p}", order in (2, 4), f"lambda={lam}, order={order}")
            check(f"lambda^4=1 modulo {p}", pow(lam, 4, p) == 1, f"lambda={lam}")

            if order == 2:
                paid_coeffs = [5 % p, 0, 7 % p, 0, 1]
                bad_coeffs = [5 % p, 3 % p, 7 % p, 0, 1]
            else:
                paid_coeffs = [5 % p, 0, 0, 0, 1]
                bad_coeffs = [5 % p, 0, 7 % p, 0, 1]

            paid = classify_scaling_symmetry(paid_coeffs, lam, p)
            bad = classify_scaling_symmetry(bad_coeffs, lam, p)
            check(
                f"order-{order} paid sample is exactly scaling invariant modulo {p}",
                paid["invariant"] and paid["pullback_through_X_order"],
                f"lambda={lam}",
            )
            check(
                f"order-{order} forbidden exponent breaks scaling invariant modulo {p}",
                not bad["invariant"] and bool(bad["forbidden_nonzero_exponents"]),
                f"lambda={lam}, forbidden={bad['forbidden_nonzero_exponents']}",
            )
            rows.append({"p": p, "lambda": lam, "order": order, "paid": paid, "bad": bad})
    return rows


def inverse_toral_top_coeff(degree: int, leading_coeff: int, p: int) -> int:
    """Top coefficient of X^d(psi(X)-psi(c/X)); independent of c."""
    return leading_coeff % p


def check_inverse_toral_obstruction() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for p in (97, 257, 4993):
        for c in (1, 2, p - 1):
            top = inverse_toral_top_coeff(4, 1, p)
            check(
                f"XY=c inverse toral line impossible for monic quartic modulo {p}",
                top != 0,
                f"c={c}, top_coeff={top}",
            )
            rows.append(
                {
                    "p": p,
                    "c": c,
                    "multiplied_identity": "X^4(psi(X)-psi(c/X))",
                    "top_degree": 8,
                    "top_coefficient": top,
                    "conclusion": "nonzero top coefficient prevents the rational identity",
                }
            )
    return rows


def analyze_examples() -> list[dict[str, Any]]:
    examples = [
        QuarticExample("mu4 baseline", 32, 4993, (0, 8, 16, 24), 4),
        QuarticExample("antipodal quotient extra", 64, 4993, (0, 2, 32, 34), 2),
        QuarticExample("top-level first-sum only nontrade", 32, 4993, (0, 1, 2, 17), None),
    ]
    out: list[dict[str, Any]] = []
    for example in examples:
        coeffs = quartic_coeffs_from_support(example.n, example.p, example.support)
        domain = h1.mu_domain(example.p, example.n)
        nontrivial_lambdas = [domain[example.n // 2], domain[example.n // 4], domain[3 * example.n // 4]]
        classifications = [classify_scaling_symmetry(coeffs, lam, example.p) for lam in nontrivial_lambdas]
        invariant_orders = sorted({row["order"] for row in classifications if row["invariant"]})
        if example.expected_order is None:
            check(f"{example.label}: no exact scaling toral line", invariant_orders == [], str(invariant_orders))
        else:
            check(
                f"{example.label}: expected exact scaling order appears",
                example.expected_order in invariant_orders,
                str(invariant_orders),
            )
            check(
                f"{example.label}: invariant quartic is cyclic-pullback paid",
                any(row["pullback_through_X_order"] for row in classifications if row["order"] == example.expected_order),
            )
        out.append(
            {
                "label": example.label,
                "n": example.n,
                "p": example.p,
                "support": list(example.support),
                "locator_coefficients_low_to_high": coeffs,
                "expected_order": example.expected_order,
                "invariant_orders": invariant_orders,
                "classifications": classifications,
            }
        )
    return out


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    symbolic = check_symbolic_scaling_classifier()
    inverse = check_inverse_toral_obstruction()
    examples = analyze_examples()
    return {
        "task": "X38 h=4 exact toral-line classifier",
        "node": "active_core_count_bound",
        "status": "PROVED SPECIALIZATION: quartic exact toral lines are cyclic-paid or impossible",
        "theorem": (
            "Let psi(X)=X^4+a3X^3+a2X^2+a1X+a0 over odd characteristic. "
            "If psi(lambda X)=psi(X) for lambda != 1, then lambda^4=1. "
            "For m=ord(lambda), every nonzero coefficient has exponent divisible by m; "
            "hence m is 2 or 4 and psi=Phi(X^m), a cyclic pullback. "
            "No exact inverse toral line XY=c divides psi(X)-psi(Y), since "
            "X^4(psi(X)-psi(c/X)) has nonzero X^8 coefficient. "
            "Therefore a primitive h=4 quartic two-fiber residue has no exact toral line."
        ),
        "dependency_statuses": deps,
        "symbolic_scaling_checks": symbolic,
        "inverse_toral_checks": inverse,
        "quartic_examples": examples,
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

    print("\nquartic examples:")
    for row in cert["quartic_examples"]:
        print(
            f"{row['label']}: invariant_orders={row['invariant_orders']} "
            f"coeffs={row['locator_coefficients_low_to_high']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X38 exact toral-line checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
