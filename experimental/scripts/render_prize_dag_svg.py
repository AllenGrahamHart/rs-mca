#!/usr/bin/env python3
"""Render the prize DAG to SVG with critical-path glow semantics.

Stdlib only (no graphviz). Layout: longest-path layering toward the
grand targets + barycenter ordering sweeps. Styling:
  - soft GREEN glow: req edges out of PROVED/PROVABLE nodes on the
    critical req-path to the grand targets (the conquered spine);
  - soft RED glow: req edges out of still-open nodes (TARGET /
    CONJECTURE / CONDITIONAL / TEST / WALL) on the critical path (the
    live frontier - currently the terminal-bound cluster);
  - everything else (ev edges, support nodes) dim gray.
Nodes are colored by status; every node carries a hover <title> with
its full id, status, and title. Open critical nodes are labeled.

Usage: python3 experimental/scripts/render_prize_dag_svg.py
Writes: experimental/data/prize-dag/prize_dag.svg
"""
import json
import html
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DAG = os.path.join(HERE, "..", "data", "prize-dag", "prize_dag.json")
OUT = os.path.join(HERE, "..", "data", "prize-dag", "prize_dag.svg")

GRANDS = {"mca_grand", "list_grand"}
OPEN = {"TARGET", "CONJECTURE", "CONDITIONAL", "TEST", "WALL"}
DONE = {"PROVED", "PROVABLE"}

FILL = {"PROVED": "#15803d", "PROVABLE": "#86efac", "CONDITIONAL": "#f59e0b",
        "TARGET": "#ef4444", "CONJECTURE": "#fb923c", "TEST": "#a78bfa",
        "WALL": "#7f1d1d", "REFUTED": "#9ca3af"}


