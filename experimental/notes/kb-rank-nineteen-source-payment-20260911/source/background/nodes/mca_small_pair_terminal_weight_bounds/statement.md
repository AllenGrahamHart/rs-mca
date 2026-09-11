# Original-Weight Bounds For Small Pair Terminals

Use one original finite-label MCA assignment, degrees<J, original domain
size R+J, complete joint cores of size at least d+J-t, and unchanged
raw<=t owner weights. Put S=R+1 and c_t=R-d+t. All scalar and joint
LIST padding stays in the ORIGINAL field.

An actual affine pair line of primitive height h with complete-core-union
complement e contains at most

    floor((S+h-e)/(d+1-t+h))

pairs. For m actual pairs its original weight is at most

    min(m*c_t, t+m*e)                         when h0,
    min(m*c_t, R+J+(m-1)*e)                   when h>0.       (LINE)

Given a proved source gate e>=g+1 and a height interval[l,u], use
h=l in the ratio and J<=J1 in the second weight. For each possible
integer m, put e_max=min(c_t,S+l-m*(d+1-t+l)).
Maximizing these finitely many upper bounds gives a valid height-band
price. Include both constant and nonconstant directions; singleton
actual families use c_t.

For a primitive shared carrier of dimension c in{1,2,3}, degree
D<=c-1+hi and unused v>=0, an affine pair c-space has either:

1. Function-field rank one: full-carrier rigidity makes its direction
   constant. Use the proved whole-constant scalar-dimension-c price.
2. Function-field rank two, c2 or3: a determinant anchor has original
   weight bound

       (R-D+1)/(d-D+1-t) * L_(c-2),

   when d-D+1-t>0. Here L0=c_t and L1 is a line price covering heights
   at most D-1. A shared-carrier JOINT LIST cap times c_t is another
   bound for the same family; take the minimum.

The joint-list dimension is the shared polynomial dimension c, NOT the
pair-affine dimension in a larger space. No field denominator, slope
count or source resource is changed by using a tuple LIST theorem.
