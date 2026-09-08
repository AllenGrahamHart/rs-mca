# Bounded-flat, projective-arc and progression sources are paid

Status: PROVED source-class theorem on the unchanged normalized KoalaBear
field, row, actual carrier dimension eleven and empty universal carrier core.
There is NO curve-cover hypothesis and no unpriced off-curve set.

Every source of this consumer satisfying either condition below pays:

1. On 10000<=J<=169999, nonzero carrier evaluation vectors are pairwise
   projectively distinct and every at most eleven are independent:

       N=|Gamma|+134944<=273674135808267711,
       reserve>=1306592303127376.                    (ARC1)

2. On 23000<=J<=169999, every j-dimensional subspace of the carrier
   dual contains nonzero evaluations from at most j*h original coordinates,
   for 1<=j<=10 and some real 1<=h<=(J-1)/10:

       N<=268724670028139326,
       reserve>=6256058083255761.                    (ARC-H)

An arc with fiber sizes <=h implies the weaker condition in part 2.
In particular (ARC-H) pays the ENTIRE source whenever the actual carrier
has the full geometric-progression form in section 4. Canonical selection
may be retained, but the new supplier does not require maximality.

This is not full coverage of either J interval: the structural hypotheses
are essential. Every-carrier coverage still ends at 9940.

## 1. Stronger core bases on the same original tuple resource

Keep n=1048576+J, m=67472+J and T=500. The new required supplier has
s=11 and g=0. Its low-record tuple minimum is

    beta1=12*prod_(i=0)^10(m-1-i*h).

Indeed 12T=6000<m-10h: under either hypothesis m-10h>=67473.
The supplier proves this minimum by monotonicity of
12r*prod(m-r-i*h) through r=500, not by substituting r=500 everywhere.

For every HIGH record (raw>=501), the already proved completed weight
is >=5500. Thus its tuple count is >=5500*m*prod_(i=1)^10(67472+i).
The one tuple budget gives

    N<=max(floor((n)_falling_12/beta1), floor(F(J)/5500))+134944. (1)

No LOW-pair count, scalar-defect injection, factor description or separate
HIGH family sum is needed. F(J)<=23067643444721720934 on the whole
remaining normalized interval, so the second term plus near is at most
4194116990084347.

## 2. Unclustered projective arcs

At h=1 the first rational term is

    L1(J)=(1048576+J)_falling_12
             /[12*prod_(i=0)^10(J+67471-i)].

Its logarithmic derivative is negative on 10000..169999. Bound the
twelve positive numerator terms by 12/(1048576+10000-11), and the
eleven denominator terms from below by 11/(169999+67471).
The latter is larger, by direct positive cross multiplication.
At the lower endpoint,

    floor L1(10000)+134944=273674135808267711.

This dominates the HIGH quotient and is below the original budget
274980728111395087. Equation (1) proves (ARC1) for the whole interval.

## 3. Bounded higher-dimensional evaluation subspaces

The first quotient in (1) increases with h. Relax h to (J-1)/10,
retaining fractional factors until the final floor:

    Lh(J)=10^11*(1048576+J)_falling_12
           /[12*prod_(i=0)^10((10-i)*J+674710+i)].

All denominators are positive. This function decreases throughout
4801..169999. The numerator's logarithmic derivative is at most
12/(1048576+4801-11). Just the first FOUR denominator terms, in their
unscaled form, have slopes 1,9/10,8/10,7/10 and denominators at most
169999+67472. Their derivative sum is at least
(34/10)/(169999+67472). The exact positivity certificate is

    34*(1048576+4801-11)-120*(169999+67472)=7317924>0.

The remaining denominator derivative terms are nonnegative. Hence the
upper endpoint is not an unchecked extrapolation in J or in carrier height.

At J=23000,

    floor Lh(23000)+134944=268724670028139326.

This again dominates the HIGH quotient and gives (ARC-H).
The row theorem counts DISTINCT ORIGINAL slopes and adds near only once.

## 4. Full progression carriers satisfy the hypotheses

