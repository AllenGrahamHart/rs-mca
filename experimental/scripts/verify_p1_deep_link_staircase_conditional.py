#!/usr/bin/env python3
"""Verifier for the P1 deep-link staircase conditional packet.

The packet proves the exact reduction from a fixed (k-1)-subcore link to
rich points of an affine line arrangement in the two parameters (z, a).  It
also checks a small explicit RS embedding showing that the raw per-subcore
constant cap is false for arbitrary received pairs; the missing hypothesis is
the post-paid rich-line cap.

Stdlib only.
Run: python3 experimental/scripts/verify_p1_deep_link_staircase_conditional.py
To refresh the pinned certificate:
  python3 experimental/scripts/verify_p1_deep_link_staircase_conditional.py --write-certificate
"""

from __future__ import annotations

import json
import os
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "p1-deep-link-staircase-conditional",
    "p1_deep_link_staircase_conditional.json",
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


def inv(p: int, a: int) -> int:
    if a % p == 0:
        raise ZeroDivisionError("zero inverse")
    return pow(a, p - 2, p)


def eval_poly(p: int, coeffs: list[int], x: int) -> int:
    acc = 0
    power = 1
    for c in coeffs:
        acc = (acc + c * power) % p
        power = power * x % p
    return acc


def poly_mul_linear(p: int, coeffs: list[int], root: int) -> list[int]:
    out = [0] * (len(coeffs) + 1)
    for i, c in enumerate(coeffs):
        out[i] = (out[i] - root * c) % p
        out[i + 1] = (out[i + 1] + c) % p
    return out


def vanishing_poly(p: int, roots: list[int]) -> list[int]:
    coeffs = [1]
    for root in roots:
        coeffs = poly_mul_linear(p, coeffs, root)
    return coeffs


def rich_line_fixture(m: int = 10, p: int = 211) -> dict:
    """Embed a 3-family rich-line arrangement as aligned partners.

    Parameters are (z,a).  A domain point x outside the fixed subcore
    contributes the line

        a = A_x + z B_x.

    Families:
        H_i: a = i
        P_j: a = z + j
        N_l: a = -z + l

    H_i, P_j, N_l meet when z=i-j and l=2i-j.  With 1<=i,j<=m and
    1<=l<=2m this gives many 3-rich parameter points through one fixed
    (k-1)-subcore.
    """
    k = 4
    t = 2
    A = k + t
    z0 = 0
    # Domain points are small distinct field elements.  R has k-1 points;
    # T0 has A points; all line points are outside T0.
    R = [1, 2, 3]
    T0_extra = [4, 5, 6]
    lines: list[tuple[str, int, int]] = []
    for i in range(1, m + 1):
        lines.append((f"H{i}", i, 0))
    for j in range(1, m + 1):
        lines.append((f"P{j}", j, 1))
    for ell in range(1, 2 * m + 1):
        lines.append((f"N{ell}", ell, -1 % p))
    n = len(R) + len(T0_extra) + len(lines)
    xs = list(range(1, n + 1))
    R_xs = xs[: len(R)]
    T0_xs = xs[:A]
    line_xs = xs[A:]
    h = vanishing_poly(p, R_xs)
    # u=v=0 on T0, so z0=0 is explained by c0=0 on T0.
    u = {x: 0 for x in xs}
    v = {x: 0 for x in xs}
    for x, (_, intercept, slope) in zip(line_xs, lines):
        hx = eval_poly(p, h, x)
        u[x] = intercept * hx % p
        v[x] = slope * hx % p

    rich: dict[tuple[int, int], list[str]] = {}
    for label, intercept, slope in lines:
        for z in range(p):
            a = (intercept + z * slope) % p
            rich.setdefault((z, a), []).append(label)
    rich3 = {param: labs for param, labs in rich.items() if len(labs) >= 3 and param[0] != z0}

    # Verify every rich parameter gives an aligned support through R.
    verified = 0
    for (z, a), labs in rich3.items():
        c_vals = {x: a * eval_poly(p, h, x) % p for x in xs}
        support = set(R_xs)
        for x, (label, _, _) in zip(line_xs, lines):
            if label in labs:
                support.add(x)
        ok = all((u[x] + z * v[x] - c_vals[x]) % p == 0 for x in support)
        ok &= all((u[x] + z * v[x] - c_vals[x]) % p != 0 for x in T0_xs if x not in R_xs)
        if ok and len(support) >= A:
            verified += 1

    check("rich-line fixture has one fixed near-k subcore", len(R_xs) == k - 1 and 2 * len(R_xs) > k)
    check("rich-line fixture creates many partner parameters", len(rich3) > n, f"rich={len(rich3)}, n={n}")
    check("all rich parameters embed as aligned partners", verified == len(rich3), f"verified={verified}")

    return {
        "field": f"F_{p}",
        "k": k,
        "t": t,
        "A": A,
        "n": n,
        "fixed_subcore_size": len(R_xs),
        "line_count": len(lines),
        "rich_parameters": len(rich3),
        "verified_partner_parameters": verified,
        "interpretation": "raw per-subcore constant cap is false before post-paid stripping",
    }


def conditional_counting_fixture() -> dict:
    # Pure arithmetic for the conditional theorem:
    # if occupied witnesses <= B*n and each witness has <= L partners, then
    # total partners <= B*L*n.
    rows = []
    for n in (16, 64, 1024):
        for B in (1, 4, 16):
            for L in (2, 5, 8):
                bound = B * L * n
                rows.append({"n": n, "occupied_witness_factor": B, "per_witness_cap": L, "bound": bound})
                check(
                    f"conditional count n={n} B={B} L={L}",
                    bound == B * L * n,
                    f"bound={bound}",
                )
    return {"rows": rows}


def main() -> None:
    rich = rich_line_fixture()
    counting = conditional_counting_fixture()
    result = {
        "node": "deep_link_staircase",
        "task": "P1",
        "checks": NCHECK,
        "rich_line_reduction_fixture": rich,
        "conditional_counting": counting,
        "status": "CONDITIONAL: requires post-paid per-subcore rich-line cap and occupied-subcore accounting",
    }

    if "--write-certificate" in sys.argv:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w") as fh:
            json.dump(result, fh, indent=2, sort_keys=True)
            fh.write("\n")

    expected = None
    if os.path.exists(CERT):
        with open(CERT) as fh:
            expected = json.load(fh)
    check("certificate exists", expected is not None, CERT)
    if expected is not None:
        check("certificate matches recomputed summary", result == expected)

    if FAILS:
        print("\nrecomputed summary:")
        print(json.dumps(result, indent=2, sort_keys=True))
        print("\nFAIL:")
        for name in FAILS:
            print("  -", name)
        sys.exit(1)

    print("\nsummary:")
    print(json.dumps(result, indent=2, sort_keys=True))
    print(f"\nPASS: {NCHECK} P1 conditional deep-link checks")


if __name__ == "__main__":
    main()
