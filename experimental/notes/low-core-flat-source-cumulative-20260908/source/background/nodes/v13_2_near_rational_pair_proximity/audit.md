# Source and scope audit

Audited on 2026-07-20 against Paper D v13.2 promotion commit
`4bea7abb2d9455583c8864b980e39d11d550f51d`.

- TeX blob: `5ceff5dbc4b1ac4cef53eae7eada32046e4bafeb`
- revision-note blob: `2043c69a34b100a514366e5b0768777f28cf952f`
- source labels: `thm:capfp-dichotomy`, `cor:capfp-line`

The linear algebra in the source is sound and yields the stronger joint
support bound `2w`, not merely `3w`. The following inference from common
pair proximity to absence of support-wise MCA-bad slopes is not valid; it
is isolated in `v13_2_near_rational_supportwise_payment` as REFUTED.
