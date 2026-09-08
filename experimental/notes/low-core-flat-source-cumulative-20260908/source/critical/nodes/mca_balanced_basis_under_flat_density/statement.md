# Balanced Polynomial Basis Product Under A Flat-Density Bound

Status: PROVED by the hand argument; external independent review remains due.

Let V be an actual s-dimensional polynomial space of degree <K, 2<=s<=K,
on N=D+K distinct points, D>=1. Assume every evaluation is nonzero.
Suppose every proper positive-dimensional subspace F of V* contains at
most h*dim(F) of these evaluations, counting coordinates with multiplicity.
Write c_s=floor(s^2/4). If

    c_s*h <= N,                                             (DENSITY)

the number of independent ORDERED s-tuples of evaluations satisfies

    B_s(V) >= product_(i=0)^(s-1)(D+K-i*(K-1)/(s-1)).       (PRODUCT)

The density bound concerns every proper flat, not just projective fibers.
It is a sufficient condition, not asserted necessary. No K<=D or smoothness
assumption is required. The proof contracts complete flats, retains their
actual degree loss and uses a joint fiber second moment at every descendant.

For the MCA incidence interface, a raw<=T record on an empty-universal-core
source has at least M=m-T nonzero joint-core evaluations. A density bound
on the full source also bounds every chosen M-point core subset. If
c_s*h<=M, (PRODUCT) at D=M-K gives a valid core-basis lower count; one
actual defect gives (s+1) times as many independent incidence tuples.
There is no source normalization, near add-back or row closure in this node.

The unqualified product is FALSE: the existing large-fiber construction
with s=11,K=25000,D=67466 has strictly fewer bases than (PRODUCT).
This is a counterexample to dropping (DENSITY), not an unsafe MCA line.
