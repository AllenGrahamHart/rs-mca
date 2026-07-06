#!/usr/bin/env python3
"""Validator for experimental/data/prize-dag/prize_dag.json (AUDIT).

Checks: unique ids; edge endpoints exist; legal statuses/kinds/gates;
acyclicity; every node reaches the root; refs resolve to real files;
REFUTED nodes are never 'req' children; and the STATUS-PROPAGATION rule:
  PROVED    requires all 'req' children PROVED (+ one PROVED 'alt' if gate=any)
  PROVABLE  requires all 'req' children in {PROVED, PROVABLE} (alts likewise)
Also emits (informational) the RIPE list: CONJECTURE/TARGET nodes whose
requirements are already all PROVED/PROVABLE — candidates to close next.

Run:  python3 experimental/scripts/verify_prize_dag.py
Exit non-zero iff any check fails (RIPE list is informational).
"""
from __future__ import annotations

import json
import os
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))          # repo root (parent of experimental/)
DAG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dag.json")
ROADMAPS = os.path.join(REPO, "experimental", "notes", "roadmaps")

STATUSES = {"PROVED", "PROVABLE", "CONDITIONAL", "CONJECTURE", "TARGET", "WALL", "REFUTED"}
# TEST retired 2026-07-06 (node-semantics law): every node is a truth claim; a computation
# is the PROOF of a claim ("this program on this input yields X"), never a status.
KINDS = {"req", "alt", "ev", "ref"}
GATES = {"all", "any"}


