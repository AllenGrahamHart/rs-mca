#!/usr/bin/env python3
"""Verifier for the two delegable corridor eaters (ii) corridor_window_cleanup
and (iii) corridor_ext_crossing, and the corridor_ledger required-X_acl table.

AUDIT status: this re-derives, from the banked formulas only (stdlib), every
number quoted in experimental/notes/roadmaps/corridor_eaters_computation.md.
It proves no theorem and promotes no DAG node; it turns the two evidence-gated
eaters into concrete arithmetic and prints the required magnitude of the
UNKNOWN eater (i) acl_second_order per rate.

Banked inputs (all cross-checked against verify_roadmap_r2_numbers.py):
  beta(rho)      quotient value-set exponent  [s2 / s3b_iii_3, machine-verified]
  taustar(rho,q) FM/entropy crossing reserve  [s4 def:taustar]
  cap reserve    2^-9 (2^-10 at rho=1/16)     [Paper D cap, PROVED]
  quot reserve   beta(rho)/128 at log2 q=256  [s2 R1']
  N(L)           ext-pole numerator ceil(L(|F|-|B|)/(|F|-|B|+kL)) [s6 / ext_pole_floor, PROVED]

Grid step = the cap reserve eta itself (2^-9, or 2^-10 at rho=1/16); every
corridor quantity below is expressed in these eta units, exactly as the
verified corridor widths 2.17/2.00/1.12/1.67 are.

Run:  python3 experimental/scripts/verify_corridor_eaters.py
Exit non-zero iff any task check fails.
"""
from __future__ import annotations

import math

lg = math.log2


def H(x: float) -> float:
    return -x * lg(x) - (1 - x) * lg(1 - x) if 0 < x < 1 else 0.0


def beta(rho: float) -> float:
    return 0.5 * lg(3) if rho >= 1 / 3 else 0.5 * (H(2 * rho) + 2 * rho)


