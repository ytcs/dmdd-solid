"""Fig. 10.5: valence, semicore and core shares of the germanium response that dark matter can reach, against q
(Sect. 10.6). Output: tex/figures/ch10/fig10_5.pdf. Prints every number of the onset paragraphs of Sect. 10.6.

Quantity: N_acc_nl(q) = int_{E_g + E_core}^{q v_max} S_at_nl(q, omega) domega, electrons per atom of shell nl that
dark matter of any mass can excite at momentum transfer q (core10_6.py; v_max = 2.650e-3).
  * Core and semicore shells (Ge 3d, 3p, 3s; Si 2p, 2s): free-atom, scalar-relativistic PBE orbitals, plane-wave final
    states counted from the valence maximum (core10_6.py). Variant: the same times the Fermi factor of eq:2.2-fermi with
    Z_eff = 1 at the final momentum p = [2 m_e (omega - E_core)]^{1/2} (the standard approximation of Sect. 2.2).
  * Valence: the crystal independent-particle eps2 of Knapen, Kozaczuk and Lin (ge_ip_binned.npz, from ge_ip_reduce.py;
    for Si si_elf_binned.npz of Sect. 10.2, 'ip'), S_at = q^2 Omega eps2/(8 pi^2 alpha), for q <= 15 keV; above,
    the atomic plane-wave model (the crystal table stops at 22.5 keV and its basis at |k| < 22 keV).
    Lattice constants: Ge a = 5.658 A (Sect. 3.3), Si a = 5.431 A.
  * Orthogonality check: the spurious overlap term |F_3d(q)|^2 phi(p)^2 against the angular mean of phi(|p - q|)^2,
    F_3d the elastic form factor of the shell.
"""
import os
import numpy as np
from scipy.optimize import brentq
from scipy.special import spherical_jn
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import core10_6 as c
from core10_6 import table, fermi

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch10", "fig10_5.pdf")
QSW = 15e3


def nacc_table(mat, q):
    om, qt, ip, Om = table(mat)
    j = np.argmin(abs(qt - q))
    w = np.linspace(c.EG[mat], min(qt[j] * c.VMAX, om[-1]), 400)
    return np.trapezoid(qt[j] ** 2 * Om * np.interp(w, om, ip[:, j]) / (8 * np.pi ** 2 * c.ALPHA), w)


def nacc_fermi(sh, q, n=600):
    top = q * c.VMAX
    if top <= sh.eth:
        return 0.0
    w = np.linspace(sh.eth, top, n)[1:]
    p = np.sqrt(2 * c.ME * (w - sh.ecore))
    return np.trapezoid(sh.S(q, w) * fermi(p), w)


ge, si = c.atom("Ge"), c.atom("Si")
q = np.geomspace(2e3, 100e3, 260)
val_mod = ge["4S"].nacc(q) + ge["4P"].nacc(q)
val_tab = np.array([nacc_table("Ge", qq) if qq <= 22.5e3 else np.nan for qq in q])
val = np.where(q <= QSW, val_tab, val_mod)
d3 = ge["3D"].nacc(q)
d3F = np.array([nacc_fermi(ge["3D"], qq) for qq in q])
deep = ge["3P"].nacc(q) + ge["3S"].nacc(q)
tot = val + d3 + deep

# --- numbers for the text
print("openings (E_g + E_core)/v_max [keV] and threshold masses 2(E_g + E_core)/v_max^2 [MeV]:")
for lab, e in (("Ge 3d5/2", 29.2), ("Ge 3d3/2", 29.8), ("Ge 3d (29 eV, Sect. 3.5)", 29.0), ("Ge 3p3/2", 120.8),
               ("Ge 3s", 180.1), ("Si 2p3/2", 99.42), ("Si 2s", 149.7)):
    eg = 0.744 if lab.startswith("Ge") else 1.17
    print(f"  {lab}: {(eg + e) / c.VMAX / 1e3:.1f} keV, {2 * (eg + e) / c.VMAX ** 2 / 1e6:.1f} MeV")
i = np.argmin(abs(q - QSW))
print(f"valence at the switch {QSW / 1e3:.0f} keV: table {nacc_table('Ge', QSW):.2e}, model "
      f"{ge['4S'].nacc(QSW)[0] + ge['4P'].nacc(QSW)[0]:.2e}, ratio "
      f"{(ge['4S'].nacc(QSW)[0] + ge['4P'].nacc(QSW)[0]) / nacc_table('Ge', QSW):.2f}")
for qq in (5e3, 10e3, 12e3, 15e3, 20e3, 30e3, 50e3, 80e3):
    v = nacc_table("Ge", qq) if qq <= QSW else ge["4S"].nacc(qq)[0] + ge["4P"].nacc(qq)[0]
    dd = ge["3D"].nacc(qq)[0]
    dp = ge["3P"].nacc(qq)[0] + ge["3S"].nacc(qq)[0]
    print(f"  q = {qq / 1e3:.0f} keV: valence {v:.2e}, 3d {dd:.2e} (Fermi {nacc_fermi(ge['3D'], qq):.2e}), "
          f"3p+3s {dp:.2e}; 3d share {dd / (v + dd + dp):.2f}")
