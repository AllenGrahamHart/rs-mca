#!/usr/bin/env python3
"""Generic verifier for assembly-implication packets (the radial sweep).

For each manifest entry: (1) every kid has a req edge into the node;
(2) every pinned statement still matches the live DAG (sha256/16);
(3) the node's status is CONDITIONAL or PROVED. Any statement edit
fails the entry: re-referee, then re-pin."""
import json, hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "..", "data", "prize-dag", "prize_dag.json")))
nodes = {n["id"]: n for n in d["nodes"]}
edges = {(e["from"], e["to"], e.get("kind", "req")) for e in d["edges"]}
man = json.load(open(os.path.join(HERE, "..", "data", "certificates",
                                  "assembly-implications", "manifest.json")))
fails = 0
for ent in man["entries"]:
    v = ent["node"]
    ok = True
    for k in ent["kids"]:
        if (k, v, "req") not in edges:
            print(f"FAIL: {v}: missing req edge {k} -> {v}"); ok = False
    for k, pin in ent["pins"].items():
        s = nodes[k].get("statement") or nodes[k].get("title", "")
        h = hashlib.sha256(s.encode()).hexdigest()[:16]
        if h != pin:
            print(f"FAIL: {v}: statement pin drift on {k} ({h} != {pin})"); ok = False
    if nodes[v]["status"] not in ("CONDITIONAL", "PROVED"):
        print(f"FAIL: {v}: status {nodes[v]['status']} does not reflect the packet"); ok = False
    print(("PASS: " if ok else "ENTRY FAILED: ") + v)
    fails += 0 if ok else 1
print(f"{'OK' if not fails else 'FAILED'}: {len(man['entries']) - fails}/{len(man['entries'])} entries")
sys.exit(1 if fails else 0)
