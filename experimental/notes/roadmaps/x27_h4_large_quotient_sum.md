# X27: large h=4 quotient-sum extension

- **DAG node:** `x27_h4_large_quotient_sum`.
- **Consumer:** `active_core_count_bound`.
- **Status:** exact finite evidence.
- **Verifier:** `experimental/scripts/verify_x27_h4_large_quotient_sum.py`.
- **Certificate:**
  `experimental/data/certificates/x27-h4-large-quotient-sum/x27_h4_large_quotient_sum.json`.

## Scope

X26 showed that the checked h=4 exceptional-prime mass is exactly the
antipodal lift of the quotient h=2 sum-collision problem

```text
{1, a}, {b, c} subset mu_{n/2},        1 + a = b + c.
```

This packet extends that quotient arithmetic to the full boundary windows

```text
n = 128, 256,        p == 1 mod n,        n^2 < p <= n^3.
```

It deliberately does **not** enumerate h=4 supports.  It measures only the
paid quotient-lift supply that X26 isolated.

## Method

For each prime, the verifier builds the unordered pair-sum table in
`mu_{n/2}` and then queries the anchored sums `1+a`.

This is `O((n/2)^2)` per prime rather than the h=4 support sort.  It keeps the
full n=256 window small enough to replay on the local machine.

The persistent zero-sum quotient collisions are

```text
{1, -1} and {b, -b},
```

and lift to the `mu_4` full-fiber family.  All other quotient h=2 sum
collisions are recorded as paid antipodal quotient lifts.

## Results

```text
row             primes     zero-sum baseline   extra rows   extra total   max extra
----------------------------------------------------------------------------------
n=128            2,411          31                  46            780          52
n=256            8,383          63                 214          3,056          88
```

The baseline is intact at every prime in both windows.

The extra quotient-lift mass is sparse:

```text
n=128: 46 / 2411 primes, density 0.01907922024056408
n=256: 214 / 8383 primes, density 0.0255278539902183
```

The largest single rows are:

```text
n=128: p=65537, extra=52
n=256: p=65537, extra=88
```

In both windows the total extra quotient-lift mass is below `n^2`:

```text
n=128: 780  < 16,384
n=256: 3056 < 65,536
```

## Interpretation

This strengthens the finite-p h=4 picture in quotient currency:

```text
zero-sum quotient collisions    -> mu_4 full fibers
extra quotient h=2 collisions   -> paid antipodal quotient lifts
```

The scan does not prove that all h=4 support collisions at `n=128,256` are
quotient lifts; doing that directly would require the heavier h=4 support
sort.  It does show that the X26 exception mechanism remains small and paid in
the next two full boundary windows.

For the terminal node, the useful consequence is that the first finite-p
reduction mechanism is not growing like the raw h=4 support space.  The
remaining h=4 proof target is therefore a structural exclusion:

```text
every h=4 finite-p reduction is either a full mu_4 fiber,
an antipodal quotient h=2 lift, or primitive residue.
```

The checked quotient data says the first two classes are harmless for the
rewired `n^3` column.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x27_h4_large_quotient_sum.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x27_h4_large_quotient_sum.py --write-certificate
```

Current replay: **14 PASS, 0 FAIL**.
