# Proof: Pay Heavy Receiver Classes, Then The Remaining Tuple Resource

Write H=52999, near=134944, and P_d=prod_(i=1)^10(d+i).
The generic receiver-fiber theorem applies with s=11. In particular
a<=J-10; this is an actual polynomial common-root-space bound.

## 1. Two Full Child Caps, With No New Near Event

For a degree k'=J-a<=2000 child, use the padded-Johnson supplier's
same-field padding proof with anchor degree 2000. On that anchor
n'=1050576, m'=69472 and degree convention d_0=1999. The rounded
linear Johnson theorem with multiplicity one has exact gates

    4*m'^2>=9*n'*1999, 4*1999<=n'.

Conservative integer ceilings are

    ceil(sqrt(9*n'*1999/4))=68741,
    ceil(sqrt(9*n'/(4*1999)))=35,
    max(35,ceil(9*n'/(12*1999)))=395.

Consequently a FULL child cap, including all bad slopes, is

    Q_2000=2*68741*35^2*395+(n'-m'+1)*35+395
          =66558441820.

Padding permits every smaller positive degree over the SAME field, on
arbitrary distinct points. The field has enough unused points. This is
not a claim that a Johnson cap is monotone in degree without padding.

For arbitrary k'=J-a<=R, the required padded scalar-descent theorem
gives the FULL affine-dimension-at-most-ten cap

    Q_10=156765527508668296.

Both caps admit arbitrary child words and preserve original finite labels.
Neither requires or charges a child post-near event. They are alternative
inputs to the generic theorem, not additional unproved assumptions.

## 2. One Uniform HIGH Resource

For all J in [14000,H], the resource

    C(J)=(R+J)_falling_12/[(d+J)*P_d]

is convex. With y=d+J its expansion is a polynomial with nonnegative
coefficients plus a positive constant/y, since all R-d-i are positive.
The endpoint ceilings give C(J)<=13541615650357694642=:C_0.

For raw>=7 the completed weight is >=10488/125: at seven its basis
part is at least 84*(1-77/(d+1))>10488/125; it increases on 7..84
because d+1>12*84; larger margins have truncated weight >=84.
For raw>=12 similarly its basis part at twelve is
at least 144*(1-132/(d+1))>143. It increases on 12..144 since
d+1>12*144, and thereafter truncated weight is >=144. Margins above
d also satisfy these bounds. Thus the HIGH quotients, BEFORE near, are

    floor(125*C_0/10488)=161394160592554522,
    floor(C_0/143)=94696612939564298.                (HIGH)

The product lower bounds use prod(1-x_i)>=1-sum x_i. Monotonicity of
the eleven-factor basis part follows from 1/r-11/(d+1-r)>0. These
are interval proofs, not scans of all margins.

## 3. Fibers With At Most 2000 Degrees Left

Use theta=1/11 and T=6. There are at most ten heavy receiver colors,
each paid by Q_2000+a. On light cores the generic monotonicity result
gives b_theta=F_A(0). Put D_1=d-6=67466. This value increases with a,
so a>=J-2000 gives the uniform lower bound

    B_0(J)=(D_1+J)*(D_1+1)
             *prod_(i=1)^9(D_1+J-1990-i).

All ten nonconstant factors are positive with logarithmic derivative
at least 1/(D_1+H). Since

    10*(R+14000-11)>12*(D_1+H),

(R+J)_falling_12/(12*B_0(J)) decreases on the WHOLE interval.
Its exact floor at 14000 is 248408193733124448. Taking the maximum
with the first HIGH quotient and adding the disjoint heavy groups gives

    |Gamma|+near <=10*(Q_2000+H)+248408193733124448+near
                =248408859318207582.

The harmless bound a<=H is used for the exception allowance only.
There is no summation over hypothetical fibers or a second near add-back.

## 4. Fibers Of At Least Half The Degree

Use theta=1/2 and T=11, so at most one heavy color is paid by Q_10+a.
Put D_2=d-11=67461. Since a<=J-10<=52989, a/2<D_2+1; the
light basis function has no kink on [0,a/2]. Its minimum is at 0 or a/2.
The zero branch increases in a. The half branch is positive log-concave
in a, so its minimum on J/2<=a<=J-10 is at an endpoint. Three profiles
therefore suffice, evaluated in

    B(J,a,t)=(D_2+J-t)*prod_(i=1)^9(D_2+a+10-i-t)
               *(D_2+1+10*t):

    (a,t)=(J/2,0), (J/2,J/4), (J-10,(J-10)/2).

On each profile the first ten factors have logarithmic derivative at
least 1/(4*D_2+3*H). The last factor is nondecreasing. Positivity is
immediate on 45000<=J<=H, and

    10*(R+45000-11)>12*(4*D_2+3*H).

Thus each tuple-resource quotient decreases on the whole interval.
Their exact floors at J=45000 are respectively

    83217244759090589, 115346523791651123, 24011435147053027.

Take their maximum and the second HIGH quotient. Adding just the one
heavy-class cap and one original near allowance yields

    |Gamma|+near<=Q_10+H+115346523791651123+near
                =272112051300507362.

Real profile endpoints bound integer fibers by relaxation. The proof
handles ALL fiber sizes and ALL J under each printed gate. The new
source constraints come from the actual fixed receiver, not numerical
survival or an invented classification. Their original-source use is
the existing gauge/complete-core assembly, whose labels and field remain.
