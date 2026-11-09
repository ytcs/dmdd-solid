"""Model Eliashberg and transport Eliashberg functions of aluminum for Sect. 15.4, cached in a2ftr15.npz.

The model is that of Fig. 6.6 (figscripts/ch06/fig6_6.py), unchanged: Born-von Karman force constants (first and second
neighbours) fitted to the measured zone-boundary frequencies (Savrasov and Savrasov, PRB 54, 16487 (1996),
arXiv:cond-mat/9604124, Table I, 'exp.') and the elastic constants C11 = 106.8, C12 = 60.7, C44 = 28.2 GPa (Kittel);
a = 4.05 A, M = 26.98 u; a free-electron sphere of Z = 3 electrons per atom; a screened empty-core ion
w(q) = -(4 pi Z e^2/Omega q^2) cos(q r_c)/eps_Lindhard(q, 0); r_c at the stationary point of lambda_ep (0.56 A).
The Monte Carlo sample (10^6 momentum transfers q < 2 k_F, seed 1) is drawn exactly as in fig6_6.py.

New here: the transport function.  For two points k, k' = k + q on the free-electron sphere,
    [e . (v_k' - v_k)]^2 averaged over the field direction e = |v_k' - v_k|^2/3 = (2 v_F^2/3)(1 - cos theta),
    1 - cos theta = q^2/(2 k_F^2),
so the transport function of Sect. 15.4 (Fermi-surface average with weight [e.(v'-v)]^2 / (2 <v_x^2>), <v_x^2> = v_F^2/3),
    a2F_tr(omega) = a2F weight of each sample times q^2/(2 k_F^2),
and lambda_tr = 2 int a2F_tr(omega)/omega domega.  Comparison values (Savrasov and Savrasov, Table IV):
lambda_tr = 0.37 (linear response) and 0.39 (from the measured resistivity with their computed omega_p = 12.29 eV).

Output: a2ftr15.npz with the bin edges (meV, 0.05 meV bins), the unsmoothed histograms a2F and a2F_tr (dimensionless),
lambda, lambda_tr, the moments, and the low-frequency coefficient of a2F_tr = c4 omega^4.
Run: python a2ftr15.py   (about 1 min; numpy, scipy)
"""
import os
import numpy as np
from scipy.optimize import least_squares, minimize_scalar

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "a2ftr15.npz")

HA = 27.211386
BOHR = 0.529177211
AMU = 1822.888486
THZ = 4.135667696e-3
KB = 8.617333e-5

a = 4.05 / BOHR
M = 26.98 * AMU
Z = 3
Omega = a**3 / 4
n_e = Z / Omega
kF = (3 * np.pi**2 * n_e) ** (1 / 3)
kTF2 = 4 * kF / np.pi
f_exp = {"XL": 9.69, "XT": 5.78, "LL": 9.69, "LT": 4.19}
C11, C12, C44 = 106.8e9, 60.7e9, 28.2e9
rho = 2.70e3

nn1 = np.array([[s1 * 0.5, s2 * 0.5, 0] for s1 in (1, -1) for s2 in (1, -1)]
               + [[s1 * 0.5, 0, s2 * 0.5] for s1 in (1, -1) for s2 in (1, -1)]
               + [[0, s1 * 0.5, s2 * 0.5] for s1 in (1, -1) for s2 in (1, -1)]) * a
nn2 = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]], float) * a
NB = np.vstack([nn1, nn2])


def fc_tensors(p):
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


def dynmat(q, p):
    T = fc_tensors(p)
    ph = 1 - np.cos(q @ NB.T)
    return np.einsum("...d,dij->...ij", ph, T)


def freqs(q, p):
    w2 = np.linalg.eigvalsh(dynmat(np.atleast_2d(q), p) / M)
    return np.sqrt(np.clip(w2, 0, None))


X = np.array([1.0, 0, 0]) * 2 * np.pi / a
L = np.array([0.5, 0.5, 0.5]) * 2 * np.pi / a
vel = {"100": (np.array([1.0, 0, 0]), np.sort([C11, C44, C44])),
       "110": (np.array([1.0, 1, 0]) / np.sqrt(2), np.sort([(C11 - C12) / 2, C44, (C11 + C12 + 2 * C44) / 2]))}
ATOMIC_V = 2.18769126e6


def residuals(p):
    r = []
    wX = np.sort(freqs(X, p)[0]) * HA / THZ
    wL = np.sort(freqs(L, p)[0]) * HA / THZ
    r += [(wX[0] - f_exp["XT"]) / f_exp["XT"], (wX[2] - f_exp["XL"]) / f_exp["XL"],
          (wL[0] - f_exp["LT"]) / f_exp["LT"], (wL[2] - f_exp["LL"]) / f_exp["LL"]]
    dq = 1e-3
    for key, (n, Cs) in vel.items():
        v = np.sort(freqs(n * dq, p)[0]) / dq * ATOMIC_V
        r += list((rho * v**2 - Cs) / Cs)
    return np.array(r)


