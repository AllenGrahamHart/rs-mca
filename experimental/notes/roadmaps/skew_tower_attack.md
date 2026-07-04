# The skew-tower attack (opened 2026-07-04; level-1 EXACT, three-field verified)

## The exact level-1 theorem (verified: mu_16 x {F_17, F_97, F_193}, every set)

t-null subsets A of mu_n biject with pairs (m_1, d_0): m_1 = the squaring
pushforward (a floor(t/2)-null multiset, values <= 2) and d_0 = the skew,
and the constraint system splits EXACTLY as even-nullity of m_1 plus the
twisted odd condition on d_0 (Pro's Lemma 5, bookkeeping re-verified:
238/238 reconstructions + constraint splits at F_17).

## The two discoveries

1. FACTORIZATION IS EXACT AND PROFILE-CONSTANT: the number of valid skews
   d_0 above a given m_1 depends only on m_1's multiplicity profile (its
   singleton count k), constant across states within a profile — verified
   with zero exceptions.
2. THE BRANCHING IS A KNOWN OBJECT: #valid skews = #{eps in {+-1}^k :
   sum eps_i sigma(y_i) = 0 in F_q} — the SIGNED SPARSE VANISHING SUMS
   that weight_graded_mitm enumerates and the (A)-side norm-gate theory
   classifies (p must divide the cleared norm; zero at non-exceptional
   primes). Confirmed: rich branching at the exceptional prime 17; pure
   coset recursion (branching 1) at 97 and 193.

## The program this licenses

#\{t-null\} = sum over tower profiles of prod_j N_j, with N_j = the exact
bounded-coefficient signed-relation count at level j (weight = level-j
singleton count, coefficients <= 2^j, domain mu_{n/2^{j+1}}, T_j/2 odd
constraints). The giant-regime count becomes an exact product of the SAME
exceptional-prime objects the small-h side certifies. Remaining hard parts,
honestly: (i) generalize the relation classification from +-1 to
coefficients <= 2^j (norm-gate-shaped, needs doing); (ii) the central-range
weight accounting — shallow levels can carry weight ~b (not sparse), so the
win must come from the exact constraint cascade (sum_j T_j/2 ~ t constraints
distributed down the tower) plus per-level rigidity, not sparseness alone;
(iii) iterate the profile-constancy proof (orbit argument: scaling acts
transitively within profiles — conjectured from data, unproved).

## Next pre-registered steps
- Prove profile-constancy at level 1 (the mu_n-scaling orbit argument).
- Level-2 experiment (full tower at mu_32-scale rows, exceptional q).
- The bounded-coefficient relation count at weight <= 8, coeffs <= 4
  (exact, small) — the first genuinely new object.
