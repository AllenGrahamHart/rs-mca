# A385 Pair-Core Ambient Flexibility

This packet records a route cut for the separated `A=385` no-fixed-core
pair-core obstruction.

For any 24-point external core `E` and any fixed projective `Q`-line, the
ambient equations forcing both line generators to vanish on `E` impose at most
`48` homogeneous linear constraints on the `128` base weights `W_x=Omega_x/a_x`.
The solution space has dimension at least `80`, and it contains a point with
all `W_x` nonzero.

Thus the condition `dim ker Phi_E>=2` is ambient-linearly achievable with
nonzero base weights.  This does not construct a bad slope: it does not check
split-locator divisibility, quotient payment, or finite noncontainment.

Replay:

```sh
python3 experimental/scripts/verify_f17_32_m3_rank6_a385_pair_core_ambient_flexibility.py \
  --check experimental/data/certificates/hankel-f17-32-m3-rank6-a385-pair-core-ambient-flexibility/f17_32_n512_k256_m3_rank6_a385_pair_core_ambient_flexibility.json
```
