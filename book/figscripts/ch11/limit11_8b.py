"""Limit 11.8b (fig:11-limit-8b): absorbed power of a bulk acoustic resonator mode in the halo field.

Source formula (Trickle, arXiv:2501.05504, Eqs. (7)-(8)): on resonance P is proportional to the signal quality factor
Q_s = min{Q_p, Q_DM}. Fuller result (Sect. 11.8, eq:11.8-Phalo): the mean absorbed power of a mode of width gamma_n = omega_n/Q_p
in the field whose energies are distributed as F_phi(omega),
    P/P_1 = omega_n int d omega F_phi(omega) omega omega_n gamma_n / [(omega^2 - omega_n^2)^2 + omega_n^2 gamma_n^2]   (= Q_eff),
normalized so that a monochromatic field on resonance gives Q_eff = Q_p; the mode is tuned to the omega_n that maximizes it.
Near resonance the kernel is gamma/(4 (omega - omega_n)^2 + gamma^2) (relative error O(omega - 1) < 4e-6), used below.
F_phi(omega) d omega = f_sp(v) dv with omega = m_phi(1 + v^2/2): F_phi = f_sp(v)/(m_phi v) = |eta'(v)|/m_phi, from the book's
truncated Maxwellian (phon11.eta_kms, Baxter et al. Table 1). Effective field quality factor Q_DM = (pi/2) m_phi F_phi(omega_n)
at its maximum, 1.34e6 (abs11_8.py). Horizontal axis Q_p/Q_DM; vertical axis Q_eff/Q_DM.
Gray: Q_p/Q_DM > 7.9 and < 0.2, where min{Q_p, Q_DM} is within 10 % of Q_eff (printed below).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve
import abs11_8 as A
import phon11 as P

v_kms, g = A.fsp_over_v_kms()                 # g = f_sp/v in (km/s)^-2
Fx_v = g * P.C_KMS**2                          # F in units of 1/m_phi, as a function of v
xv = 0.5 * (v_kms / P.C_KMS)**2                # (omega - m)/m
N = 2**19
x = np.linspace(0.0, xv.max() * 1.02, N)
dx = x[1] - x[0]
F = np.interp(x, xv, Fx_v, left=0.0, right=0.0)
print("norm int F dx = %.5f" % (np.sum(F) * dx))
QDM = np.pi / 2 * F.max()
print("Q_DM (pi/2 max F) = %.4e at v = %.1f km/s" % (QDM, P.C_KMS * np.sqrt(2 * x[np.argmax(F)])))

ratios = np.logspace(-3, 3, 61)
Qeff = []
kx = np.arange(-N + 1, N) * dx
for r in ratios:
    gam = 1.0 / (r * QDM)
    if gam < 20 * dx:
        # narrow line: the Lorentzian integrates to (pi/2) F(omega_n) up to O((gamma/width)^2)
        conv = np.pi / 2 * F
    else:
        K = gam / (4 * kx**2 + gam**2)
        conv = fftconvolve(F, K, mode="same") * dx
        # 'same' on a kernel of length 2N-1 centred at index N-1 aligns conv[i] with x[i]
    Qeff.append(conv.max())
Qeff = np.array(Qeff)
src = np.minimum(ratios, 1.0)
for r, q in zip(ratios, Qeff / QDM):
    if np.isclose(np.log10(r), np.round(np.log10(r))):
        print("Q_p/Q_DM = %8.3g: Q_eff/Q_DM = %.4f; min{} = %.4f" % (r, q, min(r, 1)))
rel = Qeff / QDM / src
ok = ratios[np.abs(rel - 1) < 0.10]
print("min{} within 10 %% for Q_p/Q_DM <= %.3g and >= %.3g" % (ok[ok < 1].max() if (ok < 1).any() else np.nan, ok[ok > 1].min()))
i1 = np.argmin(np.abs(ratios - 1))
print("at Q_p = Q_DM: Q_eff/Q_DM = %.3f (min{} = 1)" % (Qeff[i1] / QDM))

fig, ax = plt.subplots(figsize=(4.6, 3.0))
ax.axvspan(7.94, 1e3, color="0.88", lw=0)
ax.axvspan(1e-3, 0.2, color="0.88", lw=0)
ax.loglog(ratios, Qeff / QDM, color="k", lw=1.2, label="halo-averaged mode")
ax.loglog(ratios, src, color="k", lw=1.0, ls="--", label=r"$\min\{\mathfrak{Q}_{\mathrm{p}}, \mathfrak{Q}_{\mathrm{DM}}\}$")
ax.set_xlabel(r"$\mathfrak{Q}_{\mathrm{p}}/\mathfrak{Q}_{\mathrm{DM}}$")
ax.set_ylabel(r"$\mathfrak{Q}_{\mathrm{eff}}/\mathfrak{Q}_{\mathrm{DM}}$")
ax.set_xlim(1e-3, 1e3)
ax.set_ylim(1e-3, 3)
ax.legend(frameon=False, fontsize=8, loc="lower right")
fig.tight_layout()
fig.savefig("../../tex/figures/ch11/limit11_8b.pdf")
print("wrote limit11_8b.pdf")
