# QX.14 — the XR wall-pricing coverage table (DAG node `xr_radius_arithmetic`)

- **Status:** AUDIT. Every number below is machine-checked by
  `experimental/scripts/verify_qx14_xr_coverage.py` (215 checks, ALL PASS;
  exact integer arithmetic on the n=512 and n=1024 rows, rigorous two-sided
  Robbins/Stirling brackets on the n=2^41 rows, decisions verified at both
  bracket ends). The ball-profile lemma (S1) and the second-moment
  decomposition (S2) are PROVED-elementary **given the pinned
  pair-correlation ledger input**, which is an INPUT here, not re-derived
  (see S0.3). **MOMENT-LEVEL ONLY** (see S7).
- **DAG node:** `xr_radius_arithmetic` (execution_queue Tier D6, QX.14).
- **Parents:** `proof_sketch/s3b_iii_2_displacement_spectral.md` SS5
  (averaged XR), `proof_sketch/s2_paid_ledger.md` SS2 (FM1 conventions),
  `execution_queue.md` QX.13/QX.14.
- **Verifier:** `python3 experimental/scripts/verify_qx14_xr_coverage.py`
  (deterministic, exit 0 iff green).

## 0. Pinned notation and inputs

### 0.1 Row conventions (as in s2)

Row `(n, k, q)`, exact agreement `A = k + t`, co-support size `j = n - A`.
Agreement supports `S` (size `A`) correspond bijectively to co-supports
`T = D \ S` (size `j`) = vertices of the Johnson graph `J(n, j)`; the
exchange distance of two supports is `s = |S \ S'| = |T \ T'|`
(`J(n,j) ~ J(n,n-j)`, and the profile below is symmetric under `j <-> n-j`).
`B* = floor(q / 2^128)`. `X = X_{u,v}(A)` = number of supports of size `A`
aligned for SOME slope (`Pi_S(u) in span(Pi_S(v)) \ 0` in the
`m1_support_coefficient_test.md` normal form; each support contributes at
most one bad slope, so `X` upper-bounds the per-`A` slope count). FM scale
(Lemma FM1, s2 SS2, upper form): `E[X] <= C(n,j) q^{1-t}`.

### 0.2 The three shapes priced

```text
(a) pinned row   n = 512,  k = 256,  q = 17^32 exact.  log2 q = 130.7988
                 (NOT 131.1 as in the queue item text — rounding slip there;
                 spine says 130.799, verifier pins it), B* = 6 exact
                 (6*2^128 <= 17^32 < 7*2^128, verified).
(b) Row C        n = 2^10, k = 2^9,  log2 q = 250.  q := 2^250 used as an
                 exact SCALE STAND-IN (not a field pin); B* = 2^122.
(c) prize-max    n = 2^41, k = rho*n, rho in {1/2, 1/4, 1/8, 1/16},
                 log2 q = 255.9 (scale stand-in; the prize cap is
                 |F| < 2^256); log2 B* = 127.9.
```

Corridor `t`-values: s2 SS3 does not give per-row `t` directly, so the task's
fallback rule is used: `t* = ` the smallest `t` with
`C(n,j) q^{1-t} <= B*` (the FM/B* crossing, same convention as the spine's
"FM crosses B* between t=4 and t=5" at the pinned row — reproduced exactly),
plus neighbors `t*-1, t*+1`; row (a) also carries the `t = 9` line
(A = 265, the F1 stripped-instance exemplar). Cross-check: at `log2 q = 256`
my crossing deltas reproduce s2 SS4's FM column to `< 4e-7` at all four
rates (verified).

### 0.3 The pinned pair-correlation ledger [PINNED INPUT — not re-derived]

For two supports of size `k+t` at exchange distance `s >= 1`, the all-slope
pair probability is at most

```text
q^{1-t-min(s,t)}   (same-slope branch: union over q slopes, combined
                    syndrome rank t + min(s,t))
+ q^{2-2t}         (distinct-slope branch: independence).
```

