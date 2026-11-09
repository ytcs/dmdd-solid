"""Fig. 6.6 (fig:6-a2F) and the numbers of Sect. 6.4 and Worked example 6.4 (we:6-al): a model Eliashberg function of
aluminium, with its phonon density of states.

Model (a labelled model, not a first-principles result):
  Phonons: Born-von Karman force constants for fcc Al, first neighbours (general: 1XX, 1ZZ, 1XY) and second neighbours
    (2XX, 2YY), fitted by least squares to
      - the measured zone-boundary frequencies X_L = 9.69, X_T = 5.78, L_L = 9.69, L_T = 4.19 THz (neutron data from
        Landolt-Boernstein as tabulated by Savrasov and Savrasov, PRB 54, 16487 (1996), arXiv:cond-mat/9604124, Table I, 'exp.'),
      - the room-temperature elastic constants C11 = 106.8, C12 = 60.7, C44 = 28.2 GPa and density 2.70 g/cm^3
        (Kittel, Introduction to Solid State Physics, 8th ed.; the room-temperature set of Sect. 20.3; App. C.18 uses the 0 K set),
      lattice constant a = 4.05 A (Kittel), mass M = 26.98 u.  The fit mixes room-temperature elastic constants with
      the neutron frequencies; the misfit is printed.
  Electrons: one free-electron Fermi sphere with Z = 3 electrons per atom (k_F = 1.75 A^-1, E_F = 11.7 eV).
  Vertex: rigid screened ion, g = (2 M omega)^{-1/2} (q . e_nu) w(q) for a one-atom Bravais lattice with plane waves
    (eq:A.6-g with V = sum_R w(r - R - u_R)), q = Q + G the full momentum transfer (umklapp included), and
    w(q) = -(4 pi Z e^2 / Omega q^2) cos(q r_c) / eps_L(q): an empty-core ion of radius r_c screened by the Lindhard
    (RPA) dielectric function of the electron gas (Sect. 4.5).
  Then eq:D.17-a2F with (1/N) sum_k -> Omega int d^3k/(2pi)^3 and int d^3k/(2pi)^3 delta(xi_k) delta(xi_k+q) = m^2/(4 pi^2 q)
  (q < 2 k_F; D.17) gives
      a2F(omega) = (Omega m / 2 k_F) int_{q<2kF} d^3q/(2pi)^3  sum_nu (qhat . e_nu)^2 q |w(q)|^2 / (2 M omega_nu) delta(omega - omega_nu).
  Modelling choice: r_c is the one free parameter. lambda_ep(r_c) has a minimum near r_c = 0.56 A, where the zero of
  cos(q r_c) sits among the umklapp momentum transfers between |G111| and 2 k_F; we take r_c at that minimum, where the
  result depends least on it, and print lambda for neighbouring r_c. lambda_ep is not fitted to any coupling datum.
  Savrasov and Savrasov's specific-heat value lambda_{s-h} = 0.43 (Table II), from gamma = 1.36 mJ K^-2 mol^-1 and
  N(eps_F) = 5.49 states/(Ry cell), is reproduced below with N(eps_F) counted for both spins (the book's N_F is per spin).
  Savrasov and Savrasov (text below Table I) note that the rigid-ion empirical pseudopotential a2F of Al is practically
  identical to their linear-response one.  Comparison values: lambda_ep = 0.44 (linear response) and 0.42 (tunnelling),
  omega_log = 270 K (linear response; their Tables II, III).
  delta(omega - omega_nu) is a histogram of 0.25 meV bins smoothed by a Gaussian of 0.3 meV standard deviation (plot only;
  lambda and omega_log are computed from the samples without smoothing).
Run: python fig6_6.py > fig6_6.log   (numpy, scipy, matplotlib; about 1 min). The last block is the sensitivity to the
  0 K elastic constants (Sect. 6.4 quotes it).
"""
import os
import numpy as np
from scipy.optimize import least_squares, brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch06", "fig6_6.pdf")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

