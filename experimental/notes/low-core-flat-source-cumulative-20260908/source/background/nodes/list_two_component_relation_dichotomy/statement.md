# Two-component LIST relation dichotomy

Status: PROVED by the complete hand proof in proof.md.

Let F be a finite field, D a set of n distinct elements of F, and
1<=k<=a<=n. Put ell=a-k and P_D=prod_(x in D)(X-x). For received
data y=(y_0,y_1), let U_i be its degree-<n interpolants and define

```text
V_a(y) = {(R_0,R_1): deg R_i<=ell,
          deg rem_(P_D)(R_0 U_0+R_1 U_1)<a}.             (R1)
```

Degrees of zero polynomials are -infinity. This is an F-linear space.
Let N(y) count actual pairs f_i of degree <k whose COMMON agreement
with y has size at least a. Let M_1 be the maximum scalar RS[F,D,k]
list size at agreement a. Then:

1. Every member of N(y) satisfies R_0 f_0+R_1 f_1=T_R as a
   polynomial, for every R in V_a(y), where T_R is the remainder
   in (R1).
2. Two rows independent over F(X) imply N(y)<=1.
3. Any nonzero row gives N(y)<=M_1. More precisely, its polynomial
   gcd has to divide T_R. After division, let d be the maximum
   degree of the primitive row. Either there is no bounded-degree
   polynomial solution, or d>=k gives at most one, or the ENTIRE
   joint list is in explicit agreement-preserving bijection with
   one scalar RS[F,D',k-d] list at the SAME agreement a. The domain
   D' deletes only source-incompatible roots of the original gcd.
4. With M_0 the maximum of N(y) over sources with V_a(y)={0}
   (zero when this class is empty), the exact worst-case identity is

   ```text
   max_y N(y) = max(M_1,M_0).                           (R2)
   ```

Thus the only extra two-component obstruction, beyond ordinary scalar
LIST over the SAME field and domain, lies in the relation-free class.
Neither M_1 nor M_0 is bounded by the prize budget here.

The space is invariant under adding codewords to y and transforms
invertibly under GL_2(F) changes of components. It is the kernel of
an explicit linear map from F^(2(ell+1)) to F^(n-a). Consequently

```text
3a>n+2k-2  =>  M_0=0 and max_y N(y)=M_1.               (R3)
```

For a relation-free source and any actual listed pair, write its
nonzero polynomial error vector as G(E_0,E_1), with G monic and
gcd(E_0,E_1)=1. Necessarily

```text
max(deg E_0,deg E_1)>=a-k+1;
max(k-1,deg U_0,deg U_1)>=2a-k+1.                      (R4)
```

These are necessary conditions, not bounds on the relation-free count.
There is no field-size, smoothness, received-degree or random-source
assumption. This is a codeword theorem, not an MCA slope theorem.

## Full joint upper bound from two scalar radii

The companion [scalar_tail_bound.md](scalar_tail_bound.md) additionally
proves, for M(s) the ordinary scalar maximum on the SAME F,D,k,

```text
M_2(a)<=M(a)+(M(a)-1)*M(2a-k+1).                       (R5)
```

Set M(s)=0 for s>n. For a fixed source and two independent constant
projection rows z,w, the sharper bound is

```text
N(y)<=L_z(a)+(L_w(a)-1)*L_z(2a-k+1),
```

with empty projected lists handled as N=0. A merged projection fiber
requires the same scalar polynomial on the union of two actual
agreement sets, of size at least 2a-k+1. This proves an upper bound
even for relation-free sources. It does not prove the two scalar
inputs or a prize budget; no new conditional hypothesis is adopted.
