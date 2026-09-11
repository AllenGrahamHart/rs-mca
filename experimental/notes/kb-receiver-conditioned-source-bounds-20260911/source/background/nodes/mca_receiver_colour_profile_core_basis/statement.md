# Trim The Actual Receiver-Colour Profile To The Required Core Mass

Status: PROVED locally; external mathematical review remains due.

Fix a degree-<K polynomial space V of dimension s>=2, an affine
carrier h_*+V, a received pair(u,v), and a domain of distinct points.
Assume its literal universal carrier core is empty. On each nonzero
projective evaluation fibre ev_x=lambda_x*ell, partition by the colour
((u-h_*)/lambda_x,v/lambda_x), and write ALL class sizes as w_i.

Let M>=K and D=M-K. Let F(k)>=0 be any PROVED nondecreasing
ordered-basis lower bound for every rank-(s-1), degree-<k space on
D+k distinct points with nonzero evaluations, for s-1<=k<=K.

Define the profile lower cost

    Phi_M(w)=min sum_i x_i*F(K-w_i),
    0<=x_i<=w_i, sum_i x_i=M.                         (TRIM)

All w_i<=K-s+1 by the polynomial root-space bound. If sum w_i<M,
no complete joint core of size>=M exists. Otherwise(TRIM) is well
defined and is evaluated by filling the LARGEST classes first, taking
only the required mass from the last class.

For EVERY pair in(h_*+V) x V whose COMPLETE joint core H has
at least M points,

    number of ordered s-bases in H >=Phi_M(w).

This strengthens M*F(K-max w_i), without assuming that arbitrary class
profiles or the minimizing allocation are realizable as a polynomial core.

## Sparse Heavy-Class Corollary

For integers1<=c<=E<=K-s+1, if the TOTAL COORDINATE MASS of
classes larger than c is at most E, then

    Phi_M(w)>=(M-E)*F(K-c)+E*F(K-E).                  (TAIL)

E counts coordinates, not classes or fibres. The full profile bound
has no sparsity premise. F is a supplied proved basis bound; this
lemma introduces no conjectural child estimate or source payment.
