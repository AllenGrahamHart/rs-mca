# Flip packet: knife_edge_census

- **Node:** `knife_edge_census`
- **Current critical label:** UNPROVED
- **Verdict:** PROMOTE-CONDITIONAL
- **Referee summary:** this node is a local assembly implication. If the
  certified lower-bound child is granted for the rows selected by the arithmetic
  child, the refined knife-edge census statement follows.

## Statement

> REFINED: with bounded scales + exact counts, the census is exact Diophantine arithmetic — windows [L(n,A), K(n,A)) in B*-space per rate/candidate, undecided rows = admissible primes landing inside. Ties exist systematically (B* sweeps all integers as q varies); the residual undecided set shrinks exactly as certification strength L grows toward K. Full grand-challenge closure requires L within O(1) of K at the tie point OR per-prime typicality; exhibited-row partials dodge entirely (census_dodge_selection).

## Req Children

| child | live status | critical label | role |
|---|---:|---:|---|
| `certified_valueset_lower` | TARGET | UNPROVED | Supplies the per-prime lower-bound strength `L`. |
| `census_window_arithmetic` | PROVABLE | PROVABLE | Computes the exact `[L(n,A), K(n,A))` windows and residual rows. |

## Referee Argument

Grant the two req children as stated, read in their intended per-row schema.
`census_window_arithmetic` converts the bounded-scale exact counts into an
explicit prime/window list:

```text
undecided rows = {admissible q = 1 mod n :
                  floor(q/2^128) in [L(n,A), K(n,A))}
```

`certified_valueset_lower` supplies the lower-bound strength `L` for a
knife-edge row. Substituting the certified `L` into the exact windows is
precisely the parent statement: the undecided set is a Diophantine interval in
`B*`-space, and increasing `L` shrinks the interval until it vanishes at
`L >= K` (up to endpoint convention). The statement's final sentence about
exhibited-row partials is also inherited: a row outside every `[L,K)` window is
decided by the arithmetic alone.

No new analytic estimate is used locally. The remaining proof is entirely in
the children: make the value-set lower certificate strong enough, and compute
the windows exactly. Therefore the parent should be amber, not red.

## Caution

The child `certified_valueset_lower` is worded singularly ("For a knife-edge
row"). The promotion is valid only if the roadmap lane treats that child as the
per-row certificate schema already described in the execution queue. If the
validator reads it as one fixed row only, pluralize or schema-ify that child
before applying this packet.

## Evidence Pins

- `knife_edge_census`: `198e816a76a9e9d2`
- `certified_valueset_lower`: `00335d6a53907bd9`
- `census_window_arithmetic`: `ad0a5b69dbe08647`

## Source Quotes

- `q3r5_three_rate_dossier_skeleton.md` Section 3.2 names the exact-count,
  window-arithmetic, dodge, and residue slots separately.
- `qa3_e14_fm_margin_tables.md` records why the knife-edge rows must be
  treated exactly: the `A*+1` / `sigma*+1` margins can be positive or thin,
  so ties cannot be quoted as decided without this census.
