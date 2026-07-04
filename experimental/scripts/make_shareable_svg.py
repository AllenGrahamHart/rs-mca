#!/usr/bin/env python3
"""Wrap the derived radial SVG into a standalone, shareable image: same map,
with a title, live stat counts, and the colour/line legend baked in — so the
file explains itself with no surrounding HTML. Reads critical_dag.json for the
counts and prize_dag_critical_radial.svg for the graph; writes
prize_map_shareable.svg next to them. Idempotent; safe to call from the build."""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))


def _find(base):
    for cand in (
        os.path.join(base, "..", "orbit"),
        os.path.join(base, "..", "data", "prize-dag"),
    ):
        svg = os.path.join(cand, "prize_dag_critical_radial.svg")
        cd = os.path.join(cand, "critical_dag.json")
        if os.path.exists(svg) and os.path.exists(cd):
            return cand, svg, cd
    raise SystemExit("shareable-svg: source svg / critical_dag.json not found")


def build(base=HERE):
    outdir, svg_path, cd_path = _find(base)
    svg = open(svg_path).read()
    cd = json.load(open(cd_path))
    c = {"PROVED": 0, "PROVABLE": 0, "CONDITIONAL": 0, "UNPROVED": 0}
    for n in cd["nodes"]:
        c[n["label"]] = c.get(n["label"], 0) + 1
    total = len(cd["nodes"])

    m = re.search(r'viewBox="0 0 (\d+(?:\.\d+)?) (\d+(?:\.\d+)?)"', svg)
    W, H = float(m.group(1)), float(m.group(2))
    TOP, BOT = 360.0, 380.0
    NEW_H = H + TOP + BOT
    body = svg[svg.index("</defs>") + len("</defs>"):svg.rindex("</svg>")]
    defs = svg[svg.index("<defs>"):svg.index("</defs>") + len("</defs>")]

    ink, muted = "#dbe4f0", "#7e8ba3"
    pal = [("PROVED", "#15803d", "proved"),
           ("PROVABLE", "#86efac", "provable"),
           ("CONDITIONAL", "#f59e0b", "conditional on predicates"),
           ("UNPROVED", "#f87171", "unproved (open obligation)")]

    # header: title + subtitle + stat row
    hdr = [
        f'<text x="{W/2:.0f}" y="150" fill="{ink}" font-size="104" '
        f'font-weight="600" text-anchor="middle">rs-mca &#183; proximity prize '
        f'&#183; critical orbit</text>',
        f'<text x="{W/2:.0f}" y="238" fill="{muted}" font-size="52" '
        f'text-anchor="middle">The prize at the centre &#8212; implication flows '
        f'inward. {total} critical nodes.</text>',
    ]
    labels = [(f'{c["PROVED"]} proved', "#15803d"),
              (f'{c["PROVABLE"]} provable', "#86efac"),
              (f'{c["CONDITIONAL"]} conditional', "#f59e0b"),
              (f'{c["UNPROVED"]} open', "#f87171")]
    seg = W / len(labels)
    for i, (txt, col) in enumerate(labels):
        cx = seg * (i + 0.5)
        hdr.append(f'<text x="{cx:.0f}" y="325" fill="{col}" font-size="62" '
                   f'font-weight="700" text-anchor="middle">{txt}</text>')

    # footer legend: row 1 = four colour swatches; row 2 = line/arc notes
    fy = TOP + H + 96
    leg = []
    sw = W / len(pal)
    for i, (_k, col, desc) in enumerate(pal):
        x = sw * i + 70
        leg.append(f'<circle cx="{x:.0f}" cy="{fy-16:.0f}" r="26" fill="{col}"/>')
        leg.append(f'<text x="{x+46:.0f}" y="{fy:.0f}" fill="{ink}" '
                   f'font-size="44">{desc}</text>')
    fy2 = TOP + H + 196
    lx = W / 2 - 700
    leg.append(f'<line x1="{lx:.0f}" y1="{fy2-16:.0f}" x2="{lx+70:.0f}" '
               f'y2="{fy2-16:.0f}" stroke="{muted}" stroke-width="5" '
               f'stroke-dasharray="14 10"/>')
    leg.append(f'<text x="{lx+90:.0f}" y="{fy2:.0f}" fill="{ink}" '
               f'font-size="44">dashed arc = alternative route (one suffices)</text>')
    leg.append(f'<text x="{W/2:.0f}" y="{fy2+86:.0f}" fill="{muted}" '
               f'font-size="40" text-anchor="middle">Every arc carries its '
               f'source node&#8217;s colour; rings are implication depth.</text>')

    out = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {NEW_H:.0f}" '
        f'font-family="Helvetica,Arial,sans-serif">\n{defs}\n'
        f'<rect width="{W:.0f}" height="{NEW_H:.0f}" fill="#0b1220"/>\n'
        + "\n".join(hdr) + "\n"
        + f'<g transform="translate(0,{TOP:.0f})">' + body + "</g>\n"
        + "\n".join(leg) + "\n</svg>\n"
    )
    dest = os.path.join(outdir, "prize_map_shareable.svg")
    open(dest, "w").write(out)
    print(f"shareable svg: {dest}  ({total} nodes, {os.path.getsize(dest)//1024} KB)")
    return dest


if __name__ == "__main__":
    build()
