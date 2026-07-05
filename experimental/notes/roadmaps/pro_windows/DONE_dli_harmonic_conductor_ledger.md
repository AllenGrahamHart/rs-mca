# proof: DLI reduced to fixed-frequency second-moment flatness (Pro W1+W1b, verified)

Target (C). The sharpest possible seam; no -2log2, no Deligne.

## The chain (Pro W1 charge argument + W1b correction)
Level j (34 levels, sum L_j = t), 256 L_j coords grouped by residue r, mult m_{j,r};
normalized transform mu_hat_r(lambda), |mu_hat_r|<=1. W1 (proved): the loss is
charged only to near-peak residues, eta_j <= C_loc sum_{r in E} m_{j,r}. W1b
reduces the near-peak mass to a SECOND MOMENT, with S_{j,lambda} := sum_r m_{j,r}
|mu_hat_r(lambda)|^2: since |mu_hat_r|^2 >= 1-delta on E, S_{j,lambda} >= (1-delta)
sum_{E} m_{j,r}, so
    sum_{E} m_{j,r} <= S_{j,lambda}/(1-delta),  hence  eta_j <= C_loc S_{j,lambda}/(1-delta).
Therefore DLI holds if, for every level j, profile M, and NONZERO lambda,
    S_{j,lambda} = sum_r m_{j,r} |mu_hat_r(lambda)|^2 = o(L_j)   (equiv. (1/256L_j) sum ... = o(1)).
Then sum_j eta_j = o(sum_j L_j) = o(t). The m=1 zero atom and signed-midpoint
stress are automatically paid: each contributes <= its own m_{j,r} to S_{j,lambda}.

## The correction (W1b, verified counterexample)
Exact coincidence counting P(sigma(y1))=P(sigma(y2)) is NOT sufficient: by Parseval
it controls only the FREQUENCY-AVERAGE (1/q) sum_lambda |nu_hat(lambda)|^2, not each
fixed lambda. Counterexample to the reduction: A={0..N-1}, P(x)=x injective (zero
exact collisions) yet at lambda=1 the coefficient (1/N)sum e^{2pi i x/p} ~ 1 (near-peak).
So low exact-coincidence sparsity rules out exact constant fibers, NOT approximate
Bohr alignment. What low degree DOES prove: P(z)=P(x) has <= deg P solutions, so
exact phase ATOMS have <= (deg)|S| multiplicity -- the exact-peak part. The near-peak
/ signed-midpoint part needs the fixed-frequency bound.

## Exact remaining obligation (upgrades to target A)
Prove FIXED-FREQUENCY Bohr/second-moment flatness for psi(lambda P_lambda(sigma(y))):
S_{j,lambda} = o(L_j) uniformly in M and nonzero lambda (equivalently the eps-Bohr-pair
mass B_{j,lambda}(sqrt delta) = o(L_j)). Calibration (eta*/L=3.6e-7) supports it
numerically; the asymptotic primitive-core proof needs the fraction -> 0, or the
finite-prize reserve used explicitly.
