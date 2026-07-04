#!/usr/bin/env python3
"""Check critical-DAG flip packet fragments against the live DAG.

This verifier intentionally does not apply flips. It checks that each
flip_packets/*.json fragment names an existing packet, that the listed req
children match the live prize DAG, and that every pinned statement hash still
matches. A pin drift means the packet must be re-refereed.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
DAG = ROOT / "experimental/data/prize-dag/prize_dag.json"
CRITICAL = ROOT / "experimental/data/prize-dag/critical_dag.json"
PACKETS = ROOT / "experimental/notes/roadmaps/flip_packets"
ALLOWED_VERDICTS = {
    "PROMOTE-CONDITIONAL",
    "PROMOTE-PROVED",
    "PROMOTE-PROVABLE",
    "TRUE RED",
    "DEFECT",
}


def pin(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]


def main() -> int:
    dag = json.loads(DAG.read_text())
    critical = json.loads(CRITICAL.read_text())
    nodes = {n["id"]: n for n in dag["nodes"]}
    critical_nodes = {n["id"]: n for n in critical["nodes"]}
    req_children: dict[str, list[str]] = {}
    for edge in dag["edges"]:
        if edge.get("kind", "req") == "req":
            req_children.setdefault(edge["to"], []).append(edge["from"])
    for kids in req_children.values():
        kids.sort()

    fails = 0
    packet_paths = sorted(PACKETS.glob("*.json"))
    if not packet_paths:
        print("FAIL: no flip packet fragments found")
        return 1

    for path in packet_paths:
        entry = json.loads(path.read_text())
        node_id = entry["node"]
        ok = True

        if entry.get("schema") != "critical-dag-flip-packet-v1":
            print(f"FAIL: {path.name}: bad schema {entry.get('schema')!r}")
            ok = False
        if entry.get("verdict") not in ALLOWED_VERDICTS:
            print(f"FAIL: {path.name}: bad verdict {entry.get('verdict')!r}")
            ok = False
        if node_id not in nodes:
            print(f"FAIL: {path.name}: unknown node {node_id}")
            ok = False
        packet = ROOT / entry.get("packet", "")
        if not packet.exists():
            print(f"FAIL: {path.name}: missing packet note {packet}")
            ok = False

        _integ = entry.get("integrated")
        if _integ:
            _want = {"CONDITIONAL": ("CONDITIONAL",), "PROVED": ("PROVED", "PROVABLE")}.get(
                _integ.get("applied_as"))
            _st = nodes.get(node_id, {}).get("status")
            if _want is None or _st in _want:
                print(f"PASS (integrated as {_integ.get('applied_as')}): {node_id}")
                continue
            print(f"FAIL: {node_id}: integrated as {_integ.get('applied_as')} but live status {_st}")
            ok = False
            continue
        if node_id not in critical_nodes:
            print(f"FAIL: {path.name}: node {node_id} is not in critical_dag")
            ok = False
        expected_kids = req_children.get(node_id, [])
        listed_kids = sorted(entry.get("kids", []))
        if listed_kids != expected_kids:
            print(
                f"FAIL: {path.name}: kids {listed_kids} != live req kids "
                f"{expected_kids}"
            )
            ok = False

        for pinned_id, expected in entry.get("pins", {}).items():
            if pinned_id not in nodes:
                print(f"FAIL: {path.name}: pin for unknown node {pinned_id}")
                ok = False
                continue
            statement = nodes[pinned_id].get("statement") or nodes[pinned_id].get(
                "title", ""
            )
            got = pin(statement)
            if got != expected:
                print(
                    f"FAIL: {path.name}: pin drift on {pinned_id}: "
                    f"{got} != {expected}"
                )
                ok = False

        print(("PASS: " if ok else "ENTRY FAILED: ") + node_id)
        fails += 0 if ok else 1

    print(f"{'OK' if not fails else 'FAILED'}: {len(packet_paths) - fails}/{len(packet_paths)} flip packets")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