Suppose A,B are coprime polynomials, rho=A/B is nonconstant of degree
h=max(deg A,deg B), q is a nonzero polynomial, and

    V=q*span_F{B^10,A*B^9,...,A^10},
    deg q+10h<J.                                    (GP)

More generally (GP) may hold for V extended to ANY constant field
extension k/F, with A,B,q in k[X] and the span taken over k. Original
evaluation vectors have entries in F: their linear ranks do not change
after extending scalars, and two nonzero F-vectors proportional over k
are already proportional over F. Thus the arc/fiber conclusions proved
over k below imply the required original-field occupancy bounds.
This does NOT allow an arbitrary nonconstant function-field extension.

At a point where q!=0 the projective evaluation vector is the degree-ten
homogeneous Veronese vector of [B(x):A(x)]. Any eleven distinct such
projective points are independent: homogeneous degree-ten interpolation
on P^1, or its Vandermonde determinant including infinity, proves this
over the coefficient field in every characteristic, and hence over F
by the rank-invariance argument when k was used.

Each rho-fiber has at most h original points, using the nonzero polynomial
A-tB for finite t and B for infinity. No B-zero point is discarded.
At a point where q=0, every carrier evaluation vanishes; if an allowed
pair agrees there, the point would belong to the forbidden universal
carrier core. Thus such points are never in a minimizing pair's core.
They may still be scalar defects or nonmatching coordinates and remain
in the source, n, labels and tuple budget.

An arc with fibers <=h has at most j*h nonzero original evaluations in
each j-dimensional subspace, as proved by the supplier. This establishes
the required weaker hypothesis without asserting that (u,v)
descends to a function of rho. An arbitrary receiver can vary within
every fiber. The result pays ALL LOW and HIGH records on (GP),
not merely those on an affine-singular cubic.

## 5. Two universal restrictions on unpaid high-J carriers

For ANY unpaid source on 23000..169999, some j-dimensional subspace
of V*, 1<=j<=9, contains nonzero evaluations at at least

    floor(j*(J-1)/10)+1 original coordinates.          (HEAVY)

Indeed the proof allows real h, so use h=(J-1)/10. The dimension-ten
condition is automatic: a nonzero degree-<J polynomial annihilating
such a flat has at most J-1 distinct roots. If the first nine ranks also
satisfied their j*h bounds, condition 2 would pay the source. The earlier
integer-h formulation remains true but had an unnecessary rounding loss.
This is an actual concentration of
carrier evaluations, not an assumed flat cover. Controlling fibers alone
(j=1) would not suffice: higher ranks up to nine remain. The tiny
control already shows failure at j=2 with no repeated projective fibers.

For 23000<=J<=169999, an unpaid source cannot admit ANY constant
field extension k/F and nonconstant rho in k(X) with

    dim_k {v in V_k: rho*v in V_k} >=10.             (NO10)

Here V_k denotes scalar extension only. For the elementary carrier
classification write V for V_k in the remainder of this paragraph.
Dimension eleven would make V stable under rho; twelve successive
powers of a nonzero v would be dependent, making nonconstant rho
algebraic over k, impossible. In dimension ten, put

    H_j={v in V: rho^i*v in V for 0<=i<=j}.

The map H_(j-1)->V/H_1, v->rho^(j-1)*v modulo H_1, has kernel H_j
and target dimension one. Hence dim H_10>=1. Choose v!=0 there.
Its eleven successive powers are independent, since rho is transcendental
over k. Writing rho=A/B in primitive form, polynomiality of rho^10*v
forces v=q*B^10. Its powers form exactly the basis in (GP); their
extreme degrees give deg q+10h<J.

Thus (ARC-H) applies and contradicts the unpaid count. The elementary
classification also appears in the existing weighted-cubic supplier,
but the present conclusion needs neither a cubic nor a chosen projection.
Only constant scalars were extended; original slopes, source coordinates
and the denominator |F| never change. Constant multipliers are not excluded.
This is a proved source restriction,
not a new speculative premise required for arbitrary-source payment.

No unrestricted original-row endpoint, higher-rank theorem, LIST bound,
original-source/near/owner transport or prize closure is asserted.
