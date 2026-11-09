"""Chapter map of Chap. 5 (fig:5-map): from the coupled electrons and nuclei to the Born-Oppenheimer surface,
the harmonic crystal, phonons, polar crystals, displacement correlations and anharmonicity.
Style of Fig. 1.8 via figscripts/chapmap.py. No numbers are plotted. Output: tex/figures/ch05/map05.pdf.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import chapmap

X, W = 0.1, 5.2
XR, WR = 6.4, 3.55
P = 1.42
y = lambda i: 0.15 + (6 - i) * P
N = {
    "coul": dict(x=X, y=y(0), w=W, shade="ext", title="Coupled electrons and nuclei",
                 body="Coulomb Hamiltonian of the solid", tag="Sect. 2.3"),
    "bo": dict(x=X, y=y(1), w=W, title="Born-Oppenheimer surface",
               body="adiabatic states; Hellmann-Feynman force", tag="Sect. 5.1"),
    "harm": dict(x=X, y=y(2), w=W, title="Harmonic crystal",
                 body="dynamical matrix; acoustic sum rule; sound speeds", tag="Sect. 5.2"),
    "ph": dict(x=X, y=y(3), w=W, title="Phonons",
               body="phonon operators; zero-point and thermal motion", tag="Sect. 5.3"),
    "pol": dict(x=X, y=y(4), w=W, title="Polar crystals",
                body="Born charges; LO-TO splitting; Lyddane-Sachs-Teller", tag="Sect. 5.5"),
    "corr": dict(x=X, y=y(5), w=W, title="Displacement correlations",
                 body="Debye-Waller factor; expansion in phonon number", tag="Sect. 5.6"),
    "anh": dict(x=X, y=y(6), w=W, title="Anharmonicity",
                body="three-phonon linewidth; self-consistent phonons", tag="Sect. 5.7"),
    "ep": dict(x=XR, y=y(1) - 0.1, w=WR, shade="ext", title="Electron-phonon coupling",
               body="the nonadiabatic terms" "\n" "added back", tag="Chap. 6", h=1.15),
    "dfpt": dict(x=XR, y=y(2) - 0.1, w=WR, shade="light", title="Phonons from first principles",
                 body="frozen phonons; Sternheimer" "\n" r"equation; $2n+1$ theorem", tag="Sect. 5.4", h=1.15),
}
E = [
    ("coul", "bo", "drop the nonadiabatic couplings"),
    ("bo", "harm", r"expand to second order in $\mathbf{u}$"),
    ("harm", "ph", "quantize the normal modes"),
    ("ph", "pol", "add the long-range dipole field"),
    ("pol", "corr", "keep all phonon orders"),
    ("corr", "anh", "add cubic and quartic terms"),
    ("bo", "ep", "restore", dict(start="right", end="left", side="above", ls="--")),
    ("dfpt", "harm", "force\nconstants", dict(start="left", end="right", side="above")),
]
chapmap.draw(N, E, chapmap.outpath(__file__, "ch05"), size=(5.4, 5.8), height=y(0) + 1.05)
