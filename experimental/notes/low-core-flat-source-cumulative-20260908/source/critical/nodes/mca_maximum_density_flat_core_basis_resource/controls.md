# Small Algebraic Controls

The two checkers use independent Gaussian-rank and exact Bareiss-determinant
censuses. Matrices have size at most nine; only 2794 unordered subsets
are tested per complete nonuniform census. Everything is Python standard
library, serial, and fits RAMguard tiny. These are controls, not a formal
proof or an exhaustive search of dimension-eleven carriers.

## Dimension Eleven: A Uniform Actual Source

Over F_29 take V=F[X]_<11 and a 22-point zero received core. At two
additional points 22,23 put (u,v)=(0,1),(-1,1). Labels 0 and 1 have
different 23-point scalar supports and explanation zero. Both supports
are full-code bad: a degree-<11 pair vanishing on the common core must
be zero, contradicting its defect. Thus g=0, m=23, d=12, T=1 and c=12.

Every proper j-flat has at most j evaluations and a spanning j-set
attains that bound, so h=1. For j=1..4 and t=0..j the exact inside
partition is the Vandermonde identity

    sum_b binom(11,b)*(t)_b*(22-t)_(11-b)=(22)_11.

All fourteen cases agree with the injective construction. Every label has
337903056691200 completed tuples. Their unique defect coordinates make
the two tuple sets disjoint in the original domain.

## Inside Rank Smaller Than Flat Rank

The remaining controls test the inside-extension coupling with general
dimension s and binom(s,b), not the full j<=4,c>=12 theorem. Use

    V=span{1,X,...,X^(j-2),H,G,XG,...,X^(s-j-1)G},

where G is the locator of 0..a-1 and H of 0..z-1. All polynomial degrees
are distinct and <K. The full A has rank j, but the selected inside core
has rank j-1. Outside quotient evaluations form a full Vandermonde system.

| p,s,K,j,a,z | Inside core | Outside core | Ordered full-basis counts by inside cardinality | Coupled lower bound |
| --- | --- | --- | --- | ---: |
| 17,5,9,2,6,4 | 0..3 | 6..12 | 2520,15840,0 | 12600 |
| 13,7,11,3,7,5 | 0..4 | 7..12 | 0,25200,302400,0 | 25200 |
| 17,9,12,4,7,6 | 0..5 | 7..14 | 0,2177280,40642560,203212800,0 | 21772800 |

The primary checker measures each inside span's closure; the audit uses
the inside Vandermonde model to compute the same closure counts directly.
Both check sum y_b=E_(b+1) and each constructed inside class against the
actual full-basis census. The lower bound remains positive even when
E_j=0: demanding that the inside core span the entire flat would fail.
No assertion of maximum density for these three smaller controls is used.

The universal maximum-density/preimage argument, g=0 guard and c>=12
log-concavity proof remain hand proofs. Earlier fiber controls independently
show why free outside independence and whole-carrier zero-freeness cannot
be silently substituted for their actual hypotheses.
