# Proof

## 1. Retain Both Bounds At Every Completion Step

The required maximum-density theorem gives the actual quotient W, with
nonzero evaluations outside the COMPLETE A. It also gives the exact
independent inside-extension identity sum_B y_B=E_(b+1).

Choose an ordered quotient basis of ell outside points and an independent
ordered b-tuple inside A. Their span has rank ell+b and meets F in the
span of the inside tuple. Append k=j-b additional OUTSIDE points.
After v additions, the span has rank s-k+v<s. It contains at most

    min(K-k+v, (s-k+v)*h)

nonzero domain evaluations: both the polynomial root-space and maximum
density bounds apply. If z_B=t-y_B inside points were already in the
initial span, at least z_B still are. Thus the number of outside choices
is at least

    M-t-min(K-k+v,(s-k+v)*h)+z_B
       =max(c+k-1-v,M-(s-k+v)*h)-y_B.

Reverse i=k-1-v. These are exactly the factors d_i-y_B in R_k.
All are positive since y_B<=t<=a<c. The usual binom(s,b) interleavings
are injective: positions recover the inside tuple and the first ell outside
points recover the quotient basis. Different b give disjoint classes.
The same bound applies to EVERY quotient basis, so their actual number
can be replaced by ANY lower Q_out. This proves COUNT.

## 2. Couple Before Eliminating Signed Terms

Each R_k is a product of positive decreasing affine factors on [0,c).
Its second derivative is nonnegative, including the linear/constant cases.
The tangent at q_b gives R_k(y)>=L_k(q_b)-D_k(q_b)*y.
Multiply by the binomial coefficient and sum over actual inside tuples.
Use sum_B y_B=E_(b+1). The exact telescoping coefficients are C_b;
the b=0 contribution remains R_j(t). The final derivative D_0 is zero.

For every ordered independent b-tuple, its span contains at most b*h
inside points and at least b distinct inside points. Therefore

    max(t-b*h,0)*E_b <= E_(b+1) <= max(t-b,0)*E_b.

If E_b=0, then E_(b+1)=0 too, so no division by a zero count is used.
Eliminate E_j,...,E_2 backwards. A nonnegative tail coefficient uses the
lower ratio; a negative one uses the upper ratio. Since E_1=t, this proves
the printed backward bound. The product lower bound on E_b follows from
the same left inequality; R_k(y_B)>=R_k(t-b) when E_b is nonzero gives
the separate positive-class bound. When E_b=0 its lower product is zero.

## 3. Boxes And Complete-Core Use

Replacing d_i by smaller d_i^0 preserves the factorwise lower bound,
because all d_i^0-y remain positive. Use fixed calibrations in this smaller
polynomial, then the exact extension identity as before. The actual ratios
are bounded by max(t0-b*h1,0) and max(t1-b,0). The last signed multiple
of E_1 uses t0 or t1 in its correct direction; b=0 uses t1. This proves BOX.

These are real relaxations of actual integer tuple counts. They neither
assert fractional-degree sources nor independent realizability of chosen
ratio endpoints. A negative BOX value is not a positive basis lower bound;
the direct b=0 class remains available. Any multiplication of lower bounds
must respect this sign.

For the selected dimension-eleven MCA source, the required complete-core
lemma chooses M core points containing ALL t flat points while retaining
the old witness's defect. Each resulting basis inserts that defect in
twelve recoverable positions. Original independent incidence tuples are
disjoint across distinct finite labels. Quotient contraction here is an
auxiliary basis count, not a puncture of the received word or a new source
normalization. This completes the stated MCA interface.

## Provenance

This strengthens the already proved maximum-density inside-class count.
The new features are retaining density in the supplementary OUTSIDE
extensions, allowing any proved quotient-basis bound, and eliminating
signed coefficients through coupled actual tuple ratios. The source,
interleaving and complete-core/defect mechanisms are credited prerequisites.
