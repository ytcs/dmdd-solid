"""FBC step 3: phonon emission at T -> 0 (emission only) on the same bands.

Deformation-potential couplings with the Jacoboni-Reggiani parameter set (Rev. Mod. Phys. 55, 645 (1983), Si tables,
as quoted by open sources; not read here):
  electrons, intervalley (hbar omega meV, D_tK 1e8 eV/cm, Z_f): g-TA (12, 0.5, 1), g-LA (18.5, 0.8, 1),
     g-LO (61.2, 11, 1), f-TA (19, 0.3, 4), f-LA (47.4, 2, 4), f-TO (59, 2, 4);  acoustic intravalley Xi = 9 eV;
  holes: optical (63 meV, 6.0e8 eV/cm), acoustic Xi = 5 eV;
  rho = 2.329 g/cm^3, u_l = 9.04e5 cm/s.
Full-band form (the standard high-energy deformation-potential model of full-band Monte Carlo): an intervalley or
optical mode j with a q-independent coupling scatters into any state of the final energy, so
  W_j(E) = (Z_j/Z_tot) pi D_j^2 / (rho omega_j) g_t(E - hbar omega_j)    (Z_tot = 6 for electrons, 1 for holes),
with g_t the total density of states per spin and volume of the carrier type on the EPM bands (all bands), and the
final state uniform on the shell (random k; exact for a q-independent coupling).  Acoustic intravalley emission at
T = 0 (q-limited, quasi-elastic, momentum-conserving to within q_c):
  W_ac(E) = Xi^2 q_c^3 / (12 pi rho u hbar v),  q_c = min(2 m_d v/hbar, q_cap),  mean loss (3/4) hbar u q_c,
for a parabolic valley of DOS mass m_d (0.32 e, 0.55 h) and q_cap = 0.5 (2pi/a) (larger q belongs to the intervalley
acoustic modes above).  First-principles (DFPT) couplings are stage 2.
Outputs data/phonon_<variant>.npz: energy grid, W_j(E) per mode, hbar omega_j, DOS.  Couplings scaled by FBC_DSCALE
(D^2 multiplier) for the uncertainty runs.
Run: python3 phonon.py
"""
import fbc_common  # first: single-threaded BLAS before numpy loads  # noqa: F401
import os
import numpy as np
from fbc_common import make_epm, model_edges, RY, NV, EG, DATA, Grid, HBAR, A_LAT, json_load

EV = 1.602176634e-12        # erg
RHO = 2.329                 # g/cm^3
UL = 9.04e5                 # cm/s
HB2M = 3.80998212           # eV A^2
MODES_E = [("g-TA", 12e-3, 0.5e8, 1), ("g-LA", 18.5e-3, 0.8e8, 1), ("g-LO", 61.2e-3, 11e8, 1),
           ("f-TA", 19e-3, 0.3e8, 4), ("f-LA", 47.4e-3, 2e8, 4), ("f-TO", 59e-3, 2e8, 4)]
MODES_H = [("op", 63e-3, 6.0e8, 1)]
XI = {"e": 9.0, "h": 5.0}
MD = {"e": 0.32, "h": 0.55}
ZTOT = {"e": 6, "h": 1}


def dos(variant, n=28, sig=0.04, emax=22.5):
    """total DOS per spin per cm^3 per eV for electrons (E above CBM) and holes (E below VBM), eV grid."""
    si = make_epm(variant)
    evbm, ecbm, _ = model_edges(si)
    delta = (EG - (ecbm - evbm)) if variant == "scissor" else 0.0
    gap = ecbm - evbm + delta
    g = Grid(n)
    e = np.concatenate([si.bands(g.k[i:i + 512], nb=24) for i in range(0, g.N, 512)]) - evbm
    e[:, NV:] += delta
    Ee = (e[:, NV:] - gap).ravel()
    Eh = (-e[:, :NV]).ravel()
    x = np.arange(0, emax, 0.005)
    vol = (A_LAT * 1e-8) ** 3 / 4
    out = {}
    for t, arr in (("e", Ee), ("h", Eh)):
        h, edges = np.histogram(arr, bins=np.append(x - 0.0025, x[-1] + 0.0025))
        kk = np.arange(-int(4 * sig / 0.005), int(4 * sig / 0.005) + 1) * 0.005
        ker = np.exp(-kk ** 2 / (2 * sig ** 2))
        ker /= ker.sum()
        d = np.convolve(h, ker, mode="same") / (g.N * 0.005 * vol)
        out[t] = d
    return x, out, gap


def rates(variant="refit", dscale=1.0, xiscale=1.0):
    x, g, gap = dos(variant)
    out = dict(E=x, gap=gap)
    for t, modes in (("e", MODES_E), ("h", MODES_H)):
        W, hw, names = [], [], []
        for nm, w, D, Z in modes:
            om = w / (HBAR)                                     # rad/s
            gf = np.interp(x - w, x, g[t], left=0.0)
            W.append((Z / ZTOT[t]) * np.pi * (dscale * D ** 2) * gf * EV / (RHO * om))      # 1/s
            hw.append(w)
            names.append(nm)
        # acoustic: parabolic valley mapping v(E) = sqrt(2E/m_d)
        m = MD[t] * 9.1093837e-28
        v = np.sqrt(2 * np.maximum(x, 1e-6) * EV / m)            # cm/s
        hbar_cgs = HBAR * EV                                    # erg s
        qcap = 0.5 * 2 * np.pi / (A_LAT * 1e-8)                 # 1/cm
        qc = np.minimum(2 * m * v / hbar_cgs, qcap)
        Wac = xiscale * (XI[t] * EV) ** 2 * qc ** 3 / (12 * np.pi * RHO * UL * hbar_cgs * v)
        Wac[x < 1e-3] = 0
        loss = 0.75 * hbar_cgs * UL * qc / EV                   # eV
        out[f"W_{t}"] = np.array(W)
        out[f"hw_{t}"] = np.array(hw)
        out[f"names_{t}"] = np.array(names)
        out[f"Wac_{t}"] = Wac
        out[f"lossac_{t}"] = loss
        out[f"dos_{t}"] = g[t]
    return out


if __name__ == "__main__":
    for variant in ("refit", "scissor"):
        r = rates(variant)
        np.savez(os.path.join(DATA, f"phonon_{variant}.npz"), **r)
        x = r["E"]
        for t in ("e", "h"):
            for E in (0.05, 0.5, 1.0, 2.0, 3.0, 5.0, 8.0):
                i = int(np.argmin(np.abs(x - E)))
                Wo = r[f"W_{t}"][:, i].sum()
                print(f"{variant} {t} E={E:4.2f}: W_op+iv = {Wo:.3e} /s, W_ac = {r[f'Wac_{t}'][i]:.3e} /s, "
                      f"dE/dt = {(r[f'W_{t}'][:, i] * r[f'hw_{t}']).sum() + r[f'Wac_{t}'][i] * r[f'lossac_{t}'][i]:.3e} eV/s, "
                      f"DOS = {r[f'dos_{t}'][i]:.3e} /eV/cm^3")
