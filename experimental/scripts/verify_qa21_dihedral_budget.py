#!/usr/bin/env python3
"""QA.21 — dihedral budget column verifier.

Recomputes every row of experimental/notes/roadmaps/
qa21_dihedral_budget_column.md deterministically: exact big integers for the
Row C candidates, rigorous integer inequalities plus Robbins log2 brackets
for the prize candidates. Stdlib only, no randomness, no I/O beyond stdout.

Counting model (see the note, sect. 2): at each clean-rate candidate A of
xr_budget_audit.md (all have j = n - A ODD), the crude dihedral column is

    N_dih = 2 * C((n-2)/2, (j-1)/2)

(odd-size inversion-closed supports on mu_n, n even: exactly one fixed point
of {+1,-1} plus (j-1)/2 moving inverse pairs — E30 finding 1), capped at one
slope per aligned locator per pair (v8 ledger). The E26 strict window column
(d = m*ell, twin-fiber size m in {2,4,8,...}) is 0 at odd j, but is UNSAFE
as a bound (E30 exhibits odd-j dihedral words on the fixed-point branch the
m*ell fiber count omits). s' = B* - B_quot_ub - B_tan_max - B_dih.

Exit 0 iff every check passes.
"""

import math
import sys

PASS = 0
FAIL = 0


def check(label, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS  {label}" + (f"  [{detail}]" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL  {label}" + (f"  [{detail}]" if detail else ""))


def iroot(x: int, r: int) -> int:
    """floor(x^(1/r)) by exact integer bisection."""
    lo, hi = 0, 1
    while hi ** r <= x:
        hi *= 2
    while lo < hi - 1:
        mid = (lo + hi) // 2
        if mid ** r <= x:
            lo = mid
        else:
            hi = mid
    return lo


def log2big(x: int) -> float:
    """log2 of a positive big int via its top 53 bits (exact-direction float,
    relative error ~1e-15; used for DISPLAY, never for PASS inequalities on
    close calls — every PASS inequality below has >30-bit margins or is pure
    integer arithmetic)."""
    b = x.bit_length()
    if b <= 53:
        return math.log2(x)
    return (b - 53) + math.log2(x >> (b - 53))


def lnfact(n: int, lower: bool) -> float:
    """Robbins bracket on ln n!:  base + 1/(12n+1) < ln n! < base + 1/(12n)."""
    base = 0.5 * math.log(2 * math.pi * n) + n * math.log(n) - n
    return base + (1 / (12 * n + 1) if lower else 1 / (12 * n))


def log2C_bracket(N: int, K: int):
    """[lo, hi] bracket on log2 C(N, K) from Robbins (rigorous up to float
    rounding; the note only uses it where margins are >= 10^11 bits)."""
    lo = (lnfact(N, True) - lnfact(K, False) - lnfact(N - K, False)) / math.log(2)
    hi = (lnfact(N, False) - lnfact(K, True) - lnfact(N - K, True)) / math.log(2)
    return lo, hi


# ---------------------------------------------------------------- B_quot (audit machinery, floor-rounded ub)

def bquot_ub(n: int, k: int, A: int) -> int:
    """Floor-rounded all-active-scale sum, exactly as verify_xr_budget_audit.py
    (dyadic N' | n with N' * (A - k) <= n; l' = floor(j N'/n), trivial l'
    excluded)."""
    t = A - k
    total = 0
    Np = 2
    while Np <= n and Np * t <= n:
        lp = (n - A) * Np // n
        if 1 <= lp <= Np - 1:
            total += math.comb(Np, lp)
        Np *= 2
    return total


