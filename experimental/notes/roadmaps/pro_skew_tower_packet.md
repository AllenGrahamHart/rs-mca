# Pro skew-tower packet (verified 12/12 — see verify_pro_skew_packet.py)

1. PROFILE-CONSTANCY FALSIFIED as stated (falsification #15, mine): explicit
   F_17 level-1 witness — states M_A=(0,0,0,1,3,2,1,1), M_B=(0,0,0,2,1,1,3,1),
   identical profile, both upper-valid, B(M_A)=0 vs B(M_B)=2 (replayed).
   Level-1 constancy in our data was a subsets-only (multiplicity <= 2,
   singleton-active) artifact. Replacements, proved: scaling invariance;
   full-odd-window power invariance (fails for truncated windows); and:

2. VANDERMONDE RIGIDITY (proved, replayed): if the active support of a
   level-j skew is <= L_j = ceil(T_j/2), the only skew is zero (divide by
   x_i, the y_i are distinct, the Vandermonde minor is invertible). Hence
   B_j(M) IS profile-only in the small-support regime ({0,1} by parity),
   and any nonzero level-j skew at prize t = 2^33 needs support >=
   2^{32-j} + 1 — enormous thresholds (level 0: 2^32+1 of the 2^40 cells).

3. BOUNDED-COEFFICIENT NORM GATE (proved, example verified Res = 97^2):
   for |c_a| <= C and omega of order M = 2^R: P_c(omega) = 0 forces EITHER
   the cyclotomic/coset case (c_a = c_{a+M/2} identically — the char-0
   relation, counted exactly: C(M/2, k/2)(2C)^{k/2} for even weight k) OR
   p | Res(X^{M/2}+1, Q_c) with Q_c the folded polynomial — the explicit
   cleared norm. FOR TOWER SECTIONS (no opposite pairs): the coset case
   forces d = 0, so EVERY nonzero tower skew is norm-gated at EVERY imposed
   odd r simultaneously: p | gcd_r Res(X^N+1, Q_{d,r}). No bounded-
   coefficient escape exists.

4. THE EXACT CASCADE (the reformulated core): B_j(M) = q^{-L_j} sum_lambda
   prod_y sum_d psi(d lambda . v_y); lambda = 0 gives the balanced mean;
   sum_j L_j = t exactly (each m <= t is uniquely 2^j * odd). The central
   statement is EQUIVALENT to: the U-weighted average of prod_j rho_j
   (rho_j = B_j / balanced mean) is q^{o(t)}. Sufficient: sum_j sup log_q
   rho_j = o(t) per level on the central measure.

5. UNCONDITIONAL TWO-LEVEL GATE BOUND (proved): the levels-0/1 non-coset
   excess is carried entirely by skews with support >= 2^32+1 / 2^31+1
   respectively, each passing the simultaneous resultant gates for the
   actual prime q.

REMAINING CORE (sharp): bound the number of large-support bounded-coefficient
vectors whose L_j folded resultants share the fixed ~2^250-bit prime factor —
the rho_j product bound. The problem is now exact, structured, and entirely
in the norm-gate language the campaign certifies elsewhere.
