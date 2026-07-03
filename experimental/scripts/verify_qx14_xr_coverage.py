#!/usr/bin/env python3
"""QX.14 verifier: XR wall-pricing coverage table (DAG node xr_radius_arithmetic).

Re-derives every quantitative claim in
experimental/notes/roadmaps/qx14_xr_coverage_table.md:

  [1] Johnson ball profile N_s = C(j,s)*C(n-j,s): exhaustive brute force on
      J(8,4) and J(10,5), plus the Vandermonde total-sum identity on a sweep.
  [2] The pinned pair-correlation ledger packaging identity
      q^{1-t-min(s,t)} + q^{2-2t} <= 2 * q^{1-t} * q^{-min(s,t-1)}  (exact).
  [3] Exact second-moment s-profiles on the integer-exact rows
      (pinned row n=512 k=256 q=17^32; Row C n=1024 k=512 q=2^250 stand-in):
      head geometric decay, bulk-vs-plateau comparison, peak structure,
      excess-over-plateau budget -- all in exact integer arithmetic
      (everything scaled by q^{2t} so no Fractions are needed in the sums).
  [4] A rigorous two-sided Robbins/Stirling log2-binomial bracket engine,
      self-tested against exact binomials.
  [5] Prize-maximal rows n=2^41, k=rho*n, rho in {1/2,1/4,1/8,1/16},
      log2 q = 255.9: corridor t*, table quantities, verdict reaches
      s*_A / s*_B / s*_C, all decisions checked at BOTH bracket ends.
  [6] Cross-check of the FM-crossing deltas at log2 q = 256 against
      s2_paid_ledger.md section 4.

Deterministic; no randomness. Exit code 0 iff every check PASSes.
Run:  python3 experimental/scripts/verify_qx14_xr_coverage.py
"""

import math
import sys
from fractions import Fraction
from itertools import combinations
from math import comb

FAILS = []
NCHECK = 0


def check(name, cond, detail=""):
    global NCHECK
    NCHECK += 1
    tag = "PASS" if cond else "FAIL"
    line = "[%s] %s" % (tag, name)
    if detail:
        line += "   (%s)" % detail
    print(line)
    if not cond:
        FAILS.append(name)


def lg_int(x):
    """log2 of a positive python int, good to ~1e-13 relative."""
    nb = x.bit_length()
    if nb <= 900:
        return math.log2(x)
    sh = nb - 900
    return math.log2(x >> sh) + sh


# ---------------------------------------------------------------------------
# [1] Ball profile: exhaustive brute force + Vandermonde sweep
# ---------------------------------------------------------------------------

def brute_ball(n, j):
    """Check: for EVERY vertex T of J(n,j) and every s, the number of
    vertices U with |T \\ U| = s equals C(j,s)*C(n-j,s)."""
    verts = [frozenset(c) for c in combinations(range(n), j)]
    smax = min(j, n - j)
    expect = [comb(j, s) * comb(n - j, s) for s in range(smax + 1)]
    for T in verts:
        hist = [0] * (smax + 1)
        for U in verts:
            hist[j - len(T & U)] += 1
        if hist != expect:
            return False
        if sum(hist) != comb(n, j):
            return False
    return True


def section1():
    print("\n== [1] Johnson ball profile N_s = C(j,s)C(n-j,s) ==")
    check("J(8,4) exhaustive ball profile (70 vertices, all pairs)",
          brute_ball(8, 4))
    check("J(10,5) exhaustive ball profile (252 vertices, all pairs)",
          brute_ball(10, 5))
    ok = True
    for n in range(1, 41):
        for j in range(0, n + 1):
            smax = min(j, n - j)
            if sum(comb(j, s) * comb(n - j, s) for s in range(smax + 1)) \
                    != comb(n, j):
                ok = False
    check("Vandermonde sum_s C(j,s)C(n-j,s) == C(n,j), all n<=40, all j", ok)


# ---------------------------------------------------------------------------
# [2]+[3] Exact integer rows.  Everything scaled by q^{2t}:
#   EXs      = E[X]-scale * q^{2t}      = C(n,j) q^{t+1}
#   EX2s     = E[X]^2-scale * q^{2t}    = C(n,j)^2 q^2
#   same[s]  = C(n,j) N_s q^{t+1-min(s,t)}   (same-slope pair mass at dist s)
#   dist-sum = sum_s C(n,j) N_s q^2 = EX2s   (far-pair independence plateau)
# ---------------------------------------------------------------------------

