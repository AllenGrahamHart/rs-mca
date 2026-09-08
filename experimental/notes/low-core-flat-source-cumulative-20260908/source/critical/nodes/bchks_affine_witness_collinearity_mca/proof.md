# Proof: chosen bad witnesses and rounded Hensel bookkeeping

Notation is as in statement.md. Source symbols for the degree parameter
are reindexed to d=k-1. The sources and precise import boundary are in
provenance.md. No computation is part of this proof.

## 1. A fixed codeword line carries at most r+1 chosen bad witnesses

This elementary assertion holds for any linear code. Fix codewords c0,c1
and a set T of distinct scalars z with chosen witnesses (A_z,h_z), where
|A_z|>=n-r, h_z=c0+z*c1 agrees with u+z*v on A_z, and the received pair
has no codeword-pair explanation on A_z. Put

```text
E={x:(u(x)-c0(x),v(x)-c1(x))!=(0,0)},  e=|E|.
```

At each x in E the nonzero affine function
u(x)-c0(x)+z*(v(x)-c1(x)) has at most one scalar root.
If e>r, each z in T requires at least e-r such roots, so
|T|*(e-r)<=e and |T|<=e/(e-r)<=r+1.
If e<=r, noncontainment forces A_z to meet E, since otherwise c0,c1
explain the pair on A_z. Hence each z still requires a root in E,
giving |T|<=e<=r. In both cases |T|<=r+1.

The assertion is about witnesses already lying on a fixed codeword line.
It does not infer that all bad witnesses lie on one line from a nearby
pair, scalar over-agreement, or existence of a common core.

## 2. The interpolant works for an arbitrary selected witness set

Let S be all bad slopes of the fixed received pair. For each z in S
choose one witness A_z and its polynomial h_z of degree <=d. These
choices are retained throughout the argument, even if other scalar
explanations or other support sets exist at that slope.

BCHKS Lemma 3.1, with its stated smaller-m extension reconstructed in
exact_agreement_and_small_multiplicity.md, supplies a nonzero Q in
F[X,Y,Z] with multiplicity >=m
at (x,u(x)+Z*v(x)), for every x in D, and degree bounds

```text
deg_(1,d,0) Q < X,  deg_Y Q < Y,  deg_(0,1,1) Q < Z.
```

Here the same letters X,Y,Z also denote the real degree bounds of the
statement when used on the right of inequalities. In the rest of this
proof, polynomial indeterminates are written as Xvar,Yvar,Zvar where
ambiguity would matter.

Condition (G) is precisely a/n >= (1+1/(2m))*sqrt(rho), hence X<=m*a.
After substituting (Yvar,Zvar)=(h_z(Xvar),z), Q has at least m*a roots
counted with multiplicity and degree <X. Thus
Q(Xvar,h_z(Xvar),z)=0 identically for every selected z.
No use has been made of S being the full scalar-close set. Only the
chosen polynomial and its >=a agreements are needed by this step and
the Hensel argument below.

If |F|<=H, the result is trivial. Otherwise |F|>H throughout the rest
of the proof; this also supplies a starting point for the lifts.

## 3. Factor classes and their degree budgets

In characteristic p write

```text
Q=C(Xvar,Zvar)*product_i R_i(Xvar,Yvar^(b_i),Zvar)^(e_i),
b_i=p^(f_i),  e_i>=1,
```

with R_i irreducible and separable in its middle variable. Define

```text
d_i=deg_middle R_i,
y_i=b_i*d_i,
z_i=deg_(0,1,1) R_i(Xvar,Yvar^(b_i),Zvar).
```

Weighted degrees of nonzero products add. Therefore
sum_i y_i<Y and deg_Zvar C+sum_i z_i<Z. Multiplicities can only
strengthen these inequalities. All factors have Xvar-degree <X.

Choose x0 in F where the product of the resultants
Res_middle(R_i,partial_middle R_i) remains nonzero as a polynomial in
Zvar. This is possible: its Xvar-degree is at most
sum_i (2*d_i-1)*deg_Xvar R_i <2*X*Y<H<|F|.
Each resultant is nonzero before specialization, by separability.
The resultant condition also retains the leading coefficient in the
middle variable. It follows that the specialized factors retain their
degrees and are separable.

Write R_i(x0,Yvar,Zvar)=C_i(Zvar)*product_j H_ij(Yvar,Zvar), with
irreducible positive-middle-degree H_ij. Put

```text
h_ij=b_i*deg_middle H_ij,   w_ij=y_i*h_ij*z_i.
```

Thus sum_j h_ij=y_i, the number of (i,j) classes is <=sum_i y_i<Y,
and

```text
sum_ij w_ij=sum_i y_i^2*z_i <=Y^2*Z.                 (W)
```

At most Z scalars are exceptional because C(Xvar,z) is the zero
polynomial or some C_i(z)=0: their number is bounded by
deg_Zvar C+sum_i deg C_i <=deg_Zvar C+sum_i z_i<Z.
For each remaining z, some (i,j) satisfies

```text
R_i(Xvar,h_z(Xvar)^(b_i),z)=0,
H_ij(h_z(x0)^(b_i),z)=0.
```

Assign z to the first such class. The resulting T_ij are disjoint.
Unlike BCHKS's sharper content-free bookkeeping, z_i here bounds the
ENTIRE factor before specialization; no specialized content degree is
subtracted from the Hensel coefficient bounds.

