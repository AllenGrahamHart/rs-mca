# Actual controls for the polynomial-relation conversion

All controls use F_17, K=3, C'=span{1,X}, s=2, m=7 and d=4.
On D={0,...,11}, let w be zero on {0,...,5} and one on {6,...,11},
and set u=xw, v=-w. The polynomial relation is

    u+Xv=0,

with nonconstant primitive row (1,X). The two represented polynomial
pairs are (0,0) and (X,-1), with complete cores of size six. Their
constant received-pair gluing defect on their union D is two: any
constant polynomial combination vanishes on the first six points, so
its degree-<3 representative would be zero; on the last six this forces
both combination coefficients to be zero.

## The exceptional slope charge is necessary

At T=3, A=4 and ell=1, retain one exact support for each gamma in D:

- gamma in {0,...,5}: use pair (X,-1), h=X-gamma, and the second
  six-point core together with gamma;
- gamma in {6,...,11}: use pair (0,0), h=0, and the first six-point
  core together with gamma.

Every raw margin is one, with a UNIQUE minimizing b in C'. Every
support is pair-noncontained in the full degree-<3 code: its six equal
v-values force a constant polynomial, contradicted by the seventh value.
There are twelve distinct selected slopes, all rational-direction labels
A_1(x)/A_0(x)=x. Here U=D, e=0 and C_s=37. Omitting the exceptional
charge from (PR) would falsely give |Gamma|<=37/4<12.

Thus this is a real counterexample to the uncharged formula, not a
counterexample to the proved payment or an original prize claim.

## A nonpreferred outside label is retained and counted

Add coordinate 12 with received values (u,v)=(4,1), and keep the same
low pairs and U={0,...,11}. Add gamma=13, h=0 on the first core plus
coordinate 12. Its raw margin is again one and its minimizing pair is
(0,0). This label is NOT a rational-direction value on U and owns the
single outside point. The primitive relation fails at that outside
coordinate, as the proof permits. All thirteen labels remain counted.

## Covered versus uncovered gcd roots

On the twelve-point example use T=2, so ell=2, and the row (X,X^2).
Its gcd root zero lies in a complete low core, and primitive compatibility
u+Xv=0 holds there.

If instead u(0) is changed to one, the undivided relation still vanishes
everywhere, but its primitive relation fails at zero. The same two
polynomial pairs have joint cores of sizes five and six, so they are
still joint LIST members at A=5; their union now EXCLUDES zero. This
is the source-incompatible gcd-root case of the general LIST supplier.
It shows why covered-core compatibility must be proved rather than
deduced by pointwise division. No assertion that the perturbed data keep
the original MCA selected supports is made.
