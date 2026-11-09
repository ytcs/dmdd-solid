"""Limit 11.7a (two panels): the multipole expansion of a crystal rate, eq:11.7-rate, truncated at its first anisotropic term,
against the full direction-resolved rate, as a function of the momentum transfer q.  Output tex/figures/ch11/limit11_7a.pdf;
numbers in limit11_7a.log.

Quantity in both panels: the anisotropic part of the q-differential rate for a wind along a fixed crystal axis n,
   delta(q; n) = [d^2R/dq domega (wind along n)] / [the same with the direction-averaged response] - 1
               = sum_{l >= 1} Upsilon_l(v_min) sum_m S_lm(q) Y_lm(n) / [Upsilon_0(v_min) S_00(q) Y_00]     (eq:11.7-rate per q),
   heavy mediator, the book's halo, m_chi = 10 MeV.
Panel 1, electronic: silicon loss function in the empirical pseudopotential model, random-phase head, no local fields (elf11_7.py),
   omega = 5 eV (bin 4.5-5.5 eV), q from the kinematic edge (v_min = v_max) to 2.8 q0 (end of the model).  'Full' = all fitted
   cubic components l = 0, 4, 6, 8 (the l >= 10 remainder, bounded by the fit residual, enters with Upsilon_10/Upsilon_0, printed);
   formula = l = 4 only; leading correction = l <= 6.  Wind along [100] and along [111].
Panel 2, nuclear: sapphire, incoherent response with direction-dependent Debye-Waller exponents and q-projected DOS (lat11_7.py,
   site tensors of Stratman and Lin from the DarkELF tables), omega-integrated above 80 meV (the optical band), T = 0.
   'Full' = direct integral over a 32 x 64 grid of directions of q; formula = l <= 2; leading correction = l <= 4.
   v_min = q/2m + wbar(q)/q with wbar the mean energy deposited above 80 meV at q (direction-averaged).  Wind along the
   c axis and perpendicular to it (along x).
Shaded: q where the truncation at l <= 4 is within 10 % of the full anisotropic part, for both wind directions of the panel;
   where the anisotropic part is below 1e-3 of the rate the tolerance is 1e-4 of the rate (a floor, so that zero crossings of
   a negligible anisotropy are not counted as failures).
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import aniso11 as AN  # noqa: E402
import lat11_7 as L  # noqa: E402

C_KMS = AN.C_KMS
Q0 = 3728.94
M = 10e6
VMAX = (AN.VESC + AN.VE) / C_KMS


def shade_mask(full, trunc, tol=0.10, floor=1e-3):
    """within tol of the full anisotropic part; where |full| < floor (0.1 % of the rate), within tol * floor."""
    return np.all(np.abs(trunc - full) <= tol * np.maximum(np.abs(full), floor), axis=0)


def spans(x, ok):
    out, start = [], None
    for i, o in enumerate(ok):
        if o and start is None:
            start = i
        if (not o or i == len(ok) - 1) and start is not None:
            end = i if o else i - 1
            out.append((x[start], x[end]))
            start = None
    return out


# ---------------- panel 1
z = np.load(os.path.join(HERE, "elf11_7_Si_NK12.npz"))
c, res = AN.fit_cubic(z["DIRS"], z["L"])
ib = int(np.argmin(np.abs(z["BIN"] - 5.0)))
Q = z["Q"]
w = 5.0
qlo = w / VMAX * (1 + 1e-3)
qf = np.geomspace(max(qlo, Q[0] * Q0), Q[-1] * Q0, 300)
vmin = (w / qf + qf / (2 * M)) * C_KMS
ups = {l: AN.upsilon(l, vmin) for l in (0, 4, 6, 8, 10)}
Ll = {l: np.interp(np.log(qf / Q0), np.log(Q), c[l][:, ib]) for l in (0, 4, 6, 8)}
resq = np.interp(np.log(qf / Q0), np.log(Q), res[:, ib])
dirs = {"[100]": np.array([1, 0, 0.]), "[111]": np.ones(3) / np.sqrt(3)}
P1 = {}
for k, n in dirs.items():
    base = ups[0] * Ll[0] * AN.ycub(0, n)
    t = {l: ups[l] * Ll[l] * AN.ycub(l, n) / base for l in (4, 6, 8)}
    P1[k] = dict(full=t[4] + t[6] + t[8], f4=t[4], f6=t[4] + t[6])
ok1 = shade_mask(np.array([P1[k]["full"] for k in dirs]), np.array([P1[k]["f4"] for k in dirs]))
print("panel 1 (Si EPM loss function, 5 eV, 10 MeV): q from %.2f keV (edge) to %.2f keV" % (qf[0] / 1e3, qf[-1] / 1e3))
print("  l = 4 within 10 %% of l <= 8 for both [100] and [111] on q (keV) in %s" % [(round(a / 1e3, 2), round(b / 1e3, 2)) for a, b in spans(qf, ok1)])
for qq in (1.95e3, 2.1e3, 2.5e3, 3e3, 4e3, 6e3, 8e3, 10e3):
    i = np.argmin(np.abs(qf - qq))
    print("  q = %4.1f keV: v_min = %3.0f km/s, Ups4/Ups0 = %+.4f, Ups6/Ups0 = %+.4f, Ups10/Ups0 = %+.5f; L4/L0 = %+.3f, L6/L0 = %+.3f, "
          "fit residual %.3f; delta[100] full %+.4f (l=4 %+.4f), delta[111] full %+.4f (l=4 %+.4f)"
          % (qq / 1e3, vmin[i], ups[4][i] / ups[0][i], ups[6][i] / ups[0][i], ups[10][i] / ups[0][i], Ll[4][i] / Ll[0][i],
             Ll[6][i] / Ll[0][i], resq[i], P1["[100]"]["full"][i], P1["[100]"]["f4"][i], P1["[111]"]["full"][i], P1["[111]"]["f4"][i]))

# ---------------- panel 2
sap = L.Incoherent("darkelf_Al2O3_pDoS_anisotropic.dat", L.SAPPHIRE)
qmax = 2 * M * VMAX
q2 = np.geomspace(1.0e3, qmax * 0.995, 120)
qh, wq = AN.sphere_grid(32, 64)
sig, mom = sap.weights(q2, qh, 80e-3, moment=True)
coef = L.proj_real(sig, qh, wq, 8)
wbar = np.sum(wq * mom, axis=1) / np.sum(wq * sig, axis=1)        # mean energy above threshold (eV)
vs = (q2 / (2 * M) + wbar / q2) * C_KMS
ups2 = {l: AN.upsilon(l, vs) for l in range(0, 9, 2)}
dirs2 = {"c axis": np.array([0, 0, 1.0]), "perpendicular": np.array([1.0, 0, 0])}
P2 = {}
for k, n in dirs2.items():
    x = qh @ n
    direct = np.sum(wq[None, :] * AN.fhat(vs[:, None] + AN.VE * x[None, :]) * sig, axis=1)
    terms = {l: 2 * np.pi * ups2[l] * np.einsum("mq,m->q", coef[l], AN.ylm_real(l, n)) for l in range(0, 9, 2)}
    base = terms[0]
    P2[k] = dict(full=direct / base - 1, f2=terms[2] / base, f4=(terms[2] + terms[4]) / base)
ok2 = shade_mask(np.array([P2[k]["full"] for k in dirs2]), np.array([P2[k]["f4"] for k in dirs2]))
print("panel 2 (sapphire, incoherent, omega > 80 meV, 10 MeV): l <= 4 within 10 %% of the full anisotropic part on q (keV) in %s"
      % [(round(a / 1e3, 2), round(b / 1e3, 2)) for a, b in spans(q2, ok2)])
ok22 = shade_mask(np.array([P2[k]["full"] for k in dirs2]), np.array([P2[k]["f2"] for k in dirs2]))
print("  l <= 2 alone within 10 %% on q (keV) in %s" % [(round(a / 1e3, 2), round(b / 1e3, 2)) for a, b in spans(q2, ok22)])
for qq in (2e3, 5e3, 10e3, 20e3, 30e3, 40e3, 50e3):
    i = np.argmin(np.abs(q2 - qq))
    print("  q = %4.1f keV: v_min = %3.0f km/s, Ups2/Ups0 = %+.3f, Ups4/Ups0 = %+.4f; delta(c) full %+.4f, l<=2 %+.4f, l<=4 %+.4f; "
          "delta(perp) full %+.4f, l<=2 %+.4f"
          % (qq / 1e3, vs[i], ups2[2][i] / ups2[0][i], ups2[4][i] / ups2[0][i], P2["c axis"]["full"][i], P2["c axis"]["f2"][i],
             P2["c axis"]["f4"][i], P2["perpendicular"]["full"][i], P2["perpendicular"]["f2"][i]))

# ---------------- plot
fig, axs = plt.subplots(2, 1, figsize=(5.0, 5.6))
ax = axs[0]
for a, b in spans(qf / 1e3, ok1):
    ax.axvspan(a, b, color="0.88", lw=0)
for k, col in (("[100]", "C3"), ("[111]", "C0")):
    ax.plot(qf / 1e3, 100 * P1[k]["full"], color=col, lw=1.5, label=r"full, wind along %s" % k)
    ax.plot(qf / 1e3, 100 * P1[k]["f4"], color=col, ls="--", lw=1.1, label=r"$\ell = 4$ only")
    ax.plot(qf / 1e3, 100 * P1[k]["f6"], color=col, ls=":", lw=1.1, label=r"$\ell \leq 6$")
ax.axhline(0, color="k", lw=0.5)
ax.set_xscale("log")
ax.set_yscale("symlog", linthresh=0.1, linscale=1.0)
ax.set_xlim(qf[0] / 1e3, qf[-1] / 1e3)
ax.set_yticks([-10, -1, -0.1, 0, 0.1, 1, 10], ["\u221210", "\u22121", "\u22120.1", "0", "0.1", "1", "10"])
ax.set_xticks([2, 3, 4, 6, 10], ["2", "3", "4", "6", "10"])
ax.set_xticks([], minor=True)
ax.set_xlabel(r"$q$ [keV]")
ax.set_ylabel(r"anisotropic part [\%]")
ax.text(0.98, 0.95, r"(1) Si loss function, $\omega = 5$ eV", transform=ax.transAxes, ha="right", va="top", fontsize=8)
ax.legend(fontsize=6.3, frameon=False, ncol=2, loc="lower right")
ax = axs[1]
for a, b in spans(q2 / 1e3, ok2):
    ax.axvspan(a, b, color="0.88", lw=0)
for k, col in (("c axis", "C3"), ("perpendicular", "C0")):
    ax.plot(q2 / 1e3, 100 * P2[k]["full"], color=col, lw=1.5, label=r"full, wind %s" % ("along $c$" if k == "c axis" else r"$\perp c$"))
    ax.plot(q2 / 1e3, 100 * P2[k]["f2"], color=col, ls="--", lw=1.1, label=r"$\ell \leq 2$")
    ax.plot(q2 / 1e3, 100 * P2[k]["f4"], color=col, ls=":", lw=1.1, label=r"$\ell \leq 4$")
ax.axhline(0, color="k", lw=0.5)
ax.set_xscale("log")
ax.set_xlim(q2[0] / 1e3, q2[-1] / 1e3)
ax.set_ylim(-3.5, 3.5)
ax.set_xlabel(r"$q$ [keV]")
ax.set_ylabel(r"anisotropic part [\%]")
ax.text(0.02, 0.95, r"(2) sapphire nuclear, $\omega > 80$ meV", transform=ax.transAxes, ha="left", va="top", fontsize=8)
ax.legend(fontsize=6.3, frameon=False, ncol=2, loc="lower left")
fig.tight_layout()
out = os.path.join(HERE, "..", "..", "tex", "figures", "ch11", "limit11_7a.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
