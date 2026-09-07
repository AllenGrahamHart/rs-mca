# Proof

## 1. Full ordinary Johnson bound

For ell distinct degree-<L polynomials, choose exactly A=w+L agreeing
coordinates per polynomial. Distinct supports intersect in at most L-1
points. If c_x are incidence counts, then sum c_x=ell A and

    ell^2 A^2/N - ell A <= sum c_x(c_x-1)
                         <= ell(ell-1)(L-1).

For ell>0, division and the positive denominator give ell<=J_L.
This proof uses exact chosen supports, so no monotonicity condition on
an untruncated agreement count is needed. Since A<=N, J_L>=1.

## 2. Same-field padding

For K<L, choose L-K new evaluation points G. The field gate supplies
them. On the old domain multiply the receiver and every listed polynomial
by P_G=prod_(g in G)(X-g); set the new receiver equal to zero on G.
The injective polynomial map h -> P_G h preserves affine dimension and
adds L-K agreements. This maps every original list into a full-code
list on (r+L,L,w+L). Thus J_L pays all K<=L, without changing field.

## 3. Common-zero removal and scalar anchoring

Write a nonempty list's carrier as h_*+V. If V has dimension zero,
there is at most one word. Otherwise, if x is a common evaluation zero
of V, subtract h_* from receiver and list words, delete x and divide
by X-x. The polynomial map on V is injective and drops the ambient
degree bound by one. At most one agreeing coordinate is lost for each
word, regardless of whether the common value agrees with the receiver.
Hence the new row is (r+K-1,K-1,w+K-1), with unchanged affine dimension,
and NO word is discarded. The nonzero V ensures K>=2 here.

When V has no common zero, at each anchor x the listed polynomials
agreeing with the receiver there lie in an affine hyperplane of V.
Subtract one of these polynomials and divide by X-x on the remaining
domain. This injects the anchored list into a dimension-at-most-(s-1)
list on the same (r,w) corridor, so its size is at most U. Counting
agreement incidences gives ell(w+K)<=(r+K)U.
At K=1 the anchored polynomial space has degree bound zero and contains
only its zero word, also covered by U>=1.

Induct on K. For K<=L use padding. For K>L, common-zero removal uses
the same claimed cap at K-1, whereas the zero-free branch is bounded by
floor((r+L+1)U/(w+L+1)), because (r+K)/(w+K) decreases in K.
Both branches are at least one. This proves (P).

For (S), first use U when the actual affine dimension is <=s-1.
Otherwise it is s. Remove all common zeros without loss; the remaining
degree bound is at least s by polynomial-space dimension. Scalar anchoring
then gives the ratio at K>=s, at most (r+s)/(w+s). This ratio is >=1,
so its floored product with U also covers the lower-dimensional branch.

The proofs are uniform in receiver, domain and affine carrier. Successive
applications therefore have the quantifiers required by the recurrence.
