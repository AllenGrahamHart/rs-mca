# Joint lists with one common polynomial carrier

Status: PROVED, 2026-09-07. The SAME formulas (P),(S), starting
from U_0=1, also bound joint lists of every finite arity b>=1 in

    (h_1+V) x ... x (h_b+V),

where dim V<=s and deg h_i,deg V<K. Agreement means all b
components match the received tuple on the same coordinate. The
dimension parameter is the common POLYNOMIAL space V, not the
affine dimension of the tuple list, which can be as large as b*s.
Different component spaces may be used only after enclosing all of
them in the same V and charging its actual dimension.

## Proof of the extension

Two distinct polynomial tuples differ in at least one nonzero
degree-<K component. Their common joint agreement supports therefore
intersect in at most K-1 points. The incidence/Cauchy proof of the
full Johnson bound is unchanged and independent of arity.

Padding multiplies EVERY component by the same new locator and puts
the zero received tuple at the new coordinates. It is injective,
preserves the dimension of V and adds the same number of JOINT
agreements. Thus the full-code padded-degree bound remains valid.

At a common evaluation zero of V, subtract the tuple (h_i), delete
the coordinate and divide every component by X-x. All tuple words
survive, and at most one JOINT agreement is lost. The new common
polynomial carrier is V/(X-x), with unchanged dimension. This costs
no tuple word regardless of whether the common tuple matched there.

At a coordinate x where evaluation on V is nonzero, consider the
joint list agreeing there. If nonempty choose ONE tuple f* from it.
For every other tuple f, EACH component difference f_i-f*_i belongs
to the SAME space

    V_x={v in V:v(x)=0},   dim V_x=dim V-1.

After division by X-x the common carrier has dimension one less.
This is not a claim that the tuple list loses only one or at least
two affine dimensions: the induction measures dim V. Every agreeing
tuple maps injectively into the lower-rank joint list on the same
(r,w) corridor. Degree zero gives at most the zero tuple.

With no common zero, count joint agreement incidences just as in the
scalar proof: L*(w+K)<=(r+K)*U_(s-1). The induction on K for (P)
and the actual-dimension split for (S) are now literally the same:
for K<=the padded degree use full Johnson; at common zeros use the
same-rank smaller-K claim; otherwise anchor. A dimension-zero common
carrier contains only one tuple, so the base bound is one at every
arity. The proof is uniform in arity, receivers, domains and shifts.

The unchanged `compiler.py` therefore supplies these joint-list caps.
This is a joint LIST theorem. Converting it into an MCA count still
requires a correct slope-to-pair grouping, outside multiplicity and
global margin resource; these are provided separately, not assumed here.

Provenance: direct componentwise extension of this node's elementary
proof, with the common-carrier dimension made explicit. No MCA Hensel
or unmerged upstream theorem is used.
