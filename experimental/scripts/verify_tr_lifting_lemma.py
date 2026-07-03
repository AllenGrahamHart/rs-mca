#!/usr/bin/env python3
"""Verifier for experimental/notes/roadmaps/tr_lifting_lemma.md (Lifting Lemma).

Aligned analogue of the E34 census (verify_e34_telescoping.py): instead of
linear-model rank counts, enumerate the ACTUAL aligned sets of Conjecture TR
(gap1_terminal_reserve.md sect. 4) -- real codeword enumeration (deg < k),
real received words w, real K_M-stable agreement sets -- and check the
Lifting Lemma cell by cell.

Per row (F13-M2 / F13-M4 from the M4 packet; F17-M4 the non-degenerate
robustness row), per deterministic word w, per threshold A, per nonempty
R subseteq Z/M with D = gcd(M, {r-r'}), r0 = R[0] mod D, Rbar = the full
congruence class of r0 mod D inside Z/M:

  C     = {c in RS : Agr(c,w) K_M-stable, |Agr| >= A}    (shared ensemble)
  J_R   = {(alpha^r G_r(beta))_{r in R} : c in C}        (joint aligned data)
  T     = {alpha^r0 H_r0(gamma) : c in C}, gamma = alpha^D  (telescoped
          values, computed INDEPENDENTLY from the mod-D coefficient grouping)
  A_gen = same values over the WEAKER ensemble C_D = {Agr(c,w) K_D-stable,
          |Agr| >= A}   (the genuine scale-D single-instance aligned set)

Checks (exit 0 iff all PASS):
  LLV0: tower profile -- non-degeneracy [K(alpha^D):K] = M/D per divisor D
        matches the pinned expectation (rank test over F_p; K = B = F_p in
        all three rows).
  LLV1: pointwise identity (Lemma LL1) -- for EVERY qualifying codeword and
        every (D, r0): sum_{r in Rbar} alpha^r G_r(beta) ==
        alpha^r0 H_r0(gamma), two independent coefficient groupings.
  LLV2: set identity (Theorem LL(ii)) -- sigma(J_Rbar) == T in every cell.
  LLV3: Theorem LL(i) -- J_R is the coordinate projection of J_Rbar
        (R subseteq Rbar), so |J_R| <= |J_Rbar|.
  LLV4: Theorem LL(iii) count transfer -- |T| == |J_Rbar| in every
        NON-degenerate cell; degenerate cells get only |T| <= |J_Rbar|
        (collision cells counted and pinned: a collision there is the
        expected degenerate loss, not a failure).
  LLV5: Theorem LL(iv) -- ensemble nesting C subseteq C_D (K_M-stable =>
        K_D-stable, from independent rotation tests) and T subseteq A_gen
        in every cell; strict cells counted (flag F1 of the note).
  LLV6: census regression pin + nonvacuity (>= 1 (w,A) pair with >= 2
        qualifying codewords, so the joint data is not all singletons).

Deterministic, stdlib only, < 60 s.
"""
import math
import sys
from functools import reduce

RESULTS = []


def report(name, ok, detail):
    RESULTS.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


# ---------------------------------------------- F_p[X]/(X^e - c) (as E34)
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


