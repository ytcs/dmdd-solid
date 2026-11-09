"""Limit Check 16.6a (lim:16.6a, fig:16-limit-cc): the published color-center and bond-breaking rates as limits of the
final-state-resolved rate of Sect. 16.6.

Panel 1, color-center creation (fluorine recoil in LiF).  Published form (Budnik et al., arXiv:1705.03016, Eqs. (1), (5),
(7)): free nuclear recoil times a step Theta(E_R - E_d).  Fuller result: the impulse response of the bound nucleus
(eq. 11.4-IAgauss, Gaussian of width sigma^2 = E_R <omega>_F at T = 0) inserted in the master rate, with the step applied
to the energy the nucleus takes up, omega:
    R_free = int dq q eta(q / 2 mu) Theta(q^2/2M - E_d)
    R_IA   = int dq q int d(delta) G(delta; sigma(q)) eta((E_R + delta)/q + q/2m) Theta(E_R + delta - E_d)
(heavy mediator, F_N = 1, isotropic crystal: common prefactors cancel in the ratio).  Plotted: R_IA / R_free against
x = E_R^max / E_d, E_R^max = 2 mu^2 v_max^2 / M (eq. 1.3-ERmax), for <omega>_F = 77.2 meV (the top of the LiF optical band,
an upper value) and 33.5 meV (its bottom).  Dotted: the direction-dependent threshold of Budnik et al. Eq. (2) with a = 0.4
(E_d(r) = E_d (1 + a sin 4theta cos 4phi)^2, recoil directions isotropic in the crystal frame), divided by the step at E_d.
E_d = 27 eV (Cogswell et al. Table I).

Panel 2, bond breaking (H2 in a free-rotor molecular solid, para-hydrogen).  Published classical form (Essig et al.,
arXiv:1608.02940, Eqs. (3.3), (4.3)): free recoil of atom 1 with q >= q_min = (M1/mu12)(2 mu12 E_bond)^(1/2).
Fuller result: S_11 = S_CM (x) S_int at the reduced momentum p = (mu12/M1) q (eq. 16.6-conv), S_int in the impulse
approximation over the Gaussian radial ground state (their Eq. (3.12), sigma0^2 = 1/(mu12 omega_vib)), dissociation if the
internal energy change p.k/mu12 + p^2/2mu12 exceeds E_bond.  Also shown: the improved Born kinematics of their Eq. (3.17)
(|k + p|^2 / 2 mu12 > E_bond), which differs from the impulse form by the initial kinetic energy of the bond.  The bound
center of mass shifts v_min by (<omega>_CM / 4 M1)^(1/2) per unit of its Gaussian deviate, 2e-6 for <omega>_CM = 10 meV,
and is dropped (printed check).  x = (q_max / q_min)^2, q_max = 2 mu_chi1 v_max.
Shaded in each panel: ratio of the impulse curve (upper <omega>_F in panel 1) within 10 % of one.  Root-finder thresholds.
Run: python limit16_6a.py > limit16_6a.log  (about a minute)
"""
import os
import numpy as np
from scipy.optimize import brentq
from scipy.special import erfc
from numpy.polynomial.legendre import leggauss
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import cc16_6 as C

FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tex", "figures", "ch16")
os.makedirs(FIG, exist_ok=True)
GL_X, GL_W = leggauss(48)


def qint(f, a, b, n=600):
    """int_a^b f(q) dq on a log grid (trapezoid)."""
    if b <= a:
        return 0.0
    q = np.geomspace(a, b, n)
    return np.trapezoid(f(q), q)


# ---------------------------------------------------------------- panel 1 --------------------------------------------
M = C.M_F
ED = C.E_D_LIF


def r_free(m, Ed=ED):
    mu = C.mu(m, M)
    qd, qmax = np.sqrt(2 * M * Ed), 2 * mu * C.VMAX
    return qint(lambda q: q * C.eta(q / (2 * mu)), qd, qmax)


def r_ia(m, w, Ed=ED, exact_v=True):
    mu = C.mu(m, M)
    qmax = 2 * mu * C.VMAX
    qd = np.sqrt(2 * M * Ed)
    q = np.geomspace(0.7 * qd, qmax * 1.02, 900)
    ER = q**2 / (2 * M)
    sig = np.sqrt(ER * w)
    out = np.zeros_like(q)
    for i in range(len(q)):
        lo = max(Ed - ER[i], -9 * sig[i])
        hi = 9 * sig[i]
        if hi <= lo:
            continue
        d = 0.5 * (hi - lo) * GL_X + 0.5 * (hi + lo)
        wd = 0.5 * (hi - lo) * GL_W
        g = np.exp(-d**2 / (2 * sig[i]**2)) / np.sqrt(2 * np.pi * sig[i]**2)
        v = (ER[i] + d) / q[i] + q[i] / (2 * m) if exact_v else q[i] / (2 * mu) + 0 * d
        out[i] = q[i] * np.sum(wd * g * C.eta(v))
    return np.trapezoid(out, q)