qs = np.arange(11.3e3, 16e3, 50.0)
tv = np.array([nacc_table("Ge", x) for x in qs])
x_tab = qs[np.nonzero(ge["3D"].nacc(qs) > tv)[0][0]]
x_F = qs[np.nonzero(np.array([nacc_fermi(ge["3D"], x) for x in qs]) > tv)[0][0]]
x_mod = brentq(lambda x: ge["3D"].nacc(x)[0] - ge["4S"].nacc(x)[0] - ge["4P"].nacc(x)[0], 11.3e3, 20e3)
print(f"3d overtakes valence: crystal valence {x_tab / 1e3:.2f} keV, with Fermi factor {x_F / 1e3:.2f} keV, "
      f"atomic valence {x_mod / 1e3:.2f} keV")
x_si = brentq(lambda x: si["2P"].nacc(x)[0] - si["3S"].nacc(x)[0] - si["3P"].nacc(x)[0], 38.1e3, 70e3)
print(f"Si 2p overtakes the (atomic) valence at {x_si / 1e3:.1f} keV; Si valence vs crystal table at 10 keV: "
      f"model {si['3S'].nacc(10e3)[0] + si['3P'].nacc(10e3)[0]:.2e}, table {nacc_table('Si', 10e3):.2e}")
print(f"Si 2s overtakes 2p at {brentq(lambda x: si['2S'].nacc(x)[0] - si['2P'].nacc(x)[0], 60e3, 120e3) / 1e3:.0f} keV;"
      f" Ge 3p+3s overtake 3d at "
      f"{brentq(lambda x: ge['3P'].nacc(x)[0] + ge['3S'].nacc(x)[0] - ge['3D'].nacc(x)[0], 45e3, 120e3) / 1e3:.0f} keV")
r_, wf = c.load("ge_r1")
u = wf["3D"]
sh = ge["3D"]
worst = 0
for qq in (12e3, 15e3, 20e3, 30e3):
    F = np.trapezoid(u ** 2 * spherical_jn(0, qq / c.AU * r_), r_) / np.trapezoid(u ** 2, r_)
    for w in np.linspace(sh.eth + 1, qq * c.VMAX, 20):
        p = np.sqrt(2 * c.ME * (w - sh.ecore))
        avg = (sh.cum(p + qq) - sh.cum(abs(qq - p))) / (2 * p * qq)
        worst = max(worst, F ** 2 * np.interp(p, sh.k, sh.phi2) / avg)
print(f"orthogonality: largest spurious/true ratio for 3d, q = 12-30 keV: {worst:.3f}")
F15 = np.trapezoid(u ** 2 * spherical_jn(0, 15e3 / c.AU * r_), r_)
print(f"Fermi factor (Z_eff = 1) at p = 2, 5 keV: {fermi(2e3):.1f}, {fermi(5e3):.1f}")

# --- figure
plt.rcParams.update({"font.size": 9})
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 2.9), gridspec_kw={"wspace": 0.32})
a1.loglog(q / 1e3, val, color="k", lw=1.3, label="valence $4s4p$")
a1.loglog(q / 1e3, np.where(q > QSW, np.nan, val_mod), color="k", lw=0.8, ls=":")
a1.loglog(q / 1e3, np.where(q < QSW, np.nan, val_tab), color="0.5", lw=0.8, ls=":")
a1.loglog(q / 1e3, np.where(d3 > 0, d3, np.nan), color="C2", lw=1.3, label="semicore $3d$")
a1.loglog(q / 1e3, np.where(d3F > 0, d3F, np.nan), color="C2", lw=1.0, ls="--", label=r"$3d$, Fermi factor")
a1.loglog(q / 1e3, np.where(deep > 0, deep, np.nan), color="C0", lw=1.3, label="core $3s3p$")
for e, col in ((29.44, "C2"), (122.2, "C0")):
    a1.axvline((0.744 + e) / c.VMAX / 1e3, color=col, ls=":", lw=0.7)
a1.set_xlim(2, 100)
a1.set_ylim(1e-5, 2)
a1.set_xlabel(r"momentum transfer $q$ (keV)")
a1.set_ylabel(r"reachable electrons per atom")
a1.set_title("(a)", fontsize=9, loc="left")
a1.legend(loc="lower left", fontsize=7, frameon=False, handlelength=2.0)
sv, s3, sd = (np.nan_to_num(x / tot) for x in (val, d3, deep))
a2.fill_between(q / 1e3, 0, sv, color="0.75", lw=0, label="valence")
a2.fill_between(q / 1e3, sv, sv + s3, color="C2", alpha=0.55, lw=0, label="semicore $3d$")
a2.fill_between(q / 1e3, sv + s3, sv + s3 + sd, color="C0", alpha=0.55, lw=0, label="core $3s3p$")
a2.plot(q / 1e3, np.nan_to_num(val / (val + d3F + deep)), color="C2", ls="--", lw=1.0, label="valence share,\n$3d$ Fermi factor")
a2.set_xscale("log")
a2.set_xlim(2, 100)
a2.set_ylim(0, 1)
a2.set_xlabel(r"momentum transfer $q$ (keV)")
a2.set_ylabel("share of reachable electrons")
a2.set_title("(b)", fontsize=9, loc="left")
a2.legend(loc="center left", bbox_to_anchor=(0.0, 0.55), fontsize=6.5, frameon=True, facecolor="white", edgecolor="0.6",
           framealpha=1, handlelength=1.3, handletextpad=0.4, borderpad=0.3,
           borderaxespad=0.25)
fig.savefig(OUT, bbox_inches="tight")
print("wrote", OUT)
