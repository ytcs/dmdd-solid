"""Fig. 10.2 of Sect. 10.2: electron-recoil rates of silicon in three approximations (IP, RPA, RPA + LF), and every rate
ratio and pointwise screening number quoted in Sect. 10.2 (subsection on screening and local-field corrections).

Output: tex/figures/ch10/fig10_2.pdf
  (a) dR/domega at m_chi = 10 MeV, heavy mediator, sigma_e = 1e-37 cm^2: independent particles (IP), RPA without and
      with local fields (LF).
  (b) ratio of the rate above the gap, IP / (RPA + LF) and RPA / (RPA + LF), against m_chi, heavy and light mediator.
Inputs: rate10_2.py (constants, halo, rate integral) and si_elf_binned.npz (si_elf_reduce.py: the GPAW tables of
  Knapen, Kozaczuk and Lin, arXiv:2101.08275).  Modelling choices, also stated in the caption: the tabulated functions
  are averaged over directions in 100 eV bins of |q|; the rate is cut at the table's |q| <= 22.5 keV and omega <= 89 eV
  (kinematics, omega <= q v_max, keeps omega below 60 eV for q inside the table); threshold E_g = 1.11 eV.
Static model check (Cappellini, Del Sole, Reining, Bechstedt, Phys. Rev. B 47, 9892 (1993), with alpha_C = 1.563 and
  the book's silicon values eps_inf = 11.7 (Sect. 4.4), k_TF = 4.12 keV (Worked example 4.8), omega_p = 16.6 eV):
  eps(q) = 1 + 1/[1/(eps_inf - 1) + alpha_C (q/k_TF)^2 + q^4/(4 m_e^2 omega_p^2)]; printed for comparison only.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rate10_2 as R

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tex", "figures", "ch10")
d = R.load()
q, om = d["q"], d["omega"]

# --- pointwise static screening factors (RPA + LF table, omega = 0 row) ------------------------------------------
print("Static screening factor 1/eps(q,0)^2 from the tables, and the Cappellini model:")
for qq in (1000.0, 2000.0, R.Q0, 5000.0, 8000.0):
    j = np.argmin(abs(q - qq))
    eps_lf = 1 / (1 - d["step_lf"][j])
    eps_rpa = 1 / (1 - d["step_rpa"][j])
    x = qq
    eps_c = 1 + 1 / (1 / (11.7 - 1) + 1.563 * (x / 4120.0)**2 + x**4 / (4 * R.ME**2 * 16.6**2))
    print("  q = %6.0f eV (bin %6.0f): eps_LF = %.2f (1/eps^2 = %.3f), eps_RPA = %.2f (%.3f); model %.2f (%.3f)"
          % (qq, q[j], eps_lf, eps_lf**-2, eps_rpa, eps_rpa**-2, eps_c, eps_c**-2))
print("  optical limit of the tables: eps(0,0) noLF = %.2f, LF = %.2f" % (d["eps_opt_noLF"], d["eps_opt_LF"]))

# --- pointwise dynamic ratios at q0 -----------------------------------------------------------------------------
j0 = np.argmin(abs(q - R.Q0))
for w in (3.0, 5.0, 10.0):
    i = np.argmin(abs(om - w))
    print("  at q = %.0f eV, omega = %.1f eV: eps2_IP = %.3f, L_RPA = %.4f, L_LF = %.4f, eps2_IP/L_LF = %.1f"
          % (q[j0], om[i], d["ip"][i, j0], d["rpa"][i, j0], d["lf"][i, j0], d["ip"][i, j0] / d["lf"][i, j0]))

# --- integrated ratios ---------------------------------------------------------------------------------------------
masses = np.logspace(np.log10(0.5e6), 9, 22)
ratios = {}
for light in (False, True):
    r_ip, r_rpa, r_e2 = [], [], []
    for m in masses:
        t = {k: R.total(m, k, d, light) for k in ("ip", "rpa", "lf", "e2lf")}
        r_ip.append(t["ip"] / t["lf"])
        r_rpa.append(t["rpa"] / t["lf"])
        r_e2.append(t["e2lf"] / t["lf"])
    ratios[light] = (np.array(r_ip), np.array(r_rpa), np.array(r_e2))
print("Rate ratios above the gap (IP/LF, RPA/LF, eps2_LF/L_LF):")
for m in (1e6, 3e6, 10e6, 100e6, 1e9):
    for light in (False, True):
        t = {k: R.total(m, k, d, light) for k in ("ip", "rpa", "lf", "e2lf")}
        print("  m = %7.1f MeV %-5s: R_LF = %.3e /kg/yr; IP/LF = %.2f, RPA/LF = %.2f, eps2_LF/L_LF = %.2f"
              % (m / 1e6, "light" if light else "heavy", t["lf"], t["ip"] / t["lf"], t["rpa"] / t["lf"],
                 t["e2lf"] / t["lf"]))

# where the heavy-mediator rate at 10 MeV lives in q, and the local-field share there
m = 10e6
w = np.arange(R.EG, om[-1], 0.05)
dq = {}
for k in ("ip", "rpa", "lf"):
    rf = np.array([np.interp(w, om, d[k][:, j]) for j in range(len(q))]).T
    W, Q = np.meshgrid(w, q, indexing="ij")
    dq[k] = np.trapezoid(Q**3 * R.eta(W / Q + Q / (2 * m)) * rf, w, axis=0)
cum = np.cumsum(dq["lf"]) / dq["lf"].sum()
q50 = np.interp(0.5, cum, q)
print("10 MeV heavy: median q of the RPA+LF rate = %.1f keV; fraction above 2 q0 = %.2f; above 15 keV = %.3f"
      % (q50 / 1e3, 1 - np.interp(2 * R.Q0, q, cum), 1 - np.interp(15e3, q, cum)))
for qq in (2000.0, R.Q0, 8000.0, 10000.0):
    j = np.argmin(abs(q - qq))
    print("  q = %5.0f: per-q ratios IP/RPA = %.2f, RPA/LF = %.2f, 1/eps(q,0)^2 (LF) = %.2f"
          % (q[j], dq["ip"][j] / dq["rpa"][j], dq["rpa"][j] / dq["lf"][j], (1 - d["step_lf"][j])**2))
# mean energy of the spectra (weight moves up)
for k in ("ip", "lf"):
    ww, s = R.spectrum(10e6, k, d)
    print("  10 MeV heavy, %s: mean omega = %.1f eV" % (k, np.trapezoid(ww * s, ww) / np.trapezoid(s, ww)))

# --- figure --------------------------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.3, 2.8))
styles = {"ip": ("k", ":", "IP"), "rpa": ("C0", "--", "RPA"), "lf": ("C3", "-", "RPA + LF")}
for k in ("ip", "rpa", "lf"):
    ww, s = R.spectrum(10e6, k, d)
    c, ls, lab = styles[k]
    ax1.plot(ww, s / 1e3, color=c, ls=ls, lw=1.3, label=lab)
ax1.set_xlim(0, 30)
ax1.set_ylim(0, None)
ax1.set_xlabel(r"$\omega$ [eV]")
ax1.set_ylabel(r"$\mathrm{d}\mathcal{R}/\mathrm{d}\omega$ [$10^3$ kg$^{-1}$ yr$^{-1}$ eV$^{-1}$]")
ax1.legend(frameon=False, fontsize=8)
ax1.text(0.97, 0.62, r"$m_\chi = 10$ MeV" + "\nheavy mediator", transform=ax1.transAxes, ha="right", fontsize=8)
ax1.text(0.02, 0.93, "(a)", transform=ax1.transAxes)

mm = masses / 1e6
for light, ls in ((False, "-"), (True, "--")):
    r_ip, r_rpa, _ = ratios[light]
    tag = "light" if light else "heavy"
    ax2.semilogx(mm, r_ip, color="k", ls=ls, lw=1.3, label="IP / (RPA + LF), " + tag)
    ax2.semilogx(mm, r_rpa, color="C0", ls=ls, lw=1.3, label="RPA / (RPA + LF), " + tag)
ax2.axhline(1, color="0.6", lw=0.6)
ax2.set_yscale("log")
ax2.set_ylim(0.9, 30)
ax2.set_xlim(0.5, 1000)
ax2.set_xlabel(r"$m_\chi$ [MeV]")
ax2.set_ylabel("rate ratio above the gap")
ax2.legend(frameon=False, fontsize=7, loc="upper right")
ax2.text(0.02, 0.93, "(b)", transform=ax2.transAxes)
fig.tight_layout()
os.makedirs(OUT, exist_ok=True)
fig.savefig(os.path.join(OUT, "fig10_2.pdf"))
print("written", os.path.join(OUT, "fig10_2.pdf"))