def f_dir(E, Ed=ED, a=0.4, n=400):
    """Fraction of isotropic recoil directions with E_d (1 + a sin4t cos4p)^2 < E."""
    t = np.arccos(np.linspace(-1, 1, n))
    p = np.linspace(0, 2 * np.pi, 2 * n, endpoint=False)
    T, Pp = np.meshgrid(t, p, indexing="ij")
    thr = Ed * (1 + a * np.sin(4 * T) * np.cos(4 * Pp))**2
    thr = np.sort(thr.ravel())
    return np.searchsorted(thr, E) / thr.size


_FD_E = np.geomspace(0.3 * ED, 3 * ED, 400)
_FD_V = f_dir(_FD_E)


def r_dir(m):
    mu = C.mu(m, M)
    qmax = 2 * mu * C.VMAX
    fd = lambda q: np.interp(q**2 / (2 * M), _FD_E, _FD_V, left=0.0, right=1.0)
    return qint(lambda q: q * C.eta(q / (2 * mu)) * fd(q), np.sqrt(2 * M * 0.3 * ED), qmax, n=1500)


def m_of_x(x, Mt=M, Eth=ED):
    return C.m_threshold(x * Eth, Mt)


# ---------------------------------------------------------------- panel 2 --------------------------------------------
M1 = C.M_H
MU12 = M1 / 2
EB = C.E_B_H2
KG, KW, NORM, S0 = C.bond_kgrid(MU12, C.W_H2, C.R_H2)
QMIN_H2 = (M1 / MU12) * np.sqrt(2 * MU12 * EB)


def pd_ia(q):
    """IA dissociation probability, closed form over the isotropic direction: P(k_z > a) = sum w_k clip((k - a)/2k)."""
    p = MU12 / M1 * q
    a = MU12 * (EB - p**2 / (2 * MU12)) / p
    return float(np.sum(KW * np.clip((KG - a) / (2 * KG), 0, 1)))


def pd_born(q):
    p = MU12 / M1 * q
    u0 = (2 * MU12 * EB - KG**2 - p**2) / (2 * p * KG)
    return float(np.sum(KW * np.clip((1 - u0) / 2, 0, 1)))


def r2(m, mode):
    mu1 = C.mu(m, M1)
    qmax = 2 * mu1 * C.VMAX
    if mode == "cl":
        return qint(lambda q: q * C.eta(q / (2 * mu1)), QMIN_H2, qmax)
    f = pd_ia if mode == "IA" else pd_born
    q = np.geomspace(0.5 * QMIN_H2, qmax, 700)
    return np.trapezoid(q * C.eta(q / (2 * mu1)) * np.array([f(qq) for qq in q]), q)


def m2_of_x(x):
    """x = (q_max/q_min)^2 -> m: 2 mu_chi1 v_max = sqrt(x) q_min."""
    muv = np.sqrt(x) * QMIN_H2 / (2 * C.VMAX)
    return muv * M1 / (M1 - muv)


