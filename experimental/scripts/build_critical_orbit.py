#!/usr/bin/env python3
"""Build the self-contained critical DAG + orbit app from prize_dag.json.

One command, three outputs, zero hand-editing:
  1. critical_dag.json - the req-ancestry of the two grand nodes, each
     node carrying exactly one of four labels:
       PROVED | PROVABLE | CONDITIONAL | UNPROVED
     (CONDITIONAL = status CONDITIONAL with wired hypotheses, or
      validator-RIPE: proven/provable conditional on predicates.)
  2. prize_dag_critical_radial.svg - rendered from the same derivation.
  3. critical_orbit.html - the app, stats computed from (1).

Usage: python3 experimental/scripts/build_critical_orbit.py
"""
import json
import os
import importlib.util
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "renderer", os.path.join(HERE, "render_prize_dag_svg.py"))
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)


def derive():
    d = json.load(open(R.DAG))
    nodes = {n["id"]: n for n in d["nodes"]}
    req = [(e["from"], e["to"]) for e in d["edges"]
           if e.get("kind", "req") == "req"]
    rev = defaultdict(list)
    for u, v in req:
        rev[v].append(u)
    crit = set(g for g in R.GRANDS if g in nodes)
    stack = list(crit)
    while stack:
        v = stack.pop()
        for u in rev[v]:
            if u not in crit:
                crit.add(u)
                stack.append(u)
    alt = [(e["from"], e["to"]) for e in d["edges"] if e.get("kind") == "alt"]
    grew = True
    while grew:
        grew = False
        for u, v in alt:
            if v in crit and u not in crit and nodes[u]["status"] != "REFUTED" \
                    and nodes[v].get("gate") == "any":
                crit.add(u)
                grew = True
                st2 = [u]
                while st2:
                    w = st2.pop()
                    for x in rev[w]:
                        if x not in crit:
                            crit.add(x)
                            st2.append(x)
    _, amber, _ = R.open_classes(nodes, req, crit)
    def label(v):
        st = nodes[v]["status"]
        if st == "PROVED":
            return "PROVED"
        if st == "PROVABLE":
            return "PROVABLE"
        return "CONDITIONAL" if v in amber else "UNPROVED"
    out = {
        "derived_from": "prize_dag.json",
        "labels": ["PROVED", "PROVABLE", "CONDITIONAL", "UNPROVED"],
        "nodes": [{"id": v, "label": label(v),
                   "title": nodes[v].get("title", "")[:160]}
                  for v in sorted(crit)],
        "edges": [{"from": u, "to": v} for u, v in req
                  if u in crit and v in crit]
                 + [{"from": u, "to": v, "kind": "alt"} for u, v in alt
                    if u in crit and v in crit and nodes[v].get("gate") == "any"],
    }
    path = os.path.join(HERE, "..", "data", "prize-dag", "critical_dag.json")
    json.dump(out, open(path, "w"), indent=1)
    return out


def main():
    cd = derive()
    R.radial()
    svg = open(os.path.join(HERE, "..", "data", "prize-dag",
                            "prize_dag_critical_radial.svg")).read()
    c = defaultdict(int)
    for n in cd["nodes"]:
        c[n["label"]] += 1
    stats = (f'<div class="stat"><b>{len(cd["nodes"])}</b><span>critical nodes</span></div>\n'
             f'<div class="stat"><b style="color:#15803d">{c["PROVED"]}</b><span>proved</span></div>\n'
             f'<div class="stat"><b style="color:#86efac">{c["PROVABLE"]}</b><span>provable</span></div>\n'
             f'<div class="stat"><b style="color:#f59e0b">{c["CONDITIONAL"]}</b><span>conditional on predicates</span></div>\n'
             f'<div class="stat red"><b>{c["UNPROVED"]}</b><span>unproved</span></div>')
    html = HTML.replace("__STATS__", stats).replace("__SVG__", svg)
    out = os.path.join(HERE, "..", "data", "prize-dag", "critical_orbit.html")
    open(out, "w").write(html)
    print(f"critical_dag.json: {dict(c)} | app: {out}")


