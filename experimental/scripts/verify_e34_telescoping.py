#!/usr/bin/env python3
"""Verifier for experimental/notes/roadmaps/e34_telescoping_check.md (E34).

Wave-5 probe E34: the jointness telescoping check (face 1 of the rigidity
kernel; DAG node tr_joint_telescope).

Model: the exact linear slope-image model of E6 / the M4 verifier
(verify_gap1_terminal_reserve.py rows F13-*): data on a K_M-stable support
S -> interpolant -> value at alpha; every count below is the exact size
p^rank of an F_p-linear image (no degree cut, no fixed received word --
same caveats as E6/M4).

For each toy row, each K_M-stable support S, and each nonempty active
character set R subseteq Z/M, three exact columns:

  joint(S,R) = p^rk{ P_U(alpha) : U = sum_{r in R} U_r, each U_r
               r-isotypic w.r.t. K_M, base amplitudes }   (actual object)
  prod(S,R)  = prod_{r in R} p^rk{ P_{U_r}(alpha) }       (Conjecture TR's
                                                           bound target)
  tel(S,R)   = p^rk{ P_V(alpha) : V r_0-isotypic w.r.t. the JOINT
               STABILIZER K_D }, D := gcd(M, {r-r' : r,r' in R}); all
               r in R are congruent to r_0 mod D, so this is ONE
               quotient-row instance at the joint subgroup.

Checks per toy row (exit 0 iff all PASS):
  V1: joint <= tel in EVERY cell, via explicit span containment
      (rank(tel gens + joint gens) == rank(tel gens)).  Any violation
      falsifies tr_joint_telescope's candidate; the cell is printed.
  V2: every FULL-CLASS cell (|R| = M/D, R a whole congruence class mod D)
      has joint == tel (exact telescoping) and tel <= prod.
  V3: tel > prod (lossy telescope) happens ONLY in sparse cells
      (|R| < M/D).
  V4: singleton R: joint == tel == prod (telescope degenerates to the
      per-character instance itself).
  V5: census regression pin
      (cells, full, exact, chain, gain, lossy, gain_full).
"""
import math
import sys
from functools import reduce

RESULTS = []


def report(name, ok, detail):
    RESULTS.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


# ------------------------------------------------ F_p[X]/(X^e - c)
def make_field(p, e, c):
    def mul(u, v):
        w = [0] * (2 * e - 1)
        for i, a in enumerate(u):
            if a:
                for j, b in enumerate(v):
                    w[i + j] = (w[i + j] + a * b) % p
        for d in range(2 * e - 2, e - 1, -1):
            if w[d]:
                w[d - e] = (w[d - e] + c * w[d]) % p
                w[d] = 0
        return tuple(w[:e])
    return mul


def fpow(u, k, mul, e):
    r = (1,) + (0,) * (e - 1)
    while k:
        if k & 1:
            r = mul(r, u)
        u = mul(u, u)
        k >>= 1
    return r


def check_irreducible(p, e, mul):
    """X^e - c irreducible over F_p: X^(p^e) == X and X^(p^d) != X for
    every proper divisor d of e (valid for prime-power e; here e in
    {2, 4})."""
    x = (0, 1) + (0,) * (e - 2)
    if fpow(x, p ** e, mul, e) != x:
        return False
    return all(fpow(x, p ** d, mul, e) != x
               for d in range(1, e) if e % d == 0)


def smul(s, v, p):
    return tuple(s * z % p for z in v)


def vadd(u, v, p):
    return tuple((a + b) % p for a, b in zip(u, v))


def rank_fp(vectors, p):
    rows = [list(v) for v in vectors if any(v)]
    ncols = len(rows[0]) if rows else 0
    rank, col = 0, 0
    while col < ncols and rows:
        piv = next((i for i, r in enumerate(rows) if r[col] % p), None)
        if piv is None:
            col += 1
            continue
        rows[0], rows[piv] = rows[piv], rows[0]
        inv = pow(rows[0][col], p - 2, p)
        rows[0] = [(inv * z) % p for z in rows[0]]
        for r in rows[1:]:
            f = r[col]
            if f:
                for cc in range(col, ncols):
                    r[cc] = (r[cc] - f * rows[0][cc]) % p
        rank += 1
        rows = rows[1:]
        col += 1
    return rank


def lagrange_at_alpha(S, p, e, mul):
    """L_x(alpha) for each x in S subset F_p; alpha = X in F_p[X]/(X^e-c)."""
    out = {}
    for x in S:
        num = (1,) + (0,) * (e - 1)
        den = 1
        for y in S:
            if y == x:
                continue
            num = mul(num, ((-y) % p, 1) + (0,) * (e - 2))  # alpha - y
            den = den * (x - y) % p
        out[x] = smul(pow(den, p - 2, p), num, p)
    return out


