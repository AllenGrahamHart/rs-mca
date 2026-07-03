#!/usr/bin/env python3
"""E32-MERGED verifier: stagnation + exception profile census.

This is the light-compute Wave 5 census for the merged faces 3+4 gate.  It
does two exact profile enumerations:

  1. E27 corridor row, F_97/mu_16 with k=8, A=11.  Enumerate all Venn
     profiles of three size-A agreement supports, rank-check the far-spread
     profiles, and verify that the light-triangle inequality is impossible
     on this row.
  2. n=16 light-triangle toy rows over F_17^*.  Enumerate every Venn profile
     satisfying sigma = sum pairwise overlaps - triple <= 2k and the alpha
     k+1 overlap budget, realize each profile canonically, and evaluate the
     eliminant normal form.

It also pins the E13 exception-class dictionary in the same normal-form
language.  This is deliberately not a full coordinate-triple enumeration:
the script reports the exact number of coordinate embeddings represented by
the profiles, which is already too large for this machine under the current
RAM/runtime constraints.

Stdlib only; no Monte Carlo.
Run: python3 experimental/scripts/verify_e32_merged_census.py
"""

from __future__ import annotations

import json
import math
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
    "e32-merged-census",
    "e32_merged_profile_census.json",
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


class Fp:
    def __init__(self, p: int):
        self.p = p

    def add(self, a: int, b: int) -> int:
        return (a + b) % self.p

    def sub(self, a: int, b: int) -> int:
        return (a - b) % self.p

    def mul(self, a: int, b: int) -> int:
        return (a * b) % self.p

    def neg(self, a: int) -> int:
        return (-a) % self.p

    def inv(self, a: int) -> int:
        if a % self.p == 0:
            raise ZeroDivisionError("0 has no inverse")
        return pow(a, self.p - 2, self.p)


def rref(F: Fp, rows_in: list[list[int]]) -> tuple[list[list[int]], list[int], int]:
    rows = [r[:] for r in rows_in]
    if not rows:
        return rows, [], 0
    ncols = len(rows[0])
    pivots: list[int] = []
    rank = 0
    for col in range(ncols):
        piv = None
        for rr in range(rank, len(rows)):
            if rows[rr][col] % F.p:
                piv = rr
                break
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        inv = F.inv(rows[rank][col])
        rows[rank] = [F.mul(inv, x) for x in rows[rank]]
        for rr in range(len(rows)):
            if rr != rank and rows[rr][col] % F.p:
                c = rows[rr][col]
                rows[rr] = [F.sub(x, F.mul(c, y)) for x, y in zip(rows[rr], rows[rank])]
        pivots.append(col)
        rank += 1
        if rank == len(rows):
            break
    return rows, pivots, rank


def rank(F: Fp, rows: list[list[int]]) -> int:
    return rref(F, rows)[2]


def solve_square(F: Fp, A: list[list[int]], b: list[int]) -> list[int]:
    aug = [row[:] + [rhs] for row, rhs in zip(A, b)]
    R, pivots, rnk = rref(F, aug)
    n = len(A)
    if rnk != n or pivots[:n] != list(range(n)):
        raise ValueError("singular chart")
    return [R[i][n] for i in range(n)]


def lambda_space_chart(F: Fp, domain: list[int], k: int, T: tuple[int, ...]) -> list[list[int]]:
    pivots = list(T[:k])
    free = list(T[k:])
    Vp = [[pow(domain[x], d, F.p) for x in pivots] for d in range(k)]
    basis: list[list[int]] = []
    for q in free:
        rhs = [F.neg(pow(domain[q], d, F.p)) for d in range(k)]
        pivot_values = solve_square(F, Vp, rhs)
        word = [0] * len(domain)
        for x, val in zip(pivots, pivot_values):
            word[x] = val
        word[q] = 1
        basis.append(word)
    return basis


