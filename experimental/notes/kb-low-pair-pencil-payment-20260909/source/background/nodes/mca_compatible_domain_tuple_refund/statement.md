# A Compatible Domain Removes Its Internal Incidence Tuples

Status: PROVED by proof.md; independent external review remains due.

Use the selected-slope setup of mca_nonuniform_support_margin_resource:
degree-<K explanations h_gamma in h_*+V, actual dim V=s, and full-code-bad
size-m scalar-agreement supports on n distinct coordinates. A record owns
the ordered independent (s+1)-tuples in its selected support, in the
original incidence frame (v,-V).

Let U be ANY subset of the original domain, and suppose one of:

    finite chart:   u+gamma_0*v=c on U, c in h_*+V;
    infinite chart: v=c on U, c in V.                     (COMP)

In the finite chart remove the one possible selected label gamma_0. In
the infinite chart remove none. Let Gamma' be the retained labels.
Then their available tuple universe has size at most

    (n)_falling_(s+1)-(|U|)_falling_(s+1).                 (REFUND)

In particular, if every retained record is independently proved to own
at least beta*w_gamma independent tuples, beta>0,w_gamma>=0, then

    sum_(Gamma') w_gamma <= REFUND/beta.                  (WEIGHT)

For integer weights the right side may be floored. Taking
w_gamma=min(raw_gamma,kappa) is allowed only with a proved recordwise
lower bound; the theorem does not supply that lower bound itself.

No original source coordinate, degree, support, raw margin or carrier is
changed. This subtracts forbidden tuples from an upper-count universe,
not coordinates from the code. Every record, including high-defect records,
uses the same refund. The finite kernel slope costs at most one original
label, not a new near allowance.

The affine membership c in h_*+V or c in V is essential. An arbitrary
polynomial receiver relation or a nonconstant rational direction does not
justify (REFUND). No outside-of-union pair-to-slope conversion is provided;
that remains the consumer's separate ownership obligation.
