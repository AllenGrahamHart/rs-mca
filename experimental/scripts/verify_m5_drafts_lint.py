#!/usr/bin/env python3
"""Lint verifier for the A-M5 drafts (Q3R.5 dossier skeleton + QX.15
assembly draft).

Structural checks only (this is a lint, not a mathematics verifier):
  [S] required sections present in each draft;
  [R] the three per-rate sections of the dossier each carry the six
      mandatory subsections;
  [X] the rate-1/2 exclusion section exists and names the three
      residuals (the tight 3-13 bit composition, the 2,978,147-radius
      band, the -12.87-bit margin point);
  [D] every `[OPEN SLOT -> DAG: <id>]` marker is well-formed and every
      referenced id exists in experimental/data/prize-dag/prize_dag.json
      (read-only), with minimum slot counts per draft;
  [L] label hygiene: the all-caps proved-status token appears in
      neither draft (the drafts are AUDIT/SKELETON and claim nothing);
      each status line says AUDIT;
  [V] the assembly draft carries the wave-1 verdict line (s* = t*-1),
      the honest implausibility note, and [CITATION NEEDED] on the
      KLLM slots;
  [N] cross-source arithmetic on QUOTED numbers: headroom identities
      (qa3 ZM/E[X] vs qx14 in-band margins), s* = t*-1 per rate, and
      the rate-1/2 band count.

Standalone, stdlib only, deterministic. Prints PASS/FAIL per check plus
key numbers; exit 0 iff all PASS.
"""

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve()
REPO = HERE.parents[2]
ROADMAPS = REPO / "experimental" / "notes" / "roadmaps"
DOSSIER = ROADMAPS / "q3r5_three_rate_dossier_skeleton.md"
ASSEMBLY = ROADMAPS / "qx15_xr_assembly_draft.md"
DAG_JSON = REPO / "experimental" / "data" / "prize-dag" / "prize_dag.json"

SLOT_RE = re.compile(r"\[OPEN SLOT -> DAG: ([a-z0-9_]+)\]")
# The all-caps status label, as a standalone token (PROVABLE etc. do not
# match; lowercase prose references to upstream proofs are allowed).
BANNED_LABEL_RE = re.compile(r"\bPROVED\b")

failures = []
passes = 0


def check(name, ok, detail=""):
    global passes
    tag = "PASS" if ok else "FAIL"
    line = f"{tag}  {name}"
    if detail:
        line += f"  [{detail}]"
    print(line)
    if ok:
        passes += 1
    else:
        failures.append(name)


def section_bodies(text, level_prefix):
    """Split markdown into {heading: body} at a given heading level
    prefix (e.g. '## ')."""
    out = {}
    current = None
    buf = []
    for line in text.splitlines():
        if line.startswith(level_prefix) and not line.startswith(level_prefix + "#"):
            if current is not None:
                out[current] = "\n".join(buf)
            current = line[len(level_prefix):].strip()
            buf = []
        else:
            buf.append(line)
    if current is not None:
        out[current] = "\n".join(buf)
    return out


