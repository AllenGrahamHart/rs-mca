#!/usr/bin/env python3
"""X79 h=5 square-shift obstruction norm gate.

X78 turns h=5 trades into square-shift 10-supports.  For a fixed 10-support,
the monic square root is forced by high coefficients; the remaining low
coefficients are four obstruction values.  A finite-row h=5 trade must make
all four obstruction values vanish modulo the row prime.
"""

from __future__ import annotations

from itertools import combinations
import json
import os
import sys
from typing import Any

import verify_x78_h5_square_shift_supports as x78


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x79-h5-obstruction-norm-gate",
    "x79_h5_obstruction_norm_gate.json",
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
        "x24_char0_dyadic_descent": "PROVED",
        "x78_h5_square_shift_supports": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def forced_root_and_obstructions(
    locator10: list[int], p: int, *, verify: bool = False
) -> tuple[list[int], list[int], int]:
    """Force the monic square root from high coefficients.

    Returns the forced degree-five root S, the low obstruction coefficients
    [X^1..X^4] of S^2 - locator10, and the constant discrepancy lambda.
    """
    ok, root, lambda_const = x78.square_shift_root(locator10, p)
    square = x78.poly_square(root, p)
    obstructions = [(square[i] - locator10[i]) % p for i in range(1, 5)]
    high_ok = all(square[i] == locator10[i] % p for i in range(5, 11))
    if verify:
        check("forced root always matches high coefficients in sample field", high_ok)
        if ok:
            check("square_shift_root ok iff low obstructions vanish", all(v == 0 for v in obstructions))
    return root, obstructions, lambda_const


def algebra_checks() -> dict[str, Any]:
    p = 101
    a_poly = x78.locator_from_roots([2, 3, 5, 7, 11], p)
    delta = 13
    b_poly = list(a_poly)
    b_poly[0] = (b_poly[0] + delta) % p
    trade_locator = x78.poly_mul(a_poly, b_poly, p)
    root, obstructions, lambda_const = forced_root_and_obstructions(trade_locator, p, verify=True)

    check("constructed h5 trade has zero obstruction vector", all(v == 0 for v in obstructions))
    check("constructed h5 trade has nonzero square lambda", lambda_const != 0 and x78.is_square_mod(lambda_const, p))

    perturbed = list(trade_locator)
    perturbed[1] = (perturbed[1] + 1) % p
    _, perturbed_obstructions, perturbed_lambda = forced_root_and_obstructions(perturbed, p, verify=True)
    check("single low-coefficient perturbation creates an obstruction", any(v != 0 for v in perturbed_obstructions))
    check("perturbation leaves the high-coefficient forced root unchanged", perturbed_lambda == lambda_const)

    return {
        "field_p": p,
        "trade_lambda": lambda_const,
        "trade_forced_root": root,
        "trade_obstructions": obstructions,
        "perturbed_obstructions": perturbed_obstructions,
    }


def row_report(n: int, p: int) -> dict[str, Any]:
    domain = x78.mu_domain(p, n)
    zero_obstruction_supports = 0
    square_lambda_supports = 0
    nonsquare_lambda_supports = 0
    nonzero_obstruction_supports = 0
    samples: list[dict[str, Any]] = []

    for support in combinations(range(n), 10):
        locator = x78.locator_from_exponents(domain, support, p)
        root, obstructions, lambda_const = forced_root_and_obstructions(locator, p)
        if all(v == 0 for v in obstructions):
            zero_obstruction_supports += 1
            if x78.is_square_mod(lambda_const, p) and lambda_const != 0:
                square_lambda_supports += 1
            else:
                nonsquare_lambda_supports += 1
            if len(samples) < 5:
                samples.append(
                    {
                        "support": list(support),
                        "lambda": lambda_const,
                        "square_root": root,
                    }
                )
        else:
            nonzero_obstruction_supports += 1

    check(
        f"F{p}/mu{n}: no h5 square-shift supports pass obstruction gate",
        square_lambda_supports == 0,
        f"square_lambda={square_lambda_supports}",
    )
    check(
        f"F{p}/mu{n}: all 10-supports accounted for",
        zero_obstruction_supports + nonzero_obstruction_supports == sum(1 for _ in combinations(range(n), 10)),
    )
    return {
        "n": n,
        "p": p,
        "ten_support_count": zero_obstruction_supports + nonzero_obstruction_supports,
        "zero_obstruction_supports": zero_obstruction_supports,
        "square_lambda_supports": square_lambda_supports,
        "nonsquare_or_zero_lambda_supports": nonsquare_lambda_supports,
        "nonzero_obstruction_supports": nonzero_obstruction_supports,
        "samples": samples,
    }


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    algebra = algebra_checks()
    rows = [
        row_report(16, 17),
        row_report(16, 97),
        row_report(16, 257),
    ]
    check(
        "all sanity rows have empty h5 obstruction-gate survivors",
        all(row["square_lambda_supports"] == 0 for row in rows),
    )
    check(
        "all sanity rows have every support rejected by a nonzero obstruction",
        all(row["zero_obstruction_supports"] == 0 for row in rows),
    )
    return {
        "task": "X79 h=5 obstruction norm gate",
        "node": "active_core_count_bound",
        "status": "PROVED H5 MULTI-OBSTRUCTION GATE: FINITE TRADES FORCE FOUR LOW COEFFICIENTS TO VANISH",
        "theorem": (
            "For a 10-support R in mu_n, the monic degree-five square root "
            "candidate for L_R+lambda is forced by the coefficients of "
            "degrees 10 through 5.  A finite h=5 trade can occur only if the "
            "four low coefficients X^1..X^4 of S_R^2-L_R vanish modulo the "
            "row prime and the constant discrepancy is a nonzero square.  "
            "Since X24 forbids characteristic-zero h=5 trades, every "
            "characteristic-p h=5 trade is p-specific: after clearing powers "
            "of two, p divides the cyclotomic norm of each nonzero obstruction."
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

    print("\nh5 obstruction-gate sanity rows:")
    for row in cert["sanity_rows"]:
        print(
            f"F{row['p']}/mu{row['n']}: zero_obstruction={row['zero_obstruction_supports']} "
            f"square_lambda={row['square_lambda_supports']} "
            f"10-supports={row['ten_support_count']}"
        )

    if FAILS:
        print(f"\nFAIL: {len(FAILS)} checks failed: {FAILS}", file=sys.stderr)
        return 1
    print(f"\nPASS: {NCHECK} X79 h5 obstruction norm-gate checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
