"""Limit 11.4b (Sect. 11.4): fermionic absorption on nuclei, chi + N -> nu~ + N, in a silicon crystal.
Output: tex/figures/ch11/limit11_4b.pdf. Prints the validity boundaries and the line widths quoted in the text.

Literature form (dashed, one): rate per nucleus n A^2 F_N^2 sigma_F, sigma_F = m_chi^2/(4 pi Lambda_F^4) (Dror, Elor and McGehee,
  arXiv:1905.12635, Eqs. (1), (4); their sigma_NC), a free nucleus at rest, every absorption counted.
Crystal (solid, vector operator with continuity, eq:10.9-ferm): Gamma/(n A^2 F_N^2 sigma_F) = int domega s(m - omega, omega)
  over the excitations of the crystal, omega > 0. In the incoherent approximation at T = 0 (eq:11.3-inc) s carries the weight
  1 - e^{-2W(q)} (the zero-phonon weight needs |q| = |G| and does not enter at a generic mass), and the line integral of the
  free-recoil peak gives the Jacobian 1/(1 + q0/M) (eq:11.4-ferm-nuc).  Hence
      R_V(m) = [1 - e^{-2W(q0)}] / (1 + q0/M),   m = q0 + q0^2/2M,
  with 2W = q^2 <u_x^2>, <u_x^2> = 2.446e-3 A^2 (imp11.py, PBE DOS, T = 0).
Density row alone (dotted; the scalar operator, eq:10.9-ferm with q^2/m^2): R_S(m) = R_V(m) (q0/m)^2 -> 1 - 2m/M.
The nuclear form factor is divided out of both (the literature evaluates it at q = m_chi, the crystal at q0 = m_chi - E_R0;
  the Helm zero of Si lies at 256 MeV).
Gray band: R_V within 10 % of one. Coherence corrections (Sect. 11.3) are not included: they change the one-, two- and
  three-phonon weights by up to ~10 % below q ~ 7-18 keV.
Line widths: crystal x_R^{-1/2} = (2 M <omega>)^{1/2}/q0; halo rms of 2 v cos(theta) for an isotropic nu~ direction,
  2 (<v^2>/3)^{1/2}, <v^2> in the laboratory frame for the halo of Sect. 1.2 (Monte Carlo, 4e6 samples, seed 1).
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

MS = np.geomspace(3e3, 1e10, 600)                       # eV


def q0(m, M=I.M):
    return M * (np.sqrt(1 + 2 * m / M) - 1)


def r_vec(m):
    q = q0(m)
    return (1 - np.exp(-I.two_w(q))) / (1 + q / I.M)


def r_scal(m):
    q = q0(m)
    return r_vec(m) * (q / m)**2


if __name__ == "__main__":
    rv, rs = r_vec(MS), r_scal(MS)
    ok = np.abs(rv - 1) <= 0.10
    lo, hi = MS[ok].min(), MS[ok].max()
    print("vector, crystal/free within 10 %%: %.1f keV <= m_chi <= %.2f GeV" % (lo / 1e3, hi / 1e9))
    oks = np.abs(rs - 1) <= 0.10
    print("density row alone within 10 %% up to %.2f GeV" % (MS[oks].max() / 1e9))
    for m in (3e3, 10e3, 20e3, 30e3, 50e3, 60.5e3, 100e3, 1e6, 1e9, 2.6e9):
        print("m_chi = %10.4g keV: q0 = %.6g keV, 2W = %.3g, 1 - e^-2W = %.4f, R_V = %.4f, R_S = %.4f, 1 - m/M = %.4f, 1 - 2m/M = %.4f"
              % (m / 1e3, q0(m) / 1e3, I.two_w(q0(m)), 1 - np.exp(-I.two_w(q0(m))), r_vec(m), r_scal(m), 1 - m / I.M, 1 - 2 * m / I.M))
    # line widths
    rng = np.random.default_rng(1)
    n = 4_000_000
    v = rng.normal(0, P.V0 / np.sqrt(2), (n, 3))
    v = v[np.linalg.norm(v, axis=1) < P.VESC]
    v[:, 2] += P.VE                                        # lab frame: v_lab = v_gal + v_E (sign irrelevant for <v^2>)
    v2 = np.mean(np.sum(v**2, axis=1))
    halo = 2 * np.sqrt(v2 / 3) / P.C_KMS
    print("halo: lab <v^2>^(1/2) = %.1f km/s; rms relative shift of E_R0, 2 (<v^2>/3)^(1/2) = %.2e" % (np.sqrt(v2), halo))
    qx = np.sqrt(2 * I.M * I.W_MEAN)
    print("crystal relative width x_R^-1/2 = (2 M <w>)^1/2 / q0 = %.1f keV / q0; equal to the halo width at m_chi = %.0f MeV"
          % (qx / 1e3, qx / halo / 1e6))
    for m in (100e3, 1e6, 10e6, 100e6):
        xr = I.e_r(q0(m)) / I.W_MEAN
        print("   m_chi = %g MeV: E_R0 = %.4g eV, x_R = %.3g, relative width %.2e (halo %.2e)" % (m / 1e6, I.e_r(q0(m)), xr, xr**-0.5, halo))

    fig, ax = plt.subplots(figsize=(5.0, 3.3))
    ax.axvspan(lo, hi, color="0.88", lw=0)
    ax.axhline(1.0, color="k", ls="--", lw=1.0, label=r"free nucleus, $n A^2F_N^2\sigma_F$")
    ax.plot(MS, rv, color="C3", lw=1.5, label="crystal, vector operator")
    ax.plot(MS, rs, color="C0", lw=1.0, ls=":", label="crystal, density row alone")
    ax.set_xscale("log")
    ax.set_xlim(MS[0], MS[-1])
    ax.set_ylim(0, 1.15)
    ax.set_xticks([1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 1e10])
    ax.set_xticklabels(["10 keV", "100 keV", "1 MeV", "10 MeV", "100 MeV", "1 GeV", "10 GeV"], fontsize=7)
    ax.set_xlabel(r"$m_\chi$")
    ax.set_ylabel("absorption rate / free-nucleus rate")
    ax.legend(fontsize=7, frameon=False, loc="lower center")
    fig.tight_layout()
    outp = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "limit11_4b.pdf")
    fig.savefig(outp)
    print("wrote", os.path.normpath(outp))
