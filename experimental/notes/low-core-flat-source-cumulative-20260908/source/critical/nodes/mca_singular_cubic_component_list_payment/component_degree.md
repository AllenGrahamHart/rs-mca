# Count all top-dimensional components in original coefficient degree

Let Y_i be a positive-dimensional irreducible component of the original
coefficient locus, with dimension r. Recover its normalization parameter
sigma away from the singular pair, and take its closure Z_i in the
fixed finite-dimensional rational-function parameter space supplied by
the weighted theorem. The coefficientwise cubic normalization map gives
an everywhere-defined projective morphism on that parameter space:

    [z:h] -> [z^3 : f_s*z^3
              +(h^2-lambda*z^2)*(P*z+Q*h)].             (1)

Here h denotes the rational-function parameter vector, NOT the primitive
projection height. All output coordinates are taken in a finite-dimensional
rational-function space containing the displayed expressions. The original
polynomial affine carrier embeds as a linear projective subspace of it.

There are no basepoints: if z!=0 the first coordinate is nonzero; if
z=0 the output Q*h^3 is a nonzero rational-function pair whenever h is
nonzero. The morphism has finite fibers. In the affine chart (1) is
birational away from f_s, whose inverse fiber has at most two parameters.
At infinity, proportional pairs Q*h_1^3 and Q*h_2^3 imply h_1/h_2
is constant, so [h_1]=[h_2]. Properness and finite fibers give finiteness.

Its restriction to the projective closure of Z_i has image the projective
closure of Y_i. It is generically degree one, not merely injective on
geometric points: in the basis P,Q the affine formula recovers sigma as
the ratio of the Q and P coefficients of f-f_s. Recovering its coordinates
in the fixed rational-function space is linear algebra over the rational
function field of Y_i, so this is a rational coefficientwise inverse.

The pullback of O(1) is O(3). The finite-map degree formula therefore gives

    deg(Y_i)=3^r*deg(Z_i)>=3^r.                         (2)

See [Stacks, Lemma 33.45.11](https://stacks.math.columbia.edu/tag/0BEX).
Equivalently, pull back r general hyperplanes. They give a proper
intersection of r cubic hypersurfaces on the projective parameter closure,
of degree 3^r*deg(Z_i), with generic mapping degree one. Degrees are
measured in the ORIGINAL pair coefficient embedding, whose linear
inclusion does not change degree. An arbitrary high-dimensional parameter
ambient space introduces no new component-count factor in (2).

## Apply the nonpure degree budget

The original pair coefficient locus is defined by equations of degree <=3
in 22 affine coordinates, after clearing fixed X-denominators. The required
weighted supplier's general nonpure degree lemma, used here with e=3,
gives

    sum_i deg(Y_i)*3^(dim Y_i)<=3^22.                   (3)

In the d=7 case every component has dimension at most three. Each
three-dimensional component contributes at least 3^3*3^3=3^6 to (3).
Their total number is at most

    3^16=43046721.                                    (4)

These are all geometric components, not just components with visible
original-field points. No component or rational-normalization branch is
identified for free with another one. Intersections may be overcounted
in the later upper bound, which is harmless.
