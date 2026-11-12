#!/usr/bin/env python3
"""List near-duplicate paragraphs across chapters, per volume and across volumes.

Usage: python3 tools/dups.py OUTDIR
Writes OUTDIR/E2E-vol{1,2,3}-dups.txt. A pair is two paragraphs in different chapter files that share at least
MIN shared word 5-grams (citations, labels and references stripped) covering more than FRAC of the shorter one.
Each line: shared-5-grams fraction  file:line (chapter, volume)  file:line (chapter, volume). A pair is listed in the
file of every volume that holds one of its sides; the later side in reading order is printed second.
"""
import collections
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import volumes as V  # noqa: E402

N, MIN, FRAC = 5, 15, 0.15
STRIP = re.compile(r"\\(cref|Cref|cite|cites|label|crefrange|Crefrange|eqref|labelcref)\*?(\[[^\]]*\])*\{[^}]*\}(\{[^}]*\})?")


def main(out):
    order, where, paras = {}, {}, {}
    k = 0
    for vol in V.VOLS:
        for driver, files in V.chapters(vol):
            ch = V.chapter_label(driver)
            for f in files:
                if f.parent.name == "appB" or f in order:
                    continue
                order[f] = k
                k += 1
                where[f] = (ch, vol)
                text = f.read_text()
                line = 1
                for p in re.split(r"(\n\s*\n)", text):
                    if p.strip() and not p.strip().startswith("\\input"):
                        w = re.findall(r"[a-z0-9\\]+", STRIP.sub("", p).lower())
                        if len(w) >= 25:
                            paras[(f, line)] = w
                    line += p.count("\n")
    idx = collections.defaultdict(set)
    for key, w in paras.items():
        for j in range(len(w) - N + 1):
            idx[tuple(w[j:j + N])].add(key)
    pair = collections.Counter()
    for ks in idx.values():
        if 1 < len(ks) <= 3:
            ks = sorted(ks, key=lambda x: (order[x[0]], x[1]))
            for a in range(len(ks)):
                for b in range(a + 1, len(ks)):
                    if where[ks[a][0]][0] != where[ks[b][0]][0]:
                        pair[(ks[a], ks[b])] += 1
    lines = collections.defaultdict(list)
    for (a, b), c in pair.items():
        m = min(len(paras[a]), len(paras[b])) - N + 1
        if c >= MIN and c / m > FRAC:
            s = "%3d %.2f  %s:%d (%s, %s)  %s:%d (%s, %s)" % (
                c, c / m, a[0].relative_to(V.TEX), a[1], *where[a[0]], b[0].relative_to(V.TEX), b[1], *where[b[0]])
            for vol in {where[a[0]][1], where[b[0]][1]}:
                lines[vol].append((c, s))
    Path(out).mkdir(parents=True, exist_ok=True)
    for vol in V.VOLS:
        rows = [s for _, s in sorted(lines[vol], reverse=True)]
        (Path(out) / f"E2E-{vol}-dups.txt").write_text("\n".join(rows) + "\n")
        print(vol, len(rows), "pairs")


if __name__ == "__main__":
    main(sys.argv[1])