# ------------------------------------------------------------- one row
def run_row(label, p, n, omega, e, cc, M, k, A_list, nondeg_pin, pins):
    mul = make_field(p, e, cc)
    zero, alpha = (0,) * e, (0, 1) + (0,) * (e - 2)
    assert pow(omega, n, p) == 1 and all(
        pow(omega, i, p) != 1 for i in range(1, n)), "ord(omega) != n"
    assert check_irreducible(p, e, mul), "X^e - cc not irreducible"
    beta = fpow(alpha, M, mul, e)
    assert not any(beta[1:]), "alpha^M not in F_p"
    beta_i = beta[0]
    H = [pow(omega, i, p) for i in range(n)]
    divs = [d for d in range(1, M + 1) if M % d == 0]
    apow = {r: fpow(alpha, r, mul, e) for r in range(M)}
    gampow = {}
    for D in divs:
        g, cur, lst = fpow(alpha, D, mul, e), (1,) + (0,) * (e - 1), []
        for _ in range((k - 1) // D + 1):
            lst.append(cur)
            cur = mul(cur, g)
        gampow[D] = lst
    nondeg = {D: rank_fp([fpow(alpha, D * s, mul, e)
                          for s in range(M // D)], p) == M // D
              for D in divs}
    report(f"{label} LLV0 tower profile", nondeg == nondeg_pin,
           f"nondeg by D = {nondeg} (pinned {nondeg_pin})")

    # ---- value table for ALL p^k codewords (coeff idx: little-endian)
    pw = [[pow(x, i, p) for i in range(k)] for x in H]
    def decode(idx):
        return [(idx // p ** i) % p for i in range(k)]
    vals = []
    for idx in range(p ** k):
        cs = decode(idx)
        vals.append(bytes(sum(cf * pwx[i] for i, cf in enumerate(cs)) % p
                          for pwx in pw))

    def evalvec(cs):
        return bytes(sum(cf * pwx[i] for i, cf in enumerate(cs)) % p
                     for pwx in pw)

    # ---- 4 deterministic words
    cstar = [(3 * i + 1) % p for i in range(k)]
    c2 = [(5 * i * i + 2) % p for i in range(k)]
    # c3 = cstar + (2, 0, -1, 0, ...): on a degenerate tower with
    # alpha^2 = 2 scalar (F13 rows) this is built to sigma-collide with
    # cstar in the (D=2, r0=0) class: 2 + 2*(-1) = 0.
    c3 = [(cstar[i] + (2 if i == 0 else p - 1 if i == 2 else 0)) % p
          for i in range(k)]
    w1 = evalvec(cstar)
    w2b = bytearray(w1)
    for j in range(M):                       # bump one K_M-orbit
        w2b[j * (n // M)] = (w2b[j * (n // M)] + 1) % p
    v1, v2, v3 = evalvec(cstar), evalvec(c2), evalvec(c3)
    w3 = bytes(v1[i] if (i % (n // M)) % 2 == 0 else v2[i]  # 2-way mix
               for i in range(n))
    w4 = bytes((7 * i * i + 3 * i + 5) % p for i in range(n))
    w5 = bytes([v1, v3, v2][(i % (n // M)) % 3][i]          # 3-way mix
               for i in range(n))
    words = [("W1", w1), ("W2", bytes(w2b)), ("W3", w3), ("W4", w4),
             ("W5", w5)]

    full, minA = (1 << n) - 1, min(A_list)

    def rot(mask, s):
        return ((mask << s) | (mask >> (n - s))) & full

    def vr_of(cs, r):
        g = 0
        for i in range(r, k, M):
            g = (g + cs[i] * pow(beta_i, (i - r) // M, p)) % p
        return smul(g, apow[r], p)

    def tv_of(cs, D, r0):
        h = zero
        for i in range(r0, k, D):
            h = vadd(h, smul(cs[i], gampow[D][(i - r0) // D], p), p)
        return mul(apow[r0], h)

    keys = ("cells", "qual", "multi", "v1", "ndcells", "dcells",
            "coll", "strict", "exact_gen")
    cens = dict.fromkeys(keys, 0)
    bad = {f"LLV{i}": [] for i in range(1, 6)}

    for wname, w in words:
        cand = []
        for idx in range(p ** k):
            v = vals[idx]
            cnt = sum(a == b for a, b in zip(v, w))
            if cnt >= minA:
                mask = 0
                for xi in range(n):
                    if v[xi] == w[xi]:
                        mask |= 1 << xi
                cand.append((idx, mask, cnt))
        for A in A_list:
            CM = [idx for idx, m, c in cand
                  if c >= A and rot(m, n // M) == m]
            CD = {D: [idx for idx, m, c in cand
                      if c >= A and rot(m, n // D) == m] for D in divs}
            cens["qual"] += len(CM)
            cens["multi"] += len(CM) >= 2
            # per-codeword aligned data (both routes) + LLV1 pointwise
            VR, TV = {}, {}
            for idx in CM:
                cs = decode(idx)
                VR[idx] = [vr_of(cs, r) for r in range(M)]
                TV[idx] = {}
                for D in divs:
                    for r0 in range(D):
                        tv = tv_of(cs, D, r0)
                        TV[idx][(D, r0)] = tv
                        sig = reduce(lambda a, b: vadd(a, b, p),
                                     (VR[idx][r] for r in range(M)
                                      if r % D == r0), zero)
                        cens["v1"] += 1
                        if sig != tv:
                            bad["LLV1"].append((wname, A, idx, D, r0))
            # genuine scale-D aligned sets over the weaker ensemble C_D
            Agen = {}
            for D in divs:
                if not set(CM) <= set(CD[D]):
                    bad["LLV5"].append((wname, A, D, "nesting"))
                for r0 in range(D):
                    Agen[(D, r0)] = {tv_of(decode(i), D, r0)
                                     for i in CD[D]}
            # cells
            for rmask in range(1, 1 << M):
                R = [r for r in range(M) if rmask >> r & 1]
                D = reduce(math.gcd, (r - R[0] for r in R[1:]), M)
                r0 = R[0] % D
                Rb = [r for r in range(M) if r % D == r0]
                pos = {r: i for i, r in enumerate(Rb)}
                JR = {tuple(VR[i][r] for r in R) for i in CM}
                JRb = {tuple(VR[i][r] for r in Rb) for i in CM}
                T = {TV[i][(D, r0)] for i in CM}
                sig_img = {reduce(lambda a, b: vadd(a, b, p), t, zero)
                           for t in JRb}
                cell = (wname, A, tuple(R), D, len(JRb), len(T))
                cens["cells"] += 1
                if sig_img != T:
                    bad["LLV2"].append(cell)
                proj = {tuple(t[pos[r]] for r in R) for t in JRb}
                if not (JR == proj and len(JR) <= len(JRb)):
                    bad["LLV3"].append(cell)
                if nondeg[D]:
                    cens["ndcells"] += 1
                    if len(T) != len(JRb):
                        bad["LLV4"].append(cell)
                else:
                    cens["dcells"] += 1
                    if len(T) > len(JRb):
                        bad["LLV4"].append(cell)
                    cens["coll"] += len(T) < len(JRb)
                if not T <= Agen[(D, r0)]:
                    bad["LLV5"].append(cell)
                cens["strict"] += len(T) < len(Agen[(D, r0)])
                cens["exact_gen"] += T == Agen[(D, r0)]
    t = tuple(cens[key] for key in keys)
    print(f"  {label} census {keys} = {t}")

    def first(kk):
        return f"; first = {bad[kk][0]}" if bad[kk] else ""
    report(f"{label} LLV1 pointwise class-sum identity", not bad["LLV1"],
           f"{cens['v1']} (codeword, D, r0) checks, "
           f"violations={len(bad['LLV1'])}" + first("LLV1"))
    report(f"{label} LLV2 sigma(J_Rbar) == T", not bad["LLV2"],
           f"{cens['cells']} cells, violations={len(bad['LLV2'])}"
           + first("LLV2"))
    report(f"{label} LLV3 J_R = projection of J_Rbar", not bad["LLV3"],
           f"violations={len(bad['LLV3'])}" + first("LLV3"))
    report(f"{label} LLV4 count transfer", not bad["LLV4"],
           f"nondeg cells={cens['ndcells']} all |T|==|J_Rbar|; "
           f"degenerate cells={cens['dcells']}, collisions={cens['coll']}; "
           f"violations={len(bad['LLV4'])}" + first("LLV4"))
    report(f"{label} LLV5 nesting + T subseteq A_gen", not bad["LLV5"],
           f"strict cells={cens['strict']}, exact cells={cens['exact_gen']}, "
           f"violations={len(bad['LLV5'])}" + first("LLV5"))
    report(f"{label} LLV6 census pin + nonvacuity",
           t == pins and cens["qual"] > 0 and cens["multi"] >= 1,
           f"observed {t}, pinned {pins}, multi-codeword (w,A) pairs = "
           f"{cens['multi']}")


def main():
    print("TR lifting-lemma verifier (stdlib, deterministic)")
    # (label, p, n, omega, e, cc, M, k, A_list, nondeg pin, census pin)
    run_row("F13-M2", 13, 12, 2, 2, 2, 2, 4, [4, 8],
            {1: True, 2: True},
            (30, 31, 4, 93, 30, 0, 0, 4, 26))
    run_row("F13-M4", 13, 12, 2, 2, 2, 4, 4, [4, 8],
            {1: False, 2: False, 4: True},
            (150, 8, 2, 56, 40, 110, 10, 52, 98))
    run_row("F17-M4", 17, 16, 3, 4, 3, 4, 4, [4, 8],
            {1: True, 2: True, 4: True},
            (150, 9, 1, 63, 150, 0, 0, 52, 98))
    n_pass = sum(RESULTS)
    print(f"== {n_pass}/{len(RESULTS)} PASS ==")
    sys.exit(0 if all(RESULTS) else 1)


if __name__ == "__main__":
    main()
