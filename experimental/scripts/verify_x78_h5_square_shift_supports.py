#!/usr/bin/env python3
"""X78 h=5 square-shift support criterion.

For h=5, two monic locator polynomials have the same top four coefficients
exactly when they differ by a constant.  Multiplying them shows that the
10-point union locator becomes a square after changing only the constant term.

This verifier records the algebraic criterion and runs small exact sanity
checks on n=16 rows.  It is intentionally not a large h=5 scan.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations
import json
import os
import sys
from typing import Any


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x78-h5-square-shift",
    "x78_h5_square_shift_supports.json",
)
DAG = os.path.join(REPO, "experimental", "data", "prize-dag", "prize_dag.json")

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
        "x30_finite_p_norm_gate": "PROVED",
        "x77_h5_norm_gate_reduction": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def primitive_root(p: int) -> int:
    factors: list[int] = []
    x = p - 1
    d = 2
    while d * d <= x:
        if x % d == 0:
            factors.append(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        factors.append(x)
    for g in range(2, p):
        if all(pow(g, (p - 1) // r, p) != 1 for r in factors):
            return g
    raise AssertionError(f"no primitive root found for p={p}")


def mu_domain(p: int, n: int) -> list[int]:
    g = primitive_root(p)
    zeta = pow(g, (p - 1) // n, p)
    return [pow(zeta, i, p) for i in range(n)]


def poly_mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return out


def poly_square(a: list[int], p: int) -> list[int]:
    return poly_mul(a, a, p)


def locator_from_roots(roots: list[int], p: int) -> list[int]:
    coeffs = [1]
    for root in roots:
        nxt = [0] * (len(coeffs) + 1)
        for i, coeff in enumerate(coeffs):
            nxt[i] = (nxt[i] - coeff * root) % p
            nxt[i + 1] = (nxt[i + 1] + coeff) % p
        coeffs = nxt
    return coeffs


def locator_from_exponents(domain: list[int], exps: tuple[int, ...], p: int) -> list[int]:
    return locator_from_roots([domain[i] for i in exps], p)


def mask_from_tuple(values: tuple[int, ...]) -> int:
    out = 0
    for value in values:
        out |= 1 << value
    return out


def exps(mask: int, n: int) -> list[int]:
    return [i for i in range(n) if (mask >> i) & 1]


def top_four(locator: list[int]) -> tuple[int, int, int, int]:
    # Degree-five monic locator coefficients are
    # c0 + c1 X + c2 X^2 + c3 X^3 + c4 X^4 + X^5.
    return tuple(locator[1:5])  # e4, -e3, e2, -e1 in low-to-high order.


def square_shift_root(locator10: list[int], p: int) -> tuple[bool, list[int], int]:
    """Return whether locator10 + lambda is a monic square.

    The monic square root S has degree five and is forced recursively by the
    coefficients of degrees 10 down to 5.  Degrees 1 through 4 are then
    constraints; the constant mismatch is lambda.
    """
    inv2 = pow(2, -1, p)
    s = [0] * 6
    s[5] = 1
    for degree in range(9, 4, -1):
        unknown = degree - 5
        known = 0
        for i in range(max(0, degree - 5), min(5, degree) + 1):
            j = degree - i
            if not 0 <= j <= 5:
                continue
            if i == unknown or j == unknown:
                continue
            known = (known + s[i] * s[j]) % p
        s[unknown] = ((locator10[degree] - known) * inv2) % p

    s2 = poly_square(s, p)
    ok = all(s2[degree] == locator10[degree] % p for degree in range(1, 11))
    lambda_const = (s2[0] - locator10[0]) % p
    return ok, s, lambda_const


def is_square_mod(lambda_const: int, p: int) -> bool:
    return any((x * x - lambda_const) % p == 0 for x in range(p))


def algebra_checks() -> dict[str, Any]:
    p = 101
    inv2 = pow(2, -1, p)
    a_poly = locator_from_roots([2, 3, 5, 7, 11], p)
    delta = 13
    b_poly = list(a_poly)
    b_poly[0] = (b_poly[0] + delta) % p
    union_locator = poly_mul(a_poly, b_poly, p)
    midpoint = [((a + b) * inv2) % p for a, b in zip(a_poly, b_poly)]
    lambda_const = (delta * delta * pow(4, -1, p)) % p
    shifted = list(union_locator)
    shifted[0] = (shifted[0] + lambda_const) % p

    check("constructed h5 pair has equal top four coefficients", top_four(a_poly) == top_four(b_poly))
    check("constructed h5 union becomes a square after constant shift", shifted == poly_square(midpoint, p))
    ok, forced_midpoint, forced_lambda = square_shift_root(union_locator, p)
    check("forced square-shift root recovers constructed midpoint", ok and forced_midpoint == midpoint)
    check("forced square-shift lambda recovers constructed lambda", forced_lambda == lambda_const)

    a = 17
    s_poly = [19, 23, 29, 31, 37, 1]
    left = list(s_poly)
    right = list(s_poly)
    left[0] = (left[0] - a) % p
    right[0] = (right[0] + a) % p
    product = poly_mul(left, right, p)
    ok2, forced_s, forced_lambda2 = square_shift_root(product, p)
    check("converse sample product is square-shifted", ok2 and forced_s == s_poly)
    check("converse sample factors differ only in the constant term", top_four(left) == top_four(right))
    check("converse sample lambda is a square", forced_lambda2 == (a * a) % p)

    return {
        "field_p": p,
        "delta": delta,
        "constructed_lambda": lambda_const,
        "midpoint_coefficients": midpoint,
        "converse_square_root_coefficients": s_poly,
    }


def analyze_mu_row(n: int, p: int) -> dict[str, Any]:
    domain = mu_domain(p, n)
    groups: dict[tuple[int, int, int, int], list[int]] = defaultdict(list)
    for subset in combinations(range(n), 5):
        locator = locator_from_exponents(domain, subset, p)
        groups[top_four(locator)].append(mask_from_tuple(subset))

    unordered_trade_pairs = 0
    for masks in groups.values():
        for index, left in enumerate(masks):
            for right in masks[index + 1 :]:
                if not left & right:
                    unordered_trade_pairs += 1

    square_shift_supports = 0
    square_lambda_supports = 0
    examples: list[dict[str, Any]] = []
    for support in combinations(range(n), 10):
        locator = locator_from_exponents(domain, support, p)
        ok, root, lambda_const = square_shift_root(locator, p)
        if not ok:
            continue
        square_shift_supports += 1
        square_lambda = is_square_mod(lambda_const, p)
        if square_lambda:
            square_lambda_supports += 1
        if len(examples) < 5:
            examples.append(
                {
                    "support": list(support),
                    "lambda": lambda_const,
                    "lambda_is_square": square_lambda,
                    "square_root_coefficients": root,
                }
            )

    check(
        f"F{p}/mu{n}: h5 trade pairs equal square-lambda supports",
        unordered_trade_pairs == square_lambda_supports,
        f"pairs={unordered_trade_pairs}, supports={square_lambda_supports}",
    )
    check(
        f"F{p}/mu{n}: no non-square square-shift supports in sanity row",
        square_shift_supports == square_lambda_supports,
        f"all={square_shift_supports}, square_lambda={square_lambda_supports}",
    )

    return {
        "n": n,
        "p": p,
        "five_subset_count": sum(1 for _ in combinations(range(n), 5)),
        "ten_support_count": sum(1 for _ in combinations(range(n), 10)),
        "unordered_h5_trade_pairs": unordered_trade_pairs,
        "square_shift_supports": square_shift_supports,
        "square_lambda_square_shift_supports": square_lambda_supports,
        "examples": examples,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    algebra = algebra_checks()
    rows = [
        analyze_mu_row(16, 17),
        analyze_mu_row(16, 97),
        analyze_mu_row(16, 257),
    ]
    check(
        "all sanity rows have square-shift count equal to h5 trade count",
        all(row["unordered_h5_trade_pairs"] == row["square_lambda_square_shift_supports"] for row in rows),
    )
    check(
        "boundary sanity row F257/mu16 is h5-injective",
        next(row for row in rows if row["p"] == 257)["unordered_h5_trade_pairs"] == 0,
    )

    return {
        "task": "X78 h=5 square-shift support criterion",
        "node": "active_core_count_bound",
        "status": "PROVED H5 ALGEBRAIC COMPRESSION: TRADES BIJECT WITH SQUARE-SHIFT 10-SUPPORTS",
        "theorem": (
            "Over any odd-characteristic field, a disjoint h=5 same-top-four "
            "pair (P,Q) is equivalent to the union locator L_{P union Q} "
            "admitting a unique monic degree-five S and a square lambda with "
            "L_{P union Q}+lambda=S^2.  The square lambda is nonzero for "
            "disjoint supports, and the split is unique up to swapping P "
            "and Q.  Thus h=5 pair counting may be replaced by counting "
            "square-shift 10-supports with nonzero square shift."
        ),
        "dependency_statuses": deps,
        "algebra_checks": algebra,
        "sanity_rows": rows,
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

    print("\nh5 square-shift sanity rows:")
    for row in cert["sanity_rows"]:
        print(
            f"F{row['p']}/mu{row['n']}: trades={row['unordered_h5_trade_pairs']} "
            f"square_supports={row['square_lambda_square_shift_supports']} "
            f"10-supports={row['ten_support_count']}"
        )

    if FAILS:
        print(f"\nFAIL: {len(FAILS)} checks failed: {FAILS}", file=sys.stderr)
        return 1
    print(f"\nPASS: {NCHECK} X78 h5 square-shift checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
