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

def validator_ripe():
    """The validator owns RIPE semantics (requirements met AND the node is
    discharge-only); parse its report rather than re-deriving by wiring."""
    import subprocess
    out = subprocess.run(
        ["python3", os.path.join(HERE, "verify_prize_dag.py")],
        capture_output=True, text=True).stdout
    for line in out.splitlines():
        if line.startswith("RIPE"):
            return set(x.strip() for x in line.split(":", 1)[1].split(","))
    return set()


def open_classes(nodes, req, crit):
    """LOCAL color semantics (user scheme 2026-07-04):
      green = the statement is proved (PROVED / PROVABLE);
      amber = the LOCAL implication is proved - CONDITIONAL with wired
              hypotheses, or validator-RIPE (assembly trivially pending);
      red   = no local proof of any kind: one proof (statement or
              assembly argument) remains to be written HERE.
    #red = the true remaining work inventory. Orthogonal halo signal:
    frontier reds (no red among critical req children) can start today.
    Returns (frontier_red, amber, deep_red)."""
    from collections import defaultdict
    rev = defaultdict(list)
    for u, v in req:
        rev[v].append(u)
    ripe_set = validator_ripe()
    amber = {v for v in crit if nodes[v]["status"] in OPEN
             and (nodes[v]["status"] == "CONDITIONAL" or v in ripe_set)}
    reds = {v for v in crit if nodes[v]["status"] in OPEN and v not in amber}
    frontier = {v for v in reds
                if not any(u in reds for u in rev[v] if u in crit)}
    return frontier, amber, reds - frontier


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


