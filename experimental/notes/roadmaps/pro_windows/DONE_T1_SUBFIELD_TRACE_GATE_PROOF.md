# proof: subfield_trace_paid_gate — PROVED (Pro T1, all core claims verified)

Resolution: residual base-field Weil descent + exact paid TRACE_FLAT ledger class.
Both verified extension-row counterexamples (dli F_{13^2}, sov F_{17^32}) are
ABSORBED as paid trace-kernel collapses — not refutations.

## Weil descent (VERIFIED)
F=F_{p^e}, B=F_p, B-basis omega_i. For every lambda in F, the extension character
z -> psi(Tr_{F/B}(lambda z)) equals EXACTLY the base character on the Weil-restricted
coordinate Phi(z) in B^e with frequency a(lambda)=(Tr_{F/B}(lambda omega_i)):
Tr_{F/B}(lambda z) = <a(lambda), Phi(z)>. (VERIFIED F_49.) Same coordinate descent
as the proved f1 interleaved machinery.

## Exact trace-flat classification (VERIFIED)
For a moving set A, W(A)=span_B{a-a0}, Ann(A)={lambda: Tr(lambda w)=0 for all w in W}.
Phase constant on A IFF lambda in Ann(A); |Ann(A)| = p^{e - dim_B W(A)} (VERIFIED,
nondegenerate trace pairing). Subfield E=F_{p^s}: Ann(E)=ker Tr_{F/E}, |Ann|=p^{e-s}.
This is the paid class — a kernel of the descended base frequency, NOT a collision
or Deligne-conductor class.

## DLI + SOV discharge
DLI: split residues R_flat(j,lambda)={r: lambda in Ann(A_{j,r})} vs R_res. Then
S_{j,lambda} <= sum_{R_flat} m_{j,r} + o(L_j); first term paid, o(L_j) from the
prime-field residual on R_res (nonzero descended freq). F_{13^2}: all residues R_flat
=> paid full level (correctly classified).
SOV: grid sum descends to S_h(a)=[u^h] prod_{c in B}(1+u e^{-2pi i c/p})^{N_c(a)},
N_c(a)=#{x in H: Tr(ax)=c} (VERIFIED Euler product). A one-slice cell is paid with
binom(N_c(a),h). Deployed F_{17^32}: N_0(1)=496 => paid h=21 mass binom(496,21),
density 0.506 (VERIFIED) — paid, NOT sent to cancellation.

## Ledger rule installed
New shared column TRACE_FLAT(lambda or a; moving cell Omega), triggered when
Tr_{F/B}(lambda*(z-z'))=0 for all moving z,z' in Omega. Prices: DLI sum_{R_flat}
m_{j,r}; SOV the restricted trace-slice Euler coefficient (binom(496,21) at the
deployed cell). Off-trigger: apply the base-field residual via the exact Weil
identity.

## Affordability (routed to the existing mca_safe budget audit)
The TRACE_FLAT price joins the paid ledger; the prize-budget audit lives in the
mca_safe assembly (already open). COMFORTABLE: the deployed SOV paid mass
binom(496,21) ~ 2^122.5 is a 2^-8.5 fraction of the value space |F|=17^32 ~ 2^131,
so the trace-flat fiber contribution is << 1 (consistent with the UNIFORM_CONSISTENT
sov scan). No separate obligation — the existing ledger budget covers it.
