# QX.6 + QX.8 — the two elementary KMS bridges: E_3 <-> expansion, junta => paid

- **Status:** PROVED — every Lemma/Proposition/Theorem below carries a full
  elementary proof written in this note. The tightness-CONTRAST numbers for
  non-cell sets (random/ball slack ratios) are verified computation on toys,
  labelled as such. No [HEURISTIC] content is used anywhere in this note.
- **DAG nodes:** `xr_e3_to_expansion` (Bridge 1), `xr_junta_to_paid`
  (Bridge 2). Queue items QX.6 / QX.8 (Tier D3 of
  `execution_queue.md`). Parent sketch:
  `proof_sketch/s3b_iii_2_displacement_spectral.md` SS3; consumer:
  `c_xr_content` (the KMS decomposition of the XR inverse).
- **Verifier:** `experimental/scripts/verify_qx6_qx8_kms_bridges.py` —
  deterministic (seed 20260703), exact Fraction/integer arithmetic
  cross-checked against numpy eigendecompositions; exhaustive on
  J(6,3), J(8,4). GREEN: 167/167 PASS.
- **One flag for the maintainer (SS1.5):** the literal inequality direction
  quoted in the DAG node text ("phi(A) <= 1 - lambda_max(M_A)") is FALSE as
  stated; the corrected chain proved here delivers exactly what the KMS
  consumer needs, so no downstream statement changes. The DAG text should be
  re-worded on integration (not edited from this branch per task scope).

## 0. Pinned notation

```text
D          domain, |D| = n (in the program: the evaluation domain; j = n - A).
J(n,j)     Johnson graph: vertices V = {T subset D : |T| = j} (co-supports;
           locator l_T(X) = prod_{x in T}(X - x), root set = T, per
           s3b_iii_2 SS1); edges = one-exchanges T ~ T' iff |T cap T'| = j-1.
           No self-loops. Degree d = j(n-j); |V| = C(n,j).
M          = Adj/d, the one-exchange walk transition matrix: symmetric,
           doubly stochastic, stationary law uniform on V.
P_A        coordinate projection (diagonal 0/1 matrix) onto A subset V.
M_A        = P_A M P_A, the restricted operator; lambda_max(M_A) = top
           eigenvalue (equivalently of the principal submatrix M[A,A],
           since the complementary block is 0 and lambda_max >= 0).
mu(A)      = |A|/|V|.
E_k(A)     = <1_A, M_A^k 1_A> / |V|   (k >= 0; E_3 is the object of QX.6).
phi(A)     = e(A, V\A) / (d |A|), edge expansion (boundary edges once each).
lazy walk  M^lz = (I + M)/2, used ONLY in SS1.6; its expansion is phi/2
           (self-loops never leave). All DAG-facing quantities use the
           non-lazy M.
Eigenvalues of J(n,j):  lam_i = (j-i)(n-j-i) - i, i = 0..j (unnormalized);
           exact gap lam_0 - lam_1 = n (s3b_iii_2 SS3; re-verified).
```

Throughout, `A` is a nonempty subset of `V` (all statements are trivial for
`A` empty).

## 1. Bridge 1: E_3-large => non-expanding (node `xr_e3_to_expansion`)

### 1.1 Lemma (walk identity — task item (i))

For every `A subset V` and every `k >= 0`,

```text
<1_A, (P_A M P_A)^k 1_A>  =  |V| * P[ X_0, X_1, ..., X_k all in A ],
```

where `X_0` is uniform on `V` and `(X_i)` is the `M`-walk. Hence `E_k(A)` is
the probability that a stationary `k`-step walk stays in `A` at all `k+1`
times; `E_0 = mu(A)`, and `E_k(A)` is the quadratic form of the k-th power of
the restricted operator `M_A`.

*Proof.* `P_A` is idempotent and `P_A 1 = 1_A`, so the interior projections
collapse: `(P_A M P_A)^k = P_A (M P_A)^k`. Expanding the matrix product,

