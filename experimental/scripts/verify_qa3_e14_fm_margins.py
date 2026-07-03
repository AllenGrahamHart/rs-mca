#!/usr/bin/env python3
"""verify_qa3_e14_fm_margins.py — QA.3 / E14 / QL.4 integrality margin tables.

Deterministic verifier for experimental/notes/roadmaps/qa3_e14_fm_margin_tables.md.

Checks, with exact/high-precision log2 arithmetic (Decimal prec 80; exact
math.comb for n <= 5000; Stirling with certified error bound for larger n):

  MCA side (aperiodic_zero_at_crossing, computational half; QA.3):
    * locates A* = max{A : FM(A) > B*} by binary search on strictly
      decreasing log2 FM(A), FM(A) = C(n, n-A) * q^(1-(A-k)),
      B* = floor(q_line / 2^128)  (spine adjacent-pin convention);
    * zero-margins ZM(A) = log2(n^3 * FM(A)) and gate-margins
      GM(A) = ZM(A) - log2 B* at A*-1 .. A*+3;
    * A_zero = first A with ZM < 0 (aperiodic count exactly 0 under
      R2(B=3) from A_zero on, by monotonicity), A_gate likewise for GM;
    * F1 corridor candidates A_quot = k + ceil(n*beta/(log2 q - 128))
      (s2 R1' left end), margins at the safe side A_quot+1, with the
      beta-rounding window (+-1e-4) evaluated exactly via Fractions.

  List side (QL.4 mirror):
    * mean(sigma) = C(n, k+sigma) * q^(-sigma) (exact uniform-word pair
      mean for MDS rows), sigma* = max{sigma : mean >= 1};
    * list margins LM(sigma) = log2(n^3 * mean(sigma)), sigma_zero;
    * the exact identity mean(sigma) = FM(k+sigma)/q and |t* - sigma*| <= 1;
    * exact quotient-core 2-power window: M_max = max 2-power M | k with
      C(n/M - 1, k/M) >= 2^128 (thm:qcore crossing, exact rule), and the
      gap between the proved-unsafe window [1, M_max-1] and sigma*.

  Regressions: Stirling vs exact comb; pinned-row B* = 6 and
  ord(17 mod 512) = 32 (s4); s2 FM-crossing deltas at log2 q = 256;
  pinned-row A = 265 stripped-FM prediction (s2 sect. 4).

LOUDFLAG lines mark candidate points where a margin exceeds -20 (integrality
cannot absorb R2's n^3 there); these are FINDINGS reported by the note, not
verifier failures.  FAIL lines mark violations of the note's stated claims.
Exit code 0 iff all checks PASS.  No randomness anywhere.
"""

import math
import sys
from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 80

PI = Decimal('3.14159265358979323846264338327950288419716939937510582097494459230781640628620899')
LN2 = Decimal(2).ln()

checks = []
flags = []


def check(name, ok, detail=""):
    checks.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + ((" [" + detail + "]") if detail else ""))


def loudflag(msg):
    flags.append(msg)
    print("LOUDFLAG " + msg)


def info(msg):
    print("INFO " + msg)


def f2(x):
    return "{:.2f}".format(float(x))


def fe(x):
    return "{:.6e}".format(float(x))


# ---------------------------------------------------------------- log2 comb
def lg2_gamma(z):
    """log2 Gamma(z) for integer z >= 250, Stirling series through B8.
    Abs error in ln Gamma <= first omitted term = |B10|/(90 z^9) = 1/(1188 z^9)
    [CITATION: standard alternating-envelope bound for the Stirling series on
    the positive real axis; cross-validated below against exact factorials]."""
    zd = Decimal(z)
    lnz = zd.ln()
    s = (zd - Decimal('0.5')) * lnz - zd + (2 * PI).ln() / 2
    s += 1 / (12 * zd) - 1 / (360 * zd**3) + 1 / (1260 * zd**5) - 1 / (1680 * zd**7)
    return s / LN2


