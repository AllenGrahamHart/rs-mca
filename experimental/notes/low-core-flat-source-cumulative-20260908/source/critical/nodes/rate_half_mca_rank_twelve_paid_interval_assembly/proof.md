# Proof: Bind The Normalized Bounds To Every Original Label

## 1. Freeze The Original Selection

Use the near set and complete post-near selection from statement.md.
Its at most 134944 near slopes are added back ONCE at the end. A family
with at most one retained slope is immediate. The required rank-eleven
theorem pays a<=11 by 156765527508803240. Assume a=12.

Same-support badness implies v is not an original codeword. Otherwise
(h_gamma-gamma*v,v) would be a degree-<K polynomial pair explaining
the received pair on every selected scalar support.

Fix gamma_0 and form the actual polynomial/slope space

    E=span{(gamma-gamma_0,h_gamma-h_gamma0)} subset F direct_sum C.

The map (delta,c) -> delta*v-c is injective: if delta is nonzero its
kernel would make v a codeword; if delta=0, injectivity of polynomial
evaluation on n>=K points gives c=0. Its image is the error-difference
space, so dim E=a=12. The first-coordinate projection has rank one.
Choose (1,b) in E and put

    v^g=v-b, h_gamma^g=h_gamma-gamma*b,
    h_*=h_gamma0^g, V=span{h_gamma^g-h_*}.

The differences generate precisely the kernel of the slope projection
of E, so V has ACTUAL dimension eleven, not merely an upper bound.
Errors and complete scalar agreement sets are unchanged by this gauge.
Adding or subtracting b in a pair's second polynomial proves two-way
preservation of full-code pair containment on every support.

## 2. The Complete Shared Core Is Exactly The Universal Carrier Core

We claim

    G={x:V(x)=0, v^g(x)=0, u(x)=h_*(x)}.            (1)

Right-to-left is immediate. If every selected error vanishes at x,
each generator (delta,c) of E satisfies c(x)=delta*v(x), hence so
does every element of E. Applying this to (1,b) gives b(x)=v(x).
Applying it to the zero-slope kernel gives V(x)=0. The gamma_0
equation then gives u(x)=h_*(x). This proves (1).

In particular every V-polynomial vanishes on G. The polynomial common
root-space bound gives g<=K-11 and J=K-g>=11. The larger zero set
{x:V(x)=0} need not equal G. We do NOT remove that larger set: a
nonuniversal zero may agree at one original slope, which must remain.

## 3. All Labels Admit Saturated Full-Bad Supports

Let A_gamma be the COMPLETE scalar agreement set of h_gamma^g.
It contains G and its original full-code-bad witness, so no polynomial
pair can explain it entirely. Apply the required common-core transport
theorem with P=P_G. On D'=D minus G define

    u'=(u-h_*)/P, v'=v^g/P,
    V'=V/P, h'_gamma=(h_gamma^g-h_*)/P.

There is no division by a zero locator value on D'. The dimensions are

    n'=n-g=1048576+J, K'=J, m'=m-g=67472+J,
    dim V'=11, deg V'<J.

For clarity, each A_gamma minus G contains an exact size-m' bad subset.
Otherwise polynomial pairs on all its m'-subsets would agree on adjacent
overlaps of size m'-1>=J. Connectedness under one-point exchanges glues
them to one pair on the complete remainder. Lifting by P and adding
(h_*,b) would explain the original A_gamma, a contradiction.
Adding G to such a child subset gives a saturated original witness.
Thus every original label remains, with no exception charge.

The child's universal carrier core is empty by (1): any point in it
would have belonged to the complete original G and was removed.
Common V'-zeros outside that core may remain. The field, slope values
and cardinality |Z| are unchanged, so the normalized numerator is
exactly |Z|, not a quotient image or independently maximized fiber sum.
At this cancellation stage the original error affine rank is also
preserved: all selected errors vanish on G, so restriction and nonzero
coordinate rescaling are injective on their affine-difference span.

## 4. Canonical Reselection Does Not Reopen Transport

The high-interval theorem requires no maximal-raw selector. For the
lower-strip theorem, maximize the raw mismatch for each label over all
size-m' full-bad supports and explanations in the SAME fixed V'. This
maximum exists over the finite field and finite domain; the family is
nonempty by section 3. Choose one maximizer and a minimizing second
polynomial. The lower-strip prerequisite uses 2*500<67472, as required.

This operation keeps the original label set and the actual ambient
carrier V' with empty universal core. It need not preserve the previous
raw values, selected explanations, shared complete core or error rank.
Those are not new obligations: a and G were used BEFORE reselection
to obtain the fixed child row, and the normalized lower-strip theorem
is uniform over all permitted canonical selections on that fixed carrier.
Do not shrink V' to a newly selected explanation span or cancel a new
shared core as an uncharged extra normalization.

## 5. Compose Whole-Source Alternatives, Not Owner Charges

The existing common-core forcing theorem already pays rank twelve for
g<=878576 and, in every rank, g>=1043776. Its stated uniform totals
are at most 273540953998915577 and 100000000000134944 respectively.
The completed-child improvement has the smaller total 270992495272115150
on 793577<=g<=878576; all these are below the total in (ORIGINAL).

For the remaining 878577<=g<=1043775, sections 1--4 give the exact
normalized row J=4801..169999 without losing labels. The required
all-carrier interval theorems now pay:

    original g interval     child J interval      |Z|+134944 upper bound
    878577..983576           65000..169999         274929007493481160
    1038636..1043775         4801..9940            274979661975561635.

The remaining original interval is exactly 983577..1038635, equivalent
to J=9941..64999. Every other rank-twelve case has a whole-family bound.
The finite alternatives refer to the ONE g attached to the fixed original
selection; their worst-case totals combine by MAXIMUM, never addition.
Since |Z_bad|=|Z|+|N|<=|Z|+134944, the largest bound proves (ORIGINAL).

Taking the contrapositive for an arbitrary complete selection proves
the EVERY-selection restriction on any over-budget original line.
Changing a selection may change a and G; no favorable choice is assumed
to exist. The existing all-rank large-core restriction remains valid.

## Scope And Provenance

The gauge and core identification are already proved in the rank-twelve
common-core supplier; saturated-support transport is already proved in
its separate supplier. This node makes their complete source interface
explicit and composes it with the new normalized bounds. The transport
mechanism is not claimed as a new independent discovery.

This is a DIRECT original-source theorem, not a claimed active-v4 atom.
An owner ledger is unnecessary for its direct conclusion; bankability
inside such a ledger would require its separate owner contract. Error
ranks >=13 and rank twelve on the remaining interval are unpaid.
No unrestricted endpoint, LIST theorem or full prize claim is made.