def radial():
    """Critical-only radial view: the grand targets at the center, rings
    by req-distance to the prize. Writes prize_dag_critical_radial.svg."""
    import math
    d = json.load(open(DAG))
    nodes = {n["id"]: n for n in d["nodes"]}
    req = [(e["from"], e["to"]) for e in d["edges"]
           if e.get("kind", "req") == "req" and e["from"] in nodes and e["to"] in nodes]
    rev = defaultdict(list)
    cons = defaultdict(list)
    for u, v in req:
        rev[v].append(u); cons[u].append(v)
    crit = set(g for g in GRANDS if g in nodes)
    stack = list(crit)
    while stack:
        v = stack.pop()
        for u in rev[v]:
            if u not in crit:
                crit.add(u); stack.append(u)
    # ring = LONGEST req-path to a grand: guarantees ring(u) > ring(v) for
    # every requirement edge u -> v, so implication always flows strictly
    # inward - the radial direction IS the direction of implication.
    import functools

    @functools.lru_cache(maxsize=None)
    def lrank(v):
        if v in GRANDS:
            return 0
        outs = [w for w in cons[v] if w in crit]
        return 1 + max(lrank(w) for w in outs) if outs else 0

    ring = {v: lrank(v) for v in crit}
    maxring = max(ring.values())
    rings = defaultdict(list)
    for v, r in ring.items():
        rings[r].append(v)
    # angular ordering: init alphabetical, then barycenter sweeps by neighbor angle
    ang = {}
    for r in rings:
        for i, v in enumerate(sorted(rings[r])):
            ang[v] = 2 * math.pi * i / len(rings[r])
    nb = defaultdict(list)
    for u, v in req:
        if u in crit and v in crit:
            nb[u].append(v); nb[v].append(u)
    def cmean(v):
        ns = [w for w in nb[v] if w in ang]
        if not ns:
            return ang[v]
        x = sum(math.cos(ang[w]) for w in ns)
        y = sum(math.sin(ang[w]) for w in ns)
        if x * x + y * y < 1e-12:
            return ang[v]
        return math.atan2(y, x) % (2 * math.pi)

    def total_arc():
        return sum(abs((ang[u] - ang[v] + math.pi) % (2 * math.pi) - math.pi)
                   for u, v in req if u in ang and v in ang)

    before = total_arc()
    # circular-mean relaxation with a minimum angular gap per ring:
    # nodes drift toward their neighbours' angles (short arcs) but keep
    # 55% of uniform spacing so labels never collide.
    for _ in range(40):
        for r in sorted(rings):
            if r == 0:
                continue
            lay = rings[r]
            m = len(lay)
            des = {v: cmean(v) for v in lay}
            lay.sort(key=lambda v: des[v])
            gap = 2 * math.pi / m * 0.55
            a = [des[v] for v in lay]
            for i in range(1, m):
                if a[i] < a[i - 1] + gap:
                    a[i] = a[i - 1] + gap
            span = a[-1] - a[0]
            if m > 1 and span > 2 * math.pi - gap:
                scale = (2 * math.pi - gap) / span
                a = [a[0] + (x - a[0]) * scale for x in a]
            for v, x in zip(lay, a):
                ang[v] = x % (2 * math.pi)
    print(f"angular relaxation: total arc length {before:.1f} -> {total_arc():.1f} rad")
    RSTEP, PAD = 92, 60
    R = (maxring + 0.5) * RSTEP + PAD
    W = H = int(2 * R + 240)
    cx, cy = W / 2, H / 2
    X, Y = {}, {}
    for v in ring:
        rr = ring[v] * RSTEP + (0 if ring[v] == 0 else 30)
        X[v] = cx + rr * math.cos(ang[v]); Y[v] = cy + rr * math.sin(ang[v])
    if all(g in ring for g in GRANDS) and len(GRANDS) == 2:
        a, b = sorted(GRANDS)
        X[a], Y[a], X[b], Y[b] = cx - 34, cy, cx + 34, cy
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
             f'font-family="Helvetica,Arial,sans-serif">']
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
    for r in range(1, maxring + 1):
        parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r*RSTEP+30}" fill="none" '
                     f'stroke="#1d2a44" stroke-width="0.7" stroke-dasharray="2 5"/>')
    leaf, staged, inh = open_classes(nodes, req, crit)

    def ecls(u):
        st = nodes[u]["status"]
        if st in DONE: return "green"
        if u in leaf: return "red"
        if u in staged: return "amber"
        if st in OPEN: return "inh"
        return "dim"
    def polar_path(x1, y1, x2, y2):
        """Natural radial-flow edge: interpolate angle and radius in polar
        space (shortest angular way), eased so the sweep happens mid-path."""
        t1, r1 = math.atan2(y1 - cy, x1 - cx), math.hypot(x1 - cx, y1 - cy)
        t2, r2 = math.atan2(y2 - cy, x2 - cx), math.hypot(x2 - cx, y2 - cy)
        dt = (t2 - t1 + math.pi) % (2 * math.pi) - math.pi
        pts = []
        N = 18
        for i in range(N + 1):
            s = i / N
            ease = s * s * (3 - 2 * s)          # smoothstep on the angle
            th = t1 + dt * ease
            rr = r1 + (r2 - r1) * s
            pts.append(f"{cx + rr * math.cos(th):.1f},{cy + rr * math.sin(th):.1f}")
        return "M" + " L".join(pts)

    order = {"dim": 0, "inh": 1, "green": 2, "amber": 3, "red": 4}
    for u, v in sorted((e for e in req if e[0] in crit and e[1] in crit),
                       key=lambda e: order[ecls(e[0])]):
        pth = polar_path(X[u], Y[u], X[v], Y[v])
        c = ecls(u)
        dat = f'data-u="{u}" data-v="{v}"'
        # ARC RULE: an arc carries the color of its SOURCE node - the
        # proof-state of the hypothesis flowing along it. (Frontier vs
        # deep red lives on the node halo, not the arc.)
        if c == "green":
            parts.append(f'<path {dat} d="{pth}" fill="none" stroke="#4ade80" stroke-width="1.3" '
                         f'stroke-opacity="0.8" filter="url(#glow-green)"/>')
        elif c in ("red", "inh"):
            parts.append(f'<path {dat} d="{pth}" fill="none" stroke="#f87171" stroke-width="1.7" '
                         f'stroke-opacity="0.9" filter="url(#glow-red)"/>')
        elif c == "amber":
            parts.append(f'<path {dat} d="{pth}" fill="none" stroke="#f59e0b" stroke-width="1.4" '
                         f'stroke-opacity="0.85"/>')
        else:
            parts.append(f'<path {dat} d="{pth}" fill="none" stroke="#475569" stroke-width="0.8" stroke-opacity="0.5"/>')
    for v in ring:
        n = nodes[v]; st = n["status"]
        fill = FILL.get(st, "#64748b")
        if v in staged:
            fill = "#f59e0b"   # class drives color: RIPE targets are amber like CONDITIONALs
        r0 = 10 if v in GRANDS else (6.5 if st in OPEN else 5.5)
        halo = ""
        if v in leaf:
            halo = f'<circle cx="{X[v]:.0f}" cy="{Y[v]:.0f}" r="{r0+3.5}" fill="none" ' \
                   f'stroke="#f87171" stroke-width="1.2" stroke-opacity="0.8" filter="url(#glow-red)"/>'
        elif v in staged:
            halo = f'<circle cx="{X[v]:.0f}" cy="{Y[v]:.0f}" r="{r0+3}" fill="none" ' \
                   f'stroke="#f59e0b" stroke-width="0.9" stroke-opacity="0.55"/>'

        tip = html.escape(f'{v} [{st}] {n.get("title","")[:160]}')
        parts.append(f'<g data-id="{v}">{halo}<circle cx="{X[v]:.0f}" cy="{Y[v]:.0f}" r="{r0}" fill="{fill}" '
                     f'stroke="#0b1220" stroke-width="1"><title>{tip}</title></circle></g>')
        if v in GRANDS or v in leaf or v in staged:
            anc = "middle" if v in GRANDS else ("start" if X[v] >= cx else "end")
            dx = 0 if v in GRANDS else (r0 + 4 if X[v] >= cx else -(r0 + 4))
            dy = -r0 - 5 if v in GRANDS else 3
            parts.append(f'<text x="{X[v]+dx:.0f}" y="{Y[v]+dy:.0f}" font-size="8.5" '
                         f'text-anchor="{anc}" fill="#e2e8f0">{html.escape(v[:32])}</text>')
    parts.append(f'<text x="{cx:.0f}" y="{cy-58:.0f}" font-size="13" text-anchor="middle" '
                 f'fill="#94a3b8" letter-spacing="2">THE PRIZE</text>')
    parts.append("</svg>")
    out = os.path.join(HERE, "..", "data", "prize-dag", "prize_dag_critical_radial.svg")
    with open(out, "w") as f:
        f.write("\n".join(parts))
    ne = sum(1 for u, v in req if u in crit and v in crit)
    print(f"wrote {out}: {len(ring)} critical nodes, {ne} critical edges, {maxring} rings")


if __name__ == "__main__" and os.environ.get("RADIAL"):
    radial()
