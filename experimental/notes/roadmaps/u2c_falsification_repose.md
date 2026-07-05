# u2c_giant_tnull_dichotomy: FALSIFIED AS STATED (2026-07-06) + re-pose

## The verified falsifying witness
Row q=97, n=32 (mu_32, zeta=28), t=2. T = {zeta^i : i in (0,1,2,8,12,30)} is 2-null
(p_1=p_2=0 mod 97), NOT a coset union. By the COMPLEMENTATION LEMMA (below), its
complement S (|S|=26 = 81% of the coset -- GIANT) is also 2-null, and S is not a
union of mu_M-cosets (verified directly, all dyadic M incl. mixed partitions).
160 such accidents exist at size 6 alone at this row; 168 at (73,24,t=2); 128 at
(17,16,t=2) size 5.

## The COMPLEMENTATION LEMMA (proved; verified 27,762/27,762 at t=2,3,4)
For S a subset of the full coset C = roots of X^n - delta: S is t-null iff C\S is
t-null (t < n). Proof: prod_{x in C}(1+ux) = 1 + (-1)^(n+1)(-1)^n delta u^n is SPARSE
(no u^1..u^(n-1) terms), so prod_{x in S}(1+ux) = sparse / prod_{x in C\S}(1+ux) and
the first t coefficients of prod_S equal (up to sign) the complete homogeneous
symmetric functions h_1..h_t of C\S; Newton's identities convert h_1..h_t = 0 <=>
p_1..p_t = 0 <=> e_1..e_t = 0. QED. COROLLARY (top band): any t-null S with
|S| >= n-t is the FULL coset (complement has support <= t, killed by the proved
Vandermonde/skew_support_threshold).

## Why the witness exists: the above-balance window
Accidents are RANDOM-MODEL objects: expected count of non-structural t-null b-sets
is ~ C(n,b)/q^t. At (97,32,t=2): q^t = 9409 << C(32,b) for b in [4,28] -- a huge
above-balance window; observed 160 accidents at b=6 matches the model (~96).
At t=3 and at large q/n the window closes and the census is CLEAN (0 accidents:
(97,16,t=2,3), (193,16,t=2), (73,24,t=3)).
PRIZE-MAX ROWS: t*log2(q) ~ 2.15e12 > n ~ 1.1e12, so q^t > 2^n: the window is
EMPTY AT EVERY b -- accidents entropically forbidden. The dichotomy was always
implicitly a sub-balance-regime claim; the statement failed to say so.

## Re-posed statement (the honest form)
At rows with q^t >= 2^n * (slack) (sub-balance everywhere; includes all official
prize-max rows by ~2%): every t-null block is a union of mu_M-cosets (M >= t,
zero-sum value patterns at multiples of M <= t). GUARDRAIL: the witness above
shows the regime hypothesis is NECESSARY, not decorative.

## Honest difficulty update
The repaired claim = "zero accidents when the expected count is < 1 uniformly" --
an entropic-suppression / anti-concentration statement (rare != impossible). This
is the SAME hard shape as the dli RES count. u2c is therefore NOT the easiest red
(previous assessment revised); its proved assets (complementation lemma, top-band
rigidity, t+1-coset rigidity) remain permanently banked.
