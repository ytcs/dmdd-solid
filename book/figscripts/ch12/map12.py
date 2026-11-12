"""Chapter map of Chap. 12 (fig:12-map): the Migdal entry of the joint electron-lattice response and its
truncations, from the isolated atom to the crystal loss function and the phonon final states, with the exact
moments, bremsstrahlung and absorption as branches. Style of Fig. 1.8 via figscripts/chapmap.py. No numbers are
plotted; tags give section and Limit Check numbers. Output: tex/figures/ch12/map12.pdf.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import chapmap

X, W = 0.1, 4.45
XR, WR = 6.35, 3.6
H2 = 1.15
P = 1.75
y = lambda i: 0.3 + (4 - i) * P
N = {
    "in": dict(x=X, y=y(0), w=W, shade="ext", title="Lattice and electronic responses", h=H2,
               body="sectors of the decomposition" "\n" "theorem", tag="Sect. 8.6; Chaps. 10, 11"),
    "joint": dict(x=X, y=y(1), w=W, title="Joint electron-lattice response", h=H2,
                  body=r"Migdal entry: boost $\mathbf{q}\cdot\mathbf{p}/M_\kappa\omega_e^2$;" "\n" "double counting of recoils",
                  tag="Sect. 12.1"),
    "atom": dict(x=X, y=y(2), w=W, title="Atomic limit", h=H2,
                 body="boost to all orders; dipole order;" "\n" "bound final states",
                 tag="Sect. 12.2; Limit Check 12.1"),
    "loss": dict(x=X, y=y(3), w=W, title="Crystal: loss-function probability", h=H2,
                 body=r"soft limit $p \ll q$; impulse lattice;" "\n" "Wannier picture of the boost",
                 tag="Sect. 12.3; Limit Checks 12.2-12.4"),
    "ph": dict(x=X, y=y(4), w=W, title="Phonon final states", h=H2,
               body="multiphonon lattice factor;" "\n" "phonon-mediated form",
               tag="Sect. 12.4; Limit Checks 12.5, 12.6"),
    "mom": dict(x=XR, y=y(1.5), w=WR, shade="light", title="Moments of the spectrum", h=H2,
                body="drag mass; trace rule;" "\n" "two-sided bounds", tag="Sect. 12.5"),
    "brem": dict(x=XR, y=y(3), w=WR, shade="light", title="Bremsstrahlung, absorption", h=H2,
                 body="dynamical Born charge;" "\n" "Migdal-type scalar absorption", tag="Sect. 12.6"),
}
E = [
    ("in", "joint", r"resolve $\omega_e$ and $\omega_l$"),
    ("joint", "atom", "one atom: free recoil" "\n" "of the whole atom"),
    ("atom", "loss", "valence electrons of the" "\n" "crystal; diagonal of $\\varepsilon^{-1}$"),
    ("loss", "ph", "below the impulse onset:" "\n" "harmonic lattice factor"),
    ("joint", "mom", "exact\nmoments", dict(start="right", end="top", conn="arc3,rad=-0.3", side="end")),
    ("loss", "brem", "photon emitted\nor absorbed", dict(start="right", end="left", side="above")),
]
chapmap.draw(N, E, chapmap.outpath(__file__, "ch12"), size=(5.4, 5.6), height=y(0) + 1.25)