Relative to the one-support FM scale `q^{1-t}` the extra suppression is
`q^{-c(s,t)}` with `c(s,t) = min(s, t-1)`; the exact packaging inequality
`q^{1-t-min(s,t)} + q^{2-2t} <= 2 q^{1-t} q^{-min(s,t-1)}` is verified for
every `s` on rows (a)/(b) as exact fractions. **Provenance (per
execution_queue QX.13):** external derivation (GPT Pro), independently
checked by hand + Monte Carlo; the repo-standard proof packaging is QX.13's
deliverable and is NOT done here. If QX.13 moves the exponent, the
same-slope column of this table moves with it. This is a moment-level
(average over `(u,v)`) statement throughout.

## 1. Ball profile [PROVED + exhaustively verified]

**Lemma B1.** In `J(n,j)`, the number of ordered pairs at exchange distance
`s` from a fixed vertex `T` is

```text
N_s = C(j,s) * C(n-j,s),        0 <= s <= min(j, n-j),
```

*Proof:* choose the `s` points of `T` that leave and the `s` points of the
complement that enter; the map is a bijection onto distance-`s` vertices.
QED. Totals: `sum_s N_s = C(n,j)` (Vandermonde). *Verification:* exhaustive
on **J(8,4)** (70 vertices, all 4900 ordered pairs, per-vertex histograms)
and **J(10,5)** (252 vertices, all 63504 pairs), plus the Vandermonde
identity for all `n <= 40`, all `j`. All PASS.

`N_s` grows like `(j(n-j))^s / (s!)^2` until the bulk peak: `N_{s+1} >= N_s`
iff `s <= (j(n-j)-1)/(n+2)`, so `argmax N_s = floor((j(n-j)-1)/(n+2)) + 1`
(verified exactly on rows (a)/(b); e.g. peak at `s = 128` for (a),
`s = 256` for (b), `s ~ 5.5e11 ~ j(n-j)/n` for (c) rate 1/2).

## 2. Second-moment profile [PROVED given the S0.3 input]

Grade `E[X^2] = sum_{S,S'} P[both aligned]` by exchange distance. With
Lemma B1 and the pinned ledger:

```text
E[X^2] <= E[X]                                        (diagonal, s = 0)
        + sum_{s>=0} C(n,j) N_s q^{2-2t}  =  E[X]^2   (far-pair independence
                                                       PLATEAU; the sum is
                                                       EXACTLY E[X]^2 by
                                                       Vandermonde)
        + sum_{s>=1} C(n,j) N_s q^{1-t-min(s,t)}      (same-slope branch).
```

The same-slope `s`-profile `T_s = C(n,j) N_s q^{1-t-min(s,t)}` splits:

```text
HEAD (1 <= s <= t):  per-step ratio T_{s+1}/T_s <= j(n-j)/q  << 1
   (verified exactly per row; gap G = log2 q - log2 j(n-j) is 114.8 /
   232.0 / ~176-178 bits on rows (a)/(b)/(c)) — strictly decreasing, so
   s = 1 dominates the head, and
   HEAD total <= E[X] * j(n-j)/(q - j(n-j))            [exact, verified].
TAIL (s > t):  suppression saturates at q^{-t}; POINTWISE the tail term
   equals the plateau term divided by q (T_s = plateau_s / q, verified
   exactly), so
   TAIL total <= E[X]^2 / q                            [exact, verified].
```

**Grand total (verified as exact integers on rows (a)/(b)):**

```text
E[X^2] <= E[X]^2 (1 + 1/q) + E[X] (1 + j(n-j)/(q - j(n-j))).
```

Measured sizes: row (a): head/E[X] = 2^-114.8, tail/E[X]^2 <= 2^-130.8;
row (b): 2^-232 and 2^-250. The excess over the plateau is `E[X](1 + tiny)`
at every in-band row.

## 3. Adjudication of the key claim

Claim as posed: *"since `j(n-j) << q`, the `q^{-s}` suppression dominates
ball growth for ALL `s >= 1`, so the same-slope close-pair mass is dominated
by `s = 1` and `E[X^2] = E[X]^2 (1+o(1)) + E[X] (1+small)`."*