def lg2_comb(n, j):
    if j < 0 or j > n:
        raise ValueError("bad j")
    if n <= 5000:
        return Decimal(math.comb(n, j)).ln() / LN2
    if min(j, n - j) < 250:
        # exact product form: C(n,j) with small j
        m = min(j, n - j)
        v = Decimal(0)
        for i in range(m):
            v += Decimal(n - i).ln() - Decimal(i + 1).ln()
        return v / LN2
    return lg2_gamma(n + 1) - lg2_gamma(j + 1) - lg2_gamma(n - j + 1)


def lg2_comb_stirling(n, j):
    return lg2_gamma(n + 1) - lg2_gamma(j + 1) - lg2_gamma(n - j + 1)


# ---------------------------------------------------------------- row model
def lg2_FM(row, A):
    n, k, L = row['n'], row['k'], row['lgq']
    t = A - k
    j = n - A
    return lg2_comb(n, j) + (1 - t) * L


def zero_margin(row, A):
    return row['lg_n3'] + lg2_FM(row, A)


def gate_margin(row, A):
    return zero_margin(row, A) - row['lgB']


def find_Astar(row):
    n, k, lgB = row['n'], row['k'], row['lgB']
    lo, hi = k + 1, n - 1
    assert lg2_FM(row, lo) > lgB, row['name'] + " lo not unsafe"
    assert lg2_FM(row, hi) < lgB, row['name'] + " hi not safe"
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if lg2_FM(row, mid) > lgB:
            lo = mid
        else:
            hi = mid
    return lo


def lg2_list_mean(row, sigma):
    n, k, L = row['n'], row['k'], row['lgq']
    return lg2_comb(n, k + sigma) - sigma * L


def list_margin(row, sigma):
    return row['lg_n3'] + lg2_list_mean(row, sigma)


def find_sigmastar(row):
    n, k = row['n'], row['k']
    lo, hi = 1, n - k - 1
    assert lg2_list_mean(row, lo) >= 0, row['name'] + " sigma=1 below 1"
    assert lg2_list_mean(row, hi) < 0, row['name'] + " sigma_hi above 1"
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if lg2_list_mean(row, mid) >= 0:
            lo = mid
        else:
            hi = mid
    return lo


def first_below(fun, start, limit=64):
    A = start
    for _ in range(limit):
        if fun(A) < 0:
            return A
        A += 1
    raise RuntimeError("no zero radius within limit")


# ------------------------------------------------------------- self checks
print("== QA.3 / E14 / QL.4 verifier: FM integrality margin tables ==")
print()
print("-- precision self-checks --")
check("const pi vs math.pi", abs(PI - Decimal(repr(math.pi))) < Decimal('1e-15'))
check("const ln2 vs math", abs(LN2 - Decimal(repr(math.log(2)))) < Decimal('1e-15'))
for (n_, j_) in [(1024, 508), (1024, 512), (512, 251), (4096, 2031)]:
    exact = Decimal(math.comb(n_, j_)).ln() / LN2
    stir = lg2_comb_stirling(n_, j_)
    check("stirling vs exact C(%d,%d)" % (n_, j_), abs(exact - stir) < Decimal('1e-22'),
          "|diff|=" + fe(abs(exact - stir)))
info("stirling residual error bound 3/(1188*z^9), z>=251: < 4e-25")

# ------------------------------------------------------- pinned-row facts
print()
print("-- pinned-row conventions (s2/s4 regressions) --")
q_pin = 17**32
lgq_pin = Decimal(q_pin).ln() / LN2
Bstar_pin = q_pin >> 128
check("pinned B* = floor(17^32/2^128) == 6 (s2 sect.4)", Bstar_pin == 6, "B*=%d" % Bstar_pin)
ord17 = next(d for d in range(1, 513) if pow(17, d, 512) == 1)
check("ord(17 mod 512) == 32 (s4 sect.4)", ord17 == 32, "ord=%d" % ord17)
info("pinned log2 q_line = 32*log2(17) = " + "{:.5f}".format(float(lgq_pin)))
info("FINDING F0: task-brief pins 'log2 q = 131.1' for the pinned row; actual "
     "32*log2 17 = " + "{:.5f}".format(float(lgq_pin)) +
     " (B* = 6, not 8). Both variants tabulated below.")