# ---- constants (CODATA, App. A.1) -------------------------------------------------------------------------------
HA = 27.211386          # eV per hartree
BOHR = 0.529177211      # Angstrom per bohr
AMU = 1822.888486       # electron masses per u
THZ = 4.135667696e-3    # eV per THz (h * 1 THz)
KB = 8.617333e-5        # eV per K
RY = HA / 2

# ---- aluminium -------------------------------------------------------------------------------------------------
a = 4.05 / BOHR                     # bohr (Kittel)
M = 26.98 * AMU                     # electron masses
Z = 3
Omega = a**3 / 4                    # bohr^3
n_e = Z / Omega
kF = (3 * np.pi**2 * n_e) ** (1 / 3)
EF = kF**2 / 2
kTF2 = 4 * kF / np.pi               # Thomas-Fermi wavevector squared, a.u.
NF_cell = kF / (2 * np.pi**2) * Omega   # N_F Omega: per spin, per cell, per hartree (free electrons)

# measured inputs
f_exp = {"XL": 9.69, "XT": 5.78, "LL": 9.69, "LT": 4.19}            # THz (Savrasov Table I, exp.)
C11, C12, C44 = 106.8e9, 60.7e9, 28.2e9                           # Pa (Kittel, room temperature)
rho = 2.70e3                                                      # kg/m^3

# ---- Born-von Karman model ----------------------------------------------------------------------------------------
nn1 = np.array([[s1 * 0.5, s2 * 0.5, 0] for s1 in (1, -1) for s2 in (1, -1)]
               + [[s1 * 0.5, 0, s2 * 0.5] for s1 in (1, -1) for s2 in (1, -1)]
               + [[0, s1 * 0.5, s2 * 0.5] for s1 in (1, -1) for s2 in (1, -1)]) * a
nn2 = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]], float) * a


def fc_tensors(p):
    """Force-constant tensors Phi_d (hartree/bohr^2) for each neighbour vector d."""
    a1, b1, g1, a2, b2 = p
    T = []
    for d in nn1:
        u = np.sign(d)
        nz = np.nonzero(u)[0]
        z = [i for i in range(3) if i not in nz][0]
        P = np.zeros((3, 3))
        P[nz[0], nz[0]] = P[nz[1], nz[1]] = a1
        P[z, z] = b1
        P[nz[0], nz[1]] = P[nz[1], nz[0]] = g1 * u[nz[0]] * u[nz[1]]
        T.append(P)
    for d in nn2:
        i = np.nonzero(d)[0][0]
        P = np.eye(3) * b2
        P[i, i] = a2
        T.append(P)
    return np.array(T)


NB = np.vstack([nn1, nn2])


def dynmat(q, p):
    """Phi(q) = sum_d Phi_d (1 - cos q.d); q array (..., 3) in 1/bohr. Returns (..., 3, 3) in hartree/bohr^2."""
    T = fc_tensors(p)
    ph = 1 - np.cos(q @ NB.T)                       # (..., nd)
    return np.einsum("...d,dij->...ij", ph, T)


def freqs(q, p):
    w2 = np.linalg.eigvalsh(dynmat(np.atleast_2d(q), p) / M)
    return np.sqrt(np.clip(w2, 0, None))


X = np.array([1.0, 0, 0]) * 2 * np.pi / a
L = np.array([0.5, 0.5, 0.5]) * 2 * np.pi / a
# elastic data as small-q velocities: [100] L: C11, T: C44; [110] L: (C11+C12+2C44)/2, T1: C44, T2: (C11-C12)/2
vel = {"100": (np.array([1.0, 0, 0]), np.sort([C11, C44, C44])),
       "110": (np.array([1.0, 1, 0]) / np.sqrt(2), np.sort([(C11 - C12) / 2, C44, (C11 + C12 + 2 * C44) / 2]))}
