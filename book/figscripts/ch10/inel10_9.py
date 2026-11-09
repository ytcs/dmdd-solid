"""Inelastic and exothermic electron recoil in silicon (Sect. 10.9): Fig. 10.8, Worked example 10.9 and Limit 10.9a.
Natural units hbar = c = 1, Heaviside-Lorentz e^2 = 4 pi alpha; energies and momenta in eV.

Rate (Sect. 10.9, eq:10.9-inel; the loss-function rate eq:10.2-rate with the splitting in v_min):
  dR/domega = rho_chi sigma_e / (8 pi^2 alpha rho_T m mu^2) int dq q^3 eta(v_min) F_DM(q)^2 L(q, omega),
  v_min = |(omega + Delta)/q + q/(2m)|                       (Sect. 1.3, eq:1.3-vmin; Gu, Wu, Zhu arXiv:2203.06664 Eq. (11))
  The IP rate puts eps_2 of the independent-particle head in place of L (S^IP = (2q^2/e^2) eps_2^IP, Sect. 10.2); it
  stands in for the QEdark form factor of 2203.06664 Eqs. (16), (20) (same many-body approximation, different code).
Exothermic shell (Sect. 10.9, eq:10.9-shell), Delta < 0, v << v_Delta = q_Delta/m:
  dR/domega = rho_chi sigma_e q_Delta^3 F_DM(q_Delta)^2 L(q_Delta, omega) / (4 pi^2 alpha rho_T mu^2) [1 + O(v^2/v_Delta^2)],
  q_Delta = sqrt(2 m (|Delta| - omega)).  Derived in the text: the delta function of omega_q fixes |q - m v| = k_*, a
  sphere centred at m v; for constant F the q integral is exactly 4 pi m k_*, k_*^2 = q_Delta^2 + m^2 v^2.
Free-electron line (Sect. 10.9): omega_line = mu_chi_e |Delta| / m_e (exothermic down-scattering on an electron at rest).
Inputs: everything from rate10_2.py (constants, book halo v0 = 238, v_esc = 544, v_E = 250.5 km/s, rho_chi = 0.3 GeV/cm^3,
  rho_T = 2.33 g/cm^3, eta of App. D.1) and the silicon loss functions si_elf_binned.npz (Knapen-Kozaczuk-Lin GPAW tables,
  directions averaged in 100 eV bins of |q|; scissor gap 1.11 eV, the tables' projection threshold; the physical low-T gap
  is 1.17 eV).
Modelling choices (stated in the captions): below the first tabulated momentum, 493 eV, L(q, omega) is held at its value
  in the first bin (the dispersion of the valence loss function below 0.5 keV is a few percent); above 22.5 keV and
  89 eV the tables end and L = 0 (every rate of this script lies inside them unless printed otherwise); threshold E_g =
  1.11 eV; T = 0.
Outputs: tex/figures/ch10/fig10_8.pdf, tex/figures/ch10/limit10_9a.pdf, and every number of the text and of WE 10.9.
"""
import os
import sys
import numpy as np
from scipy.interpolate import RegularGridInterpolator
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rate10_2 as R

OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch10")
D = R.load()
OM, QQ = D["omega"], D["q"]
WTOP, QTOP = OM[-1], QQ[-1]


def make_interp(key):
    tab = D[key]                                   # (n_omega, n_q)
    f = RegularGridInterpolator((OM, QQ), tab, bounds_error=False, fill_value=0.0)

    def L(q, w):
        q = np.asarray(q, float)
        w = np.asarray(w, float)
        qc = np.clip(q, QQ[0], None)              # hold the first bin below 493 eV
        val = f(np.stack(np.broadcast_arrays(w, qc), axis=-1))
        return np.where((q <= QTOP) & (w <= WTOP), val, 0.0)
    return L


LF = make_interp("lf")
IP = make_interp("ip")


def fdm2(q, light):
    return (R.Q0 / q)**4 if light else np.ones_like(q)


def mu(m):
    return m * R.ME / (m + R.ME)


def q_window(m, w, delta, vmax=R.VMAX):
    """momenta with v_min(q, w) <= vmax: q^2/2m + (w + delta) in [-q vmax, q vmax]."""
    a = w + delta
    disc_hi = (m * vmax)**2 - 2 * m * a          # roots of q^2/2m - q vmax + a = 0
    if disc_hi < 0:
        return None
    if a <= 0:
        lo = -m * vmax + np.sqrt((m * vmax)**2 - 2 * m * a)
        hi = m * vmax + np.sqrt((m * vmax)**2 - 2 * m * a)
    else:
        lo = m * vmax - np.sqrt(disc_hi)
        hi = m * vmax + np.sqrt(disc_hi)
    return max(lo, 1e-3), hi


