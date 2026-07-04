#!/usr/bin/env python3
"""E36 verifier: PGL_2 stabilizer of 2-power multiplicative domains.

For toy prize-class rows q in {17, 97}, n = 2^a | q-1, and every distinct
coset domain alpha * mu_n, enumerate the PGL_2(F_q) set-stabilizer and verify
that it equals the expected dihedral group:

  x |-> zeta x,       zeta in mu_n
  x |-> alpha^2 zeta / x.

Rows with identical coset sets are deduplicated.  The stabilizer enumeration is
exact: a PGL_2 map is determined by the images of three domain points, so we
enumerate every ordered image triple and then test the induced map on the whole
domain.  Negative results publish identically: if any stabilizer is larger than
2n, the extra normalized matrices are printed and the verifier fails.

Stdlib only; no Monte Carlo.
Run: python3 experimental/scripts/verify_e36_pgl2_stabilizer.py
To refresh the pinned certificate:
  python3 experimental/scripts/verify_e36_pgl2_stabilizer.py --write-certificate
"""

from __future__ import annotations

from itertools import permutations
import json
import os
import sys
from dataclasses import dataclass


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CERT = os.path.join(
    REPO,
    "experimental",
    "data",
    "certificates",
    "e36-pgl2-stabilizer",
    "e36_pgl2_stabilizer.json",
)

INF = -1
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
        raise ZeroDivisionError("0 has no inverse")
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
    raise RuntimeError(f"no primitive root mod {p}")


def canonical_matrix(p: int, a: int, b: int, c: int, d: int) -> tuple[int, int, int, int]:
    vals = [a % p, b % p, c % p, d % p]
    scale = next((x for x in vals if x), None)
    if scale is None:
        raise ValueError("zero matrix")
    s = inv(p, scale)
    return tuple((s * x) % p for x in vals)  # type: ignore[return-value]


def act(p: int, M: tuple[int, int, int, int], x: int) -> int:
    a, b, c, d = M
    if x == INF:
        if c == 0:
            return INF
        return a * inv(p, c) % p
    den = (c * x + d) % p
    if den == 0:
        return INF
    return (a * x + b) * inv(p, den) % p


def nullspace_vector_3x4(p: int, rows: list[list[int]]) -> tuple[int, int, int, int]:
    """Return a nonzero kernel vector for a rank-3 3x4 matrix over F_p."""
    mat = [[x % p for x in row] for row in rows]
    pivots: list[int] = []
    r = 0
    for c in range(4):
        pivot = next((i for i in range(r, 3) if mat[i][c] % p), None)
        if pivot is None:
            continue
        mat[r], mat[pivot] = mat[pivot], mat[r]
        scale = inv(p, mat[r][c])
        mat[r] = [(scale * x) % p for x in mat[r]]
        for i in range(3):
            if i != r and mat[i][c] % p:
                factor = mat[i][c]
                mat[i] = [(mat[i][j] - factor * mat[r][j]) % p for j in range(4)]
        pivots.append(c)
        r += 1
        if r == 3:
            break
    if len(pivots) != 3:
        raise ValueError("triple constraints did not have rank 3")
    free = next(c for c in range(4) if c not in pivots)
    sol = [0, 0, 0, 0]
    sol[free] = 1
    for i in reversed(range(3)):
        c = pivots[i]
        sol[c] = (-mat[i][free]) % p
    return canonical_matrix(p, *sol)


def mobius_from_triples(
    p: int,
    xs: tuple[int, int, int],
    ys: tuple[int, int, int],
) -> tuple[int, int, int, int]:
    rows = []
    for x, y in zip(xs, ys):
        rows.append([x, 1, (-y * x) % p, -y])
    M = nullspace_vector_3x4(p, rows)
    if any(act(p, M, x) != y for x, y in zip(xs, ys)):
        raise AssertionError("computed Mobius map does not realize the triple")
    return M