def main():
    d = json.load(open(DAG))
    nodes = {n["id"]: n for n in d["nodes"]}
    edges = [(e["from"], e["to"], e.get("kind", "req")) for e in d["edges"]
             if e["from"] in nodes and e["to"] in nodes]

    consumers = defaultdict(list)   # via req edges only (proof flow)
    for u, v, k in edges:
        if k == "req":
            consumers[u].append(v)

    # critical-relevant: req-path to a grand target
    crit = set()
    stack = [i for i in GRANDS if i in nodes]
    crit.update(stack)
    rev = defaultdict(list)
    for u, v, k in edges:
        if k == "req":
            rev[v].append(u)
    while stack:
        v = stack.pop()
        for u in rev[v]:
            if u not in crit:
                crit.add(u)
                stack.append(u)

    # layering: longest path distance TO a grand (grands at rank 0)
    from functools import lru_cache
    import sys
    sys.setrecursionlimit(10000)

    @lru_cache(maxsize=None)
    def rank(v):
        outs = [w for w in consumers.get(v, [])]
        if not outs:
            return 0 if v in GRANDS else 1
        return 1 + max(rank(w) for w in outs)

    ranks = {v: rank(v) for v in nodes}
    maxr = max(ranks.values())

    layers = defaultdict(list)
    for v, r in ranks.items():
        layers[r].append(v)

    # barycenter ordering sweeps
    pos = {}
    for r in layers:
        for i, v in enumerate(sorted(layers[r])):
            pos[v] = i
    neigh = defaultdict(list)
    for u, v, k in edges:
        neigh[u].append(v)
        neigh[v].append(u)
    for _ in range(6):
        for r in sorted(layers):
            lay = layers[r]
            lay.sort(key=lambda v: (sum(pos[w] for w in neigh[v]) / len(neigh[v])
                                    if neigh[v] else pos[v]))
            for i, v in enumerate(lay):
                pos[v] = i

    DX, DY, R0 = 150, 26, 5
    W = (maxr + 2) * DX
    H = (max(len(l) for l in layers.values()) + 2) * DY
    X = {v: W - (ranks[v] + 1) * DX for v in nodes}          # grands at right
    Y = {}
    for r, lay in layers.items():
        off = (H - len(lay) * DY) / 2
        for i, v in enumerate(lay):
            Y[v] = off + (i + 0.5) * DY

    def edge_class(u, v, k):
        if k != "req" or u not in crit or v not in crit:
            return "dim"
        return "green" if nodes[u]["status"] in DONE else \
               ("red" if nodes[u]["status"] in OPEN else "dim")

    parts = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'font-family="Helvetica,Arial,sans-serif">')
    parts.append("""<defs>
 <filter id="glow-green" x="-60%" y="-60%" width="220%" height="220%">
  <feGaussianBlur stdDeviation="2.6" result="b"/>
  <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
 </filter>
 <filter id="glow-red" x="-60%" y="-60%" width="220%" height="220%">
  <feGaussianBlur stdDeviation="3.2" result="b"/>
  <feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
 </filter>
</defs>""")
    parts.append(f'<rect width="{W}" height="{H}" fill="#0b1220"/>')

    order = {"dim": 0, "green": 1, "red": 2}
    for u, v, k in sorted(edges, key=lambda e: order[edge_class(*e)]):
        cls = edge_class(u, v, k)
        x1, y1, x2, y2 = X[u], Y[u], X[v], Y[v]
        mx = (x1 + x2) / 2
        path = f"M{x1:.0f},{y1:.0f} C{mx:.0f},{y1:.0f} {mx:.0f},{y2:.0f} {x2:.0f},{y2:.0f}"
        if cls == "green":
            parts.append(f'<path d="{path}" fill="none" stroke="#4ade80" '
                         f'stroke-width="1.4" stroke-opacity="0.85" filter="url(#glow-green)"/>')
        elif cls == "red":
            parts.append(f'<path d="{path}" fill="none" stroke="#f87171" '
                         f'stroke-width="1.8" stroke-opacity="0.95" filter="url(#glow-red)"/>')
        else:
            parts.append(f'<path d="{path}" fill="none" stroke="#334155" '
                         f'stroke-width="0.5" stroke-opacity="0.35"/>')

    for v, n in nodes.items():
        st = n["status"]
        fill = FILL.get(st, "#64748b")
        r = R0 + (2 if v in crit else 0) + (3 if v in GRANDS else 0)
        extra = ""
        if v in crit and st in OPEN:
            extra = f'<circle cx="{X[v]:.0f}" cy="{Y[v]:.0f}" r="{r+3}" fill="none" ' \
                    f'stroke="#f87171" stroke-width="1" stroke-opacity="0.6" filter="url(#glow-red)"/>'
        tip = html.escape(f'{v} [{st}] {n.get("title", "")[:160]}')
        parts.append(
            f'<g>{extra}<circle cx="{X[v]:.0f}" cy="{Y[v]:.0f}" r="{r}" fill="{fill}" '
            f'stroke="#0b1220" stroke-width="0.8"><title>{tip}</title></circle></g>')
        if v in crit and (st in OPEN or v in GRANDS):
            label = html.escape(v[:30])
            parts.append(f'<text x="{X[v]+r+3:.0f}" y="{Y[v]+3:.0f}" font-size="7.5" '
                         f'fill="#e2e8f0">{label}</text>')

    # legend
    lx, ly = 18, 16
    leg = [("PROVED / PROVABLE critical edge (soft green glow)", "#4ade80"),
           ("open critical path — the live frontier (red glow)", "#f87171"),
           ("support / evidence (dim)", "#334155")]
    for i, (txt, col) in enumerate(leg):
        parts.append(f'<line x1="{lx}" y1="{ly+i*16}" x2="{lx+34}" y2="{ly+i*16}" '
                     f'stroke="{col}" stroke-width="2.5"/>')
        parts.append(f'<text x="{lx+42}" y="{ly+i*16+3}" font-size="10" fill="#cbd5e1">{txt}</text>')
    sx = lx
    for i, (st, col) in enumerate(FILL.items()):
        parts.append(f'<circle cx="{sx+10}" cy="{ly+58+i*14}" r="4.5" fill="{col}"/>')
        parts.append(f'<text x="{sx+20}" y="{ly+61+i*14}" font-size="9" fill="#cbd5e1">{st}</text>')

    parts.append("</svg>")
    with open(OUT, "w") as f:
        f.write("\n".join(parts))
    green = sum(1 for e in edges if edge_class(*e) == "green")
    red = sum(1 for e in edges if edge_class(*e) == "red")
    print(f"wrote {OUT}: {len(nodes)} nodes, {len(edges)} edges "
          f"({green} green-glow, {red} red-glow), {maxr + 1} ranks")


if __name__ == "__main__":
    main()
