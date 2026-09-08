# Rounded linear Johnson MCA bound

- **status:** PROVED by the source-based hand argument in proof.md
- **scope:** arbitrary finite fields and distinct evaluation domains; M=1
- **review:** independent hand review and generated DAG replay pending

Let C=RS[F,D,k] mean degree <k, with n=|D| and 2<=k<n. Put
d=k-1 and rho=d/n. Let a be an integer, 0<=a<=n, and r=n-a.
For an integer m>=1 assume

```text
4*m^2*a^2 >= (2*m+1)^2*n*d.                          (G)
```

Define the following positive real bounds and integer lifting length:

```text
t=m+1/2,  X=t*sqrt(n*d),  Y=t*sqrt(n/d),
Z=max(Y,t^2*n/(3*d)),  L=ceil(X),
H=2*L*Y^2*Z + (r+1)*Y + Z.                          (H)
```

For every received pair (u,v), the number of distinct ORIGINAL finite
slopes z admitting a set A of size >=a on which u+z*v has a degree-<k
explanation but (u,v) has no pair of degree-<k explanations is <=floor(H).
Consequently the full worst-case MCA numerator satisfies

```text
B_C(a) <= min(|F|,floor(H)).                         (M)
```

This counts the complete threshold event, including all higher-agreement
witnesses. No strip, owner census, quotient flatness, or near-pair
exception assumption is used. For fixed rho and fixed m this is O(n).

The proof uses BCHKS Lemma 3.1 and the written Hensel estimates in
BCIKS Section 5 and Appendices A/C. It does NOT import the sketched
BCHKS Theorem 4.6 as a proved black box. Its constant is slightly larger:
the lifting length is rounded up and specialization-content exceptions
are paid separately. No claim about the exact printed constant or M>1.

The companion exact_agreement_and_small_multiplicity.md proves the
relaxed gate and the m=1,2 boundary cases. Z is unchanged for m>=2;
at m=1 it is unchanged only when 4d<=n. The old m>=3 theorem and
stronger agreement gate remain valid special cases.

At prize budget B=floor(|F|/2^128), H<B+1 suffices for safety. Exact
integer tests and improved full-row certificates are in the consuming
prize_full_threshold_brackets/exact_gate_johnson_payment.md; the older
linear_johnson_bounds.md retains valid weaker certificates.
This node does not supply adjacent unsafety or determine the true crossing.
