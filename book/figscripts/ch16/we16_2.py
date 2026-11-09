"""Worked example 16.2 (the acoustic plasmon of a two-band two-dimensional system) of Sect. 16.2: every number.

Model sheet (illustrative parameters, named in the text): two parabolic bands, spin-degenerate, each with areal density
n = 1.0e13 cm^-2, masses m_l = 0.2 m_e (light) and m_h = 4.0 m_e (heavy), suspended in vacuum (eps_a = eps_b = 1).
Formulas of Sect. 16.2:
  k_F = sqrt(2 pi n) (same in both bands), v_F = k_F/m;  total density of states of a band N = m/pi;
  2D Thomas-Fermi wavevector q_s = e^2 N_l/(eps_a + eps_b) = 2 alpha m_l (eps_a = eps_b = 1);
  heavy-band sheet plasma frequency omega_2D,h^2(q) = e^2 n q/((eps_a + eps_b) m_h);
  acoustic mode omega_a^2 = omega_2D,h^2/(1 + q_s/q) -> v_a^2 q^2, v_a^2 = n_h/(m_h N_l);
  weight share in L: (q/(q + q_s))^2 of the heavy band's f-sum (pi/2) omega_2D,h^2;
  width Gamma_a/omega_a = (v_a/v_Fl)/sqrt(1 - v_a^2/v_Fl^2).
Fuller check: eps = 1 + (q_s,l/q) f2(omega/q v_Fl) + (q_s,h/q) f2(omega/q v_Fh), both bands with the q << k_F
Lindhard function f2 of lowd16_2 (so the heavy band is no longer assumed dynamic), at q = 20 eV.
"""
import os
import sys
import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lowd16_2 as L

N_CM2 = 1.0e13
n = N_CM2 * (L.HBARC * 1e-7) ** 2        # eV^2  (1 cm = 1e7 nm)
ML, MH = 0.2 * L.ME, 4.0 * L.ME
kF = np.sqrt(2 * np.pi * n)
vFl, vFh = kF / ML, kF / MH
NL, NH = ML / np.pi, MH / np.pi
qsl = L.E2 * NL / 2
qsh = L.E2 * NH / 2
va = np.sqrt(n / (MH * NL))
x = va / vFl
print(f"n = {N_CM2:.1e} cm^-2 = {n:.1f} eV^2; k_F = {kF:.1f} eV = {kF/L.HBARC:.3f} nm^-1")
print(f"v_F,l = {vFl:.4e}, v_F,h = {vFh:.4e}; q_s,l = 2 alpha m_l = {qsl:.0f} eV (check {2*L.ALPHA*ML:.0f}); q_s,h = {qsh:.0f} eV")
print(f"v_a = {va:.4e} = {va*L.C_KMS:.1f} km/s; v_a/v_F,l = {x:.4f} (sqrt(m_l/2m_h) = {np.sqrt(0.2/8):.4f}); "
      f"v_a/v_F,h = {va/vFh:.4f}; v_a/v_max = {va/L.VMAX:.4f}")

q = 20.0
w2h = L.E2 * n * q / (2 * MH)
wa_form = np.sqrt(w2h / (1 + qsl / q))
share = (q / (q + qsl)) ** 2
gam = x / np.sqrt(1 - x ** 2)
print(f"q = {q} eV (q/k_F = {q/kF:.3f}, q/q_s,l = {q/qsl:.4f}):")
print(f"  omega_2D,h = {np.sqrt(w2h)*1e3:.2f} meV; omega_a = {wa_form*1e3:.3f} meV (v_a q = {va*q*1e3:.3f} meV)")
print(f"  weight share (q/(q+q_s))^2 = {share:.3e}; width Gamma_a/omega_a = {gam:.4f}, Gamma_a = {gam*wa_form*1e3:.3f} meV")
w2opt = L.E2 * q / 2 * (n / ML + n / MH)
print(f"  optical 2D plasmon of both bands omega = {np.sqrt(w2opt)*1e3:.1f} meV (q v_F,l = {q*vFl*1e3:.1f} meV)")
# next term of eq:16.2-2Dpl for two bands: + (3/4) <v_F^2> q^2, <v_F^2> weighted by the Drude weights n/m of the bands
vF2 = (n / ML * vFl**2 + n / MH * vFh**2) / (n / ML + n / MH)
print(f"  with the (3/4) v_F^2 q^2 term of eq:16.2-2Dpl (Drude-weighted): omega = {np.sqrt(w2opt + 0.75*vF2*q**2)*1e3:.1f} meV")

# fuller: both bands with the q << k_F 2D Lindhard function
w = np.linspace(1e-4, 0.03, 600001)
eps = 1 + (qsl / q) * L.f2(w / (q * vFl)) + (qsh / q) * L.f2(w / (q * vFh))
Lw = np.imag(-1 / eps)
mask = w < 3 * q * vFh * 4
pk, fw = L.fwhm(w[mask], Lw[mask])
print(f"  fuller (both bands Lindhard): peak {pk*1e3:.3f} meV, FWHM {fw*1e3:.3f} meV, Gamma/omega = {fw/pk:.4f}")
# weight: first moment of L within three widths of the peak, over the heavy band's f-sum (pi/2) omega_2D,h^2;
# the light band alone (no heavy band) gives the pair-continuum background in the same window
Ll = np.imag(-1 / (1 + (qsl / q) * L.f2(w / (q * vFl))))
win = (w > pk - 3 * fw) & (w < pk + 3 * fw)
m_line = np.trapezoid((w * Lw)[win], w[win]) / (np.pi / 2 * w2h)
m_bg = np.trapezoid((w * Ll)[win], w[win]) / (np.pi / 2 * w2h)
below = w < 0.5 * q * vFl
m_cont = np.trapezoid((w * Ll)[below], w[below]) / (np.pi / 2 * w2h)
print(f"  fuller first moment within peak +- 3 FWHM over (pi/2) omega_2D,h^2: {m_line:.3e} "
      f"(light-band continuum alone in the window {m_bg:.2e}; formula {share:.3e})")
print(f"  light-band continuum alone below {0.5*q*vFl*1e3:.1f} meV: {m_cont:.2e} of the same f-sum")
print(f"  heavy-band dynamic correction: (3/4)(v_F,h/v_a)^2 = {0.75*(vFh/va)**2:.3f}")

# kinematics of a halo particle
for m in [1e3, 1e4]:
    print(f"  m_chi = {m/1e3:.0f} keV: omega_max = {m*L.VMAX**2/2*1e3:.2f} meV, q_max = {2*m*L.VMAX:.2f} eV")
m_min_q = q / (2 * L.VMAX)
m_min_w = 2 * wa_form / L.VMAX ** 2
print(f"  to reach q_par = {q} eV: m_chi >= q/(2 v_max) = {m_min_q/1e3:.2f} keV; to deposit omega_a: m_chi >= {m_min_w/1e3:.2f} keV")
print(f"  total momentum needed for omega_a: omega_a/v_max = {wa_form/L.VMAX:.2f} eV (< q_par = {q} eV)")
