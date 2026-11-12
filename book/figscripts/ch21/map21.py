"""Chapter map of Chap. 21 (fig:21-map): from the channel responses and the measured signal of the previous chapters to
the rate assembly (21.1), the halo-independent bounds (21.2), the kinematic edge (21.3), the theory band (21.4),
statistics, combination and recasting (21.5), and the guide to next targets (21.7).
Style of Fig. 1.8 via figscripts/chapmap.py. No numbers are plotted. The Limit Check tags assume the planned boxes
of Sects. 21.1 (one) and 21.2 (one), numbered 21.1 and 21.2; the caption references them live with \\cref.
Output: tex/figures/ch21/map21.pdf.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import chapmap

H2 = 1.1
P = 1.8
y = lambda i: 0.25 + (6 - i) * P
XL, XR, W = 0.1, 6.0, 3.9
N = {
    "in": dict(x=2.2, y=y(0), w=5.6, shade="ext", title="Responses and readout", h=H2,
               body=r"$S_{ab}$ per channel, final-state classes;" "\n" "pair energies, collection, backgrounds",
               tag="previous chapters"),
    "ra": dict(x=2.2, y=y(1), w=5.6, title="Rate assembly", h=H2,
               body="halo functional and rate kernel;" "\n" r"$\eta(v_{\min})$ of the standard halo; floors",
               tag="Sect. 21.1; Limit Check 21.1"),
    "hi": dict(x=XL, y=y(2), w=W, title="Halo-independent bounds", h=H2,
               body="linear program over velocity" "\n" "distributions; streams; certificate",
               tag="Sect. 21.2; Limit Check 21.2"),
    "ed": dict(x=XR, y=y(2), w=W, title="Kinematic edge", h=H2,
               body=r"power law near $m_{\min}$;" "\n" "threshold, gap and halo degeneracy",
               tag="Sect. 21.3"),
    "nu": dict(x=2.2, y=y(3), w=5.6, title="Theory uncertainties in a limit", h=H2,
               body="Poisson limit; profiled nuisance" "\n" "parameters; theory band per channel",
               tag="Sect. 21.4"),
    "st": dict(x=XL, y=y(4), w=W, title="Statistics and recasting", h=H2,
               body="unknown background; shared parameters;" "\n" "recast for a corrected response",
               tag="Sect. 21.5"),
    "nt": dict(x=2.2, y=y(5), w=5.6, title="Next targets", h=H2,
               body="leader per channel with its probability;" "\n" "missing demonstration; deciding measurement",
               tag="Sect. 21.6"),
    "out": dict(x=2.2, y=y(6), w=5.6, shade="ext", title="Open problems", h=H2,
                body="what stays open, by chapter", tag="Chap. 22"),
}
E = [
    ("in", "ra", "contract with the halo", dict(side="right")),
    ("ra", "hi", "drop the halo model", dict(sfrac=0.2, side="left", dx=-0.05)),
    ("ra", "ed", r"let $v_{\min}$ reach $v_{\max}$", dict(sfrac=0.8, side="right", dx=0.05)),
    ("ra", "nu", "add theory\nuncertainties", dict(side="right", dy=-1.0)),
    ("nu", "st", "unknown background;\nseveral experiments", dict(sfrac=0.2, side="left", dx=-0.45)),
    ("st", "nt", "", dict(efrac=0.2)),
    ("nu", "nt", "add rankings, pair energies,\nreadout, backgrounds", dict(sfrac=0.8, efrac=0.8, side="right", dx=0.05)),
    ("nt", "out", "", dict()),
]
chapmap.draw(N, E, chapmap.outpath(__file__, "ch21"), size=(5.6, 8.2), height=y(0) + 1.2)
