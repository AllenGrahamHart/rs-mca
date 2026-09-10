# Transfer Three Core Cutoffs On One Original Resource

The [branch recurrence](branch_recurrence.md) proves actual rank-eleven
nonzero-evaluation basis lower bounds B_T(J)=beta_T(J)/12 for all
T in{9,44,150}, with degree<J on m-T distinct points. Since the
original universal carrier core is empty, evaluations on every joint
core are nonzero. The gap 67472-T exceeds J, so each selected subset
spans V*. No auxiliary basis count changes the original receiver.

For an original record with raw<=T, select any m-T joint-core points.
The all-defect insertion proof gives at least raw*beta_T(J) independent
ordered12-tuples owned by that record. It keeps every actual defect,
and tuples from different finite labels are disjoint.

## Intermediate Raw Values

Pair corresponding branches of the COMPLETE three endpoint trees by
their identical spike/equal choices. Exact coefficient checks prove

    (t+1)*f_150*q_150(x)-t*f_t*q_t(x)>=0

coefficientwise for EVERY branch and t in{9,44}. There are512 checks;
all shifted coefficients are rational and nonnegative. In particular,
each corresponding pair obeys the inequality at every x>=0. Taking
minima preserves its orientation: evaluate the smaller side at a
minimizer of the larger side. Therefore

    t*beta_t(J)<=(t+1)*beta_150(J).                     (TRANSFER)

For t<raw<=150 the record's actual core bound is consequently at least

    raw*beta_150 >=(t+1)*beta_150 >=t*beta_t.

This step does not assume the T150 quotient bounds min(raw,150).

## Every Higher Raw Value

The completed-basis supplier's cumulative_low_weights.md proves that
every original record owns at least11*min(raw,500)*m*P_d tuples, where
P_d=prod_(i=1)^10(67472+i). Hence raw>=151 owns at least

    H(J)=11*151*(67472+J)*P_d.

The exact endpoint test is47<=H(E)/beta_150(E)<48. The proved
monotonicity of beta_150(J)/m implies

    H(J)>=47*beta_150(J)                               (HIGH)

throughout9941..21499. Since t+1<=47 for t=9 or44, (TRANSFER)
makes this at least t*beta_t(J). This includes raw>500 and raw>67472;
no unpriced far tail is discarded.

For raw<=t use its own t-core count, for t<raw<=150 use(TRANSFER),
and for raw>=151 use(HIGH). Each original record thus owns at least
beta_t(J)*min(raw,t) tuples. These are CASES for a single tuple set,
not a sum of counts obtained from different selected core subsets.

## Global Floors

Distinct original finite slopes own disjoint independent tuples, and
there are at most U(J)=(1048576+J)_12 ordered coordinate tuples.
Thus sum min(raw,t)<=floor(U(J)/beta_t(J)). The branch recurrence
proves this quotient decreasing on the whole interval. Its exact floors
at9941 and14000 give both rows of the statement. The two alternative
truncation bounds are not additive budgets; each separately holds for
all original records. Near is outside the sums and is added by consumers.

This improves an unconditional resource for EVERY original source,
including full-rank regular low-pair families. It does not assert that
this resource alone suffices to finish those families or a Prize row.
