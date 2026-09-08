# Hand audit and classical inputs

The proof uses the following standard results with their actual scope:

- Schuett and Shioda, [Elliptic Surfaces, arXiv:0907.0298v3](https://arxiv.org/pdf/0907.0298v3):
  section 3 constructs the relatively minimal smooth surface from an
  elliptic curve over a curve function field. Section 4.10 gives the
  global minimal Weierstrass weights over P^1. Theorem 6.8 and
  Corollary 6.9 give the canonical class and section self-intersection;
  Theorem 6.10 and Corollary 6.11 give positive Euler characteristic
  when a singular fiber exists. Pages 7--10, 17, 26--27.
- [Stacks, Proposition 32.6.1, tag 01ZC](https://stacks.math.columbia.edu/tag/01ZC):
  morphisms to a finite-presentation target descend through an inverse
  system of quasi-compact quasi-separated schemes with affine transition
  maps. Equality of two such morphisms also descends.

Both sources were read directly on 2026-09-07. The section-normal
calculation is classical, not claimed as new mathematics. The bounded
polynomial-family application, its spreading/injectivity details, and
the eventual original-coordinate degree accounting are local proofs.
These classical results are explicit foundational inputs, not unresolved
prize premises. No empirical claim stands in for them.

Scope audit:

- The curve is projectively geometrically smooth over k(X).
- A nonempty coefficient locus supplies a rational origin; no flex
  in the original plane coordinates is assumed.
- A genuine family is spread before differentiating, so possible
  first-order failure of integral coordinates is not overlooked.
- The all-smooth product case is handled separately. The cited strict
  positivity statement is never applied to the constant product.
- Characteristic zero or >3 suffices, independent of polynomial degree.
- The coordinate map is an isomorphism, not an inseparable isogeny.
- There is no reduction of the original component degree after changing
  the elliptic equation, nor deletion of exceptional domain coordinates.

Independent external hand review remains due. Algebraic controls in
`controls.md` cover the most consequential missing-hypothesis errors;
no automated geometry or formal proof certification is claimed.
