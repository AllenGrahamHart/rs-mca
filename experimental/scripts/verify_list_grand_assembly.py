#!/usr/bin/env python3
"""Verifier for the list_grand assembly implication packet.

Checks (1) the five req edges into list_grand exist; (2) every statement
the packet quotes still matches the live DAG (sha256 pins); (3) the
rate-1/2 coverage wire (rate_half_coverage_gap -> list_adjacency_closing)
is present. Any statement edit FAILS this packet: re-referee then re-pin.
"""
import json, hashlib, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
DAG = os.path.join(HERE, "..", "data", "prize-dag", "prize_dag.json")
NOTE = os.path.join(HERE, "..", "notes", "roadmaps", "list_grand_assembly_implication.md")
d = json.load(open(DAG))
nodes = {n["id"]: n for n in d["nodes"]}
edges = {(e["from"], e["to"], e.get("kind", "req")) for e in d["edges"]}
kids = ["s0_zero_open", "list_safe", "list_unsafe", "mixed_radix_frontier",
        "list_adjacency_closing"]
fails = 0
def check(ok, msg):
    global fails
    print(("PASS" if ok else "FAIL") + ": " + msg)
    fails += 0 if ok else 1
for k in kids:
    check((k, "list_grand", "req") in edges, f"req edge {k} -> list_grand")
check(("rate_half_coverage_gap", "list_adjacency_closing", "req") in edges,
      "rate-1/2 coverage wired into the exhibit node")
pins = dict(re.findall(r"- `([a-z0-9_]+)`: sha256/16 = `([0-9a-f]{16})`",
                       open(NOTE).read()))
for k in ["list_grand"] + kids:
    s = nodes[k].get("statement") or nodes[k].get("title", "")
    h = hashlib.sha256(s.encode()).hexdigest()[:16]
    check(pins.get(k) == h, f"statement pin {k} ({h})")
check(nodes["list_grand"]["status"] in ("CONDITIONAL", "PROVED"),
      "list_grand status reflects the implication (CONDITIONAL until children land)")
print(f"{'OK' if fails == 0 else 'FAILED'}: {13 - fails}/13")
sys.exit(1 if fails else 0)
