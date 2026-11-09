"""Sect. 15.4-spin and App. D.40: corrections to direct spin-current pair breaking beyond the bare BCS bubble, the
normal-metal spin-current absorption from electron-electron collisions, and the axion-like-particle reach in aluminum.

Formulas (T = 0; abs15.py inputs: Delta_BCS = 0.18 meV, omega_p^intra = 12.29 eV, rho_T = 2.70 g cm^-3, rho_chi = 0.3 GeV cm^-3):
  bare BCS: sigma^J_dir (Eq. 15.4-sJ), integral (pi/2) omega_p^2.
  Coherent weight near 2 Delta: sigma^J = Z_s sigma^J_dir with Z_s = (1 + F1a/3)/(1 + lambda_ep). The factor
    1/(1 + lambda_ep) is the quasiparticle residue of Eq. 6.4-mass: the spin Drude weight of the normal metal at
    omega << omega_D is omega_p^2/(1 + lambda_ep), like the charge Drude weight; the rest of the sum rule lies near
    omega_D (spin analogue of the Holstein band). lambda_ep = 0.43 (specific heat, Sect. 6.4).
  Fermi-liquid dressing (Leggett form). With f(omega) the bare BCS spin-current bubble normalized to f(0) = 1,
      f(w) = Int_0^inf dt 4/(4 cosh^2 t - w^2)       (w = omega/Delta; principal value above 2),
      Im f(w) = 2 pi/(w sqrt(w^2 - 4)) for w > 2,
    the dressed kernel is K_s = (n/m*)(1 + F)(1 - f)/(1 + F f), F = F1a/3, and sigma^J = -Im K_s/omega. Its ratio to
    the bare BCS value at the same omega is r(F) = Im[(1 + F)(f - 1)/(1 + F f)]/Im f.
    For F < 0, 1 + F Re f(w) = 0 has a root below 2 Delta: a bound spin-one, l = 1 mode.
  Normal metal, spin current relaxed by electron-electron collisions (spin Coulomb drag) at T -> 0:
      Gamma_sd = beta omega^2, beta = 0.03-0.3 /eV (Quinn-Ferrell scale), sigma^J_N = omega_p^2 Gamma_sd/(omega^2 + Gamma_sd^2).
    This is an order-of-magnitude estimate; beta for aluminum is not computed here.
  ALP rate: Eq. 10.7-alp with sigma^J (abs15.rate_alp).
Run: python spin15.py > spin15.log
"""
import numpy as np
from scipy import integrate
from scipy.optimize import brentq
import abs15 as A

D = A.DELTA
LAM_EP = 0.43
Z = 1 / (1 + LAM_EP)


def g3(sig, w):
    return np.sqrt(3 / A.rate_alp(w, sig))


def f_bub(w):
    h = lambda t: 4.0 / (4 * np.cosh(t) ** 2 - w**2)  # noqa: E731
    if w < 2:
        a = w / 2   # closed form below the edge: Int_0^inf dt/(cosh^2 t - a^2) = arcsin(a)/(a sqrt(1 - a^2))
        return complex(1.0 if a == 0 else np.arcsin(a) / (a * np.sqrt(1 - a * a)), 0.0)
    t0 = np.arccosh(w / 2)
    # principal value: h(t) = reg(t)/(t - t0), integrated with the Cauchy weight
    reg = lambda t: 4.0 / (4 * (np.cosh(t) + w / 2)) * ((t - t0) / (np.cosh(t) - w / 2) if abs(t - t0) > 1e-12 else 1 / np.sinh(t0))  # noqa: E731
    re = integrate.quad(reg, 0, 40, weight="cauchy", wvar=t0, limit=400)[0]
    return complex(re, 2 * np.pi / (w * np.sqrt(w**2 - 4)))


print("f(0) = %.6f (normalization 1)" % f_bub(0.0).real)
hq = integrate.quad(lambda t: 4.0 / (4 * np.cosh(t) ** 2 - 1.5**2), 0, 40)[0]
print("check: closed form below 2 Delta at w = 1.5: %.10f, quadrature %.10f" % (f_bub(1.5).real, hq))
I = integrate.quad(lambda w: f_bub(w).imag / w, 2, 2e3, limit=800)[0]
print("(2/pi) Int_2^inf Im f/w dw = %.4f (sum rule of the bare bubble, 1)" % (2 / np.pi * I))

