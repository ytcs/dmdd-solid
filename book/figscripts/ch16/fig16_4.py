"""Fig. 16.4 (fig:16-anthracene): the Frenkel-exciton rate of an anthracene crystal by the direction of the dark-matter wind,
in the binned (incoherent) form of eq:16.4-rate with the pi-electron model of frenkel16_4.py.

Rate: events per kg-year at sigma_e = 1e-37 cm^2 for the Earth's velocity vhat_E along a, b and c' (crystal axes; the wind
arrives from -vhat_E, and the rate is even in vhat_E since the crystal is centrosymmetric), and its average over directions.
Plot: (a) the direction-averaged rate, heavy (F_DM = 1, solid) and light (F_DM = (alpha m_e/q)^2, dashed) mediator;
(b) the rate for vhat_E along a, b, c' divided by the average, heavy (solid) and light (dashed).  Singlets with E_x <= 7.5 eV (20 states per
molecule); the ionization continuum above the crystal gap (3.9-4.2 eV, arXiv:1604.00041 Table II) is not included.
Quadrature: q log-spaced 0.5-60 keV (70 values), 1500 Fibonacci directions of q.  Also printed: rates along the molecular
axes of molecule 1, the largest and smallest rate over 300 wind directions at selected masses (the largest daily amplitude
any mounting could show, (R_max - R_min)/(R_max + R_min)), the share of the lowest singlet in the rate, the isotropic rate
against the isotropic formula (eta form), and a quadrature check.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import frenkel16_4 as F  # noqa: E402

FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch16")
states = [s for s in range(len(F.E_X)) if F.E_X[s] <= 7.5]
print(f"{len(states)} singlets with E_x <= 7.5 eV; energies {np.round(F.E_X[states], 3)}")
qk = np.geomspace(0.5, 60.0, 70)
dirs = F.fib_sphere(1500)
ff2 = F.ff2_table(qk, dirs, states)
axes = {"a": np.array([1.0, 0, 0]), "b": np.array([0, 1.0, 0]), "c'": np.array([0, 0, 1.0])}
vh = np.array(list(axes.values()))
masses = np.geomspace(0.9e6, 1e9, 36)


def iso_rate(m, light=False, sub=None):
    """Isotropic rate from the eta form: rho sigma/(2 m mu^2 M_cell) int q dq eta F^2 <sum |f|^2> (events/kg/yr)."""
    mu = m * F.ME / (m + F.ME)
    q = qk * 1e3
    w = np.gradient(np.log(q))
    w[0] *= 0.5
    w[-1] *= 0.5
    FDM2 = (F.ALPHA * F.ME / q) ** 4 if light else np.ones_like(q)
    tot = 0.0
    for si, s in enumerate(states):
        if sub is not None and s not in sub:
            continue
        vmin = (F.E_X[s] / q + q / (2 * m)) * F.C_KMS
        eta = F.eta(vmin) * F.C_KMS
        tot += (q**2 * w * FDM2 * eta * ff2[si].mean(-1)).sum()
    sig = 1e-37 / F.CM_PER_INVEV**2
    pref = F.RHO_CHI * F.CM_PER_INVEV**3 * sig / (2 * m * mu**2 * F.M_CELL_EV)
    return pref * tot * F.KG_EV / 6.582119569e-16 * F.YR


rows = {}
for light in (False, True):
    R = np.array([F.rate(m, vh, qk, dirs, ff2, states, light=light) for m in masses])
    Riso = np.array([iso_rate(m, light) for m in masses])
    rows[light] = (R, Riso)
    lab = "light" if light else "heavy"
    print(f"\n[{lab} mediator] events/kg/yr at sigma_e = 1e-37 cm^2")
    for m, r, ri in zip(masses, R, Riso):
        print(f"  m = {m/1e6:8.3f} MeV: along a {r[0]:.3e}, b {r[1]:.3e}, c' {r[2]:.3e}; average {ri:.3e};"
              f" max/min over the three axes {r.max()/r.min():.2f}")

# the isotropic average from the direction-resolved form, as a check of eq:16.4-rate against the eta form
dir_avg = F.fib_sphere(200)
for m in (2e6, 100e6):
    ra = F.rate(m, dir_avg, qk, dirs, ff2, states).mean()
    print(f"check at {m/1e6:.0f} MeV: mean over 200 wind directions {ra:.4e} vs isotropic (eta) form {iso_rate(m):.4e}")

# lowest-singlet share and molecular axes
L, M, N = F.AX1
for m in (1.0e6, 2e6, 10e6, 100e6, 1e9):
    r_all = iso_rate(m)
    r_la = iso_rate(m, sub=[0])
    r_ax = F.rate(m, np.array([L, M, N]), qk, dirs, ff2, states)
    print(f"m = {m/1e6:7.1f} MeV: share of L_a in the isotropic rate {r_la/r_all:.3f};"
          f" wind along L1, M1, N1: {np.round(r_ax/r_all, 3)} of the average")

# scan of wind directions
scan = F.fib_sphere(300)
dirs_s = F.fib_sphere(800)
ff2_s = F.ff2_table(qk, dirs_s, states)
print("\nscan over 300 wind directions (800 q directions):")
for light in (False, True):
    for m in (1.0e6, 1.5e6, 3e6, 10e6, 100e6, 1e9):
        r = F.rate(m, scan, qk, dirs_s, ff2_s, states, light=light)
        imax, imin = np.argmax(r), np.argmin(r)
        ang = lambda u, v: np.degrees(np.arccos(min(1, abs(u @ v))))   # noqa: E731
        print(f"  {'light' if light else 'heavy'} {m/1e6:7.1f} MeV: R_max/R_min = {r.max()/r.min():.2f},"
              f" (R_max - R_min)/(R_max + R_min) = {(r.max()-r.min())/(r.max()+r.min()):.3f};"
              f" R_max at {ang(scan[imax], np.array([0,1.,0])):.0f} deg from b, R_min at {ang(scan[imin], np.array([0,1.,0])):.0f} deg from b,"
              f" {ang(scan[imin], np.array([0,0,1.])):.0f} deg from c'")
# quadrature check
for m in (2e6, 100e6):
    a = F.rate(m, vh, qk, dirs_s, ff2_s, states)
    b = rows[False][0][np.argmin(np.abs(masses - m))]
    print(f"quadrature check at {m/1e6:.0f} MeV (800 vs 1500 q directions; nearest grid mass {masses[np.argmin(np.abs(masses-m))]/1e6:.2f} MeV):",
          np.round(F.rate(masses[np.argmin(np.abs(masses-m))], vh, qk, dirs_s, ff2_s, states) / b, 3))

for m in (10e6, 100e6):
    print(f"isotropic rate at {m/1e6:.0f} MeV: heavy {iso_rate(m):.3e}, light {iso_rate(m, light=True):.3e} events/kg/yr")

# ---- plot ----------------------------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 9, "axes.labelsize": 9, "legend.fontsize": 7.5})
fig, axs = plt.subplots(1, 2, figsize=(6.4, 2.9))
cols = {"a": "C0", "b": "C3", "c'": "C2"}
ax = axs[0]
for light, ls in ((False, "-"), (True, "--")):
    R, Riso = rows[light]
    ax.loglog(masses / 1e6, Riso, color="k", lw=1.2, ls=ls, label="light mediator" if light else "heavy mediator")
ax.set_xlim(0.9, 1000)
ax.set_ylim(1e1, 3e5)
ax.set_xlabel(r"$m_\chi$ (MeV)")
ax.set_ylabel(r"events / (kg yr), $\bar\sigma_e = 10^{-37}\,\mathrm{cm}^2$")
ax.set_title("(a) rate averaged over directions", fontsize=9)
ax.legend(loc="lower right", frameon=False)
ax = axs[1]
for light, ls in ((False, "-"), (True, "--")):
    R, Riso = rows[light]
    for i, name in enumerate(axes):
        ax.semilogx(masses / 1e6, R[:, i] / Riso, color=cols[name], lw=1.3, ls=ls,
                    label=(rf"$\hat{{\mathbf{{v}}}}_{{\mathrm{{E}}}} \parallel {name}$" if not light else None))
ax.axhline(1.0, color="0.5", lw=0.6)
ax.set_xlim(0.9, 1000)
ax.set_ylim(0.0, 2.5)
ax.set_xlabel(r"$m_\chi$ (MeV)")
ax.set_ylabel("rate / average")
ax.set_title("(b) by direction of the Earth's velocity", fontsize=9)
ax.legend(loc="upper right", frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig16_4.pdf"))
print("wrote fig16_4.pdf")
