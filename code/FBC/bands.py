"""FBC step 1: bands. Band edges, valley energies and effective masses of the book EPM (Cohen-Bergstresser local),
with the rigid scissor to E_g = 1.160 eV (primary) and a refit of the three form factors (variant 'refit', used
only as the band-calibration uncertainty). Writes data/bands_summary.json and data/refit_formfactors.json.

Measured reference values (low T, quoted):  indirect gap 1.17 eV (4 K; book uses 1.160 eV at 123 K), CBM at 0.85 X,
m_l = 0.916, m_t = 0.191 (cyclotron resonance, Hensel-Hasegawa-Nakayama 1965 as quoted in standard tables),
L1c ~ 2.04 eV, Gamma15c 3.34 eV, Gamma2'c 4.15 eV (room-T values as tabulated by Kotani and van Schilfgaarde,
arXiv:0812.2923 Table I, from Madelung), X4v ~ -2.9 eV, L3'v ~ -1.2 eV, Gamma1v -12.5 +- 0.6 eV (photoemission,
as quoted by Chelikowsky-Cohen 1976), heavy/light hole masses (no SOC): m_hh[100] = 0.29 ... m_hh[111] = 0.73,
m_lh[100] = 0.20, m_lh[111] = 0.14 (Dresselhaus-Kip-Kittel parameters as quoted in standard tables).
Run: python3 bands.py
"""
from fbc_common import EPM as _E  # noqa: F401  (sets single-thread BLAS before numpy loads)
import json
import numpy as np
from scipy.optimize import least_squares
from fbc_common import EPM, EPM_custom, RY, model_edges, DATA, EG, NV, Grid, A_LAT

MEAS = dict(Eg=1.17, X1c=1.30, L1c=2.04, G15c=3.34, G2pc=4.15, X4v=-2.9, L3pv=-1.2, G1v=-12.5,
            ml=0.916, mt=0.191)
X = np.array([1.0, 0, 0]); L = np.array([.5, .5, .5]); G0 = np.zeros(3)
HB2M = 3.80998212          # eV A^2
UNIT = 2 * np.pi / A_LAT


def levels(si, delta):
    e = si.bands(np.array([G0, X, L]), nb=10)
    ev = e[0, 3]
    e = e - ev
    e[:, NV:] += delta
    evbm, ecbm, kc = model_edges(si)
    return dict(Eg=ecbm - evbm + delta, kcbm=kc, X1c=e[1, 4], L1c=e[2, 4], G15c=e[0, 4], G2pc=e[0, 7],
                X4v=e[1, 2], L3pv=e[2, 2], G1v=e[0, 0], width=-e[0, 0])


def mass(si, k0, d, band, h=0.004):
    """effective mass (m_e) of band at k0 along unit direction d by a 5-point second derivative (k in 2pi/a)."""
    ks = np.array([k0 + j * h * d for j in (-2, -1, 0, 1, 2)])
    e = si.bands(ks, nb=8)[:, band]
    d2 = (-e[0] + 16 * e[1] - 30 * e[2] + 16 * e[3] - e[4]) / (12 * (h * UNIT) ** 2)   # eV A^2
    return HB2M * 2 / d2


def summary(si, delta):
    lv = levels(si, delta)
    k0 = np.array([lv["kcbm"], 0, 0])
    lv["ml"] = mass(si, k0, np.array([1., 0, 0]), 4)
    lv["mt"] = mass(si, k0, np.array([0, 1., 0]), 4)
    h = 0.01
    for nm, d in (("100", np.array([1., 0, 0])), ("111", np.array([1., 1, 1]) / np.sqrt(3))):
        ks = np.array([j * h * d for j in (0, 1, 2)])
        e = si.bands(ks, nb=4)
        for b, lab in ((3, "hh"), (1, "lh")):
            # parabola through Gamma (degenerate point): E = -hbar^2 k^2/2m
            lv[f"m_{lab}{nm}"] = -HB2M * (2 * h * UNIT) ** 2 / (e[2, b] - e[0, b])
    return lv


def refit():
    keys = ["Eg", "L1c", "G15c", "X4v", "G1v"]
    wts = np.array([10, 1, 1, 1, 0.3])
    tgt = dict(MEAS, Eg=EG)

    def res(p):
        si = EPM_custom({3: p[0], 8: p[1], 11: p[2]})
        lv = levels(si, 0.0)
        return wts * np.array([lv[k] - tgt[k] for k in keys])
    r = least_squares(res, [-0.21, 0.04, 0.08], diff_step=1e-3)
    return r.x


if __name__ == "__main__":
    si = EPM("Si")
    evbm, ecbm, kc = model_edges(si)
    delta = EG - (ecbm - evbm)
    out = {"scissor": summary(si, delta), "raw": summary(si, 0.0), "delta": delta, "meas": MEAS}
    p = refit()
    json.dump({"VS": {"3": p[0], "8": p[1], "11": p[2]}}, open(f"{DATA}/refit_formfactors.json", "w"), indent=1)
    sf = EPM_custom({3: p[0], 8: p[1], 11: p[2]})
    out["refit"] = summary(sf, 0.0)
    out["refit_VS"] = list(p)
    # bands needed: highest band index whose minimum on a 12^3 grid is below EG + 20.5 eV above the VBM
    g = Grid(12)
    for nm, s, dl in (("scissor", si, delta), ("refit", sf, 0.0)):
        e = s.bands(g.k, nb=40) - s.bands(np.zeros((1, 3)), nb=4)[0, 3]
        e[:, NV:] += dl
        need = int(np.max(np.where(e.min(0) < out[nm]["Eg"] + 20.5)[0])) + 1
        out[nm]["nb_needed_20p5"] = need
        out[nm]["top_needed_min"] = float(e[:, need].min())
    for nm in ("raw", "scissor", "refit"):
        print(nm, {k: round(v, 3) if isinstance(v, float) else v for k, v in out[nm].items()})
    print("refit V_S(3,8,11) =", np.round(p, 4), " scissor delta =", round(delta, 4))
    json.dump(out, open(f"{DATA}/bands_summary.json", "w"), indent=1)
