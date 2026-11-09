"""Limit 10.2b (sum-rule bounds on the loss function) of Sect. 10.2: comparison plot and the numbers quoted with it.

Output: tex/figures/ch10/limit10_2b.pdf.  Silicon, m_chi = 1 MeV, heavy mediator, sigma_e = 1e-37 cm^2, threshold
omega_th = 1 meV (a calorimetric threshold inside the phonon band), rate per unit ln q against q:
  * computed electronic rate, RPA + LF (si_elf_binned.npz);
  * acoustic peak of an electron-only coupling (model of rate10_2.phonon_dRdq; choices listed in limit10_2a.py);
  * clamped bounds (eq:10.2-bound): n = -1 with the static step 1 - 1/eps(q,0) of the RPA + LF table, n = +1 with
    omega_p = 31.1 eV (all electrons; Sect. 4.3);
  * relaxed bound for the electron-only coupling: n = -1 with the step plus the lattice term (eq:10.2-relaxed)
    G(q) -> Omega_Pe^2/(c_LA q)^2, Omega_Pe = 0.513 eV, c_LA = 8.43 km/s; the q -> 0 form is used at all q shown,
    which the caption states (it is derived only asymptotically; App. E.16 specifies the finite-q calculation).
Below the first momentum of the table (0.49 keV) the clamped step is held at its value there.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rate10_2 as R

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tex", "figures", "ch10")
d = R.load()
m = 1e6
wth = 1e-3
conv = R.to_per_kg_yr(1.0)
C = R.coeff(m)
q = np.geomspace(150.0, 2 * m * R.VMAX * 0.999, 400)
step = np.interp(q, d["q"], d["step_lf"])
G = (R.OMEGA_PE / (R.C_LA * q))**2

b_m1 = conv * C * q**4 * R.eta_max(q, m, -1, wth) * np.pi / 2 * step          # per ln q: extra factor q
b_p1 = conv * C * q**4 * R.eta_max(q, m, 1, wth) * np.pi / 2 * R.WP_ALL**2
b_rel = conv * C * q**4 * R.eta_max(q, m, -1, wth) * np.pi / 2 * (step + G)
ph = conv * q * R.phonon_dRdq(q, m)

# electronic per-q rate from the table (threshold E_g; omega <= q v_max - q^2/2m)
om, qt = d["omega"], d["q"]
w = np.arange(R.EG, 6.0, 0.02)
rf = np.array([np.interp(w, om, d["lf"][:, j]) for j in range(len(qt))]).T
W, Q = np.meshgrid(w, qt, indexing="ij")
el_t = conv * C * qt**4 * np.trapezoid(R.eta(W / Q + Q / (2 * m)) * rf, w, axis=0)
el_t = np.where(qt <= 2 * m * R.VMAX, el_t, 0.0)

for qq in (500.0, 1000.0, 2000.0, 3000.0):
    i = np.argmin(abs(q - qq))
    print("q = %5.0f eV: step %.2f, lattice term %.0f; phonon / clamped n=-1 bound = %.1f; relaxed bound / phonon = %.1f"
          % (q[i], step[i], G[i], ph[i] / b_m1[i], b_rel[i] / ph[i] if ph[i] > 0 else np.nan))
# where the electron-only rate (phonon + electronic) drops below the clamped n = -1 bound
el_on_q = np.interp(q, qt, el_t, left=0.0)
tot = ph + el_on_q
viol = tot > b_m1
qc = q[viol].max() if viol.any() else None
print("electron-only rate exceeds the clamped n=-1 bound for q < %.2f keV (the acoustic model ends at %.2f keV)"
      % (qc / 1e3, R.Q_X / 1e3))
print("lattice term (q -> 0 form) equals 1 at %.1f keV; at 1 keV it is %.0f" % (R.OMEGA_PE / R.C_LA / 1e3, (R.OMEGA_PE / (R.C_LA * 1e3))**2))
print("pairs open above q_min = E_g / v_max = %.2f keV" % (R.EG / R.VMAX / 1e3))
assert (b_rel >= ph - 1e-12).all()
assert (b_m1 >= el_on_q).all()

plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 3.0))
ax.axvspan(R.EG / R.VMAX / 1e3, q[-1] / 1e3, color="0.92", lw=0)   # electron-hole pairs kinematically open
ax.loglog(q / 1e3, b_p1, color="C0", ls=":", lw=1.2, label=r"bound $n = +1$ ($f$-sum)")
ax.loglog(q / 1e3, b_rel, color="k", ls="-.", lw=1.1, label=r"bound $n = -1$, lattice free")
ax.loglog(q / 1e3, b_m1, color="C0", ls="--", lw=1.3, label=r"bound $n = -1$, clamped")
ax.loglog(q / 1e3, np.where(ph > 0, ph, np.nan), color="k", lw=1.3, label="acoustic peak, electron-only")
ax.loglog(qt[el_t > 0] / 1e3, el_t[el_t > 0], color="C3", lw=1.6, label="computed, RPA + LF")
ax.set_xlim(0.15, 5.3)
ax.set_xticks([0.2, 0.5, 1, 2, 5])
ax.set_xticklabels(["0.2", "0.5", "1", "2", "5"])
ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.set_ylim(1e-6, 1e11)
ax.set_xlabel(r"$q$ [keV]")
ax.set_ylabel(r"$\mathrm{d}\mathcal{R}/\mathrm{d}\ln q$ [kg$^{-1}$ yr$^{-1}$]")
ax.legend(frameon=False, fontsize=6.5, loc="lower center", ncol=2)
fig.tight_layout()
os.makedirs(OUT, exist_ok=True)
fig.savefig(os.path.join(OUT, "limit10_2b.pdf"))
print("written limit10_2b.pdf")
