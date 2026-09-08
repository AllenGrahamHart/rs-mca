# Proof by maximum density and coupled inside counts

## 1. Actual flats and their quotient

Nonzero evaluations span V*: evaluation on n>=m>K distinct points is
injective on V. A maximum density over proper flats exists. It may be
chosen spanned by its contained evaluations, since shrinking to their
span only increases density. If its dimension is j and cardinality a,
its annihilator W in V has dimension l=11-j and vanishes on all a
coordinates. The polynomial root-space bound gives a<=K-l.

Every i-dimensional proper subspace contains at most i*h nonzero
original evaluations, by maximality. It also contains at most K-11+i
such evaluations, since its polynomial annihilator has dimension 11-i.
Greedy choice on any M-point joint-core subset proves (HYBRID).
Core evaluations are nonzero: a joint agreement at a carrier zero would
belong to the forbidden universal carrier core.

Let A be the entire nonzero fiber set of the maximizing j-flat F.
Its locator G_A divides every W-polynomial, leaving an l-dimensional
space W' of degree <K-a=l+e. On core points outside A its evaluations
are nonzero. A rank-i span in W'* contains at most e+i outside points
by the root-space bound. Its preimage in V* is a (j+i)-flat containing
ALL a points of A; maximal density bounds its outside nonzero points by
(j+i)*h-a=i*h. These statements apply for i<l, so the preimage is proper.

Thus an M-point core subset having t points in A has at least P(M-t)
ordered quotient bases outside A. All factors are positive because
M-t>=M-a>=K-a=l+e. Dividing the locator is used only for this rank
count; it does not modify the receiver, supports or original slope labels.

## 2. Count exact inside-cardinality classes

Fix the inside set of t points. Let E_b be the number of its independent
ordered b-tuples, with E_0=1 and E_1=t. For each such b-tuple let z_b
be the number of inside points in its span, and y_b=t-z_b. Exactly

    sum_(independent ordered b-tuples) y_b=E_(b+1).   (1)

Choose an ordered quotient basis outside A, and an independent ordered
b-tuple inside A. Their span has dimension l+b and intersects F in
exactly the span of that inside tuple. To obtain a full basis with exactly
b inside points, append k=j-b further OUTSIDE points.

After v such additions the span has dimension l+b+v and still contains
at least z_b inside points. The root-space bound limits its total core
occupancy by K-j+b+v. Consequently there are at least

    M-t-(K-j+b+v-z_b)=c+k-1-v-y_b

outside choices. If y_b<c, multiplying these positive bounds gives
R_k(y_b)=prod_(i=0)^(k-1)(c+i-y_b). For y_b>=c use zero, and
put R_0(y)=1. Interleave the b inside and 11-b outside ordered points
in binom(11,b) ways. Every tuple is counted at most once: its inside
positions, their order, and the first l outside positions recover the
construction. Classes with different b are disjoint.

For b=0 this gives exactly the valid lower count P(M-t)*R_j(t).
For b>=1 use the tangent bound

    R_k(y)>=A_k-D_k*y for y>=0,
    A_k=prod_(i=0)^(k-1)(c+i),
    D_k=sum_(v=0)^(k-1)prod_(i!=v)(c+i), D_0=0.     (2)

For k>=1, R_k is convex on [0,c]; it is a product of decreasing
positive factors with nonnegative second derivative. Extending it by
zero beyond c preserves convexity, since its derivative jumps upwards
there. Thus its tangent at zero proves (2). k=0 is immediate.

Using (1) and summing the disjoint b>=1 classes yields

    P(M-t)*[11*A_(j-1)*t + sum_(b=2)^j C_(j,b)*E_b],
    C_(j,b)=binom(11,b)*A_(j-b)
              -binom(11,b-1)*D_(j-b+1).            (3)

For j<=4 the remaining coefficients are nonnegative (c>=12):

    j=2:  C_2=44;
    j=3:  C_2=11*(3c-1), C_3=110;
    j=4:  C_2=11*(2c^2-c-2), C_3=55*(c-1), C_4=165.

Drop those nonnegative terms and add the disjoint b=0 count. This
proves the lower bound P(M-t)*g_j(t). Negative tangent terms were
cancelled using the EXACT extension identity (1), not discarded separately.
This is the coupling that permits inside sets of rank smaller than j.

## 3. Only three core intersections need be considered

On 0<=t<=c, g_j(t) is positive and increasing. Write R=R_j, so
R''>=0 and R'''<=0 there (the latter is zero for j<=2). At zero,

    g'_j(0)=11*A_(j-1)-D_j>=6*A_(j-1),
    g_j(0)*g''_j(0)<=12*(1+3/c)^2*A_(j-1)^2
                       <=75*A_(j-1)^2/4.

Indeed D_j<=j*A_j/c, A_j/A_(j-1)=c+j-1, j<=4 and c>=12.
Hence g_j(0)g''_j(0)-g'_j(0)^2<0. The derivative of this expression
at general t is g_j*g'''_j-g'_j*g''_j<=0, so log g_j is concave
throughout [0,c]. For t>=c, g_j is positive linear and log-concave.

P(M-t) is a product of positive affine factors in t. Its logarithm
is concave too. On each side of c the product P(M-t)*g_j(t) is
positive log-concave, and its minimum on 0<=t<=a occurs at 0, a,
or c when c<=a. This proves (FLAT), retaining the kink explicitly.

## 4. Return to the same original slope resource

For raw<=T the actual core contains at least M points. Choose any
fixed M-point subset and apply the preceding bounds. Inserting one of
the r>=1 actual defects in any of twelve positions gives at least
12*r*B, hence 12*B, independent incidence tuples. The defect is unique
relative to this record's core, so the insertion has no multiplicity loss.

Every independent tuple fixes the entire affine parameter (gamma,lambda).
Distinct selected labels own disjoint tuples. Old completed counts and
new counts on the same record may overlap; they combine by maximum.
Give every HIGH record its established m*P_d*L lower tuple count and
divide the ONE global (n-z)_falling_12 budget by the smaller LOW/HIGH
count. This proves (SOURCE), not a sum of independent family maxima.
