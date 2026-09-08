# Cumulative LOW weights pay d=7 through height 1600

Status: PROVED restricted source payment. Keep this consumer's exact
canonical normalized source, LOW_500, 4801<=J<=169999. Suppose all
but <=256 LOW pairs lie on one affine-singular one-boundary cubic
whose actual projection-kernel dimension is d=7 and primitive height
h<=1600. Then

    N=|Gamma|+134944<=274778805314695460,
    reserve>=201922796699627.                         (CL7)

All coefficient components, singular pairs, original scalar defects and
finite labels are retained. This theorem does not assume such a cover
for arbitrary sources.

## 1. Bound every cumulative count on the fixed source

The required completed-basis supplier's cumulative_low_weights.md gives

    |Gamma|<=floor(C/5500+(1/500)*sum_(t=1)^499 L_t),
    C=23067643444721720934.

For any fixed t, a raw<=t record has a complete joint core of size
at least m-t. A fixed represented pair has at most n-m+t=981104+t
such finite labels, because their nonempty defects are disjoint outside
its OWN complete core. No support is reselected as t changes.

The weighted cubic supplier applies to the same whole coefficient locus,
of dimension <=ceil(7/3)=3, at joint agreement m-t. It gives

    M_t<=2^7*3^12*((1048577-h)/(67473-t-h))^3.

The parameter degree is really <J+h. The denominator is positive and
the ratio is >=3 in this range. The same 256 off-curve pairs suffice
for every nested subset, so

    L_t<=(981104+t)*(M_t+256).                         (1)

This counts all singular and isolated coefficient solutions, not only
top-dimensional families.

## 2. A two-endpoint convex bound replaces a large sum

The ratio increases with h, so replace h by 1600. Put

    F(t)=(981104+t)*2^7*3^12*(1046977/(65873-t))^3.

It is convex on 1<=t<=499: the second derivative of
(b+t)/(q-t)^3 is 6/(q-t)^4+12*(b+t)/(q-t)^5>0.
Each integer point lies below the chord through 1 and 499. Summing
the chord, whose average is the average of its endpoint values, gives

    (1/500)*sum_(t=1)^499 F(t)
        <=(499/1000)*(F(1)+F(499)).                   (2)

The exception term sums exactly to (499/500)*256*981354. Thus

    N<=floor(C/5500+(499/1000)*(F(1)+F(499))
             +(499/500)*256*981354)+134944
      =274778805314695460.

The exact endpoint denominators are 65872 and 65374. All resource
weights and cumulative counts refer to the same raw margins and source.
The original near is added once. Treating every LOW label as having
only the minimum weight, or charging every pair at t=500, loses this
payment; no previously discounted expression has been reused.

## 3. Retain the per-pair raw defect budget when useful

Section 4 of the already required homogeneous-level supplier's proof
gives a stronger cumulative bound on the SAME source. For a fixed
pair, the mismatch sets of its assigned labels are disjoint outside its
own complete core. A raw-r label uses r such points. Consequently

    S_t=sum_(gamma:raw<=t) raw <=(981104+t)*(M_t+256).

Unlike (1), this bounds the SUM OF RAW MARGINS, not just the number
of labels. Use the completed-basis supplier's equivalent raw-weighted
conversion to get the stronger optional expression

    N<=floor(C/5500
         +sum_(t=1)^499 (981104+t)*(M_t+256)/(t*(t+1)))+134944. (3)

No factor of t is inserted in the numerator: defect disjointness already
bounds the total raw per pair by its available complement. The exact
telescoping weights are recomputed for T=500, not copied from the old
/501 resource. The primary (CL7) proof above does not require this
refinement. Equation (3) is also valid for other height envelopes where
the same weighted pair bound and agreement-degree guards hold; further
numerical source coverage must be checked at its actual parameters.
