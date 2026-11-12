"""Chapter map of Chap. 14 (fig:14-map): magnetic excitations, from the spin waves of Sect. 7.1 and the spin rows of
Sect. 8.1 through one-magnon scattering to two-magnon continua, absorption into uniform modes, neutron data, chiral
targets and coherent fields. Style of Fig. 1.8 via figscripts/chapmap.py. No numbers are plotted; tags give section
numbers and the Limit Check numbers the chapter plans in order (Limit Check 14.1 = lim:14.1a, 14.2 = lim:14.3a,
14.3 = lim:14.4a, 14.4-14.5 = lim:14.5a/b, 14.6-14.8 = lim:14.6a-c). Rerun when the later sections fix their boxes.
Output: tex/figures/ch14/map14.pdf.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import chapmap

X, W = 0.1, 4.2
XR, WR = 6.3, 3.6
H2 = 1.15
P = 1.6
y = lambda i: 0.3 + (3 - i) * P
N = {
    "in": dict(x=X, y=y(0), w=W, shade="ext", title="Spin waves and spin couplings", h=H2,
               body="linear spin-wave theory, magnetic form factor;" "\n" r"spin rows $\mathbf{s}_e$, tensor $\mathfrak{D}_{ab}$",
               tag="Sects. 7.1, 8.1, 8.2"),
    "one": dict(x=X, y=y(1), w=W, title="One-magnon scattering", h=H2,
                body="transverse spin creates one magnon;" "\n" r"Bogoliubov weights; zero-point reduction $\Delta S$",
                tag="Sect. 14.1; Limit Check 14.1"),
    "two": dict(x=X, y=y(2), w=W, title="Two-magnon continua, hybrids", h=H2,
                body="longitudinal spin creates pairs;" "\n" "magnon-phonon modes",
                tag="Sect. 14.2"),
    "neu": dict(x=X, y=y(3), w=W, title="Spin responses from neutron data", h=H2,
                body="measured magnetic cross-section" "\n" "in place of a model",
                tag="Sect. 14.4; Limit Check 14.3"),
    "abs": dict(x=XR, y=y(1), w=WR, shade="light", title="Absorption into magnons", h=H2,
                body="uniform precession; Kittel mode;" "\n" "antiferromagnetic resonance",
                tag="Sect. 14.3; Limit Check 14.2"),
    "chi": dict(x=XR, y=y(3), w=WR, shade="light", title="Chiral, nonreciprocal targets", h=H2,
                body="inversion and time reversal" "\n" "broken; cross responses",
                tag="Sect. 14.5; Limit Check 14.4"),
    "coh": dict(x=XR, y=y(2), w=WR, shade="light", title="Coherent fields", h=H2,
                body="classical wave; precessing" "\n" "nuclear spins",
                tag="Sect. 14.6; Limit Checks 14.5-14.7"),
}
E = [
    ("in", "one", r"Holstein-Primakoff to order $|\mathbf{S}|$;" "\n" "one transverse spin flip"),
    ("one", "two", r"next order in $1/|\mathbf{S}|$:" "\n" "longitudinal weight"),
    ("two", "neu", "measured response"),
    ("one", "abs", r"$\mathbf{k} \to 0$:" "\n" "absorption", dict(start="right", end="left", side="above", sfrac=0.7, efrac=0.7)),
    ("one", "chi", "break inversion" "\n" "and time reversal", dict(start="right", end="left", side="left", sfrac=0.3,
                                                                     dx=0.435, dy=-0.66)),
    ("abs", "coh", "classical field", dict(side="left")),
]
chapmap.draw(N, E, chapmap.outpath(__file__, "ch14"), size=(5.6, 4.4), height=y(0) + 1.25)
