"""Limit-box plot 10.4a (tex/figures/ch10/limit10_4a.pdf) and every number of Sect. 10.4 and WE 10.4.

Coupling: O_8 = S_chi . v_perp (Sect. 8.1), spin-1/2 dark matter, heavy mediator (c_8 constant), elastic, book halo
(App. A.8: v0 = 238, v_esc = 544, v_E = 250.5 km/s), threshold omega_th = E_g = 1.11 eV (the tables' scissor gap, Sect. 10.2).
Rate (App. D.30, eq:D.30-O8T, eq:D.30-kernel), responses averaged over directions (the cross term then vanishes):
  Gamma = (c_8^2/4) * C * int domega int dq q [ eta_2(v_min) S_nn(q, w) + eta(v_min) Tr S_jTjT(q, w) ]  =  Gamma_A + Gamma_B,
  eta_2(v_min) = 2 int_{v_min}^inf dv' v' eta(v')   (App. A.8),   r = Gamma_B / Gamma_A   (eq:D.30-r).
The literature formula of the box (Hochberg et al., arXiv:2510.25835, Eq. (6), static electron): Gamma_lit = Gamma_A.
Band (eq:8.3-bound, eq:D.30-band): (sqrt r - 1)^2 <= Gamma / Gamma_A <= (sqrt r + 1)^2; no cross term: 1 + r.
Shaded: r where Gamma_lit is within 10 % of every value the band allows, (sqrt r + 1)^2 <= 1.1, i.e. r <= 2.4e-3.

Inputs
  si_jresp_NK10_NC36.npz (si_jresp.py): IP S_nn and Tr S_jTjT of the empirical pseudopotential model (Cohen-Bergstresser),
    on q/q0 = 0.12 ... 3.6 along [100], [110], [111] and (5,3,1); 0.1 eV bins. Direction average: the 26-point Lebedev rule
    of degree 7 (weights 1/21, 4/105, 9/280 on the 6 face, 12 edge and 8 corner directions; by cubic symmetry
    S_avg = (6/21) S[100] + (48/105) S[110] + (72/280) S[111]). (5,3,1) is used for the cross-term size only.
    Model limits: plane waves up to 2.8 q0 (no high-momentum tails beyond), model gap 0.82 eV; the fraction of Gamma_A
    from q > 2.8 q0 is printed for each mass.
  si_elf_binned.npz (Sect. 10.2): Knapen-Kozaczuk-Lin GPAW tables (direction averaged), used for the screening factor of the
    density row with the eta_2 weight: s_n = int q^3 eta_2 eps2_IP / int q^3 eta_2 L_LF  (S = (2q^2/e^2) L, eq:4.4-SL).
  si_jresp_lf_NK10_a.npy (si_jresp.py, LF runs): local-field change of Tr S_jTjT in the model at (q, omega) points.
Run: python3 limit10_4a.py
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rate10_2 as R   # noqa: E402

ME, ALPHA = R.ME, R.ALPHA
Q0 = ALPHA * ME
EG = R.EG
VMAX = R.VMAX

d = np.load(os.path.join(HERE, "si_jresp_NK10_NC36.npz"))
Qf, WC = d["Q"], d["WC"]
DW = WC[1] - WC[0]
WC0 = WC.copy()
SCIS = 1.11 - 0.82          # scissor: raise every pair energy so that the model gap 0.82 eV becomes the 1.11 eV of the tables

wts = {"100": 6 / 21, "110": 48 / 105, "111": 72 / 280}
Snn = sum(w * d[f"S_{k}"][:, :, 0, 0] for k, w in wts.items())                       # (nq, nw) eV^2
Sjj = sum(w * (d[f"S_{k}"][:, :, 1, 1] + d[f"S_{k}"][:, :, 2, 2]) for k, w in wts.items())
qe = Qf * Q0

# eta_2 on a fine grid of v_min
_vg = np.linspace(0, VMAX * 1.0001, 20001)
_eta = R.eta(_vg)
_cum = np.concatenate([[0], np.cumsum(0.5 * (_vg[1:] * _eta[1:] + _vg[:-1] * _eta[:-1]) * np.diff(_vg))])
_eta2 = 2 * (_cum[-1] - _cum)


def eta2(vmin):
    return np.interp(vmin, _vg, _eta2, right=0.0)


def gammas(m, qcut=None, wth=EG, shift=0.0):
    W, Q = np.meshgrid(WC + shift, qe, indexing="ij")
    vmin = W / Q + Q / (2 * m)
    mask = (W >= wth).astype(float)
    if qcut is not None:
        mask *= (Q <= qcut)
    gA = np.trapezoid(np.sum(Q * eta2(vmin) * Snn.T * mask, 0) * DW, qe)
    gB = np.trapezoid(np.sum(Q * R.eta(vmin) * Sjj.T * mask, 0) * DW, qe)
    return gA, gB


def screening_density(m, light=False):
    """s_n: IP / (RPA + LF) for the eta_2-weighted density rate, from the GPAW tables of Sect. 10.2."""
    t = R.load()
    om, q = t["omega"], t["q"]
    W, Q = np.meshgrid(om, q, indexing="ij")
    vmin = W / Q + Q / (2 * m)
    k = Q**3 * eta2(vmin) * R.fdm2(Q, light) * (W >= EG)
    ip = np.trapezoid(np.trapezoid(k * t["ip"], q, axis=1), om)
    lf = np.trapezoid(np.trapezoid(k * t["lf"], q, axis=1), om)
    eta_ip = np.trapezoid(np.trapezoid(Q**3 * R.eta(vmin) * (W >= EG) * t["ip"], q, axis=1), om)
    eta_lf = np.trapezoid(np.trapezoid(Q**3 * R.eta(vmin) * (W >= EG) * t["lf"], q, axis=1), om)
    return ip / lf, eta_ip / eta_lf


print("Model checks (si_jresp_NK10_NC36.npz):")
for k in ["100", "110", "111", "531"]:
    res = d[f"res_{k}"]
    S = d[f"S_{k}"]
    iS = S.sum(1) * DW
    corr = np.sqrt(iS[:, 0, 1]**2 + iS[:, 0, 2]**2) / np.sqrt(iS[:, 0, 0] * (iS[:, 1, 1] + iS[:, 2, 2]))
    sel = Qf <= 2.8
    print(f"  [{k}] continuity residual {res[sel].min():.3f}-{res[sel].max():.3f} (q <= 2.8 q0); "
          f"omega-integrated |S_njT|/sqrt(S_nn TrS_jj) max {corr[sel].max():.4f}")
for i in [0, 4, 9, 16]:
    ratio = np.sum(Sjj[i]) / np.sum(Snn[i])
    print(f"  q = {Qf[i]:.2f} q0: int Tr S_jTjT / int S_nn = {ratio:.3e} (direction average); "
          f"2 <omega^2>/q^2 = {2*np.sum(WC**2*Snn[i])/np.sum(Snn[i])/qe[i]**2:.3e}")

print("\nO_8, heavy mediator, threshold 1.11 eV:")
out = {}
for m in [0.5e6, 1e6, 2e6, 3e6, 5e6, 10e6, 30e6]:
    gA, gB = gammas(m)
    gAc, gBc = gammas(m, qcut=2.8 * Q0)
    r = gB / gA
    sn, sn_eta = screening_density(m)
    gAs, gBs = gammas(m, shift=SCIS)
    out[m] = (r, sn)
    print(f"  m = {m/1e6:5.1f} MeV: with a scissor of {SCIS:.2f} eV (pair energies raised, vertices unchanged): "
          f"r_IP = {gBs/gAs:.1f} ({gBs/gAs/r - 1:+.1%})")
    print(f"  m = {m/1e6:5.1f} MeV: r_IP = {r:6.1f}; fraction of Gamma_A (Gamma_B) from q > 2.8 q0: "
          f"{1-gAc/gA:.2f} ({1-gBc/gB:.2f}); band (sqrt r -+ 1)^2 = [{(np.sqrt(r)-1)**2:.1f}, {(np.sqrt(r)+1)**2:.1f}], "
          f"1 + r = {1+r:.1f}; density screening s_n (eta_2 weight) = {sn:.2f} (eta weight {sn_eta:.2f}); "
          f"r_med = r_IP s_n (1 + delta), delta in [-0.3, 0.3]: [{r*sn*0.7:.0f}, {r*sn*1.3:.0f}]; "
          f"lower edge at r_med(delta=-0.3): {(np.sqrt(r*sn*0.7)-1)**2:.0f}")

# moment estimate: <v_eT^2> from the IP ratio at large q against the DM <v_T^2> = eta_2/eta
print("\nDark-matter side: eta_2/eta (= <|v_T|^2> over the halo above v_min):")
for vm in [0.0, 0.5e-3, 1.0e-3, 1.5e-3, 2.0e-3]:
    print(f"  v_min = {vm:.1e}: eta_2/eta = {eta2(vm)/R.eta(vm):.2e}")

lf = np.load(os.path.join(HERE, "si_jresp_lf_NK10_a.npy"))
print("\nLocal fields on the transverse current (model, (5,3,1) unless noted): q/q0, omega, delta_LF^jT, S_nn LF/IP")
for row in lf:
    print(f"  {row[0]:.1f} q0, {row[1]:.0f} eV: delta = {row[7]/row[5]-1:+.3f}; density LF/IP = {row[4]/row[2]:.3f}; "
          f"head-only current change {row[6]/row[5]-1:+.1e}")

# WE numbers
MWE = 10e6
gA, gB = gammas(MWE)
r = gB / gA
sn, _ = screening_density(MWE)
print(f"\nWE 10.4 (m = {MWE/1e6:.0f} MeV): Gamma_B/Gamma_A = r_IP = {r:.1f}; sqrt = {np.sqrt(r):.2f}; "
      f"band [{(np.sqrt(r)-1)**2:.1f}, {(np.sqrt(r)+1)**2:.1f}]; 1 + r = {1+r:.1f}; s_n = {sn:.2f}")
for dl in (-0.3, -0.15, 0.0, 0.3):
    rm = r * sn * (1 + dl)
    print(f"   delta = {dl:+.2f}: r_med = {rm:.0f}, band [{(np.sqrt(rm)-1)**2:.0f}, {(np.sqrt(rm)+1)**2:.0f}], 1 + r = {1+rm:.0f}")
rcut = (np.sqrt(1.1) - 1)**2
print(f"validity: (sqrt r + 1)^2 <= 1.1 for r <= {rcut:.2e}; 2 sqrt r/(1 + r) < 0.1 for r < {rcut:.2e} or r > "
      f"{((20 + np.sqrt(396))/2)**2:.0f}")

# ---------------- plot ----------------
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 9, "axes.labelsize": 9, "legend.fontsize": 7.5, "pdf.fonttype": 42,
                     "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 3.1))
x = np.geomspace(1e-3, 1e3, 600)
lo, hi = (np.sqrt(x) - 1)**2, (np.sqrt(x) + 1)**2
ax.fill_between(x, np.maximum(lo, 1e-3), hi, color="C0", alpha=0.18, lw=0, label=r"allowed band, $(\sqrt{r}\mp1)^2$")
ax.plot(x, hi, color="C0", lw=0.8)
ax.plot(x, np.maximum(lo, 1e-3), color="C0", lw=0.8)
ax.plot(x, 1 + x, "k--", lw=1.1, label=r"no cross term, $1 + r$")
ax.plot(x, np.ones_like(x), color="C3", lw=1.4, label=r"electron at rest, $\varGamma_A$")
ax.axvspan(1e-3, rcut, color="0.85", lw=0)
rIP = out[10e6][0]
rmed_lo, rmed_hi = rIP * out[10e6][1] * 0.7, rIP * out[10e6][1] * 1.3
ax.axvline(rIP, color="0.3", lw=0.9, ls=":")
ax.text(rIP * 0.9, 3e-2, r"$r_{\mathrm{IP}}$", ha="right", fontsize=7.5, color="0.25")
ax.axvspan(rmed_lo, rmed_hi, ymin=0, ymax=1, color="0.6", alpha=0.25, lw=0)
ax.text(rmed_hi * 1.1, 3e-2, "in medium", ha="left", fontsize=7, color="0.25")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1e-3, 1e3)
ax.set_ylim(1e-2, 2e3)
ax.set_xlabel(r"$r = \mathit{\Gamma}_B/\mathit{\Gamma}_A$")
ax.set_ylabel(r"$\mathit{\Gamma}/\mathit{\Gamma}_A$")
ax.legend(loc="upper left", bbox_to_anchor=(0.11, 1.0), frameon=False)
ax.text(1.15e-3, 1.4e-2, "formula\nwithin 10%", fontsize=6.5, color="0.35")
fig.tight_layout()
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch10")
fig.savefig(os.path.join(OUT, "limit10_4a.pdf"))
print("wrote limit10_4a.pdf")
