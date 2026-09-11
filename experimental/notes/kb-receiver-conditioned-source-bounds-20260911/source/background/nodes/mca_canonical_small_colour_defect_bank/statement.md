# Canonical Low Defects Live In Small Receiver-Colour Classes

Status: PROVED locally; external mathematical review remains due.

Fix the standard full-code-bad support setup over F: distinct domain D
of size n, degree<K, agreement m=K+d, fixed carrier h_*+V of dimension
s>=1, and distinct finite labels. Maximize raw over ALL admissible
supports and explanations in that SAME fixed carrier for each label.
Let 1<=T with2T<d.

On each complete NONZERO projective evaluation fibre of V, write
ev_x=lambda_x*ell, lambda_x!=0. Partition it by the receiver colour

    ((u(x)-h_*(x))/lambda_x, v(x)/lambda_x).

These classes, equivalently nonzero-V projective fibres of the augmented
vector(ev_x,u(x)-h_*(x),v(x)), do not depend on the chosen scaling.
Let B_t be the union of colour classes of cardinality at most t,
and sigma_t=|B_t|. These are coordinate counts, not class counts.

For a canonical record with raw r<=T, its COMPLETE defect set has
size r. Every nonzero-evaluation defect belongs to a colour class of
size at most r. Hence those defects lie in B_r, and in B_t when r<=t.

At zero-evaluation coordinates with v(x)!=0, the scalar equality fixes
the single finite label gamma=-(u(x)-h_*(x))/v(x), independently of the
chosen explanation. There are at most z<=K-s such labels, where z
counts zero-evaluation coordinates. Remove those labels once.
A coordinate with v=0 cannot be a defect there.

## Restricted Tuple Resource

Suppose each retained canonical record of raw r<=t owns at least r*beta
distinct ordered(s+1)-tuples made from s points of its complete joint
core and one actual defect, with tuples of distinct labels disjoint.
Here beta>0 is any proved uniform lower cost. Then

    sum_(retained raw<=t) raw
      <=[n_falling_(s+1)-(n-sigma_t)_falling_(s+1)]/beta.

Every such tuple hits B_t, possibly in MORE than one position.
No assertion that its bank point is unique is needed.

For a fixed represented pair, the retained original raw weight at cutoff
t is also at most sigma_t, by same-pair defect disjointness.

The maximum-margin requirement is essential: explicit nonmaximizing
raw-one supports can have defects in a colour class of size three.
The bound alone is not a Prize-row payment.
