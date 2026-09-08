# Proof By An Exhaustive Source Split And Uniform Record Costs

Put D=67466, R=1048576, d=67472, T0=180000000 and near=134944.
The source, carrier, labels and full-code-bad records are fixed first.

## 1. One Source Fiber Either Pays Or Bounds All Source Fibers

If any complete nonzero SOURCE projective fiber has size>=J-6000, the
required two-cost receiver-fiber theorem pays the WHOLE source, including
near, by266180883463176443. Its21000..52999 scope contains this interval.
Otherwise every nonzero source fiber has size<=J-6001. Let z be the
number of carrier-zero coordinates and put T=sum_i a_i(a_i-1), using all
nonzero source fibers. Root capacity gives z<=J-11. We do not cancel z.

Every LOW raw<=6 label has a fixed minimizing second polynomial in V and at
least m-6=J+D joint-core points. Choose any fixed M=J+D such points.
Their V-evaluations are nonzero: a carrier-zero joint-core point would
be universally satisfied, contradicting the source contract. They span
V* since M>J. The restriction's ordered same-fiber pairs are<=T, even
though its projective fibers may be smaller than those of the full source.

The required completed-basis count inserts an actual defect from the
original bad witness in twelve recoverable positions. Thus B ordered
core bases give at least12B original independent incidence tuples. This
uses the SAME explanation even for core points outside the original
chosen witness. Distinct labels own disjoint independent tuples.

## 2. Cover Every Core, Including Low Density And All Ten Ranks

Choose a maximum-density proper flat of this core, completed inside the
core and spanned by its points. Write its rank t, size a, and density h.
Then1<=t<=10, a=t*h, h>=1. Its annihilator has dimension11-t; division
by the full locator gives the integer bound

    t<=a<=J-11+t.

At t=1 also a<=J-6001, since a core fiber is a restriction of one SOURCE
fiber. There is no other maximum-density threshold or missing low-density
branch. All cores with any maximizing rank are covered below, including
the ranks that were separated in earlier proofs.

For one degree box J0..J1 and size box a0..a1, put

    M0=D+J0, h1=a1/t, ell=11-t, k1=J1-a0.

Use the original-rank hereditary profile mu_r calibrated for
(D,J0,J1,11,h1). Every proper core flat has density<=h1. The new
flat-split moment theorem gives the first-step lower cost

    beta(C)=12*M0*F_10(D,J0-q_C),
    q=min(h1,mu_11*(J1-1),
          [a1*h1+min((D+k1)*h1,Q(D+k1,k1,ell))]/M0),
    q_C=min(q,1+C/M0) when a uniform collision cap C is available.

Here Q is the proved full-fiber second-moment envelope (n^2 at rank one),
NOT a lower basis count. Without C use q. The SAME original profile
mu_3..mu_10 remains after the improved first step. We never recompute it
at the relaxed real argument. The actual quotient degree is>=ell and
the certificate verifies J0-q_C>=1 in every box.

The inside moment and outside quotient upper bounds apply to the ORIGINAL
fiber partition. In particular, quotient fibers need not themselves be
bounded by h1. Completeness makes their partition a coarsening, so its
moment upper bound still bounds the original outside moment. Every
numerator is bounded above using a1,k1,h1; divide by M>=M0. This is
whole-box monotonicity, not testing a few source parameter samples.

## 3. Retain The Previous Arbitrary-Flat Basis Count

For t<=5 a second cost can improve both source branches. Set

    k0=max(ell,J0-a1), k1=J1-a0,
    d_i=max(D+1+i,M0-floor((10-i)*a1/t)), 0<=i<t,
    c_i=floor(i*a1/t), 1<=i<t.

Every actual completion complement M-u_r is at least
max(D+11-r,M0-floor(r*a1/t)); the d_i are these bounds in reverse order.
They all exceed a1 because a1<23000<D+1. The required arbitrary-flat
theorem's signed tangent elimination therefore gives its positive BOX
inside factor I(d_i,a0,a1,c_i). Lower extension ratios are
max(a0-c_i,0), upper ratios are a1-i. A negative coefficient uses the
UPPER ratio, never the lower one. The independent audit reconstructs
and eliminates the entire tangent coefficient vector.

The quotient of this MAXIMIZING flat has proper-flat density<=h:
a rank-i quotient flat lifts to an original rank-(t+i) flat containing
all a=t*h points, so its outside size is<=i*h. The quotient greedy
bound on the box is

    G=(D+k0)*product_(i=1)^(ell-1)
          max(D+ell-i,D+k0-floor(i*a1/t)).

Take the maximum of G, the proved general quadratic bound, the
root-balanced product ONLY when its hereditary guard holds, and the
quotient rank-profile bound at density min(k1-ell+1,h1). These supply
a valid positive Q_basis. All quotient boxes have ell<=k0<=k1<D, within
the generic quadratic proof. The reused finite scripts implement those
generic formulas; their older narrow J payment is not invoked here.

