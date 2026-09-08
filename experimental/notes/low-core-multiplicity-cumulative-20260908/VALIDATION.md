# Publication Replay Record

Executed in the outbound snapshot on 2026-09-08, before publication.
No external independent mathematical review is claimed.

| Replay | Result | Wall Time | Peak RSS |
| --- | --- | ---: | ---: |
| Python normal wrapper | 55/55 PASS | 3.62 seconds | 16512 KiB |
| Python optimized wrapper | 55/55 PASS | 3.67 seconds | 20900 KiB |

Both runs verified all 212 frozen sources (653486 bytes of source content)
against SOURCE_MANIFEST.json and rejected four malformed manifest variants:
changed hash, duplicated file, missing file and nonlocal path. The unchanged
baseline was checked again after the mutations.

The wrapper always runs its children serially without optimization, clears
PYTHONOPTIMIZE, disables bytecode output and caps each child at 15 seconds.
The new multiplicity and cumulative-tail checks also use explicit checks
that survive optimization. Existing earlier arithmetic children can contain
assertions; the optimized-wrapper run does not claim those assertions were
rewritten or that they would survive optimizing the children themselves.

Both complete executions were enclosed in the origin's RAMguard tiny
profile: 256 MiB RAM, 64 MiB swap, 60 seconds. Resource figures above are
measurements, not a portable worst-case performance guarantee.

The tests verify integer/rational arithmetic, small Taylor/Hasse controls,
finite kernel gaps, factor prices, resource identities and snapshot identity.
They do not formally certify universal geometry, prove original-source
exhaustion, or establish a safe or optimal unrestricted row endpoint.

No field-sized enumeration, large interpolation matrix, CAS, TeX or Lean
build, dependency install, Modal job or compute spending was used.
