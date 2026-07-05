# proof: DLI fixed-freq flatness — PRIME-FIELD scoped (Pro P2, verified)

## Pro P2 finding (verified): the general-F_q claim is FALSE
Over F_q = F_{p^2} with p ≡ 1 mod 2n, the section sigma(mu_n) subset mu_{2n}
subset F_p (prime subfield). For lambda with Tr_{F_q/F_p}(lambda)=0 (exists, the
trace-zero line is 1-dim) and P_lambda(X)=X: for every section point x in F_p,
Tr(lambda x) = x Tr(lambda) = 0, so psi(lambda P(sigma(y)))=1 for ALL y, giving
|mu_hat_r(lambda)|=1 and S_{j,lambda} = sum m_{j,r} = Omega(L_j), NOT o(L_j).
VERIFIED (F_13^2). This is a TRACE-KERNEL collapse, not exact-collision failure
(P=X is injective) — the obstruction lives in the trace pairing.

## Scope resolution (verified)
Over a PRIME field F_p, Tr = identity, so psi(lambda .) is a nontrivial additive
character for every nonzero lambda — NO trace-zero collapse. So the fixed-freq
second-moment flatness S_{j,lambda}=o(L_j) is a PRIME-FIELD estimate, consistent
with b2b's "the fixed prime q" framing. dli holds prime-field-wise (still needs
the fixed-frequency Bohr bound, P2 target A on prime rows).

## NEW obligation (extension rows): see b2b note
The challenge includes EXTENSION rows (KoalaBear sextic F_{p^6}), where the
collapse frequencies are real. For those the primitive core must EITHER (a)
Weil-restrict to the base F_p (same interleaved/Weil machinery that closed f1),
OR (b) carry an explicit no-subfield-trace-kernel-collapse hypothesis proved for
the actual phases. This is a genuine scope gap P2 exposed; flagged on b2b.
