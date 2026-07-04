# Pro brief C: sharpen the universal cap at rate 1/8 (wedge route a)

SETTING. Paper D's universal cap theorem (attached): for ALL linear codes,
the unsafe regime begins above 1 - rho - 2^-9 — the reserve 2^-9 is a
declared constant of the proof, not an optimum. The campaign's corridor
arithmetic at rate rho = 1/8 (RS over mu_n, n = 2^41, q ~ 2^256, official
prize parameters) is 0.00707 GRID STEPS short of collapsing the
safe/unsafe bracket to adjacency, where one grid step = eta = 2^-9 in
rate units. Everything else is exact: the quotient/ACL end is a computed
number, the window cleanup is computed, the extension end is exactly
zero.

ASK. Sharpen the cap's reserve at rate 1/8 for Reed-Solomon (or
interleaved RS) specifically: any improvement of the proven-unsafe
boundary by >= 0.00707 * 2^-9 ~ 1.4e-5 in absolute rate. Full
generality not needed — RS over 2-power mu_n at the stated parameters
suffices. EQUALLY VALUABLE: a matching construction showing the cap is
tight at rate 1/8 within < 1.4e-5 (this would prove route (a) dead and
focus the campaign on its two sibling routes). The proof shape of the
existing cap (half-Johnson correlated-agreement bound + the deep-regime
safe theorem) is in the attached tex; the 2^-9 enters at [locate it —
the reserve slack in the union step is the natural target].

Attach: the cap section of tex/cs25_cap_v12.tex (from
github.com/przchojecki/rs-mca), plus this node's statement.md.
