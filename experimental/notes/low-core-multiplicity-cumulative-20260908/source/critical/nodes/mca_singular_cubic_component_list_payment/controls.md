# Hand Guards And Small Controls

1. A positive-dimensional family is not necessarily a full affine parameter
   space. The polynomial-model proof uses only irreducibility and varying
   evaluation at every finite point after dividing the gcd of differences.
   It also uses a varying leading coefficient at infinity. Both assertions
   follow from the chosen center and gcd, not generic receiver assumptions.
2. One cannot use 315 pairs without multiplying by the number of components.
   That number is paid via a finite, basepoint-free cubic map and its degree
   cost 3^r, in ORIGINAL pair coordinates. Injectivity on geometric points
   alone would not prove degree one in positive characteristic; the explicit
   rational normalization inverse is used.
3. Lower-dimensional pairs are counted outside all top-dimensional
   components. A lift of such a pair cannot lie on a three-dimensional
   component of the finite cover. The smaller-dimensional budget is then
   valid; no pure over-cover is substituted.
4. Exceptional fibers are real. Put A=X,B=1 and
   `(Phi,Psi)=((z^2-1)*z, X*(z^2-1)-X*(z^2-1)*z)`.
   Its projection is X*(z^2-1), so E=X and gamma=1. At X=0,
   the map is `(z^3-z,0)`, with a three-element fiber over F_7.
5. Constant fibers must be handled separately. Multiplying the model
   `((z^2-1)*z,(z^2-1)-X*(z^2-1)*z)` by X^2 gives gamma=X^2
   and E=X^2. At X=0 every parameter gives (0,0). If the receiver
   is (0,0), this coordinate is an identical agreement and must be
   subtracted from both counts, not bounded by a three-element list.
   A different received value yields an empty list.
6. Every such identical coordinate is a root of E as well as gamma.
   Its removal reduces the slot budget by three in the used envelope.
   g need not equal its maximum: the proof includes the monotonicity step.
7. The worst h and parameter degree used in the final rectangle need
   not be simultaneously attainable. They give an upper relaxation with
   a verified positive denominator, not a constructed extremal source.

The finite controls use only F_7 to check displayed fibers. They do not
claim the KoalaBear source contracts hold for that toy field or prove the
generic component model. The ordinary field-size/characteristic guard in
the application remains p=2130706433>J.