# ------------------------------------------------------------ census
def run_toy(label, p, n, omega, e, c, M, pins):
    mul = make_field(p, e, c)
    alpha = (0, 1) + (0,) * (e - 2)
    assert pow(omega, n, p) == 1 and all(
        pow(omega, i, p) != 1 for i in range(1, n)), "ord(omega) != n"
    assert check_irreducible(p, e, mul), "X^e - c not irreducible"
    assert not any(fpow(alpha, M, mul, e)[1:]), "alpha^M not in F_p"
    zeta = pow(omega, n // M, p)
    seen, cosets = set(), []
    for i in range(n):
        x = pow(omega, i, p)
        if x in seen:
            continue
        cs = [x * pow(zeta, j, p) % p for j in range(M)]
        seen.update(cs)
        cosets.append(cs)              # cs[i] = rep * zeta^i
    zero = (0,) * e
    keys = ("cells", "full", "exact", "chain", "gain", "lossy", "gain_full")
    cens = dict.fromkeys(keys, 0)
    bad = {k: [] for k in ("V1", "V2", "V3", "V4")}
    max_lossy = 0
    for mask in range(1, 1 << len(cosets)):
        sel = [cs for i, cs in enumerate(cosets) if mask >> i & 1]
        S = [x for cs in sel for x in cs]
        L = lagrange_at_alpha(S, p, e, mul)
        vecs, rk = {}, {}
        for r in range(M):
            vr = []
            for cs in sel:
                v = zero
                for i, x in enumerate(cs):
                    v = vadd(v, smul(pow(zeta, r * i, p), L[x], p), p)
                vr.append(v)
            vecs[r] = vr
            rk[r] = rank_fp(vr, p)
        for rmask in range(1, 1 << M):
            R = [r for r in range(M) if rmask >> r & 1]
            D = reduce(math.gcd, (r - R[0] for r in R[1:]), M)
            eta, r0 = pow(zeta, M // D, p), R[0] % D
            tel_vecs = []
            for cs in sel:
                for s in range(M // D):
                    u = zero
                    for ip in range(D):
                        u = vadd(u, smul(pow(eta, r0 * ip, p),
                                         L[cs[s + (M // D) * ip]], p), p)
                    tel_vecs.append(u)
            joint_vecs = [v for r in R for v in vecs[r]]
            rk_tel = rank_fp(tel_vecs, p)
            rk_joint = rank_fp(joint_vecs, p)
            rk_prod = sum(rk[r] for r in R)
            contained = rank_fp(tel_vecs + joint_vecs, p) == rk_tel
            full = len(R) == M // D
            cell = (tuple(sorted(S)), tuple(R), D,
                    rk_joint, rk_tel, rk_prod)
            cens["cells"] += 1
            cens["full"] += full
            cens["exact"] += rk_joint == rk_tel
            cens["chain"] += rk_joint <= rk_tel <= rk_prod
            cens["gain"] += rk_tel < rk_prod
            cens["lossy"] += rk_tel > rk_prod
            cens["gain_full"] += full and rk_tel < rk_prod
            if rk_tel > rk_prod:
                max_lossy = max(max_lossy, rk_tel - rk_prod)
            if not (rk_joint <= rk_tel and contained):
                bad["V1"].append(cell)
            if full and not (rk_joint == rk_tel and rk_tel <= rk_prod):
                bad["V2"].append(cell)
            if full and rk_tel > rk_prod:
                bad["V3"].append(cell)
            if len(R) == 1 and not (rk_joint == rk_tel == rk_prod):
                bad["V4"].append(cell)
    t = tuple(cens[k] for k in keys)
    print(f"  {label} census (cells, full, exact, chain, gain, lossy, "
          f"gain_full) = {t}, max lossy excess exponent = {max_lossy}")

    def first(k):
        return f"; first cell (S, R, D, rk_joint, rk_tel, rk_prod) = " \
               f"{bad[k][0]}" if bad[k] else ""
    report(f"{label} V1 joint<=tel + span containment", not bad["V1"],
           f"{cens['cells']} cells, violations={len(bad['V1'])}"
           + first("V1"))
    report(f"{label} V2 full-class exact telescoping", not bad["V2"],
           f"{cens['full']} full-class cells, joint==tel<=prod "
           f"violations={len(bad['V2'])}" + first("V2"))
    report(f"{label} V3 tel>prod only when sparse", not bad["V3"],
           f"lossy cells={cens['lossy']} (max excess exponent "
           f"{max_lossy}), full-class lossy={len(bad['V3'])}" + first("V3"))
    report(f"{label} V4 singleton degeneracy", not bad["V4"],
           f"violations={len(bad['V4'])}" + first("V4"))
    report(f"{label} V5 census pin", t == pins,
           f"observed {t}, pinned {pins}")


def main():
    print("E34 telescoping verifier (stdlib, deterministic)")
    # (label, p, n, omega, e, c, M, pinned census) -- F = F_p[X]/(X^e - c),
    # alpha = X, H_n = <omega>.  F13 rows reuse the M4 toy (alpha = sqrt 2,
    # a DEGENERATE tower for M=4: [F:B] = 2 < M).  F17 row is the
    # non-degenerate robustness row: alpha^4 = 3, [F:B] = 4 = M.
    run_toy("F13-M2", 13, 12, 2, 2, 2, 2, (189, 189, 189, 189, 0, 0, 0))
    run_toy("F13-M4", 13, 12, 2, 2, 2, 4, (105, 49, 105, 105, 49, 0, 21))
    run_toy("F17-M4", 17, 16, 3, 4, 3, 4, (225, 105, 105, 105, 0, 120, 0))
    n_pass = sum(RESULTS)
    print(f"== {n_pass}/{len(RESULTS)} PASS ==")
    sys.exit(0 if all(RESULTS) else 1)


if __name__ == "__main__":
    main()
