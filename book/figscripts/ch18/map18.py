"""Chapter map of Chap. 18 (fig:18-map): from the final-state-resolved response of Sect. 8.7 to the cascade kernels and
the branching generating functional (18.1), its reductions (18.1), the moments eps_eh and F_eh (18.2), seeding and the
phenomenological models (18.3), the pair energies of Si, Ge and GaAs (18.4) and the end of the cascade (18.5), which
hand the pair number to the readout (Chap. 20) and the guide to next targets (Sect. 21.7).
Style of Fig. 1.8 via figscripts/chapmap.py. No numbers are plotted. The Limit Check tags assume the planned boxes
of Sects. 18.2 (three), 18.3 (one) and 18.4 (three), numbered in order through the chapter; the caption references
them live with \\cref. Output: tex/figures/ch18/map18.pdf.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import chapmap

H2 = 1.1
P = 1.55
y = lambda i: 0.25 + (6 - i) * P
XL, XR, W = 0.1, 5.4, 4.5
N = {
    "in": dict(x=2.2, y=y(0), w=5.6, shade="ext", title="Final-state-resolved response", h=H2,
               body="prompt pairs, phonons and recoils" "\n" "of each class at fixed momentum transfer",
               tag="Sect. 8.7"),
    "ker": dict(x=XL, y=y(1), w=W, title="Cascade kernels", h=H2,
                body="impact ionization and phonon emission" "\n" "as rates of the master formula",
                tag="Sect. 18.1"),
    "gf": dict(x=XL, y=y(2), w=W, title="Branching generating functional", h=H2,
               body="backward equation over the" "\n" "carrier states; its moment recursions",
               tag="Sect. 18.1"),
    "red": dict(x=XL, y=y(3), w=W, shade="light", title="Energy-only and random-k", h=H2,
                body="carrier state reduced to type and energy;" "\n" "constant matrix elements",
                tag="Sect. 18.1"),
    "seed": dict(x=XR, y=y(3), w=W, title="Seed distributions", h=H2,
                 body="cascade distribution of the pair number;" "\n" "step and Ramanathan-Kurinsky models as limits",
                 tag="Sect. 18.3; Limit Check 18.4"),
    "mom": dict(x=XL, y=y(4), w=W, title="Mean energy per pair, Fano factor", h=H2,
                body="first and second moments;" "\n" "variance terms below and above threshold",
                tag="Sect. 18.2; Limit Checks 18.1-18.3"),
    "mat": dict(x=XR, y=y(4), w=W, title="Calibrated pair energies", h=H2,
                body="Klein relation, linear law in the gap;" "\n" "range in which the model is validated",
                tag="Sect. 18.4; Limit Checks 18.5-18.7"),
    "end": dict(x=2.2, y=y(5), w=5.6, title="Capture and excitons", h=H2,
                body="end of the cascade below the" "\n" "impact-ionization threshold",
                tag="Sect. 18.5"),
    "out": dict(x=2.2, y=y(6), w=5.6, shade="ext", title="Readout and next targets", h=H2,
                body="pair number handed to the sensor;" "\n" "pair energies to the choice of targets",
                tag="later chapters"),
}
E = [
    ("in", "ker", "take the carrier as projectile", dict(sfrac=0.18, efrac=0.55, side="left", dx=-0.05)),
    ("in", "seed", "seed each class", dict(sfrac=0.85, efrac=0.6, side="right", dx=0.05)),
    ("ker", "gf", "Markov steps, independent siblings", dict(side="right")),
    ("gf", "red", "forget the momentum", dict(side="right")),
    ("gf", "seed", "", dict(start="right", end="left", efrac=0.7)),
    ("red", "mom", "take two moments", dict(side="right")),
    ("mom", "mat", "", dict(start="right", end="left")),
    ("mom", "end", "", dict(efrac=0.2)),
    ("seed", "mat", "", dict()),
    ("mat", "end", "", dict(efrac=0.8)),
    ("end", "out", "hand over the pair number", dict(side="right")),
]
chapmap.draw(N, E, chapmap.outpath(__file__, "ch18"), size=(5.6, 7.2), height=y(0) + 1.2)
