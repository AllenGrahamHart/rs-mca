# Weighted payment of most affine-singular cubic cases

The later [geometric-progression payment](geometric_progression_cubic_payment.md)
pays ALL d=10 coefficient dimensions on 7117..8655, whole
N<=82951498428798039. The current residual is only d=7,dim Y=3,
1301<=h<=4327, with paid alternative 274979661292365251 unchanged.
The two-pattern theorem below is the preceding, still valid refinement.

## Completed-HIGH refinement

The same supplier now also consumes the completed-basis resource. It
proves that every HIGH record has weight >=5500, so the global base
becomes 4194116990084347. This pays d=11 on the entire normalized
interval when all LOW pairs lie on the cubic, with N<=268384711205699531.
On 7117..8655, including <=64 off-curve pairs, the latest paid alternative
is 274979661292365251; only d=7,dim Y=3,1301<=h<=4327 and
d=10,dim Y=4,1<=h<=865 remain. The d=10 carrier is exactly the
geometric-progression space printed in the supplier's height proof.

## Baseline raw-resource count

The required PROVED supplier
`mca_singular_cubic_weighted_incidence_payment` handles the remaining
affine-singular one-place curve class, using weights two and three in
coordinates adapted to its primitive linear projection. It does not
substitute a quadratic normalization parameter for a linear input.

On this node's same normalized source with 7117<=J<=8655, let d
be that projection's kernel dimension on VxV. The pair cap is

    M <=floor(2^d*3^(22-d-r)*Q_h^r),
    r=ceil(d/3), Q_h=(1048577-h)/(66973-h).

If a smaller coefficient-dimension bound is proved, it may replace r.
The same supplier proves floor(10/(11-d))*h<=J-1 for 1<=d<11,
and h=0 for d=11. Its finite table accounts for all d=0,...,11.

For d outside {7,10,11}, a group on this cubic plus at most 64
exceptional pairs has whole-source bound <=261013572486287276,
with resource, HIGH labels and the original near allowance counted once.
The other three d also pay if coefficient dimension is less than its
maximum 3,4,4 respectively. The curve and off-curve coverage are supplied
by the full-kernel child, not asserted for arbitrary sources here.

Every polynomial pair, including the singular one, is priced; the 64
exceptions are only the off-cubic pairs. The finite bound leaves reserve
13967155625107811. This is a new bound for a stronger residual
restriction, not the old smaller cubic paid-alternative bound.

This local extension is not in the immutable 1e838002 cubic export.
The remaining maximal-dimensional cases, larger normalized interval,
higher original ranks, active-v4 ownership and both prizes stay open.
