# Scalar lists in an algebraic coefficient family

This companion proves the geometric input, including its degree cost.
Work over an algebraic closure k of F. An affine coefficient variety is
embedded in an affine space of polynomials of degree <K. Its degree
means the degree of its projective closure in these coefficient coordinates.
For a pure-dimensional reduced union, degrees add over its components.

## 1. The hypersurface degree fact used here

For an irreducible affine variety Z of dimension v>=1 and degree Delta,
a nonzero polynomial of degree at most e on Z either has empty zero set
or cuts a pure-dimensional variety of dimension v-1 whose component
degrees sum to at most e*Delta. Apply the projective statement to the
closure and the homogenized equation, then discard multiplicities and
components at infinity. Nonzero constants give empty intersections.
The projective statement follows from multiplication by a nonzerodivisor:
the Hilbert polynomial changes from P(t) to P(t)-P(t-e), whose leading
coefficient gives degree e*Delta. See
[Vakil, Bezout Exercise 1.8, PDF page 84](https://math.stanford.edu/~vakil/0506-216/216Bjun2807.pdf#page=84).

All later cuts are applied componentwise to reduced varieties and do NOT
assume that a hypersurface containing a component lowers its dimension.

## 2. Degree-weighted LIST incidence

Let Z be irreducible of dimension v and degree Delta. For an arbitrary
received scalar word on n distinct points and K<=A<=n, put

    Q=(n-K+1)/(A-K+1) >=1.

Then the number of polynomial points of Z with at least A agreements
is at most Delta*Q^v. This even counts points over k, so also bounds
the original F-points. For v=0 the number of points is at most Delta.

For v>0 let g be the number of domain points at which agreement with
the received word holds identically on Z. Two distinct polynomial points
of Z have degree-<K difference, so g<=K-1. Every counted polynomial
therefore satisfies at least A-g nonidentical agreement equations.
Each such equation is an affine hyperplane in coefficient space. Empty
sections cost zero; other sections have dimension v-1 and sum of
component degrees <=Delta. Induction bounds their lists by
Delta*Q^(v-1). Counting incidences gives

    (A-g)*M <= (n-g)*Delta*Q^(v-1).

Since (n-g)/(A-g)<=Q for 0<=g<=K-1, the assertion follows.
For a reduced union, sum over its irreducible components; repeated list
points are only overcounted. Universal agreement coordinates are charged
explicitly and never treated as proper hyperplane sections.

## 3. Cover a bounded-dimensional polynomial locus

Let X in affine s-space be the common zero set of finitely many
polynomials of degree <=e, with e>=1, and suppose dim X<=r<=s. Then X is
contained in a pure r-dimensional reduced algebraic set Z of degree
at most e^(s-r), unless X is empty, which is harmless.

Start with affine s-space. While the current pure dimension v exceeds
r, none of its irreducible components can be contained in X. Thus, for
each component, some defining polynomial of X is nonzero on it. Over
the infinite field k choose a linear combination nonzero on all the
finitely many current components. Its zero set still contains X.
Section 1 lowers the dimension by one and multiplies the sum of degrees
by at most e. Reduce the result before the next step. After s-r
steps the dimension is r and the degree is at most e^(s-r).

This is an existence argument over k, not a finite-field genericity
assumption or a demand to compute a Groebner basis. It does not bound the
number of equations in terms of K. Combining this cover with section 2
gives the scalar list bound e^(s-r)*Q^r for points in X. The earlier
quadratic theorem uses e=2 exactly as before.

## 4. Joint polynomial-pair version

Section 2 holds verbatim for an affine variety of polynomial PAIRS,
each component of degree <K, when agreement means both components
agree at the coordinate. Its degree is in the original pair coefficient
space. For an irreducible positive-dimensional component let g count
universally agreeing JOINT coordinates. Two distinct pairs differ by
a nonzero polynomial of degree <K in at least one component, so
g<=K-1. At a nonuniversal coordinate, its joint section is empty or
contained in a proper agreement hyperplane for one component. That
hyperplane section has dimension v-1 and total degree <=Delta.
Induction bounds its jointly agreeing list by Delta*Q^(v-1).

Counting joint incidences gives (A-g)M<=(n-g)Delta*Q^(v-1), and
(n-g)/(A-g)<=Q finishes the same bound Delta*Q^v. At dimension
zero there are at most Delta points; sum over reduced components.
One never multiplies unrelated scalar list sizes or assumes both
hyperplanes separately lower dimension. This extracts the proved
joint argument from the affine-product-level child so that other
coefficient-family consumers can use it without a dependency cycle.
