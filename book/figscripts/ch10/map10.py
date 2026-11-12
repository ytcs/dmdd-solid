"""Chapter map of Chap. 10 (fig:10-map): the ladder of the electronic density response (crystal form factor,
screened loss function, excitons, nuisances) on the left, and on the right the response classes that leave slow,
elastic density scattering (electron gas, spin and current rows, core shells, absorption, two insertions,
inelastic and fast dark matter). Style of Fig. 1.8 via figscripts/chapmap.py. No numbers are plotted; tags give
section and Limit Check numbers. Output: tex/figures/ch10/map10.pdf.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import chapmap

X, W = 0.1, 4.45
XR, WR = 6.35, 3.6
BUS = 4.8
H2 = 1.15
P = 1.5
y = lambda i: 0.3 + (5 - i) * P
N = {
    "ff": dict(x=X, y=y(0) - 0.2, w=W, title="Crystal form factor", h=H2,
               body="independent-particle structure" "\n" "factor; sum rules",
               tag="Sect. 10.1"),
    "loss": dict(x=X, y=y(1.5), w=W, title="Loss-function rate", h=H2,
                 body="random-phase screening, then local" "\n" "fields; sum-rule bounds",
                 tag="Sect. 10.2; Limit Checks 10.1, 10.2"),
    "exc": dict(x=X, y=y(3), w=W, title="Excitons at finite momentum", h=H2,
                body="Bethe-Salpeter rate; bound lines" "\n" "below the gap",
                tag="Sect. 10.5; Limit Check 10.5"),
    "nui": dict(x=X, y=y(4.5), w=W, title="Theory uncertainties", h=H2,
                body="many-body spread; gap and" "\n" "threshold", tag="Sect. 10.10"),
    "gas": dict(x=XR, y=y(0) - 0.2, w=WR, shade="light", title="The plasmon", h=H2,
                body="pole of the electron gas;" "\n" "threshold speed; decay", tag="Sect. 10.3; Limit Check 10.3"),
    "spin": dict(x=XR, y=y(1) - 0.2, w=WR, shade="light", title="Spin and current couplings", h=H2,
                 body="minimal response table; singlet" "\n" "and triplet blocks", tag="Sect. 10.4; Limit Check 10.4"),
    "core": dict(x=XR, y=y(2) - 0.2, w=WR, shade="light", title="Core and relativistic states", h=H2,
                 body="core shells within reach;" "\n" "relativistic corrections", tag="Sect. 10.6"),
    "abs": dict(x=XR, y=y(3) - 0.2, w=WR, shade="light", title="Absorption on electrons", h=H2,
                body="dark photon, axion-like particle," "\n" "scalar; in-medium mixing",
                tag="Sect. 10.7; Limit Checks 10.6, 10.7"),
    "two": dict(x=XR, y=y(4) - 0.2, w=WR, shade="light", title="Two-insertion processes", h=H2,
                body="pair absorption; dark Compton" "\n" "scattering", tag="Sect. 10.8; Limit Check 10.8"),
    "inel": dict(x=XR, y=y(5) - 0.2, w=WR, shade="light", title="Inelastic and fast dark matter", h=H2,
                 body="exothermic; boosted; fermionic" "\n" "absorption; in-medium decay",
                 tag="Sect. 10.9; Limit Check 10.9"),
}
bus_top = N["ff"]["y"] + 0.5 * H2
bus_bot = N["inel"]["y"] + 0.5 * H2
E = [
    ("ff", "loss", r"screen: divide by $|\varepsilon|^2$"),
    ("loss", "exc", "add the electron-hole" "\n" "attraction"),
    ("exc", "nui", "many-body" "\n" "spread"),
    ((BUS, 0), "gas", "collective" "\n" "mode", dict(end="left", side="above", dx=0.03)),
    ((BUS, 0), "spin", "spin and" "\n" "current rows", dict(end="left", side="above", dx=0.03)),
    ((BUS, 0), "core", r"large $q$:" "\n" "core shells", dict(end="left", side="above", dx=0.03)),
    ((BUS, 0), "abs", "absorbed," "\n" "not scattered", dict(end="left", side="above", dx=0.03)),
    ((BUS, 0), "two", "second order" "\n" "in the coupling", dict(end="left", side="above", dx=0.03)),
    ((BUS, 0), "inel", "inelastic, fast," "\n" "fermionic", dict(end="left", side="above", dx=0.03)),
]
chapmap.draw(N, E, chapmap.outpath(__file__, "ch10"), size=(5.4, 6.1), height=y(0) + 1.0,
             lines=[((X + W + 0.02, bus_top), (BUS, bus_top)), ((BUS, bus_bot), (BUS, bus_top))])
