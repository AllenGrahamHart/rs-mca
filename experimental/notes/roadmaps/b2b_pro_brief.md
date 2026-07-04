# Hand-off brief: the giant-regime no-concentration bound (B2b)

Self-contained; verification-first culture: every claim below labeled
PROVED has a machine-checked certificate in the repo
(github.com/AllenGrahamHart/rs-mca, branch allen/prize-dag-delta,
experimental/notes/roadmaps/ — esp. b1_char0_giant_coset_theorem.md,
b2b_balance_concentration_scan.md). Citations you use will be checked;
please flag anything cited from memory as [CITATION NEEDED].

## Setup

F_q with q = p prime (~2^256; a variant allows q = p^2), n = 2^s | q-1
with n = 2^41, mu_n < F_q* the 2-power subgroup, domain D = gamma mu_n
(|D| = n). For B a SUBSET of D and r >= 1 write p_r(B) = sum_{x in B}
x^r. Call B "t-null" if p_r(B) = 0 for r = 1..t, with t = t* =
8589934593 (~2^33). Note char p > t, so Newton gives: t-null iff the
locator L_B(X) = prod_{x in B}(X - x) has its top t sub-leading
coefficients zero.

## What you may assume (PROVED, verifier-backed)

1. **Char-0 classification.** Over C: every 0/1 t-null subset of mu_n
   is a union of mu_M-cosets, M = least 2-power > t. Proof shape
   (one paragraph, reusable): the exponent polynomial f_B has INTEGER
   coefficients, so f_B(zeta^r) = 0 propagates to the full Galois
   orbit = all r' with the same 2-adic valuation; r in [1,t] realizes
   every valuation <= log2 t; hence the spectrum of B lies in MZ and a
   0/1 function with spectrum in MZ is a coset union.
2. **The Frobenius gap.** At the rows in question q = 1 mod n, so
   Frobenius acts trivially on frequencies: the Galois forcing above
   has NO mod-p analogue. Finite-row extras genuinely exist:
3. **The boundary class (real, priced).** Coset unions at scale M = t
   whose quotient patterns are zero-sum sets exist at finite rows via
   subset-sum arithmetic (the "X-8 class"); they are EXACTLY counted
   (<= 64 per official row) and are budgeted. Any theorem must carve
   this class out, not exclude it.
4. **First-moment balance.** t log2 q is within ~2 percent of n
   (2.15e12 vs 2.20e12): the number of subsets and the number of
   constraint-bits nearly match. Pure counting/pigeonhole CANNOT
   close the problem. (This is also why the X-8 class exists.)
5. **Failed routes (quantified in-repo).** Char-0 lifting: dead
   (weight b ~ 10^9; norm thresholds astronomically exceeded).
   Naive union bounds: dead by (4).

## The target

**Theorem (B2b, sought).** At the official prize-max rows: the number
of t-null subsets B of D that are NOT unions of mu_M-cosets (M > t)
and NOT in the priced boundary class is at most n^3 = 2^123 —
aggregated over all sizes |B|.

Lossiness is free: any bound <= 2^123 wins; even per-size bounds
summing to 2^123 win. We do NOT need zero.

## Empirical calibration (exhaustive scan, replayed; 39/39 rows)

Scaled rows reproducing the near-critical ratio t log2 q ~ n:
- Non-coset extras track the balanced mean EXACTLY below balance
  (ratio 2^0.00 at the widest row), max excess ratio 2^4.18 observed
  anywhere (vs toy cushion 2^15), and die BEFORE nominal balance —
  decay is faster than the mean. NO phase transition at the crossing.
- Above balance: ZERO non-coset blocks — the exact coset floor.
- Every near-crossing survivor is boundary-class (zero-sum quotient
  patterns, profiles (2,2,...,2), some antipodal). No sixth guise.
So the true concentration exponent is ~4 bits against a 123-bit
cushion. The theorem "should" be true with enormous room.

## Suggested frames (any route accepted)

(a) **The divisor frame.** t-null B of size b <=> L_B is a monic
degree-b divisor of the FULLY SPLIT X^n - delta (delta = gamma^n)
with a top-t coefficient gap. The complementary divisor M_B =
(X^n - delta)/L_B then also has constrained top coefficients (the
product's top t+1 coefficients are 0...0). Count divisor pairs
(L, M), LM = X^n - delta, both tops constrained. Possible tools:
log-derivative L'/L = sum 1/(X - x), gcd/lattice structure of the
divisor poset, Hayes-style equidistribution of divisors in short
coefficient boxes [CITATION NEEDED if used].

(b) **The dyadic descent (three prior wins with this shape).** Under
x -> x^2, a t-null SET B on mu_n pushes to a MULTISET B2 on mu_{n/2}
(multiplicities <= 2) with p_r(B2) = p_{2r}(B) = 0 for r <= t/2: so
t-null at scale n descends to (t/2)-null multisets at n/2. Iterating
log2(M) times reaches the boundary scale. The wanted induction: a
classification/count of near-null MULTISETS with bounded
multiplicity at each scale, with the coset unions as the fixed
points and the boundary class as the only leakage. (The set->multiset
generalization is the price of the descent; multiplicity <= 2^j at
depth j.)

(c) **Character orthogonality / large sieve at a FIXED row.** The
exact mean comes from orthogonality over delta or over rows; the
obstruction is fixing the row. A second-moment over the n conjugate
domains gamma mu_n (delta ranging over (F_q*)^n-th-power classes) is
admissible IF the final bound holds per fixed official row — variance
over an ambient family + a positivity/deletion argument may suffice
given the 119-bit margin.

## Acceptance bar and deliverable

Rigorous at the stated parameters (n = 2^41, t = t*, q ~ 2^256,
q = 1 mod n); constants lossy up to ~2^100 are fine. Partial results
of high value: the descent step alone (b), with the multiset
bookkeeping done honestly; or the divisor-pair count (a) at any
polynomial loss. State every hypothesis explicitly. Deliverable:
theorem + complete proof in plain LaTeX/markdown; number your
lemmas; we will machine-verify the arithmetic and replay any
computational claims.