```text
<1_A, P_A (M P_A)^k 1> = sum over (x_0, ..., x_k), all in A, of
                          M(x_0,x_1) M(x_1,x_2) ... M(x_{k-1},x_k),
```

which is exactly `|V| * P[X_0 in A, ..., X_k in A]` since `P[X_0 = x_0] =
1/|V|` and `M` is the transition kernel. QED

### 1.2 Lemma (monotonicity and the exact one-step identity)

```text
(a)  mu(A) = E_0(A) >= E_1(A) >= E_2(A) >= E_3(A) >= ... >= 0.
(b)  E_1(A) = mu(A) * (1 - phi(A))     EXACTLY.
```

*Proof.* (a) By Lemma 1.1 each `E_k` is the probability of the event
`{X_0..X_k in A}`, and these events are nested decreasing in `k`.
(b) `<1_A, M 1_A> = (1/d) * 2 e(A)` where `e(A)` = edges inside `A`; counting
edge-endpoints in `A`: `d|A| = 2 e(A) + e(A, V\A)`, so
`<1_A, M 1_A> = |A| (1 - phi(A))`; divide by `|V|`. QED

### 1.3 Lemma (spectral cap — task item (ii))

Let `lambda_max = lambda_max(M_A)`. Then for every `k >= 1`

```text
E_k(A) <= mu(A) * lambda_max^k ,      and consequently
lambda_max(M_A) >= (E_k(A)/mu(A))^{1/k}   (large energy => large local
                                           spectral radius).
```

*Proof.* `M_A` is real symmetric with NONNEGATIVE entries. First,
`lambda_max` equals the spectral radius `rho(M_A)`: let `v` be a unit
eigenvector with `|lambda| = rho`; then, entrywise,

```text
rho = |<v, M_A v>| <= <|v|, M_A |v|> <= lambda_max
```

(first step triangle inequality using `M_A >= 0` entrywise, second step
Courant-Fischer), so `rho <= lambda_max <= rho`, i.e. `lambda_max = rho >= 0`
and `|lambda_i| <= lambda_max` for every eigenvalue. Now diagonalize:
`1_A = sum_i c_i u_i` in an orthonormal eigenbasis of `M_A`; then

```text
|V| E_k = sum_i lambda_i^k c_i^2 <= sum_i |lambda_i|^k c_i^2
        <= lambda_max^k sum_i c_i^2 = lambda_max^k |A|.   QED
```

(For odd `k` — the QX.6 case `k = 3` — monotonicity of `x -> x^k` already
suffices without the Perron step; the proof above covers all `k`.)

### 1.4 Lemma (Rayleigh direction — the true half of task item (iii))

```text
lambda_max(M_A) >= 1 - phi(A).
```

*Proof.* Courant-Fischer with the test vector `1_A`:
`lambda_max >= <1_A, M_A 1_A>/<1_A,1_A> = |A|(1-phi(A))/|A|` by the count in
Lemma 1.2(b). QED

### 1.5 Proposition (THE BRIDGE) — and a repair of the DAG wording

```text
phi(A)  <=  1 - E_3(A)/mu(A).
In particular:  E_3(A) >= eps * mu(A)   =>   phi(A) <= 1 - eps
                                        and  lambda_max(M_A) >= eps^{1/3}.
```

*Proof.* By Lemma 1.2, `E_3 <= E_1 = mu (1 - phi)`; rearrange. The spectral
consequence is Lemma 1.3 at `k = 3`. QED

This is the exact statement the KMS import (node `xr_kms_import`, QX.7)
consumes: `E_3`-large sets are non-expanding in the KMS hypothesis sense
(`phi(A) <= 1 - eps`, expansion bounded away from 1), with the small-set
regime supplied by `mu(A)` itself.