def ledger_identity_row(n, k, q, t):
    """Exact: q^{1-t-min(s,t)} + q^{2-2t} <= 2 q^{1-t-min(s,t-1)} for all s.
    Multiply by q^{t-1+min(s,t)}:  1 + q^{min(s,t)+1-t} <= 2 q^{min(s,t)-min(s,t-1)}.
    Checked as exact Fractions."""
    j = n - k - t
    for s in range(j + 1):
        lhs = Fraction(q, q ** (t + min(s, t))) + Fraction(q * q, q ** (2 * t))
        rhs = 2 * Fraction(q, q ** (t + min(s, t - 1)))
        if lhs > rhs:
            return False
    return True


def exact_row(tag, n, k, q, Bstar, t, Lfloat, note=""):
    A = k + t
    j = n - A
    C = comb(n, j)
    Ns = [comb(j, s) * comb(n - j, s) for s in range(j + 1)]
    check("%s t=%d: Vandermonde sum N_s == C(n,j)" % (tag, t), sum(Ns) == C)

    jj = j * (n - j)
    check("%s t=%d: j(n-j) < q (per-step decay premise)" % (tag, t), jj < q,
          "log2 j(n-j)=%.2f, log2 q=%.2f" % (lg_int(jj), Lfloat))

    EXs = C * q ** (t + 1)
    EX2s = C * C * q * q
    same = [C * Ns[s] * q ** (t + 1 - min(s, t)) for s in range(j + 1)]
    check("%s t=%d: same[0] equals the diagonal E[X]-scale" % (tag, t),
          same[0] == EXs)

    in_band = (C * q <= Bstar * q ** t)     # E[X] <= B*, exact
    markov = (C * q <= q ** t)              # E[X] <= 1, exact

    # head decay: same[s+1]/same[s] <= j(n-j)/q for 1 <= s < min(t,j);
    # in particular strictly decreasing, so s=1 dominates the head.
    head_hi = min(t, j)
    hd = all(same[s + 1] * q <= same[s] * jj for s in range(1, head_hi))
    check("%s t=%d: head ratio same[s+1]/same[s] <= j(n-j)/q, s=1..%d"
          % (tag, t, head_hi - 1), hd)
    check("%s t=%d: head strictly decreasing (s=1 dominates head)" % (tag, t),
          all(same[s + 1] < same[s] for s in range(1, head_hi)))

    # head sum <= T_1 / (1 - j(n-j)/q), exact
    head_sum = sum(same[1:head_hi + 1])
    bound = Fraction(same[1]) * Fraction(q, q - jj)
    check("%s t=%d: head sum <= T_1 * (1 - j(n-j)/q)^-1 (exact)" % (tag, t),
          Fraction(head_sum) <= bound)
    # crisp form of "small": head sum <= E[X] * j(n-j)/(q - j(n-j)), exact
    check("%s t=%d: head sum <= E[X] * j(n-j)/(q - j(n-j)) (exact)" % (tag, t),
          head_sum * (q - jj) <= EXs * jj)

    # tail (s>t) rides the plateau at a q^{-1} discount: pointwise
    # same[s] = plateau[s]/q for s > t, and total tail <= EX^2/q.
    tail_sum = sum(same[t + 1:])
    check("%s t=%d: same-slope tail (s>t) <= E[X]^2/q (exact)" % (tag, t),
          tail_sum * q <= EX2s)
    check("%s t=%d: pointwise same[s] == plateau[s]/q for s>t (exact)"
          % (tag, t),
          all(same[s] * q == C * Ns[s] * q * q for s in range(t + 1, j + 1)))

    # bulk peak location: N_s increases while s <= (j(n-j)-1)/(n+2)
    m = (jj - 1) // (n + 2)
    pk_scan = max(range(j + 1), key=lambda s: Ns[s])
    check("%s t=%d: argmax N_s == floor((j(n-j)-1)/(n+2))+1 within 1"
          % (tag, t), abs(pk_scan - (m + 1)) <= 1,
          "scan=%d formula=%d" % (pk_scan, m + 1))

    # who wins pointwise: s=1 head term vs the bulk same-slope peak
    bulk_max = max(same[t + 1:]) if t + 1 <= j else 0
    s1_wins = same[1] >= bulk_max
    # consistency: bulk wins iff N_peak * E[X] > N_1 * C  (exact cross-mult)
    pred_bulk = max(Ns[t + 1:]) * C * q > Ns[1] * C * q ** t \
        if t + 1 <= j else False
    check("%s t=%d: bulk-vs-s=1 outcome matches N_peak*E[X] vs N_1*C(n,j)"
          % (tag, t), s1_wins == (not pred_bulk))

    # excess over the plateau
    excess = EXs + sum(same[1:])
    check("%s t=%d: excess <= n^3*E[X] + E[X]^2 (moment budget, exact)"
          % (tag, t), excess <= n ** 3 * EXs + EX2s)
    budget_n3 = (excess <= n ** 3 * EXs)

    # verdict s*_A: smallest reach s with C(n,j) <= n^3 q^s, capped at t-1
    sA = None
    mech = "(ii) plateau"
    for s in range(1, t):
        if C <= n ** 3 * q ** s:
            sA = s
            mech = "(i) n^3"
            break
    if sA is None:
        sA = max(t - 1, 1)
    # formula cross-check
    s0 = math.ceil((lg_int(C) - 3 * math.log2(n)) / Lfloat)
    sA_formula = min(max(t - 1, 1), max(1, s0))
    check("%s t=%d: s*_A scan == ceil-formula" % (tag, t), sA == sA_formula,
          "scan=%d formula=%d (uncapped ceil=%d)" % (sA, sA_formula, s0))
    # reach t-1 saturated tail == plateau, exactly (the (ii) mechanism):
    # E[X] * q^{-(t-1)} * C(n,j) == E[X]^2, scaled: EXs * C == EX2s * q^{t-1}
    check("%s t=%d: reach-(t-1) saturated tail E[X]*C(n,j)q^{-(t-1)} == "
          "E[X]^2 (exact identity)" % (tag, t),
          EXs * C == EX2s * q ** (t - 1))

    # verdict s*_B: Chebyshev-at-n^3 reading: s >= t-1 - 3log2(n)/L
    x = 3 * math.log2(n) / Lfloat
    check("%s t=%d: 0 < 3log2(n)/log2(q) < 1 (so s*_B = t-1)" % (tag, t),
          0 < x < 1)
    sB = max(t - 1, 1)

    # verdict s*_C: three-regime scenario (plateau free at s >= t-1):
    # smallest reach s* with sum_{s*<s<=t-2} N_s <= n^3 q^{s*}
    sC = None
    for sst in range(1, t):
        Ssum = sum(Ns[sst + 1:t - 1])  # s = sst+1 .. t-2
        if Ssum <= n ** 3 * q ** sst:
            sC = sst
            break
    if sC is None:
        sC = max(t - 1, 1)

    check("%s t=%d: ledger packaging identity c(s,t)=min(s,t-1) (exact)"
          % (tag, t), ledger_identity_row(n, k, q, t))

    lgC = lg_int(C)
    lgEX = lgC + (1 - t) * Lfloat
    lg_head_rel = lg_int(head_sum) - lg_int(EXs)   # log2(head/E[X])
    lg_tail_rel = (lg_int(tail_sum) - lg_int(EX2s)) if tail_sum else None
    print("       info %s t=%d: log2(head/E[X]) = %.2f  "
          "log2(tail/E[X]^2) = %s  log2(excess/E[X]) = %.4f"
          % (tag, t, lg_head_rel,
             "%.2f" % lg_tail_rel if lg_tail_rel is not None else "-inf",
             lg_int(excess) - lg_int(EXs)))
    row = dict(tag=tag, n=n, k=k, t=t, A=A, j=j, lgq=Lfloat,
               lgC=lgC, lgEX=lgEX, lgB=lg_int(Bstar),
               G=Lfloat - lg_int(jj), in_band=in_band, markov=markov,
               s_peak=pk_scan, s1_wins=s1_wins, budget_n3=budget_n3,
               sA=sA, mech=mech, sB=sB, sC=sC,
               lg_excess_over_EX=lg_int(excess) - lg_int(EXs), note=note)
    return row


