# Proof

Every polynomial in C' vanishes on G, so division by P embeds C'
isomorphically into degree-<J polynomials. A nonzero element has at
most K-1 roots; more precisely the space of degree-<K multiples of
P has dimension K-g, whence g<=K-s.

## Bad supports containing the entire core exist

Each A_gamma contains G. On A_gamma minus G the divided scalar
equation is u'+gamma v'=h'_gamma. This COMPLETE remainder cannot
be pair-contained: a child polynomial pair would lift as
(h_*+P a',P b'), fitting the whole original A_gamma, including G.

There is a bad subset of the remainder of size m-g=J+d. Otherwise
every such subset has an explaining pair. Pairs on adjacent subsets
agree on J+d-1>=J points and hence coincide. The graph of fixed-size
subsets under one-point exchanges is connected, so all these pairs
glue to one pair on the complete remainder, a contradiction. This
also covers a remainder of exactly J+d points. Adding G yields the
required original bad support. Conversely, any original saturated
bad support has a bad child: containment lifts as above.

In fact containment is equivalent. An original pair (a,b) fitting
G has a-h_* and b divisible by P, so its child fits the remainder.
Thus this argument concerns full degree-<K pairs, not just pairs
whose components belong to the chosen carrier.

## Minima and complete cores

For every b in C', v=b at each x in G, and on the complement
v=b iff v'=b/P. For a fixed saturated support the disagreement
counts are therefore equal for EVERY candidate b. Taking minima
gives equality of raw margins and a bijection of all minimizers,
including ties. The corresponding first component is

    a=h_gamma-gamma b,
    (a-h_*)/P=h'_gamma-gamma(b/P).

Both components match on G. On the complement their complete
joint agreement sets correspond pointwise. Raw classification is
unchanged, and any nonempty low union contains G. An empty low
family stays empty, but should not be described as containing G.

## Polynomial relations, including locator roots

A row is in the original relation space iff there is a polynomial
Q of degree <A with R_0 u+R_1 v=Q at every point of U. This is
equivalent to the remainder definition, even when |U|<A.
At the points of G, Q-R_0 h_* vanishes. Since
deg(R_0 h_*)<K+ell=A, the polynomial

    Q'=(Q-R_0 h_*)/P

has degree <A-g and realizes R_0 u'+R_1 v'=Q' on U'. Conversely,
a child Q' lifts to Q=R_0 h_*+P Q' of degree <A. No division at
a locator root is performed on received values. The row R itself
does not change, nor its component gcd or primitive height.

The same argument with constant rows and thresholds K,J proves
equality of the kernels of the maps F^2 -> received classes modulo
the respective polynomial evaluation codes. Each received-pair
defect is two minus the dimension of that kernel, proving equality.

The proof uses only elementary polynomial root bounds and linear
algebra. It does not assume that arbitrary previously selected
supports contain G, or that reselection preserves their old margins.