def spectrum(m, delta, L=LF, light=False, wgrid=None, nq=1500):
    """dR/domega [events kg^-1 yr^-1 eV^-1] at sigma_e = 1e-37 cm^2, full |v_min| kernel (eq:10.9-inel)."""
    if wgrid is None:
        wgrid = np.arange(R.EG, min(WTOP, m * R.VMAX**2 / 2 - delta) + 1e-9, 0.02)
    out = np.zeros_like(wgrid)
    for i, w in enumerate(wgrid):
        win = q_window(m, w, delta)
        if win is None:
            continue
        lo, hi = win
        q = np.geomspace(lo, hi, nq)
        vmin = np.abs((w + delta) / q + q / (2 * m))
        integrand = q**3 * R.eta(vmin) * fdm2(q, light) * L(q, w)
        out[i] = np.trapezoid(integrand, q)
    pre = R.RHO_CHI * R.SIGMA_REF / (8 * np.pi**2 * R.ALPHA * R.RHO_T * m * mu(m)**2)
    return wgrid, R.to_per_kg_yr(pre * out)


def shell(m, delta, wgrid, L=LF, light=False):
    """halo-independent exothermic shell form (eq:10.9-shell)."""
    qd = np.sqrt(np.clip(2 * m * (-delta - wgrid), 0, None))
    val = np.where(qd > 0, qd**3 * fdm2(np.maximum(qd, 1e-9), light) * L(qd, wgrid), 0.0)
    pre = R.RHO_CHI * R.SIGMA_REF / (4 * np.pi**2 * R.ALPHA * R.RHO_T * mu(m)**2)
    return R.to_per_kg_yr(pre * val)


def total(w, s, wth=R.EG):
    s = np.where(w >= wth, s, 0.0)
    return np.trapezoid(s, w)


def peak(w, s):
    return w[np.argmax(s)]


