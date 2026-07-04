#!/usr/bin/env python3
"""X39 h=4 affine-line normal form.

For a monic quartic psi in characteristic > 4, every exact affine line factor
X = aY+b of psi(X)-psi(Y) comes from a centered power:

    psi(X) = Phi((X-c)^m),       m in {2,4},       c=b/(1-a).

The zero-center case is the cyclic-paid branch already isolated by X38.  The
nonzero-center case is not silently charged here; it is recorded as the
centered-power affine residue.
"""

from __future__ import annotations

import json
import math
import os
import sys
from typing import Any

import verify_x38_h4_exact_toral_line_classifier as x38


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "x39-h4-affine-line-normal-form",
    "x39_h4_affine_line_normal_form.json",
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
        "x38_h4_exact_toral_line_classifier": "PROVED",
        "active_core_count_bound": "TARGET",
    }
    for node, expected in needed.items():
        actual = statuses.get(node, "missing")
        check(f"DAG node {node} has expected status", actual == expected, actual)
    return {node: statuses.get(node, "missing") for node in needed}


def trim(coeffs: list[int]) -> list[int]:
    out = coeffs[:]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_shift(coeffs: list[int], c: int, p: int) -> list[int]:
    """Return coefficients of psi(T+c), low-to-high."""
    out = [0] * len(coeffs)
    for i, coeff in enumerate(coeffs):
        if coeff == 0:
            continue
        for j in range(i + 1):
            out[j] = (out[j] + coeff * math.comb(i, j) * pow(c, i - j, p)) % p
    return trim(out)


def poly_compose_affine(coeffs: list[int], a: int, b: int, p: int) -> list[int]:
    """Return coefficients of psi(aX+b), low-to-high."""
    out = [0] * len(coeffs)
    for i, coeff in enumerate(coeffs):
        if coeff == 0:
            continue
        for j in range(i + 1):
            out[j] = (
                out[j]
                + coeff * math.comb(i, j) * pow(a, j, p) * pow(b, i - j, p)
            ) % p
    return trim(out)


def pad(coeffs: list[int], size: int) -> list[int]:
    return coeffs + [0] * (size - len(coeffs))


def poly_equal(left: list[int], right: list[int]) -> bool:
    size = max(len(left), len(right))
    return pad(trim(left), size) == pad(trim(right), size)


def centered_power_coeffs(center: int, order: int, p: int) -> list[int]:
    if order == 2:
        # (X-c)^4 + 7 (X-c)^2 + 5
        centered = [5 % p, 0, 7 % p, 0, 1]
    elif order == 4:
        # (X-c)^4 + 5
        centered = [5 % p, 0, 0, 0, 1]
    else:
        raise ValueError(order)
    return poly_compose_affine(centered, 1, (-center) % p, p)


def affine_normal_form(coeffs: list[int], a: int, b: int, p: int) -> dict[str, Any]:
    direct_invariant = poly_equal(poly_compose_affine(coeffs, a, b, p), coeffs)
    if a % p == 1:
        return {
            "a": a,
            "b": b,
            "translation": True,
            "direct_invariant": direct_invariant,
            "translation_top_x3_coefficient": (4 * b) % p,
            "normal_form": None,
        }

    center = (b * pow((1 - a) % p, -1, p)) % p
    shifted = poly_shift(coeffs, center, p)
    order = x38.multiplicative_order(a, p)
    forbidden = [i for i, coeff in enumerate(shifted) if coeff and i % order != 0]
    centered_power = direct_invariant and order in (2, 4) and not forbidden
    zero_center_paid = centered_power and center == 0
    return {
        "a": a,
        "b": b,
        "translation": False,
        "center": center,
        "order": order,
        "a_fourth": pow(a, 4, p),
        "direct_invariant": direct_invariant,
        "shifted_coefficients_low_to_high": shifted,
        "forbidden_shifted_exponents": forbidden,
        "centered_power": centered_power,
        "zero_center_cyclic_paid": zero_center_paid,
        "nonzero_center_affine_residue": centered_power and center != 0,
    }


def check_translation_branch() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for p in (97, 4993):
        coeffs = [11 % p, 13 % p, 17 % p, 19 % p, 1]
        for b in (1, 2, p - 1):
            row = affine_normal_form(coeffs, 1, b, p)
            check(
                f"translation symmetry b={b} impossible for monic quartic modulo {p}",
                not row["direct_invariant"] and row["translation_top_x3_coefficient"] != 0,
                f"top={row['translation_top_x3_coefficient']}",
            )
            rows.append({"p": p, "coefficients": coeffs, **row})
    return rows


