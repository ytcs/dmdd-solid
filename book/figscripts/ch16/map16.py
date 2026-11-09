"""Chapter map of Chap. 16 (fig:16-map): novel targets, from the bulk channels of Chaps. 10-15 to the Dirac materials
(16.1), low-dimensional plasmons (16.2), graphene, nanotubes and quantum dots (16.3) and molecular crystals (16.4) on
the side of delocalized electrons, and to dopants (16.5), color centers (16.6), glasses (16.7) and two-level systems at
millikelvin (16.8) on the side of localized final states; both feed the input table of 16.9.
Style of Fig. 1.8 via figscripts/chapmap.py.  No numbers are plotted; tags give section numbers and the Limit Check
numbers the chapter plans in order (16.1 = lim:16.1a; 16.2-16.4 = lim:16.2a-c; 16.5-16.6 = lim:16.3a-b;
16.7 = lim:16.4a; 16.8 = lim:16.5a; 16.9 = lim:16.6a; 16.10-16.13 = lim:16.7a-d; 16.14-16.17 = lim:16.8a-d).
Rerun when the later sections fix their boxes.  Output: tex/figures/ch16/map16.pdf.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import chapmap

X, W = 0.1, 4.3
XR, WR = 5.6, 4.3
H2 = 1.1
P = 1.62
y = lambda i: 0.25 + (5 - i) * P
N = {
    "in": dict(x=2.2, y=y(0), w=5.6, shade="ext", title="Bulk channels and responses", h=H2,
               body="loss-function rate, absorption, screening;" "\n" "Dirac cones, donors, color centers",
               tag="Chaps. 7, 8, 10-15"),
    "dir": dict(x=X, y=y(1), w=W, title="Dirac materials", h=H2,
                body="slow linear bands; background" "\n" r"$\varepsilon_{\mathrm{bg}}$ in the total $\varepsilon$",
                tag="Sect. 16.1; Limit Check 16.1"),
    "low": dict(x=X, y=y(2), w=W, title="Low-dimensional plasmons", h=H2,
                body="1D and 2D gases, acoustic mode;" "\n" "layered stacks",
                tag="Sect. 16.2; Limit Checks 16.2-16.4"),
    "gra": dict(x=X, y=y(3), w=W, title="Graphene, nanotubes, dots", h=H2,
                body="ejection into vacuum;" "\n" "confined electrons, depolarization",
                tag="Sect. 16.3; Limit Checks 16.5, 16.6"),
    "mol": dict(x=X, y=y(4), w=W, title="Molecular crystals", h=H2,
                body="Frenkel excitons;" "\n" "molecular form factors",
                tag="Sect. 16.4; Limit Check 16.7"),
    "dop": dict(x=XR, y=y(1), w=WR, shade="light", title="Dopants", h=H2,
                body="donor transitions;" "\n" "impurity band",
                tag="Sect. 16.5; Limit Check 16.8"),
    "col": dict(x=XR, y=y(2), w=WR, shade="light", title="Color centers, broken bonds", h=H2,
                body="defects created by a recoil;" "\n" "cage escape",
                tag="Sect. 16.6; Limit Check 16.9"),
    "gla": dict(x=XR, y=y(3), w=WR, shade="light", title="Glasses, two-level systems", h=H2,
                body="tunneling model; absorption" "\n" "and scattering in random media",
                tag="Sect. 16.7; Limit Checks 16.10-16.13"),
    "tls": dict(x=XR, y=y(4), w=WR, shade="light", title="Two-level systems at mK", h=H2,
                body="relaxation by phonons, electrons;" "\n" "heat release",
                tag="Sect. 16.8; Limit Checks 16.14-16.17"),
    "unc": dict(x=2.2, y=y(5), w=5.6, title="Inputs and their uncertainties", h=H2,
                body="material inputs of each target;" "\n" "limited by theory or by data",
                tag="Sect. 16.9"),
}
E = [
    ("in", "dir", "delocalized electrons", dict(sfrac=0.18, efrac=0.55, side="left", dx=-0.05)),
    ("in", "dop", "localized final states", dict(sfrac=0.82, efrac=0.45, side="right", dx=0.05)),
    ("dir", "low", "reduce the dimension"),
    ("low", "gra", "confine the electrons"),
    ("gra", "mol", "localize on molecules"),
    ("dop", "col", "defects made by the recoil", dict(side="left")),
    ("col", "gla", "disorder: tunneling atoms", dict(side="left")),
    ("gla", "tls", "kinetics at millikelvin", dict(side="left")),
    ("mol", "unc", "", dict(efrac=0.25)),
    ("tls", "unc", "", dict(efrac=0.75)),
]
chapmap.draw(N, E, chapmap.outpath(__file__, "ch16"), size=(5.6, 6.6), height=y(0) + 1.2)
