# Corridor eaters (ii)+(iii) and the corridor_ledger required-X_acl table

- **Status:** AUDIT / computation. Turns the two *delegable* corridor eaters
  (`corridor_window_cleanup` = (ii), `corridor_ext_crossing` = (iii)) into
  concrete arithmetic on banked, verifier-backed formulas, and prints the
  resulting **required magnitude** of the UNKNOWN eater (i)
  `acl_second_order` per rate. No theorem is proved and no DAG node is
  promoted here. Every cell is re-derived from first principles by
  `experimental/scripts/verify_corridor_eaters.py` (stdlib only, exit 0 iff
  green; all four checks PASS).
- **Parents / sources (all banked):**
  `proof_sketch/s2_paid_ledger.md` (corridor + Paid(A) frame; #3 = the
  corridor statement; R1' left end), `proof_sketch/s8_s9_assembly_and_negative.md`
  (verified widths 2.17/2.00/1.12/1.67), `proof_sketch/s5_s0_statements_and_object.md`
  (master per-rate table), `proof_sketch/s6_extension_lift.md` +
  `ext_pole_floor` (N(L)), `qfloor_exact`, `wp_detail/wp3_2_symbolic_scaling.md`
  (the acl second-order open item), `wp_detail/wp2_5_wp4_1_window_charts_and_displacement.md`
  (the per-point residual-chart machinery). Cross-checked against the
  pre-existing `verify_roadmap_r2_numbers.py` (identical beta/taustar/cap forms).
- **DAG nodes filled:** the numeric outputs of `corridor_ext_crossing` (iii)
  and `corridor_window_cleanup` (ii); the assembled `corridor_ledger` row set.

## 0. Frame, units, and the banked formulas

For a clean rate `rho`, at the top-of-range operating point `log2 q = 256`,
in **delta = 1 - a/n** coordinates, the corridor is the bracket of the true
threshold `delta*`, with four banked boundary reserves (reserve = `1-rho-delta`):

```text
quot  = 1 - rho - beta(rho)/128      quotient value-set crossing (R1' left end)
tau*  = 1 - rho - taustar(rho,256)   FM / entropy crossing (= list_hi)
cap   = 1 - rho - eta                Paper D cap (unsafe boundary), PROVED
        eta = 2^-9  (rho in {1/2,1/4,1/8}),  2^-10  (rho = 1/16)
ordering at every rate:   quot < tau* < cap
beta(rho) = (1/2)log2 3 if rho>=1/3 else (1/2)(H(2rho)+2rho)
          = 0.7925 / 0.7500 / 0.5306 / 0.3343   at 1/2 / 1/4 / 1/8 / 1/16
```

**Grid step = the cap reserve `eta` itself.** The verified corridor widths are
`W(rate) = (cap - quot)/eta`, reproducing 2.17 / 2.00 / 1.12 / 1.67 exactly.
The adjacency endgame (`adjacency_closing`) asks the three eaters to recover
`W - 1` grid steps so the residual bracket is one grid step:

```text
(i) X_acl(rate)  +  (ii) window  +  (iii) ext   >=  W(rate) - 1.
```

**Rate 1/2 is excluded** from the ledger (per `q3r5`: its three named
residuals are a separate endgame); the three *clean* rates are 1/4, 1/8, 1/16.

**Mechanism-to-interval assignment (the one modeling choice, stated openly).**
The corridor `[quot, cap]` splits at the entropy crossing `tau*`:
`[quot, tau*]` is governed by the quotient value-set count (the
`acl_second_order` o(1)) and `[tau*, cap]` by the FM/aperiodic residual (the
window machinery). Eater (iii) is the extension column. This partition makes
the three eaters sum to `W - 1` **by construction** (verified identity in
TASK C); the numbers `W, quot, tau*, cap` are banked, the assignment is the
convention that names which eater owns which sub-interval.

## 1. TASK A — eater (iii) `corridor_ext_crossing` (ext column at 6 points)

The proved ext-pole numerator (`ext_pole_floor`, s6 §2):

```text
N(L) = ceil( L(|F| - |B|) / (|F| - |B| + kL) ),   k <= 2^40,  |F| < 2^256.
```

At the six crossing points (three clean rates x {a_safe, a_safe-1}), the base
list size `L` is the qfloor mass `Acl = 2^{beta(rho) N'}` (`qfloor_exact`);
representative `N' = 256` gives `L = 2^192.0 / 2^135.8 / 2^85.6`.

**Generating rows (hypothesis H3 — the intended, favorable prize rows):**
`F = F_p(D) = B`, so `|F| - |B| = 0` and **N(L) = 0 for every L**. Result,
exact and interval-free:

```text
rate   a_safe   a_safe-1     N(L)=B_ext     grid steps recovered
1/4      -         -             0                0.000
1/8      -         -             0                0.000
1/16     -         -             0                0.000
```

**(iii) recovers 0.000 grid steps at every clean rate.** `corridor_ext_crossing`
is a *guard, not a term* for generating rows (s6 fork F2): the value is
point-independent because `F\B` is empty. No corridor is widened -> the node's
falsifier does not fire.

**Non-generating branch (EXCLUDED by H3, priced for honesty):** there `N(L) ~ L`
below saturation and crosses the MCA gate `~2^128` exactly at `L ~ 2^128`
(verified: `N(2^120)=2^120`, `N(2^128)=2^128`, `N(2^136)=2^136`), but this
imports the *wider* S7 list window (base reserve doubled) — it WIDENS rather
than tightens. So (iii) can only help under H3, where it contributes 0.

## 2. TASK B — eater (ii) `corridor_window_cleanup` (per-point boundary windows)

Machinery: `window_fm` (window FM ~ `2^-16000`, all alignments structured) and
`window_pred_aper0` (aperiodic numerator 0 throughout), applied per corridor
point as the finite residual-chart decision of
`wp2_5_wp4_1_window_charts_and_displacement.md` §1 (per-point, not per-curve).
The boundary window a point can clean is bounded by the FM/aperiodic gap
`[tau*, cap]`; cleaned per-point bounds, grid-step fraction recovered:

```text
rate   tau* (delta)   cap (delta)    (ii) = (cap - tau*)/eta   falsifier
1/4     0.746811       0.748047           0.6326               ok (tightens)
1/8     0.872853       0.873047           0.0991               ok (tightens)
1/16    0.936162       0.936523           0.3700               ok (tightens)
```

**FALSIFIER CHECK:** at every rate `cap > tau*`, so every per-point cleaned
window has strictly positive width. **NO point widens** — the eater's
falsifier ("a corridor point whose cleaned window widens") is NOT triggered
at any clean rate. (ii) recovers the `[tau*, cap]` gap above.

## 3. TASK C — `corridor_ledger`: required `X_acl(rate)`

Eater (i) `acl_second_order` is UNKNOWN; leave it symbolic as `X_acl(rate)`.
The ledger requires

```text
X_acl(rate)  >=  W(rate) - 1 - (ii) - (iii)
             =   (tau* - quot)/eta - 1        (since (ii)=[tau*,cap], (iii)=0).
```

| rate | W | (iii) ext | (ii) window | **required X_acl (i)** |
|------|------|-----------|-------------|------------------------|
| 1/4  | 2.000 | 0.000 | 0.6326 | **>= 0.3674** |
| 1/8  | 1.123 | 0.000 | 0.0991 | **>= 0.0234** |
| 1/16 | 1.674 | 0.000 | 0.3700 | **>= 0.3043** |

Identity `(i)+(ii)+(iii) = W - 1` holds exactly at all three rates (verified),
and `X_acl(rate)` equals the residual `[quot, tau*]` window minus one grid step
(cross-checked). **This is the deliverable that turns `acl_second_order` into a
concrete target:** the generating-function / saddle-point second-order term of
`Acl(N', l')` must supply at least the tabulated grid-step fraction per rate.

- **Rate 1/8 is nearly closed:** it needs only `>= 0.023` grid steps from (i)
  — consistent with `adjacency_closing`'s note that "width 1.12 = rho 1/8 is
  closest." Rates 1/4 and 1/16 need `~0.37 / ~0.30`.
- The `acl_second_order` regression anchor (its own attack surface): exact
  small-`N'` class counts `log2 Acl = 49.72 / 100.44 / 201.88` in the E1 packet
  — the expansion that produces `X_acl` must reproduce these, then be evaluated
  at the corridor-active order to certify `X_acl(rate)` meets the bar above.

## 4. Coverage, honesty ledger, and what is NOT computed here

- **Fully computed from banked formulas (all PASS):** the six ext values
  (TASK A), the three per-point window recoveries (TASK B), the three required
  `X_acl` (TASK C), and the master-table anchor.
- **The one modeling choice** (owned openly, §0): the assignment of `[tau*,cap]`
  to (ii) and `[quot,tau*]` to (i). If (ii) cleans *less* than the full
  `[tau*, cap]` gap at some point, the required `X_acl` at that rate rises by the
  shortfall; the ledger identity keeps the total at `W - 1`.
- **NOT proved / NOT located:** (i) `acl_second_order` itself is the open item
  (`wp3_2` open item A) — only its required magnitude is produced. The exact
  E1 small-`N'` count table (`log2 Acl = 49.72/100.44/201.88`) is cited from the
  `acl_second_order` node's attack surface; its standalone packet file was not
  located in-repo during this pass (named here so it can be pinned), but it is
  not needed for the required-magnitude computation, which uses only the banked
  `beta`, `taustar`, `cap`, and `N(L)` forms.
- **Verifier:** `python3 experimental/scripts/verify_corridor_eaters.py`
  (single process, <2 GB, deterministic; exit 0 = ANCHOR + TASK A/B/C all PASS).
