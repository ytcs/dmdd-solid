"""Charge transport and the measured charge (Sect. 20.1): shared functions, every number printed in Sect. 20.1 that
is not a Limit Check value, and Fig. 20.1 (fig:20-hecht).  Log: charge20_1.log.
Run: python charge20_1.py > charge20_1.log   (about 20 s).

Model (all derived in Sect. 20.1):
  planar detector of thickness d (lengths in units of d), uniform field; a pair born at depth z (0 = hole-collecting
  electrode, 1 = electron-collecting electrode); each carrier survives a drift path s with probability exp(-s/lambda)
  (exponential trapping, drift length lambda_d per carrier type); Ramo's theorem with the planar weighting potential
  phi = z gives the induced charge per pair (units of e)
      q = s_e + s_h,   s_e = min(X_e, 1 - z),  s_h = min(X_h, z),  X ~ Exp(lambda).
  Moments: E[min(X, L)] = lam (1 - exp(-L/lam));  E[min(X, L)^2] = 2 lam^2 [1 - exp(-L/lam)(1 + L/lam)].
  Hecht relation (charge generated at one face, one carrier crosses the whole gap): lam (1 - exp(-1/lam)).
  Measured-charge Fano factor (eq:20.1-Fpos), with mean qbar(z), variance var(z) over the event-position law:
      F_meas = [F_eh <qbar^2> + <var>] / <qbar>  +  Nbar Var_z(qbar) / <qbar>.
Inputs (book values): F_eh = 0.114 (Sect. 18.2, 18.4), eps_eh = 3.75 eV (Sect. 18.4); Si static dielectric constant at
liquid-helium temperature 11.4 (Sect. 7.4, NOTATION eps_0 row); CODATA e, eps0_SI, alpha, m_e c^2.
Luke-emission constants quoted from Leman, arXiv:1109.1193, Table II: Si holes m = 0.5 m_e, Xi = 5.0 eV;
Si electrons (Herring-Vogt space) m_c = 0.26 m_e, Xi = 9.0 eV; v_L = 9.0 km/s; rho = 2.335 g/cm^3; l0 printed 7.5 / 16.9 um.
"""
import os
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch20")
os.makedirs(FIG, exist_ok=True)

F_EH = 0.114          # Sect. 18.2/18.4 cascade value, silicon
EPS_EH = 3.75         # eV, Sect. 18.4
EPS_SI_STATIC = 11.4  # liquid-helium value, Sect. 7.4
E_CH = 1.602176634e-19
EPS0_SI = 8.8541878128e-12
HBAR = 1.054571817e-34
ME = 9.1093837015e-31
KB_EV = 8.617333262e-5
HBARC_EVNM = 197.3269804
ALPHA = 1 / 137.035999


# ---------------------------------------------------------------- transport functions
def mean_min(lam, L):
    return lam * (1 - np.exp(-L / lam))


def m2_min(lam, L):
    a = L / lam
    return 2 * lam**2 * (1 - np.exp(-a) * (1 + a))


def hecht_face(lam):
    """Hecht relation: collected fraction for charge generated at one face, drift length lam (units of d)."""
    return lam * (1 - np.exp(-1 / lam))


def qbar(z, le, lh):
    return mean_min(le, 1 - z) + mean_min(lh, z)


def qvar(z, le, lh):
    return (m2_min(le, 1 - z) - mean_min(le, 1 - z) ** 2) + (m2_min(lh, z) - mean_min(lh, z) ** 2)


def qbar_uniform(le, lh):
    """Depth average of qbar for a uniform event position (closed form)."""
    return sum(l * (1 - l * (1 - np.exp(-1 / l))) for l in (le, lh))


def moments_uniform(le, lh):
    m1 = quad(lambda z: qbar(z, le, lh), 0, 1, epsabs=1e-13)[0]
    m2 = quad(lambda z: qbar(z, le, lh) ** 2, 0, 1, epsabs=1e-13)[0]
    v = quad(lambda z: qvar(z, le, lh), 0, 1, epsabs=1e-13)[0]
    return m1, m2, v


