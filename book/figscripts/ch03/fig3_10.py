"""Fig. 3.10: momentum distribution of the electrons of each atomic shell of silicon and germanium (Sect. 3.5).
Output: tex/figures/ch03/fig3_10.pdf. Prints the numbers quoted in Sect. 3.5 (shell radii, median momenta,
fractions above the kinematic opening, crossovers).

Orbitals: all-electron atoms from ld1.x (Quantum ESPRESSO 7.6 atomic code), PBE, scalar-relativistic (rel=1),
reference configurations [Ne]3s2 3p2 (Si) and [Ar]3d10 4s2 4p2 (Ge); inputs and outputs in ld1/ (si_r1.*, ge_r1.*).
ld1.x writes the seven outermost orbitals only, so Ge 1s is absent; it opens at q >= 4 MeV and plays no role here.
The .wfc files hold u_nl(r) = r R_nl(r) on a logarithmic grid in bohr, normalized to int u^2 dr = 1.

Momentum amplitude: phi_nl(p) = sqrt(2/pi) int_0^inf dr r u_nl(r) j_l(p r), normalized to int p^2 phi^2 dp = 1.
Plotted: electrons per keV of momentum, N_nl p^2 phi_nl(p)^2 / (keV per bohr^-1), with N_nl the shell occupation.
Modelling choice: free-atom orbitals (frozen core); for the valence shells the crystal redistributes the weight
below a few keV, but not the large-p tails that matter here.

Kinematic openings (vertical lines): a transition from a shell at depth E_core below the valence-band maximum needs
omega >= E_g + E_core, hence q >= omega / v_max (Eq. 1.3-vmin with q/2m_chi > 0), v_max = 2.650e-3 (Sect. 1.3).
E_core relative to the valence maximum, X-Ray Data Booklet Table 1-1 (Williams 2009), extract in
sources/3.5/xdb_table1-1.txt: Si 2p3/2 99.42 (quoted 99.4), 2s 149.7 (quoted 150), 1s 1839 eV; Ge 3d5/2 29.2
(quoted 29), 3p3/2 120.8, 3s 180.1, 2p3/2 1217.0 eV. Gaps 1.17 eV (Si) and 0.744 eV (Ge), low temperature (Sect. 3.3).
Unit: 1 bohr^-1 = alpha m_e = 3.72894 keV (CODATA).
"""
import os
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import spherical_jn
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch03", "fig3_10.pdf")
AU_KEV = 3.72894          # keV per bohr^-1
BOHR_A = 0.529177         # Angstrom per bohr
VMAX = 2.650e-3
L = {"S": 0, "P": 1, "D": 2}


def load(name):
    path = os.path.join(HERE, "ld1", name + ".wfc")
    heads = open(path).readline().split()[2:]
    d = np.loadtxt(path)
    return d[:, 0], {h: d[:, i + 1] for i, h in enumerate(heads)}


def momentum(r, u, l, p, rmax=20.0, dr=2e-4):
    """Radial momentum amplitude on the bohr^-1 grid p, from a spline of u on a uniform fine grid."""
    sp = CubicSpline(r, u)
    x = np.arange(dr, rmax, dr)
    ux = np.where(x >= r[0], sp(x), u[0] * (x / r[0]) ** (l + 1))
    out = np.empty_like(p)
    for i, pp in enumerate(p):
        out[i] = np.sqrt(2 / np.pi) * np.trapezoid(x * ux * spherical_jn(l, pp * x), x)
    return out


def shells(name, occ):
    r, w = load(name)
    p = np.logspace(np.log10(0.05), np.log10(400 / AU_KEV), 500)
    res = {}
    for h, u in w.items():
        l = L[h[1]]
        ph = momentum(r, u, l, p)
        dens = p ** 2 * ph ** 2
        norm = np.trapezoid(dens, p)
        cum = np.concatenate([[0], np.cumsum(0.5 * (dens[1:] + dens[:-1]) * np.diff(p))]) / norm
        res[h] = dict(p=p * AU_KEV, n=occ[h] * dens / AU_KEV, cum=cum, norm=norm,
                      rpk=r[np.argmax(np.abs(u))] * BOHR_A, rmean=np.trapezoid(r * u ** 2, r) * BOHR_A)
    return res


si = shells("si_r1", {"3P": 2, "3S": 2, "2P": 6, "2S": 2, "1S": 2})
ge = shells("ge_r1", {"4P": 2, "4S": 2, "3D": 10, "3P": 6, "3S": 2, "2P": 6, "2S": 2})