ATOMIC_V = 2.18769126e6           # m/s per atomic unit of velocity


def residuals(p):
    r = []
    wX = np.sort(freqs(X, p)[0]) * HA / THZ
    wL = np.sort(freqs(L, p)[0]) * HA / THZ
    r += [(wX[0] - f_exp["XT"]) / f_exp["XT"], (wX[2] - f_exp["XL"]) / f_exp["XL"],
          (wL[0] - f_exp["LT"]) / f_exp["LT"], (wL[2] - f_exp["LL"]) / f_exp["LL"]]
    dq = 1e-3
    for key, (n, Cs) in vel.items():
        v = np.sort(freqs(n * dq, p)[0]) / dq * ATOMIC_V      # m/s
        r += list((rho * v**2 - Cs) / Cs)
    return np.array(r)


p0 = np.array([0.01, -0.001, 0.01, 0.001, 0.0])
fit = least_squares(residuals, p0, x_scale=0.01)
P = fit.x
res = residuals(P)
print("BvK force constants (eV/A^2): 1XX=%.3f 1ZZ=%.3f 1XY=%.3f 2XX=%.3f 2YY=%.3f"
      % tuple(P * HA / BOHR**2))
print("fit residuals (relative): zone boundary XT XL LT LL =", np.round(res[:4], 3),
      " elastic [100],[110] =", np.round(res[4:], 3))
wX = np.sort(freqs(X, P)[0]) * HA / THZ
wL = np.sort(freqs(L, P)[0]) * HA / THZ
print("model X: %.2f %.2f THz, L: %.2f %.2f THz" % (wX[0], wX[2], wL[0], wL[2]))

# ---- phonon density of states g_ph(omega) of eq:5.2-dos (called F in the code), one atom per cell, normalized to 3 ------------------------------------------------
rng = np.random.default_rng(1)
b = 2 * np.pi / a * np.array([[-1, 1, 1], [1, -1, 1], [1, 1, -1]], float)   # reciprocal basis of fcc
NQ = 600_000
fr = rng.random((NQ, 3))
Qs = fr @ b
wQ = freqs(Qs, P).ravel() * HA * 1e3            # meV
bins = np.arange(0, 45.0001, 0.25)
cent = 0.5 * (bins[1:] + bins[:-1])
dw = bins[1] - bins[0]
F_hist, _ = np.histogram(wQ, bins=bins)
F = 3 * F_hist / (len(wQ) * dw)                  # per meV, integral 3
wmax = wQ.max()
print("max phonon energy %.1f meV = %.0f K" % (wmax, wmax * 1e-3 / KB))

# ---- coupling: samples of q uniformly in the sphere q < 2 kF ----------------------------------------------------
NS = 1_000_000
u = rng.normal(size=(NS, 3))
u /= np.linalg.norm(u, axis=1)[:, None]
qmag = 2 * kF * rng.random(NS) ** (1 / 3)
qv = u * qmag[:, None]
Vsph = 4 * np.pi / 3 * (2 * kF) ** 3
w2, ev = np.linalg.eigh(dynmat(qv, P) / M)
om = np.sqrt(np.clip(w2, 1e-30, None))           # hartree, (NS, 3)
proj2 = np.einsum("si,sin->sn", u, ev) ** 2      # (qhat . e_nu)^2


def lindhard(q):
    x = q / (2 * kF)
    Fx = 0.5 + (1 - x**2) / (4 * x) * np.log(np.abs((1 + x) / (1 - x)))
    return 1 + kTF2 / q**2 * Fx


def wq(q, rc):
    return -(4 * np.pi * Z / (Omega * q**2)) * np.cos(q * rc) / lindhard(q)


pref = Omega * 1.0 / (2 * kF) * Vsph / (2 * np.pi) ** 3 / NS    # Omega m / 2kF * int d^3q/(2pi)^3, MC weight


