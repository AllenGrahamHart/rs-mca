# Raw-weighted accounting pays every cubic at cutoff 125

Status: PROVED restricted source theorem. Use this node's EXACT canonical
normalized source, 9822<=J<=9940. The raw margins and carrier are unchanged;
only the accounting cutoff becomes T=125. Suppose all but <=256 LOW_125
pairs lie on one irreducible cubic of primitive weighted degree
<2*(J+67347) for weights (1,J-1,J-1). Then

    N=|Gamma|+134944<=274811931500367244,
    B=274980728111395087, reserve>=168796611027843.    (RW125)

This file pays the curve class. The full-kernel child supplies its own
exhaustive cover and reducible-factor accounting, with no reverse dependency.

## 1. Restrict the actual resource, not the source

The completed-basis supplier gives sum w<=F(J), with

    F(J)=(1048576+J)_falling_12
          / ((67472+J)*prod_(i=1)^10(67472+i)).

As in the earlier seven-margin proof, F is convex: on writing y=J+67472
its numerator is a product of twelve factors y+c_i with c_i>0; division
by y leaves a positive combination of nonnegative powers and 1/y.
Endpoint ceilings on the new interval are

    ceil F(9822)=13062473626374413737,
    ceil F(9940)=13060022408459260015.

Use C125=13062473626374413737. The completed-basis supplier already
proves w(r)>=11*min(r,500) for EVERY raw margin. Therefore its exact
raw-weighted conversion gives, on the SAME selected source,

    N<=floor(C125/1375
         +sum_(t=1)^124 S_t/[t*(t+1)])+134944,         (1)

where S_t is the sum of raw margins of labels with raw<=t.
There is no re-selection or mixing of margins from different sources.

The complete-core disjointness proof in the homogeneous-level supplier
bounds S_t by (n-m+t) times the number of represented pairs at that depth.
A raw-r label uses r distinct defect points, not just one. In particular,
if M bounds ALL LOW_125 pairs, the simpler direct conversion is

    N<=base+981229*M, base=C125//1375+134944
                            =9499980819316335.        (2)

This drops the LOW contribution from the same resource and pays every
LOW label at most once. M must include all exceptional pairs.

## 2. A general weighted-chord conversion

For T>=3, suppose S_t<=f(t) and f is increasing and convex on [1,T-1].
The chord and exact telescoping sums give

    sum_(t=1)^(T-1) S_t/[t*(t+1)]
      <=(1-1/T)*f(1)
        +[H_(T-1)-2+2/T]*(f(T-1)-f(1))/(T-2),         (3)
    H_k=sum_(t=1)^k 1/t.

Indeed the two weights sum to 1-1/T and
sum (t-1)/[t*(t+1)]=H_(T-1)-2+2/T. This is the actual raw budget
on one source, not an extrapolated per-pair label count.

For T=125, H_124<=6 has a short hand proof. On each dyadic block
m..2m-1 with m=2,4,8,16,32,64, convexity of 1/x bounds the sum by
m*(1/m+1/(2m-1))/2<=5/6. Add the initial term 1 to obtain
H_124<=H_127<=1+6*(5/6)=6.

## 3. The d=7 low-height source

For projection-kernel dimension d=7 and h<=1550, the weighted cubic
supplier, at actual agreement m-t and input degree <J+h, gives

    M_t<=2^7*3^12*((1048577-h)/(67473-t-h))^3.

All components and singular solutions are included. The ratio increases
with h, and the same 256 exceptions cover every nested subset. Thus use

    f(t)=(981104+t)*(2^7*3^12*(1047027/(65923-t))^3+256).

The second derivative of (b+t)/(q-t)^3 is
6/(q-t)^4+12*(b+t)/(q-t)^5>0; the exception term is linear.
The function also increases, so replacing H_124 by 6 in (3) is valid.
The resulting exact rational bound is

    floor(C125/1375+(124/125)*f(1)
          +(502/15375)*(f(124)-f(1)))+134944
       =274811931500367244.                           (4)

The two endpoint denominators are 65922 and 65799. The raw-margin
sum, full per-pair defect budget, resource and near are each used once.

## 4. Every other irreducible cubic type

The generic geometric classification is unchanged. Smooth cubics and
rational multi-boundary cubics have the existing LOW_500 pair cap
163774741769, which also counts their LOW_125 subset. A nongeometric
irreducible cubic has at most six rational pairs.

A one-boundary cubic singular at infinity is a polynomial cubic projection.
Its ACTUAL factor weight gives

    h<=floor((2*(J+67347)-1-3*(J-1))/3)
      =floor((134696-J)/3)<=41624<51391.

The previously proved height-51391 cap 223154201664 applies, even at the
weaker LOW_500 agreement. Both types pay by (2), with 256 exceptions.

For affine-singular one-boundary cubics, put r=ceil(d/3). At cutoff 125,

    M<=floor(2^d*3^(22-d-r)*((1048577-h)/(67348-h))^r).

For 1<=d<11 use h<=9939/floor(10/(11-d)); for d=11 use h=0.
At d=0 the direct zero-dimensional cap is 3^22. Every d outside
{7,10} pays by (2); the largest such total is 267756687104005804
at d=11, including 256 exceptions.

For d=7,h>=1551, the component supplier's cutoff125.md gives

    N<=base+981229*(4225*3^16+57119482443+1+256)
      =244005743185015160.

For d=10, the GP supplier's cutoff125.md gives

    N<=base+981229*(79311626937+256)
      =87322849458276532.

These exhaust every irreducible cubic. Combine the complete whole-source
alternatives by MAXIMUM, obtaining (RW125). No new source hypothesis,
normal-form guess, receiver descent or finite-field scan is used.
