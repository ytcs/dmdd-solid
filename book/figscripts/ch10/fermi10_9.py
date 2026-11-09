"""Fermionic absorption on a bound electron (Sect. 10.9, Limit 10.9c): scalar and vector operators on a hydrogen-like
1s shell, with the vector operator in the continuity form of the text and in the free-vertex form of Dror et al.
(arXiv:2011.01940 Eq. (9)).  Natural units; energies in eV.

Rates per atom, in units of sigma_F = m_chi^2/(4 pi Lambda_F^4) (2011.01940 writes sigma_e), with q = m_chi - omega
(massless nu~, v -> 0, eq:8.1-omega-ferm) and S_at(q, omega) the dynamic structure factor of the shell per atom
(book normalization, S = 2 pi sum_f |<f|e^{iqr}|i>|^2 delta(omega - E_f + E_i), both spins):
  scalar                     d<sigma v>/domega = sigma_F q^2 S_at / (2 pi m^2)           (= 2011.01940 Eq. (10))
  vector, continuity (text)  d<sigma v>/domega = sigma_F S_at / (2 pi)  + transverse-current row (not computed)
  vector, free vertex        d<sigma v>/domega = sigma_F S_at r(q) / (2 pi),
       r = q [2 m_e m (2 m_e + m) - 2 m_e^2 q - q^2 (2 m_e + m)] / (2 m_e^2 m^2)     (2011.01940 Eq. (9) / continuity form)
  With S_at = pi |f_ion|^2 / (2 E_ej) (book eq:2.2-fion, both spins) these are 2011.01940 Eqs. (9), (10).
  Free electron at rest: every form -> N_e sigma_F (plus O(m^2/m_e^2)); the plot divides by N_e sigma_F.
Model (exact, non-relativistic): hydrogen-like 1s shell of nuclear charge Z_eff, two electrons, bound-free transitions
  only (bound-bound lines lie below the ionization threshold and are dropped).  Generalized oscillator strength per
  Rydberg of the reduced units (K = q a0/Z, kappa = p_ej a0/Z, E = 1 + kappa^2 in units of Z^2 Ry):
     df/dE = 2^7 E (K^2 + E/3) exp[-(2/kappa) arctan(2 kappa/(K^2 - kappa^2 + 1))]
             / {[(K + kappa)^2 + 1]^3 [(K - kappa)^2 + 1]^3 (1 - exp(-2 pi/kappa))},   arctan in (0, pi)
  and sum_f |<f|e^{iqr}|1s>|^2 per unit E = (K^2/E) df/dE.  Checks asserted below: the continuum oscillator strength
  at K -> 0 is 0.4350 (H 1s, the remainder going to the discrete lines), the continuum sum at K = 10 is 1 - 4e-9
  (Bethe sum rule), and two points agree to 1e-5 with a direct radial integration over Coulomb functions (run once,
  mpmath; not repeated here).
Silicon K shell: binding E_B = 1839 eV (Henke, Gullikson and Davis, At. Data Nucl. Data Tables 54, 181 (1993), Si K edge
  1838.9 eV); Z_eff = sqrt(E_B / 13.6057 eV) = 11.63 fixes the model binding to it.  m_e = 510998.95 eV.
Output: tex/figures/ch10/limit10_9c.pdf and the numbers quoted in Sect. 10.9.
"""
import os
import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch10")
ME = 510998.95
ALPHA = 1 / 137.035999084
RY = 13.605693
EB = 1839.0
ZEFF = np.sqrt(EB / RY)
P0 = ZEFF * ALPHA * ME                     # inverse Bohr radius of the shell, eV


def dfdE(K, k):
    x = K**2 - k**2 + 1
    at = np.arctan2(2 * k, x)
    E = 1 + k**2
    return 2**7 * E * (K**2 + E / 3) * np.exp(-2 / k * at) / (((K + k)**2 + 1)**3 * ((K - k)**2 + 1)**3
                                                             * (1 - np.exp(-2 * np.pi / k)))


def checks():
    s0 = quad(lambda k: dfdE(1e-4, k) * 2 * k, 1e-7, 400, limit=1000)[0]
    s10 = quad(lambda k: dfdE(10.0, k) * 2 * k, 1e-7, 400, limit=1000, points=[10.0])[0]
    print("continuum oscillator strength at K -> 0: %.4f (H 1s: 0.4350); continuum sum at K = 10: %.9f" % (s0, s10))
    assert abs(s0 - 0.4350) < 2e-4 and abs(s10 - 1) < 1e-6


