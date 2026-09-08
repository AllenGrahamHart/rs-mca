# Near-rational support-wise two-anchor payment

- **status:** PROVED
- **object:** finite-affine support-wise MCA bad slopes
- **role:** replace the false one-slope near-rational payment by a uniform
  same-witness bound

Let `C=RS[F,D,K]`, where `|D|=n`, and let `m=K+w`. Assume

```text
w>=1,                    3w<=n-K.                    (NR1)
```

Fix a received line `u+zv`. Let `L` be any set of distinct finite slopes
such that, for every `z in L`, both of the following hold.

1. There are `c_z in C` and `eta_z in F^D` with

   ```text
   u+zv=c_z+eta_z,       wt(eta_z)<=w.               (NR2)
   ```

2. The slope has an actual support-wise MCA-bad witness: there are
   `S_z subset D`, `|S_z|=m`, and `h_z in C` such that `h_z=u+zv` on
   `S_z`, but no pair `c_0,c_1 in C` agrees with `(u,v)` simultaneously
   on that same `S_z`.

Then

```text
|L|<=2w.                                                (NR3)
```

Thus a near-rational stratum may be charged by `2w` distinct slopes. The
theorem does not delete the stratum, define a first-owner predicate, or
bound any complementary far-from-code stratum.
