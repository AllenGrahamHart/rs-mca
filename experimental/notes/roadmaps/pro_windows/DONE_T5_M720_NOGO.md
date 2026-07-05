# proof: m720_conductor_compression — compression REFUTED; real routes clarified (Pro T5, verified)

## T5-A (support-size conductor compression): REFUTED (VERIFIED)
The lemma "the anchored-core obstruction lives in a field bounded by the 2h-support
size" is FALSE. Witness (n=1024, h=7): the anchored 14-support A={0,1,2,3,5,7,11,15,
23,31,63,127,255,511} (exponents) has TRIVIAL multiplicative stabilizer mod 1024
(|Stab|=1, VERIFIED) — it is not antipodal-closed (genuinely non-toral) — so its
symmetric functions, hence the cleared obstructions A_j(R)=2^{26}O_j(R), generate the
FULL Q(zeta_1024), degree phi(1024)=512. Then 291*[L:Q]=291*512=148992 >> log2 p ~ 250,
so the height gate does NOT close. A small support does NOT bound the field; any true
compression must use survivor-SPECIFIC equations, not anchoredness/non-torality/size.

## T5-C (conditional height gate): PROVED
Fix an official row F_q (q=p or p^2, n|q-1), h in [7,20]. IF every primitive non-toral
anchored survivor R has a nonzero cleared obstruction A_j(R) in a field L_R with
291*[L_R:Q] < log2 p, THEN no survivor exists: by P4-HB all A_j(R)≡0 mod P; if all=0
in char 0 then X24 makes R toral/paid (contradiction); else some A_j!=0 with
p | N_{L_R/Q}(A_j) and |N| <= B_h^{[L_R:Q]} <= 2^{291[L_R:Q]} < p — impossible.

## T5-(ii) D(n,h)-GCD certificate route: BLOCKED ON PAYLOAD
Sound in principle (gcd(p,D(n,h))=1 => good reduction => row candidates = char-0
candidates), but the public repo lacks the required data: the explicit D(n,h) integers
per (n,h) window AND the actual official Row-C ~250-bit prime list (the repo uses a
labeled stand-in). No honest official certificate can be printed without that payload.

## Corrected obligation (this node)
The m720 norm gate is discharged for a (row,h) pair iff EITHER (i) a SURVIVOR-
CONDITIONED small-field certificate 291[L:Q]<log2 p is proved for a nonzero obstruction
(needs survivor-specific equations, NOT support size), OR (ii) the C2 certificate
gcd(p,D(n,h))=1 is supplied (needs the missing D(n,h) + official-prime payload). The
support-size compression lemma is false.