**Repair remark [the wording flag].** The DAG node text (and the task
phrasing) quotes the direction "`phi(A) <= 1 - lambda_max(M_A)`". That
inequality is FALSE in general — Lemma 1.4 proves the OPPOSITE direction,
`phi(A) >= 1 - lambda_max(M_A)`, and the gap is real: `lambda_max` is a max
over the restricted spectrum while `1 - phi(A)` is the AVERAGE Rayleigh
quotient of `1_A`, so any `A` whose indicator is not a top eigenvector gives
strict `lambda_max > 1 - phi(A)`. Explicit counterexample family (verified):
pad a tight cell with one far vertex. On `J(8,4)`, take
`A = {T : {0,1} subset T} u {{4,5,6,7}}`; the extra vertex is isolated in
`A`, so `lambda_max(M_A) = 1/2` (the cell block, Theorem 1.7) while

```text
phi(A) = 17/32 = 0.53125 > 1/2 = 1 - lambda_max(M_A)          [J(8,4)]
phi(A) = 11/15 = 0.7333  > 2/3 = 1 - lambda_max(M_A)          [J(6,3)]
```

Consequences, stated honestly: (a) the `E_3 => non-expansion` inference must
NOT route through `lambda_max`; Proposition 1.5 routes it directly through
monotonicity and is what this node now proves; (b) recovering a small-
expansion SUBSET of `A` from `lambda_max(M_A) ~ 1` is a local-Cheeger sweep
argument — standard but NOT proved here and NOT needed by the consumer
[CITATION NEEDED if some future consumer wants that variant]; (c) nothing
downstream changes: `c_xr_content`'s decomposition needs exactly
"E_3-large => KMS-hypothesis-shaped non-expansion", which 1.5 delivers.

### 1.6 Lemma (lazy walk: the reverse direction, parity-safe)

Define `M^lz = (I + M)/2` and `E_k^lz(A)` by Lemma 1.1 with kernel `M^lz`
(identity 1.1 holds verbatim for any transition kernel). The restricted lazy
operator `(P_A + M_A)/2` (compressed: `(I + M[A,A])/2`) is PSD, since
`spec(M[A,A]) subset [-1,1]` (as `||M[A,A]|| <= ||M|| = 1`). Then:

```text
(a)  E_1^lz(A) = mu(A) (1 - phi(A)/2)                        EXACTLY;
(b)  E_k^lz(A) >= mu(A) (1 - phi(A)/2)^k    for all k >= 0   (Jensen);
(c)  E_k^lz(A) <= mu(A) ((1 + lambda_max(M_A))/2)^k          (cap, as 1.3).
```

*Proof.* (a) The lazy kernel leaves `A` with probability `phi(A)/2` per step
on average over `A` (self-loop mass `1/2` never leaves), by the same count as
1.2(b). (b) Write the weights `w_i = c_i^2/|A|` of `1_A` in the eigenbasis of
the compressed lazy operator, `sum_i w_i = 1`, eigenvalues `nu_i in [0,1]`;
then `E_k^lz/mu = sum_i w_i nu_i^k >= (sum_i w_i nu_i)^k = (E_1^lz/mu)^k` by
convexity of `x -> x^k` on `[0, infty)`. (c) is Lemma 1.3 for the lazy
kernel, whose compressed eigenvalues are `(1 + lambda_i)/2`. QED

Why the lazy detour exists: for the NON-lazy walk, (b) can fail because
`M[A,A]` may have large negative eigenvalues (the Jensen step needs PSD).
Combining (b) and 1.2(a)-style monotonicity for the lazy kernel gives the
two-sided equivalence

```text
(1 - phi(A)/2)^3  <=  E_3^lz(A)/mu(A)  <=  ((1 + lambda_max(M_A))/2)^3 ,
```

i.e. for the LAZY energy, `E_3`-large and non-expanding are equivalent up to
cubing — the "structured => E_3-large" half that QX.1 wants is free here for
the lazy normalization. The non-lazy statements 1.1-1.5 are what
`xr_e3_to_expansion` itself asserts.

