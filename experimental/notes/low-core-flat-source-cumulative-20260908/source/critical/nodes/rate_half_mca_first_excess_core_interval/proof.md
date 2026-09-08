# Proof By Core-Local Density And A First Excess Flat

Write D=67466 and M=J+D. All raw margins and minimizing pairs below
are fixed AFTER normalization on the same dimension-eleven source.

## 1. Whole-Source Fiber Gate And Raw Record Costs

If any complete nonzero SOURCE projective fiber has size >=J-2000,
the required receiver-fiber theorem pays the whole source by
248408859318207582 including original near. Otherwise every rank-one
flat in any nonzero core subset has <=J-2001 coordinates.

For raw<=6 choose one M-point subset H of the complete minimizing-pair
joint core. Its evaluations are nonzero by empty universal carrier core,
and polynomial roots give actual rank eleven. The existing defect-insertion
resource supplies twelve independent incidence tuples per counted basis.
Different original finite labels have disjoint tuple sets, even when these
tuples use complete-core points outside the old selected witness.

Every raw-HIGH record raw>=7 retains cost
(d+J)*P_d*10488/125. This uses only the earlier proved weight arithmetic,
NOT the earlier source-density premise. Raw-HIGH is distinct from the
high-core-density case below.

## 2. Two Exhaustive Geometric Cases For Each LOW Core

Let h_H be the maximum proper-flat COORDINATE density on H alone,
and set H0(J)=(J-5)/6.

If h_H<=H0, a basis-rich core uses 12*P_11(D,J). Otherwise the required
first-excess theorem gives a least rank t with b>M/(11-t) coordinates.
All rank-r flats with r<t have at most floor(M/(11-r)) coordinates.
Root capacity gives b<=J-11+t; t=8,9 are impossible here because they
would require (10-t)J>D+(11-t)^2. Thus t<=7. All proper rank-r caps are

    c_r(J)=min(J-11+r, floor(r*(J-5)/6),
               floor((J+D)/(11-r)) when r<t).

The chosen G is complete inside H, not necessarily in the whole source,
and has exactly b core coordinates. It need not maximize density.

If h_H>H0, choose a maximizing core flat of rank t with b=t*h_H points.
The root bound h_H<=1+(J-11)/t excludes t>=6, so 1<=t<=5 and

    b>=floor(t*(J-5)/6)+1, b<=J-11+t.

At t=1 also b<=J-2001 by the original whole-source fiber split.
All core rank-r counts are bounded by min(J-11+r,floor(r*b/t)).
The chosen core flat has its FULL b-point occupancy, not an assumed
favorable intersection with a globally maximizing source flat.

## 3. Quotient Counts And Rank-Specific Tangents

Apply the arbitrary-core-flat supplier in both cases. Put ell=11-t.
The quotient has actual degree k=J-b>=ell, length D+k and gap D.
Its greedy count comes from the proved proper-rank caps. Also use the
downward-rounded quadratic certificate proved in the quotient-density
supplier: at rank ell, gap D, ell<=k0<=k<=k1<=D it gives Q_quad(k0).
Only that general certificate construction and its verified coefficient,
spike and tangent gates are used, not the parent's old finite J interval.

Set f=floor(ell^2/4). If (f-1)k1<=D+f(ell-1), the polynomial root cap
bounds quotient density by k-ell+1 and f(k-ell+1)<=D+k for ALL k in
the hull. The proved balanced-basis theorem gives P_ell(D,k), so
P_ell(D,k0) is another lower count. Take the MAXIMUM of valid quotient
counts, never their sum; the unqualified balanced product is not assumed.

The arbitrary-flat BOX theorem allows one independent tangent q_i for
each inside rank i. With lower d_v, size interval b0..b1 and upper caps c_i,
write L_i=max(b0-c_i,0), U_i=b1-i. Starting A_t=binom(11,t), for
i=t-1,...,1 choose ANY integer q_i in [L_i,U_i] and set

    T=A_(i+1)-binom(11,i)*D_(t-i)(q_i),
    A_i=binom(11,i)*[R_(t-i)(q_i)+q_i*D_(t-i)(q_i)]
          +T*(L_i if T>=0 else U_i).

