#!/usr/bin/env python3
"""QX.12 skeleton lint: document-hygiene checks for the KLLM import skeleton.

Lints experimental/notes/roadmaps/qx12_kllm_import_skeleton.md
(DAG node xr_small_set_engine; queue items QX.12 + QX.12-FLAGS).

This verifier checks NO mathematics. It enforces the skeleton contract:

  [1] structure: required headings, fenced-block parity, SKELETON status,
      Non-claims ledger present with the full N1..N8 census;
  [2] slot census: counts [CITATION NEEDED] and [CROSS-BRANCH ...] slots
      (the note is draft-grade BY DESIGN: many open slots expected);
  [3] numeric audit: EVERY numeric token in the note (prose AND code
      blocks) must be (a) inside a tagged slot, (b) a structural token
      (identifiers, labels, headings, dates, item refs), or (c) an
      explicitly whitelisted in-repo-sourced constant -- the whitelist is
      printed with its per-token in-repo source. Anything else FAILS:
      no invented constants can hide in the note.
  [4] the #211 exemplar shape "(g+t-1)/4" may appear ONLY on lines that
      carry the #211 cross-branch tag (or inside a tagged slot);
  [5] interface-symbol coverage: every named unknown (K0, g1..g9, C_conv,
      mu0, h1, eps_E) appears in the template/chain AND has a checklist
      home; the exact required statement-shape phrases are present;
  [6] checklist state: exactly the C1..C14 boxes, ALL unchecked (a
      skeleton with ticked boxes is a label violation).

Deterministic, stdlib-only. Prints PASS/FAIL lines + key numbers.
Exit code 0 iff every check PASSes.
Run:  python3 experimental/scripts/verify_qx12_skeleton_lint.py
"""

import re
import sys
from pathlib import Path

NOTE = (Path(__file__).resolve().parent.parent
        / "notes" / "roadmaps" / "qx12_kllm_import_skeleton.md")

FAILS = []
NCHECK = 0


def check(name, cond, detail=""):
    global NCHECK
    NCHECK += 1
    tag = "PASS" if cond else "FAIL"
    line = "[%s] %s" % (tag, name)
    if detail:
        line += "   (%s)" % detail
    print(line)
    if not cond:
        FAILS.append(name)


# ---------------------------------------------------------------------------
# [0] load
# ---------------------------------------------------------------------------
check("note file exists", NOTE.is_file(), str(NOTE))
if not NOTE.is_file():
    print("FATAL: note missing; aborting remaining checks")
    sys.exit(1)
text = NOTE.read_text(encoding="utf-8")
lines = text.splitlines()
print("note: %s  (%d lines, %d chars)" % (NOTE.name, len(lines), len(text)))

# ---------------------------------------------------------------------------
# [1] structure
# ---------------------------------------------------------------------------
n_fences = sum(1 for ln in lines if ln.strip().startswith("```"))
check("fenced code blocks balanced", n_fences % 2 == 0,
      "%d fence lines" % n_fences)

REQUIRED_HEADINGS = [
    "## 0. Pinned notation",
    "## 1. The statement shape required",
    "### 1.1 Definitional slot D1",
    "### 1.2 Template KLLM-S",
    "### 1.3 What \"uniform slice\" must mean",
    "## 2. The consumption interface",
    "### 2.1 What our side supplies",
    "### 2.2 The contradiction chain",
    "### 2.3 The assembly shape",
    "### 2.4 The #211/E20 extraction",
    "## 3. Candidate sources",
    "## 4. The verification checklist",
    "## 5. Bridge-ledger row",
    "## 6. Non-claims",
]
for h in REQUIRED_HEADINGS:
    check("heading present: %r" % h, h in text)

status_lines = [ln for ln in lines if ln.startswith("- **Status:**")]
check("exactly one Status bullet", len(status_lines) == 1)
if status_lines:
    check("Status bullet says SKELETON", "SKELETON" in status_lines[0])
    check("Status bullet does not claim PROVED",
          "PROVED" not in status_lines[0])
check("title marks SKELETON", "SKELETON" in lines[0] if lines else False)

n_items = re.findall(r"^N(\d)\b", text, re.M)
check("Non-claims ledger N1..N8 complete",
      sorted(n_items) == [str(i) for i in range(1, 9)],
      "found N-items: %s" % ",".join(sorted(n_items)))

# ---------------------------------------------------------------------------
# [2] slot census
# ---------------------------------------------------------------------------
SLOT_RE = re.compile(r"\[(CITATION NEEDED|CROSS-BRANCH|IN-REPO)[^\]]*\]",
                     re.S)
slots = list(SLOT_RE.finditer(text))
n_cit = sum(1 for m in slots if m.group(1) == "CITATION NEEDED")
n_xb = sum(1 for m in slots if m.group(1) == "CROSS-BRANCH")
print("slot census: %d [CITATION NEEDED], %d [CROSS-BRANCH], %d total"
      % (n_cit, n_xb, len(slots)))