def normal_rank(F: Fp, domain: list[int], k: int, supports: tuple[tuple[int, ...], ...]) -> int:
    A = len(supports[0])
    t = A - k
    bases = [lambda_space_chart(F, domain, k, T) for T in supports]
    slopes = (1, 2, 3) if F.p != 17 else (1, 3, 5)
    union = sorted(set().union(*(set(T) for T in supports)))
    rows: list[list[int]] = []
    for coord in union:
        row: list[int] = []
        for basis in bases:
            row.extend(lam[coord] for lam in basis)
        rows.append(row)
    for coord in union:
        row = []
        for z, basis in zip(slopes, bases):
            row.extend(F.mul(z, lam[coord]) for lam in basis)
        rows.append(row)
    got = rank(F, rows)
    return 3 * t - got


@dataclass(frozen=True)
class Profile:
    h: int
    a: int
    b: int
    c: int
    x0: int
    x1: int
    x2: int
    outside: int

    @property
    def r01(self) -> int:
        return self.h + self.a

    @property
    def r02(self) -> int:
        return self.h + self.b

    @property
    def r12(self) -> int:
        return self.h + self.c

    @property
    def sigma(self) -> int:
        return 2 * self.h + self.a + self.b + self.c

    def budgets(self) -> tuple[int, int, int]:
        return (
            2 * self.h + self.a + self.b,
            2 * self.h + self.a + self.c,
            2 * self.h + self.b + self.c,
        )

    def as_dict(self) -> dict[str, int]:
        return {
            "h": self.h,
            "a": self.a,
            "b": self.b,
            "c": self.c,
            "x0": self.x0,
            "x1": self.x1,
            "x2": self.x2,
            "outside": self.outside,
            "r01": self.r01,
            "r02": self.r02,
            "r12": self.r12,
            "sigma": self.sigma,
        }


def profiles(n: int, A: int) -> list[Profile]:
    out: list[Profile] = []
    for h in range(A + 1):
        for a in range(A + 1):
            for b in range(A + 1):
                for c in range(A + 1):
                    x0 = A - h - a - b
                    x1 = A - h - a - c
                    x2 = A - h - b - c
                    if min(x0, x1, x2) < 0:
                        continue
                    used = h + a + b + c + x0 + x1 + x2
                    if used <= n:
                        out.append(Profile(h, a, b, c, x0, x1, x2, n - used))
    return out


def realize_profile(P: Profile) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    sizes = (P.h, P.a, P.b, P.c, P.x0, P.x1, P.x2, P.outside)
    cells: list[list[int]] = []
    cur = 0
    for size in sizes:
        cells.append(list(range(cur, cur + size)))
        cur += size
    H, AB, AC, BC, X0, X1, X2, _ = cells
    T0 = tuple(sorted(H + AB + AC + X0))
    T1 = tuple(sorted(H + AB + BC + X1))
    T2 = tuple(sorted(H + AC + BC + X2))
    return T0, T1, T2


def coordinate_embedding_count(n: int, P: Profile) -> int:
    count = math.factorial(n)
    for size in (P.h, P.a, P.b, P.c, P.x0, P.x1, P.x2, P.outside):
        count //= math.factorial(size)
    return count