def fmeas_uniform(F, N, le, lh):
    m1, m2, v = moments_uniform(le, lh)
    return (F * m2 + v) / m1 + N * (m2 - m1**2) / m1, (F * m2 + v) / m1, N * (m2 - m1**2) / m1, m1


def fmeas_fixed(F, z, le, lh):
    m, v = qbar(z, le, lh), qvar(z, le, lh)
    return (F * m**2 + v) / m, m


def thin(F, f):
    return f * F + 1 - f


def rk_printed(F, f):
    """Ramanathan-Kurinsky arXiv:2004.10709 Eqs. (A6)-(A7) as printed: F/eta + (1 - eta)."""
    return F / f + 1 - f


def lam_for_midplane(m_target):
    """Equal drift lengths, pair at mid-plane: qbar = 2 lam (1 - exp(-1/(2 lam)))."""
    return brentq(lambda l: qbar(0.5, l, l) - m_target, 1e-3, 1e4, xtol=1e-14)


def lam_for_uniform(m_target, ratio=1.0):
    return brentq(lambda l: qbar_uniform(l, ratio * l) - m_target, 1e-3, 1e5, xtol=1e-14)


if __name__ == "__main__":
    print("=== Hecht relation and depth averages (units of d) ===")
    for lam in [0.1, 0.3, 1.0, 3.0, 10.0]:
        print("lam_d/d = %5.1f: Hecht (face) %.4f; pair at mid-plane %.4f; uniform depth, equal lam %.4f; "
              "uniform, lam_h = lam_e/3 %.4f"
              % (lam, hecht_face(lam), qbar(0.5, lam, lam), qbar_uniform(lam, lam), qbar_uniform(lam, lam / 3)))
    # large-lambda expansions
    for lam in [10.0, 100.0]:
        print("lam = %g: Hecht %.6f vs 1 - 1/(2 lam) = %.6f; uniform %.6f vs 1 - 1/(3 lam) = %.6f"
              % (lam, hecht_face(lam), 1 - 1 / (2 * lam), qbar_uniform(lam, lam), 1 - 1 / (3 * lam)))
    m1n, m2n, vn = moments_uniform(4.0, 4.0)
    print("closed-form vs quadrature <qbar> at lam = 4: %.12f %.12f" % (qbar_uniform(4.0, 4.0), m1n))

    print("\n=== Monte Carlo check of the measured-charge Fano factor (eq:20.1-Fpos) ===")
    rng = np.random.default_rng(20201)
    nev = 400000
    ntr, p = 30, 1 - F_EH          # binomial pair number: mean 30*0.886 = 26.58, Fano 0.114
    Nbar = ntr * p
    for (le, lh, label) in [(4.0, 4.0, "equal"), (6.0, 2.0, "unequal")]:
        Nk = rng.binomial(ntr, p, size=nev)
        z = rng.random(nev)
        Q = np.zeros(nev)
        tot = Nk.sum()
        idx = np.repeat(np.arange(nev), Nk)
        zz = z[idx]
        se = np.minimum(rng.exponential(le, tot), 1 - zz)
        sh = np.minimum(rng.exponential(lh, tot), zz)
        np.add.at(Q, idx, se + sh)
        Fmc = Q.var() / Q.mean()
        Fan, a, b, m1 = fmeas_uniform(F_EH, Nbar, le, lh)
        print("lam_e = %.0f, lam_h = %.0f (%s): MC F_meas = %.4f +- %.4f, formula %.4f (cascade+partial %.4f, position %.4f);"
              " MC <q>/N = %.5f, formula %.5f"
              % (le, lh, label, Fmc, Fmc * np.sqrt(2 / nev) * 1.5, Fan, a, b, Q.mean() / Nbar, m1))
    # fixed position, Bernoulli limit check
    Nk = rng.binomial(ntr, p, size=nev)
    kept = rng.binomial(Nk, 0.95)
    print("Bernoulli thinning MC at f = 0.95: %.4f, exact f F + 1 - f = %.4f" % (kept.var() / kept.mean(), thin(F_EH, 0.95)))

    print("\n=== Worked example: 95 %% collection in silicon, F_eh = %.3f ===" % F_EH)
    f = 0.95
    print("binomial thinning: %.4f" % thin(F_EH, f))
    print("Ramanathan-Kurinsky printed form F/f + 1 - f: %.4f (difference F(1/f - f) = %.4f)"
          % (rk_printed(F_EH, f), F_EH * (1 / f - f)))
    lm = lam_for_midplane(f)
    Fm, mm = fmeas_fixed(F_EH, 0.5, lm, lm)
    vmid = qvar(0.5, lm, lm)
    print("pair at mid-plane, equal drift lengths: lam_d/d = %.4f gives qbar = %.4f; var(q) = %.5f against the "
          "Bernoulli f(1-f) = %.5f; F_meas = %.4f" % (lm, mm, vmid, f * (1 - f), Fm))
    lu = lam_for_uniform(f)
    print("uniform depth, equal drift lengths: lam_d/d = %.4f gives <qbar> = %.4f" % (lu, qbar_uniform(lu, lu)))
    for om in [100.0, 1000.0, 5900.0]:
        N = om / EPS_EH
        Ft, a, b, m1 = fmeas_uniform(F_EH, N, lu, lu)
        print("  omega = %6.0f eV, N = %7.1f: F_meas = %.4f = %.4f (cascade + partial charge) + %.4f (position)"
              % (om, N, Ft, a, b))
    m1, m2, v = moments_uniform(lu, lu)
    print("  Var_z(qbar) = %.3e, <var> = %.4e, <qbar^2> = %.5f" % (m2 - m1**2, v, m2))
    # depth spread needed for the position term to equal the thinning excess
    print("  position term equals 0.01 at N = %.1f" % (0.01 * m1 / (m2 - m1**2)))
    print("  at 5.9 keV the position term stays below 0.01 only for Var_z(qbar) < %.2e" % (0.01 * m1 / (5900 / EPS_EH)))
    # unequal drift lengths at the same mean collection
    lu3 = lam_for_uniform(f, 1 / 3)
    Ft, a, b, m1 = fmeas_uniform(F_EH, 100 / EPS_EH, lu3, lu3 / 3)
    print("uniform depth, lam_h = lam_e/3: lam_e/d = %.3f; at 100 eV F_meas = %.4f (%.4f + %.4f)" % (lu3, Ft, a, b))

    print("\n=== Bhatia-Davis: Var q <= qbar(1 - qbar) for q in [0, 1] (scan) ===")
    worst = -1
    for lam in np.logspace(-2, 3, 200):
        for z in np.linspace(0.01, 0.99, 99):
            m, v = qbar(z, lam, lam) / 1.0, qvar(z, lam, lam)
            # q = s_e + s_h lies in [0, 1]
            worst = max(worst, v - m * (1 - m))
    print("max over scan of var - qbar(1 - qbar) = %.3e (must be <= 0)" % worst)

    print("\n=== Space charge (planar, fixed bias) ===")
    jump_per_n = E_CH / (EPS_SI_STATIC * EPS0_SI)      # V/m per (1/m^2)
    target = 0.01 * 100.0                               # 1 % of 1 V/cm, in V/m
    n_face = target / jump_per_n * 1e-4                 # per cm^2
    print("eps_0 = %.1f: sheet jump e n/(eps_0 eps0_SI) = %.3e V/cm per e/cm^2" % (EPS_SI_STATIC, jump_per_n * 1e4 / 100))
    print("1%% of 1 V/cm: n_sh = %.3e e/cm^2 (sheet at a face, max|dE| = jump) to %.3e (mid-plane, max = jump/2)"
          % (n_face, 2 * n_face))
    R, ptr = 1.0, 0.1
    N100 = 100 / EPS_EH
    rate = R * N100 * ptr
    print("illustration: 1 Hz/cm^2 of 100 eV events, %.1f pairs, trapped charge %.2f e per pair -> %.2f e/cm^2/s;"
          " time to 1%% of 1 V/cm: %.2f h (face) to %.2f h (mid-plane)"
          % (N100, ptr, rate, n_face / rate / 3600, 2 * n_face / rate / 3600))
    ptr2 = 0.127   # per-carrier trapping probability used to model a Si charge-resolving detector, arXiv:2303.02196 p. 4
    rate2 = R * N100 * ptr2
    print("same with %.3f trapped charges of one sign per pair: %.2f e/cm^2/s -> %.2f h (face) to %.2f h (mid-plane)"
          % (ptr2, rate2, n_face / rate2 / 3600, 2 * n_face / rate2 / 3600))
    for Efield in [1.0, 4.0, 100.0]:
        print("field %5.1f V/cm: sheet density for xi_SC = 1 %%: %.2e to %.2e e/cm^2"
              % (Efield, Efield * n_face, 2 * Efield * n_face))
    # Poole-Frenkel lowering and thermal emission
    for Efield in [4.0, 100.0]:
        dE = np.sqrt(E_CH**3 * Efield * 100 / (np.pi * EPS_SI_STATIC * EPS0_SI)) / E_CH
        print("Poole-Frenkel lowering at %5.1f V/cm: %.2f meV" % (Efield, dE * 1e3))
    print("thermal emission exponent E_b/kT for 45 meV at 50 mK: %.3e" % (0.045 / (KB_EV * 0.05)))
    # electrostatic energy of a trapped pair, separation r
    for r_mm in [0.01, 1.0]:
        Ees = ALPHA * HBARC_EVNM / (EPS_SI_STATIC * r_mm * 1e6)
        print("Coulomb energy alpha/(eps_0 r) of a trapped pair at r = %.2f mm: %.2e eV" % (r_mm, Ees))

    print("\n=== Luke emission (golden rule, LA phonons, isotropic band) ===")
    rho = 2335.0
    vL = 9.0e3
    for name, mrel, Xi in [("Si holes", 0.5, 5.0), ("Si electrons (Herring-Vogt, m_c)", 0.26, 9.0)]:
        m = mrel * ME
        l0 = np.pi * HBAR**4 * rho / (2 * m**3 * (Xi * E_CH) ** 2)
        mc2 = m * vL**2 / E_CH                      # eV
        print("%s: l0 = %.2f um; m c_LA^2 = %.4f meV; c_LA/(3 l0) = %.3e 1/s" % (name, l0 * 1e6, mc2 * 1e3, vL / (3 * l0)))
        for M in [1.2, 1.5, 2.0, 3.0]:
            G = vL / (3 * l0) * (M - 1) ** 3 / M
            Gp = vL / (3 * l0) * (M - 1) ** 3 / M**2
            print("   k/k_s = %.1f: Gamma_L = %.3e 1/s (printed form with one power less: %.3e); <E_ph> = %.3f meV, "
                  "E_max = %.3f meV" % (M, G, Gp, 1.5 * mc2 * (M - 1) * 1e3, 2 * mc2 * (M - 1) * 1e3))
        for gap in [0.36e-3, 0.6e-3]:
            print("   all Luke phonons below %.2f meV while k/k_s < %.3f" % (gap * 1e3, 1 + gap / (2 * mc2)))
        # energy balance estimate: e E (M c_LA) = Gamma_L <E_L>  ->  (M-1)^4/M^2 = 2 e E l0/(m c^2)
        # (upper estimate of M: the drift velocity along the field is below the speed M c_LA)
        for Ef in [1.0, 4.0, 100.0]:
            rhs = 2 * Ef * 100 * l0 / mc2
            Mb = brentq(lambda M: (M - 1) ** 4 / M**2 - rhs, 1.0001, 1e4)
            Emax = 2 * mc2 * (Mb - 1)
            print("   balance estimate at %5.1f V/cm: k/k_s = %.2f, <E_L> = %.2f meV, E_max = %.2f meV, "
                  "energy fraction below 0.36 meV = (0.36/E_max)^4 = %.4f"
                  % (Ef, Mb, 1.5 * mc2 * (Mb - 1) * 1e3, Emax * 1e3, min(1, (0.36e-3 / Emax) ** 4)))
    # energy-weighted spectrum: fraction of emitted energy below E_c is (E_c/E_max)^4 (weight u^2 x energy u)
    M = 3.0
    uc = 0.3 * (1 - 1 / M)
    frac = quad(lambda u: u**3, 0, uc)[0] / quad(lambda u: u**3, 0, 1 - 1 / M)[0]
    print("check: energy fraction below 0.3 E_max = %.6f vs 0.3^4 = %.6f" % (frac, 0.3**4))
    # analytic check of the angular integral: int_{1/M}^1 4 (M c - 1)^2 dc = 4 M^2 (1 - 1/M)^3 / 3
    for M in [1.5, 4.0]:
        num = quad(lambda c: 4 * (M * c - 1) ** 2, 1 / M, 1)[0]
        print("angular integral at M = %.1f: %.8f vs 4 M^2 (1-1/M)^3/3 = %.8f" % (M, num, 4 * M**2 * (1 - 1 / M) ** 3 / 3))
    # mean phonon energy check: weight (c - 1/M)^2, energy 2 c_LA k (c - 1/M)
    M = 2.5
    w = lambda c: (c - 1 / M) ** 2
    e = lambda c: 2 * M * (c - 1 / M)               # units of m c^2 (k = M k_s, k_s = m c)
    me = quad(lambda c: w(c) * e(c), 1 / M, 1)[0] / quad(w, 1 / M, 1)[0]
    print("mean Luke phonon energy at M = 2.5: %.6f m c^2 vs (3/2)(M - 1) = %.6f" % (me, 1.5 * (M - 1)))

    # ------------------------------------------------------------ Fig. 20.1
    plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 2.8))
    lam = np.logspace(-2, 2, 400)
    a1.semilogx(lam, hecht_face(lam), "k-", lw=1.5, label="Hecht: one carrier from a face")
    a1.semilogx(lam, [qbar(0.5, l, l) for l in lam], "b--", lw=1.2, label="pair at mid-plane")
    a1.semilogx(lam, qbar_uniform(lam, lam), "r-", lw=1.2, label=r"uniform depth, $\lambda_{\mathrm{d}}^h = \lambda_{\mathrm{d}}^e$")
    a1.semilogx(lam, qbar_uniform(lam, lam / 3), "r:", lw=1.2, label=r"uniform depth, $\lambda_{\mathrm{d}}^h = \lambda_{\mathrm{d}}^e/3$")
    a1.set_xlabel(r"$\lambda_{\mathrm{d}}^e/d_{\mathrm{det}}$")
    a1.set_ylabel(r"mean induced charge per pair ($e$)")
    a1.set_ylim(0, 1.45)
    a1.set_xlim(1e-2, 1e2)
    a1.legend(fontsize=6.3, frameon=False, loc="upper left")
    a1.text(0.97, 0.05, "(a)", transform=a1.transAxes, ha="right")
    z = np.linspace(0, 1, 300)
    for l, ls in [(0.3, ":"), (1.0, "--"), (3.0, "-")]:
        a2.plot(z, qbar(z, l, l), "k" + ls, lw=1.2, label=r"$\lambda_{\mathrm{d}}/d_{\mathrm{det}} = %.1f$" % l)
    a2.set_xlabel(r"depth of the pair $z/d_{\mathrm{det}}$")
    a2.set_ylabel(r"$\bar{\mathfrak{q}}(z)$")
    a2.set_ylim(0, 1.02)
    a2.set_xlim(0, 1)
    a2.legend(fontsize=6.5, frameon=False, loc="lower center")
    a2.text(0.97, 0.05, "(b)", transform=a2.transAxes, ha="right")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "fig20_1.pdf"))
    print("wrote fig20_1.pdf")