```text
CONFIRMED  for the head 1 <= s <= t: per-step decay <= j(n-j)/q, s = 1
           dominates (exact checks, every row).
REFUTED    as stated "for ALL s >= 1": for s > t the ledger suppression
           saturates at q^{-t} and ball growth wins; the same-slope profile
           has a SECOND peak at the ball bulk s ~ j(n-j)/n.  Whether the
           bulk peak exceeds the s = 1 term is row-dependent:
           bulk wins  iff  N_peak * E[X] > N_1 * C(n,j)  (exact criterion,
           verified): s = 1 wins on row (a) and on all Markov-trivial rows;
           BULK wins on the contentful corridor rows (b) t=5 and (c) rate
           1/2 t*, and on every FM-unsafe (t*-1) row.
CONFIRMED  the conclusion, with the corrected mechanism: the bulk mass
           rides the PLATEAU at a q^{-1} discount (T_s = plateau_s/q
           pointwise for s > t), so
           E[X^2] <= E[X]^2 (1 + 1/q) + E[X] (1 + j(n-j)/(q-j(n-j)))
           holds on every row regardless of which peak is taller.
```

So the honest form of the claim is: *the excess over the plateau* is
dominated by `s = 1`; the raw same-slope profile is not.

## 4. The coverage table

All quantities re-derived by the verifier (`log2` values; exact integers
underneath on (a)/(b); Robbins brackets, both-ends-stable, on (c)).
`G = log2 q - log2 j(n-j)` = per-step head decay in bits. "Markov" =
`E[X] <= 1` (moment-level R2 then already follows from Markov;
see S5.4). `peak` = argmax of the same-slope profile over `s >= 1`.

```text
row  rate  n     t           A              j              log2C(n,j)   log2E[X] log2B* band Markov peak       s*_A            mech  s*_C
(a)  1/2   512   4           260            252            507.1        114.7    2.6    OUT  no     bulk       3 = t-1         (ii)  1
(a)  1/2   512   5 = t*      261            251            507.0        -16.2    2.6    IN   yes    s=1        4 = t-1  FULL   (i)   1
(a)  1/2   512   6           262            250            507.0        -147.0   2.6    IN   yes    s=1        4 < t-1 partial (i)   1
(a)  1/2   512   9 (A=265)   265            247            506.7        -539.7   2.6    IN   yes    s=1        4 << 8  partial (i)   1
(b)  1/2   1024  4           516            508            1018.6       268.6    122.0  OUT  no     bulk       3 = t-1         (ii)  1
(b)  1/2   1024  5 = t*      517            507            1018.6       18.6     122.0  IN   no     s=1        4 = t-1  FULL   (i)   1
(b)  1/2   1024  6           518            506            1018.6       -231.4   122.0  IN   yes    s=1        4 < t-1 partial (i)   1
(c)  1/2   2^41  8592912738  1108104540514  1090918715038  2.19893e12   376.0    127.9  OUT  no     bulk       t-1             (ii)  566581428
(c)  1/2   2^41  8592912739* 1108104540515  1090918715037  2.19893e12   120.1    127.9  IN   no     bulk       t-1      FULL   (i)   566581429
(c)  1/2   2^41  8592912740  1108104540516  1090918715036  2.19893e12   -135.9   127.9  IN   yes    s=1        t*-1    partial (i)   566581429
(c)  1/4   2^41  7014660389  556770474277   1642252781275  1.79505e12   201.0    127.9  OUT  no     bulk       t-1             (ii)  467502331
(c)  1/4   2^41  7014660390* 556770474278   1642252781274  1.79505e12   -53.4    127.9  IN   yes    s=1        t-1      FULL   (i)   467502331
(c)  1/4   2^41  7014660391  556770474279   1642252781273  1.79505e12   -307.7   127.9  IN   yes    s=1        t*-1    partial (i)   467502331
(c)  1/8   2^41  4722556391  279600463335   1919422792217  1.20850e12   250.3    127.9  OUT  no     bulk       t-1             (ii)  321589749
(c)  1/8   2^41  4722556392* 279600463336   1919422792216  1.20850e12   -2.8     127.9  IN   yes    s=1        t-1      FULL   (i)   321589749
(c)  1/8   2^41  4722556393  279600463337   1919422792215  1.20850e12   -255.9   127.9  IN   yes    s=1        t*-1    partial (i)   321589749
(c)  1/16  2^41  2943177799  140382131271   2058641124281  7.53159e11   208.3    127.9  OUT  no     bulk       t-1             (ii)  205816237
(c)  1/16  2^41  2943177800* 140382131272   2058641124280  7.53159e11   -43.7    127.9  IN   yes    s=1        t-1      FULL   (i)   205816237
(c)  1/16  2^41  2943177801  140382131273   2058641124279  7.53159e11   -295.8   127.9  IN   yes    s=1        t*-1    partial (i)   205816237
```

