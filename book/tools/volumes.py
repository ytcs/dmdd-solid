#!/usr/bin/env python3
"""Source map of the three volumes: which chapter file and which section file belongs to which volume.

Read from tex/vol{1,2,3}.tex and the chapter drivers they \\input. Used by tools/xref.py, tools/split_B1.py
and tools/volmap.py. Labels are stable identifiers (sec:3.4, app:E.14, app:D.29 keep the numbers of the
one-volume edition); the printed number comes from the build.
"""
import re
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
TEX = BOOK / "tex"
VOLS = ("vol1", "vol2", "vol3")
INPUT = re.compile(r"^[^%\n]*?\\input\{([^}]+)\}", re.M)
LABEL = re.compile(r"\\label\{([^}]+)\}")
LIMLABEL = re.compile(r"\\begin\{limitbox\}\[[^\]]*\]\[([^\]]+)\]")


def inputs(path, volid):
    text = path.read_text()
    out = []
    for m in INPUT.finditer(text):
        name = m.group(1).replace(r"\volid", volid)
        if name in ("preamble", "macros"):
            continue
        out.append(TEX / (name if name.endswith(".tex") else name + ".tex"))
    return out


def chapters(vol):
    """[(chapter driver path, [files of the chapter, driver first])] in order, front matter excluded."""
    volid = vol[-1]
    out = []
    for f in inputs(TEX / f"{vol}.tex", volid):
        if f.parent.name == "front":
            continue
        files, stack = [], [f]
        while stack:
            g = stack.pop(0)
            if not g.exists():      # a generated file not written yet (appB/B-1-volN.tex)
                continue
            files.append(g)
            stack = inputs(g, volid) + stack
        out.append((f, files))
    return out


def labels_of(path):
    text = path.read_text()
    return LABEL.findall(text) + LIMLABEL.findall(text)


def chapter_label(driver):
    m = re.search(r"\\chapter\{.*?\}\\label\{([^}]+)\}", driver.read_text(), re.S)
    return m.group(1) if m else None


def label_home():
    """label -> list of (vol, chapter label); a shared appendix gives one entry per volume."""
    home = {}
    for vol in VOLS:
        for driver, files in chapters(vol):
            ch = chapter_label(driver)
            for f in files:
                if not f.exists():
                    continue
                for lab in labels_of(f):
                    home.setdefault(lab, []).append((vol, ch))
    return home


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3 and sys.argv[1] == "--number":
        # printed number of a chapter directory: its position in the volume drivers (chapters only)
        n = {"vol1": 0, "vol2": 8, "vol3": 22}
        for vol in VOLS:
            k = n[vol]
            for driver, _ in chapters(vol):
                if driver.parent.name.startswith("ch"):
                    k += 1
                    if driver.parent.name == sys.argv[2]:
                        print(k)
                        sys.exit(0)
        sys.exit(f"{sys.argv[2]} is in no volume")
