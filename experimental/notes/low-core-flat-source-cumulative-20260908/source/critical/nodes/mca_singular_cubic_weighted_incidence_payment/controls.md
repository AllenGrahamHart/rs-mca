# Guards and surviving dimension examples

## Three maximal-dimension patterns occur algebraically

These test the baseline dimension limits. The completed-HIGH-weight
refinement now pays d=11 and low heights in d=7; the examples are not
claims that those source classes remain unpaid.

Take V=P_<=10, so K=11, and characteristic >11.

- For d=7, choose A=1,B=X^4 and
  f(T)=(T^2-X^4*T^3,T^3), deg T<=2. Then a+X^4*b=T^2,
  b^2=(a+X^4*b)^3, and the parameter family has dimension three.
  The cubic point at infinity is smooth and its cusp is affine.
- For d=10, use A=1,B=X and the same construction with deg T<=3.
  Both outputs have degree <=10; the family has dimension four.
- For d=11, use A=1,B=0 and f(T)=(X^4*T^2,T^3), deg T<=3.
  Its equation is a^3=X^12*b^2, and its family has dimension four.

The coordinate spans together fill all eleven directions in each case.
For the first two examples, varying a scalar multiplier of T separates
the quadratic and cubic homogeneous parts, and polarization gives the
polynomial product spans. Their unions are respectively P_<=4 plus
X^4*P_<=6, and P_<=6 plus X*P_<=9. In the last example they are
X^4*P_<=6 and P_<=9. Each sum equals V. The parametrization is
generically injective since T=b/(a+X^h*b) in the first two examples,
and T=X^4*b/a in the third.

These are sharp dimension controls, NOT canonical unsafe sources or
error-rank-twelve examples. No received pair, huge bad-slope count or
full source contract is manufactured from them.

The two current residual height/dimension ranges also have examples at
the actual lower-strip degree scale: replace X by U=X^800 in the first
two displays and take V=span{1,U,...,U^10}, K=J=8001. The d=7
example has h=3200 and dimension three; d=10 has h=800 and dimension
four. All output degrees are <=8000 and V contains 1. This needs no
large polynomial expansion. It still supplies no received pair or unsafe
slope count; it only rules out deleting the remaining geometric classes
by their degree, height, dimension or empty-carrier-core requirements.

## The common carrier factor can vanish outside the joint cores

The normalized source assumes {x:V(x)=0,v(x)=0,u(x)=h_*(x)} is
empty; it does NOT assume V is basepoint-free on the whole domain.
For example V=X*span{1,X^800,...,X^8000} has q=X, and at X=0
the receiver value v(0)=1 excludes that point from the universal core
regardless of u(0). Every allowed second polynomial has value zero there,
so it is outside every complete joint core but can carry scalar defects.
This is a guard on the definition, not an unsafe-source claim. The exact
geometric-progression identity remains valid. Only division by q on the
whole domain would be unjustified; none of the proved counts does that.

## Power-cover multiplicity requires a branch guard

Over k, z->z^2 has two distinct preimages away from zero, but only
one at zero. Likewise w->w^3 has three away from zero in characteristic
not three. The proof chooses shifts away from the FINITE counted set;
blindly dividing a count by 2^N*3^d at branch points is invalid.
Small F_37 controls have two square roots of 1 and three cube roots of
8, but one root each of zero. These count only the displayed fibers.

The shifts live in the algebraic closure for degree counting. They are
not transformations of original finite slope labels or code coordinates.

## A pure degree cover can break finite projection

The point {(x,y)=(0,0)} has a finite x projection. The pure line cover
{x=0} does not: its x coordinate is constant on a positive-dimensional
component. A scalar incidence induction cannot be applied to that cover
using the assertion g<=K+h-1. This is why the proof uses the weighted
degree budget of the ACTUAL equation locus and retains its low-dimensional
components instead of introducing a convenient pure cover.

The assumption Q_h>=3 is also needed to maximize (2Q_h/6)^v at
v=r. For Q_h<3 this monotonicity reverses; the stated formula is not
obtained by that step. The finite source has Q_h>15 throughout.

## Recipe limits are not counterexamples

The three large entries in the baseline raw-resource table are upper bounds exceeding
the budget, not unsafe constructions. Dropping their actual coefficient
dimension by one makes every entry affordable. The new dichotomy uses
261013572486287276, not the older smaller paid-alternative bound.
