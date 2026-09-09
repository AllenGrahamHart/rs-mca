# Proof: A Truncated-Raw Budget Forces High-Rank Low-Defect Mass

## 1. Eight Universal Quadratic Certificates

Set D=67347=d-125,E=21499,X=5000 and
P_r=product_(i=1)^(r-1)(D+i). We prove at each rank3<=r<=11 a
universal core-basis bound P_r*q_r(K) for r<=K<=E, with

    q_r(K)=a_r+b_r*K+c*K^2, c=1/[2(D+2)].

The required contraction theorem's rank-three seed gives
a_3=D(2D+1)c,b_3=(3D+1)c. Its quadratic step has the following
normalized branches at rank r, using the previous a,b and H=D+r-1:

    alpha=(r-2)/(r-1), delta=1/(r-1), f=q_(r-1)(r-1),
    S(K)=s0+s1*K+c*K^2,
    s1=b-2c+f/H, s0=a-b+c-(r-1)f/H,
    U(K)=(D+K)*q_(r-1)(alpha*K+delta)/H.

Write U=u0+u1*K+u2*K^2+u3*K^3. Then

    u3=c*alpha^2/H,
    u2=(b*alpha+2c*alpha*delta+D*c*alpha^2)/H,
    u1=(a+b*delta+c*delta^2+D*(b*alpha+2c*alpha*delta))/H,
    u0=D*(a+b*delta+c*delta^2)/H.

Use the fixed tangent

    t1=u1+2(u2-c)X+3u3*X^2,
    t0=u0-(u2-c)X^2-2u3*X^3,
    eta=max(0,t0+t1*r-s0-s1*r,t0+t1*E-s0-s1*E),
    a_r=t0-eta, b_r=t1.

All eight exact certificates have b>=D*c,u2>=c,u3>=0 and b_r>=D*c.
The difference S-q_r is affine and nonnegative at both r and E.
For the other branch the EXACT identity is

    U(K)-q_r(K)
      =eta+(K-X)^2*((u2-c)+u3*(K+2X))>=0 on K>=0.

Thus q_r lies below both branches on the whole required interval, and
the generic contraction theorem proves the next-rank bound. No source
maximizer, fitted degree interpolation or experimental premise enters.
All final coefficients are positive. The recurrence fixes them exactly;
rounded printed coefficients are not proof inputs.

## 2. One Budget For All Raw Values

Write q=q_11,P=P_11 and beta(J)=12*P*q(J). Apply the required raw-mass
theorem with T=125,kappa=4 and B=P*q(J). Each raw<=125 record has at
least m-125=D+J nonzero joint-core evaluations; dimension and degree are actual.

Let P_d=product_(i=1)^10(d+i). The all-raw HIGH gate is

    126*(d+J)*P_d >=4*beta(J).

It holds throughout9941..21499. Indeed q(J)/(d+J) is increasing since

    (d+J)q'(J)-q(J)=d*b-a+2*d*c*J+c*J^2>0,

and d*b>=a is certified exactly. It suffices to check the displayed
inequality at E=21499; that exact rational check passes. This covers
raw>=126, including raw>d, not just the finite LOW range.

Consequently

    sum min(raw_gamma,4)<=floor Q(J),
    Q(J)=(1048576+J)_falling_12 /[12*P*q(J)].

Put L=9941. The exact certificate gives

    (b+2*c*L)*(1048576+L-11)>12*q(E).

Since q is positive increasing, this makes its logarithmic derivative
strictly larger than that of the falling numerator throughout[L,E].
Thus Q(J) is decreasing on the ENTIRE real interval. Exact divisions give

    floor Q(9941)=624373932788019251=W0,
    floor Q(14000)=522680876725222604=W1.

This proves(W), including the smaller upper-range constant. Nonuniversal
carrier zeros were not removed: a joint-core point at such a zero would
belong to the empty universal core. No source-fiber gate is used.

## 3. Actual Graph Flats Have Credited Label Caps

Any actual parameter subset of affine dimension a<=11, with at least
two distinct labels, has difference space E' with slope projection rank1.
Choose(1,b0) in E'. The gauge v'=v-b0,h'_gamma=h_gamma-gamma*b0
lowers the explanation dimension to at most a-1, preserving every label,
row and full-code-bad support. This is precisely the fixed-subset argument
of the required parameter-graph theorem, now also at dimension a<=10.

The required padded caps therefore give

    dim G_t<=11 -> |G_t|<=V10=156765527508668296;
    dim G_t<=10 -> |G_t|<=V9 = 10755802499540570.

Empty and singleton subsets trivially obey both bounds. These are counts
of actual original labels; different flat gauges are NOT freely summed.

