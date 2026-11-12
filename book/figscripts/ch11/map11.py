"""Chapter map of Chap. 11 (fig:11-map): the lattice regimes of the nuclear response as the momentum transfer
grows (one acoustic phonon, multiphonon, impulse and free recoil, anharmonic and quantum crystals, nuisances) on
the left, and on the right the couplings and observables that branch off it (polar crystals, site-dependent
couplings, anisotropy, absorption). Style of Fig. 1.8 via figscripts/chapmap.py. No numbers are plotted; tags
give section and Limit Check numbers. Output: tex/figures/ch11/map11.pdf.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import chapmap

X, W = 0.1, 4.45
XR, WR = 6.35, 3.6
BUS = 4.8
H2 = 1.15
P = 1.75
y = lambda i: 0.3 + (5 - i) * P
N = {
    "in": dict(x=X, y=y(0) - 0.2, w=W, shade="ext", title="Harmonic crystal, master formula", h=H2,
               body="displacement correlations;" "\n" "nuclear operators", tag="Chaps. 5, 8"),
    "ac": dict(x=X, y=y(1) - 0.2, w=W, title="One acoustic phonon", h=H2,
               body="long-wavelength limit; sound" "\n" "speeds; light and heavy mediators",
               tag="Sect. 11.1; Limit Checks 11.1, 11.2"),
    "mp": dict(x=X, y=y(2) - 0.2, w=W, title="Multiphonon response", h=H2,
               body=r"$n$-phonon terms; incoherent" "\n" "approximation; exact weights",
               tag="Sect. 11.3; Limit Checks 11.5, 11.6"),
    "imp": dict(x=X, y=y(3) - 0.2, w=W, title="Impulse limit and free recoil", h=H2,
                body=r"peak at $E_R$; free recoil with" "\n" "the Helm form factor",
                tag="Sect. 11.4; Limit Check 11.7"),
    "anh": dict(x=X, y=y(4) - 0.2, w=W, title="Anharmonic and quantum crystals", h=H2,
                body="cubic decay; Markov-Krein band;" "\n" "solid helium",
                tag="Sect. 11.5; Limit Checks 11.8-11.10"),
    "nui": dict(x=X, y=y(5) - 0.2, w=W, title="Nuisance parameters", h=H2,
                body="truncations; sound speeds and" "\n" "Born charges", tag="Sect. 11.9"),
    "pol": dict(x=XR, y=y(1) - 0.2, w=WR, shade="light", title="Optical phonons, polar crystals", h=H2,
                body="phonon loss function; Born" "\n" "charge; band integral",
                tag="Sect. 11.2; Limit Checks 11.3, 11.4"),
    "iso": dict(x=XR, y=y(2) - 0.2, w=WR, shade="light", title="Nuclear spins and isotopes", h=H2,
                body=r"broadband response; mass" "\n" r"defect; $B - L$ vector",
                tag="Sect. 11.6; Limit Checks 11.11, 11.12"),
    "ani": dict(x=XR, y=y(3) - 0.2, w=WR, shade="light", title="Anisotropy", h=H2,
                body="rate at fixed orientation;" "\n" "daily modulation", tag="Sect. 11.7; Limit Check 11.13"),
    "abs": dict(x=XR, y=y(4) - 0.2, w=WR, shade="light", title="Absorption on phonons", h=H2,
                body="single phonon; acoustic modes" "\n" "of a finite body",
                tag="Sect. 11.8; Limit Checks 11.14-11.16"),
}
bus_top = N["pol"]["y"] + 0.5 * H2
bus_bot = N["abs"]["y"] + 0.5 * H2
E = [
    ("in", "ac", r"$q$ inside the zone: one phonon"),
    ("ac", "mp", "above the zone:" "\n" "all phonon orders"),
    ("mp", "imp", r"large $q$: orders" "\n" "merge into one peak"),
    ("imp", "anh", "add cubic and" "\n" "quartic terms"),
    ("anh", "nui", "truncations" "\n" "as nuisances"),
    ((BUS, 0), "pol", "couple to" "\n" "charge", dict(end="left", side="above", dx=0.03)),
    ((BUS, 0), "iso", "couplings that" "\n" "vary by site", dict(end="left", side="above", dx=0.03)),
    ((BUS, 0), "ani", "fix the crystal" "\n" "orientation", dict(end="left", side="above", dx=0.03)),
    ((BUS, 0), "abs", "absorbed," "\n" "not scattered", dict(end="left", side="above", dx=0.03)),
]
chapmap.draw(N, E, chapmap.outpath(__file__, "ch11"), size=(5.4, 6.8), height=y(0) + 1.0,
             lines=[((X + W + 0.02, bus_top), (BUS, bus_top)), ((BUS, bus_bot), (BUS, bus_top))])
