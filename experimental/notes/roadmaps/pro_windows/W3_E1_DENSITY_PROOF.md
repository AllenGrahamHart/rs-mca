# proof: e1 N'=256 density bound (Pro W3, verified)

The WEAKENED density target (o(1)-sparsity, not zero-survivor) is delivered by a
bad-prime union bound over the norm divisors.

Non-quotient collision => nonzero folded c in {-2..2}^d (d=phi(N')=N'/2) with
sum_i c_i tau^i = 0 mod p => p | Norm_{Q(zeta_N')/Q}(alpha_c), alpha_c = sum c_i
omega^i != 0. Each conjugate |sigma(alpha_c)| <= sum|c_i| <= 2d = N', so
|Norm(alpha_c)| <= N'^d. A nonzero integer <= N'^d has at most
r_N = floor(d log N' / log P) primes in the dyadic shell [P,2P) (P^{r+1} > N'^d).
With <= 5^d folded vectors and |{p ~ [P,2P): p=1 mod N'}| ~ P/(d log P) (PNT in
APs), the first-moment average is
    E_p S_p <= (1+o(1)) 5^d r_N d log P / P.

Prize scale P=2^250 (VERIFIED, notes/verify_density_suffices.py):
- N'=128: d=64, r_N=1, E S_p <= 2^-87.4 => Pr[S_p>0] <= p^-0.350.
- N'=256: d=128, r_N=4, E S_p <= 2^64.2 => Pr[S_p > p^1/2] <= p^-0.243.

So for all but a p^-0.24-fraction of admissible N'=256 row primes, non-quotient
survivors <= p^1/2 = p^-1/2 * value-set(~p) = o(1)-SPARSE. This is the W3 target
(density/typicality over the admissible prime family, matching the prize's
admissible-|F| quantifier). Discharged via the typicality route
(e1_official_typicality_or_certificate). Scope: folded-survivor density, not raw
ordered pairs (the brief moved the target to survivor density).