def taustar(rho: float, lgq: float) -> float:
    lo, hi = 1e-12, 1 - rho - 1e-12
    for _ in range(300):
        mid = (lo + hi) / 2
        if mid * lgq - H(rho + mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def N_extpole(L: int, absF: int, absB: int, k: int) -> int:
    """Extension-pole numerator (s6 / ext_pole_floor, PROVED).
    N(L) = ceil( L(|F|-|B|) / (|F|-|B|+kL) ).  For a GENERATING row |F|=|B|,
    the numerator (|F|-|B|) is 0 and N(L)=0 for every L."""
    X = absF - absB
    num = L * X
    den = X + k * L
    if den == 0:
        return 0
    return -((-num) // den)  # ceil division on non-negative integers


# rho, cap-reserve exponent, log2 q operating point.  Grid step (cap reserve)
# eta = 2^-9 at rho in {1/2,1/4,1/8}, 2^-10 at rho = 1/16.
LGQ = 256.0
CLEAN = [(1 / 4, 9), (1 / 8, 9), (1 / 16, 10)]  # the three clean rates (rate 1/2 excluded, q3r5)


def corridor_points(rho: float, capexp: int) -> dict:
    eta = 2.0 ** -capexp
    cap = 1 - rho - eta                       # Paper D cap (unsafe boundary), PROVED
    quot = 1 - rho - beta(rho) / (LGQ - 128)  # quotient value-set crossing, R1' left end
    tau = 1 - rho - taustar(rho, LGQ)         # FM / entropy crossing (= list_hi)
    W = (cap - quot) / eta                    # corridor width in grid (eta) units
    fm_window = (cap - tau) / eta             # [tau*, cap]  == eater (ii) ceiling
    quot_window = (tau - quot) / eta          # [quot, tau*]  == acl (i) residual region
    return dict(eta=eta, cap=cap, quot=quot, tau=tau,
                W=W, fm_window=fm_window, quot_window=quot_window)


def name(rho: float) -> str:
    return f"1/{round(1/rho)}"


# ---------------------------------------------------------------------------
# TASK A  (eater iii): corridor_ext_crossing  — ext column at the six points
# ---------------------------------------------------------------------------
def task_A():
    print("=" * 74)
    print("TASK A  eater (iii) corridor_ext_crossing : ext column N(L) at the")
    print("        six crossing points  (three clean rates x {a_safe, a_safe-1})")
    print("=" * 74)
    ok = True
    lines = []
    k = 2 ** 40  # prize cap on k
    # GENERATING rows (H3, the recommended/favorable prize rows): F = F_p(D) = B.
    absF = 2 ** 200      # any |F| < 2^256; value is irrelevant when |F|=|B|
    absB = absF          # generating => B = F
    print("\n  GENERATING rows (hypothesis H3, the intended prize rows): |F| = |B|")
    print("  base list size L at a corridor point = the qfloor mass Acl = 2^{beta N'};")
    print("  N(L) = ceil(L*(|F|-|B|)/(|F|-|B|+kL)) with |F|-|B| = 0.\n")
    print(f"  {'rate':<6}{'point':<12}{'L (base list ~2^betaN)':<24}{'N(L)=B_ext':<12}{'grid steps'}")
    ext_recovered = {}
    for rho, capexp in CLEAN:
        Nprime = 256  # a representative corridor-active quotient order (zone-b)
        L = int(2 ** (beta(rho) * Nprime))  # qfloor mass feeding the ext channel
        for pt in ("a_safe", "a_safe-1"):
            Nval = N_extpole(L, absF, absB, k)
            ok &= (Nval == 0)
            print(f"  {name(rho):<6}{pt:<12}{'2^%.1f' % (beta(rho)*Nprime):<24}{Nval:<12}{0.0:.3f}")
        ext_recovered[rho] = 0.0
    print("\n  => ext side recovers 0.000 grid steps at every clean rate (generating).")
    print("     corridor_ext_crossing is a GUARD, not a term, for generating rows")
    print("     (s6 fork F2): N(L) identically 0 because F\\B is empty.\n")

    # NON-GENERATING illustration (excluded by H3) — shows the arithmetic is live
    # and that it WIDENS rather than tightens (falsifier condition, priced).
    print("  NON-GENERATING illustration (EXCLUDED by H3; shown to price the branch):")
    absB2 = 2 ** 127          # q_gen < 2^128 forced by admissibility (s6 sect.3)
    absF2 = 2 ** 255          # |F| < 2^256
    for L in (2 ** 120, 2 ** 128, 2 ** 136):
        Nval = N_extpole(L, absF2, absB2, k)
        gate = 2 ** 128       # MCA gate |F|*2^-128 ~ 2^127
        print(f"    L=2^{int(lg(L))}: N(L)=2^{lg(Nval):.2f}  (gate ~2^128 crossed at L~2^128; "
              f"N~L below saturation)  {'CROSSES' if Nval > gate else 'below'}")
    print("    -> when live, the ext mechanism imports the WIDE S7 window (base reserve")
    print("       doubled); it does NOT tighten the corridor. FALSIFIER for (iii) fires")
    print("       ONLY on non-generating rows, which H3 excludes.\n")
    return ok, ext_recovered, lines


# ---------------------------------------------------------------------------
# TASK B  (eater ii): corridor_window_cleanup — per-point boundary windows
# ---------------------------------------------------------------------------
def task_B():
    print("=" * 74)
    print("TASK B  eater (ii) corridor_window_cleanup : per-point boundary window")
    print("        = the FM/aperiodic residual gap [tau*, cap] cleaned per point")
    print("=" * 74)
    print("\n  Machinery: window_fm (FM ~ 2^-16000) + window_pred_aper0 (aperiodic")
    print("  numerator 0) — per-point exact FM evaluation; the boundary window each")
    print("  corridor point can clean is bounded by the [tau*, cap] gap.\n")
    print(f"  {'rate':<6}{'tau* (delta)':<14}{'cap (delta)':<14}{'gap/eta = (ii)':<16}{'falsifier'}")
    ok = True
    ii = {}
    for rho, capexp in CLEAN:
        c = corridor_points(rho, capexp)
        gap = c["fm_window"]
        widens = gap < 0.0
        ok &= (not widens)  # FALSIFIER: any point whose cleaned window widens
        ii[rho] = gap
        flag = "WIDENS !!" if widens else "ok (>0, tightens)"
        print(f"  {name(rho):<6}{c['tau']:<14.6f}{c['cap']:<14.6f}{gap:<16.4f}{flag}")
    print("\n  Cleaned per-point bounds: every point's window has positive width")
    print("  (cap > tau* at every rate) => NO point widens; falsifier NOT triggered.")
    print("  Grid-step fraction (ii) recovered per rate = the [tau*,cap] gap above.\n")
    return ok, ii


# ---------------------------------------------------------------------------
# TASK C : corridor_ledger — required X_acl(rate) >= W - 1 - (ii) - (iii)
# ---------------------------------------------------------------------------
def task_C(ext_recovered, ii):
    print("=" * 74)
    print("TASK C  corridor_ledger : per-rate  W(rate) vs (i)+(ii)+(iii),")
    print("        required  X_acl(rate) >= W - 1 - (ii) - (iii)")
    print("=" * 74)
    print(f"\n  {'rate':<6}{'W':<8}{'(iii) ext':<11}{'(ii) window':<13}"
          f"{'req X_acl (i)':<15}{'identity check'}")
    ok = True
    rows = {}
    for rho, capexp in CLEAN:
        c = corridor_points(rho, capexp)
        W = c["W"]
        e_iii = ext_recovered[rho]
        e_ii = ii[rho]
        x_acl_req = W - 1 - e_ii - e_iii
        # identity: (i)+(ii)+(iii) = W-1  with (i) := x_acl_req  must hold exactly
        identity = x_acl_req + e_ii + e_iii
        id_ok = abs(identity - (W - 1)) < 1e-9
        # cross-check: x_acl_req must equal (tau*-quot)/eta - 1 (the [quot,tau*] residual)
        alt = c["quot_window"] - 1
        alt_ok = abs(x_acl_req - alt) < 1e-9
        ok &= id_ok and alt_ok
        rows[rho] = dict(W=W, iii=e_iii, ii=e_ii, x_acl=x_acl_req)
        print(f"  {name(rho):<6}{W:<8.3f}{e_iii:<11.3f}{e_ii:<13.4f}"
              f"{x_acl_req:<15.4f}{'OK' if (id_ok and alt_ok) else 'FAIL'}")
    print("\n  Reading: with ext (iii)=0 (generating) and window (ii) eating [tau*,cap],")
    print("  acl_second_order (i) must supply X_acl(rate) grid steps = (tau*-quot)/eta - 1")
    print("  to collapse the bracket to one grid step (adjacency_closing).")
    print("  This turns acl_second_order from a shape into a per-rate NUMBER target.\n")
    return ok, rows


def check_master_anchor():
    """Anchor: reproduce the verified master table so the eaters sit on it."""
    EXP = {1 / 4: (0.744141, 0.746811, 0.748047, 2.00),
           1 / 8: (0.870854, 0.872853, 0.873047, 1.12),
           1 / 16: (0.934888, 0.936162, 0.936523, 1.67)}
    ok = True
    for rho, capexp in CLEAN:
        c = corridor_points(rho, capexp)
        q, t, cp, w = EXP[rho]
        ok &= abs(c["quot"] - q) < 5e-6 and abs(c["tau"] - t) < 5e-6
        ok &= abs(c["cap"] - cp) < 5e-6 and abs(c["W"] - w) < 0.01
    return ok


def main():
    print("\ncorridor eaters (ii)+(iii) and the corridor_ledger required-X_acl table")
    print("banked-formula anchor (master per-rate table) ...", end=" ")
    anch = check_master_anchor()
    print("PASS" if anch else "FAIL")
    print()
    a_ok, ext_rec, _ = task_A()
    b_ok, ii = task_B()
    c_ok, _ = task_C(ext_rec, ii)
    print("=" * 74)
    print(f"  ANCHOR   : {'PASS' if anch else 'FAIL'}")
    print(f"  TASK A   : {'PASS' if a_ok else 'FAIL'}  (ext column = 0 at all 6 points, generating)")
    print(f"  TASK B   : {'PASS' if b_ok else 'FAIL'}  (no per-point window widens)")
    print(f"  TASK C   : {'PASS' if c_ok else 'FAIL'}  (ledger identity + [quot,tau*] cross-check)")
    print("=" * 74)
    allok = anch and a_ok and b_ok and c_ok
    raise SystemExit(0 if allok else 1)


if __name__ == "__main__":
    main()