Here R_k is the product of d_v-y and D_k=-R_k'. The inner lower count is
max(R_t(b1), R_t(b1)+A_1*(b0 if A_1>=0 else b1)).
This is the existing signed telescoping formula regrouped backwards.

The certificate chooses q_i by integer bisection of the nondecreasing T,
then takes the better of the two bracketing integers. All selected points
lie in the required interval and below every d_v. Optimality is NOT needed:
each selected tangent is valid. The independent audit reconstructs all
coefficients from the selected points and eliminates the full coefficient
vector again. Negative coefficients never use lower extension ratios.

## 4. Complete Parameter Boxes

Use consecutive degree blocks J0..J1 of width 32 from 28000 to29999,
truncating the last. Their upper endpoint gives U=(R+J1)_falling_12.
Basis-rich LOW and raw-HIGH costs use J0.

In the lower-density case, all actual sizes are enclosed by

    bmin=floor((J0+D)/(11-t))+1,
    bmax=min(J1-11+t,floor(t*(J1-5)/6)).

Partition into at most 128 consecutive bins; for t>=6 and J0<28256 use
256 bins. Empty ranges contribute nothing. All c_r(J) are nondecreasing,
and all J+D-c_r(J) are nondecreasing. For r<=5 this follows from the
increment of floor(r*(J-5)/6) being <=1. At r>=6 the polynomial root
branch dominates that density cap, giving constant root complements;
any additional first-excess complement M-floor(M/(11-r)) is nondecreasing.
Thus d_v uses J0 and inside caps use J1. The quotient hull is
k0=max(ell,J0-b1), k1=J1-b0. The clipping uses the actual quotient rank,
not a presumed fractional-degree source. Its greedy lower count uses
(D+J0-b1)*product_(i=1)^(ell-1)(D+J0-c_(t+i)(J0)).

In the higher-density case use quotient degree as the box coordinate.
All actual k lie between ell (2001 for t=1) and
J1-floor(t*(J1-5)/6)-1. Start with at most 64 equal-width integer bins.
Insert the root-balanced threshold floor((D+f*(ell-1))/(f-1))+1, and
for t=1 insert 2001,2033,...,2481 to retain the large-fiber endpoint.

For a degree bin k0..k1 set b0=J0-k1,b1=J1-k0. Since t<=5 and every
completion rank r>=11-t exceeds t, J+D-floor(r*(J-k)/t) is nonincreasing
in J and nondecreasing in k. Hence

    d_i^low=max(D+1+i,D+J1-floor((10-i)*b1/t)),
    c_i^upper=floor(i*b1/t).

The quotient greedy lower count is
(D+k0)*product_(i=1)^(ell-1)max(D+ell-i,D+k0-floor(i*b1/t)).
These are uniform corner bounds, not evaluations used as samples.

All boxes check rank/degree gates and positive factors. They cover every
core, every permitted first-excess or maximizing rank and every integer
size. A record with several suitable flats is counted ONCE. Divide the
ONE resource by the smallest record cost; combine source alternatives
by maximum and add the original near allowance once.

## 5. Finite Total And Original Source

The exact certificates check all 63312 parameter boxes and 63 basic
record comparisons. Their maximum is 273019482620216244 at
J=28000..28031, high core density, rank one, quotient degree 2001..2032.
The separately paid source-fiber class is smaller and included in the
maximum. The previous refined interval pays 30000..169999; the union
retains 274929007493481160.

The original assembly supplies the same-field, full-code-bad, original-label
transport. This removes 2000 complete original degrees, not just a source
subclass, leaving 9941..27999. No auxiliary quotient changes the received
word, discards exceptions or redefines the challenge numerator. Smaller
degrees, original ranks >=13, unrestricted MCA and ordinary LIST remain open.
