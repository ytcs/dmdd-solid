"""Counts of Table 9.1 (tab:9-atlas) of Sect. 9.1, read from the tabular in tex/ch09/s9-1.tex (never edited here).

Every count that Sect. 9.1, Worked Example 9.1 and the Chapter 9 summary print comes from this log:
  cells that name a section (a channel with a home), cells marked $\\circ$ (allowed at leading order, computed in
  no section), cells marked --- (no channel at leading order), per column and in total; the list of circle cells
  (they form one row of tab:22-gaps); and the cells that a dark photon populates (WE 9.1).
Dark-photon cells (WE 9.1, we:8-darkphoton, tab:8-operators): the photon couples to n_Z = -n_e + sum Z_k n_k in
scattering and to the current of all charges in absorption, so it enters every filled cell of the density, nuclear
and vector-absorption columns (cells that a material forbids, such as the single phonon of silicon, still count as
cells of the atlas); in the last column it enters the inelastic pair rate (10.9) and exothermic down-scattering
into plasmons and optical phonons (17.3). The script asserts that each of these cells is filled.
Run: python atlas9_1.py (< 1 s). Output: atlas9_1.log.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
TEX = os.path.join(HERE, "..", "..", "tex", "ch09", "s9-1.tex")
LOG = open(os.path.join(HERE, "atlas9_1.log"), "w")


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")


t = open(TEX).read()
tab = t.split(r"\label{tab:9-atlas}", 1)[1].split(r"\end{tabular}", 1)[0]
body = tab.split(r"\midrule", 1)[1].split(r"\bottomrule", 1)[0]
COLS = ["electron density", "nuclei", "spin, current", "vector abs.", "ALP, scalar abs.", "inelastic, other"]
rows = []
for line in body.split(r"\\"):
    line = line.replace(r"\addlinespace[2pt]", "").strip()
    if not line:
        continue
    f = [x.strip() for x in line.split("&")]
    assert len(f) == 8, f
    rows.append((re.sub(r"\s*\(\\ref.*", "", f[0]), f[2:]))


def kind(c):
    if c == "---":
        return "empty"
    if c == r"$\circ$":
        return "circle"
    assert re.fullmatch(r"\\ref\{sec:\d+\.\d+\}", c), c
    return "filled"


log("Table 9.1 (tab:9-atlas), read from tex/ch09/s9-1.tex")
log(f"rows: {len(rows)}; columns: {len(COLS)}; cells: {len(rows) * len(COLS)}")
tot = {"filled": 0, "circle": 0, "empty": 0}
for j, c in enumerate(COLS):
    k = [kind(r[1][j]) for r in rows]
    log(f"  column {c:18s}: filled {k.count('filled'):2d}, circle {k.count('circle')}, empty {k.count('empty'):2d}")
    for key in tot:
        tot[key] += k.count(key)
log(f"total: filled {tot['filled']}, circle {tot['circle']}, empty (---) {tot['empty']}; "
    f"filled + circle + empty = {sum(tot.values())}")
log(f"cells without a computed channel (circle + empty): {tot['circle'] + tot['empty']}")
log("circle cells (allowed at leading order, computed in no section):")
for name, cells in rows:
    for j, c in enumerate(cells):
        if kind(c) == "circle":
            log(f"  {name} x {COLS[j]}")
rows_all_empty = [name for name, cells in rows if all(kind(c) == "empty" for c in cells)]
log("rows with no filled or circle cell:", rows_all_empty)

# ---------------------------------------------------------------- dark photon (WE 9.1)
DP_LAST = ("Electron--hole pairs", "Electron-gas continua", "Single phonons")
dp = {c: [] for c in COLS}
for name, cells in rows:
    for j in (0, 1, 3):
        if kind(cells[j]) == "filled":
            dp[COLS[j]].append(name)
    if name.startswith(DP_LAST):
        assert kind(cells[5]) == "filled", name
        dp[COLS[5]].append(name)
log("dark-photon cells (WE 9.1):")
for c in COLS:
    if dp[c]:
        log(f"  {c:18s}: {len(dp[c]):2d}  " + "; ".join(dp[c]))
ndp = sum(len(v) for v in dp.values())
log(f"  total {ndp} of the {tot['filled']} filled cells")

# Sound-speed range quoted in WE 9.1 (Sect. 5.2 branch speeds, km/s, over c)
C_KMS = 299792.458
log("Si sound speeds over c (Sect. 5.2): slow TA [110] 4.67 km/s -> %.2e ; fastest LA 9.4 km/s -> %.2e" % (4.67/C_KMS, 9.4/C_KMS))
LOG.close()
