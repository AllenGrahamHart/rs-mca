# Cancel Only The Auxiliary Universal Core, Then Insert Every Defect

## 1. Retain The Original Labels And Chosen Pairs

Translate the received functions by a0,b0. The pair differences
a_gamma-a0,b_gamma-b0 belong to U, and the selected explanation becomes

    h'_gamma=(a_gamma-a0)+gamma*(b_gamma-b0) in U.

The scalar agreement equation remains exact with the SAME gamma. A
coordinate is a joint core point on S_gamma if and only if v=b_gamma:
the scalar equation then gives u=a_gamma. Thus each support contains
m-tau_gamma joint core points and tau_gamma genuine defects.

Every member of U vanishes on Z, so is divisible by
G_Z=product_(x in Z)(X-x). The space of degree-<K multiples of G_Z
has dimension max(0,K-z); since it contains the s-dimensional U,
z<=K-s. Divide U and both translated pair components by G_Z, and
divide the translated received values on D'=D\Z by its nonzero values.
The resulting U'=U/G_Z has dimension s and degree bound K'=K-z.

No original defect lies in Z: there both received coordinates equal
every translated pair's zero values. After deleting Z from a selected
support there remain at least m-tau_gamma-z joint points and ALL its
tau_gamma defects. Choose ANY L=m-z-T of these joint points, since
tau_gamma<=T. This does not presume that S_gamma contained Z, nor
reselect or reclassify an original source. No auxiliary minimizer is used.

On each remaining joint point the evaluation of U' is nonzero. Otherwise
both divided pair components vanish there, as do both divided receiver
coordinates; before division that point would have belonged to Z.

## 2. A Uniform Number Of Ordered Core Bases

On these L>=K'>=s joint points, the first evaluation vector can be
chosen in L ways. Suppose i independent evaluations have been chosen,
where1<=i<s. Their i-dimensional span is annihilated by a polynomial
subspace of U' of dimension s-i. If b coordinates have their evaluations
in that span, every member of this subspace vanishes on those coordinates.
Root-product divisibility gives s-i<=K'-b, hence b<=K'-s+i.

Consequently at least L-K'+s-i=d-T+s-i evaluations extend the basis.
Multiplying these lower bounds proves that the ordered independent
s-tuples among the chosen core points number at least

    B=L*product_(j=1)^(s-1)(d-T+j)=L*P.

All factors are positive. Common zeros outside the chosen core cause no
problem: the root-product bound includes them, and the first vector is
nonzero by section1. This also proves the basis assertion for s=1.

## 3. Independent Incidence Tuples Have Unique Labels

Fix a basis phi_1,...,phi_s of U'. In the divided scalar equations the
unknowns are gamma and the coefficients c of h'_gamma/G_Z:

    gamma*v'(x)-sum_j c_j*phi_j(x)=-u'(x).

On core points v' equals the chosen b'_gamma in U'. Subtracting its
coefficient combination from the v' column makes that column zero on
any chosen core basis. At EACH original defect it is nonzero. Inserting
that defect in any of s+1 positions of an ordered core basis therefore
gives an independent (s+1)-tuple of incidence equations.

Within one record these tuples are distinct: the unique selected defect
recovers its coordinate and insertion position, and deleting it recovers
the ordered core basis. Across different records an independent tuple
can belong to at most one label, since it uniquely determines gamma
and c. This is the credited raw-margin proof's weighted insertion
mechanism, applied directly to the divided LOW family; no HIGH-funding
or full-code-badness hypothesis is imported for that auxiliary family.

There are at most(n')_falling_(s+1) ordered tuples of distinct coordinates.
The disjoint ownership just proved gives

    (s+1)*L*P*sum_gamma tau_gamma <= (n')_falling_(s+1).

The left mass is an integer, proving(LOW). The count concerns one fixed
original-label family, not separately normalized sources or a sum over Z.
