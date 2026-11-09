"""Chapter map of Chap. 3 (fig:3-map): from the Coulomb Hamiltonian to Bloch bands, Kohn-Sham bands, plane-wave
and pseudopotential calculations and Wannier functions, ending at the density vertex of silicon.
Style of Fig. 1.8 via figscripts/chapmap.py. No numbers are plotted. Output: tex/figures/ch03/map03.pdf.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import chapmap

X, W = 0.1, 5.2
XR, WR = 6.4, 3.55
P = 1.42
y = lambda i: 0.15 + (7 - i) * P
N = {
    "coul": dict(x=X, y=y(0), w=W, shade="ext", title="Coulomb Hamiltonian",
                 body="electrons and point nuclei", tag="Sect. 2.3"),
    "lat": dict(x=X, y=y(1), w=W, title="Lattice and reciprocal space",
                body="Brillouin zone; crystal momentum; lattice sum", tag="Sect. 3.1"),
    "bloch": dict(x=X, y=y(2), w=W, title="Bloch states and bands",
                  body="nearly free electrons; tight binding; density vertex", tag="Sect. 3.2"),
    "ks": dict(x=X, y=y(3), w=W, title="Kohn-Sham equations",
               body="Hartree-Fock; density functionals; band-gap problem", tag="Sect. 3.4"),
    "sc": dict(x=X, y=y(4), w=W, title="Scissor shift",
               body="rigid conduction bands; rescaled velocity", tag="Sect. 3.4"),
    "pw": dict(x=X, y=y(5), w=W, title="Plane waves and pseudopotentials",
               body="cutoff; frozen core; all-electron vertex from PAW", tag="Sect. 3.5"),
    "wan": dict(x=X, y=y(6), w=W, title="Wannier functions",
                body="maximal localization; exact interpolation; one gauge", tag="Sect. 3.6"),
    "vert": dict(x=X, y=y(7), w=W, shade="ext", title="Density vertex of silicon",
                 body=r"$\langle m\mathbf{k}+\mathbf{q}|e^{i\mathbf{q}\cdot\mathbf{r}}|n\mathbf{k}\rangle$ from first principles",
                 tag="Chaps. 4, 10"),
    "si": dict(x=XR, y=y(2.55), w=WR, shade="light", title="Si, Ge and GaAs",
               body=r"valleys; $\mathbf{k}\cdot\mathbf{p}$ masses; spin-orbit;" "\n" "minimum pair energy",
               tag="Sect. 3.3", h=1.15),
    "core": dict(x=XR, y=y(5.55), w=WR, shade="light", title="Core states",
                 body="semicore shells; relativistic" "\n" "corrections", tag="Sect. 3.5", h=1.15),
}
E = [
    ("coul", "lat", "clamp the nuclei on a lattice"),
    ("lat", "bloch", "one electron in a periodic potential"),
    ("bloch", "ks", r"model potential $\to$ Kohn-Sham"),
    ("ks", "sc", "correct the Kohn-Sham gap"),
    ("sc", "pw", "expand in plane waves; drop the core"),
    ("pw", "wan", "rotate to localized orbitals"),
    ("wan", "vert", "interpolate on fine grids", dict(ls="--")),
    ("bloch", "si", "expand at\nthe band edges", dict(start="right", end="top", conn="arc3,rad=-0.3", side="end")),
    ("pw", "core", "restore\nthe core", dict(start="right", end="top", conn="arc3,rad=-0.3", side="end")),
]
chapmap.draw(N, E, chapmap.outpath(__file__, "ch03"), size=(5.4, 6.6), height=y(0) + 1.05)