# ---------------------------------------------------------------------------
# [4] Robbins bracket engine
# ---------------------------------------------------------------------------

LN2 = math.log(2.0)


def lgbinom_bracket(n, j, force_stirling=False):
    """Rigorous two-sided bracket for log2 C(n,j) via Robbins' bounds
    sqrt(2 pi n)(n/e)^n e^{1/(12n+1)} < n! < sqrt(2 pi n)(n/e)^n e^{1/(12n)},
    with a float-slop pad."""
    if j < 0 or j > n:
        raise ValueError
    if j == 0 or j == n:
        return (0.0, 0.0)
    if n <= 5000 and not force_stirling:
        v = lg_int(comb(n, j))
        return (v - 1e-9, v + 1e-9)
    main = j * math.log(n / j) + (n - j) * math.log(n / (n - j))
    half = 0.5 * math.log(n / (2 * math.pi * j * (n - j)))
    lo_r = 1 / (12 * n + 1) - 1 / (12 * j) - 1 / (12 * (n - j))
    hi_r = 1 / (12 * n) - 1 / (12 * j + 1) - 1 / (12 * (n - j) + 1)
    pad = 4e-15 * abs(main) + 1e-9
    return ((main + half + lo_r - pad) / LN2,
            (main + half + hi_r + pad) / LN2)


