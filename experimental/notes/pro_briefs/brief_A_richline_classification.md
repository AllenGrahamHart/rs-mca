# Pro brief A: the rich-line classification (no fifth class)

SETTING. RS code over F_q, evaluation domain mu_n (n = 2^s | q-1, char p >= n^2,
prize scale n = 2^41, q ~ 2^256; toy rows F_193 etc. for intuition). Fix a
near-k agreement subcore: k-1 evaluation points held in common. Each additional
off-core point x defines a LINE in the (z, a) parameter plane (z = slope
parameter of the residual pencil through the subcore, a = intercept; the
normalization is in the attached P3 note). A line is (t+1)-RICH if it contains
t+1 or more of the off-core points' lines' intersections (t = the nullity
parameter, 3..5 at the relevant rows).

GRANTED (proved, attached):
1. The toral-symmetry classification (tame Laurent-Ritt): the only toral
   symmetries of G_m available are x -> x^m (cyclic) and x -> x^m + alpha
   x^-m (dihedral). [attach: the Laurent-Ritt packet]
2. Three symmetry-derived families produce rich lines: tangent pencils,
   quotient-with-tails (cyclic pullbacks), dihedral. [same packet + P3 note]
3. PROVED P3 verdict: these three do NOT exhaust — MULTI-DIRECTION AFFINE
   NETS occur as a genuine fourth class (14 exhaustive cases over F_193).
   [attach: p3 note]
4. Evidence (not proof): after stripping all four classes, residual rich
   lines number <= 5 at every toy row scanned (E33).

ASK. Prove: every (t+1)-rich line through a near-k subcore lies in
{tangent pencil, quotient-with-tails, dihedral, affine-net} — NO FIFTH
CLASS — and the post-strip residue is bounded by an absolute constant C
uniformly over rows. OR construct a fifth class (equally valuable; it
would falsify our p1 cap route). Route hint: the four classes appear to
correspond to the stabilizer types of line configurations in the (z,a)
plane under the affine + toral actions; a stabilizer classification may
be the clean proof.

Attach: nodes/p1_post_paid_subcore_richline_cap/proof.md (the gap-flagged
argument), the P3/affine-net note, the Laurent-Ritt packet.