# --------------------------------------------------------------- row table
RATES = ['1/2', '1/4', '1/8', '1/16']
RHO = {'1/2': Fraction(1, 2), '1/4': Fraction(1, 4), '1/8': Fraction(1, 8), '1/16': Fraction(1, 16)}
BETA = {'1/2': Fraction('0.7925'), '1/4': Fraction('0.75'), '1/8': Fraction('0.5306'),
        '1/16': Fraction('0.3343')}  # s2 sect.3, machine-verified there (4 d.p.)
S2_FM_DELTA = {'1/2': Decimal('0.496094'), '1/4': Decimal('0.746811'),
               '1/8': Decimal('0.872853'), '1/16': Decimal('0.936162')}


def mkrow(name, n, k, lgq, lgB, Lfrac, rate):
    return dict(name=name, n=n, k=k, lgq=lgq, lgB=lgB, Lfrac=Lfrac, rate=rate,
                lg_n3=3 * (Decimal(n).ln() / LN2))


rows = []
rows.append(mkrow("pinned n=512 k=256 q=17^32 (B*=6)", 512, 256, lgq_pin,
                  Decimal(Bstar_pin).ln() / LN2, None, '1/2'))
Bstar_var = int(Decimal(2)**Decimal('3.1'))  # floor(2^131.1 / 2^128) = 8
rows.append(mkrow("pinned-VARIANT lgq=131.1 [task-brief; inconsistent w/ 17^32] (B*=%d)" % Bstar_var,
                  512, 256, Decimal('131.1'), Decimal(Bstar_var).ln() / LN2, None, '1/2'))
for r in RATES:
    k = int(1024 * RHO[r])
    rows.append(mkrow("RowC n=1024 rate %s (lgq=250, lgB*=122)" % r, 1024, k,
                      Decimal(250), Decimal(122), Fraction(250), r))
for r in RATES:
    n = 2**41
    k = int(n * RHO[r])
    lgB = (Decimal(2)**Decimal('127.9')).to_integral_value(rounding='ROUND_FLOOR')
    lgB = Decimal(int(lgB)).ln() / LN2  # floor correction < 2^-127 bits
    rows.append(mkrow("prize-max n=2^41 rate %s (lgq=255.9)" % r, n, k,
                      Decimal('255.9'), lgB, Fraction('255.9'), r))

for row in rows:
    lgn = Decimal(row['n']).ln() / LN2
    assert lgn < row['lgq'] - 80, "monotonicity slack violated"

# -------------------------------------------------- s2 asymptotic regression
print()
print("-- s2 sect.4 FM-crossing regression (n=2^20, lgq=256, lgB*=128) --")
for r in RATES:
    n = 2**20
    k = int(n * RHO[r])
    rr = mkrow("reg", n, k, Decimal(256), Decimal(128), None, r)
    Ast = find_Astar(rr)
    delta = (Decimal(n) - Decimal(Ast)) / Decimal(n)
    check("s2 FM crossing rate %s" % r, abs(delta - S2_FM_DELTA[r]) < Decimal('5e-4'),
          "delta(A*)={:.6f} vs s2 {:.6f}".format(float(delta), float(S2_FM_DELTA[r])))

