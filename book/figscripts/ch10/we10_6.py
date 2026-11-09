"""Worked example 10.6 (Sect. 10.6): the germanium 3d onset in q, the mass that reaches it, and the 3d share of the
heavy-mediator rate in the model of Fig. 10.5. Prints every number of the worked example.

Rate weight per atom (heavy mediator, F_DM = 1): the q- and omega-dependent part of eq:1.5-rate,
    W_nl(m_chi) = int q dq int domega eta(v_min) S_at_nl(q, omega),   v_min = omega/q + q/(2 m_chi),
common prefactors cancel in the ratio 3d / valence. eta: closed form of App. D.1 (rate10_2.eta), book halo.
Valence: crystal IP table of Knapen, Kozaczuk and Lin for q <= 22.5 keV (omega <= 81 eV; ge_ip_binned.npz), atomic
plane-wave model above. 3d: plane-wave model, with and without the Fermi factor (Z_eff = 1), as fig10_5.py.
Threshold: one electron-hole pair, omega >= E_g = 0.744 eV for the valence.
"""
import numpy as np
import core10_6 as c
import rate10_2 as r
from core10_6 import table, fermi

ge = c.atom("Ge")
sh = ge["3D"]
om, qt, ip, Om = table("Ge")

# mass needed to reach q at the 3d threshold: v_min(q, omega_th) <= v_max
for e in (29.2, 29.8):
    wth = 0.744 + e
    for q in (12.45e3, 13.0e3):
        m = q / (2 * (c.VMAX - wth / q))
        print(f"3d edge {e} eV, q = {q / 1e3:.2f} keV: v_min <= v_max needs m_chi >= {m / 1e6:.1f} MeV")
wth = 0.744 + 29.2
for m in (10e6, 20e6, 30e6):
    disc = c.VMAX ** 2 - 2 * wth / m
    print(f"m = {m / 1e6:.0f} MeV reaches the 3d5/2 edge for q = {m * (c.VMAX - np.sqrt(disc)) / 1e3:.1f}-"
          f"{m * (c.VMAX + np.sqrt(disc)) / 1e3:.1f} keV")


def weight(m, Sfun, q, w):
    inner = np.array([np.trapezoid(r.eta(w / qq + qq / (2 * m)) * Sfun(qq, w), w) for qq in q])
    return np.trapezoid(q * inner, q)


def S_tab(q, w):
    j = np.argmin(abs(qt - q))
    return q ** 2 * Om * np.interp(w, om, ip[:, j], right=0.0) / (8 * np.pi ** 2 * c.ALPHA)


def S_3dF(q, w):
    p = np.sqrt(2 * c.ME * np.maximum(w - sh.ecore, 1e-6))
    return sh.S(q, w) * fermi(p)


for m in (10e6, 20e6, 30e6, 50e6, 100e6, 1e9):
    qmax = 2 * m * c.VMAX
    wv = np.linspace(0.744, 81.0, 500)
    Wv = weight(m, S_tab, np.linspace(500, min(22.5e3, qmax), 300), wv)
    if qmax > 22.5e3:
        Wv += weight(m, lambda q, w: ge["4S"].S(q, w) + ge["4P"].S(q, w), np.linspace(22.5e3, qmax, 300),
                     np.linspace(0.744, qmax * c.VMAX, 800))
    q3 = np.linspace(11.3e3, max(qmax, 11.4e3), 400)
    w3 = np.linspace(sh.eth, max(qmax * c.VMAX, sh.eth + 1), 800)
    W3, W3F = weight(m, sh.S, q3, w3), weight(m, S_3dF, q3, w3)
    print(f"m = {m / 1e6:6.0f} MeV: 3d/valence rate = {W3 / Wv:.2e} (plane waves), {W3F / Wv:.2e} (Fermi factor); "
          f"Fermi/plane = {W3F / max(W3, 1e-300):.1f}")
