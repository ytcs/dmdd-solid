"""Chapter map of Chap. 19 (fig:19-map): from the electron-following nuclear response (Sects. 11.3, 11.4, 12.1) to the
hand-over and the partition of the recoil energy (19.1), the charge channel (19.2), Lindhard quenching and Bethe
stopping as limits (19.3), defects and stored energy (19.4), the balance law (19.5) and delayed release (19.6), which
hand the shares to the readout (Chap. 20).
Style of Fig. 1.8 via figscripts/chapmap.py. No numbers are plotted. The Limit Check tags assume the planned boxes
of Sects. 19.3 (two), 19.4 (one), 19.5 (two) and 19.6 (two), numbered in order through the chapter (19.1-19.7);
the caption references them live with \\cref. Output: tex/figures/ch19/map19.pdf.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import chapmap

H2 = 1.1
P = 1.55
y = lambda i: 0.25 + (6 - i) * P
XL, XR, W = 0.1, 5.4, 4.5
N = {
    "in": dict(x=2.2, y=y(0), w=5.6, shade="ext", title="Electron-following nuclear response", h=H2,
               body="multiphonon and impulse response; Migdal" "\n" "events counted apart",
               tag="Sects. 11.3, 11.4, 12.1"),
    "ho": dict(x=2.2, y=y(1), w=5.6, title="Recoil hand-over", h=H2,
               body="kicked zero-point ensemble on the energy surface;" "\n" "harmonic, anharmonic, cascade regimes",
               tag="Sect. 19.1"),
    "el": dict(x=XL, y=y(2), w=W, title="Electronic excitation", h=H2,
               body="binary threshold; close-collision" "\n" "excitation kernel",
               tag="Sect. 19.2"),
    "def": dict(x=XR, y=y(2), w=W, title="Defects and stored energy", h=H2,
                body="displacement and defect energy loss;" "\n" "bounds from calibration data",
                tag="Sect. 19.4; Limit Check 19.3"),
    "lin": dict(x=XL, y=y(3), w=W, shade="light", title="Lindhard quenching, Bethe stopping", h=H2,
                body="binary collisions in a continuum;" "\n" "stopping from the loss function",
                tag="Sect. 19.3; Limit Checks 19.1, 19.2"),
    "bal": dict(x=2.2, y=y(4), w=5.6, title="Energy balance law", h=H2,
                body="every share booked once, in time;" "\n" "heat quenching and its calibration identity",
                tag="Sect. 19.5; Limit Checks 19.4, 19.5"),
    "rel": dict(x=XR, y=y(5), w=W, title="Delayed release", h=H2,
                body="mobile defects at millikelvin;" "\n" "models of the low-energy excess",
                tag="Sect. 19.6; Limit Checks 19.6, 19.7"),
    "out": dict(x=2.2, y=y(6), w=5.6, shade="ext", title="Charge and phonon readout", h=H2,
                body="shares handed to drift, phonon" "\n" "transport and sensors",
                tag="later chapter"),
}
E = [
    ("in", "ho", "take the line without electronic excitation", dict(side="right")),
    ("ho", "el", "add nonadiabatic\nclose collisions", dict(sfrac=0.2, side="right", dx=0.6)),
    ("ho", "def", "keep the end basin", dict(sfrac=0.8, side="right", dx=0.05)),
    ("el", "lin", "drop the gap and the stored energy", dict(side="right")),
    ("lin", "bal", "", dict(efrac=0.2)),
    ("def", "bal", "", dict(efrac=0.8)),
    ("bal", "rel", "release the stored energy", dict(sfrac=0.85, side="right")),
    ("bal", "out", "", dict(sfrac=0.3, efrac=0.3)),
    ("rel", "out", "delayed events", dict(efrac=0.85, side="right")),
]
chapmap.draw(N, E, chapmap.outpath(__file__, "ch19"), size=(5.6, 7.2), height=y(0) + 1.2)