def weights(rc):
    """a2F weight of each (sample, mode): integrates to the a2F area in hartree."""
    return pref * proj2 * (qmag * wq(qmag, rc) ** 2)[:, None] / (2 * M * om)


def lam(rc):
    return 2 * np.sum(weights(rc) / om)


from scipy.optimize import minimize_scalar
opt = minimize_scalar(lambda r: lam(r / BOHR), bounds=(0.45, 0.65), method="bounded", options={"xatol": 1e-4})
rc = opt.x / BOHR
for r in (0.50, 0.53, 0.55, 0.59, 0.60, 0.62):
    print("  lambda(r_c = %.2f A) = %.3f" % (r, lam(r / BOHR)))
W = weights(rc)
lam_model = 2 * np.sum(W / om)
om_meV = om * HA * 1e3
omlog = np.exp(2 / lam_model * np.sum(W / om * np.log(om_meV)))      # meV
area = np.sum(W) * HA * 1e3                                           # meV (integral of a2F d omega)
print("r_c = %.3f bohr = %.3f A;  q r_c = pi/2 at q = %.2f A^-1; 2kF = %.2f A^-1, |G111| = %.2f A^-1"
      % (rc, rc * BOHR, np.pi / 2 / rc / BOHR, 2 * kF / BOHR, np.sqrt(3) * 2 * np.pi / a / BOHR))
print("kF = %.3f A^-1, EF = %.2f eV, N_F Omega (per spin, per cell) = %.4f /eV" % (kF / BOHR, EF * HA, NF_cell / HA))
print("model lambda_ep = %.3f, omega_log = %.1f meV = %.0f K, int a2F d omega = %.2f meV"
      % (lam_model, omlog, omlog * 1e-3 / KB, area))

# check of the N(eps_F) spin convention of Savrasov and Savrasov: gamma = (pi^2/3) k_B^2 N_tot (1 + lambda)
NA = 6.02214076e23
gam = 1.36e-3 / NA / 1.602176634e-19                           # eV/K^2 per atom
Ntot = 5.49 / RY                                               # states / (eV cell), both spins
lam_sh = gam / (np.pi**2 / 3 * KB**2 * Ntot) - 1
print("specific-heat lambda with N(eps_F) = 5.49/(Ry cell) counted for both spins: %.3f" % lam_sh)
assert abs(lam_sh - 0.43) < 0.01
print("free-electron N_F Omega both spins = %.2f /(Ry cell)" % (2 * NF_cell / 2))   # per hartree -> per Ry: /2

# ---- a2F histogram and alpha^2(omega) ----------------------------------------------------------------------------
A_hist, _ = np.histogram(om_meV.ravel(), bins=bins, weights=(W * HA * 1e3).ravel())
a2F = A_hist / dw                               # dimensionless


def smooth(y, s=0.3):
    k = np.arange(-6, 7) * dw
    g = np.exp(-0.5 * (k / s) ** 2)
    return np.convolve(y, g / g.sum(), mode="same")


a2F_s, F_s = smooth(a2F), smooth(F)

# ---- two-peak (TA, LA) Einstein model: split at the minimum of F between the peaks --------------------------------
lo = (cent > 10) & (cent < 30)
iTA = np.argmax(np.where(cent < 25, F_s, 0))
iLA = np.argmax(np.where(cent > 30, F_s, 0))
imin = np.argmin(np.where((cent > cent[iTA]) & (cent < cent[iLA]), F_s, np.inf))
w_split = cent[imin]
wT, wL_ = cent[iTA], cent[iLA]
sel = om_meV < w_split
A_T = np.sum(W[sel]) * HA * 1e3
A_L = np.sum(W[~sel]) * HA * 1e3
lam2 = 2 * (A_T / wT + A_L / wL_)
lam_T = 2 * np.sum(W[sel] / om[sel])
lam_L = 2 * np.sum(W[~sel] / om[~sel])
omlog2 = np.exp(2 / lam2 * (A_T / wT * np.log(wT) + A_L / wL_ * np.log(wL_)))
nT = np.sum(wQ < w_split) / len(wQ) * 3
print("F peaks: TA %.2f meV (%.2f THz), LA %.2f meV (%.2f THz); split at %.2f meV; modes below split %.3f of 3"
      % (wT, wT / THZ / 1e3, wL_, wL_ / THZ / 1e3, w_split, nT))
