"""Figs. for Sect. 4.8 (Feynman diagrams) and every number quoted in Worked example 4.14.

Outputs: tex/figures/ch04/fig4_9.pdf  (diagrams: bubble, random-phase chain and screened line, second-order self-energy
                                        with a boson and the GW self-energy, ladder)
         tex/figures/ch04/fig4_9b.pdf (Worked example 4.14: self-energy of an electron coupled to an Einstein boson)

Conventions (Sect. 4.7, App. D.11): energies measured from mu_ch; fermionic Matsubara frequencies (2j+1) pi T,
bosonic 2 j pi T; free boson propagator D0(i nu) = 1/(i nu - w) - 1/(i nu + w) (eq. D.11-D0); Matsubara rules of
App. D.11 (interaction line -|g|^2 D0/V, no loop in the self-energy diagram).

Model of the worked example (no external data; parameters illustrative and named in the caption):
  - one empty band with a flat density of states D per spin and volume over a width E_w = 1 eV (the flat band of
    Worked example 2.1), bottom at E_c - mu_ch = 0.5 eV (chemical potential near mid-gap of a semiconductor with a
    1.1 eV gap, so n_F <= 4e-9 at 300 K and is dropped in the closed form, kept in the Matsubara check);
  - an Einstein boson of energy w_Ein = 60 meV (a typical silicon phonon energy, the value used in Sect. 1.3);
  - a constant coupling |g|^2, fixed by the T = 0 golden-rule emission rate Gamma_em = 2 pi |g|^2 D = 20 meV.
  Then (1/V) sum_Q |g|^2 F(xi_{k-Q}) = |g|^2 int d eps D F(eps), and
  Sigma^R(w) = (Gamma_em/2pi) [ (n_B + 1) l(w - w_Ein) + n_B l(w + w_Ein) ],
  l(x) = ln[(x - E_c + i0)/(x - E_c - E_w + i0)], energies here measured from E_c (E_c -> 0 in the code).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch04")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.size": 9, "axes.linewidth": 0.6, "pdf.fonttype": 42})

kB = 8.617333e-5            # eV/K
Ew, wE, Gem = 1.0, 0.060, 0.020
Ec_mu = 0.5                 # eV, band bottom above mu_ch
T300 = 300 * kB


def nB(w, T):
    return 0.0 if T == 0 else 1.0 / np.expm1(w / T)


def ell(x, eta=1e-13):
    return np.log((x + 1j * eta) / (x - Ew + 1j * eta))


def Sig(w, T):
    """Retarded self-energy, w measured from the band bottom E_c."""
    n = nB(wE, T)
    return Gem / (2 * np.pi) * ((1 + n) * ell(w - wE) + n * ell(w + wE))


# --- Matsubara check: the closed-form frequency sum against a direct sum, for single band states --------------------
T = T300
nu = 2 * np.pi * T * np.arange(-10**6, 10**6 + 1)
D0 = 1 / (1j * nu - wE) - 1 / (1j * nu + wE)
for xi in [-0.03, 0.011, 0.2, Ec_mu]:          # band-state energies from mu_ch (eV), occupied and empty
    nF = 1 / (np.exp(xi / T) + 1)
    for j in [0, 3]:
        wF = np.pi * T * (2 * j + 1)
        direct = -T * np.sum(D0 / (1j * wF - 1j * nu - xi))        # -T sum D0 G0, the boson Fock diagram per |g|^2
        closed = (nB(wE, T) + 1 - nF) / (1j * wF - xi - wE) + (nB(wE, T) + nF) / (1j * wF - xi + wE)
        assert abs(direct - closed) < 1e-9 * abs(closed), (xi, j, direct, closed)
assert 1 / (np.exp(Ec_mu / T300) + 1) < 4e-9
print("Matsubara sum: closed form = direct sum (rel. 1e-9) at T = 300 K, j = 0, 3")

# --- quoted numbers -----------------------------------------------------------------------------------------------
res = {}
for name, TT in [("0", 0.0), ("300", T300)]:
    s = Sig(0.0, TT)
    h = 1e-6
    slope = (Sig(h, TT).real - Sig(-h, TT).real) / (2 * h)
    z = 1 / (1 - slope)
    E = 0.0
    for _ in range(200):
        E = Sig(E, TT).real
    res[name] = dict(n=nB(wE, TT), ReS=s.real, ImS=s.imag, slope=slope, z=z, Gqp=-2 * z * s.imag, Eqp=E)
    print(name, {k: round(v, 6) for k, v in res[name].items()})
r0, r3 = res["0"], res["300"]
assert np.isclose(r0["ReS"], Gem / (2 * np.pi) * np.log(wE / (Ew + wE)))
assert abs(r0["ReS"] * 1e3 - (-9.14)) < 0.005 and abs(r0["ImS"]) < 1e-9
assert abs(r0["slope"] - (-0.0500)) < 5e-5 and abs(r0["z"] - 0.952) < 5e-4
assert abs(r0["Eqp"] * 1e3 - (-8.73)) < 0.005
assert abs(r3["n"] - 0.109) < 5e-4
assert abs(r3["ReS"] * 1e3 - (-11.09)) < 0.005 and abs(r3["ImS"] * 1e3 - (-1.089)) < 5e-4
assert abs(r3["Gqp"] * 1e3 - 2.08) < 0.005 and abs(r3["z"] - 0.953) < 5e-4
assert abs(r3["ReS"] / (r0["ReS"] * (2 * r3["n"] + 1)) - 1) < 0.004   # shift ~ (2 n_B + 1)
hbar = 6.582120e-16  # eV s
print("lifetime at 300 K (ps):", hbar / r3["Gqp"] * 1e12)
assert abs(hbar / r3["Gqp"] * 1e12 - 0.32) < 0.005
# well inside the band: width Gem (1 + 2 n_B)
for TT, val in [(0.0, 20.0), (T300, 24.35)]:
    s = Sig(0.3, TT)
    assert abs(-2 * s.imag * 1e3 - val) < 0.01, (-2 * s.imag * 1e3)
print("shift at 0.3 eV:", Sig(0.3, 0).real * 1e3, Sig(0.3, T300).real * 1e3)

# --- Fig. 4.9b ---------------------------------------------------------------------------------------------------
w = np.linspace(-0.2, 0.4, 6001)
fig, axs = plt.subplots(1, 2, figsize=(6.4, 2.7), sharex=True)
for TT, ls, lab in [(0.0, "-", r"$T = 0$"), (T300, "--", r"$T = 300$ K")]:
    s = np.array([Sig(x, TT) for x in w])
    axs[0].plot(w * 1e3, -2 * s.imag * 1e3, color="k", ls=ls, lw=1.1, label=lab)
    axs[1].plot(w * 1e3, s.real * 1e3, color="k", ls=ls, lw=1.1, label=lab)
for ax in axs:
    ax.axvline(0, color="0.6", lw=0.5)
    ax.axvspan(-200, 0, color="0.92", lw=0)
    ax.set_xlabel(r"$\omega - E_{\mathrm{c}}$ (meV)")
    ax.set_xlim(-200, 400)
axs[0].set_ylabel(r"$-2\,\mathrm{Im}\,\Sigma^{\mathrm{R}}$ (meV)")
axs[0].set_ylim(0, 27)
axs[1].set_ylabel(r"$\mathrm{Re}\,\Sigma^{\mathrm{R}}$ (meV)")
axs[1].set_ylim(-25, 5)
axs[0].legend(frameon=False, fontsize=8, loc="lower right", bbox_to_anchor=(1.0, 0.03))   # clear of the onset leader line
axs[0].text(-190, 24, "(a)"); axs[1].text(-190, 1.5, "(b)")
axs[0].annotate(r"emission onset $\omega_{\mathrm{Ein}}$", xy=(60, 20), xytext=(110, 9), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", lw=0.5, color="0.4"))
axs[0].annotate("absorption only", xy=(-30, 2.2), xytext=(-197, 7), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", lw=0.5, color="0.4"))
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig4_9b.pdf"))
plt.close(fig)


# --- Fig. 4.9: diagrams ------------------------------------------------------------------------------------------
def arrow_mid(ax, xs, ys, color="k"):
    i = len(xs) // 2
    ax.annotate("", xy=(xs[i + 1], ys[i + 1]), xytext=(xs[i - 1], ys[i - 1]),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=0.8, mutation_scale=9))


def fline(ax, xs, ys, lw=1.0, double=False):
    ax.plot(xs, ys, color="k", lw=lw)
    if double:
        ax.plot(xs, ys, color="w", lw=lw * 0.35)
    arrow_mid(ax, xs, ys)


def bubble(ax, x0, x1, y=0.0, h=0.42, label=True):
    t = np.linspace(0, np.pi, 81)
    xc, r = (x0 + x1) / 2, (x1 - x0) / 2
    xu, yu = xc - r * np.cos(t), y + h * np.sin(t)          # upper arc, left to right
    xl, yl = xc + r * np.cos(t), y - h * np.sin(t)          # lower arc, right to left
    fline(ax, xu, yu)
    fline(ax, xl, yl)
    ax.plot([x0, x1], [y, y], "o", color="k", ms=3)
    if label:
        ax.text(xc, y + h + 0.1, r"$\boldsymbol{k}+\boldsymbol{q}$", ha="center", fontsize=7.5)
        ax.text(xc, y - h - 0.28, r"$\boldsymbol{k}$", ha="center", fontsize=7.5)
    return xu, yu, xl, yl


def dashed(ax, x0, x1, y0=0.0, y1=None):
    y1 = y0 if y1 is None else y1
    ax.plot([x0, x1], [y0, y1], color="k", lw=0.9, ls=(0, (3, 2)))


def wavy(ax, xs, ys, n=8, amp=0.05, double=False):
    xs, ys = np.asarray(xs), np.asarray(ys)
    s = np.concatenate([[0], np.cumsum(np.hypot(np.diff(xs), np.diff(ys)))])
    tx, ty = np.gradient(xs), np.gradient(ys)
    nrm = np.hypot(tx, ty); nx, ny = -ty / nrm, tx / nrm
    ph = 2 * np.pi * n * s / s[-1]
    offs = [0.0] if not double else [-0.03, 0.03]
    for o in offs:
        ax.plot(xs + (amp * np.sin(ph) + o) * nx, ys + (amp * np.sin(ph) + o) * ny, color="k", lw=0.8)


fig, axs = plt.subplots(2, 2, figsize=(6.4, 3.8))
for ax in axs.flat:
    ax.set_aspect("equal"); ax.axis("off")

# (a) bubble
ax = axs[0, 0]
ax.set_xlim(-0.4, 3.0); ax.set_ylim(-0.9, 0.9)
dashed(ax, -0.3, 0.4); bubble(ax, 0.4, 2.2); dashed(ax, 2.2, 2.9)
ax.text(-0.35, 0.65, "(a)")
ax.text(-0.25, 0.08, r"$\boldsymbol{q}$", fontsize=7.5); ax.text(2.6, 0.08, r"$\boldsymbol{q}$", fontsize=7.5)

# (b) random-phase chain for the screened line
ax = axs[0, 1]
ax.set_xlim(-0.2, 5.6); ax.set_ylim(-0.9, 0.9)
wavy(ax, np.linspace(0, 0.8, 50), np.zeros(50), n=4, double=True)
ax.text(1.0, -0.08, "=", fontsize=10)
dashed(ax, 1.35, 1.95)
ax.text(2.1, -0.08, "+", fontsize=10)
dashed(ax, 2.45, 2.9); bubble(ax, 2.9, 3.7, h=0.3, label=False); dashed(ax, 3.7, 4.15)
ax.text(4.3, -0.08, r"+ $\cdots$", fontsize=10)
ax.text(-0.15, 0.65, "(b)")
ax.text(0.05, 0.22, r"$W^{\mathrm{scr}}$", fontsize=7.5); ax.text(1.4, 0.15, r"$v_{\mathrm{C}}$", fontsize=7.5)

# (c) second-order self-energy with a boson; GW with the screened line
ax = axs[1, 0]
ax.set_xlim(-0.2, 5.6); ax.set_ylim(-0.6, 1.2)
for x0, dbl, lab in [(0.0, False, r"$|g|^2\mathsf{D}_0$"), (2.9, True, r"$W^{\mathrm{scr}}$")]:
    xs = np.linspace(x0, x0 + 2.4, 61)
    fline(ax, xs[:15], np.zeros(15)); fline(ax, xs[14:47], np.zeros(33)); fline(ax, xs[46:], np.zeros(15))
    ax.plot([xs[14], xs[46]], [0, 0], "o", color="k", ms=3)
    t = np.linspace(np.pi, 0, 60)
    xc, r = (xs[14] + xs[46]) / 2, (xs[46] - xs[14]) / 2
    wavy(ax, xc + r * np.cos(t), 0.75 * r * np.sin(t), n=6, double=dbl)
    ax.text(xc, 0.75 * r + 0.2, lab, ha="center", fontsize=7.5)
    ax.text(xc, -0.32, r"$\boldsymbol{k}-\boldsymbol{Q}$", ha="center", fontsize=7.5)
    ax.text(xs[3], 0.1, r"$\boldsymbol{k}$", fontsize=7.5)
ax.text(-0.15, 1.0, "(c)")

# (d) ladder
ax = axs[1, 1]
ax.set_xlim(-0.4, 3.6); ax.set_ylim(-0.9, 0.9)
xu, yu, xl, yl = bubble(ax, 0.2, 3.2, h=0.5, label=False)
for xr in [0.8, 1.35, 2.05, 2.6]:   # no rung at x = 1.7, where the propagator arrows sit
    i = np.argmin(abs(xu - xr)); k = np.argmin(abs(xl - xr))
    wavy(ax, np.full(30, xr), np.linspace(yl[k], yu[i], 30), n=3, amp=0.04, double=True)
ax.text(-0.35, 0.65, "(d)")
ax.text(1.7, 0.62, "electron", ha="center", fontsize=7.5); ax.text(1.7, -0.78, "hole", ha="center", fontsize=7.5)

fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig4_9.pdf"))
print("wrote fig4_9.pdf, fig4_9b.pdf")
