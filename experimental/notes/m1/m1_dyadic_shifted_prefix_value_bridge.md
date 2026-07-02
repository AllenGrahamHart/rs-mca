# Dyadic Shifted-Prefix Value Bridge

Status: PROVED local bridge / REPAIR / AUDIT.

This note records a compact bridge isolated in local theorem-worker audits.
It is not an official prize solve, not a protocol soundness claim, not a
Paper-A no-slack example, not a proof of the full one-point projected-residue
local limit, and not a proof of Paper B `conj:B`.  The result is narrower: in
the dyadic shifted-prefix case, projected value growth is reduced to a
quantitative finite-field/non-upstairs collision count.

## 1. Dyadic Value Bridge

Let `n=2^m`.  Let `F_q` be a finite field with `n | q-1`, and let
`H=<eta> <= F_q^*` have order `n`.  Put `K=F_p(H)`, where `p=char(F_q)`.
Choose a residue embedding

```text
rho_pfrak : Z[zeta_n] -> K,       zeta_n |-> eta.
```

For `S subset H`, define its lift

```text
S_tilde = { zeta_n^i : eta^i in S } subset mu_n.
```

Fix `1 <= tau < n`, a support size `s`, and
`alpha=(alpha_1,...,alpha_tau) in K^tau`.  Define the finite-field prefix
fiber

```text
F(alpha) = { S subset H :
             |S|=s and e_j(S)=alpha_j for 1<=j<=tau }.
```

For `S,T in F(alpha)`, say that `S` and `T` are upstairs-equal if

```text
e_j(S_tilde)=e_j(T_tilde) in Z[zeta_n]      for 1<=j<=tau.
```

Let

```text
P_pfrak(alpha)
  = #{ (S,T) in F(alpha)^2 :
       S != T and S,T are not upstairs-equal }.
```

For `c in F_q`, set

```text
I_c(alpha) = { L_S(c) : S in F(alpha) },
L_S(X) = prod_{x in S}(X-x).
```

Let `M0` be the least power of two with `M0 > tau`, and put `N0=n/M0`.
Then

```text
|I_c(alpha)| <= (1 + sqrt(P_pfrak(alpha))) 2^N0.
```

The same argument also gives

```text
|F(alpha)| <= (1 + sqrt(P_pfrak(alpha))) 2^N0.
```

In particular, if `tau >= C n/log_2 n`, then `2^N0 <= n^{1/C+o(1)}`.

### Proof

Partition `F(alpha)` into upstairs-equality classes.  Inside one class, all
lifted supports have the same first `tau` elementary symmetric coefficients in
`Z[zeta_n]`.  By Paper B `thm:upstairs` and the class-size bound in
`cor:upstairs-poly`, each class has at most `2^N0` members.

Choose one support from each distinct value in `I_c(alpha)`.  Since one
upstairs class contributes at most `2^N0` chosen supports, the chosen supports
meet at least

```text
|I_c(alpha)| / 2^N0
```

different upstairs classes.  Picking one representative from each occupied
upstairs class gives `R` supports in the same finite-field prefix fiber that
are pairwise not upstairs-equal, with

```text
R >= |I_c(alpha)| / 2^N0.
```

Their ordered off-diagonal pairs are counted by `P_pfrak(alpha)`, so

```text
R(R-1) <= P_pfrak(alpha).
```

Thus `R <= 1+sqrt(P_pfrak(alpha))`, proving the value bound.  Omitting the
step of selecting distinct values gives the support-fiber bound.

## 2. Relation To Paper B

In the split-prime setting of Paper B, namely `q=p` and `p == 1 mod n`, the
quantity `P_pfrak(alpha)` is the collision count from `prob:perfiber`: ordered
pairs in one finite-field prefix fiber that are not equal upstairs in
`Z[zeta_n]`.

For prime powers or non-split generated fields, the same formula is the
prime-ideal or generated-field analogue of `prob:perfiber`, not literally the
problem as stated in Paper B.  This distinction matters: the residue embedding
is part of the datum.

The bridge also uses only the shifted-prefix / monomial-prefix structure.  By
`prop:monomial-fiber`, a monomial-prefix received word is an exact prefix
fiber.  For arbitrary received words `U`, the condition

```text
deg(U mod L_S) < k
```

does not reduce to fixing `(e_1(S),...,e_tau(S))`.  Applying the bridge to
arbitrary `U` would be the first false line.

In the split-prime quasipolynomial range where `thm:no-collision` applies,
`P_pfrak(alpha)=0` after quotient-periodic equality is identified upstairs,
and `cor:quasipoly-upper` recovers the known monomial-prefix positive theorem.
The bridge is useful below that range because it isolates the exact collision
quantity still needed.

## 3. Quotient-Core Value Necessity

The value ledger must also remove or budget quotient-core fibers.  The reason
is not merely that quotient cores make many supports; they can make many
projected values as well.

Assume now for simplicity that `H=mu_n subset F_p^*`, with `p == 1 mod n`.
Let `M | n` be a power of two, put `N=n/M`, and set

```text
tau = M-1,          s=k+tau<n,
r = floor(s/M),     d = s-rM.
```

Choose one `mu_M`-coset above `w0 in mu_N` and a tail
`T0` inside that coset with `|T0|=d`.  For each

```text
W subset mu_N \ {w0},       |W|=r,
```

define

```text
S_W = T0 union union_{w in W} { x in H : x^M=w }.
```

Then all `S_W` lie in one shifted-prefix fiber for prefix length `tau`.  Indeed,

```text
L_{S_W}(X)=L_{T0}(X) L_W(X^M),
```

and the first `M-1` top coefficients depend only on `L_{T0}`.

For values, there is an explicit exceptional set

```text
E_bad = H union
        union_{W != W'} { c in F_p : L_W(c^M)=L_{W'}(c^M) }.
```

For every `c notin E_bad`, the values `L_{S_W}(c)` are pairwise distinct.
Thus one shifted-prefix fiber has value image size at least

```text
binom(N-1,r)
```

at every such `c`.

One may bound

```text
|E_bad| <= M( N + (r-1) binom(N-1,r)^2 ).
```

Hence a prime larger than this exceptional-set bound admits good evaluation
points.  The statement is generic in `c`, not universal in `c`; special
points, including `c=0`, may collapse the value image.

If `C n/log_2 n <= M <= 2C n/log_2 n` and `k=rho n+O(1)`, then

```text
binom(N-1,r) >= n^{H_2(rho)/(2C)-o(1)}.
```

The sharper exponent `H_2(rho)/C` requires the sharper scale
`M=(1+o(1)) C n/log_2 n`; it is not automatic from `M=tau+1 | n`.

## 4. Remaining Wall

The exact next theorem is:

```text
M1-QUANTITATIVE-PER-FIBER-COLLISION-BOUND.
```

For dyadic `n=2^m` in the remaining polynomial/generator-field window, prove
that every finite-field prefix fiber satisfies

```text
P_pfrak(alpha) <= n^{2+o(1)}
```

after quotient-core or signed quotient-periodic branches are removed or paid.

Combined with the bridge, this would give

```text
|I_c(alpha)| <= n^{1+o(1)}
```

for the shifted-prefix projected-value problem, up to the paid toggle factor
`2^N0`.

This still would not prove the arbitrary-`U` one-point projected residue local
limit or the full Paper-B `conj:B`.  Those require a general residue-pair
upstairs classification and the full residue-line packing theorem.
