# Audit

1. The proof uses the actual bad witness support `S_z`; it never infers
   support-wise badness or containment from a common support elsewhere.
2. The minimum-distance comparison is strict: `wt(Delta_z)<=3w<=n-K`,
   whereas every nonzero Reed-Solomon codeword has weight at least
   `n-K+1`.
3. The interpolation root count is exactly `m-w=K`; fewer than `K` roots
   would not identify `h_z` with `c_z`.
4. The final injection counts distinct affine slopes, not witnesses or
   supports. One coordinate with `e_v(x)!=0` gives one ratio only.
5. The `w>=1` guard handles the `|L|<=1` branch. No assertion is made at
   `w=0`.
6. `verify.py` checks the two-anchor identities and the smooth
   `RS[F_17,F_17^*,8]` regression that refutes the former `+1` charge.
7. Coordinator audit (2026-08-12, PR-sweep session): `verify_audit.py` is
   an independent second code path. It decides badness of every finite
   slope on the `mu_16` fixture by an EXHAUSTIVE scan of all
   `C(16,10)=8008` supports with a full augmented-rank solver (verify.py
   checks only the two designated supports); the bad set is exactly
   `{3,5}`. It replays the PR #1160 section-1 falsifier construction at
   the fresh field `F_29` (`K=14`, `w=3`, three bad slopes, two-anchor
   ratio recovery exact), and pins the deployed KoalaBear and Mersenne-31
   charges (`2w=134944` / `134896`, `B_*` difference consistency, the
   `2^24-1` Mersenne-31 reserve form). All PASS.