def section4():
    print("\n== [4] Robbins log2-binomial bracket self-test ==")
    ok = True
    wid = 0.0
    for (n, j) in [(512, 251), (512, 247), (1024, 507), (1024, 505),
                   (4000, 1234), (5000, 2100), (100, 37), (3000, 1500)]:
        lo, hi = lgbinom_bracket(n, j, force_stirling=True)
        ex = lg_int(comb(n, j))
        if not (lo <= ex <= hi):
            ok = False
        wid = max(wid, hi - lo)
    check("Robbins bracket contains exact log2 C(n,j) on 8 test shapes", ok)
    check("Robbins bracket width < 0.02 bits on test shapes", wid < 0.02,
          "max width %.2e bits" % wid)


# ---------------------------------------------------------------------------
# [5] Prize-maximal rows (log2-domain, bracket-stable)
# ---------------------------------------------------------------------------

def find_tstar(n, K, L):
    """Smallest t >= 1 with log2 C(n, n-K-t) <= L*t - 128, decided at both
    Robbins bracket ends; returns (t*, agree, margin_bits_at_tstar)."""
    def in_band(t, end):
        j = n - K - t
        if j <= 0:
            return True
        lo, hi = lgbinom_bracket(n, j)
        val = hi if end == "hi" else lo
        return val <= (L * t - 128)
    tlo, thi = 1, n - K - 1
    # binary search on the 'hi' end (conservative in-band)
    a, b = tlo, thi
    while a < b:
        mid = (a + b) // 2
        if in_band(mid, "hi"):
            b = mid
        else:
            a = mid + 1
    t_hi = a
    a, b = tlo, thi
    while a < b:
        mid = (a + b) // 2
        if in_band(mid, "lo"):
            b = mid
        else:
            a = mid + 1
    t_lo = a
    j = n - K - t_hi
    lo, hi = lgbinom_bracket(n, j)
    margin = (L * t_hi - 128) - hi
    return t_hi, (t_hi == t_lo), margin