## 4. Large classes force collinearity of the chosen explanations

Fix a class T=T_ij and write b=b_i, d0=d_i,
h0=deg_middle H_ij, z0=z_i, w=b^2*d0*h0*z0.
The following use of BCIKS's Hensel construction is load-bearing.
The companion hensel_weight_ledger.md proves the coarse numerator
estimates directly from its recurrence, retaining any deficit in the
leading-coefficient degree. The global-in-Z variable set is unchanged;
taking a subset of slopes or prescribing h_z changes no estimate.

BCIKS Appendix A and Section 5.2.6 construct the Hensel lift in the
function field of H_ij. The companion (D5) bounds bad denominators.
After removing
at most d0*h0*z0<=w bad substitutions from T, there is a subset T'
on which the lift specializes to h_z^b. The denominators are generated
by the specialized leading coefficient W and derivative numerator xi.
Their zero count is bounded by deg W+h0*Lambda(xi)<=d0*h0*z0.
All remaining substitutions are simple-root substitutions, so uniqueness
of Hensel lifting preserves the PRESELECTED h_z, not an arbitrary new
proximate.

In characteristic p the middle variable has weight b. The companion
(D3)-(D4), following the Appendix C convention, gives the regular
numerator beta_j of the j-th lift coefficient the estimate

```text
h0*Lambda(beta_j) <= (2*j+1)*d0*h0*z0 <=(2*j+1)*w.   (N)
```

The bound is strict for j>=1; the weak form includes j=0. It recovers
the coarse bounds used in Section 5.2.6 / Appendix C without assuming
that the algebraic root weight equals the leading-coefficient weight
plus b. Using full z0 and the larger w is conservative.

Suppose |T|>2*L*w. Then |T'|>(2*L-1)*w. For every integer
0<=j<L the right side of (N) is <=(2*L-1)*w. Specialization to
h_z^b shows that its coefficients vanish unless j is a multiple of b
with j<=b*d. The norm zero bound, Lemma A.1, therefore forces precisely
those other coefficients to vanish in the function field.

Here b*d<X<=L because b<=deg_Yvar Q<Y=X/d. Thus every potentially
nonzero coefficient of h_z^b lies below L. As in Appendix C, take
coefficientwise b-th roots in a purely inseparable extension to obtain
a polynomial P(Xvar) of degree <=d whose b-th power is the truncated
lift. Since the factor's (1,d,0)-degree is <X<=L, its substitution by
P has degree <L and vanishes modulo (Xvar-x0)^L. It is identically
zero. Uniqueness of the lift, followed by injectivity of the b-th power
map, gives pi_z(P)=h_z for every z in T'.

To force the coefficients of P to be affine in Zvar, the companion
evaluation estimate (D6), in the BCIKS Section 5.2.7 / Appendix C
construction, bounds the number of substitutions
where a nonzero P(x)-(u(x)+Zvar*v(x)) vanishes by

```text
(2*b*d+1)*d0*h0*z0 <=(2*d+1)*w.                    (A)
```

Indeed the root-extension weight is the original weight under inverse
Frobenius, and distinct z remain distinct under that permutation. Thus
no field-size or slope-multiplicity factor is introduced. This is why
both y_i and h_ij above retain their b_i factors.

There are at least d+1 points x with more than (2*d+1)*w agreements
among T'. The (d+1)-st largest agreement count is at least

```text
((a-d)/(n-d))*|T'|.
```

This follows by counting all >=a*|T'| agreements and allowing the top
d coordinates all |T'| agreements each. The companion
exact_agreement_and_small_multiplicity.md proves
((a-d)/(n-d))*(2*L-1)>2*d+1 for every m>=1 under the printed
gate, treating m=1 and m=2 separately. Since |T'|>(2L-1)w,
this proves the required strict load inequality. At these d+1 points (A)
forces equality in the function field. Interpolating in Xvar over F
now gives P(Xvar,Zvar)=c0(Xvar)+Zvar*c1(Xvar), with deg c_i<=d.
It specializes to the originally selected h_z for every z in T'.
Only elementary interpolation occurs here; no extension of the
original challenge field or resampling of the challenge slopes.

## 5. Sum the bad-witness classes

If |T_ij|>2*L*w_ij+r+1, Section 4 gives a codeword line carrying
at least |T_ij|-w_ij>r+1 selected bad witnesses. This contradicts
Section 1. Every class therefore has size <=2*L*w_ij+r+1.
Adding all classes and the separately charged content exceptions,

```text
|S| <= Z+2*L*sum_ij w_ij+(r+1)*(number of classes)
     <= Z+2*L*Y^2*Z+(r+1)*Y = H.
```

Since |S| is an integer, |S|<=floor(H). The argument is uniform in
the received pair, so taking its maximum proves (M).

Using L=ceil(X) explicitly avoids applying 2*j+1<=2*X-1 to the
largest integer j<X when X is nonintegral. Paying +Z avoids any
dependence on the sharper specialized-content saving. Neither
precaution alters the linear-in-n order at fixed rho and m.

The exact-agreement continuation changes only interpolant eligibility
and the verified coordinate-load inequality. The full-degree class
weights, content charge, Frobenius factors and preserved-witness
specializations above are unchanged.
