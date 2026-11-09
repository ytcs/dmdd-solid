"""Shared drawing routine for the chapter maps (figscripts/chNN/mapNN.py), in the style of Fig. 1.8
(figscripts/ch01/fig1_8.py): rounded grey boxes with a bold title, a one-line body in 7 pt and, on a third line,
the section and Limit Check tags in grey; arrows "-|>" in grey 0.3 carry an italic label naming what the step
adds or drops. A map is a reading aid and carries no numbers beyond section and Limit Check numbers.

Coordinates are in axis units: x from 0 to 10 across the figure width, y upward from 0 to `height`.
A node is a dict with keys x, y (lower-left corner), w, title, body, tag and optionally h, shade ("dark" for the
chapter's main ladder, "light" for side objects, "ext" for objects of other chapters, drawn dashed).
An edge is (from, to, label) with optional dict of options: side ("right"/"left"/"above"/"below"), start/end
anchors ("top", "bottom", "left", "right"), dx/dy offsets of the label, ha.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

H_BOX = 0.95


def _anchor(n, where, frac=0.5):
    h = n.get("h", H_BOX)
    if where == "top":
        return (n["x"] + frac * n["w"], n["y"] + h)
    if where == "bottom":
        return (n["x"] + frac * n["w"], n["y"])
    if where == "left":
        return (n["x"], n["y"] + frac * h)
    if where == "right":
        return (n["x"] + n["w"], n["y"] + frac * h)
    raise ValueError(where)


def draw(nodes, edges, out, size=(5.4, 6.4), height=10.0, notes=(), brackets=(), lines=()):
    fig, ax = plt.subplots(figsize=size)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, height)
    ax.axis("off")
    for key, n in nodes.items():
        h = n.get("h", H_BOX)
        shade = {"dark": "0.93", "light": "0.98", "ext": "1.0"}[n.get("shade", "dark")]
        ls = "--" if n.get("shade") == "ext" else "-"
        ax.add_patch(FancyBboxPatch((n["x"], n["y"]), n["w"], h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                    fc=shade, ec="0.3", lw=0.8, ls=ls))
        ax.text(n["x"] + 0.12, n["y"] + h - 0.12, n["title"], fontsize=8.5, weight="bold", va="top")
        if n.get("body"):
            ax.text(n["x"] + 0.12, n["y"] + h - 0.42, n["body"], fontsize=7, va="top", linespacing=1.15)
        if n.get("tag"):
            ax.text(n["x"] + 0.12, n["y"] + 0.08, n["tag"], fontsize=7, va="bottom", color="0.25")
    for e in edges:
        a, b, label = e[:3]
        o = e[3] if len(e) > 3 else {}
        nb = nodes[b]
        s = o.get("start", "bottom")
        t = o.get("end", "top")
        if isinstance(a, tuple):  # start from a point, e.g. a bus line
            p0, s = a, "point"
        else:
            p0 = _anchor(nodes[a], s, o.get("sfrac", 0.5))
        p1 = _anchor(nb, t, o.get("efrac", 0.5))
        if s == "bottom":
            p0 = (p0[0], p0[1] - 0.02)
        if t == "top":
            p1 = (p1[0], p1[1] + 0.03)
        if t == "left":
            p1 = (p1[0] - 0.03, p1[1])
        if t == "right":
            p1 = (p1[0] + 0.03, p1[1])
        if o.get("straight_x"):
            p0 = (p1[0], p0[1])
        if o.get("straight_y"):
            p0 = (p0[0], p1[1])
        if s == "point" and t == "left":
            p0 = (p0[0], p1[1])
        ax.annotate("", xy=p1, xytext=p0,
                    arrowprops=dict(arrowstyle="-|>", color="0.3", lw=0.9, ls=o.get("ls", "-"),
                                    connectionstyle=o.get("conn", "arc3")))
        if label:
            mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
            side = o.get("side", "right")
            dx, dy = o.get("dx", 0.0), o.get("dy", 0.0)
            if side == "end":
                ax.text(p1[0] + 0.12 + dx, p1[1] + 0.1 + dy, label, fontsize=7, style="italic", color="0.25",
                        va="bottom", ha="left", linespacing=1.1)
            elif side == "right":
                ax.text(mx + 0.12 + dx, my + dy, label, fontsize=7, style="italic", color="0.25",
                        va="center", ha="left", linespacing=1.1)
            elif side == "left":
                ax.text(mx - 0.12 + dx, my + dy, label, fontsize=7, style="italic", color="0.25",
                        va="center", ha="right", linespacing=1.1)
            elif side == "above":
                ax.text(mx + dx, my + 0.08 + dy, label, fontsize=7, style="italic", color="0.25",
                        va="bottom", ha=o.get("ha", "center"), linespacing=1.1)
            else:
                ax.text(mx + dx, my - 0.08 + dy, label, fontsize=7, style="italic", color="0.25",
                        va="top", ha=o.get("ha", "center"), linespacing=1.1)
    for (p0, p1) in lines:
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color="0.3", lw=0.9)
    for (x, y0, y1) in brackets:
        ax.plot([x, x], [y0, y1], color="0.5", lw=0.8)
    for (x, y, txt, kw) in notes:
        ax.text(x, y, txt, **{"fontsize": 7, "color": "0.4", **kw})
    fig.subplots_adjust(left=0.01, right=0.99, top=0.995, bottom=0.005)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out)
    print("wrote", os.path.normpath(out))


def outpath(script, chap):
    return os.path.join(os.path.dirname(os.path.abspath(script)), "..", "..", "tex", "figures", chap,
                        os.path.splitext(os.path.basename(script))[0] + ".pdf")
