"""Checks behind Sect. 13.1 (we:13-onset): the phonon-assisted onset of silicon is reached with q along the valley
axis, and letting the pair move off the band extrema (total pair momentum k_c + dP, kinetic energy dP^2/2M_eh)
lowers the threshold by well under a meV. Phonons: figscripts/ch05/si_ifc.py (PBE at the measured a, Sect. 5.2).
q tilted from [100] by theta in the (001) plane (q in x-y) and in the (01-1)-containing plane (q in x-(y+z)).
Run: python onset13_1.py (about 1 min). Log: onset13_1.log.
"""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch05"))
import si_ifc
HBARC = 1973.269804; ME = 510998.95
VMAX = 794.5 / 299792.458; EG = 1.17
G1 = 2 * np.pi * HBARC / 5.431; KC = 0.85 * G1
M_EH = (0.916 + 0.277) * ME

def wmin(Q):  # lowest branch, eV, Q cartesian eV
    return si_ifc.phonons(np.atleast_2d(Q) / G1)[0][:, 0] / 1e3

def mreq(q, E):
    return q ** 2 / (2 * (q * VMAX - E)) if q * VMAX > E else np.inf

qs = np.linspace(820, 980, 81)
best = {}
for plane, perp in (("(001)", np.array([0, 1, 0.])), ("{011}", np.array([0, 1, 1.]) / np.sqrt(2))):
    for th in (0.0, 0.05, 0.1, 0.2, 0.3):
        qhat = np.cos(th) * np.array([1, 0, 0.]) + np.sin(th) * perp
        Q = KC * np.array([1, 0, 0.])[None, :] - qs[:, None] * qhat[None, :]
        w = wmin(Q)
        m = np.array([mreq(qq, EG + ww) for qq, ww in zip(qs, w)])
        j = int(np.argmin(m))
        print(f"{plane} tilt {th:.2f} rad: m_PA = {m[j]/1e6:.5f} MeV at q = {qs[j]:.0f} eV, omega = {w[j]*1e3:.2f} meV")
# relaxation of the pair off the extrema at the on-axis optimum
q0 = 896.0
Qs = np.array([KC - q0, 0, 0.])
w0 = wmin(Qs)[0]
d = np.linspace(-60, 60, 25)   # eV
DP = np.array([[a, b, c] for a in d for b in d for c in d])
vals = (np.sum(DP ** 2, axis=1) / (2 * M_EH)) + wmin(Qs[None, :] + DP) - w0
k = int(np.argmin(vals))
print(f"on-axis Q* = {Qs[0]/G1:.3f} (2pi/a), omega_TA = {w0*1e3:.3f} meV; best relaxation dP = {DP[k]} eV: "
      f"threshold change {vals[k]*1e3:.4f} meV (grid +-60 eV, step 5 eV; M_eh = 1.19 m_e)")
# passes of WE 13.1 (q* = 2E/v_max, Q* = k_c - q* on the axis), free pair and bound pair (E_x^b = 14.7 meV)
for lab, gap in (("free pair", EG), ("bound pair", EG - 0.0147)):
    w = 0.0
    for it in range(3):
        E = gap + w
        qst = 2 * E / VMAX
        w = wmin(np.array([[KC - qst, 0, 0.]]))[0]
        print(f"WE pass {it+1} ({lab}): E = {E:.4f} eV, q* = 2E/v_max = {qst:.1f} eV, Q* = {KC - qst:.1f} eV = "
              f"{(KC - qst)/G1:.3f} (2pi/a) = {(KC - qst)/HBARC:.3f} 1/A, omega_TA(Q*) = {w*1e3:.2f} meV; "
              f"onset 2(gap + omega)/v^2 = {2*(gap + w)/VMAX**2/1e6:.4f} MeV")