def set_stabilizer(p: int, D: frozenset[int]) -> set[tuple[int, int, int, int]]:
    xs = tuple(sorted(D)[:3])
    stabilizer: set[tuple[int, int, int, int]] = set()
    for ys in permutations(sorted(D), 3):
        M = mobius_from_triples(p, xs, ys)
        if {act(p, M, x) for x in D} == set(D):
            stabilizer.add(M)
    return stabilizer


def mu_subgroup(p: int, n: int) -> set[int]:
    g = primitive_root(p)
    omega = pow(g, (p - 1) // n, p)
    return {pow(omega, i, p) for i in range(n)}


def domain(p: int, n: int, alpha: int) -> frozenset[int]:
    return frozenset((alpha * x) % p for x in mu_subgroup(p, n))


def dihedral_matrices(p: int, n: int, alpha: int) -> set[tuple[int, int, int, int]]:
    mu = mu_subgroup(p, n)
    out = set()
    for zeta in mu:
        out.add(canonical_matrix(p, zeta, 0, 0, 1))
        out.add(canonical_matrix(p, 0, (alpha * alpha * zeta) % p, 1, 0))
    return out


@dataclass(frozen=True)
class Row:
    p: int
    n: int
    alpha: int
    coset_label: str
    coset_index: int


def toy_rows() -> list[Row]:
    rows: list[Row] = []
    for p in (17, 97):
        g = primitive_root(p)
        n = 4
        while n <= p - 1:
            if (p - 1) % n == 0:
                for idx in range((p - 1) // n):
                    alpha = pow(g, idx, p)
                    label = "subgroup" if idx == 0 else f"coset-{idx}"
                    rows.append(Row(p, n, alpha, label, idx))
            n *= 2
    # Deduplicate rows whose alpha choices give the same set.
    seen: set[tuple[int, int, frozenset[int]]] = set()
    out: list[Row] = []
    for row in rows:
        key = (row.p, row.n, domain(row.p, row.n, row.alpha))
        if key not in seen:
            seen.add(key)
            out.append(row)
    return out


def check_row(row: Row) -> dict:
    D = domain(row.p, row.n, row.alpha)
    expected = dihedral_matrices(row.p, row.n, row.alpha)
    stabilizer = set_stabilizer(row.p, D)
    extra = sorted(stabilizer - expected)
    missing = sorted(expected - stabilizer)
    check(
        f"F_{row.p} n={row.n} {row.coset_label}: stabilizer is dihedral",
        not extra and not missing and len(stabilizer) == 2 * row.n,
        f"|stab|={len(stabilizer)}, |Dih|={len(expected)}, extra={len(extra)}, missing={len(missing)}",
    )
    return {
        "field": f"F_{row.p}",
        "n": row.n,
        "alpha": row.alpha,
        "coset_label": row.coset_label,
        "coset_index": row.coset_index,
        "domain_size": len(D),
        "enumeration": "ordered image triples of three domain points",
        "pgl2_size": row.p * (row.p * row.p - 1),
        "stabilizer_size": len(stabilizer),
        "expected_dihedral_size": len(expected),
        "extra_matrices": extra[:8],
        "missing_matrices": missing[:8],
    }


def main() -> None:
    rows = [check_row(row) for row in toy_rows()]
    result = {
        "node": "f_dih_subgroup_completeness",
        "task": "E36",
        "rows": rows,
        "exceptions": [row for row in rows if row["extra_matrices"] or row["missing_matrices"]],
        "checks": NCHECK,
    }

    expected = None
    if "--write-certificate" in sys.argv:
        os.makedirs(os.path.dirname(CERT), exist_ok=True)
        with open(CERT, "w") as fh:
            json.dump(result, fh, indent=2, sort_keys=True)
            fh.write("\n")

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
        for name in FAILS[:25]:
            print("  -", name)
        if len(FAILS) > 25:
            print(f"  ... {len(FAILS) - 25} more")
        sys.exit(1)

    print("\nsummary:")
    print(json.dumps(result, indent=2, sort_keys=True))
    print(f"\nPASS: {NCHECK} E36 PGL2 stabilizer checks")


if __name__ == "__main__":
    main()
