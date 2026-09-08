# Proof

If `|L|<=1`, then `(NR3)` follows from `w>=1`. Otherwise choose distinct
anchors `z_0,z_1 in L` and write their decompositions as in `(NR2)`. Define

```text
c_v=(c_(z_1)-c_(z_0))/(z_1-z_0),
c_u=c_(z_0)-z_0 c_v,
e_v=v-c_v=(eta_(z_1)-eta_(z_0))/(z_1-z_0),
e_u=u-c_u=eta_(z_0)-z_0 e_v.
```

Linearity gives `c_u,c_v in C`, and

```text
E=supp(e_u) union supp(e_v)
  subseteq supp(eta_(z_0)) union supp(eta_(z_1)),
|E|<=2w.                                                (1)
```

For any `z in L`, the vector

```text
Delta_z=c_z-(c_u+z c_v)=e_u+z e_v-eta_z
```

is a codeword supported on at most `3w` coordinates. A nonzero word in the
`[n,K]` Reed-Solomon code has weight at least `n-K+1`. The guard `(NR1)`
therefore forces `Delta_z=0`, so

```text
eta_z=e_u+z e_v.                                       (2)
```

Now use the actual bad witness `(S_z,h_z)`. On
`S_z\supp(eta_z)`, the two degree-below-`K` polynomials `h_z` and `c_z`
agree. This set has size at least

```text
|S_z|-wt(eta_z)>=K+w-w=K,
```

so Reed-Solomon root counting gives `h_z=c_z`. Since `h_z=u+zv` on all of
`S_z`, equations `(NR2)` and `(2)` now give

```text
e_u(x)+z e_v(x)=0             for every x in S_z.     (3)
```

The same-support MCA noncontainment says that `(c_u,c_v)` cannot explain
`(u,v)` on `S_z`. Hence some `x in S_z` has
`(e_u(x),e_v(x))!=(0,0)`. Equation `(3)` then forces `e_v(x)!=0` and

```text
z=-e_u(x)/e_v(x).                                     (4)
```

Every slope in `L` is therefore one of the coordinate ratios `(4)` arising
from `x in E`. Each coordinate contributes at most one slope, and `(1)`
gives `|E|<=2w`. This proves `(NR3)`.
