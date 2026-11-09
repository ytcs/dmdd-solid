"""Fig. 2.1: (a) the first-order transition function sin^2(xi t/2)/xi^2 narrowing with t (Sect. 2.1, Eq. (2.1-Pstatic));
(b) Worked example 2.1: a harmonic perturbation resonant with the center of a flat continuum.
Output: tex/figures/ch02/fig2_1.pdf. Natural units, energies in eV, times in eV^-1 (1 eV^-1 = 6.582e-16 s, hbar).

No external data. Every number is a model choice of the worked example, stated here and in the caption:
  E_W  = 1 eV          width of the flat continuum, final-state energies uniform in [-E_W/2, +E_W/2] about resonance
  DOS  = 2000 / eV     density of final states (level spacing 0.5 meV), N_f = E_W * DOS = 2000 levels
  GAM  = 0.01 eV       golden-rule rate 2 pi |O_fi|^2 DOS, which fixes |O_fi| (the same for every final state)
Model of the "exact" curve: rotating-wave model (counter-rotating term dropped), i.e. in the frame rotating with the
drive the initial state has energy 0 and final state f has energy xi_f = E_f - E_i - omega, coupled by O_fi; the
Schroedinger equation is solved by exact diagonalization of this (N_f + 1)-level Hamiltonian.
First-order probability (Sect. 2.1, WE 2.1): P1(t) = 4 |O|^2 DOS t [Si(E_W t/2) - sin^2(E_W t/4)/(E_W t/4)];
long-time form GAM (t - 4/(pi E_W)); short-time form |O|^2 N_f t^2.
hbar = 6.582119569e-16 eV s (CODATA, exact SI definition of h and e).
"""
import os
import numpy as np
from scipy.special import sici
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HBAR = 6.582119569e-16      # eV s
E_W, DOS, GAM = 1.0, 2000.0, 0.01
NF = int(round(E_W * DOS))
O2 = GAM / (2 * np.pi * DOS)   # |O_fi|^2 in eV^2


def g(xi, t):
    """sin^2(xi t/2)/xi^2, with its xi -> 0 value t^2/4."""
    xi = np.asarray(xi, dtype=float)
    out = np.full_like(xi, t**2 / 4)
    nz = np.abs(xi) > 1e-12
    out[nz] = np.sin(xi[nz] * t / 2)**2 / xi[nz]**2
    return out


# --- checks quoted in the text ---------------------------------------------------------------
# integral over xi equals pi t / 2
for t in [1.0, 5.0]:
    val = quad(lambda x: float(g(np.array([x]), t)[0]), -2000 / t, 2000 / t, limit=4000)[0]
    print(f"t={t}: int g dxi / (pi t/2) = {val / (np.pi * t / 2):.4f} (cutoff at |xi| = 2000/t)")
central = 2 * sici(2 * np.pi)[0] / np.pi    # weight in the central lobe |xi| < 2 pi/t: (1/pi) int_{-pi}^{pi} sin^2u/u^2 du
print(f"weight of the central lobe = {central:.4f}")


def P1(t):
    s = sici(E_W * t / 2)[0]
    return 4 * O2 * DOS * t * (s - np.sin(E_W * t / 4)**2 / (E_W * t / 4))


# discrete first-order sum over the actual levels (offset by half a spacing so no level sits exactly at resonance)
xi_f = (np.arange(NF) + 0.5) / DOS - E_W / 2


def P1_discrete(t):
    return 4 * O2 * np.sum(np.sin(xi_f * t / 2)**2 / xi_f**2)


# exact solution of the rotating-wave model
H = np.zeros((NF + 1, NF + 1))
H[0, 1:] = H[1:, 0] = np.sqrt(O2)
H[np.arange(1, NF + 1), np.arange(1, NF + 1)] = xi_f
ev, U = np.linalg.eigh(H)


def P_exact(t):
    ci = np.sum(np.abs(U[0, :])**2 * np.exp(-1j * ev * t))
    return 1 - abs(ci)**2


print(f"|O_fi| = {np.sqrt(O2) * 1e3:.4f} meV; N_f = {NF}; 1/E_W = {HBAR / E_W * 1e15:.3f} fs; "
      f"1/Gamma = {1 / GAM:.0f} eV^-1 = {HBAR / GAM * 1e15:.1f} fs; Heisenberg time 2 pi DOS = {2 * np.pi * DOS:.0f} eV^-1 "
      f"= {2 * np.pi * DOS * HBAR * 1e12:.2f} ps")