def S_at(q, w, EB=EB):
    """structure factor of the shell per atom [eV^-1 x 2 pi], two electrons."""
    if w <= EB:
        return 0.0
    k = np.sqrt(w / EB - 1)
    K = q / (np.sqrt(EB / RY) * ALPHA * ME)
    E = 1 + k**2
    per_eV = (K**2 / E) * dfdE(K, k) / EB          # sum |<f|e^{iqr}|1s>|^2 per eV
    return 2 * np.pi * 2 * per_eV


def r_free(q, m):
    return q * (2 * ME * m * (2 * ME + m) - 2 * ME**2 * q - q**2 * (2 * ME + m)) / (2 * ME**2 * m**2)


def rates(m, EB=EB):
    """<sigma v>/(N_e sigma_F) for scalar, vector (continuity, density row), vector (free vertex)."""
    fs = lambda w: (m - w)**2 * S_at(m - w, w, EB) / (2 * np.pi * m**2)
    fv = lambda w: S_at(m - w, w, EB) / (2 * np.pi)
    ff = lambda w: S_at(m - w, w, EB) * r_free(m - w, m) / (2 * np.pi)
    wl = m**2 / (2 * ME)                    # free recoil, where the Bethe ridge sits for q >> P0
    pts = [p for p in (wl, EB * 1.01, EB * 2) if EB < p < m]
    out = []
    for f in (fs, fv, ff):
        out.append(quad(f, EB, m, limit=2000, points=pts or None)[0] / 2)
    # mean omega^2/m^2 over the vector spectrum
    num = quad(lambda w: fv(w) * w**2 / m**2, EB, m, limit=2000, points=pts or None)[0]
    return out, num / (2 * out[1])


def main():
    checks()
    print("Z_eff = %.3f, shell momentum Z alpha m_e = %.2f keV" % (ZEFF, P0 / 1e3))
    xs = np.geomspace(1.02, 100, 70)
    S, V, F, W2 = [], [], [], []
    for x in xs:
        (s, v, f), w2 = rates(x * EB)
        S.append(s); V.append(v); F.append(f); W2.append(w2)
    S, V, F, W2 = map(np.array, (S, V, F, W2))
    ratio = F / V
    for x in (1.1, 1.5, 2, 3, 5, 10, 20, 50, 100):
        (s, v, f), w2 = rates(x * EB)
        print("m = %6.1f E_B = %7.1f keV: scalar %.4f, vector continuity %.4f, free vertex %.4f, ratio %.4f, <w^2/m^2> %.4f,"
              " 1 - <w^2/m^2> = %.4f" % (x, x * EB / 1e3, s, v, f, f / v, w2, 1 - w2))
    ok = np.abs(ratio - 1) < 0.10
    xb = xs[ok].min()
    print("free-vertex form within 10%% of the continuity form for m >= %.2f E_B = %.2f keV" % (xb, xb * EB / 1e3))
    # xenon 1s in the same model: E_B = 33317.4 eV (2011.01940 Table I); best-fit vector mass 56.5 keV (2011.01940 Sect. II)
    for m in (56.5e3, 100e3):
        (s, v, f), w2 = rates(m, 33317.4)
        print("Xe 1s model (Z_eff = %.1f), m = %.1f keV: free vertex / continuity = %.3f, <w^2/m^2> = %.3f, (Z_eff alpha)^2 = %.3f"
              % (np.sqrt(33317.4 / RY), m / 1e3, f / v, w2, (np.sqrt(33317.4 / RY) * ALPHA)**2))

    plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
    fig, ax = plt.subplots(figsize=(4.6, 2.9))
    ax.axvspan(xb, 100, color="0.9", lw=0)
    ax.semilogx(xs, V, color="C3", lw=1.5, label="vector, continuity (density row)")
    ax.semilogx(xs, F, color="k", lw=1.2, ls="--", label="vector, free-electron vertex")
    ax.semilogx(xs, S, color="C0", lw=1.2, ls="-.", label="scalar")
    ax.axhline(1, color="0.5", lw=0.6, ls=":")
    ax.set_xlim(1, 100)
    ax.set_yscale("log")
    ax.set_ylim(1e-5, 2)
    ax.set_xlabel(r"$m_\chi/E_B$")
    ax.set_ylabel(r"$\langle\sigma v\rangle/(N_e\sigma_F)$")
    ax.legend(frameon=False, fontsize=7, loc="lower right")
    ax.axvline(1, color="0.5", lw=0.6, ls=":")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "limit10_9c.pdf"))
    plt.close(fig)


if __name__ == "__main__":
    main()
