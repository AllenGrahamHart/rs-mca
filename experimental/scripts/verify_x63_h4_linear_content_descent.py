#!/usr/bin/env python3
"""X63 content descent for X62 four-term linear words.

For an X60/X62 filtered word

    f(X) = X^a + X^b - X^c - 1

with n=2^s, the content d=gcd(n,a,b,c) is a quotient-pullback marker.  If
d>1 then f(X)=g(X^d), and the finite-field triple descends verbatim to the
smaller row mu_{n/d}.  Thus the genuinely primitive X62 residue is the
content-one subfamily.
"""

from __future__ import annotations

from collections import Counter
import json
import math
import os
import sys
from typing import Any

import verify_h1_u1_toy_harness as h1


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x63-h4-linear-content-descent",
    "x63_h4_linear_content_descent.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")
X60_CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x60-h4-linear-triple-form",
    "x60_h4_linear_triple_form.json",
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


def load_json(path: str) -> Any:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def check_dependency_nodes() -> dict[str, str]:
    dag = load_json(DAG)
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    needed = {
        "x60_h4_linear_triple_form": "PROVED",
        "x62_h4_linear_norm_gate": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def excluded_flags(n: int, a: int, b: int, c: int) -> dict[str, bool]:
    return {
        "x_equals_1": a % n == 0,
        "y_equals_1": b % n == 0,
        "z_equals_1": c % n == 0,
        "y_equals_x": b % n == a % n,
        "y_equals_minus_x": b % n == (a + n // 2) % n,
    }


def is_filtered(n: int, a: int, b: int, c: int) -> bool:
    return not any(excluded_flags(n, a, b, c).values())


def word_content(n: int, a: int, b: int, c: int) -> int:
    return math.gcd(math.gcd(math.gcd(n, a), b), c)


def row_report(row: dict[str, Any]) -> dict[str, Any]:
    n = int(row["n"])
    p = int(row["p"])
    domain = h1.mu_domain(p, n)
    exponent_by_value = {value: exp for exp, value in enumerate(domain)}

    content_histogram: Counter[int] = Counter()
    quotient_histogram: Counter[int] = Counter()
    primitive_examples: list[dict[str, Any]] = []
    descended_examples: list[dict[str, Any]] = []

    filtered = 0
    descended = 0
    primitive = 0
    quotient_equation_failures = 0
    quotient_filter_failures = 0

    for a, x in enumerate(domain):
        for b, y in enumerate(domain):
            z = (x + y - 1) % p
            c = exponent_by_value.get(z)
            if c is None or not is_filtered(n, a, b, c):
                continue

            filtered += 1
            d = word_content(n, a, b, c)
            content_histogram[d] += 1

            if d == 1:
                primitive += 1
                if len(primitive_examples) < 5:
                    primitive_examples.append({"a": a, "b": b, "c": c})
                continue

            descended += 1
            quotient_n = n // d
            quotient_histogram[quotient_n] += 1
            qa, qb, qc = a // d, b // d, c // d
            qgen = pow(domain[1], d, p)
            qx = pow(qgen, qa, p)
            qy = pow(qgen, qb, p)
            qz = pow(qgen, qc, p)

            if (qx + qy - qz - 1) % p != 0:
                quotient_equation_failures += 1
            if not is_filtered(quotient_n, qa, qb, qc):
                quotient_filter_failures += 1
            if len(descended_examples) < 5:
                descended_examples.append(
                    {
                        "content": d,
                        "quotient_n": quotient_n,
                        "source_exponents": [a, b, c],
                        "quotient_exponents": [qa, qb, qc],
                    }
                )

    expected = int(row["filtered_linear_triple_count"])
    check(
        f"{row['label']}: content histogram sums to X60 filtered count",
        filtered == expected and sum(content_histogram.values()) == expected,
        f"filtered={filtered}, expected={expected}",
    )
    check(
        f"{row['label']}: primitive plus descended split is exhaustive",
        primitive + descended == filtered,
        f"primitive={primitive}, descended={descended}, filtered={filtered}",
    )
    check(
        f"{row['label']}: every nonprimitive content is a proper divisor",
        all(1 < d < n and n % d == 0 for d in content_histogram if d > 1),
        f"contents={dict(content_histogram)}",
    )
    check(
        f"{row['label']}: all nonprimitive triples satisfy quotient equation",
        quotient_equation_failures == 0,
        f"failures={quotient_equation_failures}, descended={descended}",
    )
    check(
        f"{row['label']}: all nonprimitive triples remain filtered after descent",
        quotient_filter_failures == 0,
        f"failures={quotient_filter_failures}, descended={descended}",
    )

    return {
        "label": row["label"],
        "kind": row["kind"],
        "n": n,
        "p": p,
        "filtered_linear_triple_count": filtered,
        "primitive_content_one_count": primitive,
        "quotient_descended_count": descended,
        "content_histogram": {str(k): v for k, v in sorted(content_histogram.items())},
        "quotient_row_histogram": {str(k): v for k, v in sorted(quotient_histogram.items())},
        "quotient_equation_failures": quotient_equation_failures,
        "quotient_filter_failures": quotient_filter_failures,
        "primitive_examples": primitive_examples,
        "descended_examples": descended_examples,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    x60 = load_json(X60_CERT)
    check("X60 certificate has replay rows", bool(x60.get("rows")))
    rows = [row_report(row) for row in x60["rows"]]
    check(
        "all replay rows have exhaustive primitive/quotient content split",
        all(
            row["primitive_content_one_count"] + row["quotient_descended_count"]
            == row["filtered_linear_triple_count"]
            for row in rows
        ),
    )
    check(
        "some replay row has nonprimitive quotient-descended mass",
        any(row["quotient_descended_count"] > 0 for row in rows),
    )
    check(
        "some replay row has primitive content-one mass",
        any(row["primitive_content_one_count"] > 0 for row in rows),
    )
    return {
        "task": "X63 h=4 linear content descent",
        "node": "active_core_count_bound",
        "status": "PROVED CONTENT SPLIT: NONPRIMITIVE X62 WORDS DESCEND TO QUOTIENT ROWS",
        "theorem": (
            "For an X60-filtered word f=X^a+X^b-X^c-1 on mu_n, let "
            "d=gcd(n,a,b,c).  If d>1 then f(X)=g(X^d), zeta^d is primitive "
            "of order n/d, and the triple descends to the same filtered "
            "linear equation on mu_{n/d}.  Therefore the post-quotient X62 "
            "primitive residue is the content-one subfamily."
        ),
        "dependency_statuses": deps,
        "rows": rows,
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

    print("\ncontent rows:")
    for row in cert["rows"]:
        print(
            f"{row['label']}: primitive={row['primitive_content_one_count']} "
            f"descended={row['quotient_descended_count']} "
            f"hist={row['content_histogram']}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X63 h4 linear content-descent checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
