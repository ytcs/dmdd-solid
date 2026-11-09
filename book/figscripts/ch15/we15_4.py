"""Worked example 15.4 (we:15-holstein): the Holstein onset in aluminum, and the dark-photon rate at 1 meV.

Inputs as in abs15.py: Delta_BCS = 0.18 meV; omega_p = 12.29 eV; Debye a2F_tr with lambda_tr = 0.39, omega_D = 37 meV;
v_F = 6.753e-3 (al_constants.py); rho_T = 2.70 g cm^-3; rho_chi = 0.3 GeV cm^-3; halo speed 1e-3 for the momentum of the absorbed boson.
Sound speeds from the 0 K elastic constants (al_constants.py; Kamm-Alers via arXiv:2109.13551 Table 2):
c_LA = sqrt(C11/rho) along [100], c_TA = sqrt(C44/rho), rho = 2.73 g cm^-3 near 0 K.  k_F = 1.749 A^-1 (free electrons, three per atom).
Dark photon: Eq. 10.7-dp with eps = 1 - omega_p^2/omega^2 + i sigma_1/omega (condensate sigma_2 = omega_p^2/omega).
Onset: for omega - 2 Delta << Delta the integrand has omega - omega' -> 2 Delta and g_I -> pi/2, so
    sigma_1^S -> (omega_p^2/omega^2)(2 pi/omega) (2 lambda_tr/omega_D^4)(pi/2)(2 Delta)(omega - 2 Delta)^5/5.
Run: python we15_4.py
"""
import numpy as np
import abs15 as A

D = A.DELTA
cL = A.alc.C_LA
cT = A.alc.C_TA
KF = A.alc.KF

w = 1e-3
sN = A.sigma_holstein(w, coh="N")
sS = A.sigma_holstein(w)
print("omega = 1 meV = %.2f Delta" % (w / D))
print("gamma_H(1 meV) = %.3e eV (closed form %.3e); sigma_1^N = %.4g eV; sigma_1^S = %.4g eV; ratio %.3f"
      % (sN * w**2 / A.WP**2, A.gammaH_debye_closed(w), sN, sS, sS / sN))
print("momentum of the absorbed boson m v = %.2g eV; omega/v_F = %.3f eV; k_F = %.0f eV" % (w * 1e-3, w / A.VF, KF))
print("sound speeds c_L = %.0f m/s = %.3e, c_T = %.0f m/s = %.3e" % (cL * A.C_MS, cL, cT * A.C_MS, cT))
print("largest phonon energy at 1 meV: omega - 2 Delta = %.2f meV; its momentum (omega - 2 Delta)/c_L = %.1f eV, /c_T = %.1f eV, k_F/that = %.0f"
      % ((w - 2 * D) * 1e3, (w - 2 * D) / cL, (w - 2 * D) / cT, KF / ((w - 2 * D) / cT)))
for x in (2.05, 2.2, 2.5):
    ww = x * D
    exact = A.sigma_holstein(ww)
    asym = A.WP**2 / ww**2 * 2 * np.pi / ww * (2 * A.LAM_TR / A.WD**4) * (np.pi / 2) * (2 * D) * (ww - 2 * D) ** 5 / 5
    print("onset omega = %.2f Delta: sigma_1^S = %.3e eV, (omega - 2 Delta)^5 law %.3e, ratio %.3f; sigma_1^N = %.3e eV"
          % (x, exact, asym, exact / asym, A.sigma_holstein(ww, coh="N")))
L = A.loss_clean(w, sS)
LN = A.loss_clean(w, sN)
print("loss function L(1 meV) = %.3e (sigma_1 omega^3/omega_p^4 = %.3e); eps_1 = %.4g" % (L, sS * w**3 / A.WP**4, 1 - A.WP**2 / w**2))
R = A.rate_darkphoton(w, sS)
RN = A.rate_darkphoton(w, sN)
print("dark photon at 1 meV: R = %.3g zeta^2 per kg yr; zeta for 3 events per kg yr = %.2g (normal metal: %.3g, %.2g)"
      % (R, np.sqrt(3 / R), RN, np.sqrt(3 / RN)))
print("in-medium suppression zeta_eff^2/zeta^2 = 1/|eps|^2 = %.3e" % (1 / abs(1 - A.WP**2 / w**2 + 1j * sS / w) ** 2))
GR = A.tau_inv(50e-9)
print("50 nm film at 1 meV: Mattis-Bardeen sigma_1 = %.3g eV = %.2g times the Holstein value" % (A.sigma_MB(w, GR), A.sigma_MB(w, GR) / sS))
# free-electron plasma frequency of aluminum (three electrons per atom, a = 4.05 A) against the computed intraband value
ne = 12 / (4.05 / A.HBARC) ** 3
print("free-electron omega_p = sqrt(e^2 n_e/m_e) = %.2f eV; computed intraband value used here %.2f eV" % (np.sqrt(A.E2 * ne / A.ME), A.WP))
# pair-channel (ladder) dressing of the final pair, (Delta/v_F Q)^2, at the phonon momentum Q = (omega - 2 Delta)/c_L
for x in (2.2, 1e-3 / D):
    ww = x * D
    Q = (ww - 2 * D) / cL
    print("ladder dressing at omega = %.2f Delta: Q = %.2f eV, (Delta/v_F Q)^2 = %.1e" % (x, Q, (D / (A.VF * Q)) ** 2))
# weighted over the phonon-assisted integrand alpha^2F_tr(W)(omega - W) g_I at omega = 2.2 Delta (Debye omega'^4 law)
ww = 2.2 * D
num = A.integrate.quad(lambda W: float(A.a2f_debye(W)) * (ww - W) * float(A.gI((ww - W) / D)) * (D * cL / (A.VF * W)) ** 2,
                       0, ww - 2 * D, limit=200)[0]
den = A.integrate.quad(lambda W: float(A.a2f_debye(W)) * (ww - W) * float(A.gI((ww - W) / D)), 0, ww - 2 * D, limit=200)[0]
print("ladder dressing averaged over the phonon-assisted integrand at 2.2 Delta: %.1e (5/3 of the value at the most energetic phonon: %.1e)"
      % (num / den, 5 / 3 * (D * cL / (A.VF * (ww - 2 * D))) ** 2))
ww = 1e-3
num = A.integrate.quad(lambda W: float(A.a2f_debye(W)) * (ww - W) * float(A.gI((ww - W) / D)) * (D * cL / (A.VF * W)) ** 2,
                       0, ww - 2 * D, limit=200)[0]
den = A.integrate.quad(lambda W: float(A.a2f_debye(W)) * (ww - W) * float(A.gI((ww - W) / D)), 0, ww - 2 * D, limit=200)[0]
print("ladder dressing averaged at 1 meV: %.1e" % (num / den))
print("candidate strong-coupling factor 1/(1 + lambda_tr) = %.3f for lambda_tr = %.2f; its square %.3f" % (1 / (1 + A.LAM_TR), A.LAM_TR, 1 / (1 + A.LAM_TR) ** 2))
