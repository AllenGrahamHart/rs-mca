# Uniform rank-one weighted-line cap, without a scan

Status: PROVED. Let R=1048576, d=67472. On any finite-field RS row
`(n,K,m)=(R+K,K,d+K)`, `1<=K<=R`, fix one received pair. Select one
explanation and an exact size-m scalar agreement support for each distinct
finite slope. Require pair noncontainment on that SAME support.

If the selected explanations lie in an affine polynomial subspace of
dimension at most one, then the number of selected slopes is at most

```text
4070947.
```

More precisely, for `1<=j<=R`, let `N=R+j`, `M=d+j`, `q=floor(M/2)`.
The weighted-line upper-bound expressions in PR #1174 satisfy

```text
W_low=floor(binom(N,2)/(q*(M-q))) <=483,
W_high=max floor(t*(t-1)+(N-t*M+sum_i a_i)*sum_i(1/a_i)) <=4070464,
```

where the maximum ranges over `1<=t<=floor(N/(q+1))`,
`a_i in {1,q}`, and `N-t*M+sum_i a_i>=0`. The sum of the two bounds
attains 4070947 at j=1 in this certificate class. This does not assert
that an actual received line attains that number of bad slopes.

The proof handles zero-normal coordinates and dominant lines of weight at
least M. It does not require post-near status, an enumeration, or a
large-characteristic estimate beyond the existence of the stated domain.