def main():
    # ---- load inputs -------------------------------------------------
    for p in (DOSSIER, ASSEMBLY, DAG_JSON):
        check(f"exists: {p.relative_to(REPO)}", p.is_file())
    if failures:
        return finish()

    dossier = DOSSIER.read_text(encoding="utf-8")
    assembly = ASSEMBLY.read_text(encoding="utf-8")
    dag = json.loads(DAG_JSON.read_text(encoding="utf-8"))
    dag_ids = {n["id"] for n in dag["nodes"]}
    check("prize_dag.json parsed (read-only)", len(dag_ids) > 200,
          f"{len(dag_ids)} node ids")

    # ---- [S] required sections --------------------------------------
    dossier_secs = section_bodies(dossier, "## ")
    for want in [
        "0. Pinned notation and conventions",
        "1. Reading B semantics (procedure-as-determination)",
        "2. The headline claim shape",
        "3. The certificate chain template",
        "4. Rate 1/4",
        "5. Rate 1/8",
        "6. Rate 1/16",
        "7. Rate 1/2: EXCLUDED (the exclusion is part of the submission)",
        "8. Global non-claims",
        "9. Open-slot index",
        "10. Verifier",
    ]:
        check(f"[S] dossier section: {want!r}", want in dossier_secs)

    assembly_secs = section_bodies(assembly, "## ")
    for want in [
        "0. Pinned notation",
        "1. The master statement (draft form)",
        "2. The three tools, post-verdict",
        "3. The composition inequality chain (named slots)",
        "4. Operating points: where the chain must land",
        "5. What remains (the exact list)",
        "6. Non-claims",
        "7. Verifier",
    ]:
        check(f"[S] assembly section: {want!r}", want in assembly_secs)

    # ---- [R] per-rate subsection completeness ------------------------
    rate_requirements = {
        "Row family": "row family",
        "Safe-side": "safe-side",
        "Unsafe-side": "unsafe-side",
        "certificate format": "per-row certificate format",
        "m-family": "m-family handling",
        "non-claims": "rate-local non-claims",
    }
    for rate_sec in ["4. Rate 1/4", "5. Rate 1/8", "6. Rate 1/16"]:
        body = dossier_secs.get(rate_sec, "").lower()
        for label, needle in rate_requirements.items():
            check(f"[R] {rate_sec}: has {label!r}", needle in body)

    # certificate chain template must name the two required anchors
    tmpl = dossier_secs.get("3. The certificate chain template", "")
    check("[R] template: stratified sum present",
          "Stratified sum" in tmpl and "B_tan + B_quot + B_ap + B_ext" in tmpl)
    check("[R] template: r2_clean_rates slot present",
          "r2_clean_rates" in tmpl)
    check("[R] template: certificate_grammar_v2 cited",
          "certificate_grammar_v2" in tmpl and "cs25_cap_v12" in tmpl)
    check("[R] template: census/exact-counts/dodge chain present",
          all(t in tmpl for t in
              ("census_bounded_scales", "census_exact_counts",
               "census_window_arithmetic", "census_dodge_selection")))
    tmpl_flat = " ".join(tmpl.split())
    check("[R] template: per-constant-m determinations present",
          "rules_m_reading" in tmpl_flat and "per constant" in tmpl_flat)

    # ---- [X] rate-1/2 exclusion + the three named residuals ----------
    excl = dossier_secs.get(
        "7. Rate 1/2: EXCLUDED (the exclusion is part of the submission)", "")
    check("[X] exclusion section non-empty", len(excl.strip()) > 200)
    check("[X] residual a: tight composition (3-13 bits)",
          "3-13 bits" in excl and "7.8 bits" in excl)
    check("[X] residual b: the 2,978,147-radius band",
          "2,978,147" in excl and "2^33" in excl and "8,592,912,738" in excl)
    check("[X] residual c: the -12.87-bit margin point",
          "-12.87" in excl and "-12.84" in excl)
    check("[X] three residuals labelled",
          all(t in excl for t in ("R-1/2-a", "R-1/2-b", "R-1/2-c")))

    # ---- [D] slot markers resolve to DAG ids -------------------------
    for name, text, min_slots in (
        ("dossier", dossier, 10),
        ("assembly", assembly, 6),
    ):
        # every occurrence of the phrase must be a well-formed marker
        raw = text.count("OPEN SLOT")
        slots = SLOT_RE.findall(text)
        check(f"[D] {name}: all OPEN SLOT markers well-formed",
              raw == len(slots), f"{len(slots)} markers / {raw} mentions")
        check(f"[D] {name}: >= {min_slots} open slots", len(slots) >= min_slots,
              f"{len(slots)} slots")
        unknown = sorted(set(s for s in slots if s not in dag_ids))
        check(f"[D] {name}: every slot id exists in prize_dag.json",
              not unknown, f"unknown={unknown}" if unknown else
              f"{len(set(slots))} distinct ids")

    # ---- [L] label hygiene -------------------------------------------
    for name, text in (("dossier", dossier), ("assembly", assembly)):
        hits = BANNED_LABEL_RE.findall(text)
        check(f"[L] {name}: no all-caps proved-status label", not hits,
              f"{len(hits)} hits" if hits else "clean")
        first = text.splitlines()
        status_line = next((l for l in first if "**Status:**" in l), "")
        check(f"[L] {name}: status line says AUDIT", "AUDIT" in status_line)

    # ---- [V] assembly verdict content ---------------------------------
    check("[V] assembly: s* = t*-1 verdict line", "`s* = t*-1`" in assembly
          or "s* = t*-1" in assembly)
    check("[V] assembly: honest implausibility note",
          "implausible" in assembly and "globalness" in assembly
          and "KLLM" in assembly)
    c3 = assembly_secs.get(
        "3. The composition inequality chain (named slots)", "")
    check("[V] assembly: KLLM slots K1-K3 named with [CITATION NEEDED]",
          all(t in c3 for t in ("K1", "K2", "K3", "[CITATION NEEDED]")))
    check("[V] assembly: q^{-(g+t-1)/4} tension recorded",
          "q^{-(g+t-1)/4}" in c3 and "poly(n)" in c3)
    remains = assembly_secs.get("5. What remains (the exact list)", "")
    check("[V] assembly: remaining list = leak/KLLM/composition",
          all(t in remains for t in
              ("LEAK ADJUDICATION", "KLLM CONSTANTS",
               "THE COMPOSITION ARITHMETIC")))

    # ---- [N] cross-source arithmetic on quoted numbers ----------------
    # headroom identities: log2 B* - log2 E[X] at the corridor edge
    # (qa3-vs-qx14 cross-check quoted in both drafts)
    log2_bstar = 127.9
    edges = {  # rate: (log2 E[X] at edge from qx14, quoted headroom)
        "1/2": (120.1, 7.8),
        "1/4": (-53.4, 181.3),
        "1/8": (-2.8, 130.7),
        "1/16": (-43.7, 171.6),
    }
    for rate, (lex, quoted) in edges.items():
        got = log2_bstar - lex
        ok = abs(got - quoted) < 0.15
        check(f"[N] headroom identity rate {rate}", ok,
              f"127.9 - ({lex}) = {got:.1f} vs quoted {quoted}")
        needle = f"{quoted}"
        target = assembly if rate != "1/2" else assembly
        check(f"[N] headroom {quoted} quoted in assembly", needle in assembly)
        if rate != "1/2":
            check(f"[N] headroom {quoted} quoted in dossier", needle in dossier)

    # Row-C headroom at A*+1: log2 B* - (ZM(A*+1) - 3 log2 n), n = 2^10
    rowc = {  # rate: (ZM(A*+1) from qa3 Table 1, quoted headroom bits)
        "1/4": (111.90, 40.1),
        "1/8": (90.23, 61.8),
        "1/16": (128.85, 23.2),
    }
    for rate, (zm, quoted) in rowc.items():
        got = 122.0 - (zm - 30.0)
        ok = abs(got - quoted) < 0.15
        check(f"[N] Row-C headroom identity rate {rate}", ok,
              f"122 - ({zm} - 30) = {got:.2f} vs quoted {quoted}")
        check(f"[N] Row-C headroom {quoted} quoted in dossier",
              str(quoted) in dossier)

    # s* = t* - 1 per rate (both drafts quote the same integers)
    tstar = {"1/2": 8592912739, "1/4": 7014660390,
             "1/8": 4722556392, "1/16": 2943177800}
    sstar = {"1/2": 8592912738, "1/4": 7014660389,
             "1/8": 4722556391, "1/16": 2943177799}
    for rate in tstar:
        check(f"[N] s* = t* - 1 at rate {rate}",
              sstar[rate] == tstar[rate] - 1,
              f"{tstar[rate]} - 1 = {sstar[rate]}")
        check(f"[N] assembly quotes t*/s* at rate {rate}",
              f"{tstar[rate]:,}" in assembly and f"{sstar[rate]:,}" in assembly)

    # the rate-1/2 band: radii in [2^33, sigma*] inclusive
    band = 8592912738 - 2**33 + 1
    check("[N] rate-1/2 band count", band == 2978147,
          f"8,592,912,738 - 2^33 + 1 = {band:,}")

    return finish()


def finish():
    total = passes + len(failures)
    print()
    print(f"== {passes}/{total} checks PASS, {len(failures)} FAIL ==")
    if failures:
        for f in failures:
            print(f"   FAILED: {f}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
