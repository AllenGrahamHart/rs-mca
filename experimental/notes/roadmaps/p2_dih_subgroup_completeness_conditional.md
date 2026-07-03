# P2: dihedral subgroup completeness, tame proof and wild exception

DAG node: `f_dih_subgroup_completeness`.

Status: CONDITIONAL.  The intended dihedral stabilizer theorem is true in the
tame prize rows, but the raw statement "every 2-power `n | q-1` has stabilizer
`Dih_n`" is false over extension fields.

## Statement

Let `F=F_q`, let `H=alpha * mu_n` with `n >= 4`, `n` a power of two, and
`n | q-1`.  The expected dihedral subgroup of `PGL_2(F)` is

```text
x |-> zeta x,
x |-> alpha^2 zeta / x,        zeta in mu_n.
```

It always has order `2n` and preserves `H`.

The theorem proved here is:

```text
If the PGL_2(F)-set-stabilizer of H is tame
(equivalently, for the rows used below, has no characteristic-p element),
then Stab_{PGL_2(F)}(H) = Dih_n.
```

A simple sufficient row-level check for tameness is

```text
char(F) does not divide n-1.
```

Indeed a nontrivial characteristic-`p` Mobius element has exactly one fixed
point on `P^1` and all other orbits have size `p`.  Since `p` does not divide
`n`, a `p`-element preserving an `n`-point set must have one fixed point in the
set and hence `n == 1 mod p`.

## Proof in the tame case

Work over an algebraic closure; this can only enlarge the stabilizer.  Let
`G` be the stabilizer of `mu_n`.  It contains the rotations `x |-> zeta x` and
the inversion `x |-> 1/x`, hence contains `Dih_n`.

Because `G` is tame and finite, the finite-subgroup classification for
`PGL_2` applies: `G` is cyclic, dihedral, `A_4`, `S_4`, or `A_5`.

For `n >= 8`, the groups `A_4`, `S_4`, and `A_5` have no element of order `n`.
Thus `G` is cyclic or dihedral.  It is not cyclic because it contains both the
rotation subgroup and inversion.  If `G` were a larger dihedral group `D_m`
with `m > n`, its order-`m` rotation would preserve `mu_n`; away from its two
fixed points, its orbits have size `m`, impossible on an `n`-point set.  Hence
`m=n` and `G=Dih_n`.

For `n=4`, the four points form the harmonic set `{1,-1,i,-i}`.  In tame
characteristic its unordered cross-ratio orbit is the harmonic orbit
`{-1,2,1/2}`, whose stabilizer is exactly the order-8 dihedral group.  The
larger tetrahedral case is the wild characteristic-3 case recorded below, so it
is excluded by tameness.

Finally, a coset `alpha * mu_n` is conjugate to `mu_n` by the dilation
`x |-> alpha^{-1}x`; conjugating `x |-> zeta/x` gives
`x |-> alpha^2 zeta/x`.  Thus the same result holds for every multiplicative
coset.

## The wild exception family

The raw all-`q` statement fails when the domain is a subfield circle.  If
`K=F_{p^m}`, `L=F_{p^{2m}}`, and

```text
C = {x in L^* : x^(p^m+1)=1},
```

then `|C|=p^m+1`.  Under a Cayley transform, `C` is `PGL_2(L)`-equivalent to
`P^1(K)`, so its set-stabilizer contains a conjugate of `PGL_2(K)`, of size

```text
p^m (p^(2m)-1),
```

which is much larger than `2(p^m+1)`.  When `p^m+1` is a power of two, this is
exactly a 2-power multiplicative domain and is an exotic stabilizer.

The verifier pins the first two cases:

```text
F_9,  n=4:  |Stab(mu_4)| = 24  vs |Dih_4| = 8.
F_49, n=8:  |Stab(mu_8)| = 336 vs |Dih_8| = 16.
```

It also checks nearby non-wild rows (`F_25`, `F_49` with `n=16`) where the
stabilizer returns to the dihedral size.

## Consequence for the DAG

The quotient taxonomy is complete on tame multiplicative/coset rows: every
PGL2 symmetry mechanism is cyclic or dihedral, hence already recorded as a
multiplicative or Chebyshev/dihedral quotient.

The named remaining condition is:

```text
p2_no_wild_subfield_circle_domain
```

It excludes domains PGL2-equivalent to `P^1(F_{p^m})` inside
`F_{p^{2m}}` (and their conjugates).  The existing prime-field E36 rows satisfy
it, and the pinned `F_17^32, n=512` row satisfies the easy congruence check
`17 does not divide 511`.

## Verifier

Run:

```bash
python3 experimental/scripts/verify_p2_dih_subgroup_completeness.py
```

The pinned certificate is
`experimental/data/certificates/p2-dih-subgroup-completeness/p2_dih_subgroup_completeness.json`.
