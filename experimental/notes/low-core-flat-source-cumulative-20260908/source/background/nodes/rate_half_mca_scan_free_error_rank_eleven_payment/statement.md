# Scan-free payment through affine error rank eleven

Status: PROVED. Strengthened 2026-09-07 by padded Johnson/scalar descent.
Constants: R=1048576, d=67472, U_1=4070947 and
`U_s=floor((R+s)*U_(s-1)/(d+s))` for 2<=s<=11.

## Uniform shortened-family theorem

For every `1<=s<=11`, every `1<=K<=R`, and every finite-field RS row
`(n,K,m)=(R+K,K,d+K)`, consider one received pair and one explanation
with an exact same-support pair-noncontained m-record for each distinct
finite slope in Z. If all explanations lie in an affine polynomial
subspace of dimension at most s, then

```text
|Z|<=U_s.
```

In particular, at explanation dimension at most ten,

```text
|Z|<=215108323408189165.
```

## Stronger caps when the original field permits padding

When |F|>=2097152, the required padded-Johnson compiler gives the
stronger simultaneous caps V_9=10755802499540570 and
V_10=156765527508668296 on every shortened degree K. The original
U_s above remain valid without this additional field-size gate. The new
compiler uses seven fixed certificates, not a degree-indexed numerical scan.

## Direct KoalaBear application

On the deployed KoalaBear row over `F_(2130706433^6)`, let

```text
n=2097152,   K=1048576,   m=1116048,
B_*=274980728111395087,
N={support-wise bad slopes at distance <=d from the code},
Z=Z_bad\N.
```

Suppose there is a selection of one exact bad witness per slope in Z
whose error words `e_gamma=r_0+gamma*r_1-h_gamma` have affine rank at
most eleven. Then

```text
|Z_bad| <=156765527508803240 < B_*.
```

Thus any over-budget received line must have error affine rank at least
twelve for EVERY such complete post-near selection. This is not a claim
that arbitrary lines have rank at most eleven, a payment of rank twelve,
or an active-v4 owner/ledger theorem. The slack is 118215200602591847.
The KoalaBear field and all unchanged-field children satisfy the padding
gate. The older scalar-only and raw-low proofs remain valid alternatives
with weaker constants. No optimized #1174 table is required. Even the
new V_11=2283382040940633027 is over budget.
