"""Figs. for Sect. 4.7 (Green's functions) and App. D.10, and every number quoted in Worked example 4.12.

Outputs: tex/figures/ch04/fig4_8.pdf (Matsubara contour and its deformation onto the real axis)
         tex/figures/ch04/fig4_8b.pdf (Worked example: spectral function of a level coupled to a flat band)

Conventions (Sect. 4.7, App. A.3): forward transform e^{+i omega t}; retarded functions analytic for Im z > 0;
energies measured from the chemical potential mu_ch; fermionic Matsubara frequencies omega^F_j = (2j+1) pi T,
bosonic omega^B_j = 2 j pi T. Spectral function A = -(1/pi) Im G^R, normalized to int A d omega = 1.

Model of the worked example (no external data): one level d of energy eps_d coupled by a constant hybridization V
to N_b band states spread uniformly over a width E_w centred on eps_d,
    H = eps_d d^+ d + sum_k eps_k c_k^+ c_k + sum_k (V c_k^+ d + V^* d^+ c_k).
Parameters are those of Worked example 2.1 (Sect. 2.1): E_w = 1 eV, golden-rule rate Gamma = 2 pi |V|^2 D = 10 meV,
D = N_b/E_w. Self-energy (exact for this quadratic model):
    Sigma(z) = sum_k |V|^2/(z - eps_k) -> (Gamma/2pi) ln[(z - eps_d + E_w/2)/(z - eps_d - E_w/2)]  (continuum limit),
the level-shift function R(z) of eq. (D.3-resolvent). Panel (b) plots the continuum-limit A(omega) and the
Lorentzian (1/pi)(Gamma/2)/((omega-eps_d)^2 + Gamma^2/4) on a logarithmic axis; the "exact" curve is also checked
against direct diagonalization of the (N_b+1)-level Hamiltonian with N_b = 2000 (the model of Fig. 2.2(b)),
broadened by the same small eta in both.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import integrate, linalg

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch04")
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------------------------------------------------------------
# Worked example: level coupled to a flat band
Ew = 1.0          # eV, band width (WE 2.1)
Gam = 0.010       # eV, golden-rule rate (WE 2.1)
a = Ew / 2
eps_d = 0.0       # measured from the band centre; the chemical potential does not enter G of a quadratic model

def Sigma(z):
    """Continuum-limit self-energy; z must have Im z > 0 (or be omega + i0 via small eta)."""
    x = z - eps_d
    return Gam / (2 * np.pi) * np.log((x + a) / (x - a))

def A_exact(w, eta=1e-12):
    z = w + 1j * eta
    G = 1.0 / (z - eps_d - Sigma(z))
    return -G.imag / np.pi

def A_lor(w):
    return (Gam / 2) / np.pi / ((w - eps_d) ** 2 + Gam ** 2 / 4)

# Sigma at the level: -i Gamma/2, no shift
s0 = Sigma(eps_d + 1e-14j)
assert np.isclose(s0.real, 0.0, atol=1e-12) and np.isclose(s0.imag, -Gam / 2)
# slope of Re Sigma at the level = 2 Gamma/(pi E_w) (D.3: R'(0) = 0.0064)
h = 1e-6
slope = (Sigma(eps_d + h + 1e-14j).real - Sigma(eps_d - h + 1e-14j).real) / (2 * h)
assert np.isclose(slope, 2 * Gam / (np.pi * Ew))
zqp = 1 / (1 - slope)
print(f"WE: Re Sigma'(eps_d) = {slope:.4f}, z_qp = {zqp:.4f}")
assert np.isclose(slope, 0.0064, atol=5e-5) and np.isclose(zqp, 1.0064, atol=5e-5)
# Lorentzian weight outside the band
lor_out = 1 - (2 / np.pi) * np.arctan(a / (Gam / 2))
print(f"Lorentzian weight outside |omega - eps_d| < E_w/2: {lor_out:.4f}")
assert np.isclose(lor_out, 2 * Gam / (np.pi * Ew), rtol=1e-3)
# exact weight inside the band (bound states outside are exponentially small, ~ exp(-pi E_w/Gamma))
win, _ = integrate.quad(A_exact, -a, a, points=[0.0], limit=2000, epsabs=1e-12)
print(f"exact weight inside the band: {win:.6f}")
assert abs(win - 1) < 1e-6
# bound states outside the band: omega - eps_d = Re Sigma(omega) for |x| > a
# x - a = 2a exp(-2 pi a/Gamma) to leading order, so its weight is of order exp(-pi E_w/Gamma) = exp(-314): negligible
print(f"bound states: distance from band edge ~ 2a exp(-pi E_w/Gamma) = 1e{np.log10(2*a) - np.pi*Ew/Gam/np.log(10):.0f} eV")
# peak height 2/(pi Gamma) and comparison at 10 Gamma and 40 Gamma
peak = A_exact(eps_d)
assert np.isclose(peak, 2 / (np.pi * Gam))
for n in [1, 10, 40]:
    r = A_exact(eps_d + n * Gam) / A_lor(eps_d + n * Gam)
    print(f"A_exact/A_Lorentz at omega - eps_d = {n} Gamma: {r:.4f}")
r10 = A_exact(eps_d + 10 * Gam) / A_lor(eps_d + 10 * Gam)
assert abs(r10 - 1) < 0.02
# time domain: survival amplitude |G^R(t)| = |c_i(t)|; at t = 1/Gamma, |c|^2 vs e^{-1} (D.3: excess 0.0023)
# from the pole: |c|^2 = zqp^2 exp(-Gamma t/(1 - R'))
pole_surv = zqp ** 2 * np.exp(-1 / (1 - slope))
print(f"pole estimate of survival at t = 1/Gamma: {pole_surv:.4f}  (e^-1 = {np.exp(-1):.4f}, excess {pole_surv-np.exp(-1):.4f})")
assert np.isclose(pole_surv - np.exp(-1), 0.0023, atol=1e-4)

# direct diagonalization check, N_b = 2000 band states (WE 2.1 model)
Nb = 2000
eps_k = np.linspace(-a, a, Nb)
D = Nb / Ew
V = np.sqrt(Gam / (2 * np.pi * D))
Hm = np.zeros((Nb + 1, Nb + 1))
Hm[0, 0] = eps_d
Hm[0, 1:] = V
Hm[1:, 0] = V
Hm[np.arange(1, Nb + 1), np.arange(1, Nb + 1)] = eps_k
E, U = linalg.eigh(Hm)
wts = U[0, :] ** 2
assert np.isclose(wts.sum(), 1.0)
eta = 5 * Ew / Nb   # broadening of a few level spacings (display choice for the check)
for w0 in [0.0, 0.05, 0.1]:
    Ad = np.sum(wts * (eta / np.pi) / ((w0 - E) ** 2 + eta ** 2))
    Ae = A_exact(w0, eta=eta)
    assert abs(Ad / Ae - 1) < 0.03, (w0, Ad, Ae)
print("diagonalization agrees with the continuum A to 3% at omega - eps_d = 0, 0.05, 0.1 eV")

# ---------------------------------------------------------------------------------------------------------------------
# Matsubara checks (App. D.10)
# (1) occupation from the Matsubara sum: n = 1/2 + T sum_j Re G(i omega_j)  equals  int A n_F
T = 0.02   # eV, check value
def nF(x):
    return 0.5 * (1 - np.tanh(x / (2 * T)))
for ed in [-0.03, 0.0, 0.02]:
    eps_d = ed
    j = np.arange(0, 400000)
    wj = (2 * j + 1) * np.pi * T
    G = 1 / (1j * wj - eps_d - Sigma(1j * wj))
    n_mats = 0.5 + 2 * T * np.sum(G.real)      # j and -j-1 are complex conjugates
    n_real, _ = integrate.quad(lambda w: A_exact(w) * nF(w), ed - a, ed + a, points=[ed], limit=4000, epsabs=1e-12)
    assert abs(n_mats - n_real) < 2e-4, (ed, n_mats, n_real)
    print(f"eps_d = {ed:+.2f} eV, T = {T} eV: Matsubara n = {n_mats:.5f}, real-axis n = {n_real:.5f}")
eps_d = 0.0
# free level: T sum e^{i w 0+}/(i w - xi) = n_F(xi)
xi = 0.013
j = np.arange(-2000000, 2000000)
wj = (2 * j + 1) * np.pi * T
s = 0.5 + T * np.sum((1 / (1j * wj - xi)).real)
assert np.isclose(s, nF(xi), atol=1e-6)

# (2) two-propagator sum: T sum_j 1/((i w_j - x1)(i w_j + i nu - x2)) = (nF(x1) - nF(x2))/(i nu + x1 - x2)
x1, x2 = -0.011, 0.027
for m in [0, 1, 3]:
    nu = 2 * m * np.pi * T
    tot = T * np.sum(1 / ((1j * wj - x1) * (1j * wj + 1j * nu - x2)))
    ref = (nF(x1) - nF(x2)) / (1j * nu + x1 - x2)
    assert abs(tot - ref) < 1e-5 * abs(ref), (m, tot, ref)  # truncation of the sum at |j| = 2e6
print("two-propagator Matsubara sum agrees with (nF1 - nF2)/(i nu + x1 - x2)")

# (3) bosonic Lehmann form and continuation on a random finite system
rng = np.random.default_rng(1)
n = 6
Hr = rng.normal(size=(n, n)); Hr = (Hr + Hr.T) / 2
Er, Ur = linalg.eigh(Hr)
Er[2] = Er[1]                      # force one degeneracy to show the j = 0 term
Hd = np.diag(Er)
Aop = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
Bop = Aop.conj().T                 # O_a = O_b = O: A = O^dagger, B = O
beta = 1.3
p = np.exp(-beta * Er); p /= p.sum()
def R_tau(tau):
    # -<T O^dag(tau) O(0)> for 0 < tau < beta, in the eigenbasis (V = 1)
    ph = np.exp(np.subtract.outer(Er, Er) * tau)   # e^{(E_i - E_f) tau}
    return -np.sum(p[:, None] * Aop * Bop.T * ph)
taus = np.linspace(0, beta, 20001)
Rt = np.array([R_tau(t) for t in taus])
for m in [0, 1, 2]:
    nu = 2 * np.pi * m / beta
    Rm = integrate.simpson(np.exp(1j * nu * taus) * Rt, x=taus)
    Efi = np.subtract.outer(Er, Er).T   # [i,f] -> E_f - E_i
    num = (p[:, None] - p[None, :]) * Aop * Bop.T
    with np.errstate(divide="ignore", invalid="ignore"):
        terms = np.where(np.abs(1j * nu - Efi) > 1e-12, num / (1j * nu - Efi), 0.0)
    ref = np.sum(terms)
    if m == 0:
        # degenerate pairs E_f = E_i contribute -beta p_i A_if B_fi
        deg = np.abs(Efi) < 1e-12
        ref += -beta * np.sum((p[:, None] * Aop * Bop.T)[deg])
    assert abs(Rm - ref) < 1e-6, (m, Rm, ref)
print("bosonic Matsubara Lehmann form checked, including the beta term at j = 0")

# ---------------------------------------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 9, "axes.linewidth": 0.6, "pdf.fonttype": 42})

# Orientation: the circles in (a) run counterclockwise; the boundary of the upper half plane, traversed
# counterclockwise, is the line above the axis from left to right; that of the lower half plane is the line below
# the axis from right to left. The large arcs (dotted) contribute nothing when n_F g falls off faster than 1/|z|.
# Figure: Matsubara contour (display: T fixed, a cut on the real axis drawn from -2.2 to 2.2 in units of 2 pi T)
fig, axs = plt.subplots(1, 2, figsize=(6.4, 3.1))
for ax in axs:
    ax.axhline(0, color="0.6", lw=0.5)
    ax.axvline(0, color="0.6", lw=0.5)
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_aspect("equal")
    ax.set_xticks([]); ax.set_yticks([])
    ax.plot([-2.6, 2.6], [0, 0], color="k", lw=2.2, solid_capstyle="butt")   # branch cut of G(z)
    jj = np.arange(-3, 3)
    yj = (2 * jj + 1) * 0.5        # omega^F_j in units of 2 pi T: (2j+1)/2
    ax.plot(np.zeros_like(yj), yj, "o", ms=3.5, color="C0")
    ax.text(2.95, -0.35, r"$\mathrm{Re}\,z$", ha="right", va="top")
    ax.text(0.35, 2.45, r"$\mathrm{Im}\,z$", ha="left", va="top")   # clear of the top circle and the arc
ax = axs[0]
th = np.linspace(0, 2 * np.pi, 100)
for y in (2 * np.arange(-3, 3) + 1) * 0.5:
    if abs(y) < 2.9:
        ax.plot(0.22 * np.cos(th), y + 0.22 * np.sin(th), color="C3", lw=0.9)
ax.annotate("", xy=(0.22, 0.6), xytext=(0.22, 0.4), arrowprops=dict(arrowstyle="-|>", color="C3", lw=0.8))
ax.text(0.35, 1.5, r"$\mathrm{i}\omega^{\mathrm{F}}_j$", color="C0")
ax.text(-2.8, 0.2, r"cut of $\mathsf{G}(z)$", fontsize=8)
ax.set_title("(a)", loc="left")
ax = axs[1]
d = 0.2
ax.plot([2.6, -2.6], [d, d], color="C3", lw=0.9)
ax.plot([-2.6, 2.6], [-d, -d], color="C3", lw=0.9)
ax.annotate("", xy=(1.2, d), xytext=(0.9, d), arrowprops=dict(arrowstyle="-|>", color="C3", lw=0.8))
ax.annotate("", xy=(-1.2, -d), xytext=(-0.9, -d), arrowprops=dict(arrowstyle="-|>", color="C3", lw=0.8))
arc = np.linspace(np.arcsin(d / 2.75), np.pi - np.arcsin(d / 2.75), 100)
ax.plot(2.75 * np.cos(arc), 2.75 * np.sin(arc), color="C3", lw=0.6, ls=":")
ax.plot(2.75 * np.cos(arc), -2.75 * np.sin(arc), color="C3", lw=0.6, ls=":")
ax.text(1.0, 0.35, r"$\omega + \mathrm{i}0^+$", fontsize=8, color="C3")
ax.text(0.9, -0.75, r"$\omega - \mathrm{i}0^+$", fontsize=8, color="C3")
ax.set_title("(b)", loc="left")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig4_8.pdf"))

# Figure: worked example
fig, ax = plt.subplots(figsize=(4.6, 3.0))
w = np.linspace(-0.7, 0.7, 28001)
ax.semilogy(w / Gam, np.where(np.abs(w) < a, A_exact(w), np.nan), color="k", lw=1.2, label=r"exact, $\Sigma$ of the flat band")
ax.semilogy(w / Gam, A_lor(w), color="C1", lw=1.0, ls="--", label=r"Lorentzian, width $\mathit{\Gamma}$")
ax.axvspan(-70, -a / Gam, color="0.9"); ax.axvspan(a / Gam, 70, color="0.9")
ax.set_xlim(-70, 70); ax.set_ylim(1e-3, 1e2)
ax.set_xlabel(r"$(\omega - E_{\mathrm{lev}})/\mathit{\Gamma}$")
ax.set_ylabel(r"$\mathsf{A}(\omega)$  [eV$^{-1}$]")
ax.legend(frameon=False, fontsize=8, loc="upper right")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig4_8b.pdf"))
print("figures written")
