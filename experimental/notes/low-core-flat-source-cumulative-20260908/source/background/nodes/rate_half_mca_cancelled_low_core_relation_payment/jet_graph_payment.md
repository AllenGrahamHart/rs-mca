# Projective-jet graph payment

## Moving linear projections

The supplier's new `moving_projection_graphs.md` proves the following
on the same source, with 4801<=J<=169999. For primitive A,B of
height h<=51391, if z=A*a+B*b and the actual pairs are polynomial
cubic graphs (Phi(z),Psi(z)) with A*Phi+B*Psi=Z, then

    |Gamma|+134944 <=265092257458790508,
    reserve =9888470652604579.

The input dimension is 22-d, where d is the projection kernel on
V x V. The family dimension is ceil(d/3), and its coefficient degree
is 3^(22-d-ceil(d/3)). LIST uses input degree <J+h and all original
domain points. One original resource, HIGH labels and near are retained.

For a primitive weighted-degree-<J+66972 cubic on 7117..8655,
a one-place singularity at infinity forces such a graph with h<=17580.
Its sharper whole-source total is <=117918672306944736, and group
gain <=71875471818343284. The full-kernel child consequently leaves
only one-place cubics with AFFINE singular points, not arbitrary singular
cubics. Its new explicit normal form retains rational-X coordinates.

For weighted unique-infinity nonsingular conics on J>=4801, h<=31086
gives group gain <=18684190437980288<2W. Rank-two conics already
cost <2W by the affine-product argument. Thus every irreducible conic
factor with this strict weighted bound can occupy an ordinary quadratic
slot in the mixed-cover ledger. Without the height/weight guard, keep
the earlier larger moving-conic price. Constant-direction line prices
are not changed by this conic statement.

Both new exact checks live with the existing supplier. No new required
node or edge is needed. This continuation is not in the public packet.

## Original constant-coordinate graphs

The required PROVED supplier `mca_polynomial_map_projective_jet_dimension`
strengthens the graph component dimension to ceil(s/e) when the output
polynomials have degree <K and characteristic zero or p>=K. Its proof
and finite arithmetic are self-contained relative to the existing generic
margin resource and algebraic LIST machinery; no edge points back to this
finite consumer.

On this node's exact normalized KoalaBear source, p=2130706433>J and
s=11. An actual rational-X graph b=Phi(X,a) of any degree 2..9 pays

    |Gamma|+134944<=140379757249624860,
    reserve=134600970861770227.

The full coefficient degree charge e^(11-ceil(11/e)) remains. Monotonicity
within the four constant-exponent ranges reduces the certificate to
degrees 2,3,5,9. This is a uniform consequence of a new dimension theorem,
not a sequence of numerical endpoint tuning tasks. Lower earlier graph
prices remain available where stronger.

The older numerical recipe's failure at degree eight was not unsafety;
the improved theorem now pays degrees eight and nine. It supplies no
universal graph-description theorem. General nongraph factors and their
collective coverage remain open. The already closed full-kernel strip
4801..7116 and the remaining normalized interval 7117..169999 are unchanged.

The same projective argument independently recovers dimension <=5 for
moving parabolas on these large-characteristic rows. The older moving-axis
tangent theorem has the broader characteristic !=2 scope and is retained.

Run the supplier's `verify.py` and `verify_audit.py`; the latter also checks
sharp rounding, generic-point and characteristic counterfamilies. Neither
script is a proof of the universal dimension theorem.
