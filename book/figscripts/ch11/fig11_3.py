"""Fig. 11.3: one-, two- and many-phonon parts of the nuclear response of silicon at |q| = 10 keV, T = 0.
Output: tex/figures/ch11/fig11_3.pdf. Prints the weights quoted in Sect. 11.3.

Plotted: the spectrum per nucleus, s(omega) = Omega S_A(q, omega) / (2 pi n_at A^2), averaged over the directions of q, which
integrates to one over all omega (elastic delta included) for the self part.  One species (natural Si, M = 26.162 GeV),
so A and the couplings drop out; e^{-2W} with 2W = q^2 <u_x^2>, <u_x^2> = 2.45e-3 A^2 (T = 0, WE 5.7).
Phonons: PBE force constants of Sect. 5.2 (si_ifc.py), cell-phase convention.
  One phonon, exact: eq:11.1-S1 at |q| = 10 keV, 96 x 192 Gauss-Legendre directions (phon11.sphere_grid), all six branches,
     histogram in 0.5 meV bins.
  Two phonons, exact: eq:11.3-Sn with n = 2, T = 0: for 240 wavevectors q of a 24^3 grid (q = G + grid point, so that the
     partner Q2 = q - G - Q1 is on the grid) with 9.9 <= |q| <= 10.1 keV, drawn at random (seed 3), the sum over Q1 of the grid
     (Q1 = 0 and Q2 = 0 acoustic modes dropped), each q rescaled to 10 keV by (10 keV/|q|)^4 and multiplied by e^{-2W(10 keV)}
     (modelling choice; a 1 % change of |q|); 1 meV bins.  The same pass gives the momentum-resolved self density P^(2)
     (sum over nuclei of the squared amplitudes), plotted as the upper end n_at P^(2) of the certified band.
  Incoherent parts: e^{-2W} (2W)^n/n! P_n(omega), P_1 ~ g_ph(omega)/omega from the DFPT density of states of Sect. 5.2
     (fig5_2_data.npz, 48^3 tetrahedra), P_n its n-fold convolution (0.1 meV grid), n >= 3 summed to n = 8.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "ch05"))
import mph11 as MP  # noqa: E402
import phon11 as P  # noqa: E402
import si_ifc  # noqa: E402

Q0 = 10e3                                    # eV
UX2 = 2.45e-3 / MP.HBARC**2                  # eV^-2
W2 = Q0**2 * UX2
M = MP.M_SI
print("q = 10 keV: 2W = %.4f, e^-2W = %.4f, E_R = %.3f meV" % (W2, np.exp(-W2), Q0**2 / (2 * M) * 1e3))

# ---------------- incoherent parts from the DOS ----------------
CM = 0.123984198e-3                           # eV per cm^-1
d = np.load(os.path.join(HERE, "..", "ch05", "fig5_2_data.npz"))
wd, gd = d["dos"][:, 0] * CM, d["dos"][:, 1]
m = wd > 0
wd, gd = wd[m], gd[m]
dw = 0.1e-3
wg = np.arange(dw / 2, 0.80, dw)              # eV
g = np.interp(wg, wd, gd, left=0, right=0)
P1 = g / wg
P1 /= P1.sum() * dw                           # per eV
wmax_dos = wd[gd > 1e-3 * gd.max()].max()
print("highest phonon in the DOS: %.2f meV" % (wmax_dos * 1e3))
Pn = {1: P1}
for n in range(2, 9):
    c = np.convolve(Pn[n - 1], P1)[:len(wg)] * dw
    # convolution of densities on midpoints: shift by half a bin
    Pn[n] = np.interp(wg, wg + dw / 2, c)
    Pn[n] /= Pn[n].sum() * dw
fact = np.cumprod([1] + list(range(1, 9)))
inc = {n: np.exp(-W2) * W2**n / fact[n] * Pn[n] for n in range(1, 9)}
inc3 = sum(inc[n] for n in range(3, 9))
print("incoherent weights: p1 = %.4f, p2 = %.5f, p(n>=3) = %.2e" %
      (inc[1].sum() * dw, inc[2].sum() * dw, inc3.sum() * dw))

# ---------------- exact one-phonon, direction average ----------------
qh, wq = P.sphere_grid(96, 192)
qv = (Q0 / MP.HBARC) * qh / (2 * np.pi / MP.A_ANG)
w, ev = si_ifc.phonons(qv)
w = np.maximum(w, 1e-3) * 1e-3
ph = np.exp(2j * np.pi * (qv @ MP.TAU.T))
amp = np.zeros((len(qh), 6), complex)
for k in range(2):
    amp += ph[:, k:k + 1] * np.einsum("ni,nij->nj", Q0 * qh, np.conj(ev[:, 3 * k:3 * k + 3, :]))
wt1 = np.abs(amp)**2 / (2 * M * w) * np.exp(-W2) / MP.NAT * wq[:, None]
b1 = np.arange(0, 0.0705, 0.0005)
h1, _ = np.histogram(w.ravel(), bins=b1, weights=wt1.ravel())
s1 = h1 / np.diff(b1)
print("exact one-phonon weight %.4f (incoherent %.4f, ratio - 1 = %+.3f)" % (h1.sum(), inc[1].sum() * dw,
                                                                            h1.sum() / (inc[1].sum() * dw) - 1))

# ---------------- exact two-phonon on a 24^3 grid ----------------
N = 24
idx, Qg, wg24, ev24 = MP.grid_phonons(N)
wg24 = wg24.copy()
nQ = len(Qg)
lin = lambda ijk: ((ijk[..., 0] % N) * N + (ijk[..., 1] % N)) * N + (ijk[..., 2] % N)  # noqa: E731
rng = np.random.default_rng(3)
# commensurate q: q = n . B1 / N with integer n; collect those with 9.9 <= |q| <= 10.1 keV
qunit = 2 * np.pi / MP.A_ANG * MP.HBARC      # eV per (2pi/a)
cand = []
for _ in range(400000):
    nn = rng.integers(-60, 61, 3)
    qq = (nn / N) @ MP.B1 * qunit
    if 9.9e3 <= np.linalg.norm(qq) <= 10.1e3:
        cand.append(nn)
    if len(cand) >= 240:
        break
cand = np.array(cand)
print("commensurate wavevectors used: %d" % len(cand))
b2 = np.arange(0, 0.1405, 0.001)
H2 = np.zeros(len(b2) - 1)
HP = np.zeros(len(b2) - 1)
tot2, totP = [], []
acous0 = np.zeros((nQ, 6), bool)
acous0[0, :3] = True
for nn in cand:
    qq = (nn / N) @ MP.B1 * qunit            # eV, Cartesian
    qn = np.linalg.norm(qq)
    i2 = lin(nn[None, :] - idx)              # Q2 = q - Q1 (mod G)
    # amplitudes per nucleus: q.e*_{k nu}(Q)
    a1 = np.einsum("i,qkin->qkn", qq, np.conj(ev24.reshape(nQ, 2, 3, 6)))
    a2 = a1[i2]
    phk = np.exp(2j * np.pi * ((nn / N) @ MP.B1) @ MP.TAU.T)          # e^{i q.tau_k}
    Fk = phk[None, :, None, None] * a1[:, :, :, None] * a2[:, :, None, :] / M   # (Q1, k, nu1, nu2)
    w1, w2 = wg24[:, :, None], wg24[i2][:, None, :]
    bad = acous0[:, :, None] | acous0[i2][:, None, :]
    den = 4 * np.where(bad, 1.0, w1 * w2)
    scale = (Q0 / qn)**4 * np.exp(-W2)       # amplitudes carry no Debye-Waller factor; e^{-2W} at 10 keV
    coh = np.where(bad, 0, np.abs(Fk.sum(1))**2 / den) / (2 * MP.NAT * nQ) * scale
    pself = np.where(bad, 0, (np.abs(Fk)**2).sum(1) / den) / (2 * MP.NAT * nQ) * scale
    wsum = (w1 + w2).ravel()
    h, _ = np.histogram(wsum, bins=b2, weights=coh.ravel())
    hp, _ = np.histogram(wsum, bins=b2, weights=pself.ravel())
    H2 += h
    HP += hp
    tot2.append(coh.sum())
    totP.append(pself.sum())
H2 /= len(cand)
HP /= len(cand)
s2 = H2 / np.diff(b2)
sP = HP / np.diff(b2)
p2inc = inc[2].sum() * dw
print("exact two-phonon weight (average over q): %.5f, ratio to incoherent %.4f (spread over q: %.3f-%.3f)"
      % (np.mean(tot2), np.mean(tot2) / p2inc, np.min(tot2) / p2inc, np.max(tot2) / p2inc))
print("self density P^(2) averaged over q: ratio to incoherent %.4f (zone-average check)" % (np.mean(totP) / p2inc))
# pointwise ratio exact / incoherent in the band
bc2 = 0.5 * (b2[1:] + b2[:-1])
inc2_b = np.interp(bc2, wg, inc[2])
for e in (0.02, 0.04, 0.06, 0.08, 0.10, 0.12):
    j = np.argmin(np.abs(bc2 - e))
    print("  omega = %3.0f meV: exact/incoherent = %.3f, self density/incoherent = %.3f" %
          (e * 1e3, s2[j] / inc2_b[j], sP[j] / inc2_b[j]))
j1 = np.argmax(s1)
print("one-phonon exact spectrum peaks at %.1f meV" % (0.5 * (b1[j1] + b1[j1 + 1]) * 1e3))
for frac in (0.1, 0.01):
    sel = inc2_b > frac * inc2_b.max()
    rr = s2[sel] / inc2_b[sel]
    print("bins where the incoherent two-phonon spectrum exceeds %.0f %% of its maximum (%.0f-%.0f meV): exact/incoherent %.3f-%.3f;"
          " upper band n_at P/incoherent up to %.2f" % (100 * frac, bc2[sel].min() * 1e3, bc2[sel].max() * 1e3, rr.min(), rr.max(),
                                                       (MP.NAT * sP[sel] / inc2_b[sel]).max()))

# ---------------- figure ----------------
fig, ax = plt.subplots(figsize=(5.0, 3.4))
bc1 = 0.5 * (b1[1:] + b1[:-1])
ax.step(bc1 * 1e3, s1 * 1e-3, where="mid", color="C3", lw=1.2, label="one phonon, exact")
ax.plot(wg * 1e3, inc[1] * 1e-3, color="C3", ls="--", lw=1.0, label="one phonon, incoherent")
ax.step(bc2 * 1e3, s2 * 1e-3, where="mid", color="C0", lw=1.2, label="two phonons, exact")
ax.plot(wg * 1e3, inc[2] * 1e-3, color="C0", ls="--", lw=1.0, label="two phonons, incoherent")
ax.step(bc2 * 1e3, MP.NAT * sP * 1e-3, where="mid", color="C0", ls=":", lw=1.0, label=r"two phonons, upper bound $n_{\mathrm{at}}\mathfrak{P}^{(2)}$")
ax.plot(wg * 1e3, inc3 * 1e-3, color="k", lw=1.0, label=r"$n \geq 3$, incoherent")
ax.set_yscale("log")
ax.set_xlim(0, 200)
ax.set_ylim(1e-8, 1e-2)
ax.set_xlabel(r"$\omega$ [meV]")
ax.set_ylabel(r"$\Omega S_A/(2\pi n_{\mathrm{at}}A^2)$ [meV$^{-1}$]")
ax.legend(fontsize=6.5, frameon=False, loc="upper right")
fig.tight_layout()
out = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "fig11_3.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