HTML = """<title>rs-mca prize DAG — critical orbit</title>
<style>
:root{--ground:#0b1220;--panel:#101a2d;--line:#1d2a44;--ink:#dbe4f0;--muted:#7e8ba3;
--spine:#4ade80;--frontier:#f87171;--amber:#f59e0b;}
html,body{margin:0;padding:0;background:var(--ground);color:var(--ink);
font:15px/1.55 "Avenir Next","Segoe UI",system-ui,sans-serif;}
.wrap{max-width:1280px;margin:0 auto;padding:28px 20px 40px;}
header{display:flex;align-items:baseline;justify-content:space-between;flex-wrap:wrap;gap:8px;
border-bottom:1px solid var(--line);padding-bottom:14px;margin-bottom:14px;}
h1{font-size:19px;font-weight:600;margin:0;}
.eyebrow{font:11px/1 ui-monospace,Menlo,monospace;color:var(--muted);
text-transform:uppercase;letter-spacing:.14em;display:block;margin-bottom:6px;}
.stats{display:flex;gap:26px;flex-wrap:wrap;margin:2px 0 16px;}
.stat b{display:block;font:600 20px/1.2 ui-monospace,Menlo,monospace;font-variant-numeric:tabular-nums;}
.stat span{font-size:12px;color:var(--muted);}
.stat.red b{color:var(--frontier);}
.map{position:relative;background:var(--panel);border:1px solid var(--line);
border-radius:8px;overflow:hidden;height:76vh;min-height:480px;}
.map svg{width:100%;height:100%;display:block;cursor:grab;}
.map svg:active{cursor:grabbing;}
.hint{position:absolute;top:10px;right:12px;font:11px ui-monospace,Menlo,monospace;
color:var(--muted);background:rgba(11,18,32,.75);padding:4px 8px;border-radius:5px;}
.note{color:var(--muted);font-size:13.5px;max-width:70ch;margin-top:14px;}
.note b{color:var(--ink);} .note .g{color:var(--spine);font-weight:600;}
.note .r{color:var(--frontier);font-weight:600;} .note .a{color:var(--amber);font-weight:600;}
</style>
<div class="wrap">
<header><div><span class="eyebrow">rs-mca &middot; proximity prize &middot; critical orbit</span>
<h1>The prize at the centre — implication flows inward</h1></div></header>
<div class="stats">__STATS__</div>
<div class="map" id="map">__SVG__<div class="hint">drag to pan &middot; wheel to zoom &middot; hover to isolate &middot; double-click resets</div></div>
<p class="note"><b>The colour contract:</b> <span class="g">green</span> = proven (light green =
provable, write-up pending); <span class="a">amber</span> = proven or provable conditional on its
predicate nodes; <span class="r">red</span> = unproved — one proof remains to be written at this
node. Every arc carries the colour of its source; rings are implication depth. Built by
<code>experimental/scripts/build_critical_orbit.py</code> — stats and map derive from the same
<code>critical_dag.json</code>, so they cannot drift.</p>
</div>
<script>
(function(){
const svg=document.querySelector('#map svg');
const vb0=svg.getAttribute('viewBox').split(' ').map(Number);
let vb=vb0.slice(),drag=null;
function apply(){svg.setAttribute('viewBox',vb.join(' '));}
svg.addEventListener('wheel',e=>{e.preventDefault();const s=e.deltaY>0?1.12:0.89;
const r=svg.getBoundingClientRect();
const mx=vb[0]+(e.clientX-r.left)/r.width*vb[2],my=vb[1]+(e.clientY-r.top)/r.height*vb[3];
vb=[mx-(mx-vb[0])*s,my-(my-vb[1])*s,vb[2]*s,vb[3]*s];apply();},{passive:false});
svg.addEventListener('pointerdown',e=>{drag=[e.clientX,e.clientY,...vb];svg.setPointerCapture(e.pointerId);});
svg.addEventListener('pointermove',e=>{if(!drag)return;const r=svg.getBoundingClientRect();
vb[0]=drag[2]-(e.clientX-drag[0])/r.width*vb[2];vb[1]=drag[3]-(e.clientY-drag[1])/r.height*vb[3];apply();});
svg.addEventListener('pointerup',()=>{drag=null;});
svg.addEventListener('dblclick',()=>{vb=vb0.slice();apply();});
const paths=[...svg.querySelectorAll('path[data-u]')];
svg.querySelectorAll('g[data-id]').forEach(g=>{const id=g.getAttribute('data-id');
g.addEventListener('pointerenter',()=>{paths.forEach(p=>{
const hit=p.getAttribute('data-u')===id||p.getAttribute('data-v')===id;
p.style.opacity=hit?'1':'0.06';if(hit)p.style.strokeWidth='3';});});
g.addEventListener('pointerleave',()=>{paths.forEach(p=>{p.style.opacity='';p.style.strokeWidth='';});});});
})();
</script>"""

if __name__ == "__main__":
    main()
