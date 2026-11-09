"""Worked example 16.9: the reach band of ZrTe5 from the uncertainty of its background dielectric tensor (Sect. 16.9).

Model and conventions as in zrte5_16.py and dirac16.py (Sect. 16.1): total eps = qhat.eps_bg.qhat + eps_D, light
mediator F_DM = (alpha m_e/q)^2, loss function averaged over the directions of q (rate averaged over crystal
orientations), book halo (rate10_2.py), 3 events in 1 kg yr, rho_T = 6.089 g/cm^3.  Dirac parameters always those of
Sect. 16.1: the experimental-structure (NR) row of Geilhufe et al., arXiv:1910.02091 Table 1, v = (1.1, 0.45, 1.0)e-3,
Lambda_i = (0.23, 0.215, 0.1) 1/A (Lt = 0.191 eV), g = 2, Delta_D = 11.8 meV.
Tensors of the background (diagonal; off-diagonal entries dropped as in Sect. 16.1):
  A  'later'   : 1910.02091 Table 2, 'This work'          (308.4, 20.75, 126.1)     central value of Sect. 16.1
  B  'earlier' : 1708.08929 App. D Table 1 (as quoted in Sect. 7.3 WE and 1910.02091 Table 2, 'Ref. [21]')
                                                           (187.5, 9.8, 90.9)
  C  'A minus Dirac': A with the static Dirac term of each axis removed, eps_D,ii(0,0) = (g alpha/6 pi) v_i^2/(v1 v2 v3)
                 * [ln(4 Lt^2/Delta^2) - 5/3]  (eq:7.3-aniso; 9.8, 1.57, 6.7 in Sect. 7.3 WE), the background a
                 consistent calculation would give at this gap (Sect. 7.3).
  A x f        : A scaled by a common factor f = 1.1 to give the local exponent p = d ln sigma_lim / d ln eps_bg.
Pairing B with the Dirac parameters of A is a modelling choice that isolates the tensor; the two published sets also
differ in velocities.  Absorption: per polarization along the principal axes, unpolarized average, eq:10.7-dp,
rho_T = 6.089 g/cm^3 (a common density; the ratios do not depend on it).
Half-gap: the rows of 1910.02091 Table 1 give Delta_D = 11.75 (Exp. row), 11.8, 15.6 and 17.5 meV; threshold
masses by root finding (brentq) on m with the inner maximization over q by bounded minimization, along the slowest
axis (y) and for the isotropic geometric-mean velocity.
Run: python we16_9.py > we16_9.log   (about two minutes).
"""
import numpy as np
from scipy.optimize import brentq, minimize_scalar
import dirac16 as d

np.seterr(divide="ignore", invalid="ignore")

Z = dict(d.ZRTE5, v=np.array([1.1e-3, 4.5e-4, 1.0e-3]), Lam=np.array([0.23, 0.215, 0.1]), D=11.8e-3)   # NR row
Z["Lt"] = float(np.min(Z["Lam"] * d.HBARC * Z["v"]))
v, g, D, Lt = Z["v"], Z["g"], Z["D"], Z["Lt"]
A = Z["ebg"].copy()
B = d.KAPPA_1708.copy()
pref = g * d.ALPHA / (6 * np.pi * np.prod(v))
B0 = d.B_exact(0.0, D, Lt).real
dD = pref * v**2 * B0
C = A - dD
print("Dirac parameters (1910.02091 NR row): v = %s, Delta_D = %.1f meV, Lt = %.4f eV, g = %d" % (v, D * 1e3, Lt, g))
print("static Dirac term per axis eps_D,ii(0,0) = %.2f, %.2f, %.2f  (bracket B(0) = %.3f)" % (*dD, B0))
for lab, t in [("A later", A), ("B earlier", B), ("C = A - Dirac", C)]:
    print("tensor %-14s = %7.2f %7.2f %7.2f ; harmonic mean %.2f ; alpha~ along y = %.3f"
          % (lab, *t, d.harmonic(t), d.ALPHA * v[1] ** 2 / (t[1] * np.prod(v))))
print("(B_yy/A_yy)^2 = %.4f" % ((B[1] / A[1]) ** 2))
print("ratios B/A per axis: %.3f %.3f %.3f ; harmonic means B/A = %.3f" % (*(B / A), d.harmonic(B) / d.harmonic(A)))

Bt = d.Btab(D, Lt)
nw, nq = 240, 420
W = 2 * D + (2 * Lt - 2 * D) * np.linspace(0, 1, nw) ** 2
W[0] = 2 * D * (1 + 1e-6)
Q = np.geomspace(2 * D / d.VMAX * 0.99, 2 * Lt / min(v), nq)
Wm, Qm = np.meshgrid(W, Q, indexing="ij")
rho = Z["rho_exp"] * d.GCM3


def table(t):
    mat = dict(v=v, ebg=np.asarray(t, float), g=g)
    return np.array([d.L_aniso_avg(Q, w, mat, Bt, "book") for w in W])


def rate(m, tab):
    et = d.R.eta(Wm / Qm + Qm / (2 * m))
    integ = Qm**3 * et * (d.Q0 / Qm) ** 4 * tab
    return np.trapezoid(np.trapezoid(integ, Q, axis=1), W) * d.prefactor(m, rho) * d.KGYR * d.SIG1


