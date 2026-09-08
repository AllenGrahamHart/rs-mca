# Degree-aware Hensel numerator ledger

This companion proves the coarse estimates used in proof.md, Section 4.
It follows the algebraic recurrence of BCIKS Appendix A, but keeps the
leading-coefficient degree deficit explicit. In particular, it does not
assume Lambda(T)=Lambda(W)+b. That equality need not hold when W has
less than its allowed degree. No sharper source constant is claimed.
For example, in odd characteristic H=Y^2-Z^3 has W=1, h0=2,
D0=3, b=1 and canonical T-weight 2, whereas deg(W)+1=1.
This diagnoses a weight shortcut, not a counterexample to a proximity
theorem. The ledger below allows precisely this degree deficit.

## 1. Weighted algebraic ring

Let R(X,Y,Z) be separable in Y of degree d0>=1. Give Y weight b>=1,
Z weight 1 and X weight 0, and suppose the resulting degree is <=D0.
Thus F0=D0-b*d0>=0. Choose x0 where R(x0,Y,Z) retains degree d0
and is separable. Let H(Y,Z) be an irreducible factor there of degree
h0, with leading coefficient W(Z). Put

```text
omega=deg W,  tau=D0-b*(h0-1),
V=F0+(d0-1)*tau-omega.
```

We have omega<=D0-b*h0, tau>=omega+b and tau<=D0. Also V>=0:
for d0=1, h0=1 and V=D0-b-omega>=0; for d0>=2 use
V>=F0+(d0-2)*tau+b.

Monicize H by setting Htilde(T,Z)=W^(h0-1)*H(T/W,Z), and use
the field K=F(Z)[T]/Htilde and regular ring O=F[Z][T]/Htilde.
Give T weight tau and Z weight 1. Every nonleading monomial of
Htilde has weight <=h0*tau: if a_i is the coefficient of Y^(h0-i),

```text
deg a_i+(i-1)*omega <=D0-b*h0+b*i+(i-1)*omega <=i*tau.
```

Reduction modulo the monic Htilde therefore cannot increase weight.
On O, weights are subadditive under products and maxima under sums.
The usual norm argument (BCIKS Lemma A.1) says a nonzero regular
element of weight <=M can vanish on at most h0*M distinct scalar
substitutions. This counts distinct Z values, not all root branches.
For completeness, multiplication by beta in the basis 1,T,...,T^(h0-1)
has polynomial matrix entries of degree at most M+(j-i)*tau.
Every determinant term therefore has degree <=h0*M. The determinant
is nonzero for beta!=0 because K is a field. Any specialization that
kills beta supplies a nonzero evaluation functional annihilating this
matrix, so its determinant vanishes at that z. The polynomial root
bound proves the assertion, including specializations with repeated
roots in Htilde.

## 2. The recurrence with the deficit retained

Let alpha0=T/W. The Hensel root gamma=sum_j alpha_j*(X-x0)^j of
R has derivative zeta=partial_Y R(x0,alpha0,Z)!=0. Set
xi=W^(d0-2)*zeta. It is regular, including d0=1: the specialized
leading coefficient of R is divisible by W. Direct coefficient
degree counting gives

```text
Lambda(xi)<=F0+(d0-1)*tau-omega=V.                  (D1)
```

Here and below the powers of W in a denominator are formal rational
expressions; after the indicated leading-coefficient cancellation,
the claimed numerators belong to O.

For clarity, the recurrence's general coefficient is the coefficient
of X-increment order i and Y-increment order s in the expansion of R
at (x0,alpha0). Write it as B_(i,s)/W^(d0-epsilon-s), where
epsilon=1 if i=0 and 0 otherwise. Its regular numerator satisfies

```text
Lambda(B_(i,s)) <= F0+(d0-s)*tau-epsilon*omega.     (D2)
```

To check (D2), a term from Y^j has coefficient Z-degree <=D0-b*j.
Before the leading-coefficient cancellation its numerator weight is