print(f"offset 4/(pi E_W) = {4 / (np.pi * E_W):.4f} eV^-1 = {4 / (np.pi * E_W) * HBAR * 1e15:.3f} fs")
for t in [0.1, 1.0, 10.0, 20.0, 50.0, 100.0, 200.0]:
    print(f"t={t:6.1f}: P1={P1(t):.4e}  P1_disc={P1_discrete(t):.4e}  Gam(t-4/piEw)={GAM * (t - 4 / (np.pi * E_W)):.4e}"
          f"  O2 NF t^2={O2 * NF * t**2:.4e}  exact={P_exact(t):.4e}  1-exp(-Gam t)={1 - np.exp(-GAM * t):.4e}")
# time at which first order exceeds the exact depletion by 10 per cent
ts = np.linspace(1, 300, 3000)
r = np.array([P1(t) / P_exact(t) for t in ts])
t10 = ts[np.argmax(r > 1.1)]
print(f"first order exceeds exact by 10% at t = {t10:.1f} eV^-1, Gamma t = {GAM * t10:.3f}")
# ratio exact / (1 - exp(-Gam t)) over the plotted range beyond the transient
rr = [P_exact(t) / (1 - np.exp(-GAM * t)) for t in np.linspace(100, 500, 81)]
print(f"exact/(1-exp(-Gam t)) for 100<=t<=500 (t >= 1/Gamma): min {min(rr):.4f}, max {max(rr):.4f}")

# --- figure ----------------------------------------------------------------------------------
fig, (axa, axb) = plt.subplots(1, 2, figsize=(7.0, 3.0))
xi = np.linspace(-12, 12, 4001)
for t, ls, c in [(1.0, "-.", "C0"), (2.0, "--", "C3"), (4.0, "-", "k")]:
    axa.plot(xi, g(xi, t), ls=ls, color=c, lw=1.1, label=fr"${t:g}$")
axa.set_xlim(-12, 12)
axa.set_ylim(0, 4.3)
axa.set_xlabel(r"$\xi$ [units of $1/t_1$]")
axa.set_ylabel(r"$\sin^2(\xi t/2)/\xi^2$ [units of $t_1^2$]")
axa.legend(fontsize=7, frameon=False, title=r"$t/t_1$", title_fontsize=7)
axa.text(0.03, 0.95, "(a)", transform=axa.transAxes, fontsize=8, va="top")

tt = np.logspace(-2, np.log10(500), 400)
axb.loglog(tt, [P_exact(t) for t in tt], color="k", lw=1.4, label="exact (rotating-wave model)")
axb.loglog(tt, P1(tt), color="C3", lw=1.0, ls="--", label="first order")
tl = tt[tt > 4 / (np.pi * E_W) * 1.05]
axb.loglog(tl, GAM * (tl - 4 / (np.pi * E_W)), color="C0", lw=0.9, ls="-.", label=r"$\mathit{Γ}\,[t - 4/(\pi E_{\mathrm{w}})]$")  # italic Γ (rate); mathtext lacks \varGamma
ts_ = tt[tt < 3]
axb.loglog(ts_, O2 * NF * ts_**2, color="0.5", lw=0.9, ls=":", label=r"$N_f|O_{fi}|^2t^2$")
axb.axvline(1 / E_W, color="0.6", lw=0.6)
axb.text(1 / E_W * 1.15, 2e-7, r"$1/E_{\mathrm{w}}$", fontsize=7, color="0.3")
axb.axvline(1 / GAM, color="0.6", lw=0.6)
axb.text(1 / GAM * 1.15, 2e-7, r"$1/\mathit{Γ}$", fontsize=7, color="0.3")
axb.set_xlim(1e-2, 500)
axb.set_ylim(1e-7, 3)
axb.set_xlabel(r"$t$ [eV$^{-1}$]")
axb.set_ylabel(r"$1 - |c_i(t)|^2$")
axb.legend(fontsize=6.5, frameon=False, loc="upper left", bbox_to_anchor=(0.0, 0.92))
axb.text(0.03, 0.95, "(b)", transform=axb.transAxes, fontsize=8, va="top")
fig.tight_layout()

out = os.path.join(os.path.dirname(__file__), "..", "..", "tex", "figures", "ch02", "fig2_1.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
