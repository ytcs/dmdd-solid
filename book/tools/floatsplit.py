#!/usr/bin/env python3
"""List floats that land between the parts of a box broken across pages.

Usage: python3 tools/floatsplit.py BUILD_DIR   (reads vol1.aux, vol2.aux, vol3.aux)
A box (worked example, Limit Check, key result) that starts on page a and ends on page b > a is split; a figure or
table whose page p satisfies a < p <= b is printed between two parts of the box (a top float on the continuation
page, or a float page inside the box). Floats on page a are not reported (top floats there come before the box).
"""
import re
import sys
from pathlib import Path

BOXES = r"workedexample|limitbox|keyresult"


def in_box_labels():
    """Labels that are not floats: figures and tables inside a box (\\captionof) and longtables."""
    out = set()
    for f in Path(__file__).resolve().parent.parent.joinpath("tex").rglob("*.tex"):
        t = re.sub(r"(?<!\\)%.*", "", f.read_text(errors="ignore"))
        for m in re.finditer(r"(?s)\\begin\{(%s)\}(.*?)\\end\{\1\}" % BOXES, t):
            out.update(re.findall(r"\\label\{((?:fig|tab):[^}]*)\}", m.group(2)))
        for m in re.finditer(r"(?s)\\begin\{longtable\}(.*?)\\end\{longtable\}", t):
            out.update(re.findall(r"\\label\{((?:fig|tab):[^}]*)\}", m.group(1)))  # in the text flow, not a float
    return out


def main(d):
    bad = 0
    inbox = in_box_labels()
    for v in ("vol1", "vol2", "vol3"):
        aux = (Path(d) / f"{v}.aux").read_text(errors="ignore")
        st = {i: int(p) for i, p in re.findall(r"\\bxspanstart\{(\d+)\}\{(\d+)\}", aux)}
        en = {i: int(p) for i, p in re.findall(r"\\bxspanend\{(\d+)\}\{(\d+)\}", aux)}
        spans = [(st[i], en[i]) for i in st if i in en and en[i] > st[i]]
        floats = re.findall(r"\\newlabel\{((?:fig|tab):[^}]*)\}\{\{([^}]*)\}\{(\d+)\}", aux)
        for lab, num, page in floats:
            if lab in inbox:
                continue
            p = int(page)
            for a, b in spans:
                if a < p <= b:
                    print(f"{v}: {lab} ({num}) on page {p}, inside a box on pages {a}-{b}")
                    bad += 1
    print(f"floatsplit: {bad} float(s) inside split boxes")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "build"))