print("areas A_T = %.3f meV, A_L = %.3f meV; A_T/A_L = %.2f (DOS mode ratio %.2f)" % (A_T, A_L, A_T / A_L, nT / (3 - nT)))
print("two-peak lambda = 2(A_T/w_T + A_L/w_L) = 2(%.3f/%.2f + %.3f/%.2f) = %.3f; exact parts lambda_T = %.3f, lambda_L = %.3f"
      % (A_T, wT, A_L, wL_, lam2, lam_T, lam_L))
print("two-peak omega_log = %.1f meV = %.0f K" % (omlog2, omlog2 * 1e-3 / KB))
# constant-alpha^2 comparison: same total area spread like F
alpha2_const = area / 3
lam_const = 2 * alpha2_const * np.sum(F / np.where(cent > 0, cent, np.inf)) * dw
omlog_const = np.exp(np.sum(F / cent * np.log(cent)) / np.sum(F / cent))
print("constant alpha^2 with the same area: alpha^2 = %.3f meV, lambda = %.3f, omega_log = %.1f meV = %.0f K"
      % (alpha2_const, lam_const, omlog_const, omlog_const * 1e-3 / KB))
# mass enhancement and mean linewidths from eq:D.17-lambda: alpha^2F = (1/(4 pi N_F Omega N)) sum gamma/omega delta(omega - omega_Q nu)
print("1 + lambda = %.2f" % (1 + lam_model))
NFc_eV = NF_cell / HA                                                  # per eV
mean_g_over_w = 4 * np.pi * NFc_eV * area * 1e-3 / 3                   # average of gamma/omega over all 3N modes
mean_gamma = 4 * np.pi * NFc_eV * np.sum(W * om) * HA**2 / 3 * 1e3     # meV, average gamma over all modes
print("mode average gamma/omega = %.4f, mode average gamma = %.3f meV" % (mean_g_over_w, mean_gamma))
# electronic specific heat per spin convention: gamma_el = (2 pi^2/3) k_B^2 N_F Omega (1 + lambda), per atom
NFc_sav = 5.49 / 2 / RY                                                # per spin per cell per eV
gam_band = 2 * np.pi**2 / 3 * KB**2 * NFc_sav * NA * 1.602176634e-19 * 1e3   # mJ K^-2 mol^-1
print("Savrasov N_F Omega per spin = %.4f /eV; band gamma = %.3f mJ/K^2/mol; measured/band = %.3f"
      % (NFc_sav, gam_band, 1.36 / gam_band))
# ratios quoted in the text
print("omega_max/E_F = %.4f, lambda * omega_max / E_F = %.4f" % (wmax * 1e-3 / (EF * HA), lam_model * wmax * 1e-3 / (EF * HA)))
print("v_F = %.3g m/s" % (kF * ATOMIC_V))

# ---- figure ------------------------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, ax = plt.subplots(figsize=(4.6, 2.9))
ax.fill_between(cent, F_s * (a2F_s.max() / F_s.max()), color="0.85", lw=0,
                label=r"$g_{\mathrm{ph}}(\omega)$, scaled")   # scaling stated in the caption; short label stays off the shaded area
