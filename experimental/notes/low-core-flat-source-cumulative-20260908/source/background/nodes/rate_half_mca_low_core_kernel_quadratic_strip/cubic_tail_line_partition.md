# Reducible cubic covers: price the complement of a large line

Status: PROVED. Keep the canonical normalized source, LOW_500, and
9527<=J<=9821. Suppose a degree-<=3 gcd covers all LOW pairs except
at most 256 pairs, as in the double-point kernel corollary. If that gcd
has a populated linear factor, either every such factor has at most
980 represented LOW pairs, or the entire source satisfies

    N<=273209735302733347,
    reserve>=1770992808661740.                        (LP-T)

No unrestricted large-line theorem beyond its old range is invoked.

## 1. The same height improves on-line collisions

For any populated factor line with at least two pairs, the already proved
primitive normalization gives

    A0*a+A1*b=Q, gcd(A0,A1)=1, h<=J-1<=9820.

Its intercept Q is a polynomial of degree <=J-1+h because the line
contains an actual bounded pair. On-line pairs differ by
(A1,-A0)*H with deg H<J-h, so joint collisions have size <=J-1-h.
Let S be the original coordinates satisfying A0*u+A1*v=Q.

If |S|<=590000+16h, all on-line pairs have at least 76499 joint
agreements on that domain and collision count <=9820-h. The Johnson
denominator is

    76499^2-(590000+16h)*(9820-h)
        =58297001+432880h+16h^2>=58297001.

The numerator is at most 747120*76499=57153932880. Its ratio to
the last lower bound has floor 980. A domain smaller than the required
agreement has an empty list. Singleton and empty lines already satisfy
this small alternative.

## 2. A large factor line leaves a small LIST domain for the other factors

Otherwise the complement of S has size at most 468396-16h. An
off-line bounded pair agrees on S at at most J-1+h points, by its
nonzero compatibility polynomial. Hence it has at least 66973-h
joint agreements outside S.

Use the original polynomial degree bound J<=9821 in this auxiliary
JOINT list, not a transported parameter degree. If the actual remaining
domain is too small, the list is empty. Otherwise its incidence ratio
is at most

    Q_out<=(458576-16h)/(57153-h)<=458576/57153<803/100.

The rational function decreases with h, its denominator stays positive,
and using the larger degree bound 9821 is a valid relaxation.

Assign the primary line's pairs first. The other gcd factors have total
degree at most two. A line has an affine coefficient space of dimension
<=11, degree one, and hence at most Q_out^11 rich pairs on this subset.
Any conic has coefficient dimension <=6 and a degree-<=2 equation
system in the original 22 coordinates. The existing all-conic dimension
split and joint LIST cover therefore give at most 2^16*Q_out^6 pairs.
This retains all conic types; it does not require a small direction height.

Put q0=803/100>8. Two other lines cost at most 2*q0^11, and one
conic costs no more because 2^16*q0^6<=2*q0^11. Repeated factors
do not add groups, and assigning intersection pairs only once is harmless.
All 256 off-gcd pairs are charged separately at their full label cost.

## 3. Use one partitioned source resource

The existing degree-free rational-pencil expression bounds the primary
line's gain plus ONE /501 source resource and near allowance by
255637082864553899. It explicitly permits other LOW groups to remain.
The nonconstant-direction version is smaller. Thus the whole source is

    N<=255637082864553899
       +ceil(981604*(2*(803/100)^11+256))
      =273209735302733347.

The outside-domain restriction applies only to pair counting; original
complete cores, scalar defects, finite labels and near are unchanged.
There is no additional /5500 base in this branch. This argument relies
on the degree-<=3 cover: it does not bound arbitrarily many unpriced
off-line factors. The old both-sides-Johnson argument is not extrapolated.
