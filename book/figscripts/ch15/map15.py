"""Chapter map of Chap. 15 (fig:15-map): superconductors, from the BCS state and conserving response of Sect. 7.2
and the master rate of Sect. 8.2 through the conserving density response, the bare quasiparticle bubble and the
Lindhard function (Sect. 15.1), the resummed edge (15.2), films and disorder (15.3) and absorption (15.4).
Style of Fig. 1.8 via figscripts/chapmap.py.  No numbers are plotted; tags give section numbers and the Limit Check
numbers the chapter plans in order (Limit Check 15.1 = lim:15.1a, 15.2 = lim:15.2a, 15.3 = lim:15.4a).
Rerun if the later sections change their boxes.  Output: tex/figures/ch15/map15.pdf.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import chapmap

X, W = 0.1, 4.3
XR, WR = 6.2, 3.7
H2 = 1.15
P = 1.6
y = lambda i: 0.3 + (3 - i) * P
N = {
    "in": dict(x=X, y=y(0), w=W, shade="ext", title="BCS state, master rate", h=H2,
               body="quasiparticles, coherence factors, Nambu;" "\n" r"conserving response; rate from $L$",
               tag="Sects. 7.2, 8.2, 10.2"),
    "cons": dict(x=X, y=y(1), w=W, title="Conserving density response", h=H2,
                 body="quasiparticle bubble + pair-field ladder," "\n" "screened by the Coulomb interaction",
                 tag="Sect. 15.1; Limit Check 15.1"),
    "bare": dict(x=X, y=y(2), w=W, title="Bare quasiparticle bubble", h=H2,
                 body="case-I coherence factor in Im$\\,\\varepsilon$;" "\n" "first-order shift of Re$\\,\\varepsilon$",
                 tag="Sect. 15.1"),
    "lin": dict(x=X, y=y(3), w=W, title="Lindhard loss function", h=H2,
                body="normal metal, no gap;" "\n" "pair breaking as electron-hole pairs",
                tag="Sect. 15.1"),
    "abs": dict(x=XR, y=y(0), w=WR, shade="light", title="Absorption", h=H2,
                body="Mattis-Bardeen and" "\n" "phonon-assisted (Holstein)",
                tag="Sect. 15.4; Limit Check 15.3"),
    "edge": dict(x=XR, y=y(1), w=WR, shade="light", title="Kinematic edge", h=H2,
                 body="screening resummed on" "\n" r"the line $q = \omega/v_{\mathrm{max}}$",
                 tag="Sect. 15.2; Limit Check 15.2"),
    "film": dict(x=XR, y=y(2), w=WR, shade="light", title="Films and disorder", h=H2,
                 body="relaxation-time forms;" "\n" "the dirty limit",
                 tag="Sect. 15.3"),
}
E = [
    ("in", "cons", "density row of the master rate;" "\n" "time-dependent mean field"),
    ("cons", "bare", "drop the pair-field ladder"),
    ("bare", "lin", r"$\Delta_{\mathrm{BCS}} \to 0$"),
    ("cons", "edge", "resum the" "\n" "screening", dict(start="right", end="left", side="above")),
    ("cons", "abs", "current vertex," "\n" r"$q \to 0$", dict(start="right", end="left", side="left", sfrac=0.75,
                                                             efrac=0.4, dx=0.1, dy=0.3)),
    ("cons", "film", "add impurity" "\n" "scattering", dict(start="right", end="left", side="below", sfrac=0.25,
                                                            efrac=0.6, dx=-0.15, dy=-0.02)),
]
chapmap.draw(N, E, chapmap.outpath(__file__, "ch15"), size=(5.6, 4.4), height=y(0) + 1.25)