### 1.7 Theorem (cells are EXACTLY extremal — the tightness pattern)

Fix a core `C subset D`, `|C| = d_c`, and `tau subset C`, `|tau| = t`, and let

```text
Cell_C(tau) = {T in V : T cap C = tau}          (nonempty iff
                                       max(0, j-(n-d_c)) <= t <= min(j, d_c)).
```

Then, with `A = Cell_C(tau)` nonempty:

```text
(a)  every vertex of A has the SAME number of neighbors outside A, namely
     t(n-j) + (d_c - t) j - t(d_c - t);  hence
     phi(A) = [ t(n-j) + (d_c - t) j - t(d_c - t) ] / (j(n-j));
(b)  the induced subgraph on A is isomorphic to J(n - d_c, j - t)
     (via T -> T \ tau), in particular regular;
(c)  lambda_max(M_A) = 1 - phi(A)      EXACTLY;
(d)  E_k(A) = mu(A) (1 - phi(A))^k     EXACTLY for all k >= 0 —
     equality simultaneously in the spectral cap (1.3) and the bridge (1.5).
Specializations:  dictator (fixed-core, d_c = t = 1):  phi = 1/j;
                  fixed-hole (d_c = 1, t = 0):         phi = 1/(n-j).
```

*Proof.* (a) From `T` with `T cap C = tau`, a neighbor `T' = T \ {y} u {x'}`
(`y in T`, `x' notin T`) leaves the cell iff `y in tau` or `x' in C \ tau`
(note `C \ tau` is disjoint from `T`). Counting pairs: `y in tau` gives
`t(n-j)`; `x' in C \ tau` gives `(d_c - t) j`; both, `t(d_c - t)`;
inclusion-exclusion gives the stated count, independent of `T`. Dividing by
the degree `j(n-j)` and averaging (all terms equal) gives `phi`.
(b) A within-cell exchange moves some `y in T \ tau` to some
`x' in D \ (T u C)`; under `T -> T \ tau` this is exactly a one-exchange of
`(j-t)`-subsets of `D \ C`: an isomorphism onto `J(n-d_c, j-t)`. Its degree
is `(j-t)(n - j - d_c + t) = j(n-j) - [escape count]`, consistent with (a).
(c) The adjacency spectral radius of an `r`-regular graph is `r` (Rayleigh
with the all-ones vector + PF cap); here `lambda_max(M_A) =
(j-t)(n-j-d_c+t)/(j(n-j)) = 1 - phi(A)`.
(d) By (a), `P[X_{i+1} in A | X_i = x] = 1 - phi(A)` for EVERY `x in A`
(constant escape probability), so conditioning step by step,
`P[X_0..X_k in A] = mu(A) (1-phi(A))^k`; apply Lemma 1.1. QED

