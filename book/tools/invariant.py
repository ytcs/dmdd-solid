#!/usr/bin/env python3
"""Check that a prose edit left the technical content of LaTeX files unchanged.

Usage: invariant.py BASE_COMMIT FILE.tex [FILE.tex ...]
Compares, per file, the multisets of inline math, display environments, \\SI/\\num/\\qty, citation keys and labels
between BASE_COMMIT and the working tree. Repeating or dropping a repeat of an item that stays in the file, and adding
\\cref targets, are reported but allowed. An item new to the file, or one that disappears from it, is a stop.
Exit status 1 if any file has a stop.
"""
import re
import subprocess
import sys
from collections import Counter

DISPLAY = r"equation|align|gather|multline|eqnarray"  # tables: their math, numbers and citations are compared item by item


def items(t):
    t = re.sub(r"(?<!\\)%.*", "", t)
    out = Counter()
    for m in re.finditer(r"(?s)\\begin\{(%s)\*?\}(.*?)\\end\{\1\*?\}" % DISPLAY, t):
        out["display:" + re.sub(r"\s+", " ", m.group(2)).strip()] += 1
    t2 = re.sub(r"(?s)\\begin\{(%s)\*?\}.*?\\end\{\1\*?\}" % DISPLAY, " ", t)
    for m in re.finditer(r"\$([^$]+)\$|\\\((.*?)\\\)", t2):
        out["math:" + re.sub(r"\s+", "", m.group(1) or m.group(2))] += 1
    for m in re.finditer(r"\\(SI|num|qty|SIrange|numrange)\{([^}]*)\}(?:\{([^}]*)\})?", t2):
        out["num:" + m.group(0)] += 1
    for m in re.finditer(r"\\cites?(?:\[[^\]]*\])*\{([^}]*)\}", t):
        for k in m.group(1).split(","):
            out["cite:" + k.strip()] += 1
    for m in re.finditer(r"\\label\{([^}]*)\}", t):
        out["label:" + m.group(1)] += 1
    return out


def refs(t):
    c = Counter()
    for m in re.finditer(r"\\[cC]ref(?:range)?\*?\{([^}]*)\}", t):
        for k in m.group(1).split(","):
            c[k.strip()] += 1
    return c


def main(a):
    if len(a) < 2:
        print(__doc__)
        return 0
    base, bad = a[0], 0
    for f in a[1:]:
        rel = subprocess.run(["git", "ls-files", "--full-name", f], capture_output=True, text=True).stdout.strip() or f
        old = subprocess.run(["git", "show", f"{base}:{rel}"], capture_output=True, text=True).stdout
        new = open(f).read()
        o, n = items(old), items(new)
        lost = Counter({k: v for k, v in (o - n).items() if k not in n})      # item gone entirely
        flat = re.sub(r"\s+", "", old)
        gained = Counter({k: v for k, v in (n - o).items() if k not in o       # item new to the file
                          and not (k.startswith("math:") and k[5:] in flat)})  # unless it is a piece of existing math
        recount = sorted(set((o - n) | (n - o)) - set(lost) - set(gained))     # repeats of existing items
        ro, rn = refs(old), refs(new)
        rlost, rgain = Counter({k: v for k, v in (ro - rn).items() if k not in rn}), rn - ro
        if recount:
            print(f"note {f}: repeat count changed for {len(recount)} existing item(s)")
        if lost or gained or rlost:
            bad += 1
            print(f"STOP {f}")
            for k, v in lost.items():
                print(f"   - {v}x {k[:160]}")
            for k, v in gained.items():
                print(f"   + {v}x {k[:160]}")
            for k, v in rlost.items():
                print(f"   - {v}x cref {k}")
        if rgain:
            print(f"note {f}: added cref " + ", ".join(rgain))
    print("invariant: %d file(s) with a stop" % bad)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
