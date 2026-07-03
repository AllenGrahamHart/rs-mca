# Dihedral staircase deep-regime certificate

This directory contains the deterministic certificate emitted by
`experimental/scripts/verify_dihedral_staircase_deep_regime.py`.

The certificate supports
`experimental/notes/roadmaps/dihedral_staircase_deep_regime.md`: the
deep-regime exact-support staircase is valid under `3j <= n-k`, but none of
the QA.21 clean-rate candidates satisfies that condition.

Regenerate and verify:

```bash
python3 experimental/scripts/verify_dihedral_staircase_deep_regime.py --write-certificate
python3 experimental/scripts/verify_dihedral_staircase_deep_regime.py
```
