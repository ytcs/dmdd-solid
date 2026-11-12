#!/usr/bin/env python3
"""Renumber the section and Limit Check tags of the chapter-map figures after sections have moved.

Usage: python3 tools/remap_maps.py [BUILD_DIR] [--write] [--run]
The map scripts figscripts/chNN/mapNN.py carry tags such as "Sect. 5.5; Limit Checks 5.3, 5.4" typed with the
numbers of the one-volume edition (commit 7696d03). Labels are stable (sec:5.5; lim:...), so each tagged number
is translated through its label to the number that the current build prints. Reads BUILD_DIR/vol*.aux
(default build/). Without --write it only lists the changes; --run reruns the scripts that changed.
A script is rewritten from its 7696d03 version each time, so the tool is idempotent; structural edits of a map
(a node dropped or turned into an external box) are kept in OVERRIDES below.
"""
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import volumes as V  # noqa: E402
from xref import groups  # noqa: E402

OLD = "7696d03"
REPO = V.BOOK.parent
# (script, old text, new text): applied to the 7696d03 script before the tags are renumbered.
OVERRIDES = []


def git_show(path):
    return subprocess.run(["git", "-C", str(REPO), "show", f"{OLD}:{path}"], capture_output=True, text=True).stdout


def new_numbers(build):
    num = {}
    for v in V.VOLS:
        for line in (Path(build) / f"{v}.aux").read_text(errors="replace").splitlines():
            if line.startswith("\\newlabel{") and "@cref}" not in line:
                g = groups(line[len("\\newlabel"):])
                if len(g) == 2:
                    num.setdefault(g[0], groups(g[1])[0])
    return num


def old_limit_numbers():
    """Old printed Limit Check number -> label, by counting the boxes of each chapter in the old source order."""
    out = {}
    main = git_show("book/tex/main.tex")
    chap = 0
    for m in re.finditer(r"\\input\{(ch\d+)/(ch\d+)\}", main):
        chap += 1
        driver = git_show(f"book/tex/{m.group(1)}/{m.group(2)}.tex")
        k = 0
        for s in re.finditer(r"^[^%\n]*?\\input\{([^}]+)\}", driver, re.M):
            text = git_show(f"book/tex/{s.group(1)}.tex")
            for b in re.finditer(r"\\begin\{limitbox\}(\[[^\]]*\])?(\[([^\]]+)\])?\s*(\\label\{([^}]+)\})?", text):
                k += 1
                out[f"{chap}.{k}"] = b.group(3) or b.group(5)
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    build = args[0] if args else V.BOOK / "build"
    num, oldlim = new_numbers(build), old_limit_numbers()

    def sect(m):
        lab = f"sec:{m.group(0)}"
        return num.get(lab, m.group(0))

    def lim(m):
        lab = oldlim.get(m.group(0))
        return num.get(lab, m.group(0)) if lab else m.group(0)

    def tag(m):
        parts = []
        for part in m.group(1).split("; "):
            if part.startswith("Sect"):
                part = re.sub(r"\d+\.\d+", sect, part)
            elif part.startswith("Limit Check"):
                part = re.sub(r"\d+\.\d+", lim, part)
            parts.append(part)
        return 'tag="%s"' % "; ".join(parts)

    for script in sorted((V.BOOK / "figscripts").glob("ch*/map*.py")):
        rel = script.relative_to(REPO)
        text = git_show(str(rel))
        for name, a, b in OVERRIDES:
            if name == script.name:
                if a not in text:
                    sys.exit(f"{name}: override text not found: {a[:60]}")
                text = text.replace(a, b)
        new = re.sub(r'tag="([^"]*)"', tag, text)
        if new != script.read_text():
            print(f"{rel}: tags change")
            for x, y in zip(re.findall(r'tag="[^"]*"', script.read_text()), re.findall(r'tag="[^"]*"', new)):
                if x != y:
                    print(f"   {x} -> {y}")
            if "--write" in sys.argv:
                script.write_text(new)
                if "--run" in sys.argv:
                    subprocess.run([sys.executable, str(script)], check=True, cwd=script.parent)


if __name__ == "__main__":
    main()
