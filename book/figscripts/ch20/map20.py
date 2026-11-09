"""Chapter map of Chap. 20 (fig:20-map): from the shares of the energy balance law (Sect. 19.5) to charge transport
(20.1), athermal phonons in the substrate (20.2), phonons into films (20.3), the quasiparticle yield (20.4) and the
collection kernels with the recoil-discrimination verdicts (20.5), which feed the limits of the next chapter.
Style of Fig. 1.8 via figscripts/chapmap.py. No numbers are plotted. The Limit Check tags assume the planned boxes
of Sects. 20.1 (three), 20.2 (two), 20.3 (one) and 20.4 (one), numbered in order through the chapter (20.1-20.7);
the caption references them live with \\cref. Output: tex/figures/ch20/map20.pdf.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import chapmap

H2 = 1.1
P = 1.55
y = lambda i: 0.25 + (5 - i) * P
XL, XR, W = 0.1, 5.8, 4.1
N = {
    "in": dict(x=2.2, y=y(0), w=5.6, shade="ext", title="Energy balance law", h=H2,
               body="pairs, phonons and stored energy" "\n" "at the end of the prompt cascade",
               tag="Sect. 19.5"),
    "ch": dict(x=XL, y=y(1), w=W, title="Charge transport", h=H2,
               body="drift, trapping, induced charge;" "\n" "measured Fano factor; Luke emission",
               tag="Sect. 20.1; Limit Checks 20.1-20.3"),
    "ph": dict(x=XR, y=y(1), w=W, title="Athermal phonons", h=H2,
               body="anharmonic decay, isotope scattering;" "\n" "loss of frequency and polarization memory",
               tag="Sect. 20.2; Limit Checks 20.4, 20.5"),
    "fi": dict(x=XR, y=y(2), w=W, title="Phonons into films", h=H2,
               body="acoustic and diffuse mismatch;" "\n" "film absorption and escape time",
               tag="Sect. 20.3; Limit Check 20.6"),
    "qp": dict(x=XR, y=y(3), w=W, title="Quasiparticle yield", h=H2,
               body="pair-breaking efficiency;" "\n" "Kaplan cascade in the film",
               tag="Sect. 20.4; Limit Check 20.7"),
    "ke": dict(x=2.2, y=y(4), w=5.6, title="Collection kernels and discrimination", h=H2,
               body="contrasts, position spread, collection ratio;" "\n" "high-voltage ceiling; nuclear vs electron recoils",
               tag="Sect. 20.5"),
    "out": dict(x=2.2, y=y(5), w=5.6, shade="ext", title="Exclusion limits and next targets", h=H2,
                body="measured signal to a limit;" "\n" "readout column of the guide",
                tag="next chapter"),
}
E = [
    ("in", "ch", "drift the pairs\nin the field", dict(sfrac=0.2, side="left", dx=-0.45)),
    ("in", "ph", "follow the\nprimary phonons", dict(sfrac=0.8, side="right", dx=0.6)),
    ("ch", "ph", "add Luke\nphonons", dict(start="right", end="left", side="below", dy=-0.02)),
    ("ph", "fi", "cross the interface", dict(side="right")),
    ("fi", "qp", "break Cooper pairs", dict(side="right")),
    ("ch", "ke", "induced charge", dict(efrac=0.2, side="left", dx=-0.05)),
    ("qp", "ke", "sensor energy", dict(efrac=0.8, side="right", dx=0.25)),
    ("ke", "out", "", dict()),
]
chapmap.draw(N, E, chapmap.outpath(__file__, "ch20"), size=(5.6, 6.4), height=y(0) + 1.2)
