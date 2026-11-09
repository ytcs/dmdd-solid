"""Chapter map of Chap. 8 (fig:8-map): from the couplings of a dark-matter particle to the master rate formula,
screening, the truncation label, the three sectors of final states and the final-state-resolved response.
Style of Fig. 1.8 via figscripts/chapmap.py. No numbers are plotted. Output: tex/figures/ch08/map08.pdf.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import chapmap

X, W = 0.1, 5.2
XR, WR = 6.4, 3.55
P = 1.42
y = lambda i: 0.15 + (6 - i) * P
N = {
    "ops": dict(x=X, y=y(0), w=W, title="Couplings to a target",
                body="non-relativistic operators; target operators per species", tag="Sect. 8.1"),
    "mrf": dict(x=X, y=y(1), w=W, title="Master rate formula",
                body=r"tensor contracted with $S_{ab}(\mathbf{q},\omega)$; absorption", tag="Sect. 8.2"),
    "scr": dict(x=X, y=y(2), w=W, title="Screening for every coupling",
                body="proper response; exact loss-function form; mixing", tag="Sect. 8.4"),
    "hier": dict(x=X, y=y(3), w=W, title="Expansion hierarchy",
                 body=r"small parameters; truncation label $\mathfrak{T}$; resummations", tag="Sect. 8.5"),
    "dec": dict(x=X, y=y(4), w=W, title="Decomposition theorem",
                body=r"$S = S^{\mathrm{ad}} + S^{0} + S^{+}$: three sectors of final states", tag="Sect. 8.6"),
    "fs": dict(x=X, y=y(5), w=W, title="Final-state-resolved response",
               body="final-state classes; pairs; hand-off to the cascade", tag="Sect. 8.7"),
    "chain": dict(x=X, y=y(6), w=W, shade="ext", title="Ionization yield",
                  body="cascade of the final state into quanta", tag="Chap. 18"),
    "ex": dict(x=XR, y=y(1.55), w=WR, shade="light", title="Exact relations",
               body="interference bound; moments;" "\n" "Ward identities", tag="Sect. 8.3", h=1.15),
    "unc": dict(x=XR, y=y(3.55), w=WR, shade="light", title="Uncertainty structure",
                body="truncations and many-body" "\n" "spreads as nuisance parameters", tag="Sect. 8.8", h=1.15),
}
E = [
    ("ops", "mrf", "sum over species and operators"),
    ("mrf", "scr", "separate the Coulomb lines"),
    ("scr", "hier", "truncate: record the orders kept"),
    ("hier", "dec", "split the final states by sector"),
    ("dec", "fs", "resolve each final state"),
    ("fs", "chain", "cascade probabilities", dict(ls="--")),
    ("mrf", "ex", "true for\nany target", dict(start="right", end="top", conn="arc3,rad=-0.3", side="end")),
    ("hier", "unc", "omitted\norders", dict(start="right", end="top", conn="arc3,rad=-0.3", side="end")),
]
chapmap.draw(N, E, chapmap.outpath(__file__, "ch08"), size=(5.4, 5.8), height=y(0) + 1.05)
