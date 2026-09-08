# Claim contract

- **Claim:** under `w>=1` and `3w<=n-K`, at most `2w` support-wise
  MCA-bad finite slopes can simultaneously lie within distance `w` of the
  Reed-Solomon code.
- **Inputs:** one near-codeword decomposition and one actual same-support
  MCA witness for every counted slope.
- **Currency:** distinct finite affine slopes on one fixed received line.
- **Output:** an injection into at most `2w` coordinate ratios of the joint
  two-anchor error pair.
- **Falsifier:** a legal received line with more than `2w` such slopes, or a
  counted slope whose badness is witnessed only on a different support from
  the support used in the injection.
- **Nonclaims:** no `+1` bound, no owner partition, no far-stratum bound, no
  KoalaBear/K3 endpoint, and no full-row MCA closure.
