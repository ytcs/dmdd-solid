"""Chapter map of Chap. 13 (fig:13-map): phonon-assisted electron recoil, from the kinematics of the indirect-gap
window through the second-order amplitude, the rate and its screening to the optical limit, with the off-shell
window, temperature, and excitons with phonons as side objects, and the silicon window as the end point. Style of
Fig. 1.8 via figscripts/chapmap.py. No numbers are plotted; tags give section and Limit Check numbers (Limit Check
13.1 = lim:13.5a, 13.2 = lim:13.7a, the two limit checks the chapter plans). Output: tex/figures/ch13/map13.pdf.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import chapmap

X, W = 0.1, 4.6
XR, WR = 6.2, 3.7
H2 = 1.15
P = 1.6
y = lambda i: 0.3 + (5 - i) * P
N = {
    "in": dict(x=X, y=y(0), w=W, shade="ext", title="Zero-phonon electron recoil", h=H2,
               body="crystal form factor, loss function;" "\n" "zero-phonon electronic sector",
               tag="Chap. 10; Sect. 8.6"),
    "kin": dict(x=X, y=y(1), w=W, title="Indirect-gap window", h=H2,
                body=r"$E_{\mathrm{min}}(\mathbf{q})$ against the reach;" "\n" r"$m_{\mathrm{min}}^{\mathrm{PA}}$ and $m_{\mathrm{min}}^{\mathrm{ZP}}$",
                tag="Sect. 13.1"),
    "amp": dict(x=X, y=y(2), w=W, title="Four-path amplitude", h=H2,
                body="unrestricted band sum; no interference" "\n" "with the zero-phonon line; adiabatic form",
                tag="Sect. 13.2"),
    "rate": dict(x=X, y=y(3), w=W, title="Phonon-assisted rate", h=H2,
                 body=r"loss function $L^{\mathrm{PA}}(\mathbf{q},\omega)$; Bose factors;" "\n" "onset exponent",
                 tag="Sect. 13.3"),
    "scr": dict(x=X, y=y(4), w=W, title="Screened rate", h=H2,
                body=r"external $1/\varepsilon$; pair-channel $W^{\mathrm{scr,R}}$;" "\n" r"$L^{\mathrm{PA}} = \varepsilon_2^{\mathrm{PA}}/(\varepsilon_1^0)^2$",
                tag="Sect. 13.4"),
    "opt": dict(x=X, y=y(5), w=W, title="Optical limit", h=H2,
                body="phonon-assisted absorption;" "\n" "absorption data transferred to mK",
                tag="Sect. 13.5"),
    "off": dict(x=XR, y=y(2), w=WR, shade="light", title="Off-shell window", h=H2,
                body="soft phonons; resonant" "\n" "denominators; Fano term", tag="Sect. 13.6"),
    "temp": dict(x=XR, y=y(3), w=WR, shade="light", title="Temperature, zero point", h=H2,
                 body="renormalized zero-phonon" "\n" "response; special displacements", tag="Sect. 13.7"),
    "exc": dict(x=XR, y=y(4), w=WR, shade="light", title="Exciton replicas", h=H2,
                body="exciton-phonon replicas;" "\n" "absorption of bosons", tag="Sect. 13.8"),
    "win": dict(x=XR, y=y(5), w=WR, title="The silicon window", h=H2,
                body="edges, selection rule," "\n" "what is open", tag="Sect. 13.9"),
}
E = [
    ("in", "kin", "below the zero-phonon edge:" "\n" "a phonon carries the momentum"),
    ("kin", "amp", "second order: one density" "\n" "and one electron-phonon vertex"),
    ("amp", "rate", r"square; Bose factors $n + 1$, $n$"),
    ("rate", "scr", "screen the density line" "\n" "and the pair"),
    ("scr", "opt", r"$q \to 0$"),
    ("amp", "off", "first-order\ntransition\non shell", dict(start="right", end="left", side="below")),
    ("rate", "temp", "renormalized\nbands", dict(start="right", end="left", side="above")),
    ("rate", "exc", "bound pair", dict(start="right", end="left", side="below", conn="arc3,rad=0.15")),
    ("opt", "win", "edges and\nrates", dict(start="right", end="left", side="above")),
]
chapmap.draw(N, E, chapmap.outpath(__file__, "ch13"), size=(5.6, 6.0), height=y(0) + 1.25)
