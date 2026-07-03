# QA.3 / E14 / QL.4 — integrality margin tables: FM at the candidate crossings (MCA + list mirror)

- **Status:** AUDIT — every number below is re-derived deterministically by
  `experimental/scripts/verify_qa3_e14_fm_margins.py` (117 PASS, 0 FAIL,
  17 LOUDFLAG findings, exit 0; exact `math.comb` for n <= 5000, Decimal
  prec-80 Stirling with certified error < 4e-25 bits above, no randomness).
  The two inline lemmas are PROVED (proofs written here). The
  *interpretation* layer (which DAG halves this discharges) is labeled per
  claim. Nothing here proves R2, imgfib, zone-(b), or thm:qcore endpoints.
- **DAG:** the computational half of `aperiodic_zero_at_crossing`
  (queue QA.3, overnight E14) + the QL.4 list-side mirror.
- **Parents:** `proof_sketch/s2_paid_ledger.md` (corridor, FM1, R1'),
  `s4_reserve_dictionary.md` (tau* identity, q-columns, B-budget),
  `s7_list_side.md` (list window, thm:qcore), `execution_queue.md`
  QA.3/QL.4, `overnight_orders_2026_07_03.md` E14.

## 1. Pinned conventions — and where the inputs were ambiguous

Objects (all agreements on the exact/closed grid, per the step-1 audit):

```text
FM(A)   = C(n,j) * q^(1-t),  j = n-A, t = A-k     (task formula; = the upper
          end of Lemma FM1's exact mean C(n,j)(1-q^-t)q^(1-t); conservative
          for every "< 1" check, relative gap < 2^-122 at these rows)
B*      = floor(q_line / 2^128)                    (the MCA gate, s4 sect.4)
A*      = max{ A : FM(A) > B* }                    (spine adjacent-pin form:
          FM(A*) > B* >= FM(A*+1); the "candidate crossing window" is
          A*-1 .. A*+2)
ZM(A)   = log2( n^3 * FM(A) )                      zero-margin: ZM < 0 =>
          integer aperiodic count EXACTLY 0 under R2 with B = 3
GM(A)   = ZM(A) - log2 B*                          gate-margin: GM < 0 =>
          R2(3)-worst-case count still <= B* (adjacency gate) even when
          the count is not forced to 0
A_zero  = min{ A : ZM(A) < 0 },   A_gate = min{ A : GM(A) < 0 }
mean(s) = C(n, k+s) * q^(-s)                       list extras mean at slack
          sigma = s (reserve arithmetic: s*log2 q vs log2 C(n,k+s))
sigma*  = max{ s : mean(s) >= 1 },  LM(s) = log2(n^3 * mean(s)),
sigma_zero = min{ s : LM(s) < 0 }
```

Conventions used, with honesty flags:

- **C1 (rows).** (a) pinned row `n=512, k=256, q_line = 17^32` **exact**.
  **FLAG F0:** the task brief pinned "log2 q = 131.1", but
  `32*log2(17) = 130.79881` and `B* = floor(17^32/2^128) = 6` (not 8) —
  the exact-`17^32` row is the repo's pinned row (s2 sect.4's `B* = 6`
  coherence check and s4's `ord(17 mod 512) = 32`, both re-verified).
  Both variants are tabulated; the brief's `131.1` row is labeled VARIANT.
  (b) Row C `n=1024, k = n*rho`, `log2 q = 250` taken as an **idealized
  exact** value — **FLAG:** no note I could read pins Row C's actual prime;
  margins shift by `<= (t-1)*|eps|` bits for `|eps| = |log2 q_true - 250|`
  and the integer crossing can move by 1 near knife edges. (c) prize-max
  `n = 2^41, k = rho*n`, `log2 q = 255.9` idealized exact (prize caps
  `k <= 2^40`, `|F| < 2^256`; rate 1/2 saturates the k-cap).
- **C2 (q-columns).** Everything is evaluated at `q_line`; s4 sect.4 wants
  the list/L1 reserve at `q_gen`. They coincide under the generating
  hypothesis H3 (verified for the pinned row; **assumed by convention**
  for the idealized rows — non-generating official rows split the columns).
- **C3 (poly budget).** `B = 3` per the task and s4's R2 budget. The
  tighter interleaved worst-case budget `B <= 1.6` (s7 sect.3) only
  *shrinks* `n^B`, so B = 3 is the conservative side for every check here.
- **C4 (floors).** Row C: `B* = 2^122` exact under C1(b). Prize-max:
  `log2 floor(2^127.9)` differs from `127.9` by `< 2^-127` — negligible
  against every margin below (verifier computes the floored integer).
- **C5 (list side).** `mean(s)` is the exact uniform-word (S, codeword)
  pair mean for an MDS row (Lemma L2); it upper-bounds the codeword count
  at agreement >= k+s. It is the **raw** mean: the imgfib object subtracts
  quotient/planted structure, and QL.4's "extras exactly 0 under imgfib"
  conclusion consumes this table only through the imgfib CONJECTURE. The
  planted-word *conditional* analysis is QL.2/QL.3's scope, not this note's.
- **C6 (unsafe-side windows, Table 4).** thm:qcore's `k + sigma` endpoint
  audit is still pending (s7 F1); Table 4 is corridor bookkeeping under the
  repo's current reading, labeled accordingly.

## 2. Two one-line lemmas [PROVED]

**Lemma M (monotone steps).** `FM(A+1)/FM(A) = j/((n-j+1)q) <= n/q`, so at
every row here (`log2 n <= 41 < log2 q - 80`) `log2 FM` drops by more than
80 bits per unit of A: strictly decreasing, the binary search for A* is
valid, and every `ZM < c` statement propagates to all larger A.
*Proof:* `C(n,j-1)/C(n,j) = j/(n-j+1)`; the `q^(1-t)` factor contributes
`q^-1`. QED. (Same statement for `mean(s)` with `s` increasing.)

**Lemma L2 (list mirror identity).** `mean(s) = FM(k+s)/q` exactly.
*Proof:* `FM(k+s) = C(n, n-k-s) q^(1-s)` and `C(n, n-k-s) = C(n, k+s)`. QED.
So the list crossing (`mean = 1`) is where FM crosses height `q`, which sits
`log2 q - log2 B* ~ 128` bits above B* — about half of one A-step
(`~ log2 q` bits) — whence `sigma* in {t*-1, t*}` (verified at all 10 rows).
Exactness of `mean(s)` for an MDS row: any k coordinates determine the
codeword; the remaining s agreements with a uniform word are independent
`q^-1` events, so `E[#{(S,c): |S|=k+s, c|_S = w|_S}] = C(n,k+s) q^-s`.
[PROVED-elementary; RS rows are MDS.]

## 3. MCA Table 1 — the FM/B* crossing windows (fork-F2 candidate points)

Verifier-derived (all margins in bits; `d* = delta(A*) = (n-A*)/n`):

```text
row (rate)          A*             t*          d*        ZM(A*)   ZM(A*+1)  ZM(A*+2)  ZM(A*+3)  GM(A*+1)  A_zero A_gate
pinned  (1/2,B*=6)  260            4           0.492188  +141.69  +10.84    -120.02   -250.89   +8.25     A*+2   A*+2
pinned-VARIANT(131.1,B*=8) 260     4           0.492188  +140.78  +9.63     -121.53   -252.70   +6.63     A*+2   A*+2
RowC    (1/2)       516            4           0.496094  +298.63  +48.60    -201.43   -451.46   -73.40    A*+2   A*+1
RowC    (1/4)       259            3           0.747070  +360.35  +111.90   -136.55   -385.01   -10.10    A*+2   A*+1
RowC    (1/8)       130            2           0.873047  +337.46  +90.23    -157.01   -404.27   -31.77    A*+2   A*+1
RowC    (1/16)      65             1           0.936523  +374.99  +128.85   -117.31   -363.50   +6.85     A*+2   A*+2
prize   (1/2)       1108104540514  8592912738  0.496092  +498.98  +243.06   -12.87    -268.79   +115.16   A*+2   A*+2
prize   (1/4)       556770474277   7014660389  0.746810  +323.97  +69.63    -184.71   -439.04   -58.27    A*+2   A*+1
prize   (1/8)       279600463335   4722556391  0.872852  +373.33  +120.21   -132.92   -386.04   -7.69     A*+2   A*+1
prize   (1/16)      140382131271   2943177799  0.936162  +331.30  +79.27    -172.75   -424.78   -48.63    A*+2   A*+1
```

Cross-checks: the crossing deltas reproduce s2 sect.4's FM column
(0.496094 / 0.746811 / 0.872853 / 0.936162 at `log2 q = 256`, n = 2^20;
all four within 5e-4, verifier PASS), and the pinned row's stripped-object
prediction at A = 265 has ZM = -512.67 < -400 (s2 sect.4's restated P2:
stripped count ~ 0 — reconfirmed).

**Findings (the honest part — CHECKED, not assumed):**

- **F1. The queue's expectation is FALSE inside the crossing window.**
  QA.3/E14 said "margins hugely negative (~ -thousands)" at the candidate
  points; at `A*` the margin is **positive by construction** (+141..+499:
  A* is the last mean-unsafe agreement), and at `A*+1` it is **positive at
  every one of the 10 rows** (+9.6 .. +243). `n^3 * FM < 1` first holds at
  `A_zero = A*+2` at every row, and from there for all larger A by Lemma M.
  The "-thousands" expectation is real only at the corridor candidates
  (Table 2). The DAG node's computational half is therefore TRUE **with a
  +2 offset convention** at the F2 (FM-decided) candidate, not at A*+1.
- **F2. Thin margin at prize-max rate 1/2.** `ZM(A*+2) = -12.87`: below
  zero (count = 0 under R2(3)) but above the -20 comfort bar — LOUDFLAG.
  Equivalent statement: the poly exponent absorbed at that single point is
  `B <= 3 + 12.87/41 = 3.31`; an R2 with B > 3.31 would NOT be absorbed at
  `A*+2` there (the >= 20-bit-headroom radius is A*+3, ZM = -268.79). The
  list mirror shows the same accident (`LM(sigma*+1) = -12.84`). This is a
  fractional-position (knife-edge) fact about `(n,q) = (2^41, 2^255.9)`,
  exactly the object QA.4's census parametrizes.
- **F3. Gate knife-edges.** `GM(A*+1) > 0` at pinned (+8.25 / +6.63
  variant), RowC 1/16 (+6.85), and prize-max 1/2 (+115.16): at those rows
  even the adjacency gate (count <= B*) cannot be certified at A*+1 from
  the mean with the n^3 slack — `A_gate = A*+2`. Fork-F2 adjacency
  certificates must either use the +2 offset or bring a sharper-than-mean
  input at A*+1.
- **F4. Pinned-row scope.** The pinned row's FM window (260/262) is *not*
  its operative threshold — the row is tangent-pinned at 506/507 (s2
  sect.4, `B* = 6 < n - A + 1` for all A < 507). Rows (a)/(a') are
  calibration rows for the arithmetic, nothing more.

## 4. MCA Table 2 — fork-F1 corridor candidates (where the DAG node's claim lives)

`A_quot = k + ceil(n * beta / (log2 q - 128))` (s2 R1' left end; beta =
0.7925 / 0.75 / 0.5306 / 0.3343 per s2 sect.3, 4 d.p.). The beta +-1e-4
rounding window is computed exactly over Fractions; integrality is invoked
on the candidate's safe side `A_quot + 1`:

```text
row (rate)     A_quot          beta-window            ZM(A_quot+1)            A_quot+1 - A_zero
RowC  (1/2)    519             [519, 519]             -701.51                 +2
RowC  (1/4)    263             [263, 263]             -881.94                 +3
RowC  (1/8)    133             [133, 133]             -651.53                 +2
RowC  (1/16)   67              [67, 67]               -363.50                 +1
prize (1/2)    1113137319176   +-1.72e6 steps         -1.2880e12 (+-4.4e8)    +5.03e9
prize (1/4)    562650789977    +-1.72e6               -1.4957e12 (+-4.4e8)    +5.88e9
prize (1/8)    284000672694    +-1.72e6               -1.1138e12 (+-4.4e8)    +4.40e9
prize (1/16)   143186674147    +-1.72e6               -7.0686e11 (+-4.3e8)    +2.80e9
```

All eight rows: `ZM(A_quot+1) < -20` across the whole beta window, and
`A_quot + 1 >= A_zero` (verifier PASS). At Row C the margins are hundreds
of bits; at prize-max they are ~10^12 bits — "2^-thousands" understates by
nine orders of magnitude. **Robust form (insensitive to beta precision and
to Acl's o(1), s2 F4):** by Table 1 + Lemma M, `n^3 * FM(A) < 1` for
*every* `A >= A*+2`, hence at every possible F1/zone-(b) resolution of the
candidate inside the corridor `[A_quot-ish, cap]` — the F1 conclusion does
not depend on where in the corridor the crossing lands, only on it lying
at or beyond `A*+2`, which the corridor ordering guarantees with 2.8-5.9e9
steps of room at prize scale (verified). Under fork F1, the computational
half of `aperiodic_zero_at_crossing` HOLDS with astronomical margins.
[Interpretation is conditional on R2 exactly as the DAG node states.]

## 5. List Table 3 — the QL.4 mirror: extras-mean crossings

```text
row (rate)          sigma*        t*-sigma*  LM(s*)   LM(s*+1)  LM(s*+2)  LM(s*+3)  sigma_zero
pinned  (1/2)       3             1          +141.73  +10.89    -119.96   -250.82   s*+2
pinned-VARIANT      3             1          +140.82  +9.68     -121.47   -252.63   s*+2
RowC    (1/2)       4             0          +48.63   -201.40   -451.43   -701.46   s*+1
RowC    (1/4)       3             0          +110.35  -138.10   -386.55   -635.01   s*+1
RowC    (1/8)       2             0          +87.46   -159.77   -407.01   -654.27   s*+1
RowC    (1/16)      1             0          +124.99  -121.15   -367.31   -613.50   s*+1
prize   (1/2)       8592912738    0          +243.08  -12.84    -268.77   -524.69   s*+1
prize   (1/4)       7014660388    1          +322.41  +68.07    -186.27   -440.61   s*+2
prize   (1/8)       4722556390    1          +370.55  +117.43   -135.69   -388.82   s*+2
prize   (1/16)      2943177798    1          +327.43  +75.40    -176.63   -428.65   s*+2
```

`sigma*/n` reproduces s4's tau* column (0.003906 / 0.002930... at Row C's
`log2 q = 250`; 0.003908 / 0.003190 / 0.002148 / 0.001338 at prize-max
`255.9` — cf. s4's 256-column 0.003906 / 0.003189 / 0.002147 / 0.001338).
The identity `mean(s) = FM(k+s)/q` checks to < 1e-20 bits at every row.

**Findings:**

- **F5. Same knife-edge, mirrored.** Extras-zero (`n^3 * mean < 1`) begins
  at `sigma*+1` or `sigma*+2` depending on the row's fractional crossing
  position: positive margins at `sigma*+1` at pinned (+10.89), prize 1/4
  (+68.07), 1/8 (+117.43), 1/16 (+75.40) — LOUDFLAGGED; Row C is clean at
  `sigma*+1` (margins -121 .. -201); prize 1/2 is thin (-12.84, F2 above).
  From `sigma*+3` on, every row is < -388 and monotone decreasing. The
  list endgame must treat `sigma*+1` exactly as the MCA side treats `A*+1`.

## 6. List Table 4 — exact 2-power quotient-core windows vs sigma* [convention pending s7 F1]

Exact rule (no asymptotics): `M_max` = largest 2-power `M | k` with
`C(n/M - 1, k/M) >= 2^128` (thm:qcore crossing); proved-unsafe radii are
`sigma in [1, M_max - 1]`:

```text
row (rate)     M_max        proved-unsafe   sigma*        first open radius, LM
pinned (1/2)   2            [1,1]           3             GAP [2,3]  (2 radii)
RowC   (1/2)   4            [1,3]           4             GAP [4,4]  (1 radius)
RowC   (1/4)   4            [1,3]           3             sigma=4:  -138.10
RowC   (1/8)   4            [1,3]           2             sigma=4:  -407.01
RowC   (1/16)  2            [1,1]           1             sigma=2:  -121.15
prize  (1/2)   2^33         [1, 2^33-1]     8592912738    GAP [2^33, sigma*] = 2,978,147 radii
prize  (1/4)   2^33         [1, 2^33-1]     7014660388    sigma=2^33:  -4.0066e11
prize  (1/8)   2^33         [1, 2^33-1]     4722556390    sigma=2^33:  -9.7896e11
prize  (1/16)  2^32         [1, 2^32-1]     2943177798    sigma=2^32:  -3.4070e11
```

- **F6. The s7-F2 "2-power artifact" made quantitative.** At rate 1/2 the
  2-power grid narrowly undershoots the mean crossing: at prize-max,
  `M_max = 2^33 = 8589934592` while `sigma* = 8592912738`, leaving a gap of
  **2,978,147 radii** that are neither 2-power-proved-unsafe (thm:qcore)
  nor extras-zero (mean >= 1). No contradiction — the mean is over uniform
  words while qcore plants structured words — but the list endgame's
  threshold localization at rate 1/2 NEEDS s7-F2's exact optimization over
  `M | k` (or another mechanism) to close that window. At rates 1/4, 1/8,
  1/16 the proved-unsafe window *overshoots* sigma* and the first open
  radius has margin < -121 (Row C) resp. < -3.4e11 (prize-max): clean.

## 7. Non-claims

- No claim on R2 / SPI / XR, imgfib, Conjecture F, or zone-(b): every
  "count exactly 0" statement here is the *computational premise* of the
  CONDITIONAL DAG node, never its rigidity hypothesis.
- No locator-to-slope conversion is claimed (unsafe-side fiber control).
- The FM mean is over uniform pairs; nothing here bounds a *specific*
  worst-case pair except through R2's poly envelope with B = 3.
- Idealized q rows: `log2 q in {250, 255.9}` are conventions, not official
  rows; Row C's true prime is unpinned (flag C1(b)). The pinned-row
  `131.1` task-brief value is recorded as inconsistent (F0).
- The cap point (`delta = 1 - rho - 2^-9`, `2^-10` at 1/16) is EXCLUDED:
  it lies on the unsafe side of the FM crossing (`FM > B*` there), so no
  integrality statement is meaningful at it; it is an unsafe-side
  construction (Paper D), not an integrality candidate.
- thm:qcore endpoint conventions (Table 4) pending the s7 F1 audit; the
  raw list mean vs the imgfib residual object per C5.
- beta values consumed at 4 d.p. from s2 sect.3 with exact +-1e-4 windows;
  Acl's second-order o(1) (s2 F4) is not resolved here — the F1 conclusion
  was deliberately stated in the o(1)-insensitive form (sect. 4).

## 8. Verifier

`experimental/scripts/verify_qa3_e14_fm_margins.py` — standalone python3,
stdlib only, deterministic. Re-derives every table above: precision
self-checks (Stirling vs exact comb to < 1e-22 bits), pinned-row facts
(`B* = 6`, `ord(17 mod 512) = 32`), the s2 crossing regression, both MCA
tables, both list tables, the L2 identity, and the monotonicity
preconditions. Prints PASS/FAIL per claim plus LOUDFLAG findings
(F1-F3, F5: the > -20 candidate points listed above). Current run:
**117 PASS, 0 FAIL, 17 LOUDFLAG, exit 0.**

Bottom line for the DAG: under fork F1 the computational half of
`aperiodic_zero_at_crossing` (and its QL.4 mirror away from the rate-1/2
gap) holds with margins from -121 bits (Row C) to -1.5e12 bits (prize-max).
Under fork F2 the node's phrase "at every candidate point" needs the
recorded +2 offset: integrality NEVER holds at `A*+1` (all 10 rows,
margins +9.6 .. +243), and at prize-max rate 1/2 it holds at `A*+2` with
only 12.87 bits to spare. The offsets and the rate-1/2 2-power gap are the
knife-edge objects QA.4 / s7-F2 must own before any tie is quoted as
decided.