def main():
    plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
    print("v_max = %.4e" % R.VMAX)

    # ---------------- Fig. 10.8: three splittings at 10 MeV --------------------------------------------------------
    m = 10e6
    fig, axs = plt.subplots(1, 2, figsize=(6.3, 2.8))
    for ax, light, tag in ((axs[0], False, "heavy"), (axs[1], True, "light")):
        for delta, col, ls in ((10.0, "C0", "--"), (0.0, "k", "-"), (-10.0, "C3", "-")):
            w, s = spectrum(m, delta, light=light)
            Rt = total(w, s)
            print("10 MeV %s, Delta = %+5.1f eV: total %.3e /kg/yr, peak %.2f eV, mean %.2f eV, max omega %.1f eV"
                  % (tag, delta, Rt, peak(w, s), np.trapezoid(w * s, w) / Rt, w[-1]))
            ax.plot(w, s, color=col, ls=ls, lw=1.3, label=r"$\Delta_\chi = %+d$ eV" % delta if delta else r"$\Delta_\chi = 0$")
            if delta < 0:
                qd = np.sqrt(2 * m * (-delta - w[w < -delta]))
                print("   q_Delta range %.2f - %.2f keV; v_Delta at omega = 5 eV: %.2e (v_max/v_Delta = %.2f)"
                      % (qd.min() / 1e3, qd.max() / 1e3, np.sqrt(2 * 5 / m), R.VMAX / np.sqrt(2 * 5 / m)))
        ax.set_xlim(0, 46)
        ax.set_yscale("log")
        ax.set_xlabel(r"$\omega$ [eV]")
        ax.axvline(R.EG, color="0.5", lw=0.6, ls=":")
        ax.set_title("(a) heavy mediator" if not light else "(b) light mediator", fontsize=9)
    axs[0].set_ylim(1e0, 3e5)
    axs[1].set_ylim(1e-1, 3e5)
    axs[0].set_ylabel(r"$d\mathcal{R}/d\omega$ [kg$^{-1}$ yr$^{-1}$ eV$^{-1}$]")
    axs[0].legend(frameon=False, fontsize=7.5, loc="upper right")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig10_8.pdf"))
    plt.close(fig)

    # ---------------- WE 10.9: Delta = -10 eV, line positions -----------------------------------------------------
    delta = -10.0
    print("\nWE 10.9, Delta = -10 eV, RPA + LF:")
    for m in (0.1e6, 0.3e6, 1e6, 3e6):
        vD_line = None
        wl = mu(m) * (-delta) / R.ME
        qline = np.sqrt(2 * mu(m) * (-delta))
        for light in (False, True):
            w, s = spectrum(m, delta, light=light)
            sh = shell(m, delta, w, light=light)
            Rt, Rs = total(w, s), total(w, sh)
            pk = peak(w, s)
            # half maximum width (heavy only)
            above = w[s >= 0.5 * s.max()]
            frac_top = total(w, np.where(w >= -delta - 0.5, s, 0)) / Rt
            print("  m = %.1f MeV %s: free-electron line %.2f eV (q = %.2f keV); peak %.2f eV, FWHM %.2f-%.2f eV;"
                  " total %.3e /kg/yr, shell/full %.3f; v_max/v_Delta(peak) = %.2f; max omega %.2f eV;"
                  " fraction in last 0.5 eV below |Delta| %.2f"
                  % (m / 1e6, "light" if light else "heavy", wl, qline / 1e3, pk, above.min(), above.max(), Rt,
                     Rs / Rt, R.VMAX / (np.sqrt(2 * m * max(-delta - pk, 1e-3)) / m), w[-1], frac_top))
            if light is False:
                qpk = np.sqrt(2 * m * (-delta - pk))
                print("      q_Delta at the peak = %.2f keV = %.2f q0" % (qpk / 1e3, qpk / R.Q0))
    # optical loss function at 10 eV (first bin) and measured value from Sect. 10.7 (0.2467)
    print("  table L(first bin, 10 eV) = %.4f (measured q -> 0: 0.2467, Sect. 10.7)" % LF(np.array([400.0]), np.array([10.0]))[0])
    # endothermic reach
    for dl in (1.0, 10.0):
        mmin = 2 * (dl + R.EG) / R.VMAX**2
        print("  endothermic Delta = %+.0f eV needs m >= 2(Delta + E_g)/v_max^2 = %.2f MeV" % (dl, mmin / 1e6))

    # ---------------- Limit 10.9a: IP vs RPA+LF against Delta at 1 MeV -------------------------------------------
    m = 1e6
    deltas = np.concatenate([np.arange(-85, -10, 2.5), np.arange(-10, 2.4, 0.5), [2.3]])
    r_ip, r_lf, r_ip_l, r_lf_l = [], [], [], []
    for dl in deltas:
        w, s1 = spectrum(m, dl, L=IP, nq=600)
        _, s2 = spectrum(m, dl, L=LF, nq=600)
        _, s3 = spectrum(m, dl, L=IP, light=True, nq=600)
        _, s4 = spectrum(m, dl, L=LF, light=True, nq=600)
        r_ip.append(total(w, s1)); r_lf.append(total(w, s2))
        r_ip_l.append(total(w, s3)); r_lf_l.append(total(w, s4))
    r_ip, r_lf, r_ip_l, r_lf_l = map(np.array, (r_ip, r_lf, r_ip_l, r_lf_l))
    ratio, ratio_l = r_ip / r_lf, r_ip_l / r_lf_l
    print("\nLimit 10.9a, m = 1 MeV: Delta, IP, RPA+LF, IP/LF heavy, IP/LF light")
    for dl, a, b, c, d in zip(deltas, r_ip, r_lf, ratio, ratio_l):
        if dl in (-85, -80, -70, -60, -50, -40, -35, -30, -25, -20, -15, -10, -5, -2, -1, 0, 1, 2, 2.3):
            print("   %+6.1f  %.3e  %.3e  %.3f  %.3f" % (dl, a, b, c, d))
    ok = np.abs(ratio - 1) < 0.10
    okl = np.abs(ratio_l - 1) < 0.10
    print("  heavy: within 10%% for Delta in %s" % (deltas[ok] if ok.any() else "none"))
    print("  light: within 10%% for Delta in %s" % (deltas[okl] if okl.any() else "none"))
    print("  heavy ratio min %.3f at Delta = %.1f; light min %.3f at %.1f"
          % (ratio.min(), deltas[np.argmin(ratio)], ratio_l.min(), deltas[np.argmin(ratio_l)]))

    fig, ax = plt.subplots(figsize=(4.6, 2.9))
    for i in range(len(deltas)):
        if ok[i]:
            lo = deltas[i] - 1.25 if deltas[i] < -10 else deltas[i] - 0.25
            hi = deltas[i] + 1.25 if deltas[i] < -10 else deltas[i] + 0.25
            ax.axvspan(lo, min(hi, deltas[ok].max()), color="0.9", lw=0)   # shade ends at the last passing splitting
    ax.plot(deltas, ratio, color="C3", lw=1.5, label="heavy mediator")
    ax.plot(deltas, ratio_l, color="C3", lw=1.2, ls="--", label="light mediator")
    ax.axhline(1, color="k", lw=0.8)
    ax.axhline(1.1, color="0.5", lw=0.5, ls=":")
    ax.axvline(0, color="0.5", lw=0.5, ls=":")
    ax.set_yscale("log")
    ax.set_xlabel(r"$\Delta_\chi$ [eV]")
    ax.set_ylabel(r"$\mathcal{R}_{\rm IP}/\mathcal{R}_{\rm RPA+LF}$")
    ax.set_xlim(-86, 3)
    ax.legend(frameon=False, fontsize=7.5, loc="upper left")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "limit10_9a.pdf"))
    plt.close(fig)


if __name__ == "__main__":
    main()
