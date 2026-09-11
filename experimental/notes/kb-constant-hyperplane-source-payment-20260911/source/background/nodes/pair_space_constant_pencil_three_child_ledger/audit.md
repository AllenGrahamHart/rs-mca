# Hand Review And Controls

The review checks that maximality excludes a whole-rank-one child away
from the roots, that all exceptional affine children share one direction
carrier, and that deg(gcd(T))+E<=D includes repeated roots and infinity.
The incidence ratio needs N>=A and retains the regular bad set separately.
A full constant4 instead makes every regular child whole constant3.

291 finite-coordinate constant3 controls and97 constant4 counter-controls
pass in normal/O Python at0.04/0.12seconds and12800/16344KiB RSS.
The first draft test used delayed generators for basis pairs and failed;
eager tuple construction fixed that test implementation. The corrected
controls do not replace the written universal proof.

Audit verdict: FIXED (test construction); no remaining gap found in the
printed theorem. Independent external mathematical review remains due.
