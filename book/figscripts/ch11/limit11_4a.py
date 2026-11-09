"""Limit 11.4a (Sect. 11.4): free nuclear recoil with the Helm form factor as the impulse limit of the silicon response.
Output: tex/figures/ch11/limit11_4a.pdf. Prints the validity boundary and the numbers quoted in the box and the text.

Quantity: differential rate per unit mass of a heavy-mediator (F_DM = 1), spin-independent coupling, orientation-averaged
crystal, from eq:8.2-spectrum (one row, D = |V_N|^2, S = S_A) with the velocity integral done (eta(v_min)/2q per d^3q/(2pi)^3, Sect. 11.1):
  dR/domega  proportional to  (1/M) int dq q F_N(q)^2 s(q, omega) eta(omega/q + q/2 m_chi),
divided by the free-recoil (Lewin-Smith) rate at E_R = omega, which is the same expression with s = delta(omega - q^2/2M):
  F_N(q_w)^2 eta(q_w/2 mu_N),  q_w = (2 M omega)^(1/2).
  Fuller result (solid): s = incoherent T = 0 multiphonon response of Si from the PBE DOS (imp11.spectrum), all orders.
  Leading correction (dashed): s = Gaussian of the impulse approximation, mean E_R, variance E_R <omega> (eq:11.4-IAgauss),
  truncated at omega > 0.
  F_N: Helm (eq:2.2-helm), Lewin-Smith parameters, A = 28.0855. Halo of Sect. 1.2 (phon11.eta). x axis: x_R = omega/<omega>,
  <omega> = 40.9 meV. m_chi = 1 GeV (red) and 50 MeV (blue; free-recoil endpoint 2 mu^2 v_max^2/M at x_R = 32.8).
  Gray band: x_R where the 1-GeV ratio stays within 10 % of one from there up to the end of the plot.
Grid: adaptive q grid, d ln q = min(0.01, 1/(10 x_R(q)^(1/2))); each spectrum on its own omega grid (spacing max(0.1 meV,
  sigma/60)), interpolated linearly to the 140 target energies. Checked: halving d ln q changes the ratio by < 1e-3.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import imp11 as I  # noqa: E402
import phon11 as P  # noqa: E402

A = 28.0855
XR = np.geomspace(0.3, 2000, 140)
OM = XR * I.W_MEAN
QW = np.sqrt(2 * I.M * OM)


def qgrid(fine=1.0):
    qs = [2e3]
    qtop = np.sqrt(2 * I.M * (OM[-1] + 12 * np.sqrt(OM[-1] * I.W_MEAN)))
    while qs[-1] < qtop:
        xr = I.e_r(qs[-1]) / I.W_MEAN
        qs.append(qs[-1] * np.exp(min(0.01, 1 / (10 * np.sqrt(xr))) / fine))
    return np.array(qs)


def spectra(qs):
    S = np.zeros((len(qs), len(OM)))
    SG = np.zeros_like(S)
    for i, q in enumerate(qs):
        w, s, _ = I.spectrum(q)
        S[i] = np.interp(OM, w, s, left=0, right=0)
        SG[i] = I.gauss(OM, q)
    return S, SG


def ratios(qs, S, SG, mchi):
    mu = mchi * I.M / (mchi + I.M)
    F2 = I.helm(qs, A)[0]**2
    vmin = OM[None, :] / qs[:, None] + qs[:, None] / (2 * mchi)
    ker = (qs * F2)[:, None] * P.eta(vmin)
    num = np.trapezoid(ker * S, qs, axis=0) / I.M
    numG = np.trapezoid(ker * SG, qs, axis=0) / I.M
    den = I.helm(QW, A)[0]**2 * P.eta(QW / (2 * mu))
    with np.errstate(divide="ignore", invalid="ignore"):
        return num / den, numG / den, den


if __name__ == "__main__":
    qs = qgrid()
    cache = os.path.join(HERE, "limit11_4a_spectra.npz")
    if os.path.exists(cache) and len(np.load(cache)["qs"]) == len(qs):
        c = np.load(cache)
        S, SG = c["S"], c["SG"]
    else:
        S, SG = spectra(qs)
        np.savez_compressed(cache, qs=qs, S=S, SG=SG)
    print("q grid: %d points, %.1f keV to %.0f keV" % (len(qs), qs[0] / 1e3, qs[-1] / 1e3))
    out = {}
    for m in (1e9, 50e6):
        r, rg, den = ratios(qs, S, SG, m)
        out[m] = (r, rg, den)
        mu = m * I.M / (m + I.M)
        emax = 2 * mu**2 * I.VMAX**2 / I.M
        print("m_chi = %g MeV: free endpoint E_max = %.3f eV, x_R = %.1f" % (m / 1e6, emax, emax / I.W_MEAN))
        for x in (0.5, 1, 2, 3, 4, 6, 9, 15, 30, 100, 1000):
            j = np.argmin(np.abs(XR - x))
            print("   x_R = %7.1f: crystal/free = %.4f, impulse Gaussian/free = %.4f" % (XR[j], r[j], rg[j]))
    r1 = out[1e9][0]
    bad = np.where(np.abs(r1 - 1) > 0.10)[0]
    xb = XR[bad.max() + 1]
    bad5 = np.where(np.abs(r1 - 1) > 0.05)[0]
    bad2 = np.where(np.abs(r1 - 1) > 0.02)[0]
    print("1 GeV: within 10 %% for x_R >= %.2f (q = %.1f keV, E_R = %.0f meV); 5 %% from x_R = %.2f; 2 %% from x_R = %.2f"
          % (xb, I.onset(xb, I.M, I.W_MEAN) / 1e3, xb * I.W_MEAN * 1e3, XR[bad5.max() + 1], XR[bad2.max() + 1]))
    rg1 = out[1e9][1]
    badg = np.where(np.abs(rg1 / r1 - 1) > 0.10)[0]
    print("1 GeV: impulse Gaussian within 10 %% of the crystal for x_R >= %.2f" % XR[badg.max() + 1])
    # 50 MeV near its endpoint: where the free form leaves the 10 % band, in units of the impulse width
    r50, rg50, den50 = out[50e6]
    mu50 = 50e6 * I.M / (50e6 + I.M)
    emax = 2 * mu50**2 * I.VMAX**2 / I.M
    j = np.where((OM < emax) & (np.abs(r50 - 1) > 0.10) & (XR > 10))[0].min()
    print("50 MeV: free form exceeds the 10 %% band from x_R = %.1f, (E_max - omega)/sigma = %.2f; crystal/Gaussian there %.3f; "
          "rate ratio between x_R = 2.3 and 10: %.3f-%.3f (Gaussian %.3f-%.3f)"
          % (XR[j], (emax - OM[j]) / np.sqrt(OM[j] * I.W_MEAN), r50[j] / rg50[j],
             r50[(XR > 2.3) & (XR < 10)].min(), r50[(XR > 2.3) & (XR < 10)].max(),
             rg50[(XR > 2.3) & (XR < 10)].min(), rg50[(XR > 2.3) & (XR < 10)].max()))
    for m in (1e9, 50e6):
        r, rg, den = out[m]
        mu_ = m * I.M / (m + I.M)
        below = OM < 0.75 * 2 * mu_**2 * I.VMAX**2 / I.M   # up to three quarters of the free endpoint
        d = np.abs(rg / r - 1)
        for tol in (0.10, 0.05):
            badi = np.where(below & (d > tol))[0]
            print("m_chi = %g MeV: impulse Gaussian within %.0f %% of the crystal from x_R = %.2f up to 3/4 of the free endpoint"
                  % (m / 1e6, 100 * tol, XR[badi.max() + 1]))
    sel = (XR > 3) & (XR < 8)
    print("50 MeV, 3 < x_R < 8: crystal/free %.3f-%.3f" % (r50[sel].min(), r50[sel].max()))
    # convergence check (run with CONV=1; result kept in the log of the first run: max |delta ratio| = 3.0e-03)
    if os.environ.get("CONV"):
        qs2 = qgrid(2.0)
        S2, SG2 = spectra(qs2)
        r2 = ratios(qs2, S2, SG2, 1e9)[0]
        print("convergence (d ln q halved): max |delta ratio| = %.1e" % np.nanmax(np.abs(r2 - r1)))

    fig, ax = plt.subplots(figsize=(5.0, 3.3))
    ax.axvspan(xb, XR[-1], color="0.88", lw=0)
    ax.axhline(1.0, color="k", ls="--", lw=1.0, label="free nuclear recoil (Helm)")
    for m, c, lab, z in ((1e9, "C3", r"$m_\chi = 1$ GeV", 3), (50e6, "C0", r"$m_\chi = 50$ MeV", 2)):
        r, rg, den = out[m]
        ok = den > 0
        ax.plot(XR[ok], r[ok], color=c, lw=1.5, label=lab + ", multiphonon", zorder=z)
        ax.plot(XR[ok], rg[ok], color=c, lw=1.0, ls=":", label=lab + ", impulse Gaussian", zorder=z)
    ax.axvline(emax / I.W_MEAN, color="C0", lw=0.8, ls="-.")
    ax.set_xscale("log")
    ax.set_xlim(XR[0], XR[-1])
    ax.set_ylim(0.0, 2.0)
    ax.set_xlabel(r"$x_R = \omega/\langle\omega\rangle$")
    ax.set_ylabel("crystal rate / free-recoil rate")
    ax.legend(fontsize=6.5, frameon=False, loc="upper right")
    fig.tight_layout()
    outp = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "limit11_4a.pdf")
    fig.savefig(outp)
    print("wrote", os.path.normpath(outp))
