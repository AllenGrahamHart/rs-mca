#!/usr/bin/env python3
"""Verifier for experimental/notes/roadmaps/gap1_terminal_reserve.md.

Checks (deterministic, stdlib only, toy scale):
  T1-T4: stage-1 corridor table -- exact-integer sign checks that the crude
         per-character-product bound (|K|^|R| >= q) overshoots the target
         n^3 * FM(A), plus float shortfalls cross-checked against qa3 ZM
         reference values.
  S1-S2: support-count shortcut is also short (note sect. 3(b)).
  S3   : per-leaf FM bounds over-aggregate by q^(M-t) (note sect. 3(c)).
  F13-*: #212 product-bound shape on the E6 F_13 toy -- line confinement,
         per-character rank <= 1, combined rank <= sum of per-character
         ranks, over all K_M-stable supports and active sets, M in {2,4}.

Exit 0 iff every row PASSes.
"""
import math
import sys

RESULTS = []


def report(name, ok, detail):
    RESULTS.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")


def plog2(x):
    """log2 of a positive int, safe beyond float range."""
    b = x.bit_length()
    if b <= 900:
        return math.log2(x)
    s = b - 900
    return math.log2(x >> s) + s


# ---------------------------------------------------------------- stage 1
LOG2_17 = math.log2(17)

# (name, n, k, A, log2 q (float), q exact, qa3 ZM reference)
STAGE1_ROWS = [
    ("T1 pinned t=5", 512, 256, 261, 32 * LOG2_17, 17**32, 10.84),
    ("T2 pinned t=6", 512, 256, 262, 32 * LOG2_17, 17**32, -120.02),
    ("T3 RowC   t=5", 1024, 512, 517, 250.0, 2**250, 48.60),
    ("T4 RowC   t=8", 1024, 512, 520, 250.0, 2**250, -701.51),
]


def stage1():
    for name, n, k, A, l2q, q, zm_ref in STAGE1_ROWS:
        j, t = n - A, A - k
        c = math.comb(n, j)
        zm = 3 * math.log2(n) + plog2(c) + (1 - t) * l2q
        short_min = l2q - zm            # |R|=1, e=1
        short_max = n * l2q - zm        # |R|=M=n, e=1
        # exact integer form of "crude (q^1) > n^3 * FM(A)":
        #   q * q^(t-1) > n^3 * C(n,j)  <=>  q^t > n^3 * C(n,j)
        exact_short = q**t > n**3 * c
        ok = (exact_short and short_min > 0 and short_max > short_min
              and abs(zm - zm_ref) < 0.02)
        report(name, ok,
               f"ZM={zm:+.2f} (qa3 ref {zm_ref:+.2f}), crude shortfall "
               f"|R|=1,e=1: {short_min:+.2f} bits, |R|=n: "
               f"{short_max:+.1f} bits, exact q^t > n^3*C(n,j): "
               f"{exact_short}")


