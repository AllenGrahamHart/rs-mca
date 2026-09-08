# Claim contract

- **Claim:** two distinct line combinations within Hamming distance `w`
  of codewords force the received pair within joint support distance
  `2w` of a codeword pair.
- **Inputs:** a linear code, finite `z1!=z2`, and the two displayed
  decompositions in `statement.md`.
- **Output:** an explicit codeword pair and a common agreement set of size
  at least `n-2w`.
- **Falsifier:** a coordinate outside both input error supports on which
  either reconstructed pair coordinate disagrees.
- **Nonclaims:** no support-wise MCA payment, balanced-core census,
  bucket coverage, or parameter coalescing.
