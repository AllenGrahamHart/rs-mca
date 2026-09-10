# Keep The Moving Carriers On One Quadratic Incidence System

## 1. Resolve The Three Coefficient Conditions

Let U=ker ell1 intersect ker ell2, of dimension s-2. Choose v1,v2 in V
with ell_i(v_j)=1 if i=j and0 otherwise. Condition(CHAIN) gives

    a'=alpha+t*v2, b'=beta+t*v1, alpha,beta in U.

After the FIXED receiver translation u'=u-a0,v'=v-b0, each original
label has explanation

    h'=alpha+gamma*beta+t*(v2+gamma*v1) in U_gamma,
    U_gamma=U+span(v2+gamma*v1), dim U_gamma=s-1.

The sum is direct since ell2(v2+gamma*v1)=1. Scalar agreements,
original labels and chosen defects are unchanged. No received word is
divided by a polynomial or normalized differently for different gamma.

## 2. Price The Moving Zero Evaluations By Labels

The common zeros on the domain of U number at most K-(s-2)=K-s+2,
by root-product divisibility of its s-2-dimensional polynomial space.
At any selected joint-core point x, evaluation on V is nonzero by
hypothesis. If evaluation on U_gamma is zero there, U(x)=0 and
v2(x)+gamma*v1(x)=0, while v1(x),v2(x) are not both zero.
Thus v1(x) is nonzero and x specifies the UNIQUE label
gamma=-v2(x)/v1(x).

Delete from this LOW count every label with such a zero on its selected
joint core. There are at most K-s+2 labels, not one exception per pair.
Their eventual deficit is at most T each. All coordinates remain in the
common tuple domain, and all original records remain in any original
all-record resource used later by the consumer.

## 3. Generate Many Tuples For Every Retained Label

Choose L=m-T joint-core points from its m-tau_gamma available points.
Evaluation on U_gamma is nonzero on them. The required weighted-carrier
proof's root-flat/greedy argument, here with carrier dimension s-1,
gives at least

    B=L*product_(j=1)^(s-2)(d-T+j)

ordered independent core bases. This is a basis count on each carrier,
not an application of that supplier's fixed-carrier GLOBAL resource.
All factors are positive because d>=T and L>=K>=s.

Fix a basis phi_1,...,phi_(s-2) of U. Introduce ambient variables
(z,c_1,...,c_(s-2),t,w), a total of s+1 variables. Scalar incidence
on an original coordinate x is the FIXED linear equation

    z*v'(x)-sum c_j*phi_j(x)-t*v2(x)-w*v1(x)=-u'(x).

The parameter cone is w=z*t. At the chosen record its point has
z=gamma,c=alpha+gamma*beta and w=gamma*t. Restricting the incidence
equations to coordinates(z,c,t) on this cone gives a square Jacobian
on any ordered s-tuple of coordinates. Its z-column is v'-t*v1.
Subtract the appropriate U-column combination to make it v'-b'.
This column is zero on a joint-core basis and nonzero at ANY defect.
The other s-1 columns are evaluations on U_gamma. Thus inserting
each original defect at any of s positions of any independent core
basis gives an INVERTIBLE Jacobian at this record's point.

For a fixed record these are tau_gamma*s*B distinct ordered tuples:
the unique selected defect and its position recover the core basis.
The argument does not rely on characteristic zero or a generic position.

## 4. Each Common Tuple Has At Most Two Owners

For any generated s-tuple, its s fixed linear incidence equations have
rank s: their restriction just had an invertible s-by-s Jacobian.
Their affine solution space in the s+1 ambient variables is a line.
The polynomial w-z*t restricts to degree at most two on that line.

This restriction is NOT identically zero. Indeed, if the line were
contained in the cone, its nonzero direction(delta z,delta c,delta t,
delta w) at a chosen owner would satisfy

    delta w=t*delta z+gamma*delta t.

It would then be the image of a nonzero vector(delta z,delta c,delta t)
under the cone parametrization's differential, annihilated by the s
incidence equations. This contradicts the invertible Jacobian above.
This elementary calculation remains valid in every characteristic.

A nonzero polynomial of degree at most two on an affine line has at
most two field-valued zeros. Hence at most two selected record points,
and at most two original labels, can own this tuple. Every original
label has only its one fixed explanation; no point-to-label multiplicity
is added. A tuple may really have two owners, as the focused fixture shows.

There are(n)_s possible ordered tuples of distinct original coordinates.
Therefore s*B*sum_retained tau_gamma<=2*(n)_s, proving(TWO).
Finally T+1-tau<=T*tau for every retained tau>=1; every exceptional
label costs at most T. This proves the stated whole-LOW deficit bound.
The proof never sums budgets of individually normalized moving carriers.