(`*` = corridor edge `t*`.  `G` bits: (a) 114.8, (b) 232.0, (c) 175.9 /
176.3 / 177.1 / 178.0 per rate.  Corridor `t*` pinned at both Robbins
bracket ends with in-band margins 7.8 / 181.3 / 130.7 / 171.6 bits.
Sanity: `delta*_FM = 1 - rho - t*/n` at `log2 q = 256` reproduces s2 SS4's
FM column: 0.4960939 / 0.7468114 / 0.8728533 / 0.9361621, diffs < 4e-7.)

## 5. The verdict: required ledger reach `s*`

### 5.1 Operational models (all three computed per row)

A "reach-`s*` ledger" certifies suppression `q^{-min(s, s*)}` at every
exchange distance `s` (compose `s*` one-exchange steps along a geodesic
prefix and stop — **monotone-composition assumption, a modeling choice**,
labeled as such). Budget = the R2 target scale `n^3 E[X]` (the `n^B`,
`B <= 3` budget of s3b_iii_1 / the spine's R2 line).

```text
s*_A  two-regime, task wording: smallest reach with excess-over-plateau
      <= n^3 E[X] (with the plateau E[X]^2 itself always allowed):
      s*_A = min(t-1, max(1, ceil((log2 C(n,j) - 3 log2 n)/log2 q))).
      Full reach t-1 ALWAYS suffices: E[X] * C(n,j) q^{-(t-1)} == E[X]^2
      exactly (verified identity) — mechanism (ii) "plateau".
s*_B  Chebyshev-strict at threshold n^3 E[X] with failure prob <= n^-3:
      requires Var <= n^3 E[X]^2, i.e. s* >= t-1 - 3 log2 n/log2 q;
      since 3 log2 n < log2 q on every row, s*_B = t-1 exactly. Always.
s*_C  three-regime SCENARIO: additionally grant the independence plateau
      for free at s >= t-1 (an unproved rank statement — the "easy regime"
      hope); the ledger then only has to cover the mid band, and
      s*_C = smallest s* with sum_{s* < s <= t-2} N_s <= n^3 q^{s*}
      (exact scan on (a)/(b); top-term-dominated bound on (c), band growth
      ratio >= 2^14 per step, verified).
```

### 5.2 Findings (the queue's question answered)

1. **`s* = 1` never closes a corridor row.** Under the pinned-ledger
   two-regime model, every corridor edge `t*` needs **FULL reach
   `s*_A = t* - 1`** — all three shapes, all four rates. The verdict line
   per rate at `n = 2^41`, `log2 q = 255.9`:

```text
   rate 1/2 : t* = 8,592,912,739   s*_A = s*_B = 8,592,912,738   s*_C = 566,581,429
   rate 1/4 : t* = 7,014,660,390   s*_A = s*_B = 7,014,660,389   s*_C = 467,502,331
   rate 1/8 : t* = 4,722,556,392   s*_A = s*_B = 4,722,556,391   s*_C = 321,589,749
   rate 1/16: t* = 2,943,177,800   s*_A = s*_B = 2,943,177,799   s*_C = 205,816,237
```

   **`s*` grows linearly with `t`: by the queue's own dichotomy, the wall
   is HARD, and we know WHERE** (see 3. below). Note `t*/n ~ 2^-8` at rate
   1/2 — the corridor reach is `~ n * 2^-8` exchange steps.
2. **Deeper in band the requirement freezes, not shrinks to 1:** at
   `t = t* + m` the uncapped requirement stays
   `ceil((log2 C - 3 log2 n)/log2 q) ~ t* - 1` (log2 C moves only ~bits per
   `t`-step), so partial reach `t* - 1` suffices there but nothing smaller
   does. Exception worth flagging: the **A=265 exemplar (row (a), t=9)**
   needs only reach `s*_A = 4 << t-1 = 8` — a partial, small-`t`-edge
   ledger *is* enough for the F1 stripped instance, exactly the "partial XR
   at small t is what P2 needs" fork (s3b_iii_2 SS7 F2).
3. **The three-regime softening is a small-`n` artifact.** Granting free
   independence at `s >= t-1` gives `s*_C = 1` on the (a)/(b) shapes (there
   `N_{t-2} <= 2^50 << n^3 q`), i.e. the toy wall would be genuinely soft;
   but at prize scale `s*_C ~ t*/15` at every rate (ratios 15.2 / 15.0 /
   14.7 / 14.3) — still ~half a billion exchange steps. The hard core is
   the **mid band `s in (t/15, t-1]`** of exchange distances at prize
   shapes: that is what `exchange_ledger_gen_t` would have to certify, and
   no budget reading in this table removes it.
4. **Markov column caveat:** at rates 1/4, 1/8, 1/16 (and rows (a) t>=5)
   the corridor edge has `E[X] < 1`, so moment-level R2 there follows from
   Markov alone (`P[X >= 1] <= E[X]`) with NO pair arithmetic; the
   contentful second-moment rows are rate 1/2 at (b) (`E[X] = 2^18.6`) and
   (c) (`E[X] = 2^120.1`, only 7.8 bits under `B*`). This does NOT soften
   the worst-case wall — it only says the average-case bookkeeping is
   cheap off the rate-1/2 corridor.
5. Near-coincidence worth recording: at the (c) rate-1/2 corridor edge the
   `(i)` mechanism engages with only ~3 bits of margin
   (`log2 C - 3 log2 n - (t-1) log2 q = -2.9`); mechanisms (i) and (ii)
   hand off essentially exactly at the corridor. This is the arithmetic
   shadow of `E[X] ~ B*` there.

## 6. Bridge row (LD_sw conventions)

`X` counts aligned supports at exact agreement `A` for the line pair
`(u,v)`; by the support-coefficient test (m1_support_coefficient_test.md,
PROVED) each support carries at most one bad slope, so per-`A` slope counts
are `<= X` and this table's `E[X]`-scale statements price
`B_ap(A)`-side mass in the s2 ledger's currency; `B* = floor(q/2^128)` as
in the spine's adjacent-pin form. Same `t`-crossing convention as the
spine's pinned-row consistency block (t*=5 at A=261, reproduced exactly).

## 7. Non-claims (honesty ledger)

- **Moment-level only.** Everything here is average-case over `(u,v)`
  (second-moment pricing). The fixed-word/worst-case conversion — turning
  "typical pairs have `X <= n^3 E[X]`" into "THE pair at hand does" — is
  the KMS/globalness branch's job (QX.10–QX.12) and is untouched by this
  table. This table prices only the ledger+anticode side of the
  `xr_distance_dichotomy` split.
- The pair-correlation ledger `c(s,t) = min(s,t-1)` is a **pinned input**
  (QX.13 provenance: external derivation, hand + Monte Carlo checked); it
  is NOT re-proved here, and no citation to a published reference exists
  for it [CITATION NEEDED — QX.13 packaging is the intended fix].
- `s*_B`/`s*_C` and the monotone-composition reading of "reach" are
  **modeling choices**, labeled where used; `s*_C`'s free-independence
  premise at `s >= t-1` is an unproved rank statement.
- No structured absorption credited: paid (tangent/quotient) mass is NOT
  subtracted from the pair mass; the table is conservative on that side.
- Rows (b)/(c) use `q`-scale stand-ins (`2^250`; `log2 q = 255.9`), not
  pinned prime powers; entries are scale statements. Row (a) is exact.
- No claim that `exchange_ledger_gen_t` is provable at ANY reach; the
  table only computes what reach WOULD suffice at moment level.
- The corridor `t*` is the FM/B* crossing per the task's fallback rule;
  s2 SS3's corridor is a delta-corridor and was used only as a cross-check
  (SS4 FM column reproduced to < 4e-7 at `log2 q = 256`).

## 8. Verifier

`experimental/scripts/verify_qx14_xr_coverage.py` — standalone python3,
deterministic, exit 0 iff green. Checks: [1] exhaustive ball profile on
J(8,4)/J(10,5) + Vandermonde sweep; [2] the ledger packaging identity,
exact, every `s`, rows (a)/(b); [3] exact integer second-moment profiles
(head decay/domination, tail=plateau/q pointwise, excess bounds, peak
formula, `s*` scans vs closed forms, `B* = 6`, `t* = 5`); [4] Robbins
bracket self-test vs exact binomials; [5] prize rows with both-bracket-end
stable decisions; [6] s2 SS4 cross-check. 215 checks, 0 failures at
writing.
