# Compact Exact Certificate

The eight shards under certificate/shards contain 982 compact JSONL rows,
352246 bytes in total; no shard exceeds51084 bytes. Each row prints
[a,b] and two depth certificates, each with ten triples
(rank,chosen padded degree,integer cap). Degree zero denotes the dimension
step (S); positive degree denotes the Johnson/padding step (P) in the
required ordinary LIST theorem. No search optimality is a premise.

Manifest SHA256:
`d5515bb34f6afa52fe67b616d18967af292fbe16a64b3eecbf032ffa7009b31d`.
Credited selector SHA256:
`bac33f24d1f34760518406185fcc9850d4fc61f5441486f94237e13b99eb8ca8`.

The exact unrounded R0 is

    140127742123082010779536776164838406497727166358737692518182885976528000
    /228585129067384634786905329958427041644271285504861901.

verify.py --write generates the certificate with ShardedResultWriter,
128 rows per shard. Each completed shard leaves a hashed incomplete
manifest; only successful completion sets complete:true. Existing manifests
are not overwritten. An interrupted partial result is evidence only and
both replays reject it for this theorem.

Default verify.py verifies custody and reconstructs the selected rows.
verify_audit.py imports neither that script nor the selector. It reconstructs
eight polynomial identities, checks all19640 transitions directly from
the printed inequalities, verifies gap-free e coverage and all shard hashes,
and combines each envelope using integer common denominators. Nine mutations
exercise depth, interval, rank, degree and cap corruption.

The exact maximum ceiling is274136923022229951 on[103000,103999].
The small-union ceiling is204340709149309353. The same core-sixteen
recipe without the tuple refund gives334883989706620282, above budget;
this is a failed recipe, not a proof of unsafety or an impossibility theorem.

The certificate covers finite inequality choices only. Universal incidence,
basis contraction, compatibility, ownership and original-source transport
are established by the hand proof and its printed suppliers.