ax.plot(cent, a2F_s, color="k", lw=1.3, label=r"$\alpha^2F(\omega)$, model")
ax.axvline(wT, color="0.4", lw=0.6, ls=":")
ax.axvline(wL_, color="0.4", lw=0.6, ls=":")
ax.text(wT + 0.4, a2F_s.max() * 1.02, "TA", fontsize=8, color="0.3")
ax.text(wL_ + 0.4, a2F_s.max() * 1.02, "LA", fontsize=8, color="0.3")
ax.set_xlim(0, 44)
ax.set_ylim(0, a2F_s.max() * 1.15)
ax.set_xlabel(r"$\omega$ (meV)")
ax.set_ylabel(r"$\alpha^2F(\omega)$")
ax.legend(frameon=False, fontsize=7.5, loc="upper left", bbox_to_anchor=(0.0, 0.97))
fig.tight_layout()
fig.savefig(OUT)
print("wrote", OUT)

# ---- sensitivity branch: the same fit with the zero-temperature elastic constants ---------------------------------
# C11, C12, C44 = 114.3, 61.9, 31.6 GPa (malica2020quasi Table 2, the set of App. C.18 and Sect. 20.3) at 2.70 g/cm^3.
# The book's model keeps the room-temperature set above, which is the source's (Kittel) and pairs with the
# room-temperature neutron frequencies; this branch prints how far lambda_ep, omega_log and the two-peak lambda move.
vel_rt = vel
C11_0, C12_0, C44_0 = 114.3e9, 61.9e9, 31.6e9
vel = {"100": (np.array([1.0, 0, 0]), np.sort([C11_0, C44_0, C44_0])),
       "110": (np.array([1.0, 1, 0]) / np.sqrt(2), np.sort([(C11_0 - C12_0) / 2, C44_0, (C11_0 + C12_0 + 2 * C44_0) / 2]))}
P0 = least_squares(residuals, p0, x_scale=0.01).x
vel = vel_rt
print("\nSensitivity, 0 K elastic constants C11, C12, C44 = 114.3, 61.9, 31.6 GPa at 2.70 g/cm^3:")
print("  BvK force constants (eV/A^2): 1XX=%.3f 1ZZ=%.3f 1XY=%.3f 2XX=%.3f 2YY=%.3f" % tuple(P0 * HA / BOHR**2))
wQ0 = freqs(Qs, P0).ravel() * HA * 1e3
F0 = 3 * np.histogram(wQ0, bins=bins)[0] / (len(wQ0) * dw)
w20, ev0 = np.linalg.eigh(dynmat(qv, P0) / M)
om0 = np.sqrt(np.clip(w20, 1e-30, None))
proj20 = np.einsum("si,sin->sn", u, ev0) ** 2


def weights0(r):
    return pref * proj20 * (qmag * wq(qmag, r) ** 2)[:, None] / (2 * M * om0)


rc0 = minimize_scalar(lambda r: 2 * np.sum(weights0(r / BOHR) / om0), bounds=(0.45, 0.65), method="bounded",
                      options={"xatol": 1e-4}).x / BOHR
W0 = weights0(rc0)
lam0 = 2 * np.sum(W0 / om0)
om0_meV = om0 * HA * 1e3
omlog0 = np.exp(2 / lam0 * np.sum(W0 / om0 * np.log(om0_meV)))
F0_s = smooth(F0)
iTA0 = np.argmax(np.where(cent < 25, F0_s, 0))
iLA0 = np.argmax(np.where(cent > 30, F0_s, 0))
imin0 = np.argmin(np.where((cent > cent[iTA0]) & (cent < cent[iLA0]), F0_s, np.inf))
sel0 = om0_meV < cent[imin0]
A_T0, A_L0 = np.sum(W0[sel0]) * HA * 1e3, np.sum(W0[~sel0]) * HA * 1e3
lam20 = 2 * (A_T0 / cent[iTA0] + A_L0 / cent[iLA0])
print("  r_c = %.3f A; lambda_ep = %.3f, omega_log = %.1f meV = %.0f K; two-peak lambda = %.3f (room-temperature set: %.3f, %.0f K, %.3f)"
      % (rc0 * BOHR, lam0, omlog0, omlog0 * 1e-3 / KB, lam20, lam_model, omlog * 1e-3 / KB, lam2))