def main() -> None:
    with open(DAG) as fh:
        data = json.load(fh)
    nodes = {n["id"]: n for n in data["nodes"]}
    edges = data["edges"]
    errors: list[str] = []

    if len(nodes) != len(data["nodes"]):
        errors.append("duplicate node ids")
    root = data["root"]
    if root not in nodes:
        errors.append(f"root {root} missing")

    for n in data["nodes"]:
        if n["status"] not in STATUSES:
            errors.append(f"{n['id']}: illegal status {n['status']}")
        if n.get("gate", "all") not in GATES:
            errors.append(f"{n['id']}: illegal gate")
        for ref in n.get("refs", []):
            path = ref.split("#")[0]
            if not (os.path.exists(os.path.join(ROADMAPS, path))
                    or os.path.exists(os.path.join(REPO, path))):
                _p = str(path)
                if not _p.startswith(("nodes/", "tools/", "orbit/")):
                    continue  # legacy fork pointer (vendored history), recorded in the node folder
                _root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
                if os.path.exists(os.path.join(_root, _p)):
                    continue
                errors.append(f"{n['id']}: ref does not resolve: {path}")

    out: dict[str, list[str]] = {i: [] for i in nodes}
    inc: dict[str, list[tuple[str, str]]] = {i: [] for i in nodes}
    for e in edges:
        if e["from"] not in nodes or e["to"] not in nodes:
            errors.append(f"edge endpoint missing: {e}")
            continue
        if e["kind"] not in KINDS:
            errors.append(f"illegal edge kind: {e}")
            continue
        out[e["from"]].append(e["to"])
        inc[e["to"]].append((e["from"], e["kind"]))
        if e["kind"] == "req" and nodes[e["from"]]["status"] == "REFUTED":
            errors.append(f"REFUTED node {e['from']} is a 'req' child of {e['to']}")

    # RED-LEAF LAW (added 2026-07-05): a TARGET/CONJECTURE with proof closure is an
    # open obligation — no implication is proved, so nothing can be its logical
    # hypothesis. Such nodes must be logical LEAVES: only 'ev'/'ref' in-edges.
    # (Deliverable-assembly targets, closure == 'artifact', are exempt: their req
    # edges mean staged ingredients / RIPE-when-green.)
    for n in data["nodes"]:
        if n["status"] in ("TARGET", "CONJECTURE") and n.get("closure") != "artifact":
            badk = [(f, k) for (f, k) in inc[n["id"]] if k in ("req", "alt")]
            if badk:
                errors.append(
                    f"{n['id']}: {n['status']} (proof closure) has logical in-edges "
                    f"{badk[:3]} — reds must be leaves; use kind 'ev' for evidence/ingredients")

    # leaf-conditional invariant (added 2026-07-05): CONDITIONAL means "implication
    # proved, pending wired req nodes" — a CONDITIONAL with no incoming req/alt edge
    # is hiding its hypotheses in prose (hidden red). auto_discharge skips zero-req
    # conditionals, so without this check they sit amber forever, unaudited.
    for n in data["nodes"]:
        if n["status"] == "CONDITIONAL":
            kinds = [k for (_, k) in inc[n["id"]]]
            if "req" not in kinds and "alt" not in kinds:
                errors.append(
                    f"{n['id']}: CONDITIONAL with no wired hypotheses (leaf-conditional; "
                    "wire the conditions as nodes or demote to TARGET)")

    # acyclicity (iterative DFS) + reachability to root
    color: dict[str, int] = {}
    for start in nodes:
        if color.get(start):
            continue
        stack = [(start, iter(out[start]))]
        color[start] = 1
        while stack:
            v, it = stack[-1]
            for w in it:
                if color.get(w) == 1:
                    errors.append(f"cycle through {w}")
                    color[w] = 2
                    continue
                if not color.get(w):
                    color[w] = 1
                    stack.append((w, iter(out[w])))
                    break
            else:
                color[v] = 2
                stack.pop()
    reach = {root}
    frontier = [root]
    rev: dict[str, list[str]] = {i: [] for i in nodes}
    for e in edges:
        if e["to"] in rev:
            rev[e["to"]].append(e["from"])
    while frontier:
        v = frontier.pop()
        for w in rev[v]:
            if w not in reach:
                reach.add(w)
                frontier.append(w)
    for i in nodes:
        if i not in reach:
            errors.append(f"{i} cannot reach the root")

    # status propagation + RIPE list
    ripe: list[str] = []
    okset = {"PROVED"}
    okset2 = {"PROVED", "PROVABLE"}
    for i, n in nodes.items():
        reqs = [nodes[f]["status"] for f, k in inc[i] if k == "req"]
        alts = [nodes[f]["status"] for f, k in inc[i] if k == "alt"]
        gate_any = n.get("gate", "all") == "any" and alts
        if n["status"] == "PROVED":
            if any(s not in okset for s in reqs) or (gate_any and not any(s in okset for s in alts)):
                errors.append(f"{i}: declared PROVED but requirements are not all PROVED")
        elif n["status"] == "PROVABLE":
            if any(s not in okset2 for s in reqs) or (gate_any and not any(s in okset2 for s in alts)):
                errors.append(f"{i}: declared PROVABLE but requirements exceed PROVED/PROVABLE")
        elif n["status"] in {"CONJECTURE", "TARGET"} and (reqs or gate_any):
            # own-content rule: a node carrying an attack_surface has open
            # mathematical work of its own - requirements-met never makes it
            # declaration-ready, it makes it ACTIONABLE.
            if n.get("attack_surface"):
                continue
            if all(s in okset2 for s in reqs) and (not gate_any or any(s in okset2 for s in alts)):
                ripe.append(i)

    # critical-set analysis: which OPEN nodes lie on EVERY route to the root?
    SAT = {"PROVED", "PROVABLE", "CONDITIONAL"}
    open_ids = [i for i, n in nodes.items()
                if n["status"] not in SAT and n["status"] != "REFUTED"]
    import functools
    def satisfiable(granted: frozenset) -> bool:
        memo: dict[str, bool] = {}
        def sat(v: str) -> bool:
            if v in memo:
                return memo[v]
            memo[v] = False              # cycle guard (graph is acyclic anyway)
            n = nodes[v]
            if n["status"] == "REFUTED":
                memo[v] = False
                return False
            reqs = [f for f, k in inc[v] if k == "req"]
            alts = [f for f, k in inc[v] if k == "alt"]
            base = n["status"] in SAT or v in granted
            req_ok = all(sat(f) for f in reqs)
            alt_ok = (not (n.get("gate", "all") == "any" and alts)) or any(sat(f) for f in alts)
            # SAT-status nodes still owe their hypothesis edges (CONDITIONAL!);
            # open nodes additionally need to be granted themselves.
            memo[v] = req_ok and alt_ok and (base if n["status"] not in SAT else True)
            return memo[v]
        return sat(root)
    all_granted = frozenset(open_ids)
    if satisfiable(all_granted):
        critical = [x for x in open_ids
                    if not satisfiable(frozenset(i for i in open_ids if i != x))]
        print("CRITICAL open nodes (on EVERY route to the prize):")
        for c in sorted(critical):
            print(f"  ! {c}: {nodes[c]['title'][:66]} [{nodes[c]['status']}]")
        # precision invariant: critical nodes must carry an exact statement
        for c in sorted(critical):
            if not nodes[c].get("statement"):
                errors.append(f"{c}: CRITICAL but has no 'statement' field (precision invariant)")
        # (2026-07-05) the same for critical CONDITIONALs: an amber with no statement
        # is an unauditable implication (found: strip, f1_case_pole with empty fields)
        for i, n in nodes.items():
            if n["status"] == "CONDITIONAL" and not n.get("statement"):
                errors.append(f"{i}: CONDITIONAL with no 'statement' field (unauditable implication)")
    else:
        print("WARNING: root not satisfiable even granting all open nodes (check gates)")

    print(f"prize-dag: {len(nodes)} nodes, {len(edges)} edges")
    counts: dict[str, int] = {}
    for n in nodes.values():
        counts[n["status"]] = counts.get(n["status"], 0) + 1
    print("status counts:", ", ".join(f"{k}:{v}" for k, v in sorted(counts.items())))
    if ripe:
        print("RIPE (requirements met, declaration pending):", ", ".join(sorted(ripe)))
    if errors:
        print("\nFAIL:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    # normal-form report: CONDITIONAL requires wired open hypotheses (or it is RIPE)
    _rev = {}
    for _e in edges:
        if _e.get("kind", "req") == "req":
            _rev.setdefault(_e["to"], []).append(_e["from"])
    # LAW (amber): a CONDITIONAL node must have >= 1 wired req predicate
    # (no amber leaves), and every predicate named in its conditional.md
    # must be wired as a req edge (packet/graph coherence).
    import re as _re
    _root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "nodes")
    for _id, _n in nodes.items():
        if _n["status"] not in ("CONDITIONAL", "PROVABLE"):
            continue
        if _n["status"] == "PROVABLE":
            _sm = os.path.join(_root, _id, "sketch.md")
            if os.path.exists(_sm):
                _m2 = _re.search(r"## Predicate[s]? node[s]?\s*\n((?:\s*-\s*`[^`]+`\s*\n)+)",
                                 open(_sm).read())
                if _m2:
                    _reqs2 = set(_rev.get(_id, []))
                    for _pr2 in _re.findall(r"`([^`]+)`", _m2.group(1)):
                        if _pr2 in nodes and _pr2 not in _reqs2:
                            errors.append(f"{_id}: sketch predicate {_pr2} not wired as req")
            continue
        _reqs = set(_rev.get(_id, []))
        if not _reqs:
            errors.append(f"{_id}: AMBER LEAF - CONDITIONAL with no wired req predicate")
        _cm = os.path.join(_root, _id, "conditional.md")
        if os.path.exists(_cm):
            _m = _re.search(r"## Predicate[s]? node[s]?\s*\n((?:\s*-\s*`[^`]+`\s*\n)+)",
                            open(_cm).read())
            if _m:
                for _pr in _re.findall(r"`([^`]+)`", _m.group(1)):
                    if _pr in nodes and _pr not in _reqs:
                        errors.append(f"{_id}: packet predicate {_pr} not wired as req")
    _prose = [nid for nid, n in nodes.items() if n["status"] == "CONDITIONAL"
              and not any(nodes[u]["status"] not in ("PROVED", "PROVABLE")
                          for u in _rev.get(nid, []) if u in nodes)]
    if _prose:
        print("CONDITIONAL with no open wired hypothesis (prose-only conditions or flip-ready):",
              ", ".join(sorted(_prose)))
    _arts = sorted(n["id"] for n in data["nodes"] if n.get("closure") == "artifact")
    if _arts:
        print("ARTIFACT-KIND nodes (not truth-apt; reword to propositional core or demote):",
              ", ".join(_arts))
    # status-artifact invariant (node-per-folder layout): the folder shape
    # must match the status for every critical node that has a folder.
    _need = {"PROVED": "proof.md", "PROVABLE": "sketch.md", "CONDITIONAL": "conditional.md"}
    _root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "nodes")
    _bad = []
    for _id, _n in nodes.items():
        _dir = os.path.join(_root, _id)
        if not os.path.isdir(_dir):
            continue
        if not os.path.exists(os.path.join(_dir, "statement.md")):
            _bad.append(f"{_id}: missing statement.md")
        _want = _need.get(_n["status"])
        if _want and not os.path.exists(os.path.join(_dir, _want)):
            _bad.append(f"{_id}: status {_n['status']} but no {_want}")
    if _bad:
        print("STATUS-ARTIFACT GAPS (folders lagging statuses):", len(_bad))
        for _x in _bad[:8]:
            print("  -", _x)
    print("PASS: structure, refs, acyclicity, reachability, status propagation")


if __name__ == "__main__":
    main()