m = 0.72e-3
sb = float(A.sigmaJ_direct(m))
print("\n--- ALP at m = 0.72 meV = 4 Delta ---")
print("bare BCS: sigma^J = %.3e eV, g_aee(3/kg-yr) = %.3g, events at g = 1e-13: %.3f" % (sb, g3(sb, m), A.rate_alp(m, sb, 1e-13)))
sz = Z * sb
print("with Z_s = 1/(1 + %.2f) = %.3f: sigma^J = %.3e eV, g_aee(3/kg-yr) = %.3g (x %.3f), events at g = 1e-13: %.3f"
      % (LAM_EP, Z, sz, g3(sz, m), np.sqrt(1 + LAM_EP), A.rate_alp(m, sz, 1e-13)))
s1S = A.sigma_holstein(m)
s1N = A.sigma_holstein(m, coh="N")
print("phonon-assisted sigma_1^S = %.3e eV (book recomputation, Debye a2F_tr), g_aee = %.3g; normal-metal sigma_1^N = %.3e eV"
      % (s1S, g3(s1S, m), s1N))
print("ratio g(phonon-assisted sigma_1^S)/g(direct with Z_s) = %.3g" % (g3(s1S, m) / g3(sz, m)))

print("\n--- Fermi-liquid dressing at 4 Delta (Leggett form), with Z_s = 1/(1 + lambda_ep) ---")
fv = f_bub(4.0)
for F in (0.1, 0.05, 0.0, -0.05, -0.1):
    r = ((1 + F) * (fv - 1) / (1 + F * fv)).imag / fv.imag
    print("F1a/3 = %+.2f: sigma^J/bare = %.3f, g_aee(3/kg-yr) = %.3g (change %+.0f %%)"
          % (F, r, g3(r * sz, m), (g3(r * sz, m) / g3(sz, m) - 1) * 100))
for F in (-0.05, -0.1, -0.2):
    w0 = brentq(lambda w: 1 + F * f_bub(w).real, 0.5, 2 - 1e-12, xtol=1e-14)
    print("F1a/3 = %+.2f: bound spin-one l = 1 mode at %.6f Delta, binding 2 Delta - omega = %.2e Delta" % (F, w0, 2 - w0))

print("\n--- 1 meV and the crossing with the normal-metal phonon-assisted sigma_1 ---")
w = 1e-3
print("1 meV: bare sigma^J = %.3e eV; with Z_s %.3e eV = %.2g times sigma_1^S = %.3e eV; g_aee(3/kg-yr) = %.2g"
      % (float(A.sigmaJ_direct(w)), Z * float(A.sigmaJ_direct(w)), Z * float(A.sigmaJ_direct(w)) / A.sigma_holstein(w),
         A.sigma_holstein(w), g3(Z * float(A.sigmaJ_direct(w)), w)))
xb = brentq(lambda w: float(A.sigmaJ_direct(w)) - A.sigma_holstein(w, coh="N"), 3e-3, 37e-3)
xz = brentq(lambda w: Z * float(A.sigmaJ_direct(w)) - A.sigma_holstein(w, coh="N"), 3e-3, 37e-3)
print("direct term equals normal-metal Holstein sigma_1 at %.1f meV (bare), %.1f meV (with Z_s)" % (xb * 1e3, xz * 1e3))

print("\n--- normal metal at T -> 0: spin current relaxed by electron-electron collisions (estimate) ---")
for beta in (0.03, 0.3):
    G = beta * m**2
    sN = A.WP**2 * G / (m**2 + G**2)
    print("beta = %.2f /eV: Gamma_sd = %.2e eV, sigma^J_N = %.3g eV = %.0f x phonon-assisted sigma_1^N; g_aee(3/kg-yr) = %.2g;"
          " direct (Z_s) / sigma^J_N = %.2g, bare / sigma^J_N = %.2g"
          % (beta, G, sN, sN / s1N, g3(sN, m), sz / sN, sb / sN))
