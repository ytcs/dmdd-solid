"""Limit 11.8a (fig:11-limit-8a): single-phonon absorption of a scalar coupled to electrons in GaAs.

Rate per kilogram-year per g_phiee^2 against m_phi across the optical band,
    R = (rho_chi/rho_T) (g^2 <v^2>/e^2) (eps_inf mu_red d / Z*)^2 L(m_phi)        (eq:11.8-Rscalar),
with d = v_Ga/M_Ga - v_As/M_As the mass-weighted difference of the site couplings.
  solid:  longitudinal-residue site coupling v = Z - Z*/eps_inf with the measured Z* = 2.11, eps_inf = 10.88 (Sect. 11.2, WE 5.6);
          (Z*/eps_inf varied by +-1 %, the precision of the splitting route of Sect. 11.2, moves the rate by -8.7 % / +9.0 %;
          printed, not drawn: on the log scale the band is narrower than the line.)
  (not drawn) rigid-ion structure of Mitridate et al., arXiv:2308.06314 v1, Eqs. (40)-(41), with ionic charges Q = +-3
          (N_Ga,e = 28, N_As,e = 36, text after their Eq. (44)): site coupling Z - Q/eps_inf.
  dotted: residue coupling with the PBE inputs of Sect. 5.5, Z* = 2.094, eps_inf = 13.70.
L(omega): damped one-branch dielectric function (abs11_8.GAAS_ARGS), widths 1e-2 x frequency (modelling choice of 2308.06314,
Sect. III A); its weight is the splitting value. In this model the full damped response of any density row is exactly
proportional to L (Sect. 11.8), so the curves differ only by their vertices.
Halo: <v^2> of the book's truncated Maxwellian (abs11_8.v2_mean, 378.9 km/s rms). rho_chi = 0.3 GeV/cm^3; rho_T = 5.361 g/cm^3.
Gray: |m_phi - omega_L| < 5 gamma_L, where a line of constant width describes the phonon (beyond it the frequency dependence of the
phonon self-energy matters; modelling statement, as in Sect. 5.7).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import abs11_8 as A
import phon11 as P

v2 = A.v2_mean()[0] / P.C_KMS**2
m = np.linspace(33.0e-3, 39.5e-3, 6001)
L = A.loss(m, *A.GAAS_ARGS)


def rate(zs, ei, q_ion=None):
    d = A.d_site(zs, ei, q_ion)
    return A.events_per_kgyr(L, A.RHO_GAAS, v2 / A.E2 * (A.EPSINF * A.MU * d / A.ZS)**2)


R0 = rate(A.ZS, A.EPSINF)
Rlo = rate(A.ZS * 0.99, A.EPSINF)
Rhi = rate(A.ZS * 1.01, A.EPSINF)
Rrig = rate(A.ZS, A.EPSINF, 3.0)
Rpbe = rate(2.094, 13.70)
i = np.argmax(R0)
print("peak at %.3f meV: residue %.3e, rigid %.3e (ratio %.2f), PBE %.3e (ratio %.2e); +-1%%: %.3f %.3f" %
      (m[i] * 1e3, R0[i], Rrig[i], Rrig[i] / R0[i], Rpbe[i], Rpbe[i] / R0[i], Rlo[i] / R0[i], Rhi[i] / R0[i]))
gL = 1e-2 * A.WL
print("5 gamma_L window: %.2f to %.2f meV" % ((A.WL - 5 * gL) * 1e3, (A.WL + 5 * gL) * 1e3))

fig, ax = plt.subplots(figsize=(4.6, 3.0))
ax.axvspan((A.WL - 5 * gL) * 1e3, (A.WL + 5 * gL) * 1e3, color="0.88", lw=0)
ax.semilogy(m * 1e3, R0, color="k", lw=1.2, label=r"residue, $Z - Z^*/\varepsilon_\infty$")
ax.semilogy(m * 1e3, Rpbe, color="k", lw=1.0, ls=":", label=r"residue, PBE $Z^*$, $\varepsilon_\infty$")
ax.set_xlabel(r"$m_\phi$ [meV]")
ax.set_ylabel(r"events / (kg yr $g_{\phi ee}^2$)")
ax.set_ylim(1e22, 1e29)
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
fig.tight_layout()
fig.savefig("../../tex/figures/ch11/limit11_8a.pdf")
print("wrote limit11_8a.pdf")
