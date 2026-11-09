"""Sapphire and 2H-SiC: direction-resolved incoherent nuclear response and the daily modulation of its rate (Sect. 11.7).
Inputs and model: lat11_7.py (site tensors of Stratman and Lin, arXiv:2411.03433, from the public DarkELF tables; T = 0;
incoherent approximation eq:11.3-inc with the q-projected DOS and 2W = q.B.q; coupling c_kappa = A_kappa).
Rates: heavy mediator, nucleon coupling, the book's halo (aniso11.py), m_chi = 10 MeV unless stated; v_min = q/2m_chi + wbar(q)/q
with wbar(q) the mean energy deposited above threshold at q (lat11_7.rate_vs_direction); the run with wbar = 0 is printed as a check.  Output: sap11_7.npz; numbers in sap11_7.log.
Laboratory: latitude 45 deg N; crystal c axis along the local vertical (mounting of Sect. 1.2's uniaxial example), so the angle
theta_lab between the wind and the c axis runs between 2.5 and 87.5 deg over a sidereal day (eq:1.2-angle).
Valid where the incoherent approximation is (q above a few q_BZ; q_BZ = 1.75 keV for the 10-atom rhombohedral cell of sapphire,
Omega = 84.9 A^3 from a = 4.759 A, c = 12.991 A, 1910.10716 Table I), i.e. m_chi above a few MeV.
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import aniso11 as AN  # noqa: E402
import lat11_7 as L  # noqa: E402

HBARC = 1973.269804
C_KMS = AN.C_KMS
OMEGA_SAP = np.sqrt(3) / 2 * 4.759**2 * 12.991 / 3          # A^3, rhombohedral primitive cell (10 atoms)
QBZ_SAP = (6 * np.pi**2 / OMEGA_SAP)**(1 / 3) * HBARC / 1e3     # keV


def rate_curve(inc, m_chi, wth, nq=60, grid=(32, 64), single=False, vhats=None, lmax=8):
    qmax = 2 * m_chi * AN.VESC / C_KMS + 2 * m_chi * AN.VE / C_KMS
    q = np.geomspace(0.3e3, qmax * 0.999, nq)
    qh, wq = AN.sphere_grid(*grid)
    sig, mom = (inc.single if single else inc.weights)(q, qh, wth, moment=True)       # (nq, nd)
    wbar = np.sum(wq * mom, axis=1) / np.maximum(np.sum(wq * sig, axis=1), 1e-300)
    th = np.radians(np.linspace(0, 90, 19))
    if vhats is None:
        vhats = np.stack([np.sin(th), 0 * th, np.cos(th)], axis=1)  # wind in the x-z plane, angle theta from c
    R = L.rate_vs_direction(sig, q, qh, wq, m_chi, vhats, wbar)
    R_nw = L.rate_vs_direction(sig, q, qh, wq, m_chi, vhats)
    # multipole truncations at the rate level: R(vhat) = sum_l int q^2 dlnq 2 pi Upsilon_l sum_m s_lm Y_lm(vhat)  (Funk-Hecke)
    coef = L.proj_real(sig, qh, wq, lmax)
    vstar = (q / (2 * m_chi) + wbar / q) * C_KMS
    dlq = np.gradient(np.log(q))
    Rl = {}
    for l in range(0, lmax + 1, 2):
        ups = AN.upsilon(l, vstar)
        Rl[l] = np.einsum("q,mq->m", q**2 * dlq * ups * 2 * np.pi, coef[l])
    return dict(q=q, th=th, vhats=vhats, R=R, R_nw=R_nw, Rl=Rl, sig=sig, qh=qh, wq=wq, wbar=wbar)


def trunc(Rl, vhats, lmax):
    tot = 0.0
    for l in range(0, lmax + 1, 2):
        tot = tot + np.einsum("m,mv->v", Rl[l], AN.ylm_real(l, vhats))
    return tot


def daily(res, lat=45.0, R=np.eye(3), nh=96):
    """Rate over a sidereal day from the multipoles (l <= 8), crystal axes R (rows) in (east, north, up)."""
    h = np.linspace(0, 2 * np.pi, nh, endpoint=False)
    v = AN.vhat_crystal(lat, h, R)
    r = trunc(res["Rl"], v, 8)
    return h, r


if __name__ == "__main__":
    print("sapphire: Omega = %.1f A^3, q_BZ = %.2f keV" % (OMEGA_SAP, QBZ_SAP))
    sap = L.Incoherent("darkelf_Al2O3_pDoS_anisotropic.dat", L.SAPPHIRE)
    sic = L.Incoherent("darkelf_SiC_pDoS_anisotropic.dat", L.SIC2H)
    out = {}
    for tag, inc in (("sap", sap), ("sic", sic)):
        for m in (10e6, 30e6):
            for wth in (1e-3, 25e-3, 80e-3, 300e-3):
                for single in (True, False):
                    if single and wth > 0.13:
                        continue
                    res = rate_curve(inc, m, wth, single=single)
                    R = res["R"]
                    full = R / R.mean()
                    # check: multipole sum (l <= 8) reproduces the direct angular integral
                    rt = trunc(res["Rl"], res["vhats"], 8)
                    h, rd = daily(res)
                    amp = (rd.max() - rd.min()) / (rd.max() + rd.min())
                    key = "%s_m%d_w%d_%s" % (tag, m / 1e6, wth * 1e3, "n1" if single else "all")
                    out[key + "_R"] = R
                    out[key + "_day"] = rd
                    print("%-22s [omega/q dropped: R(c)/R(perp) = %.4f] R(c)/R(perp) = %.4f; R2/R0 = %+.4f, R4/R0 = %+.5f, R6/R0 = %+.5f; max|l<=8 - direct|/R = %.1e;"
                          " daily amplitude at 45N, c vertical: %.4f"
                          % (key, res["R_nw"][0] / res["R_nw"][-1], R[0] / R[-1], res["Rl"][2][2] / res["Rl"][0][0], res["Rl"][4][4] / res["Rl"][0][0],
                             res["Rl"][6][6] / res["Rl"][0][0], np.abs(rt - R).max() / R.mean(), amp))
    np.savez(os.path.join(HERE, "sap11_7.npz"), th=np.degrees(res["th"]), h=h, **out)
    print("wrote sap11_7.npz")