tabs = {k: table(t) for k, t in [("A", A), ("B", B), ("C", C), ("A11", 1.1 * A)]}


def mthr(Dh, vv):
    def gap(m):
        f = lambda q: -(q * d.VMAX - q**2 / (2 * m) - np.sqrt((vv * q) ** 2 + 4 * Dh**2))  # noqa: E731
        r = minimize_scalar(f, bounds=(1e-3, 2 * m * d.VMAX), method="bounded", options=dict(xatol=1e-10))
        return -r.fun
    return brentq(gap, 1e3, 1e6, xtol=1e-6)


m_th = mthr(D, min(v))
masses = np.geomspace(m_th * 1.0005, 1e6, 80)
lim = {k: np.array([d.sigma_lim(rate(m, tabs[k])) for m in masses]) for k in tabs}
print("\nscattering reach sigma_e^lim [cm^2] (3 events, 1 kg yr, light mediator, orientation average):")
print("   m [keV]     A (later)     B (earlier)   C (A-Dirac)   B/A     C/A    p = dln(sig)/dln(eps_bg)")
for mt in (12e3, 15e3, 20e3, 50e3, 100e3, 300e3, 1e6):
    j = np.argmin(np.abs(masses - mt))
    p = np.log(lim["A11"][j] / lim["A"][j]) / np.log(1.1)
    print("  %7.1f   %.3e    %.3e    %.3e    %.3f   %.3f   %.3f"
          % (masses[j] / 1e3, lim["A"][j], lim["B"][j], lim["C"][j], lim["B"][j] / lim["A"][j], lim["C"][j] / lim["A"][j], p))
sel = masses >= 20e3
rBA = lim["B"] / lim["A"]
rCA = lim["C"] / lim["A"]
pp = np.log(lim["A11"] / lim["A"]) / np.log(1.1)
print("for 20 keV - 1 MeV: B/A = %.3f to %.3f ; C/A = %.3f to %.3f ; p = %.3f to %.3f"
      % (rBA[sel].min(), rBA[sel].max(), rCA[sel].min(), rCA[sel].max(), pp[sel].min(), pp[sel].max()))
ok = np.isfinite(rBA)
print("a common factor 2 on the tensor with this exponent moves the reach by 2^p = %.2f to %.2f (20 keV - 1 MeV)"
      % (2 ** pp[sel].min(), 2 ** pp[sel].max()))
print("over the whole grid from %.1f keV (finite rates): B/A = %.3f to %.3f" % (masses[ok][0] / 1e3, rBA[ok].min(), rBA[ok].max()))
for k in ("A", "B"):
    jb = np.argmin(lim[k])
    print("best reach, tensor %s: %.2e cm^2 at %.0f keV" % (k, lim[k][jb], masses[jb] / 1e3))
# weak-screening check: (sum over directions of 1/(qhat.eps.qhat)^2) ratio B/A
q2 = d.QH**2
wk = lambda t: np.sum(d.WQH / (q2 @ t) ** 2)  # noqa: E731
print("leading-form ratio <1/(qhat.eps.qhat)^2>_A / <...>_B (= B/A of the reach at weak screening, flat numerator): %.3f"
      % (wk(A) / wk(B)))
print("  share of <1/(qhat.eps.qhat)^2>_A from directions within 30 deg of y: %.3f"
      % (np.sum((d.WQH / (q2 @ A) ** 2)[d.QH[:, 1] > np.cos(np.pi / 6)]) / wk(A)))

# --- absorption ----------------------------------------------------------------------------------------------------
ma = np.geomspace(2 * D * 1.0005, 2 * Lt * 0.999, 200)
za = {}
for k, t in [("A", A), ("B", B), ("C", C)]:
    Lp = d.abs_L_pol(ma, dict(v=v, ebg=t, g=g), Bt)
    za[k] = d.zeta_lim(Lp.mean(axis=1), rho)
print("\nabsorption reach zeta (3 events, 1 kg yr): B/A = %.3f to %.3f ; C/A = %.3f to %.3f over %.0f-%.0f meV"
      % ((za["B"] / za["A"]).min(), (za["B"] / za["A"]).max(), (za["C"] / za["A"]).min(), (za["C"] / za["A"]).max(),
         ma[0] * 1e3, ma[-1] * 1e3))
j = np.argmin(np.abs(ma - 0.1))
print("at 100 meV: zeta A = %.3e, B = %.3e (ratio %.3f) ; weak-screening estimate for the y polarization alone, zeta ~ eps_yy: %.3f"
      % (za["A"][j], za["B"][j], za["B"][j] / za["A"][j], B[1] / A[1]))

# --- half-gap spread: threshold masses ------------------------------------------------------------------------------
vg = np.prod(v) ** (1 / 3)
print("\nthreshold masses with the NR velocities for the half-gaps of the table rows (11.75 measured; 11.8, 15.6, 17.5 computed):")
for Dh in (11.75e-3, 11.8e-3, 15.6e-3, 17.5e-3):
    print("  Delta_D = %.2f meV: along y %.2f keV ; isotropic v_D = %.2e: %.2f keV"
          % (Dh * 1e3, mthr(Dh, v[1]) / 1e3, vg, mthr(Dh, vg) / 1e3))

# Dirac fraction of each computed component (static Dirac term over the tensor A)
print("static Dirac term / computed tensor A per axis: %.3f %.3f %.3f" % tuple(dD / A))