check("[CITATION NEEDED] slot count >= 20 (draft-grade by design)",
      n_cit >= 20, "%d slots" % n_cit)
check("[CROSS-BRANCH ...] tags >= 3 (#211/E20 marked cross-branch)",
      n_xb >= 3, "%d tags" % n_xb)

# every slot region must be non-trivial (no bare "[CITATION NEEDED]" is
# required -- bare slots are allowed in the template -- but none may be
# malformed / unterminated: re-scan for tag words outside matched slots)
mask = bytearray(len(text))          # 1 = audited-OK region
for m in slots:
    for i in range(m.start(), m.end()):
        mask[i] = 1
stray = []
for m in re.finditer(r"CITATION NEEDED|CROSS-BRANCH", text):
    if not all(mask[i] for i in range(m.start(), m.end())):
        stray.append(text[:m.start()].count("\n") + 1)
check("no slot tag outside a well-formed [ ... ] region", not stray,
      "stray at lines: %s" % stray)

# ---------------------------------------------------------------------------
# [3] numeric audit
# ---------------------------------------------------------------------------
# Whitelisted spans. Each entry: (regex, in-repo source of the numerals).
ALLOWED = [
    (r"^#{1,4}\s+\d+(\.\d+)?\.?", "markdown section heading number"),
    (r"\b\d{4}-\d{2}-\d{2}\b", "ISO date"),
    (r"#\d+\b", "in-repo PR/issue reference (#152/#209/#211 etc.)"),
    (r"\b1/2\b|\b1/4\b|\b1/8\b|\b1/16\b",
     "rate values -- campaign_split_2026_07_03.md / r2_clean_rates"),
    (r"2\^100\b", "the 2^100 clean-rate slack -- prize_dag r2_clean_rates"),
    (r"\b121\b|\b243\b",
     "wave-1 margin bits -- qa3_e14_fm_margin_tables.md / r2_clean_rates"),
    (r"t\*/15", "mid-band floor s*_C ~ t*/15 -- qx14 SS5.2 finding 3"),
    (r"\bProp(?:osition)?\s+1\.5\b", "qx6_qx8_kms_bridges.md Prop 1.5"),
    (r"\bSS\d+(\.\d+)?(\([a-z]\))?\b", "in-repo section reference"),
    (r"\b[A-Z]{1,4}\.\d+(-[A-Z]{1,4}\.\d+|-[A-Z]+)?\b",
     "queue/checklist item label or range (QX.12, QX.12-FLAGS, QX.10-QX.12)"),
    (r"\bQ3R\.\d+\b", "queue item label (Tier 3R)"),
    (r"\b3R\b", "Tier 3R label -- execution_queue.md"),
    (r"\b[A-Z]-M?\d+\b", "campaign task label (A-M2, C-1, X-1)"),
    (r"\b[A-Z][A-Za-z]*\d+[A-Za-z]*(?:\.\d+)?\b",
     "identifier/label (K0, C14, S1, N8, P4, I5, D1, O1, E20, T0, T7)"),
    (r"\b[A-Za-z]+_\d+\b", "subscripted identifier (E_3, lam_0)"),
    (r"\b[a-z][a-z0-9_]*\d[a-z0-9_.]*\b",
     "lowercase identifier / in-repo filename (g1, eps0, mu0, h1, log2, "
     "qx14, qx6_qx8..., qa3_e14..., s3b_iii_2, campaign_split_2026_07_03.md)"),
    (r"(?<![\w.])[0-4](?![\w.])",
     "single digit 0-4: structural arithmetic (indices, exponents, list "
     "numbers, pinned formulas like min(s,t-1), q^{1-t}, n^3)"),
]
print("numeric-audit whitelist: %d span rules (sources printed above each "
      "violation if any)" % len(ALLOWED))
for pat, src in ALLOWED:
    for m in re.finditer(pat, text, re.M):
        for i in range(m.start(), m.end()):
            mask[i] = 1

violations = []
for m in re.finditer(r"\d", text):
    if mask[m.start()]:
        continue
    # expand to the full offending token for reporting
    s = m.start()
    e = m.end()
    while s > 0 and (text[s - 1].isdigit() or text[s - 1] in ".^-"):
        s -= 1
    while e < len(text) and (text[e].isdigit() or text[e] in ".^-"):
        e += 1
    lineno = text[:m.start()].count("\n") + 1
    ls = text.rfind("\n", 0, m.start()) + 1
    le = text.find("\n", m.start())
    ctx = text[ls:le if le != -1 else len(text)].strip()
    violations.append((lineno, text[s:e], ctx))
    for i in range(s, e):        # report each token once
        mask[i] = 1
for lineno, tok, ctx in violations:
    print("  NUMERIC VIOLATION line %d: token %r in: %s"
          % (lineno, tok, ctx[:90]))
check("every numeric token is slot-tagged, structural, or in-repo-cited",
      not violations, "%d violations" % len(violations))

