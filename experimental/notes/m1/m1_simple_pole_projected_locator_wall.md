# M1 simple-pole projected locator wall

**Status:** PROVED REDUCTION / ROUTE CUT / OPEN WALL.

**Agent/model:** Codex, integrating theorem-worker audits.

**Date:** 2026-07-02.

This note records a finite reduction for the degree-one residue-line stratum of
Paper B.  It is not a proof of the full M1 packing conjecture, not a protocol
soundness claim, and not another finite no-slack example.  Its purpose is to
identify the exact object left after the simple-pole, fixed-pencil, quotient,
subfield, and Johnson branches are separated.

## Simple-pole setup

Let `F` be a field, let `D subset F` be a finite set of distinct elements, and
let `c in F \ D`.  Fix `h >= 1` and put

```text
E(T) = T-c,       B(T) = 1,       f(x) = 1/(x-c).
```

Let `a:D -> F` be an arbitrary anchor word.  A finite slope `z in F` has a
simple-pole low-tail witness on a support `S subset D` if

```text
a - z f in ev_S(F[T]_<h).
```

Equivalently, there is `R in F[T]_<h` such that

```text
a(x) - z/(x-c) = R(x)              for all x in S.
```

Set

```text
b(x) = (x-c)a(x),                  x in D.
```

For `s>h`, define the one-point projected list-value set

```text
PLV_c(b;h,s)
  =
{ Q(c) :
  Q in F[T], deg Q <= h,
  |{x in D : Q(x)=b(x)}| >= s }.
```

## The reduction

The set of slopes `z` with a simple-pole low-tail witness on some support
`S_z` of size at least `s` is exactly

```text
PLV_c(b;h,s).
```

Proof.  If `z` has a witness on `S`, choose `R in F[T]_<h` with

```text
a(x) - z/(x-c) = R(x)              for x in S.
```

Multiplying by `x-c`, we get

```text
b(x) = z + (x-c)R(x)               for x in S.
```

Thus

```text
Q(T) = z + (T-c)R(T)
```

has degree at most `h`, agrees with `b` on `S`, and satisfies `Q(c)=z`.  Hence
`z in PLV_c(b;h,s)`.

Conversely, if `Q in F[T]` has degree at most `h`, agrees with `b` on a set
`S` of size at least `s`, and `z=Q(c)`, then

```text
R(T) = (Q(T)-Q(c))/(T-c)
```

is a polynomial of degree `< h`.  On `S`,

```text
a(x) - z/(x-c)
  = (b(x)-Q(c))/(x-c)
  = (Q(x)-Q(c))/(x-c)
  = R(x).
```

So `S` is a simple-pole witness support for slope `z`.

## Circuit-color form

For an `(h+1)`-set `A subset D`, let

```text
P_A(T)=prod_{x in A}(T-x),
mu_A(g)=sum_{x in A} g(x)/P_A'(x).
```

Then `mu_A` is the divided-difference circuit functional annihilating
`ev_A(F[T]_<h)`, and

```text
mu_A(f) = (-1)^h / prod_{x in A}(x-c).
```

The finite slope forced by the circuit `A` is therefore

```text
r(A)=mu_A(a)/mu_A(f)
    =(-1)^h prod_{x in A}(x-c) mu_A(a).
```

If `I_A(b)` is the unique degree-`<=h` interpolant to `b` on `A`, then

```text
r(A)=I_A(b)(c).
```

Thus a support `S` with `|S|>h` is monochromatic of color `z` in the
simple-pole secant-color hypergraph if and only if one polynomial
`Q in F[T]_{\le h}` agrees with `b` on `S` and has outside value `Q(c)=z`.

## Immediate payments and non-payments

For distinct slopes `z_i != z_j`, choose corresponding polynomials
`Q_i,Q_j` of degree at most `h`.  On `S_i cap S_j`, the two polynomials both
equal `b`; hence `Q_i-Q_j` vanishes there.  Since

```text
(Q_i-Q_j)(c)=z_i-z_j != 0,
```

`Q_i-Q_j` is nonzero, and therefore

```text
|S_i cap S_j| <= h.
```

This is the simple-pole Johnson overlap payment.  It only closes the usual
Johnson-paid regime, for example when `s^2 > n h`.  It does not prove the
corrected-reserve bound in the hard range `s^2 <= n h`.

The fixed-pencil branch is also not the remaining obstruction.  A global
fixed-pencil packet has the standard private-row payment.  Local pencils occur
inside any large monochromatic clique and do not automatically globalize, so
peeling local pencils is not a proof of the aperiodic packing bound.

Finally, quotient filtering cannot be attached only to the denominator
`T-c`.  The simple pole itself is not a proper multiplicative quotient
pullback, but quotient-core behavior can enter through the projected word
`b=(T-c)a`.  The quotient branch must therefore be stated for the projected
list-value problem, not merely for the denominator.

## The exact remaining wall

The simple-pole M1 wall is:

```text
M1-ONE-POINT-PROJECTED-LOCATOR-LOCAL-LIMIT.
```

A clean generated-field target is:

```text
For smooth generated-field domains H <= F_q^* of order n, h=rho n+O(1),
c notin H, s=h+sigma, sigma >= C n/log n, and after quotient-core, subfield,
contained/tangent, fixed-pencil, and Johnson-paid branches are separated,

  max_{b:H->F_q} |PLV_c(b;h,s)| <= n^{1+o(1)}.
```

This target is weaker than the full arbitrary locator-fiber local limit: it
counts only the one-point image `Q(c)`, not all supports or all nearby
codewords.  But it is exactly equivalent to the simple-pole slope-counting
problem above.

The first false line is:

```text
large locator fibers automatically imply many simple-pole slopes.
```

They do not.  The slope set is only the outside-value image of the locator/list
fiber.  Support-rich simple-pole packets may still have small projected slope
image.

## Relation to Paper B

This is the `t=1` simple-pole stratum of the residue-line packing problem.
Proving the projected locator wall would be genuine progress on M1 and would
connect the residue-line problem to the L1 locator-fiber program.  It would
not prove the full `conj:B`: squarefree multi-pole denominators, repeated-pole
or jet data, quotient-periodic denominator families, and extension/subfield
transfer remain separate.