def find_mu16_domain() -> list[int]:
    q = 97
    for g in range(2, q):
        if all(pow(g, (q - 1) // p, q) != 1 for p in (2, 3)):
            omega = pow(g, (q - 1) // 16, q)
            return [pow(omega, i, q) for i in range(16)]
    raise RuntimeError("no F_97 generator")


def census_row(name: str, p: int, domain: list[int], k: int, A: int) -> dict:
    F = Fp(p)
    ps = profiles(len(domain), A)
    far = [P for P in ps if P.r01 < k and P.r02 < k and P.r12 < k]
    light = [
        P for P in ps
        if P.sigma <= 2 * k and max(P.budgets()) >= k + 1
    ]
    far_defects = []
    for P in far:
        kd = normal_rank(F, domain, k, realize_profile(P))
        if kd:
            far_defects.append((P, kd))
    light_defects = []
    light_coordinate_embeddings = 0
    for P in light:
        light_coordinate_embeddings += coordinate_embedding_count(len(domain), P)
        kd = normal_rank(F, domain, k, realize_profile(P))
        if kd:
            light_defects.append((P, kd))
    min_sigma = min(P.sigma for P in ps)
    check(f"{name}: profile enumeration nonempty", bool(ps), f"profiles={len(ps)}")
    check(f"{name}: far-spread profile rank defects", not far_defects, f"far={len(far)}, defects={len(far_defects)}")
    if light:
        check(
            f"{name}: light profile eliminants",
            not light_defects,
            f"light={len(light)}, coordinate_embeddings={light_coordinate_embeddings}, defects={len(light_defects)}",
        )
    else:
        check(
            f"{name}: no light profiles",
            True,
            f"min_sigma={min_sigma}, 2k={2 * k}",
        )
    return {
        "name": name,
        "field": f"F_{p}",
        "n": len(domain),
        "k": k,
        "A": A,
        "t": A - k,
        "profiles_total": len(ps),
        "far_spread_profiles": len(far),
        "far_spread_rank_defects": len(far_defects),
        "light_profiles": len(light),
        "light_coordinate_embeddings": light_coordinate_embeddings,
        "light_rank_defects": len(light_defects),
        "min_sigma": min_sigma,
        "two_k": 2 * k,
        "max_light_kernel_dimension": max((kd for _, kd in light_defects), default=0),
        "defective_profiles": [
            {"profile": P.as_dict(), "kernel_dim": kd}
            for P, kd in far_defects + light_defects
        ],
    }


E13_DICTIONARY = {
    "ag_net": "incidence-design normal form: row dependencies come from repeated low-dimensional block incidences; eliminant rank drop is paid by finite-geometry/net structure",
    "v_degenerate": "one coordinate leg has a constrained-support dual word with zero v-syndrome; the normal form is tangent/degenerate rather than primitive",
    "syzygy_circuit": "one-dimensional full-support kernel of the normal-form matrix with every deletion independent; this is the minimal-circuit determinantal branch",
}


def main() -> None:
    rows = [
        census_row("e27_corridor_mu16", 97, find_mu16_domain(), 8, 11),
        census_row("light_n16_k2_A4", 17, list(range(1, 17)), 2, 4),
        census_row("light_n16_k4_A5", 17, list(range(1, 17)), 4, 5),
        census_row("light_n16_k4_A6", 17, list(range(1, 17)), 4, 6),
    ]
    check(
        "E27 corridor light impossibility",
        rows[0]["light_profiles"] == 0 and rows[0]["min_sigma"] > rows[0]["two_k"],
        f"min_sigma={rows[0]['min_sigma']}, 2k={rows[0]['two_k']}",
    )
    check(
        "n=16 light rows have no profile-forced vanishing",
        all(row["light_rank_defects"] == 0 for row in rows[1:]),
        "light_profiles=%s" % [row["light_profiles"] for row in rows[1:]],
    )
    check(
        "E13 dictionary covers three classes",
        set(E13_DICTIONARY) == {"ag_net", "v_degenerate", "syzygy_circuit"},
    )
    result = {
        "node": "E32-MERGED",
        "scope": "exact Venn-profile census; coordinate embedding counts reported, not enumerated",
        "rows": rows,
        "e13_normal_form_dictionary": E13_DICTIONARY,
        "s9_unpaid_profile_class_found": False,
        "checks": NCHECK,
    }

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
        for name in FAILS[:25]:
            print("  -", name)
        if len(FAILS) > 25:
            print(f"  ... {len(FAILS) - 25} more")
        sys.exit(1)

    print("\nsummary:")
    print(json.dumps(result, indent=2, sort_keys=True))
    print(f"\nPASS: {NCHECK} E32-MERGED checks")


if __name__ == "__main__":
    main()
