"""Fig. 2.3: Helm nuclear form factors F_Helm(q)^2 of silicon and germanium (Sect. 2.2, WE 2.4).
Output: tex/figures/ch02/fig2_3.pdf.

Helm form: F_Helm(q) = 3 j1(q R_nuc)/(q R_nuc) * exp(-q^2 s_skin^2 / 2)   [Helm, Phys. Rev. 104, 1466 (1956);
  as written in Duda, Kemper, Gondolo, hep-ph/0608035, Eq. (17) (Eq. (9) for its square)].
Parameters of Lewin and Smith (Astropart. Phys. 6, 87 (1996)), quoted in Duda et al. Eqs. (11), (12):
  R_nuc^2 = c_nuc^2 + (7/3) pi^2 a_nuc^2 - 5 s_skin^2,  c_nuc = 1.23 A^(1/3) - 0.60 fm,  a_nuc = 0.52 fm,  s_skin = 0.9 fm.
Modelling choice (stated in caption): the Lewin-Smith Helm parameterization; Duda et al. find it within a few percent of
form factors fitted to electron-scattering data at small q (their Sect. on 28Si and 70Ge).
Targets: Si A = 28 (28Si, 92% of natural Si); Ge A = 73 (nearest integer to natural Ge's mean mass number; standard
atomic weight 72.630, CIAAW).
Kinematics: q_max = 2 mu_chiN v_max, v_max = 2.650e-3 (794.5 km/s, Sect. 1.2, eq:1.2-vmax).
Masses: natural Si 28.0855 u = 26.16 GeV (Sect. 1.4); Ge-73 nucleus 72.923 u * 0.931494 GeV = 67.93 GeV (AME atomic mass; electrons ignored).
hbar c = 197.327 MeV fm.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HBARC = 197.327  # MeV fm
VMAX = 2.650e-3
A_NUC, S_SKIN = 0.52, 0.9
M_SI, M_GE = 28.0855 * 931.494, 72.923 * 931.494  # MeV


def rnuc(A):
    c = 1.23 * A**(1 / 3) - 0.60
    return np.sqrt(c**2 + 7 / 3 * np.pi**2 * A_NUC**2 - 5 * S_SKIN**2), c


def helm(q, A):
    R, _ = rnuc(A)
    q = np.asarray(q, dtype=float)
    x = q * R / HBARC
    out = np.ones_like(x)
    m = x > 1e-3
    out[m] = 3 * (np.sin(x[m]) - x[m] * np.cos(x[m])) / x[m]**3
    out[~m] = 1 - x[~m]**2 / 10
    return out * np.exp(-(q * S_SKIN / HBARC)**2 / 2)


def qmax(mchi, M):
    mu = mchi * M / (mchi + M)
    return 2 * mu * VMAX, mu


for name, A, M in (("Si", 28, M_SI), ("Ge", 73, M_GE)):
    R, c = rnuc(A)
    print(f"{name}: c_nuc = {c:.3f} fm, R_nuc = {R:.3f} fm, hbar c/R = {HBARC / R:.1f} MeV,"
          f" first zero q = {4.4934 * HBARC / R:.0f} MeV")
    for mchi in (1e3, 1e4, 1e5):
        qm, mu = qmax(mchi, M)
        F = helm(np.array([qm]), A)[0]
        print(f"   m_chi = {mchi / 1e3:g} GeV: mu = {mu:.1f} MeV, q_max = {qm:.2f} MeV, q R = {qm * R / HBARC:.3f},"
              f" F^2(q_max) = {F**2:.4f}")

# WE 2.4 numbers for Si: A^2 and reduced-mass factors (Sect. 1.4 values)
MP = 938.272
for mchi in (100.0, 1000.0):
    mup = mchi * MP / (mchi + MP)
    muN = mchi * M_SI / (mchi + M_SI)
    print(f"Si, m_chi={mchi:g} MeV: mu_p={mup:.1f}, mu_N={muN:.1f}, ratio^2={(muN / mup)**2:.3f},"
          f" sigma_N/sigma_p={(muN / mup)**2 * 784:.0f}")

q = np.logspace(0, 3, 800)
plt.rcParams.update({"font.size": 9})
fig, ax = plt.subplots(figsize=(4.6, 3.1))
ax.plot(q, helm(q, 28)**2, "k-", label=r"Si ($A = 28$)")
ax.plot(q, helm(q, 73)**2, "C3--", label=r"Ge ($A = 73$)")
for mchi, lab in ((1e3, "1 GeV"), (1e4, "10 GeV"), (1e5, "100 GeV")):
    qm, _ = qmax(mchi, M_SI)
    ax.axvline(qm, color="0.6", lw=0.8, ls=":")
    ax.text(qm * 1.06, 2e-5, lab, rotation=90, color="0.35", fontsize=7, va="bottom")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1, 1e3)
ax.set_ylim(1e-6, 2)
ax.set_xlabel(r"$q$ [MeV]")
ax.set_ylabel(r"$F_{\mathrm{Helm}}(q)^2$")
ax.legend(frameon=False, loc="lower left")
fig.tight_layout()
out = os.path.join(os.path.dirname(__file__), "..", "..", "tex", "figures", "ch02", "fig2_3.pdf")
fig.savefig(out)
print("wrote", os.path.abspath(out))