Also retain the full-core greedy count and original-rank profile count.
The second record cost is therefore

    beta_old=12*max(Q_basis*I,
       M0*product_(r=1)^10 max(D+11-r,M0-floor(r*a1/t)),
       F_11(D,J0)).

Taking a maximum of lower counts for the SAME record is valid. The
certificate adds this cost only for t<=5 when either preliminary branch
cap exceeds274950000000000000. This deterministic calibration selects
valid lower counts; optimality of the tangent choices or trigger is not
a proof premise. No adaptive box splitting is used.

## 4. Low Collision Mass Improves Costs Without Removing Labels

If T<=T0, every LOW core has ordered same-fiber pairs<=T0. Use beta(T0),
increased to beta_old when selected. Retain ALL labels and the unfiltered
ordered-coordinate resource (R+J)_12. No secant exceptions are charged
in this branch. This uses a statistic of the fixed SOURCE to constrain
every core simultaneously, not a separate budget for each core.

## 5. High Collision Mass Reduces The Same Source Resource

If T>T0, use the required secant theorem's ONE exceptional label set E,
including nonuniversal carrier-zero agreeing labels and normalized
same-fiber secants. It has size<=z+T/2. Outside E every owned independent
tuple uses distinct nonzero source fibers.

For n0=R+J0,n1=R+J1,A=J1-6001, the Bonferroni theorem proves the
following whole-box upper resource:

    U=(n1)_12-66*T0*(n0-2)_10
      +660*(A-2)*T0*(n1-3)_9+1485*T0^2*(n1-4)_8.

The certificate verifies on EVERY degree box

    66(n0-2)(n0-3)>=660(A-2)(n1-3)+2970*n1*(A-1).

This makes the resource polynomial nonincreasing over the ENTIRE possible
collision range0<=T<=n(A-1), for every actual n in the box. Since T>T0,
its value at T0 bounds it above. Negative terms use n0 and positive
terms n1, which is the correct whole-box direction. Singleton padding of
carrier zeros only upper-bounds the resource; it adds no agreement points.
Charge the one conservative exception allowance

    E_box=J1-11+floor(n1*(A-1)/2).

Surviving LOW costs use beta without the collision cap, increased to
beta_old when selected. All geometry remains in the same actual enclosing
carrier; surviving explanations need not span it. Neither deleting labels
from the resource nor an auxiliary polynomial quotient changes its rank.

## 6. HIGH Records And Exhaustive Exact Arithmetic

The existing completed-basis weight gives every raw>=7 record at least

    beta_high=(d+J0)*product_(i=1)^10(d+i)*10488/125.

For7<=r<=84 use12r(1-11r/(d+1)); its derivative is positive on this
range and its value at seven exceeds10488/125. For r>=84 the truncated
mismatch weight is at least84, including r>d. This generic weight proof
does not require J>=23000. Outside E these same actual independent tuple
costs are retained. LOW and HIGH divide ONE resource by their minimum
cost, not one independent resource for each class.

Partition22500..22999 into consecutive width16 blocks, truncating the
last. For each rank t use top=J1-11+t, additionally min with J1-6001
at t=1. Partition ALL integers from t to top into consecutive bins of
width ceil((top-t+1)/128), truncating the last. These are an explicit
cover of every allowed actual (J,t,a), including any maximizing flat.
Each tested box is an analytic bound on every parameter in it.

For its two final LOW costs beta_S,beta_L, the exact caps are

    floor((n1)_12/min(beta_S,beta_high))+near,
    floor(U/min(beta_L,beta_high))+E_box+near.

Both independent implementations check32 degree blocks,40960 size/rank
boxes (4096 per rank), both source branches and163840 adjacent wrong
floors. They agree on every rational cost and cap, with digest
5ace68871be07e08317ea359ac9a73f80c7a9b9a325e5390a0d6e66b9ecdc5a2.
The maximum is274938028871508001 in the low-T branch on
(J0,J1,t,a0,a1)=(22628,22643,5,18059,18235). This is a certificate
maximum, not an actual extremal received line or proof of optimality.
The separately paid large-source-fiber branch is smaller, so PAYMENT
follows with no remaining source premise on this entire J interval.

## 7. Original Scope

The number134944 is the single allowance reserved for original near in
the existing source assembly. Nothing here assumes the normalized source
is itself post-near. Adding this allowance in every alternative cap and
taking their maximum does not add it repeatedly. The union with
23000..169999 must now use274938028871508001, not its older smaller cap.
Original normalization transports the new interval to complete shared
cores1025577..1026076. Its source assembly verifies that step separately.
No arbitrary-source rank bound, remaining-gap theorem or full Prize
resolution is asserted. The structural rational atlas motivated further
work but is not used as a requirement in this proof.