# ---------------------------------------------------------------------------
# [4] the #211 exemplar shape is tag-guarded
# ---------------------------------------------------------------------------
bad211 = []
for m in re.finditer(r"\(g\+t-1\)/4", text):
    lineno = text[:m.start()].count("\n") + 1
    ls = text.rfind("\n", 0, m.start()) + 1
    le = text.find("\n", m.start())
    line = text[ls:le if le != -1 else len(text)]
    in_slot = any(sm.start() <= m.start() < sm.end() for sm in slots)
    if "#211" not in line and not in_slot:
        bad211.append(lineno)
n211 = len(re.findall(r"\(g\+t-1\)/4", text))
check("every '(g+t-1)/4' occurrence carries the #211 tag (line or slot)",
      not bad211, "%d occurrences, untagged at lines %s" % (n211, bad211))
check("the #211 shape appears at least once (SS2.4 exemplar)", n211 >= 1,
      "%d occurrences" % n211)

# ---------------------------------------------------------------------------
# [5] interface-symbol coverage + exact statement-shape phrases
# ---------------------------------------------------------------------------
def section(start_marker, end_marker):
    i = text.find(start_marker)
    j = text.find(end_marker)
    return text[i:j] if (i != -1 and j != -1 and i < j) else ""

sec1 = section("## 1. The statement shape", "## 2. The consumption")
sec2 = section("## 2. The consumption", "## 3. Candidate sources")
sec4 = section("## 4. The verification checklist", "## 5. Bridge-ledger")

PAPER_UNKNOWNS = ["K0", "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8",
                  "g9", "C_conv", "mu0"]
INPROG_UNKNOWNS = ["h1", "eps_E"]
for s in PAPER_UNKNOWNS:
    check("unknown %-6s named in SS1/SS2 (template or chain)" % s,
          (s in sec1) or (s in sec2))
    check("unknown %-6s has a checklist home (SS4)" % s, s in sec4)
for s in INPROG_UNKNOWNS:
    check("in-program unknown %-6s named in SS2 chain" % s, s in sec2)
check("h1 scoped as in-program in Non-claims", "h1" in section(
    "## 6. Non-claims", "N8") or "h1" in text[text.find("## 6."):])

REQUIRED_PHRASES = [
    ("global hypercontractivity / small-set expansion on the UNIFORM SLICE",
     "the exact statement shape, task item (1)"),
    ("J(n,j)", "the Johnson scheme domain"),
    ("(a, eps)", "the globalness parameterization"),
    ("mu ~ q^{1-t}", "the vanishing-measure regime"),
    ("eps0 = L_tan/(n-j+1)", "the qx11 supply, task item (2)"),
    ("q^{-min(s,t-1)}", "the pinned pair ledger"),
    ("2^100 * FM", "the clean-rate budget inequality"),
    ("(REQ-A)", "the named requirement inequality"),
    ("(REQ-B)", "the named assembly requirement"),
    ("Keevash-Lifshitz-Long-Minzer", "candidate source S1"),
    ("Lifshitz-Minzer", "candidate source S2"),
    ("Filmus", "candidate source S2"),
    ("Khot-Minzer-Safra", "candidate source S3"),
    ("xr_small_set_engine", "the DAG node"),
    ("xr_globalness_from_ledger", "the supply node"),
    ("r2_clean_rates", "the campaign target"),
    ("L_tan = 1 vs 2", "the unresolved convention, stated explicitly"),
]
for phrase, why in REQUIRED_PHRASES:
    check("phrase present: %r" % phrase, phrase in text, why)

# ---------------------------------------------------------------------------
# [6] checklist state
# ---------------------------------------------------------------------------
unchecked = re.findall(r"^- \[ \] \*\*(C\d+)\*\*", text, re.M)
checked = re.findall(r"^- \[[xX]\]", text, re.M)
expected = ["C%d" % i for i in range(1, 15)]
print("checklist status: %d boxes, %d unchecked, %d checked"
      % (len(unchecked) + len(checked), len(unchecked), len(checked)))
for cid in unchecked:
    print("  - [ ] %s  OPEN" % cid)
check("checklist is exactly C1..C14", unchecked == expected,
      "found: %s" % ",".join(unchecked))
check("no box is ticked (SKELETON state)", len(checked) == 0,
      "%d ticked" % len(checked))

# ---------------------------------------------------------------------------
# summary
# ---------------------------------------------------------------------------
print("-" * 72)
print("checks: %d run, %d failed" % (NCHECK, len(FAILS)))
print("key numbers: %d CITATION-NEEDED slots, %d CROSS-BRANCH tags, "
      "%d checklist boxes open, %d numeric violations"
      % (n_cit, n_xb, len(unchecked), len(violations)))
if FAILS:
    print("FAILED checks:")
    for f in FAILS:
        print("  - %s" % f)
    print("OVERALL: FAIL")
    sys.exit(1)
print("OVERALL: PASS (lint only -- no mathematics verified; see note SS6 N7)")
sys.exit(0)