def bracket_row(tag, n, K, L, t, rho_name, note=""):
    A = K + t
    j = n - A
    lo, hi = lgbinom_bracket(n, j)
    lgC = 0.5 * (lo + hi)
    jj = j * (n - j)
    lgjj = lg_int(jj)
    check("%s t=%d: j(n-j) << q (log2 gap > 0)" % (tag, t), lgjj < L,
          "gap G = %.1f bits" % (L - lgjj))
    lgEX = lgC + (1 - t) * L
    lgB = L - 128
    in_band = (hi <= L * t - 128)
    in_band_lo = (lo <= L * t - 128)
    check("%s t=%d: in-band decision identical at both bracket ends"
          % (tag, t), in_band == in_band_lo)
    markov = (lgEX < 0)

    # s*_A: ceil((lgC - 3 log2 n)/L), capped to [1, t-1]
    s0_lo = math.ceil((lo - 3 * math.log2(n)) / L)
    s0_hi = math.ceil((hi - 3 * math.log2(n)) / L)
    check("%s t=%d: s*_A ceil identical at both bracket ends" % (tag, t),
          s0_lo == s0_hi, "ceil=%d" % s0_hi)
    mech = "(i) n^3" if s0_hi <= t - 1 else "(ii) plateau"
    sA = min(max(t - 1, 1), max(1, s0_hi))

    x = 3 * math.log2(n) / L
    check("%s t=%d: 0 < 3log2(n)/log2(q) < 1 (so s*_B = t-1)" % (tag, t),
          0 < x < 1)
    sB = max(t - 1, 1)

    # s*_C: three-regime scenario.  Band mass sum_{s*<s<=t-2} N_s is
    # dominated by its top term: growth ratio r(s) = (j-s)(n-j-s)/(s+1)^2
    # >= rmin over the band, so  S <= N_{t-2} * rmin/(rmin-1).
    if t - 2 >= 1:
        m2 = t - 2
        nlo1, nhi1 = lgbinom_bracket(j, m2)
        nlo2, nhi2 = lgbinom_bracket(n - j, m2)
        lgN_lo, lgN_hi = nlo1 + nlo2, nhi1 + nhi2
        rmin = ((j - (t - 3)) * ((n - j) - (t - 3))) / float((t - 2) ** 2)
        check("%s t=%d: band growth ratio rmin > 2" % (tag, t), rmin > 2,
              "rmin = 2^%.1f" % math.log2(rmin))
        slack = math.log2(rmin / (rmin - 1.0))
        sC_lo = math.ceil((lgN_lo + slack - 3 * math.log2(n)) / L)
        sC_hi = math.ceil((lgN_hi + slack - 3 * math.log2(n)) / L)
        check("%s t=%d: s*_C ceil identical at both bracket ends" % (tag, t),
              sC_lo == sC_hi, "ceil=%d" % sC_hi)
        sC = min(max(t - 1, 1), max(1, sC_hi))
    else:
        sC = 1

    # bulk-vs-s=1 pointwise: bulk wins iff lg N_peak + lgEX > lg N_1 + lgC.
    # N_peak evaluated at the formula peak (a certified LOWER bound on max).
    spk = min((jj - 1) // (n + 2) + 1, j)
    plo1, phi1 = lgbinom_bracket(j, spk)
    plo2, phi2 = lgbinom_bracket(n - j, spk)
    bulk_wins_lo = (plo1 + plo2) + lgEX > lgjj + lgC
    bulk_wins_hi = (phi1 + phi2) + lgEX > lgjj + lgC
    check("%s t=%d: bulk-vs-s=1 decision identical at both ends" % (tag, t),
          bulk_wins_lo == bulk_wins_hi)
    row = dict(tag=tag, n=n, k=K, t=t, A=A, j=j, lgq=L, lgC=lgC, lgEX=lgEX,
               lgB=lgB, G=L - lgjj, in_band=in_band, markov=markov,
               s_peak=spk, s1_wins=(not bulk_wins_hi),
               budget_n3=None, sA=sA, mech=mech, sB=sB, sC=sC, note=note)
    return row


# ---------------------------------------------------------------------------
# [6] s2_paid_ledger cross-check at log2 q = 256
# ---------------------------------------------------------------------------

def section6(n):
    print("\n== [6] cross-check vs s2_paid_ledger.md section 4 (L=256) ==")
    s2 = {"1/2": 0.496094, "1/4": 0.746811, "1/8": 0.872853,
          "1/16": 0.936162}
    rhos = {"1/2": Fraction(1, 2), "1/4": Fraction(1, 4),
            "1/8": Fraction(1, 8), "1/16": Fraction(1, 16)}
    for name, rho in rhos.items():
        K = int(n * rho)
        tstar, agree, margin = find_tstar(n, K, 256.0)
        delta = 1.0 - float(rho) - tstar / n
        diff = abs(delta - s2[name])
        check("rate %s: FM-crossing delta at L=256 matches s2 table" % name,
              agree and diff < 1e-6,
              "mine=%.7f s2=%.6f |diff|=%.1e" % (delta, s2[name], diff))


# ---------------------------------------------------------------------------
# table print
# ---------------------------------------------------------------------------

def print_table(rows):
    hdr = ("row        rate   n      log2q   t           A           j"
           "            log2C(n,j)    log2E[X]  log2B*  band  Markov  G(bits)"
           "  peak_s      s=1_wins  s*_A        mech         s*_B        s*_C")
    print("\n" + hdr)
    print("-" * len(hdr))
    for r in rows:
        print("%-10s %-6s %-6s %-7.1f %-11d %-11d %-12d %-13.1f %-9.1f "
              "%-7.1f %-5s %-7s %-8.1f %-11d %-9s %-11s %-12s %-11d %-11d"
              % (r["tag"], r.get("rate", "-"), str(r["n"]), r["lgq"], r["t"],
                 r["A"], r["j"], r["lgC"], r["lgEX"], r["lgB"],
                 "IN" if r["in_band"] else "OUT",
                 "yes" if r["markov"] else "no",
                 r["G"], r["s_peak"],
                 "s=1" if r["s1_wins"] else "bulk",
                 str(r["sA"]) + ("=t-1" if r["sA"] == r["t"] - 1 else ""),
                 r["mech"], r["sB"], r["sC"]))
        if r.get("note"):
            print("           note: %s" % r["note"])


def main():
    section1()

    rows = []

    # -------- row (a): pinned row n=512, k=256, q=17^32 --------------------
    print("\n== [2]+[3] pinned row n=512, k=256, q=17^32 ==")
    n, k = 512, 256
    q = 17 ** 32
    L = lg_int(q)
    check("pinned row: log2 q = 130.7988 (not 131.1; see note)",
          abs(L - 130.79881) < 1e-3, "log2 q = %.5f" % L)
    Bstar = q // 2 ** 128
    check("pinned row: B* = floor(q/2^128) == 6", Bstar == 6)
    check("pinned row: 6*2^128 <= 17^32 < 7*2^128 (exact)",
          6 * 2 ** 128 <= q < 7 * 2 ** 128)
    # corridor t*: smallest t with C(n, n-k-t) q^{1-t} <= B*, exact integers
    tstar = None
    for t in range(1, 40):
        if comb(n, n - k - t) * q <= Bstar * q ** t:
            tstar = t
            break
    check("pinned row: FM crossing t* == 5 (A=261; spine: crossing "
          "between t=4 and t=5)", tstar == 5)
    for t, note in [(4, "t*-1: FM-unsafe side"), (5, "t* corridor edge"),
                    (6, "t*+1"), (9, "A=265 F1 stripped-instance exemplar")]:
        r = exact_row("(a)", n, k, q, Bstar, t, L, note)
        r["rate"] = "1/2"
        rows.append(r)

    # -------- row (b): Row C n=1024, k=512, log2 q = 250 -------------------
    print("\n== [3b] Row C n=1024, k=512, q=2^250 (scale stand-in) ==")
    n, k = 1024, 512
    q = 2 ** 250
    L = 250.0
    Bstar = q // 2 ** 128
    check("Row C: B* = floor(q/2^128) == 2^122", Bstar == 2 ** 122)
    tstar = None
    for t in range(1, 40):
        if comb(n, n - k - t) * q <= Bstar * q ** t:
            tstar = t
            break
    check("Row C: FM crossing t* == 5", tstar == 5, "t*=%s" % tstar)
    for t, note in [(4, "t*-1: FM-unsafe side"), (5, "t* corridor edge"),
                    (6, "t*+1")]:
        r = exact_row("(b)", n, k, q, Bstar, t, L, note)
        r["rate"] = "1/2"
        rows.append(r)

    section4()

    # -------- rows (c): prize-maximal n=2^41, log2 q = 255.9 ---------------
    print("\n== [5] prize-maximal rows n=2^41, log2 q = 255.9 ==")
    n = 2 ** 41
    L = 255.9
    for name, rho in [("1/2", Fraction(1, 2)), ("1/4", Fraction(1, 4)),
                      ("1/8", Fraction(1, 8)), ("1/16", Fraction(1, 16))]:
        K = int(n * rho)
        tstar, agree, margin = find_tstar(n, K, L)
        check("rate %s: corridor t* pinned at both bracket ends" % name,
              agree, "t* = %d, in-band margin %.2f bits" % (tstar, margin))
        for dt, note in [(-1, "t*-1: FM-unsafe side"),
                         (0, "t* corridor edge"), (1, "t*+1")]:
            r = bracket_row("(c)", n, K, L, tstar + dt, name, note)
            r["rate"] = name
            rows.append(r)

    section6(n)

    print_table(rows)

    # headline verdict lines
    print("\n== VERDICT: required ledger reach s* per rate "
          "(corridor edge t = t*) ==")
    for r in rows:
        if r["note"].startswith("t* corridor"):
            print("rate %-5s n=%-14d t*=%-11d s*_A=%-11d (%s; %s)  "
                  "s*_B=%-11d s*_C=%-10d soft(s*=1)? %s"
                  % (r["rate"], r["n"], r["t"], r["sA"],
                     "FULL reach t-1" if r["sA"] == r["t"] - 1 else "partial",
                     r["mech"], r["sB"], r["sC"],
                     "no" if r["sA"] > 1 else "yes"))

    print("\n%d checks, %d failures." % (NCHECK, len(FAILS)))
    if FAILS:
        print("FAILED:")
        for f in FAILS:
            print("  - " + f)
        sys.exit(1)
    print("ALL PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()
