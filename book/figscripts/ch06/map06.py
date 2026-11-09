"""Chapter map of Chap. 6 (fig:6-map): adding back to the Born-Oppenheimer crystal the couplings it dropped, from
the derivative coupling to the vertex, the electron and phonon self-energies and phonon-assisted absorption.
Style of Fig. 1.8 via figscripts/chapmap.py. No numbers are plotted. Output: tex/figures/ch06/map06.pdf.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import chapmap

X, W = 0.1, 5.2
XR, WR = 6.4, 3.55
P = 1.42
y = lambda i: 0.15 + (5 - i) * P
N = {
    "bo": dict(x=X, y=y(0), w=W, shade="ext", title="Born-Oppenheimer crystal",
               body="clamped-nucleus bands; harmonic phonons", tag="Chaps. 3-5"),
    "na": dict(x=X, y=y(1), w=W, title="Nonadiabatic coupling",
               body="derivative coupling; adiabatic and sudden limits", tag="Sect. 6.1"),
    "g": dict(x=X, y=y(2), w=W, title="Electron-phonon matrix elements",
              body=r"screened vertex $g$; deformation potentials; Fröhlich vertex", tag="Sect. 6.2"),
    "se": dict(x=X, y=y(3), w=W, title="Electron self-energy",
               body="Fan-Migdal, Allen-Heine; zero-point shift; lifetimes", tag="Sect. 6.3"),
    "pa": dict(x=X, y=y(4), w=W, title="Phonon-assisted absorption",
               body="indirect edge; Hall-Bardeen-Blatt edge; dark matter", tag="Sect. 6.5"),
    "c13": dict(x=X, y=y(5), w=W, shade="ext", title="Phonon-assisted electron recoil",
                body="the electrons kicked while a phonon carries momentum", tag="Chap. 13"),
    "mig": dict(x=XR, y=y(1) - 0.1, w=WR, shade="ext", title="Migdal effect",
                body="electrons left behind by a" "\n" "kicked nucleus", tag="Chap. 12", h=1.15),
    "pse": dict(x=XR, y=y(3.55), w=WR, shade="light", title="Phonon self-energy",
                body="electron bubble; linewidth;" "\n" "Eliashberg function", tag="Sect. 6.4", h=1.15),
}
E = [
    ("bo", "na", "restore the derivative coupling"),
    ("na", "g", "first order in the displacement"),
    ("g", "se", r"second order in $g$, electron line"),
    ("se", "pa", "add the optical vertex"),
    ("pa", "c13", "dark matter in place of the photon", dict(ls="--")),
    ("na", "mig", "sudden\nlimit", dict(start="right", end="left", side="above", ls="--")),
    ("g", "pse", r"second order in $g$," "\nphonon line", dict(start="right", end="top", conn="arc3,rad=-0.3", side="end")),
]
chapmap.draw(N, E, chapmap.outpath(__file__, "ch06"), size=(5.4, 5.0), height=y(0) + 1.05)