def check_centered_examples() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    examples = [
        {"label": "order2 nonzero-center branch", "p": 97, "center": 5, "a": 96, "order": 2},
        {"label": "order4 nonzero-center branch", "p": 97, "center": 5, "a": 22, "order": 4},
        {"label": "order2 zero-center paid branch", "p": 4993, "center": 0, "a": 4992, "order": 2},
        {"label": "order4 zero-center paid branch", "p": 4993, "center": 0, "a": 158, "order": 4},
    ]
    for ex in examples:
        p = ex["p"]
        center = ex["center"]
        a = ex["a"]
        b = ((1 - a) * center) % p
        coeffs = centered_power_coeffs(center, ex["order"], p)
        row = affine_normal_form(coeffs, a, b, p)
        check(
            f"{ex['label']}: affine invariant is detected",
            row["direct_invariant"] and row["centered_power"],
            f"center={row.get('center')}, shifted={row.get('shifted_coefficients_low_to_high')}",
        )
        check(f"{ex['label']}: center is recovered", row.get("center") == center)
        if center == 0:
            check(f"{ex['label']}: zero-center branch is cyclic-paid", row["zero_center_cyclic_paid"])
        else:
            check(
                f"{ex['label']}: nonzero-center branch is only named, not paid here",
                row["nonzero_center_affine_residue"] and not row["zero_center_cyclic_paid"],
            )
        rows.append({"label": ex["label"], "coefficients": coeffs, **row})
    return rows


def check_actual_quartic_examples() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    examples = [
        {
            "label": "mu4 baseline",
            "n": 32,
            "p": 4993,
            "support": (0, 8, 16, 24),
            "affine_maps": [(4992, 0), (158, 0)],
            "expect_any": True,
        },
        {
            "label": "top-level first-sum only nontrade",
            "n": 32,
            "p": 4993,
            "support": (0, 1, 2, 17),
            "affine_maps": [(4992, 0), (158, 0), (4992, 1), (158, 3)],
            "expect_any": False,
        },
    ]
    for ex in examples:
        coeffs = x38.quartic_coeffs_from_support(ex["n"], ex["p"], ex["support"])
        classifications = [affine_normal_form(coeffs, a, b, ex["p"]) for a, b in ex["affine_maps"]]
        hits = [row for row in classifications if row["direct_invariant"]]
        check(
            f"{ex['label']}: affine-symmetry expectation matches",
            bool(hits) == ex["expect_any"],
            f"hits={len(hits)}",
        )
        rows.append(
            {
                "label": ex["label"],
                "n": ex["n"],
                "p": ex["p"],
                "support": list(ex["support"]),
                "coefficients": coeffs,
                "classifications": classifications,
                "hits": hits,
            }
        )
    return rows


def build_certificate() -> dict[str, Any]:
    deps = check_dependency_nodes()
    translations = check_translation_branch()
    centered = check_centered_examples()
    actual = check_actual_quartic_examples()
    return {
        "task": "X39 h=4 affine-line normal form",
        "node": "active_core_count_bound",
        "status": "PROVED REFINEMENT: quartic affine-line factors are centered powers",
        "theorem": (
            "Let psi be a monic quartic over characteristic p>4.  If "
            "psi(aX+b)=psi(X) for a nonidentity affine map, then translations "
            "a=1,b!=0 are impossible.  For a!=1, with c=b/(1-a), the shifted "
            "polynomial psi(T+c) is invariant under T -> aT.  The leading term "
            "forces a^4=1, so ord(a) is 2 or 4, and all nonzero shifted "
            "exponents are multiples of ord(a).  Hence psi=Phi((X-c)^m), "
            "m in {2,4}.  The c=0 branch is cyclic-paid; the c!=0 branch is "
            "the named centered-power affine residue."
        ),
        "dependency_statuses": deps,
        "translation_checks": translations,
        "centered_power_examples": centered,
        "actual_quartic_examples": actual,
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

    print("\ncentered-power examples:")
    for row in cert["centered_power_examples"]:
        print(
            f"{row['label']}: center={row.get('center')} order={row.get('order')} "
            f"paid={row.get('zero_center_cyclic_paid')} residue={row.get('nonzero_center_affine_residue')}"
        )

    if FAILS:
        print("\nFAIL:")
        for name in FAILS:
            print(f"  - {name}")
        return 1

    print(f"\nPASS: {NCHECK} X39 affine-line normal-form checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
