#!/usr/bin/env python3
"""Print the map from stable labels to printed numbers in the three volumes.

Usage: python3 tools/volmap.py [BUILD_DIR] [--md]
Reads vol{1,2,3}.aux in BUILD_DIR (default: build/). Plain output: one line "label<TAB>volume<TAB>printed number<TAB>title"
for every chapter, section and appendix label. With --md: the table of book/VOLUMES.md.
"""
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import volumes as V  # noqa: E402
from xref import groups  # noqa: E402

NUM = {"vol1": "I", "vol2": "II", "vol3": "III"}
KEEP = re.compile(r"^(chap:\d+|sec:\d+\.\d+|app:[A-F](-II)?(\.\d+)?)$")


def rows(build):
    out = []
    for v in V.VOLS:
        aux = Path(build) / f"{v}.aux"
        if not aux.exists():
            sys.exit(f"{aux} missing: run ./build.sh first")
        kind = {}
        text = aux.read_text(errors="replace").splitlines()
        for line in text:
            if line.startswith("\\newlabel{") and "@cref}" in line:
                g = groups(line[len("\\newlabel"):])
                kind[g[0][:-5]] = re.match(r"\{?\[([a-z]+)\]", g[1]).group(1)
        for line in text:
            if not line.startswith("\\newlabel{"):
                continue
            g = groups(line[len("\\newlabel"):])
            if len(g) != 2 or not KEEP.match(g[0]):
                continue
            f = groups(g[1])
            k = kind.get(g[0], "")
            word = {"chapter": "Chap.", "section": "Sect.", "appendix": "Appendix", "subappendix": "Appendix"}.get(k, "")
            out.append((g[0], NUM[v], f"{word} {f[0]}", f[2] if len(f) > 2 else ""))
    return out


def old_number(label):
    kind, num = label.split(":")
    if kind == "chap":
        return f"Chap. {num}"
    if kind == "sec":
        return f"Sect. {num}"
    return "Appendix " + ("E (derivations)" if num == "D-II" else num)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    build = args[0] if args else V.BOOK / "build"
    r = rows(build)
    if "--md" in sys.argv:
        print("| Label | One-volume edition | Volume | Now | Title |\n|---|---|---|---|---|")
        seen = set()
        for lab, vol, new, title in r:
            if lab.startswith(("app:A", "app:B")):
                if lab in seen:
                    continue
                seen.add(lab)
                vol = "I, II, III"
            old = old_number(lab) if lab not in ("app:D-II",) and not re.match(r"chap:(2[3-9]|3\d)$", lab) else "(new)"
            mark = "" if old == new else " **"
            print(f"| `{lab}` | {old} | {vol} | {new}{mark and ' ←'} | {title} |")
    else:
        for row in r:
            print("\t".join(row))
