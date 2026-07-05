# Chain-compression policy (frontier + interface)

Adopted 2026-07-05. Applies to the critical DAG.

## The rule

A segment of >= 3 consecutive CONDITIONAL nodes that (a) each have all their
consumers inside the segment (single exit), and (b) are restatements of ONE
obligation at different resolution, is compressed to a **pair**:

- **FRONTIER** (deep end): the one honest open obligation. Colored by its true
  state (red/amber). This is where proof/falsification effort aims.
- **INTERFACE** (top end): the statement the rest of the DAG consumes. Upstream
  cites only this.

The middle links are demoted from graph structure to proof content: a
**reduction packet** (`REDUCTION_PACKET.md` on the interface node) records each
step with its statement, status, verification evidence, and the archive path of
its folder. Side-inputs (reqs of middle nodes from outside the segment) are
REATTACHED as direct reqs of the interface — nothing is silently dropped.

## Why a pair, not one node

Collapsing to one node hides the reduction distance (what is owed vs what is
delivered) — that gap is real information. Keeping the full chain has a
measured cost: **re-pose propagation debt** (a repair at the bottom silently
invalidates every interface above it — the dli sup/weighted incoherence needed
6 consumer fixes) and **overfocus** (attention lands on whichever single node
is red, though the segment stands or falls together). With a pair, a frontier
re-pose forces re-checking exactly one edge.

## Discipline: compress only STABLE material

Compress only after the segment has survived the falsification knife: middle
links validated (or falsified-and-repaired), quantifiers coherent end-to-end.
Compressing unvalidated chains buries exactly the places where errors lurk.
Autonomous falsification loops should FLAG compression candidates, not compress
mid-sweep.

## Mechanics

1. Verify containment: every middle node's consumers lie inside the segment
   (or are the interface). Abort if not — that node is itself an interface.
2. Write the reduction packet on the interface node (step list, statuses,
   evidence, archive pointers).
3. Reattach external side-reqs to the interface. Add frontier -> interface edge.
4. Remove middle nodes from dag.json; archive their folders under
   `archive/compressed_<segment>_<date>/`.
5. dag_commit ritual (validator, orbit, artifact refresh, fork sync).

## Log

- 2026-07-05: dli chain (leaf -> dirichlet_log_integral, 14 middle nodes)
  compressed after end-to-end weighted re-pose + exhaustive consumer validation.
- pending: petal chain (chargeability -> residue_line_uniformity) — waits for
  the enrichment-vs-c measurement to decide where the stable frontier sits.
