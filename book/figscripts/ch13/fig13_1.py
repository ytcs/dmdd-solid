"""Fig. 13.1 (fig:13-window) and every number of Sect. 13.1 and its worked example (we:13-onset).

Panel (a): the minimum pair energy E_min(q) of silicon along [100], [110], [111] (the cached first-principles grid of
Fig. 3.6: figscripts/ch03/qe_si_pbe.npz, QE 7.6, PBE, SG15, 60 Ry, a = 5.431 A, 48^3 grid, no spin-orbit coupling),
with the conduction bands shifted rigidly so that the indirect gap equals the measured E_g(0) = 1.17 eV (the same
scissor as Fig. 3.6, 0.613 eV); the phonon-assisted threshold E_g + min_nu omega_nu(k_c - q) for q along [100]
(G' = 0 class, electron and hole at the band extrema); and the largest energy deposited, q v_max - q^2/2m_chi, for
0.3, 0.4 and 0.5 MeV. Panel (b): the threshold mass q^2 / [2 (q v_max - E_th(q))] of each channel against |q|, whose
minimum over q is m_min^ZP or m_min^PA.

Phonons: the book's silicon force constants of Sect. 5.2 (figscripts/ch05/si_ifc.py: PBE, 60 Ry, 12^3 k, 6^3 Q, at the
measured a), whose TA branch is 8 % soft at X against neutron data (4.13 vs 4.49 THz; Dolling 1963, Nilsson-Nelin
1972, Sect. 5.2). The neutron-scaled variant multiplies the TA branch by 18.57/17.05 (ratio at X); the scaling is a
modelling choice that bounds the effect of the softness, not a measured dispersion.

Measured inputs: E_g(0) = 1.17 eV (Ramanathan-Kurinsky Eq. (11), 1.1692 eV; Sect. 3.3); k_c = 0.85 (2pi/a) (Feher
1959); E_x^b = 14.7 meV (Sect. 4.9); m_l = 0.916, m_t = 0.191 (Hensel 1965), Luttinger masses m_hh[100] = 0.277,
m_hh[111] = 0.718 (Table 3.1); Ge: E_g = 0.744 eV, |Gamma L| = 1.898 keV (a = 5.658 A), m_l = 1.59, m_hh[111] = 0.469
(Table 3.1), TA at L 1.9 THz and at X 2.4 THz (Nilsson-Nelin 1971 at 80 K, as tabulated in Haxhijaj et al. 2026 Table IV; Table 5.x: 9.9 meV at X); GaAs:
E_g = 1.52 eV, L valleys 1.815 eV, X valleys 1.981 eV, m_e* = 0.067, m_hh[100] = 0.350, m_hh[111] = 0.893 (Table 3.1,
Vurgaftman 2001), TA at X 10.5 meV (Table 5.x). v_max = 794.5 km/s (Sect. 1.2).
Run: python fig13_1.py (about 10 s). Output: tex/figures/ch13/fig13_1.pdf; numbers on stdout (fig13_1.log).
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "ch05"))
import si_ifc                                   # noqa: E402

HBARC = 1973.269804          # eV Angstrom
ME = 510998.95               # eV
VMAX = 794.5 / 299792.458    # 2.650e-3
V2 = VMAX ** 2
EG = 1.17                    # eV, Si low temperature
EXB = 0.0147                 # eV, Si exciton binding
A = 5.431
G1 = 2 * np.pi * HBARC / A   # 2pi/a = 2283 eV
KC = 0.85 * G1               # 1.94 keV
mfloor = lambda E: 2 * E / V2


def mreq(q, E):
    """Lightest mass that deposits E at momentum transfer q (inf where q v_max <= E)."""
    q = np.asarray(q, float); E = np.broadcast_to(E, q.shape)
    ok = q * VMAX > E
    return np.where(ok, q ** 2 / (2 * np.where(ok, q * VMAX - E, 1.0)), np.inf)


def edge(q, E):
    m = mreq(q, E)
    j = int(np.argmin(m))
    return m[j], q[j], j


print(f"v_max = {VMAX:.4e}, v_max^2 = {V2:.4e}; 2pi/a = {G1:.1f} eV; k_c = {KC:.0f} eV")
print(f"floor 2E_g/v^2 = {mfloor(EG)/1e6:.4f} MeV at q = {2*EG/VMAX:.0f} eV; with exciton {mfloor(EG-EXB)/1e6:.4f} MeV")

# ---------------- silicon phonons along [100] -------------------------------------------------------------------
q = np.linspace(200, 2400, 2201)              # eV, along [100]
Qx = (KC - q) / G1                            # phonon wavevector (2pi/a), along [100]
w, _ = si_ifc.phonons(np.column_stack([Qx, 0 * Qx, 0 * Qx]))
wTA = w[:, 0] / 1e3                           # eV, lowest branch
wLA = w[:, 2] / 1e3
wX = si_ifc.phonons([[1.0, 0, 0]])[0][0][0]
scaleTA = 18.57 / wX
print(f"Si PBE TA(X) = {wX:.2f} meV (measured 18.57); TA scale {scaleTA:.4f}")
for name, wt in (("PBE", wTA), ("neutron-scaled TA", wTA * scaleTA)):
    m_c, q_c, j = edge(q, EG + wt)
    m_x, q_x, jx = edge(q, EG - EXB + wt)
    Qs = (KC - q_c) / G1
    env = mfloor(EG + wt[j])
    print(f"  {name}: m_PA continuum = {m_c/1e6:.4f} MeV at q* = {q_c:.0f} eV, |Q*| = {Qs:.3f} (2pi/a) = "
          f"{Qs*2*np.pi/A:.3f} 1/A, omega_TA(Q*) = {wt[j]*1e3:.2f} meV; envelope 2(E_g+w)/v^2 = {env/1e6:.4f}; "
          f"replica = {m_x/1e6:.4f} MeV at q = {q_x:.0f} eV, omega = {wt[jx]*1e3:.2f} meV")
# slope of TA at Q*, tilt term 1/2 M |grad omega|^2 (along the axis only)
m_c, q_c, j = edge(q, EG + wTA)
dw = np.gradient(wTA, q)[j]                   # d omega / d q (dimensionless, = -d omega/dQ)
Mpair = (0.916 + 0.277) * ME
print(f"  TA group velocity at Q*: {abs(dw):.3e} (= {abs(dw)*299792.458:.2f} km/s); tilt term "
      f"M|v|^2/2 = {0.5*Mpair*dw**2*1e3:.3f} meV (M = 1.19 m_e)")
# light: photon gets k_c from phonon at k_c itself
wkc = si_ifc.phonons([[0.85, 0, 0]])[0][0]
print(f"  phonons at k_c (PBE): TA {wkc[0]:.2f}, LA {wkc[2]:.2f}, TO {wkc[3]:.2f} meV (optical edge: 18.27, 57.73)")
# LA and TO channels
for nm, br in (("LA", 2), ("TO", 3)):
    m_b, q_b, jb = edge(q, EG + w[:, br] / 1e3)
    print(f"  {nm}-assisted onset {m_b/1e6:.4f} MeV (omega {w[jb, br]:.2f} meV)")
# finite temperature: phonon absorption sideband weight
for T in (0.01, 0.1, 1.0, 4.0, 77.0):
    kT = 8.617333e-5 * T
    nB = 1 / np.expm1(wTA[j] / kT) if wTA[j] / kT < 700 else 0.0
    print(f"  n_B(omega_TA(Q*)) at T = {T} K: {nB:.3e}" + ("" if nB else " (exp < 1e-300)"))
mabs = edge(q, EG - wTA)[0]
print(f"  absorption-sideband kinematic onset (T > 0 only): {mabs/1e6:.4f} MeV")

# ---------------- zero-phonon edges: grid and parabolic ---------------------------------------------------------
d = np.load(os.path.join(HERE, "..", "ch03", "qe_si_pbe.npz"))
kp, eb = d["kp"], d["bands"]
iG = int(np.argmin(np.linalg.norm(kp[:100], axis=1)))
vbm = eb[iG, 3]
sk, se = d["scan_k"], d["scan_e"] - vbm
s, cb = sk[:61, 0], se[:61, 4]
jj = int(np.argmin(cb)); win = slice(jj - 4, jj + 5)
c = np.polyfit(s[win] - s[jj], cb[win], 2)
Eg_pbe = np.polyval(c, -c[1] / (2 * c[0]))
scis = EG - Eg_pbe
print(f"PBE gap {Eg_pbe:.4f} eV; scissor {scis:.3f} eV")
Emin = {n: (d["q" + n], d["E" + n] + scis) for n in ("[100]", "[110]", "[111]")}
for n, (qs, es) in Emin.items():
    mz, qz, _ = edge(qs, es)
    print(f"  grid E_min {n}: lightest mass {mz/1e6:.4f} MeV at q = {qz:.0f} eV (48^3 grid)")
# parabolic valley along the axis, eq:3.3-Eminpar
for lab, Mm in (("Si [100] hh 0.277", 0.916 + 0.277), ("Si [100] lh 0.201", 0.916 + 0.201)):
    M = Mm * ME
    mz, qz, _ = edge(q, EG + (q - KC) ** 2 / (2 * M))
    print(f"  parabolic {lab} (M = {Mm:.3f} m_e): m_ZP = {mz/1e6:.4f} MeV at q = {qz:.0f} eV, "
          f"E = {EG + (qz-KC)**2/(2*M):.3f} eV; deficit k_c - q = {KC-qz:.0f} eV")
mz_exact_kc = KC ** 2 / (2 * (KC * VMAX - EG))
print(f"  deposit E_g at exactly k_c: {mz_exact_kc/1e6:.4f} MeV (3.3: 0.474)")
# closed form check: parabolic m(q) minimum, stationary condition
M = (0.916 + 0.277) * ME
qq = np.linspace(500, 2400, 200001)
mm = mreq(qq, EG + (qq - KC) ** 2 / (2 * M))
print(f"  parabolic fine: {mm.min()/1e6:.4f} MeV at q = {qq[np.argmin(mm)]:.1f} eV")

# ---------------- germanium -------------------------------------------------------------------------------------
EGG = 0.744; KL = np.sqrt(3) / 2 * 2 * np.pi * HBARC / 5.658
print(f"Ge: |Gamma L| = {KL:.1f} eV; floor {mfloor(EGG)/1e6:.4f} MeV at q = {2*EGG/VMAX:.0f} eV")
for lab, wt in (("TA(L) 1.9 THz", 1.9 * 4.135667696), ("TA(X) 9.9 meV", 9.9)):
    print(f"  PA onset with omega <= {lab} = {wt:.2f} meV: <= {mfloor(EGG + wt/1e3)/1e6:.4f} MeV")
print(f"  deposit E_g at exactly |Gamma L|: {KL**2/(2*(KL*VMAX-EGG))/1e6:.4f} MeV")
qg = np.linspace(200, 2400, 220001)
for lab, Mm in (("[111] hh 0.469", 1.59 + 0.469), ("[111] lh 0.041", 1.59 + 0.041)):
    M = Mm * ME
    mz, qz, _ = edge(qg, EGG + (qg - KL) ** 2 / (2 * M))
    print(f"  Ge parabolic {lab} (M = {Mm:.3f}): m_ZP = {mz/1e6:.4f} MeV at q = {qz:.0f} eV")
# Gamma route of Ge (direct gap 0.89 eV): m_ZP = m_g M/(M - m_g)
for lab, Mm in (("Gamma, hh[111] 0.469, m_c 0.038 (orientation only, not printed)", 0.038 + 0.469),):
    M = Mm * ME; mg = mfloor(0.89)
    print(f"  Ge {lab}: M v^2/2 = {M*V2/2:.3f} eV vs 0.89; m_ZP = {mg*M/(M-mg)/1e6 if M > mg else np.inf:.3f} MeV")

# ---------------- GaAs ------------------------------------------------------------------------------------------
EGA = 1.52
mg = mfloor(EGA)
print(f"GaAs: floor 2E_g/v^2 = {mg/1e6:.4f} MeV at q* = {2*EGA/VMAX:.0f} eV = {2*EGA/VMAX/(2*np.pi*HBARC/5.653):.2f} (2pi/a)")
for lab, Mm in (("[100] hh", 0.067 + 0.350), ("[111] hh", 0.067 + 0.893)):
    M = Mm * ME
    tag = f"{mg*M/(M-mg)/1e6:.2f} MeV" if M > mg else "never"
    print(f"  Gamma pair {lab}: M = {Mm:.3f} m_e, max (q v - q^2/2M) = M v^2/2 = {M*V2/2:.3f} eV; zero-phonon onset: {tag}")
    print(f"     pair recoil at q* = q*^2/2M = {(2*EGA/VMAX)**2/(2*M):.2f} eV")
print(f"  PA onset (phonon takes q, omega <= TA(X) 10.5 meV): {mg/1e6:.4f} - {mfloor(EGA+0.0105)/1e6:.4f} MeV")
KLg = np.sqrt(3) / 2 * 2 * np.pi * HBARC / 5.653
for lab, E in (("L 1.815", 1.815), ("X 1.981", 1.981)):
    kk = KLg if lab[0] == "L" else 2 * np.pi * HBARC / 5.653
    print(f"  {lab} valley: floor {mfloor(E)/1e6:.4f} MeV; deposit at exactly the valley ({kk:.0f} eV): "
          f"{kk**2/(2*(kk*VMAX-E))/1e6:.4f} MeV")

# ---------------- figure ----------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 9})
fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.6, 3.2), gridspec_kw={"wspace": 0.34})
cols = {"[100]": "C0", "[110]": "C1", "[111]": "C2"}
for n, (qs, es) in Emin.items():
    if n != "[111]":                          # [111] stays above 2.13 eV, off the plotted range
        ax.plot(qs / 1e3, es, color=cols[n], lw=1.1, label=r"$E_{\mathrm{min}}$ " + n)
ax.plot(q / 1e3, EG + wTA, color="C3", lw=1.1, label=r"$E_{\mathrm{g}} + \omega_{\mathrm{TA}}(\mathbf{k}_{\mathrm{c}} - \mathbf{q})$")
ax.axhline(EG, color="0.4", lw=0.6, ls="-.")
qq = np.linspace(1, 3000, 600)
for m, ls in ((0.3e6, ":"), (0.4e6, "--"), (0.5e6, "-")):
    ax.plot(qq / 1e3, qq * VMAX - qq ** 2 / (2 * m), color="k", lw=0.8, ls=ls)
    jm = np.argmax(qq * VMAX - qq ** 2 / (2 * m))
    ytop = qq[jm] * VMAX - qq[jm] ** 2 / (2 * m)
    if m == 0.4e6:                            # inside its own parabola, clear of the [100] edge and the 0.5 MeV curve
        ax.text(qq[jm] / 1e3, ytop - 0.09, f"{m/1e6:.1f} MeV", fontsize=7, ha="center", va="top")
    else:                                     # above the apex; 0.3 MeV nudged right, clear of the 0.5 MeV curve
        ax.text(qq[jm] / 1e3 + (0.08 if m == 0.3e6 else 0.0), ytop + 0.03, f"{m/1e6:.1f} MeV", fontsize=7,
                ha="center", va="bottom")
ax.axvline(KC / 1e3, color="0.6", lw=0.5)
ax.text(KC / 1e3 + 0.03, 0.93, r"$k_{\mathrm{c}}$", color="0.3", fontsize=8)
ax.text(0.05, EG - 0.07, r"$E_{\mathrm{g}}$", color="0.3", fontsize=8)
ax.set_xlim(0, 2.6); ax.set_ylim(0.9, 2.3)
ax.set_xlabel(r"$|\mathbf{q}|$ (keV)"); ax.set_ylabel(r"$E_{\mathrm{min}}$, $\omega$ (eV)")
ax.legend(loc="upper right", fontsize=6.5, frameon=False, handlelength=1.6)
ax.text(0.02, 0.97, "(a)", transform=ax.transAxes, va="top")

for n, (qs, es) in Emin.items():
    if n != "[111]":                          # [111] minimum 0.615 MeV, off the plotted range
        bx.plot(qs / 1e3, mreq(qs, es) / 1e6, color=cols[n], lw=1.1)
        mz, qz, _ = edge(qs, es)
        bx.plot([qz / 1e3], [mz / 1e6], "o", color=cols[n], ms=3)
bx.plot(q / 1e3, mreq(q, EG + wTA) / 1e6, color="C3", lw=1.1)
bx.plot(q / 1e3, mreq(q, EG - EXB + wTA) / 1e6, color="C3", lw=0.8, ls="--")
bx.plot(q / 1e3, mreq(q, np.full_like(q, EG)) / 1e6, color="0.4", lw=0.6, ls="-.")
mp, qp, _ = edge(q, EG + wTA)
bx.plot([qp / 1e3], [mp / 1e6], "o", color="C3", ms=3)
bx.set_xlim(0.4, 2.6); bx.set_ylim(0.3, 0.6)
bx.set_xlabel(r"$|\mathbf{q}|$ (keV)"); bx.set_ylabel(r"$q^2/[2(qv_{\mathrm{max}} - E_{\mathrm{th}})]$ (MeV)")
bx.text(0.02, 0.97, "(b)", transform=bx.transAxes, va="top")
out = os.path.join(HERE, "..", "..", "tex", "figures", "ch13", "fig13_1.pdf")
fig.savefig(out, bbox_inches="tight")
print("wrote", os.path.normpath(out))