fit = least_squares(residuals, np.array([0.01, -0.001, 0.01, 0.001, 0.0]), x_scale=0.01)
P = fit.x

# same random sequence as fig6_6.py: first the DOS sample, then the coupling sample
rng = np.random.default_rng(1)
b = 2 * np.pi / a * np.array([[-1, 1, 1], [1, -1, 1], [1, 1, -1]], float)
_ = rng.random((600_000, 3))
NS = 1_000_000
u = rng.normal(size=(NS, 3))
u /= np.linalg.norm(u, axis=1)[:, None]
qmag = 2 * kF * rng.random(NS) ** (1 / 3)
qv = u * qmag[:, None]
Vsph = 4 * np.pi / 3 * (2 * kF) ** 3
w2, ev = np.linalg.eigh(dynmat(qv, P) / M)
om = np.sqrt(np.clip(w2, 1e-30, None))
proj2 = np.einsum("si,sin->sn", u, ev) ** 2


def lindhard(q):
    x = q / (2 * kF)
    Fx = 0.5 + (1 - x**2) / (4 * x) * np.log(np.abs((1 + x) / (1 - x)))
    return 1 + kTF2 / q**2 * Fx


def wq(q, rc):
    return -(4 * np.pi * Z / (Omega * q**2)) * np.cos(q * rc) / lindhard(q)


pref = Omega / (2 * kF) * Vsph / (2 * np.pi) ** 3 / NS


def weights(rc):
    return pref * proj2 * (qmag * wq(qmag, rc) ** 2)[:, None] / (2 * M * om)


def lam(rc):
    return 2 * np.sum(weights(rc) / om)


opt = minimize_scalar(lambda r: lam(r / BOHR), bounds=(0.45, 0.65), method="bounded", options={"xatol": 1e-4})
rc = opt.x / BOHR
W = weights(rc)
Wtr = W * (qmag**2 / (2 * kF**2))[:, None]
lam_ep = 2 * np.sum(W / om)
lam_tr = 2 * np.sum(Wtr / om)
om_meV = om * HA * 1e3
bins = np.arange(0, 45.0001, 0.05)
dw = bins[1] - bins[0]
a2F = np.histogram(om_meV.ravel(), bins=bins, weights=(W * HA * 1e3).ravel())[0] / dw
a2Ftr = np.histogram(om_meV.ravel(), bins=bins, weights=(Wtr * HA * 1e3).ravel())[0] / dw
area = np.sum(Wtr) * HA * 1e3                       # meV, int a2F_tr d omega
mom1 = np.sum(Wtr * om) * HA**2 * 1e6               # meV^2, int omega a2F_tr d omega
omlog_tr = np.exp(2 / lam_tr * np.sum(Wtr / om * np.log(om_meV)))
# low-frequency coefficient: a2F_tr = c4 omega^4 fitted on samples below 3 meV (cumulative area ~ c4 w^5 / 5)
sel = om_meV < 3.0
c4 = 5 * np.sum(Wtr[sel]) * HA * 1e3 / 3.0**5       # meV^-4
print("r_c = %.3f A (as Fig. 6.6)" % (rc * BOHR))
print("model lambda_ep = %.3f, lambda_tr = %.3f (Savrasov Table IV: calc 0.37, from resistivity 0.39)" % (lam_ep, lam_tr))
print("int a2F_tr domega = %.3f meV; int omega a2F_tr domega = %.2f meV^2; omega_log,tr = %.1f meV; max phonon %.1f meV"
      % (area, mom1, omlog_tr, om_meV.max()))
print("low-frequency coefficient of a2F_tr: c4 = %.3e meV^-4 (Debye form 2 lambda_tr/omega_D^4 = %.3e meV^-4 for 0.39, 37 meV)"
      % (c4, 2 * 0.39 / 37.0**4))
# weight below a few meV against the Debye omega^4 law (2 lambda_tr omega^5/(5 omega_D^4), 0.39 and 37 meV)
for wc in (1.0, 4.0, 8.0):
    cum = np.sum(Wtr[om_meV < wc]) * HA * 1e3
    print("int_0^%g meV a2F_tr = %.3g meV (model) against %.3g meV (Debye omega^4 law): ratio %.3g"
          % (wc, cum, 2 * 0.39 * wc**5 / (5 * 37.0**4), cum / (2 * 0.39 * wc**5 / (5 * 37.0**4))))
np.savez(OUT, bins=bins, a2F=a2F, a2Ftr=a2Ftr, lam_ep=lam_ep, lam_tr=lam_tr, area_tr=area, mom1_tr=mom1, c4=c4,
         omlog_tr=omlog_tr, rc=rc * BOHR)
print("wrote", OUT)
