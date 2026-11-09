"""Chapter map of Chap. 4 (fig:4-map): from the Kubo formula to the hierarchy of many-body approximations of the
density response (independent particles, random phase, local fields, TDDFT kernel, Bethe-Salpeter), with the
exact constraints that test every approximation. Style of Fig. 1.8 (figscripts/ch01/fig1_8.py) via figscripts/chapmap.py.
No numbers are plotted. Output: tex/figures/ch04/map04.pdf.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import chapmap

X, W = 0.7, 5.3
XR, WR = 6.45, 3.45
P = 1.42
y = lambda i: 0.15 + (7 - i) * P
N = {
    "kubo": dict(x=X, y=y(0), w=W, title="Kubo formula",
                 body=r"$\chi_{AB}$ from $\langle[A(t), B]\rangle$; Lehmann representation", tag="Sect. 4.1"),
    "S": dict(x=X, y=y(1), w=W, title="Response matrix and dynamic structure factor",
              body=r"$\chi''_{ab} \leftrightarrow S_{ab}(\mathbf{q},\omega)$; positivity", tag="Sect. 4.2"),
    "eps": dict(x=X, y=y(2), w=W, title="Dielectric matrix and loss function",
                body=r"$\varepsilon^{-1}_{\mathbf{G}\mathbf{G}'}(\mathbf{q},\omega)$; $S \propto \mathrm{Im}[-1/\varepsilon]$",
                tag="Sect. 4.4"),
    "ip": dict(x=X, y=y(3), w=W, title="Independent particles",
               body=r"bubble $\chi^0$; Lindhard function in the electron gas", tag="Sects. 4.5, 4.6"),
    "rpa": dict(x=X, y=y(4), w=W, title="Random-phase approximation",
                body=r"Hartree head $v(\mathbf{q})$; Thomas-Fermi screening; plasmon",
                tag="Sects. 4.5, 4.6; Limit Checks 4.1, 4.2"),
    "lf": dict(x=X, y=y(5), w=W, title="Local fields",
               body=r"full Hartree matrix $\bar v_{\mathbf{G}\mathbf{G}'}$", tag="Sect. 4.6"),
    "tddft": dict(x=X, y=y(6), w=W, title="Time-dependent density-functional theory",
                  body=r"kernel $f_{\mathrm{xc}}$ added to $\bar v$", tag="Sect. 4.6"),
    "bse": dict(x=X, y=y(7), w=W, title="Bethe-Salpeter equation",
                body=r"screened attraction $-K^{\mathrm{d}}$ on top of local fields", tag="Sect. 4.9"),
    "exact": dict(x=XR, y=y(2.55), w=WR, shade="light", title="Exact constraints",
                  body="Kramers-Kronig, f-sum and" "\n" "moment rules test" "\n" "every approximation", tag="Sect. 4.3", h=1.4),
    "gf": dict(x=XR, y=y(6.5), w=WR, shade="light", title="Green's functions",
               body=r"$G$, $\Sigma$, Dyson equation;" "\n" r"diagrams, $GW$ energies", tag="Sects. 4.7, 4.8", h=1.15),
}
E = [
    ("kubo", "S", "density operators: matrix $\\chi_{ab}$"),
    ("S", "eps", "separate the long-range Coulomb line"),
    ("eps", "ip", "approximate the proper response"),
    ("ip", "rpa", "add the Hartree field at $\\mathbf{q}$"),
    ("rpa", "lf", "add $\\mathbf{G} \\neq \\mathbf{G}'$ (local fields)"),
    ("lf", "tddft", "add exchange-correlation kernel"),
    ("tddft", "bse", "add electron-hole attraction"),
    ("S", "exact", "causality,\ncommutators", dict(start="right", end="top", conn="arc3,rad=-0.3", side="right",
                                                    dx=0.9, dy=0.1)),   # label clear of the arc
    ("exact", "ip", "", dict(start="left", end="right", efrac=0.5, sfrac=0.25, ls="--")),
    ("gf", "bse", "quasiparticle energies, $W$",
     dict(start="bottom", end="right", conn="arc3,rad=-0.25", side="right", dx=-0.25, dy=-0.4)),
]
brackets = [(0.45, y(7) + 0.05, y(3) + 0.9)]
notes = [(0.25, y(5) + 0.5, "each approximation is a limit of the next", dict(rotation=90, va="center", ha="center"))]
chapmap.draw(N, E, chapmap.outpath(__file__, "ch04"), size=(5.4, 7.0), height=y(0) + 1.1, notes=notes, brackets=brackets)
