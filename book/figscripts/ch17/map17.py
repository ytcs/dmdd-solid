"""Chapter map of Chap. 17 (fig:17-map): the channel rates of Chaps. 10-16 read along the interaction axis, scattering
(17.1) and absorption (17.2) at fixed coupling, inelastic and exothermic dark matter (17.3), cross-sector interference
(17.4), then the reduction to response-level figures of merit (17.5, Limit Check 17.1) and the ranking under input
uncertainty (17.6), which feeds the guide to next targets of Sect. 21.7.
Style of Fig. 1.8 via figscripts/chapmap.py. No numbers are plotted; tags give section numbers and the one Limit Check
the chapter has (Limit Check 17.1, in Sect. 17.5). Output: tex/figures/ch17/map17.pdf.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import chapmap

H2 = 1.1
P = 1.62
y = lambda i: 0.25 + (5 - i) * P
XL, XR, W = 0.1, 5.6, 4.3
N = {
    "in": dict(x=2.2, y=y(0), w=5.6, shade="ext", title="Channel rates, one chapter each", h=H2,
               body="electrons, phonons, Migdal, phonon-assisted," "\n" "magnons, superconductors, novel targets",
               tag="Chaps. 10-16"),
    "sca": dict(x=XL, y=y(1), w=W, title="Scattering across channels", h=H2,
                body="one coupling, every sector;" "\n" "dominant-sector map in mass and threshold",
                tag="Sect. 17.1"),
    "abs": dict(x=XR, y=y(1), w=W, title="Absorption across channels", h=H2,
                body="one boson, every target;" "\n" "coverage by boson mass",
                tag="Sect. 17.2"),
    "ine": dict(x=XL, y=y(2), w=W, shade="light", title="Inelastic and exothermic", h=H2,
                body="mass splitting; down-scattering" "\n" "into phonons, magnons, plasmons",
                tag="Sect. 17.3"),
    "int": dict(x=XR, y=y(2), w=W - 0.55, shade="light", title="Interference between channels", h=H2,
                body="cross-sector terms;" "\n" "bound by positivity",
                tag="Sect. 17.4"),
    "fom": dict(x=2.2, y=y(3), w=5.6, title="Figures of merit per channel", h=H2,
                body="the few material numbers that set rate and reach;" "\n" "validity windows",
                tag="Sect. 17.5; Limit Check 17.1"),
    "rank": dict(x=2.2, y=y(4), w=5.6, title="Ranking under uncertainty", h=H2,
                 body="provenance widths, probability of ranking first," "\n" "tiers of rank intervals",
                 tag="Sect. 17.6"),
    "out": dict(x=2.2, y=y(5), w=5.6, shade="ext", title="Guide to next targets", h=H2,
                body="pair energy, readout and backgrounds added",
                tag="Sect. 21.6"),
}
E = [
    ("in", "sca", "fix the coupling", dict(sfrac=0.18, efrac=0.55, side="left", dx=-0.05)),
    ("in", "abs", "fix the boson", dict(sfrac=0.82, efrac=0.45, side="right", dx=0.05)),
    ("sca", "ine", "add a mass splitting", dict(side="left")),
    ("sca", "int", "keep the cross terms", dict(start="right", end="left", efrac=0.5, side="right")),
    ("ine", "fom", "", dict(efrac=0.2)),
    ("abs", "fom", "", dict(sfrac=0.93, end="right", efrac=0.6, conn="angle,angleA=-90,angleB=0,rad=0")),  # past the narrowed int box
    ("int", "fom", "", dict(efrac=0.6)),
    ("fom", "rank", "add the input uncertainties", dict(side="right")),
    ("rank", "out", "add the measurement side", dict(side="right")),
]
chapmap.draw(N, E, chapmap.outpath(__file__, "ch17"), size=(5.6, 6.6), height=y(0) + 1.2)