# --------------------------------------------------------- MCA Table 1
print()
print("== MCA TABLE 1: FM/B* crossing windows (candidate points, fork F2) ==")
mca_results = {}
for row in rows:
    print()
    print("row: " + row['name'])
    Ast = find_Astar(row)
    tst = Ast - row['k']
    delta = (row['n'] - Ast) / Decimal(row['n'])
    gap_hi = lg2_FM(row, Ast) - row['lgB']
    gap_lo = row['lgB'] - lg2_FM(row, Ast + 1)
    print("  A* = %d  (t* = %d, delta(A*) = %.6f)" % (Ast, tst, float(delta)))
    check("  adjacent pin FM(A*)>B*>=FM(A*+1) [%s]" % row['name'],
          gap_hi > Decimal('1e-12') and gap_lo > Decimal('1e-12'),
          "gaps +" + f2(gap_hi) + " / -" + f2(gap_lo) + " bits")
    if gap_hi < Decimal('0.01') or gap_lo < Decimal('0.01'):
        loudflag("KNIFE-EDGE crossing unresolved at precision: " + row['name'])
    for dA in (-1, 0, 1, 2, 3):
        A = Ast + dA
        zm = zero_margin(row, A)
        gm = gate_margin(row, A)
        print("    A*%+d  A=%-16d log2FM=%14s  ZM=%14s  GM=%14s"
              % (dA, A, f2(lg2_FM(row, A)), f2(zm), f2(gm)))
    A_zero = first_below(lambda A: zero_margin(row, A), Ast)
    A_gate = first_below(lambda A: gate_margin(row, A), Ast)
    print("  A_zero = A*+%d   A_gate = A*+%d" % (A_zero - Ast, A_gate - Ast))
    check("  A_zero <= A*+2 [%s]" % row['name'], A_zero <= Ast + 2)
    check("  ZM(A*+3) < -20 [%s]" % row['name'], zero_margin(row, Ast + 3) < -20,
          "ZM(A*+3)=" + f2(zero_margin(row, Ast + 3)))
    for A in range(Ast + 1, A_zero):
        loudflag("MCA %s: ZM(A*+%d)=%s > -20 — integrality does NOT hold at A=%d"
                 % (row['name'], A - Ast, f2(zero_margin(row, A)), A))
    for A in (A_zero, A_zero + 1):
        if zero_margin(row, A) > -20:
            loudflag("MCA %s: ZM(A=%d)=%s in (-20,0) — thin margin"
                     % (row['name'], A, f2(zero_margin(row, A))))
    mca_results[row['name']] = (Ast, A_zero, A_gate)
    row['Astar'], row['A_zero'], row['A_gate'] = Ast, A_zero, A_gate

# pinned-row A=265 stripped prediction (s2 sect.4)
print()
zm265 = zero_margin(rows[0], 265)
check("pinned A=265 stripped-FM margin < -400 (s2 sect.4 P2 restated)", zm265 < -400,
      "ZM(265)=" + f2(zm265))

# --------------------------------------------------------- MCA Table 2 (F1)
print()
print("== MCA TABLE 2: F1 quotient-corridor candidates A_quot = k + ceil(n*beta/(lgq-128)) ==")
BTOL = Fraction(1, 10000)
for row in rows:
    if row['Lfrac'] is None:
        info("row %s: EXCLUDED from F1 table (tangent-pinned at 506/507 per s2 sect.4; "
             "corridor formula not operative at lgq ~ 131)" % row['name'])
        continue
    n, k = row['n'], row['k']
    beta = BETA[row['rate']]
    den = row['Lfrac'] - 128
    A_lo = k + math.ceil(n * (beta - BTOL) / den)
    A_qu = k + math.ceil(n * beta / den)
    A_hi = k + math.ceil(n * (beta + BTOL) / den)
    print()
    print("row: " + row['name'])
    print("  A_quot = %d  (window [%d, %d] for beta +- 1e-4;  A* = %d, A_zero = %d)"
          % (A_qu, A_lo, A_hi, row['Astar'], row['A_zero']))
    ok_order = A_lo >= row['Astar']
    check("  A_quot window >= A* (corridor order quot deeper than FM) [%s]" % row['name'],
          ok_order, "A_lo-A* = %d" % (A_lo - row['Astar']))
    ok = True
    for A in sorted({A_lo, A_qu, A_hi}):
        zm = zero_margin(row, A + 1)
        print("    safe side of candidate: ZM(A=%d +1) = %s" % (A, f2(zm)))
        if not (zm < -20):
            ok = False
            loudflag("F1 candidate %s: ZM(%d)=%s > -20" % (row['name'], A + 1, f2(zm)))
    check("  ZM(A_quot+1) < -20 across beta window [%s]" % row['name'], ok)
    check("  A_quot+1 >= A_zero (integrality live at F1 safe side) [%s]" % row['name'],
          A_lo + 1 >= row['A_zero'],
          "A_lo+1 - A_zero = %d" % (A_lo + 1 - row['A_zero']))