def stage1_shortcuts():
    # S1-S2: support-count refinement C(n/2, ceil(j/2)) still short of ZM.
    for name, n, k, A, l2q, q, _ in (STAGE1_ROWS[0], STAGE1_ROWS[2]):
        j, t = n - A, A - k
        zm = 3 * math.log2(n) + plog2(math.comb(n, j)) + (1 - t) * l2q
        sc = plog2(math.comb(n // 2, (j + 1) // 2))
        gap = sc - zm
        # note sect. 3(b): 240.79 (pinned) / 458.55 (Row C)
        ref = 240.79 if n == 512 else 458.55
        ok = gap > 0 and abs(gap - ref) < 0.02
        report(f"S{1 if n == 512 else 2} support-count {name[3:]}", ok,
               f"log2 C(n/2,~j/2)={sc:.2f}, still short of ZM by "
               f"{gap:+.2f} bits (note ref {ref})")

    # S3: aggregation failure. Pinned row, t=5, M=8 > t: the product of
    # per-leaf mean factors q^(1-t/M) over |R|=M leaves carries q^(M-t),
    # exceeding the parent q^(1-t) by q^(M-1). Exact integers.
    n, k, A, q, M = 512, 256, 261, 17**32, 8
    t = A - k
    lhs = q**(M - t)             # aggregated leaf q-factor
    parent = q**(1 - t + M - 1)  # q^(M-t) == parent q^(1-t) * q^(M-1)
    overshoot_bits = (M - 1) * 32 * LOG2_17
    ok = lhs == parent and overshoot_bits > 900
    report("S3 per-leaf FM aggregation", ok,
           f"M={M}>t={t}: leaf-product q-factor exceeds parent q^(1-t) by "
           f"q^(M-1) = 2^{overshoot_bits:.1f} exactly")

# ------------------------------------------------- F_13 toy (#212 shape)
P = 13
NR = 2  # quadratic nonresidue mod 13; F_169 = F_13[s]/(s^2 - 2)


def fmul(u, v):
    a, b = u
    c, d = v
    return ((a * c + NR * b * d) % P, (a * d + b * c) % P)


def finv(u):
    a, b = u
    nrm = (a * a - NR * b * b) % P  # nonzero for u != 0 (2 is a nonresidue)
    ni = pow(nrm, P - 2, P)
    return ((a * ni) % P, (-b * ni) % P)


def fpow(u, e):
    r = (1, 0)
    for _ in range(e):
        r = fmul(r, u)
    return r


def lagrange_at_alpha(S, alpha):
    """L_x(alpha) in F_169 for each x in S (S subset of F_13, embedded)."""
    out = {}
    for x in S:
        num = (1, 0)
        den = 1
        for y in S:
            if y == x:
                continue
            num = fmul(num, ((alpha[0] - y) % P, alpha[1]))
            den = (den * (x - y)) % P
        out[x] = fmul(num, (pow(den, P - 2, P), 0))
    return out


def rank_f13(vectors):
    """Rank over F_13 of a list of 2-vectors (F_169 as F_13^2)."""
    rows = [list(v) for v in vectors if v != (0, 0)]
    rank, col = 0, 0
    while col < 2 and rows:
        piv = next((i for i, r in enumerate(rows) if r[col] % P), None)
        if piv is None:
            col += 1
            continue
        rows[0], rows[piv] = rows[piv], rows[0]
        inv = pow(rows[0][col], P - 2, P)
        rows[0] = [(inv * z) % P for z in rows[0]]
        for r in rows[1:]:
            f = r[col]
            for c in range(2):
                r[c] = (r[c] - f * rows[0][c]) % P
        rank += 1
        rows = rows[1:]
        col += 1
    return rank


def f13_toy(M):
    """All K_M-stable supports of H_12 = <2> in F_13^*, alpha = sqrt(2)."""
    omega, n = 2, 12
    assert all(pow(omega, i, P) != 1 for i in range(1, n)), "ord(2)=12"
    zeta = pow(omega, n // M, P)
    alpha = (0, 1)                      # alpha^2 = 2 in F_13
    assert fpow(alpha, M)[1] == 0, "alpha^M must lie in F_13"
    H = [pow(omega, i, P) for i in range(n)]
    cosets, seen = [], set()
    for x in sorted(H):
        if x in seen:
            continue
        c = [(x * pow(zeta, i, P)) % P for i in range(M)]
        seen.update(c)
        cosets.append(c)                # c[i] = rep * zeta^i
    ainv = finv(alpha)
    n_sup = n_case = 0
    viol_line = viol_rank1 = viol_comb = 0
    for mask in range(1, 1 << len(cosets)):
        sel = [c for i, c in enumerate(cosets) if mask >> i & 1]
        S = [x for c in sel for x in c]
        L = lagrange_at_alpha(S, alpha)
        vecs = {}                       # r -> list of per-coset vectors
        for r in range(M):
            vr = []
            for c in sel:
                v = (0, 0)
                for i, x in enumerate(c):
                    zi = pow(zeta, r * i, P)
                    v = ((v[0] + zi * L[x][0]) % P,
                         (v[1] + zi * L[x][1]) % P)
                vr.append(v)
                # line confinement: v * alpha^(-r) must lie in F_13
                w = fmul(v, fpow(ainv, r))
                if w[1] != 0:
                    viol_line += 1
            vecs[r] = vr
            if rank_f13(vr) > 1:
                viol_rank1 += 1
        n_sup += 1
        for rmask in range(1, 1 << M):
            R = [r for r in range(M) if rmask >> r & 1]
            comb = rank_f13([v for r in R for v in vecs[r]])
            if comb > sum(rank_f13(vecs[r]) for r in R):
                viol_comb += 1
            n_case += 1
    ok = viol_line == viol_rank1 == viol_comb == 0
    report(f"F13-M{M} #212 shape", ok,
           f"{n_sup} stable supports, {n_case} (support, active-set) cases: "
           f"line violations={viol_line}, per-char rank>1: {viol_rank1}, "
           f"combined>sum: {viol_comb}")


def main():
    print("gap1_terminal_reserve verifier (stdlib, deterministic)")
    print("-- stage 1: corridor table --")
    stage1()
    print("-- stage 1: failed shortcuts --")
    stage1_shortcuts()
    print("-- #212 product-bound shape on the E6 F_13 toy --")
    for M in (2, 4):
        f13_toy(M)
    n_pass = sum(RESULTS)
    print(f"== {n_pass}/{len(RESULTS)} PASS ==")
    sys.exit(0 if all(RESULTS) else 1)


if __name__ == "__main__":
    main()
