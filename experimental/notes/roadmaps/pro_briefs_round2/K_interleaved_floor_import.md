# Pro follow-up — interleaved_floor_import (the exact S9 seam)

*Same ef thread. You proved F-valued word source => e-interleaved base-list
witness, and reduced ef_fullfield_bridge to this one import. This brief is that
import, with ext_pole_floor's mechanism pinned so it closes or exposes S9.*

## Recap of your reduction
Every trivial-stabilizer, noncontainment, non-tower horizontal component C of
X_E is, at its generic point, an e = [E:B]-interleaved base-field
multiplication-slice witness:
    H_B( Syn_B(Phi(f)) + M_z Syn_B(Phi(g)) ) ell_T = 0,   with interleaved
noncontainment (M_z = the B-linear mult-by-z matrix on E, e = [E:B]). The
ORDINARY-base-list version is false (the proved X - alpha counterexample), so
the interleaved form is the correct object. The bridge closes iff ext_pole_floor
covers it.

## ext_pole_floor pinned (PROVED, s6 / Paper D v12)
The extension-pole floor converts a base LIST of size L (over B) into genuinely
F-valued witness lines meeting the extension-pole divisor D_E, with numerator
    N(L) = ceil( L (|F| - |B|) / (|F| - |B| + k L) ),   k = 2^40, X = |F| - |B|.
Behavior: N(L) ~ L below the saturation cap X/k ~ 2^216; the gate crosses at
L ~ 2^128. It is stated/proved for F-valued witness lines arising from an
ORDINARY base list over B; it BINDS on non-generating rows (F \\ B nonempty).

## The ask (prove the import, or exhibit S9)
> **interleaved_floor_import:** every e-interleaved base-list multiplication-
> slice witness (as above) meets the extension-pole divisor D_E -- i.e.
> ext_pole_floor's N(L) mechanism applies with the interleaved witness's
> effective base-list size.

- **(A) Prove it:** show the interleaved witness has a well-defined effective
  base-list size L_eff to which N(L_eff) applies (candidate: the interleaving
  over a B-basis presents e coupled base lists sharing the locator ell_T, and
  the multiplication-slice M_z couples them so the pole floor still forces D_E;
  the effective L is at least the base list size, so N(L_eff) still crosses the
  gate on non-generating rows). Make the list-counting precise: does the
  interleaving PRESERVE, MULTIPLY (L^e), or DILUTE the pole-forcing list mass?
- **(B) Exhibit S9:** an interleaved witness whose effective list mass falls
  BELOW the N(L) gate -- e.g. the multiplication-slice coupling reduces the
  independent F-valued list so N(L_eff) < |F| 2^-128 -- so it escapes the pole
  floor. This is the genuine new extension-valued S9 ledger class; it would need
  its own reserve/pricing and reshapes the S6 classification.
- **(C) Conditional:** the import modulo a clean stated bound on L_eff.

## Why this is decisive
This is the SOLE remaining input to ef_pole_free_cycle_exclusion ->
ef_full_orbit_pole_forcing -> ef_ru -> f1_full_field_pole_forcing. (A) closes
all four unconditionally; (B) is a new ledger column the prize dossier must
carry. Either resolves the F1 typecheck the s6 sketch flagged and never closed.
The crux is purely the list-counting of the interleaved multiplication slice
against N(L) -- no more Galois descent, no more noncontainment.
