#!/usr/bin/env python3
r"""Verifier for experimental/notes/roadmaps/qx6_qx8_kms_bridges.md
(DAG nodes xr_e3_to_expansion + xr_junta_to_paid; queue items QX.6/QX.8).

Bridge 1 (E_3 <-> expansion), on J(6,3) and J(8,4):
  - Johnson spectrum: eigenvalues ((j-i)(n-j-i)-i)/d with multiplicities
    C(n,i)-C(n,i-1); exact unnormalized gap lam0-lam1 = n.
  - For a battery of structured + seeded-random sets A:
      (i)   walk identity: <1_A,(P_A M P_A)^k 1_A>/|V| equals the exact
            (Fraction-arithmetic) probability that a stationary k-step walk
            stays in A at all k+1 times (k = 0..3);
      (ii)  spectral cap E_k(A) <= mu(A) * lambda_max(M_A)^k;
      (iii) Rayleigh direction lambda_max(M_A) >= 1 - phi(A);
      (iv)  exact identity E_1(A) = mu(A)(1 - phi(A)) and monotonicity
            E_3 <= E_2 <= E_1 <= E_0 = mu;
      (v)   the bridge inequality phi(A) <= 1 - E_3(A)/mu(A) (exact);
      (vi)  Perron-Frobenius for the restricted operator:
            lambda_max(M_A) = spectral radius;
      (vii) lazy walk (I+M)/2: restricted operator PSD, exact identity
            E1_lazy = mu(1 - phi/2), Jensen lower bound
            Ek_lazy >= mu(1 - phi/2)^k.
  - Cell tightness: for junta cells Cell_C(tau) the escape degree is
    constant, phi equals the closed formula
    [t(n-j) + (d_core - t) j - t(d_core - t)] / (j(n-j)),
    lambda_max(M_A) = 1 - phi(A), and E_k = mu(1-phi)^k EXACTLY
    (equality in the spectral cap) -- dictators/fixed-core cells are
    extremal.  Non-cell battery sets show strict slack.
  - Counterexample: the naive direction "phi(A) <= 1 - lambda_max(M_A)"
    is FALSE: a depth-2 cell plus one far vertex violates it strictly.

Bridge 2 (junta => paid), exhaustive on J(8,4), domain D = {0..7}:
  - all cores C with |C| in {1,2}: cells partition V; cell sizes
    C(n-d,j-t); T -> T \ tau bijects Cell_C(tau) onto the (j-t)-subsets
    of D \ C; locator factorization l_T = g_tau * l_{T\tau} (exact
    integer polynomial arithmetic);
  - divisor/avoidance characterization, all (C,tau,T) exhaustively:
    T in Cell_C(tau)  <=>  g_tau | l_T  and  l_T(x) != 0 on C \ tau;
  - every union of cells is a junta, every junta over C is a union of
    cells (property checked exhaustively per junta); negative control:
    a cell minus one vertex is NOT a junta;
  - pigeonhole correlation transfer (raw + centered) for seeded random
    and structured alignment stand-ins against every junta.

Deterministic: single fixed seed SEED = 20260703.
Run: python3 experimental/scripts/verify_qx6_qx8_kms_bridges.py
Exit 0 iff every check PASSes.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb
import sys

import numpy as np

SEED = 20260703
TOL = 1e-9

_results: list[bool] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    _results.append(bool(ok))
    line = f"[{'PASS' if ok else 'FAIL'}] {name}"
    if detail:
        line += f"  |  {detail}"
    print(line)
    return ok


# ---------------------------------------------------------------- Johnson
def johnson(n: int, j: int):
    verts = [frozenset(c) for c in combinations(range(n), j)]
    index = {T: i for i, T in enumerate(verts)}
    V = len(verts)
    nbrs: list[list[int]] = [[] for _ in range(V)]
    for i, T in enumerate(verts):
        for y in T:
            for x in range(n):
                if x not in T:
                    nbrs[i].append(index[frozenset((T - {y}) | {x})])
    d = j * (n - j)
    assert all(len(nb) == d for nb in nbrs)
    A = np.zeros((V, V))
    for i, nb in enumerate(nbrs):
        for k in nb:
            A[i, k] = 1.0
    return verts, index, nbrs, d, A


def exact_stay_energies(Aset: set[int], nbrs, d: int, V: int, kmax: int,
                        lazy: bool = False) -> list[Fraction]:
    """E_k = P[X_0..X_k all in A], X_0 uniform on V, exact Fractions."""
    v = {x: Fraction(1, V) for x in Aset}
    energies = [sum(v.values(), Fraction(0))]
    for _ in range(kmax):
        w: dict[int, Fraction] = {}
        for x, px in v.items():
            if lazy:
                w[x] = w.get(x, Fraction(0)) + px / 2
                step = px / (2 * d)
            else:
                step = px / d
            for y in nbrs[x]:
                if y in Aset:
                    w[y] = w.get(y, Fraction(0)) + step
        v = w
        energies.append(sum(v.values(), Fraction(0)))
    return energies


def edge_expansion(Aset: set[int], nbrs, d: int) -> Fraction:
    cut = sum(1 for x in Aset for y in nbrs[x] if y not in Aset)
    return Fraction(cut, d * len(Aset))


def cell_vertices(verts, core: frozenset, tau: frozenset) -> set[int]:
    return {i for i, T in enumerate(verts) if T & core == tau}


def cell_phi_formula(n: int, j: int, dc: int, t: int) -> Fraction:
    return Fraction(t * (n - j) + (dc - t) * j - t * (dc - t), j * (n - j))


# ---------------------------------------------------------- Bridge 1 battery
def bridge1(n: int, j: int) -> None:
    print(f"\n=== Bridge 1 on J({n},{j}) ===")
    verts, index, nbrs, d, Adj = johnson(n, j)
    V = len(verts)
    M = Adj / d

    # --- Johnson spectrum ---
    eigs = np.linalg.eigvalsh(Adj)
    formula = [(j - i) * (n - j - i) - i for i in range(j + 1)]
    mult = [comb(n, i) - comb(n, i - 1) if i else 1 for i in range(j + 1)]
    ok = True
    for lam, m in zip(formula, mult):
        got = int(np.sum(np.abs(eigs - lam) < 1e-8))
        ok &= got == m
    check(f"J({n},{j}) spectrum = formula (mults {mult})", ok,
          f"|V|={V} deg={d} eigs {sorted(set(formula), reverse=True)}")
    check(f"J({n},{j}) exact gap lam0-lam1 = n", formula[0] - formula[1] == n,
          f"{formula[0]}-{formula[1]}={formula[0]-formula[1]}")

    # --- battery ---
    rng = np.random.default_rng(SEED)
    battery: list[tuple[str, set[int], tuple | None]] = []
    battery.append(("fixed-core cell {T:0 in T} (dictator)",
                    cell_vertices(verts, frozenset({0}), frozenset({0})),
                    (1, 1)))
    battery.append(("fixed-hole cell {T:0 not in T}",
                    cell_vertices(verts, frozenset({0}), frozenset()),
                    (1, 0)))
    battery.append(("depth-2 core cell {T:{0,1} sub T}",
                    cell_vertices(verts, frozenset({0, 1}), frozenset({0, 1})),
                    (2, 2)))
    battery.append(("mixed cell {T:0 in T,1 notin T}",
                    cell_vertices(verts, frozenset({0, 1}), frozenset({0})),
                    (2, 1)))
    battery.append(("closed ball B(v0,1)", {0} | set(nbrs[0]), None))
    for frac_name, size in (("quarter", max(2, V // 4)),
                            ("half", V // 2)):
        pick = set(int(x) for x in rng.choice(V, size=size, replace=False))
        battery.append((f"random {frac_name} (seeded, |A|={size})",
                        pick, None))

    print(f"{'set':44s} {'|A|':>4s} {'mu':>8s} {'phi':>8s} "
          f"{'lam_max':>8s} {'E_3':>10s} {'E3/(mu*lam^3)':>14s}")
    ratios: dict[str, float] = {}
    for name, Aset, cellinfo in battery:
        idx = sorted(Aset)
        a = len(idx)
        mu = Fraction(a, V)
        phi = edge_expansion(Aset, nbrs, d)
        B = M[np.ix_(idx, idx)]                    # compressed M_A
        ev = np.linalg.eigvalsh(B)
        lam_max, lam_min = float(ev[-1]), float(ev[0])
        E = exact_stay_energies(Aset, nbrs, d, V, 3)
        ones = np.ones(a)
        Enp = [float(ones @ np.linalg.matrix_power(B, k) @ ones) / V
               for k in range(4)]
        Elazy = exact_stay_energies(Aset, nbrs, d, V, 3, lazy=True)
        Blazy = (np.eye(a) + B) / 2
        evlazy = np.linalg.eigvalsh(Blazy)

        ratio = float(E[3]) / (float(mu) * lam_max ** 3) if lam_max > 0 else 0.0
        ratios[name] = ratio
        print(f"{name:44s} {a:4d} {float(mu):8.5f} {float(phi):8.5f} "
              f"{lam_max:8.5f} {float(E[3]):10.7f} {ratio:14.9f}")

        ok_i = all(abs(float(E[k]) - Enp[k]) < TOL for k in range(4))
        check(f"  (i) walk identity k=0..3 [{name}]", ok_i)
        ok_mono = E[3] <= E[2] <= E[1] <= E[0] == mu
        check(f"  (iv) monotone E_3<=E_2<=E_1<=E_0=mu [{name}]", ok_mono)
        check(f"  (iv) exact E_1 = mu(1-phi) [{name}]",
              E[1] == mu * (1 - phi))
        ok_cap = all(float(E[k]) <= float(mu) * lam_max ** k + TOL
                     for k in (1, 2, 3))
        check(f"  (ii) cap E_k <= mu lam_max^k [{name}]", ok_cap)
        check(f"  (iii) Rayleigh lam_max >= 1-phi [{name}]",
              lam_max >= float(1 - phi) - TOL,
              f"lam_max={lam_max:.6f} 1-phi={float(1-phi):.6f}")
        check(f"  (v) bridge phi <= 1 - E_3/mu [{name}]",
              phi <= 1 - E[3] / mu)
        check(f"  (vi) PF: lam_max = spectral radius [{name}]",
              lam_max >= abs(lam_min) - TOL)
        ok_lazy = (evlazy[0] >= -TOL
                   and Elazy[1] == mu * (1 - phi / 2)
                   and all(Elazy[k] >= mu * (1 - phi / 2) ** k
                           for k in range(4)))
        check(f"  (vii) lazy: PSD + E1=mu(1-phi/2) + Jensen [{name}]",
              ok_lazy)

        if cellinfo is not None:
            dc, t = cellinfo
            phif = cell_phi_formula(n, j, dc, t)
            check(f"  cell phi formula (d={dc},t={t}) [{name}]",
                  phi == phif, f"phi={phi}")
            check(f"  cell size C(n-d,j-t) [{name}]",
                  a == comb(n - dc, j - t))
            degs = {sum(1 for y in nbrs[x] if y in Aset) for x in Aset}
            check(f"  cell induced graph regular [{name}]", len(degs) == 1)
            check(f"  cell lam_max = 1-phi exactly [{name}]",
                  abs(lam_max - float(1 - phi)) < TOL)
            ok_eq = all(E[k] == mu * (1 - phi) ** k for k in range(4))
            check(f"  cell EQUALITY E_k = mu(1-phi)^k (cap tight) [{name}]",
                  ok_eq)

    # cells extremal, non-cells strictly slack
    cell_names = [nm for nm, _, ci in battery if ci is not None]
    noncell_names = [nm for nm, _, ci in battery if ci is None]
    check("cells achieve ratio E_3/(mu lam_max^3) = 1",
          all(abs(ratios[nm] - 1.0) < 1e-8 for nm in cell_names))
    worst = max(ratios[nm] for nm in noncell_names)
    check("non-cell battery sets strictly slack (ratio <= 0.99)",
          worst <= 0.99, f"max non-cell ratio = {worst:.6f}")

    # --- counterexample to the naive direction phi(A) <= 1 - lam_max ---
    cellD2 = cell_vertices(verts, frozenset({0, 1}), frozenset({0, 1}))
    far = index[frozenset(range(n - j, n))]        # T* = {n-j..n-1}, misses 0,1
    assert far not in cellD2
    assert all(far not in nbrs[x] for x in cellD2)
    Ax = cellD2 | {far}
    idx = sorted(Ax)
    phix = edge_expansion(Ax, nbrs, d)
    lamx = float(np.linalg.eigvalsh(M[np.ix_(idx, idx)])[-1])
    check("COUNTEREXAMPLE: phi(A) > 1 - lam_max(M_A) strictly "
          "(naive direction false)",
          float(phix) > 1 - lamx + 1e-6,
          f"A = depth-2 cell + far vertex: phi={phix}={float(phix):.6f} "
          f"> 1-lam_max={1-lamx:.6f}")


# ---------------------------------------------------------- polynomials (Z)
def poly_from_roots(roots) -> list[int]:
    p = [1]
    for r in roots:
        q = [0] * (len(p) + 1)
        for i, c in enumerate(p):
            q[i + 1] += c
            q[i] -= r * c
        p = q
    return p


def poly_mul(p: list[int], q: list[int]) -> list[int]:
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for k, b in enumerate(q):
            out[i + k] += a * b
    return out


def poly_divides(g: list[int], f: list[int]) -> bool:
    """g monic: exact division over Z; True iff remainder == 0."""
    assert g[-1] == 1
    f = list(f)
    dg = len(g) - 1
    if dg == 0:
        return True
    if len(f) - 1 < dg:
        return all(c == 0 for c in f)
    for i in range(len(f) - 1, dg - 1, -1):
        c = f[i]
        if c:
            for k in range(dg + 1):
                f[i - dg + k] -= c * g[k]
    return all(c == 0 for c in f[:dg])


def poly_eval(p: list[int], x: int) -> int:
    acc = 0
    for c in reversed(p):
        acc = acc * x + c
    return acc


# ---------------------------------------------------------------- Bridge 2
def bridge2(n: int = 8, j: int = 4) -> None:
    print(f"\n=== Bridge 2 on J({n},{j}), domain D = 0..{n-1}, "
          f"locators over Z ===")
    verts, index, nbrs, d, _ = johnson(n, j)
    V = len(verts)
    locator = [poly_from_roots(sorted(T)) for T in verts]

    n_div_checks = 0
    n_juntas = 0
    n_pigeon = 0
    all_ok_char = True
    all_ok_cells = True
    all_ok_junta = True
    all_ok_factor = True

    cores = ([frozenset(c) for c in combinations(range(n), 1)]
             + [frozenset(c) for c in combinations(range(n), 2)])

    # alignment stand-ins for the pigeonhole checks
    rng = np.random.default_rng(SEED)
    stands: list[tuple[str, set[int]]] = [
        ("cell {T:7 in T}", cell_vertices(verts, frozenset({7}),
                                          frozenset({7}))),
        ("2-junta {T: T cap {6,7} != empty}",
         {i for i, T in enumerate(verts) if T & {6, 7}}),
    ]
    for s in (10, 20, 35):
        stands.append((f"random |A|={s}",
                       set(int(x) for x in
                           rng.choice(V, size=s, replace=False))))

    for C in cores:
        dc = len(C)
        taus = [frozenset(t) for sz in range(dc + 1)
                for t in combinations(sorted(C), sz)]
        cells = {tau: cell_vertices(verts, C, tau) for tau in taus}

        # partition + sizes + bijection + factorization
        seen: set[int] = set()
        for tau, cell in cells.items():
            t = len(tau)
            if cell & seen:
                all_ok_cells = False
            seen |= cell
            if len(cell) != comb(n - dc, j - t):
                all_ok_cells = False
            image = {frozenset(verts[i] - tau) for i in cell}
            expect = {frozenset(s) for s in
                      combinations(sorted(set(range(n)) - C), j - t)}
            if image != expect or len(image) != len(cell):
                all_ok_cells = False
            g_tau = poly_from_roots(sorted(tau))
            for i in cell:
                rest = poly_from_roots(sorted(verts[i] - tau))
                if poly_mul(g_tau, rest) != locator[i]:
                    all_ok_factor = False
        if seen != set(range(V)):
            all_ok_cells = False

        # divisor/avoidance characterization, exhaustive over (tau, T)
        for tau in taus:
            g_tau = poly_from_roots(sorted(tau))
            holes = sorted(C - tau)
            for i, T in enumerate(verts):
                lhs = (T & C == tau)
                rhs = (poly_divides(g_tau, locator[i])
                       and all(poly_eval(locator[i], x) != 0 for x in holes))
                n_div_checks += 1
                if lhs != rhs:
                    all_ok_char = False

        # all unions of cells are juntas; recovery unique; pigeonhole
        ncells = len(taus)
        for mask in range(1 << ncells):
            S = [taus[b] for b in range(ncells) if (mask >> b) & 1]
            junta = set().union(*(cells[tau] for tau in S)) if S else set()
            n_juntas += 1
            # junta property: membership depends only on T cap C
            member = {}
            for i, T in enumerate(verts):
                key = T & C
                inA = i in junta
                if key in member and member[key] != inA:
                    all_ok_junta = False
                member[key] = inA
            # recovery: cells with nonempty intersection are contained
            recovered = [tau for tau in taus
                         if cells[tau] and cells[tau] <= junta]
            spurious = [tau for tau in taus
                        if cells[tau] and not cells[tau] <= junta
                        and (cells[tau] & junta)]
            rec_union = set().union(*(cells[t2] for t2 in recovered)) \
                if recovered else set()
            if spurious or rec_union != junta or len(recovered) > 2 ** dc:
                all_ok_junta = False
            if not junta:
                continue
            for _, stand in stands:
                m = len(stand & junta)
                best = max(len(stand & cells[tau]) for tau in taus)
                n_pigeon += 1
                if Fraction(best) < Fraction(m, 2 ** dc):
                    all_ok_junta = False
                # centered version
                muA = Fraction(len(stand), V)
                excess = Fraction(m) - muA * len(junta)
                bestex = max(Fraction(len(stand & cells[tau]))
                             - muA * len(cells[tau]) for tau in taus)
                if bestex < excess / (2 ** dc):
                    all_ok_junta = False

    check(f"cells partition V, sizes C(n-d,j-t), bijection to J(n-d,j-t) "
          f"[{len(cores)} cores]", all_ok_cells)
    check("locator factorization l_T = g_tau * l_(T minus tau), all cells",
          all_ok_factor)
    check("divisor/avoidance characterization, exhaustive",
          all_ok_char, f"{n_div_checks} (C,tau,T) triples")
    check("unions of cells are exactly the juntas; recovery unique; "
          "pigeonhole (raw+centered)",
          all_ok_junta,
          f"{n_juntas} juntas x {len(stands)} stand-ins, "
          f"{n_pigeon} pigeonhole checks")

    # negative control: a cell minus one vertex is NOT a junta
    C0 = frozenset({0})
    cell = cell_vertices(verts, C0, C0)
    broken = set(sorted(cell)[1:])
    is_junta = True
    member = {}
    for i, T in enumerate(verts):
        key = T & C0
        inA = i in broken
        if key in member and member[key] != inA:
            is_junta = False
        member[key] = inA
    check("negative control: cell minus one vertex FAILS junta property",
          not is_junta)

    # headline numbers
    dict_cell = cell_vertices(verts, frozenset({0}), frozenset({0}))
    print(f"key numbers: |V|={V}, dictator cell size {len(dict_cell)} "
          f"(mu={Fraction(len(dict_cell), V)}), cores checked {len(cores)}, "
          f"max cells/core {2**2}")


def main() -> None:
    print("verify_qx6_qx8_kms_bridges: Bridges 1 & 2 "
          "(xr_e3_to_expansion, xr_junta_to_paid)")
    print(f"deterministic seed = {SEED}")
    bridge1(6, 3)
    bridge1(8, 4)
    bridge2(8, 4)
    n_pass = sum(_results)
    n_all = len(_results)
    print(f"\n{'ALL CHECKS PASS' if all(_results) else 'FAILURES PRESENT'} "
          f"({n_pass}/{n_all})")
    sys.exit(0 if all(_results) else 1)


if __name__ == "__main__":
    main()