```text
D0-b*j+(j-s)*tau+(d0-j)*omega.
```

This is increasing in j since tau-omega-b>=0, and its value at
j=d0 is F0+(d0-s)*tau. For i=0 the leading coefficient is divisible
by W, allowing the extra cancellation and subtraction of omega.
This proves both regularity and the bound; lower j terms already
carry the canceled W. The case i=0,s=d0 is interpreted by this same
cancellation, so no negative-power regularity assumption is needed.

Write e_j=max(0,2*j-1) and alpha_j=beta_j/(W^(j+1)*xi^(e_j)).
Then beta0=T, while the implicit-root recurrence shows beta_j is
regular and, for j>=1,

```text
Lambda(beta_j) <= (2*j-1)*V+j*omega+tau.            (D3)
```

Here is the induction without a homogeneity shortcut. A nonisolated
term for coefficient j uses X-increment i and a partition lambda
of j-i into positive lower indices l<j; put s=sum_l lambda_l.
After clearing W^(j+1)*xi^(2*j-1), that term is a constant times

```text
W^(i+epsilon-1)*xi^(2*i+s-2)*B_(i,s)
       *product_l beta_l^(lambda_l).
```

The exponents are nonnegative. If i=0 then s>=2, since the sole
s=1 term is the isolated zeta*alpha_j; if i>=1 the assertion is
immediate. Substituting (D1), (D2) and the induction hypothesis,
and using sum_l l*lambda_l=j-i, bounds the weight by

```text
(2*j-2)*V+(j-1)*omega+d0*tau+F0
       = (2*j-1)*V+j*omega+tau.
```

This proves (D3). In particular, for j>=1,

```text
Lambda(beta_j)
 <= (2*j-1)*F0+((2*j-1)*(d0-1)+1)*tau+(1-j)*omega
 <= ((2*j-1)*d0+1)*D0-(2*j-1)*b*d0
 < (2*j+1)*d0*D0.                                 (D4)
```

For j=0, Lambda(beta0)<=tau<=D0<=d0*D0. The weak inequality
is sufficient, since all zero-forcing substitution counts are strict.

## 3. Bad denominators and evaluation numerators

The bad-substitution count is at most

```text
deg W+h0*Lambda(xi)
 <=h0*F0+h0*(d0-1)*tau-(h0-1)*omega
 <=h0*d0*D0-h0*b*d0 <h0*d0*D0.                    (D5)
```

Suppose the lift is a polynomial of X-degree J>=1. A common
denominator for its evaluation is W^(J+1)*xi^(2*J-1). By (D3),
each term of its numerator, INCLUDING the j=0 term, has weight
at most (2*J-1)*V+J*omega+tau.

For any polynomial g(Z) of degree <=b, the numerator of
gamma(x)-g(Z) has the same bound because
b+(J+1)*omega<=J*omega+tau. It therefore has weight
<(2*J+1)*d0*D0 by (D4). This proves the evaluation zero bound
used to force affine coefficients when b=1.

For an inseparable factor with b=p^f, the lift has exponents divisible
by b and degree <=b*d. Apply the coefficientwise inverse Frobenius
to its monicized function field, with new variables T_hat,Z_hat and
weights tau,1. The monomial degree bounds are unchanged. The
substitutions Z_hat=z^(1/b) are still distinct. The b-th root
polynomial P has coefficients obtained from those of the lift, and
u(x)+Z*v(x)=u(x)+Z_hat^b*v(x) has weight <=b in that field.
Use J=b*d in the common-denominator argument to obtain the bound

```text
h0*Lambda(numerator) < (2*b*d+1)*d0*h0*D0.         (D6)
```

This establishes the inseparable evaluation estimate directly. The
factor b^2 in w=b^2*d0*h0*D0 conservatively dominates it by
(2*d+1)*w. No equality between tau and omega+b is required.
