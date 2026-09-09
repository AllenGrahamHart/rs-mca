# Root Escape And Joint Johnson Counting

## 1. Charge The Full Primitive Row Degree

For an off-pencil pair f=(a,b), the polynomial

    P_f=A0*a+A1*b-Q

is nonzero and has degree at most K+h-1. At every joint agreement
coordinate of f inside U, compatibility of the receiver makes P_f vanish.
Thus at most K+h-1 of f's joint agreements lie in U. At least
A=m-T-(K+h-1) lie outside U. This proves escape and the zero case A>e.

The credited rational-pencil theorem obtains its primitive row by removing
the gcd of an actual pair difference. Compatibility on the COMPLETE core
union follows from an agreeing pair at each coordinate, including gcd
roots. It does not require dividing received values at those roots.

## 2. The Johnson Argument Counts Joint Pairs Directly

Assume 1<=A<=e and A^2>e*(K-1). These imply A>K-1 and hence A>=K.
For each distinct off-pencil pair choose exactly A outside agreements.
Two distinct pairs differ in at least one nonzero polynomial of degree<K,
so their chosen joint supports intersect in at most K-1 coordinates.

For M such pairs and coordinate incidences c_x on the e-point complement,
sum c_x=M*A and Cauchy--Schwarz gives

    M^2*A^2/e-M*A <= sum c_x*(c_x-1)
                   <= M*(M-1)*(K-1).

For M>0, rearrange and divide by the positive denominator to get (ESC).
The integer floor is valid because M is an integer. This is the credited
ordinary Johnson proof applied to joint supports, not the product of two
scalar lists. Over an infinite field the list is still finite: A>=K and
any K agreeing coordinates determine both component polynomials.

## 3. Shared-Carrier LIST Beyond The Direct Johnson Gate

Restriction to D\U does not change the polynomial identities specifying
the two affine component carriers. If they share a space V of dimension
at most s, the credited shared_carrier_joint_lists.md bounds these
off-pencil pairs on (e,K,A) by its proved common-carrier LIST compiler.
The dimension is dim V, not the pair family's possibly larger affine rank.

One may add distinct auxiliary coordinates with arbitrary received values:
every formerly A-agreeing pair remains A-agreeing. Likewise, relaxing its
degree bound upwards or agreement threshold downwards only enlarges the
candidate set. Thus a valid larger-domain, larger-degree, lower-agreement
shared-carrier cap remains an upper bound. All finite field/padding and
positive corridor gates must still be checked by the consumer.

The original source, its labels, degree bound and carrier do not change.
Only this auxiliary pair count is restricted to D\U. Whether and how it
pays original finite slopes must be proved separately.
