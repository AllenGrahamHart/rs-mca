# proof: hankel_rank_profile_entropy
Pro rounds 7-8 (refereed; the literal round-7 principal-kernel statement was
FALSE — boundary factor at infinity, falsification #19, counterexample
S = e_{t+j-1}; the CORRECTED torus form is proved referee-grade and verified
5086/5086 row-deficient cases incl. 2966 with alpha > 0):

(1) PRINCIPAL KERNEL (corrected): rank M < t forces P = q K[X]_{<=D-1},
deg q = (j+1-D) - alpha, alpha = root-at-infinity multiplicity; X^alpha P =
qtilde K[X]_{<=D-1}, deg qtilde = j+1-D. X^alpha is invertible on mu_n, so
the zero-support matroid on H is the degree-(j+1-D) principal GRS segment.
Proof: divided-power apolarity (char p > t+j kills the divided/ordinary
mismatch — stated explicitly); Mf = 0 iff Phi_f o F = 0; binary apolar ideal
= complete intersection (Q,R), deg sum t+j+1 (Sylvester); row-fullness iff
a >= t via dim (I_F)_j = (j-a+1)_+ + (j-b+1)_+; deficiency forces a < t,
b > j+1, so (I_F)_j = Q K[A,B]_{j-a}; dehomogenize with Q = A^alpha Q_0.
Edge cases t=0,1, D=j+1, zero window handled. After root strip: GRS/MDS,
no unpaid entropy.
(2) ROW-FULL WIDE (j-t+3 > 2W): separation + same-class collapse (the
rational-defects node) give Delta_u <= 1.
(3) ROW-FULL NARROW: dim P = j+1-t <= 2W-2; each branch drops dim; <= O(W)
branching levels of width <= n^W.
TOTAL (entropy/Kraft + QF.12 budget chains): unpaid primitive saturated
states <= n^{O(W^2)}, fixed cutoff W. Verifier:
notes/verify_rank_profile_lemmas.py + verify_corrected_lemma_and_pinned.py.
