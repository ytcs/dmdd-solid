"""Worked example 12.3 and the remaining numbers of Sect. 12.3 (soft-limit coefficient from the f-sum; silicon numbers).
Run: python we12_3.py (prints every number quoted in the example and in the validity paragraphs).

(1) f-sum check of the coefficient: for each momentum p of the table, the fifth moment of the per-p Migdal weight,
    int domega omega^5 [4 alpha Z^2 (v.p)^2 L(p, omega)/(omega^4 p^2)] = 4 alpha Z^2 (v.p)^2/p^2 x int domega omega L,
    against the double-commutator value (v.p)^2 |v_kappa(p)|^2 n_e p^2/(2 m_e) with v_kappa = -Z e^2/p^2 and the valence
    density n_e (4 electrons per atom): the ratio is int omega L / ((pi/2) omega_p,val^2), the fraction of the valence
    f-sum the table holds at p. omega_p,val = 16.6 eV (Sect. 10.2).
(2) Leading correction to the soft limit: the exact free-recoil bracket [1/(omega - y) - 1/omega]^2 with y = v_N.p gives,
    after the angle average, (v_N^2 p^2/3 omega^4)[1 + (9/5) v_N^2 p^2/omega^2 + ...]; printed as the probability-weighted
    mean of (9/5) v_N^2 p^2/omega^2 at E_R = 100 eV and 1 keV (silicon, local fields, Z_ion(p)).
(3) Silicon at E_R = 100 eV: q, v_N, P (omega >= 1.11 eV), median and mean omega, plasmon share (p < 2.5 keV).
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mig12 as G  # noqa: E402

WP_VAL = 16.6

if __name__ == "__main__":
    print("(1) f-sum fraction held by the table, = ratio of the table fifth moment to the double-commutator value:")
    for p in [1e3, 2e3, 3e3, 5e3, 7.5e3, 10e3]:
        j = np.argmin(abs(G.QT - p))
        f = np.trapezoid(G.OM * G.LF[:, j], G.OM) / (np.pi / 2 * WP_VAL**2)
        print(f"   p = {G.QT[j]/1e3:5.2f} keV: {f:.3f}")
    # explicit coefficient check (symbolic identity, numbers at p = 2 keV)
    a = G.ALPHA
    e2 = 4 * np.pi * a
    p = 2e3
    ne = WP_VAL**2 * G.ME / e2                                   # valence density from omega_p,val
    lhs = 4 * a * (np.pi / 2) * (e2 * ne / G.ME) / p**2          # 4 alpha Z^2/p^2 (pi/2) omega_p^2, per Z^2 (v.p)^2
    rhs = (e2 / p**2)**2 * ne * p**2 / (2 * G.ME)               # |v|^2 n_e p^2/2m_e, per Z^2 (v.p)^2
    print(f"   coefficient check at p = 2 keV: loss-function form / double commutator = {lhs/rhs:.12f}")
    assert abs(lhs / rhs - 1) < 1e-12
    print(f"   valence density n_e = {ne:.4e} eV^3 = {ne/G.HBARC**3*1e24/1e23:.3f} x 10^23 cm^-3 (4 per atom: "
          f"{4/ (5.431**3/8):.4f} A^-3 = {4/(5.431**3/8)*1e24/1e23:.3f} x 10^23 cm^-3)")
    print("(2) leading correction (9/5) <v^2 p^2/omega^2>:")
    m = G.OM >= G.EG
    w = G.OM[m]
    K = G.KG[1:]
    integ = (K**2 * G.ZG[1:]**2)[None, :] * G.LF_G[m][:, 1:] / w[:, None]**4
    base = np.trapezoid(np.trapezoid(integ, K, axis=1), w)
    for ER in [100.0, 300.0, 1000.0]:
        v2 = 2 * ER / G.M
        corr = np.trapezoid(np.trapezoid(integ * (9 / 5) * v2 * K[None, :]**2 / w[:, None]**2, K, axis=1), w) / base
        print(f"   E_R = {ER:6.0f} eV (v_N = {np.sqrt(v2):.3e}): {corr:.4f}")
    print("(2b) expansion parameter v_N p/omega_e of the free-recoil bracket at the median p = 5.68 keV, omega_e = 1.2 eV,"
          " and the recoil term 2 p^2/(M omega_e):")
    for ER in [100.0, 1000.0]:
        vN = np.sqrt(2 * ER / G.M)
        print(f"   E_R = {ER:6.0f} eV: v_N p = {vN*5.68e3:.3f} eV, v_N p/omega_e = {vN*5.68e3/1.2:.3f}")
    print(f"   2 p^2/(M omega_e) = {2*5.68e3**2/(G.M*1.2):.2e}")
    print("(3) silicon at E_R = 100 eV:")
    ER = 100.0
    q = np.sqrt(2 * G.M * ER)
    y = G.dP_domega(ER)
    P = np.trapezoid(y[m], w)
    cum = np.concatenate([[0], np.cumsum(0.5 * (y[m][1:] + y[m][:-1]) * np.diff(w))]) / P
    print(f"   q = {q/1e6:.3f} MeV, v_N = {np.sqrt(2*ER/G.M):.3e} = {np.sqrt(2*ER/G.M)*299792.458:.1f} km/s")
    print(f"   P = {P:.3e}; with Z_ion = 4: {G.p_total(ER, zfix=4.0):.3e}; scalar RPA: {G.p_total(ER, resp='rpa'):.3e}")
    print(f"   median omega {np.interp(0.5, cum, w):.2f} eV, mean omega {np.trapezoid(w*y[m], w)/P:.2f} eV")
    pl = np.trapezoid(G.dP_domega(ER, kmax=2.5e3)[m], w) / P
    print(f"   share from p < 2.5 keV (plasmon region): {pl:.3f}")
    print(f"   q / median p ratio: {q/5.68e3:.0f}")
    # first moment and implied drag mass (for Sect. 12.5)
    E1 = np.trapezoid(w * y[m], w)
    print(f"   first moment {E1:.4e} eV -> delta M = {E1 * G.M / ER / G.ME:.1f} m_e (valence, table)")