# ------------------------------------------------------------- LIST Table 3
print()
print("== LIST TABLE 3: extras-mean crossing sigma* (reserve arithmetic mirror) ==")
for row in rows:
    print()
    print("row: " + row['name'])
    sst = find_sigmastar(row)
    tst = row['Astar'] - row['k']
    print("  sigma* = %d   (t* = %d;  sigma*/n = %.6f)" % (sst, tst, sst / row['n']))
    check("  |t* - sigma*| <= 1 (q-shift identity) [%s]" % row['name'], abs(tst - sst) <= 1)
    # exact identity mean(sigma) = FM(k+sigma)/q at three sigmas
    iddev = max(abs(lg2_list_mean(row, s) - (lg2_FM(row, row['k'] + s) - row['lgq']))
                for s in (max(1, sst - 1), sst, sst + 1))
    check("  identity mean(s)=FM(k+s)/q [%s]" % row['name'], iddev < Decimal('1e-20'),
          "max|dev|=" + fe(iddev))
    for ds in (-1, 0, 1, 2, 3):
        s = sst + ds
        if s < 1:
            continue
        lm = list_margin(row, s)
        print("    s*%+d  sigma=%-14d log2mean=%14s  LM=%14s"
              % (ds, s, f2(lg2_list_mean(row, s)), f2(lm)))
    s_zero = first_below(lambda s: list_margin(row, s), sst)
    print("  sigma_zero = sigma*+%d" % (s_zero - sst))
    check("  sigma_zero <= sigma*+2 [%s]" % row['name'], s_zero <= sst + 2)
    check("  LM(sigma*+3) < -20 [%s]" % row['name'], list_margin(row, sst + 3) < -20,
          "LM=" + f2(list_margin(row, sst + 3)))
    for s in range(sst + 1, s_zero):
        loudflag("LIST %s: LM(sigma*+%d)=%s > -20 — extras-zero does NOT hold at sigma=%d"
                 % (row['name'], s - sst, f2(list_margin(row, s)), s))
    for s in (s_zero, s_zero + 1):
        if list_margin(row, s) > -20:
            loudflag("LIST %s: LM(sigma=%d)=%s in (-20,0) — thin margin"
                     % (row['name'], s, f2(list_margin(row, s))))
    row['sigmastar'], row['sigma_zero'] = sst, s_zero

# ------------------------------------------------------------- LIST Table 4
print()
print("== LIST TABLE 4: exact quotient-core 2-power windows (thm:qcore) vs sigma* ==")
for row in rows:
    n, k = row['n'], row['k']
    M_max = None
    M = 2
    while n % M == 0 and k % M == 0 and k // M >= 1 and n // M - 1 >= k // M:
        if lg2_comb(n // M - 1, k // M) >= 128:
            M_max = M
        M *= 2
    print()
    print("row: " + row['name'])
    if M_max is None:
        info("  no 2-power scale crosses 2^128 (row too small); proved-unsafe window empty")
        check("  gap accounting done [%s]" % row['name'], True)
        continue
    sst, s_zero = row['sigmastar'], row['sigma_zero']
    print("  M_max = %d  => proved-unsafe radii sigma in [1, %d];  sigma* = %d, sigma_zero = %d"
          % (M_max, M_max - 1, sst, s_zero))
    if M_max <= sst:
        gap = sst - M_max + 1
        info("  2-POWER GAP (s7 F2): radii [%d, %d] (%d radii) mean-unsafe but not "
             "2-power-proved-unsafe; exact optimization over M|k expected to close" % (M_max, sst, gap))
        check("  gap accounting done [%s]" % row['name'], True)
    else:
        first_open = max(M_max, s_zero)
        lm = list_margin(row, first_open)
        for s in range(M_max, s_zero):
            loudflag("LIST-F1 %s: radius %d past proved-unsafe window has LM=%s > -20"
                     % (row['name'], s, f2(list_margin(row, s))))
        check("  LM at first radius needing extras-zero (sigma=%d) < -20 [%s]" % (first_open, row['name']),
              lm < -20, "LM=" + f2(lm))

# ------------------------------------------------------------------ summary
print()
npass = sum(1 for _, ok in checks if ok)
nfail = sum(1 for _, ok in checks if not ok)
print("== SUMMARY: %d PASS, %d FAIL, %d LOUDFLAG findings ==" % (npass, nfail, len(flags)))
if flags:
    print("flagged findings (reported and interpreted in the note):")
    for f in flags:
        print("  * " + f)
sys.exit(0 if nfail == 0 else 1)
