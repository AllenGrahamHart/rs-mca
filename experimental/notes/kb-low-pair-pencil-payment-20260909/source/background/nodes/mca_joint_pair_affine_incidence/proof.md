# Joint Affine Incidence And A Determinant Guard

## 1. The Credited Affine LIST Bound

The joint-pair extension in the required supplier's
algebraic_list_bound.md section 4 gives (AFF) for an affine variety of
degree one. Here is its elementary affine proof, including universal
agreement coordinates.

Dimension zero has at most one pair. For r>0, let g count coordinates
where the entire affine family equals the received pair. Two distinct
members differ in at least one nonzero polynomial of degree<K, hence
g<=K-1. At any other coordinate, the joint agreement section is empty
or lies in a proper affine hyperplane of the family. Induction bounds
its A-agreeing pairs by Q^(r-1). Therefore

    (A-g)M <= (n-g)Q^(r-1) <= (A-g)Q^r.

The last step uses 0<=g<=K-1 and A<=n. When the exact section has
smaller dimension, Q>=1 justifies the same upper bound. All these counts
are finite even if F is infinite: any K agreeing coordinates determine
the pair, and there are only finitely many such coordinate sets.

The same statement for a scalar affine family follows by embedding each
polynomial H as (H,0), with receiver (w,0). No product of independent
scalar lists is taken.

## 2. Count Only Rank-Two Anchors

At every x outside E the linear map W -> F^2 is surjective. Its joint
agreement fiber in f_*+W is either empty or an affine space of dimension
r-2. Count only members of that fiber which retain at least A joint
agreements on the ORIGINAL D. Section 1 bounds their number by Q^(r-2).

Every globally counted pair agrees at at least A-e good coordinates.
Double-counting the pair/good-coordinate incidences gives

    (A-e)M <= (n-e)Q^(r-2).

This proves (TWO). Removing E was only a restriction of the anchor count:
no polynomial degree, original domain, agreement threshold or downstream
MCA source was punctured. The A-e denominator is essential.

## 3. A Polynomial Determinant Supplies The Bad Set

Function-field rank two means some w_1=(a_1,b_1), w_2=(a_2,b_2) in W
have nonzero determinant a_1*b_2-a_2*b_1. Its degree is at most 2K-2.
Take E to be its roots in D. Outside E the two evaluated vectors are
independent, so joint evaluation of the entire W has rank two.

Now e<=2K-2<A. The function (n-e)/(A-e) is nondecreasing in e:
its derivative is (n-A)/(A-e)^2>=0. Relax e to 2K-2 in (TWO) to
obtain (DET). This is only a sufficient degree gate; (TWO) may still
apply with a smaller actual bad set when that coarse gate fails.

If W has function-field rank one, every such determinant is zero and
there is no rank-two anchor set of the asserted kind. A separate rational
pencil/ownership argument is necessary. The explicit controls distinguish
this case from an affine-dimension claim over F.
