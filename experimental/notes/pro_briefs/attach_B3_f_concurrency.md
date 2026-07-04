# f_concurrency_equiv proof

Let an `r`-flat `P` be parametrized by coordinates `t`. For each domain point
`x in H`, evaluation at `x` is a linear functional on the locator coefficients.
Its pullback to the parameter space is a hyperplane

```text
H_x = { t : P(t)(x) = 0 }.
```

A member `P(t)` has root `x` exactly when `t in H_x`. Therefore `P(t)` has at
least `j` roots in the evaluation domain exactly when `t` lies on at least `j`
of the hyperplanes `{H_x : x in H}`.

The only conventional adjustment is the leading-coefficient hyperplane, which
accounts for projective or affine chart choices. It does not change the
equivalence of root count and hyperplane concurrency.

Thus `P cap D_j` is exactly the locus of `j`-fold concurrency points in the
evaluation-hyperplane arrangement, with tangent/common-divisor shapes
corresponding to flats near the intersections defining multiples of shared
root locators and periodic shapes corresponding to pullback subarrangements.