So the fixed-core cells (the k=1 "dictator" extremals of the E11/#191 scans)
do not merely come close to the spectral cap — they achieve EQUALITY in 1.3
and 1.5 at every `k`. This is the proved form of the "dictators are
near-extremal" tightness pattern.

### 1.8 Verified battery (toy numbers; verified computation)

Verifier output on `J(6,3)` (|V| = 20, d = 9, spectrum {9,3,-1,-3} with
multiplicities {1,5,9,5}, gap 6 = n) and `J(8,4)` (|V| = 70, d = 16,
spectrum {16,8,2,-2,-4}, multiplicities {1,7,20,28,14}, gap 8 = n). Ratio
column = `E_3 / (mu * lambda_max^3)` (= 1 iff the cap is tight):

```text
J(8,4)  set                       |A|   mu      phi      lam_max  E_3        ratio
        dictator {T: 0 in T}      35    1/2     1/4      3/4      27/128     1.000000000
        fixed-hole {T: 0 notin T} 35    1/2     1/4      3/4      27/128     1.000000000
        depth-2 core {0,1} sub T  15    3/14    1/2      1/2      3/112      1.000000000
        mixed {0 in T, 1 notin T} 20    2/7     7/16     9/16     729/14336  1.000000000
        closed ball B(v0,1)       17    0.24286 0.52941  0.50000  0.0289063  0.952205882
        random quarter (seeded)   17    0.24286 0.80147  0.24335  0.0027274  0.779297308
        random half (seeded)      35    0.50000 0.49643  0.54232  0.0716099  0.897915591

J(6,3)  dictator {T: 0 in T}      10    1/2     1/3      2/3      4/27       1.000000000
        (cells all ratio = 1; max non-cell ratio 0.970825 [closed ball])
```

All four cell rows are EXACT rational equalities (checked in Fraction
arithmetic, not floats). Every non-cell battery set shows strict slack
(ratio <= 0.99 on both graphs) — the contrast is a verified computation on
these toys, not a theorem about all non-cell sets.

## 2. Bridge 2: junta => paid strata (node `xr_junta_to_paid`)

### 2.1 Definitions

Fix a core `C subset D`, `|C| = d_c <= d_0` (a bounded constant; "d-junta"
below means `d_c <= d`). A set `A_J subset V` is a **junta on core C** if
membership depends only on the intersection pattern with `C`:

```text
T cap C = T' cap C   =>   ( T in A_J  <=>  T' in A_J ).
```

For `tau subset C` write `g_tau(X) = prod_{x in tau} (X - x)` (the fixed
divisor factor; `g_empty = 1`) and `Cell_C(tau)` as in SS1.7.

### 2.2 Proposition (cell decomposition — at most 2^d cells)

The cells `{Cell_C(tau) : tau subset C}` partition `V` (they are the fibers
of `T -> T cap C`), and a set `A_J` is a junta on core `C` iff it is a
disjoint union of cells:

```text
A_J = disjoint union over tau in S of Cell_C(tau),
S = { tau subset C : Cell_C(tau) cap A_J nonempty }   (unique),
|S| <= 2^{d_c} <= 2^d.
```

Moreover `|Cell_C(tau)| = C(n - d_c, j - |tau|)` (0 iff infeasible).

*Proof.* Fibers of a map partition the domain. If `A_J` is a junta and
`T in A_J cap Cell_C(tau)`, every `T' in Cell_C(tau)` has `T' cap C = tau =
T cap C`, so `T' in A_J`: the cell is contained in `A_J`; hence `A_J` is the
union of the cells it meets, disjointly, and `S` as defined is the unique
such index set. Conversely a union of cells trivially has the junta
property. The count: choosing `T` with `T cap C = tau` is choosing
`T \ tau subset D \ C` of size `j - |tau|`. QED

### 2.3 Proposition (divisor/avoidance characterization + the complementary-domain instance)

For every `tau subset C` and every `T in V`:

```text
T in Cell_C(tau)   <=>   g_tau | l_T   AND   l_T(x) != 0 for all x in C \ tau.
```

In locator language: the cell of pattern `tau`, `|tau| = t`, is exactly the
set of co-supports whose locator carries the FIXED divisor factor `g_tau`
(a common-divisor / tangent-type condition of depth `t`) and AVOIDS the
remaining core points `C \ tau`. Moreover:

```text
T -> T \ tau  is a bijection  Cell_C(tau) -> { (j-t)-subsets of D \ C },
l_T = g_tau * l_{T \ tau},
```

so the internal structure of a cell IS the Johnson instance
`J(n - d_c, j - t)` on the complementary domain `D' = D \ C` (matching SS1.7(b)),
with all locators sharing the fixed factor `g_tau`. The pure-avoidance cell
`tau = empty` is the complementary-domain instance outright.

*Proof.* `l_T` is monic with simple roots exactly at `T`. So `g_tau | l_T`
iff `tau subset T`, and `l_T(x) != 0` for `x in C \ tau` iff
`T cap (C \ tau) = empty`; together these say `T cap C = tau`. The bijection
and the factorization are immediate from `T = tau u (T \ tau)` with
`T \ tau subset D \ C`. QED

### 2.4 Proposition (correlation transfer — pigeonhole at cost 2^d)

Let `Al subset V` be any set (the intended instance: an alignment set
`A_{u,v}` per s3b_iii_2 SS3) and `A_J` a junta on core `C`, `|C| = d_c <= d`.

```text
(a) raw:      |Al cap A_J| >= delta |V|
              =>  exists tau subset C with
                  |Al cap Cell_C(tau)| >= delta |V| / 2^d.
(b) centered: |Al cap A_J| - mu(Al) |A_J| >= delta |V|
              =>  exists tau subset C with
                  |Al cap Cell_C(tau)| - mu(Al) |Cell_C(tau)|
                      >= delta |V| / 2^d.
```

*Proof.* By 2.2, `Al cap A_J` is the disjoint union of the `<= 2^d` sets
`Al cap Cell_C(tau)`, `tau in S`; the largest part is at least the average
(and in (b) the excesses likewise add over cells, since both the counts and
the sizes are additive over the disjoint cells). QED

### 2.5 Where the mass lands: the priced strata (consumers, by name)

Combining 2.3 + 2.4: **correlation of an alignment set with a d-junta =
alignment mass concentrated, at a `2^-d` pigeonhole discount, on one cell —
which is a common-divisor stratum of depth `t` (all co-supports share the
fixed factor `g_tau`: tangent-type structure) intersected with a
common-avoidance stratum, whose internal geometry is the complementary-
domain instance `J(n - d_c, j - t)` on `D \ C`.** Both landing zones are
priced strata in the repo taxonomy, and the pricing CONSUMERS are, by DAG
node name:

```text
common-divisor / tangent-type, depth t >= 1:
    `staircase`                (tangent staircase compiler #147, PROVED;
                                s2_paid_ledger SS1: B_tan(A) <= n - A + 1)
    `common_code_line_budget`  (MDS residual budget, PROVED;
                                experimental/notes/m2/
                                m2_common_code_line_residual_budget.md —
                                the general tangent-payment engine)
    assembled into Paid(A) via `paid_tan_fn` (s2_paid_ledger SS5).

common-avoidance / t = 0 (and the internal factor of every cell):
    the complementary-domain instance — the SAME alignment-counting problem
    with (n, j) -> (n - d_c, j - t) on D \ C. The pricing ledger consumes
    this by instance restriction (the recursion the Paid(A) compiler
    performs); no new stratum type is created.
```

Honest scope: this note DELIVERS mass onto those strata (the bridge); that
the strata are within budget is the consumers' proved content, cited above,
not re-proved here.

### 2.6 Base case remark

For `d = 1` the two cells are the fixed-core cell (`(X - x_0) | l_T`: the
depth-1 tangent / dictator structure) and the fixed-hole cell (the pure
complementary-domain instance on `D \ {x_0}`). Per the DAG and the overnight
orders, PR #191's proved `k = 1` extremal computation identifies exactly the
dictator structures as the `k = 1` extremals — the base case this bridge
generalizes. (#191 is cited as context and is NOT re-verified in this note.)

## 3. What the verifier checks (all green, 167/167)

`experimental/scripts/verify_qx6_qx8_kms_bridges.py`, deterministic seed
20260703, exit 0 iff all PASS:

```text
Bridge 1, on J(6,3) AND J(8,4), for a battery of 7 sets per graph
(dictator, fixed-hole, depth-2 core cell, mixed cell, closed ball,
seeded random quarter/half):
  - Johnson spectrum = formula incl. multiplicities; gap lam0-lam1 = n;
  - (1.1) walk identity, k = 0..3: exact Fraction DP for
    P[stay k steps] == numpy quadratic form of M_A^k   (< 1e-9);
  - (1.2) E_3 <= E_2 <= E_1 <= E_0 = mu and E_1 == mu(1-phi), EXACT rational;
  - (1.3) E_k <= mu lambda_max^k, k = 1,2,3;
  - (1.4) lambda_max >= 1 - phi;
  - (1.5) phi <= 1 - E_3/mu, EXACT rational;
  - PF: lambda_max(M_A) = spectral radius (>= |lambda_min|);
  - (1.6) lazy restricted operator PSD; E_1^lz == mu(1-phi/2) exact;
    E_k^lz >= mu(1-phi/2)^k exact rational, k = 0..3;
  - (1.7) all four cell sets: phi == closed formula, |A| == C(n-d,j-t),
    induced regularity, lambda_max == 1-phi, and EXACT equality
    E_k == mu(1-phi)^k (cap tight, ratio = 1); non-cell sets strictly
    slack (max ratio 0.9708 / 0.9522);
  - (1.5 repair) counterexample: phi(A) > 1 - lambda_max(M_A) strictly for
    depth-2-cell + far vertex (11/15 > 2/3 on J(6,3); 17/32 > 1/2 on J(8,4)).

Bridge 2, exhaustive on J(8,4), D = {0..7}, integer polynomial arithmetic:
  - all 36 cores |C| in {1,2}: cells partition V; sizes C(n-d,j-t);
    T -> T\tau bijects onto the (j-t)-subsets of D\C;
    l_T == g_tau * l_{T\tau} for every T (exact poly multiply);
  - divisor/avoidance characterization exhaustively: 8960 (C,tau,T)
    triples, T cap C == tau <=> g_tau | l_T and l_T != 0 on C\tau
    (exact division over Z, monic divisor);
  - all 480 unions-of-cells across all cores satisfy the junta property;
    recovery of the cell index set is unique with <= 2^d cells; negative
    control: a cell minus one vertex FAILS the junta property;
  - pigeonhole transfer (raw + centered), 2220 checks against 5 alignment
    stand-ins (2 structured + 3 seeded random).
```

## 4. Non-claims

```text
N1  NOT the KMS/DKKMS import (QX.7 / node `xr_kms_import`): no literature
    statement is used or asserted anywhere above; both bridges are
    self-contained and elementary. The quantitative matching of KMS's
    constants to FM scale is QX.9/QX.10-12, untouched here.
N2  No pricing re-proved: that tangent-type / complementary strata are
    within budget is consumed from `staircase`,
    `common_code_line_budget`, and the Paid(A) assembly (s2 SS5) — this
    note only lands the mass there (SS2.5).
N3  The literal DAG-node direction "phi(A) <= 1 - lambda_max(M_A)" is
    FALSE and NOT claimed (proved false by the SS1.5 counterexamples);
    the corrected chain (1.5) is what consumers should cite. The
    subset-version (local Cheeger sweep) is not proved here
    [CITATION NEEDED if ever consumed].
N4  The non-lazy converse "non-expanding => E_3-large" is NOT claimed
    (Jensen fails for non-PSD restrictions); the lazy version (1.6(b))
    is the proved substitute.
N5  Strict slack of NON-cell sets (SS1.8's contrast column) is a verified
    computation on the two toys, not a theorem about all non-cell sets;
    nothing downstream consumes it.
N6  PR #191's k=1 extremal computation is cited as context (SS2.6), not
    re-verified here.
N7  Nothing here is at prize scale: general-(n,j) statements are proved
    abstractly; the verifier grounds them exhaustively on J(6,3)/J(8,4)
    only.
N8  No claim that E_3-largeness of alignment sets HOLDS — that is the XR
    inverse's content (`c_xr_content`, `xr_inverse`); these are bridges,
    not the engine.
```
