# A two-radius scalar upper bound for the full joint list

Status: PROVED, hand continuation 2026-09-06.

## 1. Statement

Let F be a finite field, D a set of n distinct points, and
1<=k<=a<=n. Write M(s) for the maximum ordinary RS[F,D,k] list
size at agreement >=s, and set M(s)=0 when s>n. Put

```text
b=2a-k+1.
```

Then the worst two-component common-support list size satisfies

```text
M_2(a) <= M(a) + (M(a)-1)*M(b).                       (T1)
```

In particular, proven integers U>=M(a), V>=M(b) give

```text
M_2(a) <= U+(U-1)*V.                                 (T2)
```

The code dimension k, field F and domain D are IDENTICAL in both
scalar inputs. Only the agreement threshold changes. This is an
upper bound, not an equality and not a proof of either scalar input.
It applies to all received pairs, including the relation-free class
from proof.md, without requiring a nonzero polynomial relation.

A sharper source-specific version keeps the actual projections.
Choose any two linearly independent constant row vectors z,w in F^2.
For received pair y, let L_z(s) be the scalar list size of z*y at
agreement s, with the same convention beyond n. If either L_z(a)
or L_w(a) is zero, the joint list is empty. Otherwise its size obeys

```text
N(y) <= L_z(a) + (L_w(a)-1)*L_z(b).                   (T3)
```

One may minimize over ordered independent rows. Scaling either row
does not change its list sizes, so projective directions, including
infinity, are sufficient. No sum over directions is charged.

## 2. Proof

Partition the actual joint list by its projected polynomial p=z*f.
Every nonempty fiber maps to a scalar codeword in the list for z*y
at agreement a. Let J be the number of nonempty fibers, and H the
number with at least two members. Thus J<=L_z(a).

Consider two different joint codeword pairs f and g in the same fiber.
Choose their full common agreement sets with y, called A_f and A_g.
They have size at least a. Since f and g differ, one component of
f-g is a nonzero degree-<k polynomial. Every point in A_f intersect
A_g is a root of that component. Hence

```text
|A_f intersect A_g|<=k-1,
|A_f union A_g|>=2a-k+1=b.                            (T4)
```

At every point in this union, z*y equals the SAME polynomial p.
Consequently each nonsingleton fiber supplies one distinct member
of the scalar list for z*y at agreement b. Therefore H<=L_z(b).
If b>n, there are no such fibers, as (T4) would be impossible.

Within a fixed z-fiber, projection by w is injective: equality of
both z*f and w*f would give equality of the two original polynomial
components, since the 2-by-2 constant projection matrix is invertible.
Every image lies in the scalar list for w*y at agreement a. Thus
each fiber has size at most L_w(a).

Counting one member for every nonempty fiber, then its additional
members only for nonsingleton fibers, gives

```text
N(y) <= J + (L_w(a)-1)*H
     <= L_z(a) + (L_w(a)-1)*L_z(b).
```

This proves (T3) in the nonempty case; if a scalar list is empty,
every potential joint member would project into it, so N(y)=0.

For the uniform bound, use the two coordinate projections and
L_z(a),L_w(a)<=M(a), L_z(b)<=M(b). Since M(a)>=1 (take a
codeword as receiver), the coefficient M(a)-1 is nonnegative.
This proves (T1). Monotonicity for U>=1 and V>=0 proves (T2).

The fibers, images and union sets are all attached to actual
codewords. There is no independent product of chosen supports,
no presumed saturation of an exact-a shell, and no random-word
or collision-free-projection assumption.

## 3. Boundaries and scope

- k=1 is included: distinct polynomials in a differing component
  are distinct constants, so the intersection bound is zero.
- a=k gives b=k+1, still a strict higher-agreement scalar input.
- If b>n, (T1) reads M_2(a)<=M(a). The diagonal source (W,0)
  proves the reverse inequality, so equality holds in this regime.
- If M(b)=1, (T1) gives at most 2M(a)-1, not M(a).
- No scalar uniqueness at b or estimate on M(b) is assumed.
- A same-radius scalar upper U with U^2>B may still be usable
  through (T2), but only after proving a suitable higher-agreement
  scalar bound V. The budget test U+(U-1)V<=B is inclusive.

The relation dichotomy remains useful: nonzero-row sources already
cost at most M(a). Formula (T1) provides a scalar-only sufficient
upper route for the previously unpriced relation-free sources as well.
It does not remove the need for strong scalar decoding theorems.
