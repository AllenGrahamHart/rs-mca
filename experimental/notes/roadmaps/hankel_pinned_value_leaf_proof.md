# proof: hankel_moment_clean_leaves (the pinned-value variant, option b)
CLEANLINESS (option a) IS FALSE in general: the monic slice of K[X]_{<=d} has
direction-dual weight-(d+1) words with nonzero affine constant (Pro's MDS
example) — the pinned seam is real. THE PINNED-VALUE LEMMA (proved, general
affine linear algebra, not Hankel-specific; VERIFIED 279 clean flats, counts
always in {0, q^{dim A - s}}): if the AFFINE annihilator Ann(A,E) has no
nonzero weight-<=r word (the terminal-leaf condition), then for every |T| =
s <= r, ev_T(A) is either missing 0 (count 0) or onto (count q^{dim A - s})
— else a functional vanishing on the image extends to a sparse affine-
annihilator word. Hence sum_f C(rho(f), s) <= C(|E|, s) q^{dim A - s}: the
SAME member/moment upper bound as the clean case; pinned words only remove
the all-zero assignment, never add members. This is exactly the leaf input
QF.12 leaves family-specific.
