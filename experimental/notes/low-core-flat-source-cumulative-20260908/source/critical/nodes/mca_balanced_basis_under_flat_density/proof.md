# Proof By A Hereditary Joint Second-Moment Bound

We use the exact full-fiber locator contraction from the required supplier.
Its earlier large-fiber construction is also the antecedent of the guard
counterexample below. The new ingredient is a sufficient density condition
that propagates the balanced second moment to EVERY contracted source.

## 1. A Capped Fiber Moment

Consider any nonzero polynomial evaluation space of rank r>=2, degree <k
and length n=D+k. Order its projective fiber sizes a_i decreasingly.
Any r-1 fibers lie in a proper subspace. A nonzero annihilating polynomial
gives sum_(i=1)^(r-1) a_i<=k-1. Let b=a_(r-1), m=r-1, and suppose
every fiber is at most n/m. Tail sizes are at most b, so

    sum_i a_i^2 <= b*n + sum_(i=1)^m a_i*(a_i-b)
                <= b*n + (n/m)*((k-1)-m*b)
                 = n*(k-1)/(r-1).                         (MOMENT)

There are at least r fibers, since the evaluations span the dual. All
excesses in the second inequality are nonnegative. This argument retains
the joint top-fiber constraint rather than independently maximizing sizes.

## 2. Density Gives This Moment At Every Descendant

Fix any complete original flat F of rank j<=s-2, with a coordinates.
Its annihilator, divided by the full locator of those a points, has
actual rank r=s-j, degree k=K-a and n=N-a nonzero evaluations. The gap
D is unchanged and k>=r. This includes F=0, j=a=0.

A projective fiber of this child lifts to a rank-(j+1) original flat
containing F. Its coordinate size is at most (j+1)*h-a. Therefore

    (r-1)*fiber_size <= (s-j-1)*(j+1)*h-(r-1)*a
                     <= N-(r-1)*a <= N-a=n.

Here (s-j-1)*(j+1)<=floor(s^2/4), and r>=2. The first inequality
uses the COMPLETE original flat: its a coordinates have already been
removed from every child fiber. Thus every such child satisfies MOMENT.
Any further full-fiber contraction is another complete original flat,
so the conclusion is hereditary without reimposing DENSITY on the child.

## 3. Jensen Closes The Full Product Induction

For real x>=1 define P_1(D,x)=D+x and, for r>=2,

    P_r(D,x)=product_(i=0)^(r-1)(D+x-i*(x-1)/(r-1)).

Its factors are D+1+alpha*(x-1), with alpha=0,1/(r-1),...,1.
It is positive, nondecreasing and convex on x>=1: its polynomial in
x-1 has nonnegative coefficients. For r=1 it is linear.

Induct over the rank of all descendants in section 2. Rank one has n
bases exactly. The required exact contraction and the proved bounds on
its children give

    B_r >= sum_i a_i P_(r-1)(D,k-a_i)
         >= n P_(r-1)(D,k-sum_i a_i^2/n)
         >= n P_(r-1)(D,1+(r-2)*(k-1)/(r-1))
          = P_r(D,k).

The middle steps are weighted Jensen and MOMENT, then monotonicity.
The arguments k-a_i are actual integer child degrees at least r-1.
Only the Jensen average is real; it is still at least r-1. The product
identity also holds at r=2, using P_1(D,1)=D+1. This proves PRODUCT.
There is no assumption that an iterated numerical envelope has curvature.

## 4. Scope And The Necessary Guard

Use the existing large-fiber construction: take a=K-s+1 distinct roots,
their locator P_A, and V=span(1,P_A,X*P_A,...,X^(s-2)*P_A). It has
actual dimension s and degree <K. All evaluations are nonzero, and
the a root coordinates belong to one projective fiber. Any basis uses
at most one of them. On N=D+K points it has at most

    (N-a)_falling_(s-1) * (N-a-s+1+s*a)

ordered bases. At s=11,K=25000,D=67466 this is

    product_(i=1)^10(D+i) * (D+11*(K-10)) < P_11(D,K).

The strict rational inequality is checked by the exact finite consumer.
All N points and the locator exist in the official KoalaBear field; no
large polynomial is expanded. Its fiber a=24990 violates 30*h<=92466.
This refutes the unqualified product even at K<D. It is neither an
unsafe received line nor a counterexample to the density-qualified result.

For MCA, choose M nonzero points of the fixed pair's joint core. They
inherit the full source's proper-flat density bound. The earlier incidence
interface inserts an actual defect, preserving the original slope and
using the same shared tuple resource. No receiver or field is descended.