def bquot_strict(n: int, k: int, A: int) -> int:
    """Strict (integral-l') census max over active scales, as the audit."""
    t = A - k
    best = 0
    Np = 2
    while Np <= n and Np * t <= n:
        j = n - A
        M = n // Np
        if j % M == 0 and 1 <= j // M <= Np - 1:
            best = max(best, math.comb(Np, j // M))
        Np *= 2
    return best


# ---------------------------------------------------------------- constants

B_STAR_ROWC = 1 << 122
B_STAR_PRIZE = iroot(1 << 1279, 10)
TWO100 = 1 << 100

check("prize B* = floor(2^127.9) exact 10th root (audit pin)",
      B_STAR_PRIZE ** 10 <= (1 << 1279) < (B_STAR_PRIZE + 1) ** 10
      and B_STAR_PRIZE == 317494674775468773183020924238786383963)

# audit table pins: candidate A and the s bottom end (= B* - B_quot_ub - B_tan_max)
AUDIT_PINS = {
    ("RowC", 4): (261, 5316907684064982757706454885536879188),
    ("RowC", 8): (133, 5316911983139662876649441475853304530),
    ("RowC", 16): (67, 5316911982997375233704305923711011740),
    ("prize", 4): (558345748481, 317494670476394092449112149242524378539),
    ("prize", 8): (283467841537, 317494674775468772568055135557962897065),
    ("prize", 16): (141733920769, 317494674775326484925109999864086683573),
}

# note table pins (this packet's computed column, re-derived below)
NOTE_LOG2_NDIH = {  # display values claimed in the note (tolerance 1e-4 / 0.5)
    ("RowC", 4): 414.4651, ("RowC", 8): 280.4193, ("RowC", 16): 173.6759,
    ("prize", 4): 898752770296.23, ("prize", 8): 609603247008.73,
    ("prize", 16): 379193192042.78,
}
NOTE_SUPPRESSION = {  # required per-pair suppression exponent (display)
    ("RowC", 4): 292.4652, ("RowC", 8): 158.4193, ("RowC", 16): 51.6759,
    ("prize", 4): 898752770168.33, ("prize", 8): 609603246880.83,
    ("prize", 16): 379193191914.88,
}

ROWS = [
    ("RowC", 1024, 4, 256, B_STAR_ROWC),
    ("RowC", 1024, 8, 256, B_STAR_ROWC),
    ("RowC", 1024, 16, 512, B_STAR_ROWC),
    ("prize", 1 << 41, 4, 256, B_STAR_PRIZE),
    ("prize", 1 << 41, 8, 256, B_STAR_PRIZE),
    ("prize", 1 << 41, 16, 512, B_STAR_PRIZE),
]

print()
print("row    rate  A              j (odd)        log2 N_dih       s'_crude   s'_E26strict(log2)  needed suppression (bits)")

for label, n, rd, dec, bstar in ROWS:
    key = (label, rd)
    k = n // rd
    A = k + n // dec + 1
    j = n - A
    A_pin, s_bottom_pin = AUDIT_PINS[key]
    tag = f"{label} 1/{rd}"

    check(f"{tag}: candidate A = {A_pin} (audit sect.2 pin)", A == A_pin)
    check(f"{tag}: j = n - A = {j} is ODD", j % 2 == 1)

    bq_ub = bquot_ub(n, k, A)
    bq_strict = bquot_strict(n, k, A)
    btan = n - A + 1
    check(f"{tag}: B_quot strict = 0 at odd j (audit convention)", bq_strict == 0)

    # E26 strict window column: d = m*ell with twin-fiber size m even (m = 2
    # pure, 4, 8, ... mixed) can never equal odd j -> column is exactly 0.
    e26_zero = all((j % m != 0) or (j // m) * m != j for m in (2,)) and j % 2 == 1
    check(f"{tag}: E26 strict window count at d = j is 0 (j odd, d = m*ell even)",
          e26_zero)

    # crude dihedral column
    P = (n - 2) // 2          # moving inverse pairs on mu_n (n even)
    K = (j - 1) // 2          # pairs in an odd-size inversion-closed support
    check(f"{tag}: support shape feasible (1 <= K <= P)", 1 <= K <= P)

    if n <= 1 << 12:  # Row C: exact big integers
        N_dih = 2 * math.comb(P, K)
        l2nd = log2big(N_dih)
        check(f"{tag}: LOUD — N_dih > B* on its own (exact)",
              N_dih > bstar, f"excess {l2nd - log2big(bstar):.4f} bits")
        s_crude = bstar - bq_ub - btan - N_dih
        check(f"{tag}: s'_crude < 0 (exact)", s_crude < 0,
              f"log2|s'| = {log2big(-s_crude):.4f}")
        check(f"{tag}: s'_crude fails the 2^100 flag", s_crude < TWO100)
        s_e26 = bstar - bq_ub - btan
        check(f"{tag}: s'_E26strict = audit s bottom end (exact)",
              s_e26 == s_bottom_pin)
        check(f"{tag}: s'_E26strict >= 2^100 (INVALID column, see note)",
              s_e26 >= TWO100, f"log2 = {log2big(s_e26):.4f}")
        b_allow = s_e26 - TWO100
        supp = l2nd - log2big(b_allow)
        check(f"{tag}: note log2 N_dih pin", abs(l2nd - NOTE_LOG2_NDIH[key]) < 1e-4,
              f"{l2nd:.4f}")
        check(f"{tag}: note suppression-exponent pin",
              abs(supp - NOTE_SUPPRESSION[key]) < 1e-4, f"{supp:.4f}")
        crude_str = f"-2^{log2big(-s_crude):.2f}"
    else:  # prize: rigorous integer route + Robbins display bracket
        m = min(K, P - K)
        # C(P,K) >= (P/m)^m >= 2^m since P >= 2m; 2^m > B* iff m >= bitlen(B*)
        check(f"{tag}: rigorous N_dih > B* (P >= 2m and m >= bitlen(B*))",
              P >= 2 * m and m >= bstar.bit_length(),
              f"m = {m}, bitlen(B*) = {bstar.bit_length()}")
        lo, hi = log2C_bracket(P, K)
        lo, hi = lo + 1, hi + 1  # the factor 2 (choice of fixed point)
        check(f"{tag}: Robbins bracket sane (0 <= hi - lo < 1e-4)",
              0 <= hi - lo < 1e-4, f"log2 N_dih in [{lo:.2f}, {hi:.2f}]")
        l2nd = lo
        # s'_crude = B* - bq_ub - btan - N_dih <= B* + bq_ub + btan - 2^m < 0:
        # rigorous via bit lengths (x < 2^bitlen(x) <= 2^m), never building 2^m
        check(f"{tag}: s'_crude < 0 (rigorous: N_dih >= 2^m > B* + B_quot_ub + B_tan)",
              m >= (bstar + bq_ub + btan).bit_length())
        check(f"{tag}: s'_crude fails the 2^100 flag", True,
              "implied by s'_crude < 0")
        s_e26 = bstar - bq_ub - btan
        check(f"{tag}: s'_E26strict = audit s bottom end (exact)",
              s_e26 == s_bottom_pin)
        check(f"{tag}: s'_E26strict >= 2^100 (INVALID column, see note)",
              s_e26 >= TWO100, f"log2 = {log2big(s_e26):.4f}")
        b_allow = s_e26 - TWO100
        supp = lo - log2big(b_allow)
        check(f"{tag}: note log2 N_dih pin", abs(l2nd - NOTE_LOG2_NDIH[key]) < 0.5,
              f"{l2nd:.2f}")
        check(f"{tag}: note suppression-exponent pin",
              abs(supp - NOTE_SUPPRESSION[key]) < 0.5, f"{supp:.2f}")
        crude_str = f"< 0; log2|s'| ~ {l2nd:.2f}"

    print(f"{label:6s} 1/{rd:<3d} {A:<14d} {j:<14d} {l2nd:<16.4f} "
          f"{crude_str:<28s} {log2big(s_e26):<19.4f} {supp:.4f}")

print()
print(f"{PASS} PASS, {FAIL} FAIL")
if FAIL == 0:
    print("VERDICT: crude (only VALID in-repo) column gives s' < 0 at all six")
    print("candidates — the 2^100 flag FAILS; gap QA21-G1 stands (see note).")
sys.exit(0 if FAIL == 0 else 1)
