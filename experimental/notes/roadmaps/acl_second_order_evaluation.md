# Acl second-order term: evaluated for the corridor ledger (eater (i))

- **Status:** AUDIT / computation. Turns the UNKNOWN corridor eater (i)
  `acl_second_order` into a concrete per-rate NUMBER by substituting the
  EXACT, certified canonical-slope count `Acl(N', l')` (Paper B
  `thm:exactcount`) for its leading-order approximation `2^{beta(rho) N'}`,
  and reports the grid-step recovery `X_acl(rate)` the exact quotient end
  delivers. **No theorem is proved and no DAG node is promoted.** Every number
  is re-derived from banked, verifier-backed formulas by
  `experimental/scripts/verify_acl_second_order.py` (stdlib only, single
  process, < 2 GB; exit 0 = all recomputations self-consistent).
- **Parents / sources (all banked):**
  `proof_sketch/s2_paid_ledger.md` §3–4 (the `prop:qfloor` mass, the quot/FM/cap
  crossings, `beta`), `corridor_eaters_computation.md` (the required-magnitude
  table and the eater partition), `wp_detail/wp3_2_symbolic_scaling.md` (the
  `acl_second_order` open item = "A_cl second-order term"),
  `experimental/notes/m1/paperb_23_smooth_exact_count.md` +
  `experimental/scripts/verify_paperb_23_smooth_exact_count.py` (the EXACT count
  `thm:exactcount`, certified against brute force to `N' = 48`). DAG node
  `acl_second_order` (`attack_surface`: "verify against exact small-N' counts …
  log2 A = 49.72/100.44/201.88").
- **DAG node addressed:** `acl_second_order` — its required magnitude
  (`corridor_ledger`) is compared against the value the exact count actually
  supplies. This is an evaluation, not a promotion.

## 1. TASK 1 — the E1 counts, pinned

**The anchors `log2 Acl = 49.72 / 100.44 / 201.88` are the TOTAL (all-size)
antipodal `e1` value-set counts, not a size-restricted count.** For a 2-power
quotient order `N'` there are `n1 = N'/2` antipodal pairs `{z,-z}`; each pair
contributes one of three values `{0, +z, -z}` to `e1 = sum`, and global negation
identifies pairs, so the number of distinct `e1` classes is

```text
Acl_tot(N') = (3^{n1} + 1) / 2,     n1 = N'/2.
```

Recomputed exactly (verifier TASK 1a): `N' = 64/128/256` give
`log2 = 49.7188 / 100.4376 / 201.8752`, matching the cited `49.72/100.44/201.88`
to the printed precision. The leading exponent is the universal
`beta_0 = (1/2) log2 3 = 0.79248` and the second-order term is the constant
`-1` bit (the `/2` antipodal identification). **These anchors are for the
FULL count (`l' = N'/2`, i.e. `rho = 1/2`); rate 1/2 is excluded from the
ledger, so the anchors are a REGRESSION target, not the corridor input.**

**No standalone "E1 packet" integer file exists in-repo.** The E1 pilot
(PR #180, DAG node `row_c_experiment`) measured value-set *support*
`>= 2^33.4` by birthday sampling and cited these class counts as targets; the
exact class-count integers are supplied by the certified count formula, not
stored separately. Located and reused: `verify_paperb_23_smooth_exact_count.py`
(hash of the b=0 branch = `thm:exactcount`).

**The corridor input is the SIZE-restricted exact count** `Acl(N', l')` with
`l' = rho N' + 1` (`prop:qfloor`), on the 2-power domain (Row C: `n = 1024`):

```text
Acl(2^a, l') = sum_{u>=0, t=l'-2u>=0, u<=n1-t} C(n1, t) 2^t,   n1 = 2^{a-1}
```

(Paper B `thm:exactcount`; **CONDITIONAL** on the import `thm:vsimport` exactly
as `thm:23rigidity` is, but the finite values below are **unconditional** —
the verifier self-certifies them against brute-force distinct-`e1` enumeration
over two faithful primes at `N' = 8, 16`). The exact size-restricted counts at
the two 2-power orders bracketing each rate's crossing are pinned in verifier
TASK 1b — and their second-order **deficit** `D = beta*N' - log2 Acl` is
rate-dependent, NOT the constant `-1` bit of the full count:

```text
rate   N'         log2 Acl(N', rhoN'+1)   beta*N'    deficit (bits)
1/4    128 / 256   94.011 / 189.548       96 / 192   +1.989 / +2.452
1/8    128 / 256   67.335 / 134.803       67.9/135.8 +0.587 / +1.040
1/16   256 / 512   86.067 / 171.190       85.6/171.2 -0.491 / -0.037
```

## 2. TASK 2 — the second-order term, evaluated

The banked quot end (`s2` R1', reproduced by `verify_corridor_eaters.py`) is
`quot = 1 - rho - beta/128`: the leading mass `2^{beta N'}` crosses the MCA gate
`2^128` at reserve `= beta/128` (`N' = 128/beta`, using `reserve = t/n = 1/N'`).
Replacing the leading exponent by the exact count moves the crossing to `N'*`
solving `log2 Acl(N'*, rho N'*+1) = 128`; then

```text
X_acl(rate) = (reserve_firstorder - reserve*) / eta = (beta/128 - 1/N'*) / eta
sign(X_acl) = sign of deficit D(N'_fo) = 128 - log2 Acl(N'_fo, l')
```

(positive deficit ⇒ exact count is *below* the gate at the first-order crossing
⇒ true crossing is deeper ⇒ quot moves RIGHT ⇒ corridor tightens ⇒ `X_acl>0`).
`N'*` is found by log-linear interpolation across the two bracketing 2-powers;
the `X_acl` interval is the rigorous deficit-bracket `D(N'*) in [D(Nlo),D(Nhi)]`.

```text
rate   N'* (cross)   X_acl (point)   X_acl interval (rigorous)   sign
1/4    173.54        +0.04965        [+0.0466, +0.0575]          POS  (tightens)
1/8    243.09        +0.01637        [+0.0097, +0.0173]          POS  (tightens)
1/16   382.11        -0.00560        [-0.0103, -0.0008]          NEG  (widens!)
```

**The sign is robust:** the deficit at BOTH 2-powers bracketing each crossing
has a single sign per rate (independent of the interpolation), so `X_acl > 0`
for 1/4, 1/8 and `X_acl < 0` for 1/16 hold rigorously.

## 3. TASK 3 — the verdict table

Required magnitudes (from `corridor_eaters_computation.md` TASK C,
`= (tau*-quot)/eta - 1`, recomputed here):

| rate | X_acl delivered | required | margin | verdict |
|------|-----------------|----------|--------|---------|
| 1/4  | **+0.0497** | 0.3674 | −0.3178 | **FALLS SHORT by 0.318** |
| 1/8  | **+0.0164** | 0.0234 | −0.0071 | **FALLS SHORT by 0.0071** |
| 1/16 | **−0.0056** | 0.3043 | −0.3099 | **FALLS SHORT + FALSIFIER FIRES** |

**No rate CLOSES.** The exact second-order term supplies only `~0.02–0.05`
grid steps, while rates 1/4 and 1/16 need `~0.30–0.37` — a shortfall of an
order of magnitude. The `[quot, tau*]` segment is NOT eaten by the
second-order term alone at any rate.

**Headline — rate 1/8 (full precision):**

```text
X_acl(1/8) = 0.016367 grid steps   (rigorous interval [0.009732, 0.017253])
required   = 0.023435   ( quot = 0.870854, tau* = 0.872853, eta = 2^-9 )
margin     = -0.007067  ->  DOES NOT CLOSE (the ENTIRE interval < required)
```

Rate 1/8 is the closest (as `adjacency_closing` anticipated — width 1.12 is
nearest to 1), but the exact quotient-end count falls short by
`0.00707 +- 0.007` grid steps. Closure would require the rate-1/8 second-order
deficit to be `>= ~1.43` bits at the crossing scale; the exact count gives
`~0.99` bits there.

**FALSIFIER — rate 1/16 FIRES.** At the crossing scale `N' ~ 383` the exact
finite-`N'` effective exponent `log2 Acl / N' ~ 0.3353` *exceeds* the
asymptotic `beta = 0.33428`, so the exact count is LARGER than the leading
approximation and the second-order correction moves quot slightly LEFT —
`X_acl(1/16) = -0.0056 < 0`, the corridor marginally WIDENS. The magnitude is
tiny and swamped by the `0.304` requirement, but the sign is a genuine,
robust falsification of "the second-order term only tightens."

## 4. Conventions consumed and hypotheses (what any closure would be conditional on)

The `X_acl` numbers above consume, in order:

1. **Eater partition** (`corridor_eaters` §0, the one modeling choice):
   `[quot, tau*] -> (i) acl`, `[tau*, cap] -> (ii) window`, `(iii) ext = 0`.
2. **H3 generating-rows reading** (ext `|F| = |B|`, so `(iii) = 0`): sets the
   required target as `(tau*-quot)/eta - 1` rather than a wider bound.
3. **Banked cap / tau* / quot / beta formulas** (`s2`, `verify_roadmap_r2`,
   `verify_corridor_eaters`), operating point `log2 q = 256`, gate `2^128`,
   `eta = 2^-9` (`2^-10` at 1/16).
4. **The `reserve = 1/N'` ↔ quot map** (continuous idealization). On a 2-power
   domain the available `N'` are 2-powers only; the continuous crossing is a
   model of the banked continuous quot.
5. **`l' = rho N' + 1`** (`prop:qfloor`). The `+1` is load-bearing for 1/16:
   without it the deficit stays positive; with it, the count clears the gate at
   `N' ~ 383` and `X_acl(1/16)` goes negative.
6. **Exact count `Acl = thm:exactcount`** — CONDITIONAL on `thm:vsimport`
   (Paper B labeling); finite values here are unconditional (brute-certified).

**Honesty ledger.** Fully computed from banked/certified inputs: the anchor
reproduction, the exact size-restricted counts, the three `X_acl` values (with
rigorous sign and deficit-bracket intervals), and the verdict/margins. NOT
proved / NOT claimed: that `acl_second_order` closes any corridor (it closes
none); the continuous-`N'` interpolation of a 2-power-only count (its effect is
bounded by the deficit bracket, which does not change any verdict). The
determination lands **bracket-grade at all three clean rates** on the strength
of eater (i) alone — the honest failure mode `corridor_ledger` prices — with an
additional finding that at rate 1/16 the second-order term is (marginally) the
wrong sign.

- **Verifier:** `python3 experimental/scripts/verify_acl_second_order.py`
  (single process, < 2 GB, deterministic; exit 0 = TASK 1/2/3 self-consistent;
  the FALSIFIER firing at 1/16 is reported as a finding, not an exit failure).
