# A populated rational line is small or the source pays

Status: PROVED. Keep this node's canonical normalized KoalaBear source
with 8656<=J<=9526, LOW cutoff 500, complete joint agreements at least
A=J+66972, and distinct original finite slopes. Put n=1048576+J.

For EVERY affine line over F(X) containing represented LOW pairs,
either it contains at most 696 such pairs, or the WHOLE source satisfies

    N=|Gamma|+134944<=255637083438792239<B.             (L)

There is no constant-direction or primitive-height premise. In the second
case all LOW pairs off the line, not only those on another chosen curve,
number at most 585. This is a collective source dichotomy, not a bound
obtained by summing separate full-source charges.

## 1. Height improves the on-line collision bound

A group with at most one pair already meets the small alternative.
Otherwise the required rational-pencil proof writes the line as

    A0*a+A1*b=Q,
    gcd(A0,A1)=1, h=max(deg A0,deg A1)<=J-1,
    (a,b)=(a_*,b_*)+(A1,-A0)*H, deg H<J-h.

Q is a polynomial of degree <=J-1+h because an actual bounded pair
lies on the line. The coprime direction has no simultaneous evaluation
zero. Two distinct on-line pairs agree jointly only at zeros of their
parameter difference, hence on at most J-1-h coordinates. This is the
degree improvement that must be retained for nonconstant directions.

Let S={x:A0(x)u(x)+A1(x)v(x)=Q(x)}. All joint agreements of
on-line pairs lie in S. For an off-line bounded pair f, the nonzero
polynomial A0*f0+A1*f1-Q has degree <=J-1+h. At most that many
joint agreements lie in S; at least 66973-h lie outside S.

## 2. An asymmetric split works uniformly in h

Use cutoff N1=592000+16h. If |S|<=N1, on-line pairs have agreement
at least a1=75628 on at most N1 coordinates and mutual collision
at most c1=9525-h. Their Johnson denominator is

    a1^2-N1*c1=80794384+439600h+16h^2>=80794384.

Their numerator N1*(a1-c1) increases on 0<=h<=9525 and is at
most 744400*75628. Its ratio to the displayed minimum denominator
has floor 696. This proves the small alternative without optimizing h.

If |S|>N1, the complementary domain has size at most
N2=466101-16h, agreement at least a2=66973-h, and off-line pair
collision at most c2=9525. Now

    a2^2-N2*c2=45770704+18454h+h^2>=45770704.

The numerator N2*(a2-c2) decreases with h on this range, since both
positive factors do; at h=0 it equals 26776570248. Its ratio to the
minimum denominator has floor 585. These Johnson bounds count joint
pairs via the ordinary Cauchy incidence argument. A domain too small
for the required agreement simply has an empty list.

## 3. Pay the whole source in the large-line alternative

Partition LOW pairs into the line and its complement, retaining all
their assigned labels. The existing degree-free pencil supplier bounds
the on-line gain together with ONE original /501 resource and near
allowance by 255637082864553899. For constant directions this is
its coupled expression bound; for nonconstant directions the stronger
bound C//501+134944+17200000000000000 is below it. Both groupwise
arguments allow other LOW groups to remain and do not relabel them HIGH.

Every off-line pair carries at most 981604 original finite labels.
Thus the entire source has

    N<=255637082864553899+585*981604
      =255637083438792239.

The bound includes any off-kernel pairs. There is no extra resource,
near charge, coordinate deletion, or assumption about the received pair
off either group. Therefore a source exceeding (L) has at most 696
represented LOW pairs on EVERY populated rational line.