## 4. Price The Low-Raw Classes Or Force Their Mass

Let N=|Gamma| and L_t=|G_t|. The raw-mass theorem gives

    (t+1)*N-t*L_t<=W0 for t=1,2,3.

If L_2=0, N<=floor(W0/3). If dim G_2<=10, N<=floor((W0+2V9)/3).
If dim G_3<=11, N<=floor((W0+3V10)/4). Add original near134944 ONCE.
The three exact totals are208124644262808027,215295179262501741,
and273667628828640978. All are below B*. For J>=14000, dim G_1<=10
likewise gives floor((W1+V9)/2)+134944<B*.

The sharper FLAG identity gives3N-L_1-L_2<=W0. If dim G_1<=10 and
dim G_2<=11, it pays the whole line by floor((W0+V9+V10)/3)+134944<B*,
regardless of the dimension of G_3. This does not require low-raw sets
to be disjoint or a separately charged hyperplane cover.

Conversely, an over-budget original line has

    N>=N_min=B*-134944+1=274980728111260144.

Taking the integer ceilings in TAIL yields

    L_2>=ceil((3N_min-W0)/2)=100284125772880591>V9,
    L_3>=ceil((4N_min-W0)/3)=158516326552340442>V10.

These strict inequalities prove the asserted actual graph ranks. For
J>=14000, L_1>=2N_min-W1=27280579497297684>V9. Projecting a graph to
its h-coordinate can lower affine dimension by at most one, proving the
corresponding explanation-span assertions.

The nested identity also gives L_1+L_2>=3N_min-W0=200568251545761181.
If dim G_1<=10, then L_1<=V9 and L_2>=189812449046220611>V10,
forcing dim G_2=12. If dim G_2<=11, then L_2<=V10 and
L_1>=43802724037092885>V9, forcing dim G_1>=11. This is the mixed
rank alternative, not a new assumption on an arbitrary received line.

All these arguments hold for ANY valid selection in the fixed carrier.
Choose the required maximum-raw selection and use its complete-core
theorem with T=3, since2T<d. The raw<=3 labels have their unique minimizer
on the complete scalar agreement set, with exactly the recorded raw defects.
The same conclusion applies to raw<=1 and raw<=2 subsets. This is an
actual low-defect reduction, not a premise asserting a convenient selection.

For a fixed represented pair f=(a,b), its complete joint core H_f has
size at least m-2 for raw<=2 owners. Each owned bad label needs a scalar
agreement outside H_f. At an outside point the equation
(u-a)+gamma*(v-b)=0 determines at most one gamma. Hence that pair owns
at most n-|H_f|<=981106 labels. Since981106*10^11<100284125772880591,
more than10^11 distinct pairs are represented. A common joint core of
size>=m-2>=J determines the full degree<J pair uniquely, so these also
have distinct complete joint cores. No pair-to-label projection is free.

For a valid selection after deletion of e labels, extend it arbitrarily
to valid records on all of Gamma. Apply the uniform mass theorem and then
remove those e records. Each low-raw population falls by at most e.
The existing E_max=1149710068 is smaller than each strict population
margin over V9 or V10 above, so the stated rank bounds survive it.

## 5. Source-Owned Complete-Pair Census

The owner ledger gives a concrete remaining census.
Put Delta=sum_(raw<=3)(4-raw). Exactly4N-Delta is the
truncated-four mass, so4N<=W0+Delta. For a fixed represented pair with
|H|>=m-1, OWNER bounds its deficit by3(n-m+1)=2943315. For|H|=m-2,
it gives n-m+2=981106. For|H|=m-3, it gives
floor((n-m+3)/3)=327035. Therefore

    Delta<=2943315*M1+981106*M2+327035*M3.

The exact sufficient integer ceiling is4*(B*-near+1)-W0-1
=475548979657021324. Under that ceiling,4N<=4*(B*-near)+3 and
integrality yields N+near<=B*. An over-budget line has the opposite
lower threshold475548979657021325. This is a rigorous reduction to a
source-owned weighted complete-pair census, not its asserted solution.

## Scope And Provenance

The eight-step quadratic method, incidence ownership, rank gauge, padded
caps, canonical complete-core selection and original normalization are
credited suppliers. The new finite application changes the core gap to
d-125, restricts its degree ceiling to21499, retains all raw multiplicities,
and combines the resulting mass with actual graph-flat caps.

There is still no census of the full-rank one/two/three-defect families.
Those families may exist; the theorem does not assert a contradiction.
No entire degree interval, higher original rank, unrestricted threshold,
LIST endpoint or Prize problem closes. This is a proved source-class
payment and a sharper necessary structure for any over-budget source.