if __name__ == "__main__":
    print("== Panel 1: fluorine recoil in LiF, E_d = %.0f eV ==" % ED)
    print("q_d = sqrt(2 M E_d) = %.1f keV; m_min (E_R^max = E_d) = %.4f GeV" % (np.sqrt(2 * M * ED) / 1e3, m_of_x(1.0) / 1e9))
    for w in C.W_LIF:
        sig = np.sqrt(ED * w)
        dp = np.sqrt(M * w / 2)
        print("<omega>_F = %.1f meV: sigma at E_d = %.3f eV (%.2f %% of E_d); zero-point momentum per component sqrt(M<omega>/2) = "
              "%.1f keV = %.1f alpha m_e; / q_d = %.4f; v_min shift sigma/q = %.2e"
              % (w * 1e3, sig, 100 * sig / ED, dp / 1e3, dp / C.P.Q0, dp / np.sqrt(2 * M * ED), sig / np.sqrt(2 * M * ED)))
    m_t = m_of_x(1.5)
    print("check (x = 1.5): R_IA exact v_min / R_IA v_min = q/2mu: %.6f" % (r_ia(m_t, C.W_LIF[1]) / r_ia(m_t, C.W_LIF[1], exact_v=False)))
    print("check sigma -> 0 (w = 1e-9 eV), x = 2: R_IA/R_free = %.5f" % (r_ia(m_of_x(2.0), 1e-9) / r_free(m_of_x(2.0))))
    xs1 = np.concatenate([np.geomspace(1.003, 1.2, 30), np.geomspace(1.2, 30, 50)[1:]])
    rat = {w: [] for w in C.W_LIF}
    rdir = []
    for x in xs1:
        m = m_of_x(x)
        rf = r_free(m)
        for w in C.W_LIF:
            rat[w].append(r_ia(m, w) / rf)
        rdir.append(r_dir(m) / rf)
    for x, a, b, d in zip(xs1, rat[C.W_LIF[0]], rat[C.W_LIF[1]], rdir):
        if x in xs1[::6]:
            print("  x = %7.3f  m = %.4f GeV  IA/free (33.5 meV) = %.4f  (77.2 meV) = %.4f  directional/step = %.4f"
                  % (x, m_of_x(x) / 1e9, a, b, d))
    x10 = {}
    for w in C.W_LIF:
        x10[w] = brentq(lambda x: r_ia(m_of_x(x), w) / r_free(m_of_x(x)) - 1.10, 1.0005, 3.0, xtol=1e-5)
        x2 = brentq(lambda x: r_ia(m_of_x(x), w) / r_free(m_of_x(x)) - 1.02, 1.0005, 5.0, xtol=1e-5)
        print("<omega>_F = %.1f meV: IA within 10 %% for x >= %.4f (m >= %.4f GeV); within 2 %% for x >= %.4f (m >= %.4f GeV)"
              % (w * 1e3, x10[w], m_of_x(x10[w]) / 1e9, x2, m_of_x(x2) / 1e9))
    xd = brentq(lambda x: abs(r_dir(m_of_x(x)) / r_free(m_of_x(x)) - 1) - 0.10, 3.0, 30.0, xtol=1e-4)
    print("directional (a = 0.4) / step: within 10 %% of one for x >= %.3f (m >= %.4f GeV)" % (xd, m_of_x(xd) / 1e9))
    # rate below the classical threshold and shift of the rate curve
    m12 = m_of_x(1.1)
    rf12 = r_free(m12)
    for w in C.W_LIF:
        ms = brentq(lambda m: r_ia(m, w) - rf12, 0.9 * m12, m12, xtol=1e4)
        print("<omega>_F = %.1f meV: impulse rate equals the step rate at x = 1.1 (m = %.4f GeV) at m = %.4f GeV: ratio %.4f"
              % (w * 1e3, m12 / 1e9, ms / 1e9, ms / m12))
    m_b = m_of_x(0.95)
    print("x = 0.95 (m = %.4f GeV): R_IA(77.2 meV)/R_free(x = 1.1) = %.3e (step rate zero)" % (m_b / 1e9, r_ia(m_b, C.W_LIF[1]) / rf12))
    print("\n== Panel 2: H2 bond, E_bond = %.2f eV, omega_vib = %.4f eV, r_e = %.4f A ==" % (EB, C.W_H2, C.R_H2 * C.HBARC_EV_A))
    print("ground-state norm on the k grid = %.6f; sigma0 = %.4f A; radial momentum rms (mu omega/2)^1/2 = %.2f keV; "
          "<k_z^2>^1/2 = %.2f keV = %.2f alpha m_e" % (NORM, S0 * C.HBARC_EV_A, np.sqrt(MU12 * C.W_H2 / 2) / 1e3,
                                                     np.sqrt(np.sum(KW * KG**2) / 3) / 1e3, np.sqrt(np.sum(KW * KG**2) / 3) / C.P.Q0))
    print("q_min = %.2f keV; classical m_min = %.4f MeV" % (QMIN_H2 / 1e3, m2_of_x(1.0) / 1e6))
    print("initial kinetic energy <k^2>/2mu12 = %.4f eV (omega_vib/4 = %.4f)" % (np.sum(KW * KG**2) / (2 * MU12), C.W_H2 / 4))
    print("CM shift of v_min per unit deviate, <omega>_CM = 10 meV: %.2e (v_max = %.3e)" % (np.sqrt(0.01 / (4 * M1)), C.VMAX))
    print("internal shift of v_min per unit deviate (omega_vib/4M1)^1/2/sqrt(3): %.2e" % (np.sqrt(C.W_H2 / (4 * M1)) / np.sqrt(3)))
    xs2 = np.concatenate([np.geomspace(0.6, 1.2, 30), np.geomspace(1.2, 30, 45)[1:]])
    r_ia2, r_b2 = [], []
    for x in xs2:
        m = m2_of_x(x)
        rc = r2(m, "cl") if x > 1 else np.nan
        r_ia2.append(r2(m, "IA") / rc if x > 1 else np.nan)
        r_b2.append(r2(m, "Born") / rc if x > 1 else np.nan)
    for x, a, b in zip(xs2, r_ia2, r_b2):
        if x in xs2[::6]:
            print("  x = %7.3f  m = %.2f MeV  IA/classical = %.4f  Born/classical = %.4f" % (x, m2_of_x(x) / 1e6, a, b))
    x10b = brentq(lambda x: r2(m2_of_x(x), "IA") / r2(m2_of_x(x), "cl") - 1.10, 1.001, 10.0, xtol=1e-5)
    x10c = brentq(lambda x: r2(m2_of_x(x), "Born") / r2(m2_of_x(x), "cl") - 1.10, 1.001, 30.0, xtol=1e-5)
    print("IA within 10 %% of classical for x >= %.4f (m >= %.2f MeV); improved Born for x >= %.4f (m >= %.2f MeV)"
          % (x10b, m2_of_x(x10b) / 1e6, x10c, m2_of_x(x10c) / 1e6))
    # shift of the rate curve: mass at which the impulse (Born) rate equals the classical rate at x = 1.1
    m11 = m2_of_x(1.1)
    rc11 = r2(m11, "cl")
    for mode in ("IA", "Born"):
        ms = brentq(lambda m: r2(m, mode) - rc11, 0.6 * m11, m11, xtol=1e3)
        print("%s rate equals the classical rate at x = 1.1 (m = %.2f MeV) at m = %.2f MeV: mass ratio %.4f"
              % (mode, m11 / 1e6, ms / 1e6, ms / m11))
    for xx in (0.8, 0.9, 1.0):
        m = m2_of_x(xx)
        print("x = %.1f (m = %.2f MeV): R_IA / R_cl(x = 1.1) = %.3e, R_Born / R_cl(x = 1.1) = %.3e"
              % (xx, m / 1e6, r2(m, "IA") / rc11, r2(m, "Born") / rc11))
    print("source's Eq. (3.8) estimate 1 - Delta p/sqrt(2 mu12 E_b) with Delta p = <k_z^2>^1/2: %.4f"
          % (1 - np.sqrt(np.sum(KW * KG**2) / 3) / np.sqrt(2 * MU12 * EB)))
    for x in (1.0, 1.5):
        q = np.sqrt(x) * QMIN_H2
        print("P_diss at q = sqrt(%.1f) q_min: IA %.4f, Born %.4f" % (x, pd_ia(q), pd_born(q)))

    # ---------------------------------------------------------------- figure -----------------------------------------
    plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 2.9))
    a1.axvspan(x10[C.W_LIF[1]], 30, color="0.88", lw=0)
    a1.semilogx(xs1, rat[C.W_LIF[1]], color="C3", lw=1.5, label=r"impulse, $\langle\omega\rangle_{\mathrm{F}} = 77.2$ meV")
    a1.semilogx(xs1, rat[C.W_LIF[0]], color="C0", lw=1.5, label=r"impulse, $33.5$ meV")
    a1.semilogx(xs1, rdir, color="k", lw=1.0, ls=":", label=r"direction-dependent $E_{\mathrm{d}}$")
    a1.axhline(1.0, color="k", lw=0.6)
    a1.set_ylim(0.0, 2.5)
    a1.set_xlim(1.0, 30)
    a1.set_xlabel(r"$E_R^{\max}/E_{\mathrm{d}}$")
    a1.set_ylabel("rate / step-threshold rate")
    a1.set_title("(a) F recoil in LiF", fontsize=9)
    a1.legend(fontsize=7, frameon=False, loc="upper right", bbox_to_anchor=(1.0, 0.82))
    a2.axvspan(x10b, 30, color="0.88", lw=0)
    a2.semilogx(xs2, r_ia2, color="C3", lw=1.5, label="impulse (book)")
    a2.semilogx(xs2, r_b2, color="C2", lw=1.5, ls="--", label="improved Born")
    a2.axhline(1.0, color="k", lw=0.6)
    a2.set_ylim(0.0, 2.5)
    a2.set_xlim(1.0, 30)
    a2.set_xlabel(r"$(q_{\max}/q_{\min})^2$")
    a2.set_ylabel("rate / classical rate")
    a2.set_title(r"(b) H$_2$ bond", fontsize=9)
    a2.legend(fontsize=7, frameon=False, loc="upper right")
    fig.tight_layout()
    out = os.path.join(FIG, "limit16_6a.pdf")
    fig.savefig(out)
    print("wrote", out)
