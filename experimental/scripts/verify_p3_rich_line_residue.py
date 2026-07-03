#!/usr/bin/env python3
"""P3 verifier: affine-net residue for the post-strip rich-line cap.

P1 reduced a fixed near-k subcore to rich points in an affine line arrangement
in parameters (z,a).  This verifier embeds the same obstruction on a 2-power
multiplicative domain and checks the intended rich supports against the current
local paid predicates: tangent pencil, quotient-with-tail, and dihedral
full-fiber staircase.

The result is a negative/conditional packet: the current strip does not by
itself prove a constant post-strip cap.  A new residue, the affine-net rich-line
residue, must be excluded or promoted to a paid class.
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
    "p3-rich-line-residue",
    "p3_rich_line_residue.json",
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


def primitive_root(p: int) -> int:
    factors = set()
    m = p - 1
    d = 2
    while d * d <= m:
        if m % d == 0:
            factors.add(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        factors.add(m)
    for g in range(2, p):
        if all(pow(g, (p - 1) // r, p) != 1 for r in factors):
            return g
    raise RuntimeError("no primitive root")


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


def multiplicative_domain(p: int, n: int) -> list[int]:
    g = primitive_root(p)
    omega = pow(g, (p - 1) // n, p)
    return [pow(omega, i, p) for i in range(n)]


def k_cosets(n: int, M: int) -> list[set[int]]:
    step = n // M
    return [{r + q * step for q in range(M)} for r in range(step)]


def quotient_tail_paid(indices: set[int], n: int, A: int, t: int) -> bool:
    """Natural local predicate for an X-4 quotient-tail support.

    The family has at least one full K_M-coset and, if b>0, one tail coset.
    Scales with h=0 are excluded here; otherwise every small support would be
    a vacuous tail inside the whole domain, which is not the staircase family.
    """
    for M in (1, 2, 4, 8, 16, 32, 64):
        if n % M or M <= t or M > A:
            continue
        h, b = divmod(A, M)
        if h < 1:
            continue
        cosets = k_cosets(n, M)
        full = [C for C in cosets if C <= indices]
        partial = [C for C in cosets if 0 < len(C & indices) < len(C)]
        if b == 0:
            if len(full) == h and not partial:
                return True
        else:
            if len(full) == h and len(partial) == 1 and len(partial[0] & indices) == b:
                return True
    return False


def inversion_closed(indices: set[int], n: int) -> bool:
    return {-i % n for i in indices} == indices


def dihedral_full_fiber_paid(indices: set[int], n: int, A: int, t: int) -> bool:
    """Local Chebyshev staircase predicate with at least one full dihedral fiber."""
    for M in (1, 2, 4, 8, 16, 32, 64):
        if n % M or M <= t or 2 * M > A:
            continue
        cosets = k_cosets(n, M)
        coset_id = {}
        for cid, C in enumerate(cosets):
            for i in C:
                coset_id[i] = cid
        paired = set()
        for cid, C in enumerate(cosets):
            inv_cid = coset_id[(-next(iter(C))) % n]
            if cid <= inv_cid:
                paired.add((cid, inv_cid))
        for c1, c2 in paired:
            fiber = cosets[c1] | cosets[c2]
            if fiber <= indices:
                return True
    return False


def build_fixture(m: int = 10, p: int = 193, n: int = 64) -> dict:
    k = 4
    t = 2
    A = k + t
    z0 = 0
    xs = multiplicative_domain(p, n)
    R_idx = [0, 1, 2]
    T0_extra_idx = [3, 4, 5]
    R_xs = [xs[i] for i in R_idx]
    h = vanishing_poly(p, R_xs)

    lines: list[tuple[str, int, int, int]] = []
    idx = A
    for i in range(1, m + 1):
        lines.append((f"H{i}", idx, i, 0))
        idx += 1
    for j in range(1, m + 1):
        lines.append((f"P{j}", idx, j, 1))
        idx += 1
    for ell in range(1, 2 * m + 1):
        lines.append((f"N{ell}", idx, ell, -1 % p))
        idx += 1

    intended: dict[tuple[int, int], list[str]] = {}
    for i in range(1, m + 1):
        for j in range(1, m + 1):
            ell = 2 * i - j
            z = (i - j) % p
            if 1 <= ell <= 2 * m and z != z0:
                intended[(z, i)] = [f"H{i}", f"P{j}", f"N{ell}"]

    # Fill the unused domain points with lines that avoid every intended rich
    # parameter, so the intended supports stay exactly 6 points.
    used = {line[1] for line in lines}
    for free_idx in range(A, n):
        if free_idx in used:
            continue
        for slope in range(2, p):
            for intercept in range(50, p):
                if all((intercept + slope * z - a) % p for (z, a) in intended):
                    lines.append((f"D{free_idx}", free_idx, intercept, slope))
                    used.add(free_idx)
                    break
            if free_idx in used:
                break

    u = {x: 0 for x in xs}
    v = {x: 0 for x in xs}
    label_to_index = {}
    for label, point_idx, intercept, slope in lines:
        x = xs[point_idx]
        hx = eval_poly(p, h, x)
        u[x] = intercept * hx % p
        v[x] = slope * hx % p
        label_to_index[label] = point_idx

    supports = []
    paid_quot = 0
    paid_dih = 0
    exact_six = 0
    verified = 0
    max_multiplicity = 0
    for (z, a), labs in intended.items():
        incident = []
        for label, point_idx, intercept, slope in lines:
            if (intercept + slope * z - a) % p == 0:
                incident.append(label)
        max_multiplicity = max(max_multiplicity, len(incident))
        support = set(R_idx) | {label_to_index[label] for label in incident}
        c_vals = {x: a * eval_poly(p, h, x) % p for x in xs}
        ok = all((u[xs[i]] + z * v[xs[i]] - c_vals[xs[i]]) % p == 0 for i in support)
        ok &= all((u[xs[i]] + z * v[xs[i]] - c_vals[xs[i]]) % p != 0 for i in T0_extra_idx)
        if ok:
            verified += 1
        if len(support) == A:
            exact_six += 1
        if quotient_tail_paid(support, n, A, t):
            paid_quot += 1
        if inversion_closed(support, n) or dihedral_full_fiber_paid(support, n, A, t):
            paid_dih += 1
        supports.append(sorted(support))

    direction_set = {slope % p for label, _, _, slope in lines if not label.startswith("D")}
    rich_count = len(intended)
    check("fixture uses a 2-power multiplicative domain", p == 193 and n == 64 and (p - 1) % n == 0)
    check("fixture has many intended rich parameters", rich_count > n, f"rich={rich_count}, n={n}")
    check("all intended rich parameters embed as aligned supports", verified == rich_count, f"verified={verified}")
    check("intended supports are exact A-point supports", exact_six == rich_count, f"exact={exact_six}")
    check("not a tangent pencil: no rich point has multiplicity > t+1", max_multiplicity == t + 1)
    check("not quotient-tail paid under the local full-coset predicate", paid_quot == 0)
    check("not dihedral paid under inversion/full-fiber predicates", paid_dih == 0)
    check("affine-net has three non-dummy directions", direction_set == {0, 1, p - 1}, f"directions={sorted(direction_set)}")

    return {
        "field": f"F_{p}",
        "domain": f"mu_{n}",
        "k": k,
        "t": t,
        "A": A,
        "line_family_parameter_m": m,
        "intended_rich_parameters": rich_count,
        "verified_aligned_supports": verified,
        "max_intended_multiplicity": max_multiplicity,
        "quotient_tail_paid_supports": paid_quot,
        "dihedral_paid_supports": paid_dih,
        "sample_supports": supports[:8],
        "named_residue": "p3_affine_net_richline_residue",
    }


def main() -> None:
    fixture = build_fixture()
    result = {
        "node": "deep_link_staircase",
        "task": "P3",
        "status": "CONDITIONAL/NEGATIVE: current paid strip does not prove the fixed-subcore rich-line cap",
        "fixture": fixture,
        "checks": NCHECK,
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
        print("\nFAIL:")
        for name in FAILS:
            print("  -", name)
        print(json.dumps(result, indent=2, sort_keys=True))
        sys.exit(1)
    print("\nsummary:")
    print(json.dumps(result, indent=2, sort_keys=True))
    print(f"\nPASS: {NCHECK} P3 rich-line residue checks")


if __name__ == "__main__":
    main()
