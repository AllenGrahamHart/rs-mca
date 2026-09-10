# Cover Proper Actual Spans Before Treating Full Terminals

Set R=1048576,d=67472,E=21499. All weights remain the sums of
ORIGINAL assigned raw values, not raw values of shortened auxiliary
codes. The inherited source gates have whole-source price<=270000000000000000,
so an over-budget source is outside both the old full-height gates
and the newer degree-adapted gates. Fix its regular3/3 terminal W.

## Actual Dimension At Most Two

For an empty family the weight is zero. A singleton has original weight
at most R-d+t by same-pair defect disjointness.

An actual line is a polynomial pencil. If nonconstant, its weight is
bounded by the inherited full-height P_(t,1) from the coupled source
theorem. If constant, the constant-plane bound below also applies,
since its scalar ratio is at least one on a populated union.

An actual affine plane has function-field direction rank one or two.
In rank two, the weighted determinant anchor with eight old anchors
has factor (R-J+10)/(d-J+10-t). Its good children have dimension zero.
The factor increases with J and has positive denominator, so its raw
weight is at most

    (R-E+10)/(d-E+10-t) * (R-d+t).                    (RANK2)

This includes all previous anchors in the bad-coordinate bound; no
unproved repeated shared-rank drop is used at pair/shared equality.

For a constant-direction actual plane, its complete core-union complement
e is at least g(J)+1 by the new constant source gate, and at most R-d+t.
The inherited weighted pencil bound gives

    t+e*((R+1-e)/(d+1-t))^2.

Its nonconstant term decreases for e>=(R+1)/3. Every certified g+1
exceeds that threshold, so a valid cap is

    t+(g+1)*((R-g)/(d+1-t))^2.                       (CONSTANT2)

For a nonconstant rank-one actual plane, its direction is a rank-one
plane in W. A whole rank-one W would have constant direction by
full-carrier rigidity, so here W has rank two. The required rational-plane
terminal theorem applies to that very enclosure and bounds its weight
by L_t(J). No hypothetical extension or new plane cover is used.

The exact certificate compares the singleton, nonconstant-line,
RANK2 and CONSTANT2 bounds with L_t(J) on all13 profiles. The inherited
rational-plane theorem supplies the remaining plane case. This proves1.

## Whole Constant Enclosures And The Survivor

[constant_prefix.md](constant_prefix.md) proves statement2 by scalar
dimension3 LIST bounds and the same degree-adapted source gates.
Actual families need not fill that scalar space.

If every populated terminal fit both L_t, the inherited weighted descent
and original truncated-raw identity would pay the whole source. An
over-budget source therefore has a cutoff/path with weight>L_t. Statement1
forces actual span3. The earlier rational-plane theorem excludes rank-two
enclosures with a rank-one plane. Statement2 also excludes whole constant
enclosures on the prefix. This yields the asserted actual-span frontier,
without claiming that the remaining terminal classes are paid.
