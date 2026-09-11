# The Coarse Guard Does Not Yet Fit The Original Allowances

The guarded anchor inequality is proved in anchor_guard.md. Its additional
exceptional-coordinate charge is not free. The small guard_prices.py
diagnostic tests the recipe of using that coarse geometric envelope once,
at the LAST anchor, while leaving the first seven anchor factors unchanged.

At a profile endpoint J1 take the permitted degree-envelope parameters

    prefix shared dimension4, pair dimension5,
    image degree d_image=J1-8, normalization degree1,
    H=floor((J1-1)/10), h=H+1.

These parameters define a test of the proposed uniform bound, not a
realized official MCA source. The branch supplier gives

    b_geo=floor(binom(d_image-2,2)/(2H-1)).

At the last original anchor, n-B_reg=1048577 and A-B_reg=67473-t.
Replace only its factor by

    (1048577-b_geo)/(67473-t-b_geo).

All denominators stay positive. With the SAME L_1,L_2 and original
mass/near terms, the resulting available-weight price exceeds B* on
EVERY one of the13 profiles:

| Original J profile | H | b_geo | Resulting recipe price |
| --- | ---: | ---: | ---: |
| 9965..10964 | 1096 | 27380 | 287653690518906432 |
| 20965..21499 | 2149 | 53730 | 711653815961044142 |

The minimum over all profiles is287653690518906432, above
B*=274980728111395087. The diagnostic uses thirteen small exact rational
calculations, not a finite-field scan.

This does NOT show the actual exceptional set is that large, that any
anchor necessarily incurs this cost, or that the Prize bound is false.
It shows the coarse geometric upper bound cannot simply be inserted in
the current uniform-allowance recipe. Original-source overlap, a weighted
distribution of child costs, or a sharper exceptional-centre theorem
could still improve it. Generic birationality by itself cannot.
