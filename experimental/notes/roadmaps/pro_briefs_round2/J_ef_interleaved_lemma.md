# proof: F-valued word source => e-interleaved base-list witness (Pro; verified)

Refines the naive "F-valued => ordinary base-list witness" (which is FALSE: the
proved extension-line counterexample f(x)=x^a/(x-alpha) has denominator X-alpha
genuinely extension-valued, not a B-line with reinterpreted slopes).

CLAIM. Let B <= E, [E:B] = e, D subset B, {omega_i} a B-basis of E. Let C be a
reduced horizontal component of X_E whose generic point is an E-valued line
f + z g (f,g : D -> E) with locator ell_T and Hankel noncontainment
H_{t,j}(Syn_E(g)) ell_T != 0. Expand f = sum f_i omega_i, g = sum g_i omega_i
(f_i,g_i : D -> B), M_z = the B-linear mult-by-z matrix on E. Then the generic
point satisfies the e-INTERLEAVED base equation
    H_B( Syn_B(Phi(f)) + M_z Syn_B(Phi(g)) ) ell_T = 0
with interleaved noncontainment.

PROOF. Because D subset B, all eval points x, powers x^m, and dual weights
lambda_x lie in B, so syndrome formation commutes with the B-basis expansion:
Syn_E(sum y_i omega_i) = sum Syn_B(y_i) omega_i (B-linearity). Multiplication by
z in E is B-linear = M_z. Hence the E-equation (H(u)+zH(v))ell = 0 decomposes
coordinate-by-coordinate into the interleaved B-equation; noncontainment is
preserved since an E-vector is 0 iff its B-coordinate vector is 0. The
expansion E^D ~ (B^D)^e is a B-linear isomorphism preserving reduced generic
points, so C lies in the interleaved witness locus; trivial stabilizer +
non-tower makes it genuinely full-field. QED.

VERIFIED (verify_interleaved.py): over B=F_101, E=F_101^2, (1) syndrome commutes
with B-basis expansion, (2) mult-by-z equals M_z, (3) noncontainment preserved.