EG = {"Si": 1.17, "Ge": 0.744}
ECORE = {"Si": {"2P": 99.4, "2S": 150.0, "1S": 1839.0}, "Ge": {"3D": 29.0, "3P": 120.8, "3S": 180.1, "2P": 1217.0}}


def qmin(mat, sh):
    return (EG[mat] + ECORE[mat][sh]) / VMAX / 1e3    # keV


def mmin(mat, sh):
    return 2 * (EG[mat] + ECORE[mat][sh]) / VMAX ** 2 / 1e6   # MeV


for mat, res in (("Si", si), ("Ge", ge)):
    print(f"--- {mat}")
    for h, d in res.items():
        med = np.interp(0.5, d["cum"], d["p"])
        line = (f"{h}: norm {d['norm']:.4f}, radial peak {d['rpk']:.3f} A, <r> {d['rmean']:.3f} A, "
                f"median p {med:.2f} keV")
        if h in ECORE[mat]:
            q0 = qmin(mat, h)
            frac = 1 - np.interp(q0, d["p"], d["cum"])
            line += f"; opening q >= {q0:.2f} keV, m >= {mmin(mat, h):.2f} MeV; fraction of shell above: {frac:.3f}"
        print(line)


def crossing(a, b):
    """Lowest p (keV) above 2 keV at which shell a's density exceeds shell b's."""
    pa, na, nb = a["p"], a["n"], b["n"]
    m = (pa > 2) & (na > nb)
    return pa[m][0] if m.any() else np.nan


val_si = dict(p=si["3S"]["p"], n=si["3S"]["n"] + si["3P"]["n"])
val_ge = dict(p=ge["4S"]["p"], n=ge["4S"]["n"] + ge["4P"]["n"])
print(f"Si: 2p exceeds valence above {crossing(si['2P'], val_si):.1f} keV; 1s exceeds 2p above "
      f"{crossing(si['1S'], si['2P']):.1f} keV")
print(f"Ge: 3d exceeds valence above {crossing(ge['3D'], val_ge):.1f} keV")
for q in (10.0, 30.0):
    i = np.argmin(np.abs(si["2P"]["p"] - q))
    print(f"Si at p = {q} keV: valence {val_si['n'][i]:.3e}, 2p {si['2P']['n'][i]:.3e}, 2s {si['2S']['n'][i]:.3e}, "
          f"1s {si['1S']['n'][i]:.3e} electrons/keV")

plt.rcParams.update({"font.size": 9})
fig, axes = plt.subplots(1, 2, figsize=(6.4, 3.0), sharey=True, gridspec_kw={"wspace": 0.08})
styles = {"val": ("k", "-"), "1S": ("C3", "-"), "2S": ("C1", "--"), "2P": ("C1", "-"),
          "3S": ("C0", "--"), "3P": ("C0", "-"), "3D": ("C2", "-")}
panels = (("Si", si, val_si, ["2P", "2S", "1S"], r"$3s^23p^2$"), ("Ge", ge, val_ge, ["3D", "3P", "3S", "2P", "2S"],
                                                                         r"$4s^24p^2$"))
for ax, (mat, res, val, core, vlab) in zip(axes, panels):
    ax.loglog(val["p"], val["n"], color="k", lw=1.2, label=f"valence {vlab}")
    for h in core:
        col, ls = styles[h]
        lab = f"{h[0]}{h[1].lower()}"
        ax.loglog(res[h]["p"], res[h]["n"], color=col, ls=ls, lw=1.0, label=lab)
        if h in ECORE[mat] and qmin(mat, h) < 400:
            q0 = qmin(mat, h)
            ax.axvline(q0, color=col, ls=":", lw=0.8)
            ax.text(q0 * 1.04, 2.2, lab, color=col, fontsize=7, rotation=90, va="top")
    ax.set_xlim(0.5, 400)
    ax.set_ylim(1e-6, 3)
    ax.set_xlabel(r"momentum $p$ (keV)")
    ax.set_title(f"({'ab'[axes.tolist().index(ax)]}) {'silicon' if mat == 'Si' else 'germanium'}", fontsize=9, loc="left")
    ax.legend(loc="lower left", fontsize=7, frameon=True, framealpha=0.9, facecolor="white", edgecolor="none",
              handlelength=1.8)   # opaque box: the small-p tails run through this corner
axes[0].set_ylabel(r"electrons per keV")
fig.savefig(OUT, bbox_inches="tight")
print("wrote", OUT)
