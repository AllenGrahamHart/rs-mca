# Bounded row remainders force an affordable global margin

Current continuation: [seven_margin_payment.md](seven_margin_payment.md)
weakens the remainder ceiling to m-7 on the remaining 4801..169999
interval, using the full proved basis weights. The proof below retains
its older m-139 ceiling on the wider 4801..254999 interval and is still
valid. Its core-ceiling and cancellation arguments are reused unchanged.

Status: PROVED. This extends the remainder allowance while retaining
the SAME normalized KoalaBear row, actual carrier dimension eleven,
empty universal carrier core and complete raw<=500 union U.

Set m=J+67472, ell=66972, A=m-500. Suppose some NONZERO polynomial
row R=(R_0,R_1), deg R_i<=ell, has received remainder

    Q=rem_(P_U)(R_0*u+R_1*v), deg Q<=m-139.            (BR)

Then the whole original finite bad-slope set is paid, with original
near-inclusive bound

    total <=274482706723995445 <274980728111395087,
    reserve =498021387399642.                          (PAY)

No subfield-valuedness hypothesis is imposed on R, Q or the receiver.
The older nonzero-relation case deg Q<A retains its sharper bound.
The new degree band is A<=deg Q<=m-139, comprising 362 additional
integer remainder degrees. It is a source-class extension, not a proof
that every remaining zero/cyclic row-space source satisfies (BR).

## 1. General core-ceiling lemma

For any actual low minimizing pair f=(a,b), its complete core H_f
has at least A=m-T points and is included in the low-core union U.
If deg R_i<=d-T and Q agrees with R*y on U, then

    deg(R*f)<m-T=A.

When deg Q=D>=A, the polynomial R*f-Q is NONZERO of degree D.
It vanishes on H_f. Therefore |H_f|<=D and

    raw_gamma=|S_gamma minus H_f|>=m-D.                 (GAP)

This holds for every represented low pair, not just pairs in one fiber
of the row-image map. If instead deg Q<A, no margin floor follows:
the polynomial can be identically zero, and the exact-relation theorem
is the appropriate branch. In particular a small scalar LIST bound for
the row images is not needed for (GAP).

## 2. Exact finite payment

Small/empty unions retain their existing bound. If deg Q<A, this node's
previous relation theorem applies and gives total <=255637082864553899.
Otherwise (BR) and (GAP) give raw>=139 for every low label. Every high
label has raw>=501 anyway. Thus ALL selected post-near labels satisfy
theta=min(d+1,raw)>=139. The original empty-core resource gives

    139*|Gamma| <= sum theta <=F(J),
    F(J)=(R+J)_falling_12 / ((d+J)*product_(i=1)^10(d+i)),
    R=1048576, d=67472.

The already printed positive-coefficient convexity proof bounds F(J)
over J=4801..254999 by its two endpoints. Their ceilings are

    13195104981505077258, 38153096234616609717.

Using the larger integer ceiling C and adding only the original near
charge 134944 gives floor(C/139)+134944, which is (PAY). The same
uniform resource with margin 138 does not meet the budget; this is a
failure of that numerical recipe, not an unsafe witness at margin 138.

The source outside U is arbitrary. All high labels were included in the
same resource, and no independent image-fiber upper or extra near charge
is added.

## 3. Original-row transport and the cyclic case

Saturated cancellation gives U'=U_original minus G and
y'=((u-h_*)/P_G,v/P_G). A polynomial identity R*y=Q on U_original
implies Q-R_0*h_* vanishes on G, so

    Q'=(Q-R_0*h_*)/P_G

is a polynomial. Its degree bound drops by |G|, because
deg(R_0*h_*)<K+ell<m_original-139+1. Conversely the lift is
Q=R_0*h_*+P_G*Q'. Thus (BR) is equivalent across cancellation,
with the same row-degree bound and the appropriate m. On small unions
the existence-of-Q formulation is used; reducing a polynomial modulo
P_U can only improve its degree bound.

For a cyclic subfield row R_*, use its degree-adapted offset Q_* of
degree <J+deg R_*<=A. Let w be the E-valued residual R_*y-Q_* on U
and let W be its interpolation polynomial. If deg W<=m-139, then
Q_*+W has this same upper degree bound and witnesses (BR). This pays
that part of the ENTIRE cyclic branch without a separate generator-degree
case. Changing the admissible degree-adapted offset adds only a polynomial
of degree <A, so this upper-degree condition is intrinsic at the printed
threshold. An unpaid cyclic residual must have degree at least m-138.

## 4. Actual scope control

The companion verifier and `row_remainder_controls.md` give an actual
cyclic full row space with no nonzero old polynomial relation, but a
bounded row remainder in the NEW degree band. Its six selected labels
have raw two, exactly the root-forced floor. This is a genuine scope
extension, not an assertion that the deployed-row new class is exhaustive.
