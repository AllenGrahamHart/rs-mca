# Proof

Subtract the two displayed line equations and divide by `z1-z2`:

```text
v = cv+epsilon_v,
cv=(c1-c2)/(z1-z2),
epsilon_v=(eta1-eta2)/(z1-z2).
```

Linearity gives `cv in C`. Substitute this identity into the first line
equation and put

```text
cu=c1-z1 cv,
epsilon_u=eta1-z1 epsilon_v.
```

Then `cu in C` and `u=cu+epsilon_u`. Both error vectors are coordinatewise
linear combinations of `eta1` and `eta2`. Therefore

```text
supp(epsilon_u) union supp(epsilon_v)
    subseteq supp(eta1) union supp(eta2),
```

whose size is at most `2w`. The complement is a common agreement set for
`(u,v)` and `(cu,cv)`, proving the claim.

The v13.2 near-rational dichotomy supplies `c_i,eta_i` from a nonzero
census with `d1(u+z_i v)<=w`. No Reed-Solomon property is needed after
that step. The stronger `n-2w` conclusion also implies the source's
`n-3w` common-proximity bound, but not its support-wise MCA payment.
