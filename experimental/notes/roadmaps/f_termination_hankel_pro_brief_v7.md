# Pro brief v7 (same thread) — the final two deliverables

*Your rank-profile dichotomy was refereed and banked: the separation bound
verified on 233,130 distinct-closure atom pairs (0 violations), the
principal-kernel lemma on 4,000/4,000 row-deficient states (deg gcd = j+1-D
exactly, every time), and wide states were generically atom-free — all three
parts hold. Your Chebyshev syndrome transform is recorded as the L2 quotient
reduction. f_termination_hankel is now CONDITIONAL on exactly two packets.
This brief asks for those two. Close them and the whole chain discharges:
f_termination_hankel -> f_descent_termination -> f_dim_induction ->
f_primitive_case -> Conjecture F.*

## Deliverable 1 — the principal-kernel lemma, referee-grade
Write the binary-apolarity argument as a self-contained proof a referee can
check line by line:

> **Lemma (principal kernel).** Let M = (S_{i+c}), 0 <= i < t, 0 <= c <= j,
> be a finite Hankel matrix over a field K, and P = ker M with D = dim P > 0.
> If rank M < t, then there is a nonzero q in K[X] with deg q = j + 1 - D and
> P = q(X) * K[X]_{<= D-1}.

Please include: (i) the homogenization of the window S_0..S_{t+j-1} as a
binary form F of degree t+j-1 and the identification of P with the degree-j
piece of the apolar ideal I_F; (ii) the complete-intersection structure
I_F = (Q, R), deg Q + deg R = t + j + 1 (cite or prove the classical
statement — Sylvester / apolarity of binary forms — in the finite-field
setting, noting any characteristic caveats: our fields have char p > n >>
t+j, so divided-power subtleties should vanish, but SAY SO explicitly);
(iii) the rank-profile computation dim (I_F)_j = (j-a+1)_+ + (j-b+1)_+ and
the row-fullness criterion a >= t; (iv) the dehomogenization bookkeeping
(boundary monomial factors never vanish on mu_n). Also state the edge cases:
t = 0/1, D = j+1 (zero matrix), and the all-zero window.

## Deliverable 2 — L4: moment-clean leaves (the last mathematical open)
The state count n^{O(W^2)} bounds STATES; the downstream moment/residue count
needs a MEMBER bound at terminal leaves. The accounting framework stops the
recursion at states whose processed-atom family is empty, and its leaf lemma
requires the direction dual C_dir(P,E)^perp to contain no nonzero word of
weight <= r (r-wise uniformity of evaluations) — BUT the divisor count takes
a monic slice, which is AFFINE, so sparse direction-dual words with nonzero
affine constant can survive (the pinned-value seam).

The ask: for terminal UNPAID PRIMITIVE saturated Hankel leaves (post
gcd-strip, post Luroth/quotient routing, no weight-<=W atoms remaining),
prove ONE of:
- **(a) Cleanliness:** the direction dual on the active set has no nonzero
  weight-<=r word for the needed moment order r (note: by your own normal
  form, a weight-<=r direction-dual word IS a rational-defect atom — so
  "no atoms remain" may already imply cleanliness; if that implication is
  exact, the proof may be one page: make the linear-vs-affine distinction
  precise and check the monic slice);
- **(b) Pinned-value variant:** an explicit leaf member bound when sparse
  affine words with nonzero constant survive — the moment identity with the
  pinned values contributing an explicit, bounded correction term;
- **(c) A counterexample:** a terminal unpaid primitive Hankel leaf whose
  monic slice carries super-polynomially many members despite atom-freeness
  — this would show the descent's leaf convention must change.

## Constraints (unchanged)
Fixed sparse cutoff W = O(1); no prefix-map fiber counts (circularity guard);
the w >= 3 many-sparse inverse remains unavailable (and per your own
architecture, unneeded).
