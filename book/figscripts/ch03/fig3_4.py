"""Fig. 3.4: nearly-free-electron bands of a one-dimensional crystal and the density vertex between its two lowest bands
(Sect. 3.2); the numbers of Worked examples 3.3 and 3.4. Output: tex/figures/ch03/fig3_4.pdf.

Model (definitions and modelling choices, no external input beyond the constants below):
  one electron in one dimension, h = p^2/2m_e + U(x), period a, reciprocal vectors G_j = j G1 with G1 = 2pi/a;
  U(x) = sum_G U_G exp(-i G x) (the book's lattice convention, App. A.3) with only U_{+-G1} = U1 nonzero:
  U(x) = 2 U1 cos(G1 x). Modelling choices: a = 5.431 A (the silicon lattice constant, used only to set the scale)
  and U1 = -0.5 eV (attractive at the lattice sites x = R; the magnitude is chosen so that the first gap is ~1 eV,
  like silicon's). The Bloch states are expanded in plane waves exp(i(k+G)x), G = j G1 with |j| <= JMAX = 12
  (25 plane waves; the lowest four bands change by < 1e-9 eV from JMAX = 8 to 12). The Hamiltonian matrix in this basis is
  H_{GG'} = delta_{GG'} (k+G)^2/2m_e + U_{G'-G}, and the eigenvector c_nk(G) is the coefficient of exp(iGx) in u_nk,
  the code convention of App. E.7. Vertex (Sect. 3.2): k+q = k' + G_U with k' in the zone,
  rho_mn(k,q) = sum_G c*_{m k'}(G + G_U) c_{nk}(G); velocity v_mn(k) = sum_G c*_mk(G) (k+G)/m_e c_nk(G).

Inputs and their sources:
  a = 5.431 A                  (CODATA 2022, Mohr et al., RMP 97, 025002 (2025), lattice parameter of silicon)
  hbar c = 1973.2698 eV A      (CODATA 2018)
  m_e = 510998.95 eV           (CODATA 2018)
  v_max = 2.650e-3             (Sect. 1.2 of the book)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HBARC = 1973.2698          # eV A
A = 5.431                  # A
ME = 510998.95             # eV
U1 = -0.5                  # eV (modelling choice)
VMAX = 2.650e-3
JMAX = 12
G1 = 2 * np.pi * HBARC / A  # eV
JS = np.arange(-JMAX, JMAX + 1)


def solve(k, jmax=JMAX):
    js = np.arange(-jmax, jmax + 1)
    H = np.diag((k + js * G1) ** 2 / (2 * ME)).astype(complex)
    for i, j in enumerate(js):
        for ip, jp in enumerate(js):
            if abs(jp - j) == 1:
                H[i, ip] += U1          # U_{G'-G} with G'-G = +-G1
    e, c = np.linalg.eigh(H)
    return e, c, js


def fold(kq):
    """k + q = k' + G_U with k' in [-G1/2, G1/2); returns k', integer jU (G_U = jU G1)."""
    jU = int(np.floor((kq + G1 / 2) / G1))
    return kq - jU * G1, jU


def rho(m, n, k, q):
    e1, c1, js = solve(k)
    kp, jU = fold(k + q)
    e2, c2, _ = solve(kp)
    # sum_G c*_{m k'}(G + G_U) c_{n k}(G)
    s = 0j
    for i, j in enumerate(js):
        jj = j + jU
        if -JMAX <= jj <= JMAX:
            s += np.conj(c2[jj + JMAX, m]) * c1[i, n]
    return s, e1, e2, jU


def vel(m, n, k):
    e, c, js = solve(k)
    return np.sum(np.conj(c[:, m]) * (k + js * G1) / ME * c[:, n]), e


# ---- convergence check -------------------------------------------------------------------------------------------
for k in [0.0, 0.3 * G1, -G1 / 2]:
    d = np.max(np.abs(solve(k, 8)[0][:4] - solve(k, 12)[0][:4]))
    assert d < 1e-9, d

# ---- Worked example 3.3: the gaps ----------------------------------------------------------------------------------
eps0_b = (G1 / 2) ** 2 / (2 * ME)           # free energy at the zone boundary
eps0_G = G1 ** 2 / (2 * ME)                  # free energy at k = G1
e_b, c_b, _ = solve(-G1 / 2)
e_0, c_0, _ = solve(0.0)
gap1 = e_b[1] - e_b[0]
gap2 = e_0[2] - e_0[1]
gap2_est = 2 * U1 ** 2 / eps0_G             # second order: effective coupling U1^2/(eps0(G1) - eps0(0))
print(f"G1 = 2pi/a = {G1:.1f} eV;  free energy at the boundary (G1/2)^2/2m = {eps0_b:.4f} eV; at G1: {eps0_G:.3f} eV")
print(f"first gap (k = G1/2): exact {gap1:.4f} eV, two-wave 2|U1| = {2*abs(U1):.4f} eV;"
      f" band edges {e_b[0]:.4f}, {e_b[1]:.4f} eV (two-wave: {eps0_b-abs(U1):.4f}, {eps0_b+abs(U1):.4f})")
print(f"second gap (k = 0): exact {gap2:.4f} eV, second-order estimate 2U1^2/eps0(G1) = {gap2_est:.4f} eV;"
      f" edges {e_0[1]:.4f}, {e_0[2]:.4f} eV")
print(f"lowest state at k=0: {e_0[0]:.4f} eV (second order: {-2*U1**2/eps0_G:.4f} eV)")
# which standing wave is lower at the boundary: weight of the lower state at x = 0 versus x = a/2
x = np.array([0.0, A / 2])
js = JS
for n in (0, 1):
    psi = np.array([np.sum(c_b[:, n] * np.exp(1j * (-G1 / 2 + js * G1) * xx / HBARC)) for xx in x])
    print(f"boundary band {n+1}: |psi(0)|^2 / |psi(a/2)|^2 = {abs(psi[0])**2:.3f} / {abs(psi[1])**2:.3f}")
assert abs(gap1 - 2 * abs(U1)) < 0.01
assert abs(gap2 - gap2_est) / gap2 < 0.1

# ---- Worked example 3.4: rho_21 at the left zone boundary ----------------------------------------------------------
k0 = -G1 / 2
mixw = 4 * ME * abs(U1) / G1                 # q scale of the two-wave mixing at the boundary
v21, e_k0 = vel(1, 0, k0)
print(f"\nk = -pi/a: eps_1 = {e_k0[0]:.4f}, eps_2 = {e_k0[1]:.4f} eV; |v_21| = {abs(v21):.4e}"
      f" (two-wave G1/2m_e = {G1/(2*ME):.4e}); v_11 = {vel(0,0,k0)[0].real:.2e}")
print(f"two-wave mixing scale 4 m_e |U1| / G1 = {mixw:.1f} eV = {mixw/G1:.3f} (2pi/a)")
qmin = 2 * abs(U1) / VMAX
print(f"E_gap/v_max = {qmin:.0f} eV")


def two_wave_rho21(k, q):
    """two-plane-wave model for k, k+q in [-G1/2, ...] built from exp(ikx) and exp(i(k+G1)x)."""
    def theta(kk):
        d = ((kk + G1) ** 2 - kk ** 2) / (2 * ME)          # eps0_{k+G1} - eps0_k
        return 0.5 * np.arctan2(2 * abs(U1), d)
    return abs(np.sin(theta(k + q) - theta(k)))


rows = []
for q in [10.0, 50.0, 100.0, 200.0, 400.0, qmin]:
    r, e1, e2, jU = rho(1, 0, k0, q)
    opt = abs(q * v21 / (e_k0[1] - e_k0[0]))
    tot = sum(abs(rho(m, 0, k0, q)[0]) ** 2 for m in range(2 * JMAX + 1))
    assert abs(tot - 1) < 1e-10
    assert jU == 0
    rows.append((q, abs(r), opt, two_wave_rho21(k0, q), e2[1] - e1[0]))
    print(f"q = {q:6.1f} eV: |rho_21| exact {abs(r):.4f}, optical q|v21|/(e2-e1) {opt:.4f}, two-wave {two_wave_rho21(k0,q):.4f};"
          f" omega = eps_2(k+q) - eps_1(k) = {e2[1]-e1[0]:.4f} eV; sum_m |rho_m1|^2 = {tot:.12f}")
# Umklapp: q = G1 takes k = -pi/a to k + q = +pi/a, folded back to -pi/a with G_U = G1
r21U, e1, e2, jU = rho(1, 0, k0, G1)
r11U = rho(0, 0, k0, G1)[0]
w = [abs(rho(m, 0, k0, G1)[0]) ** 2 for m in range(6)]
print(f"\nUmklapp q = G1 = {G1:.0f} eV, G_U index {jU}: |rho_21| = {abs(r21U):.4f} (two-wave 1/2), |rho_11| = {abs(r11U):.4f};"
      f" |rho_m1|^2 for m = 1..6: {', '.join(f'{x:.4f}' for x in w)}; sum = {sum(abs(rho(m,0,k0,G1)[0])**2 for m in range(25)):.10f}")
assert jU == 1
# normalization rho_nn(k,0) = 1 at a generic k
assert abs(rho(0, 0, 0.17 * G1, 0.0)[0] - 1) < 1e-12
# group velocity = v_nn: finite difference
kk, dk = 0.23 * G1, 1e-3
vg = (solve(kk + dk)[0][0] - solve(kk - dk)[0][0]) / (2 * dk)
assert abs(vg - vel(0, 0, kk)[0].real) < 1e-9
print(f"group velocity check at k = 0.23 G1: d eps/dk = {vg:.6e}, v_11 = {vel(0,0,kk)[0].real:.6e}")

# ---- figure -------------------------------------------------------------------------------------------------------
plt.rcParams.update({"font.size": 9})
fig, (ax, bx) = plt.subplots(1, 2, figsize=(7.0, 3.3), gridspec_kw={"width_ratios": [1, 1.1]})
ks = np.linspace(-G1 / 2, G1 / 2, 401)
bands = np.array([solve(k)[0][:4] for k in ks])
for j in range(-2, 3):
    ax.plot(ks / G1, (ks + j * G1) ** 2 / (2 * ME), color="0.6", ls="--", lw=0.7)
for n in range(4):
    ax.plot(ks / G1, bands[:, n], color="#08519c", lw=1.4)
ax.annotate("", xy=(-0.47, e_b[1]), xytext=(-0.47, e_b[0]), arrowprops=dict(arrowstyle="<->", color="#cb181d", lw=0.9))
ax.text(-0.44, 0.5 * (e_b[0] + e_b[1]), rf"$2|U_{{G_1}}|$", color="#cb181d", va="center", fontsize=8)
ax.annotate("", xy=(0.02, e_0[2]), xytext=(0.02, e_0[1]), arrowprops=dict(arrowstyle="<->", color="#cb181d", lw=0.9))
ax.text(0.06, e_0[2] + 0.25, f"{gap2*1e3:.0f} meV", color="#cb181d", fontsize=8)
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.6, 14.2)                    # tall enough to show band 4, which starts at 11.4 eV at the zone edge
ax.set_xlabel(r"$k\;[2\pi/a]$")
ax.set_ylabel(r"$\varepsilon_{nk}$ [eV]")
ax.set_xticks([-0.5, -0.25, 0, 0.25, 0.5])
ax.text(0.02, 0.97, "(a)", fontsize=9, transform=ax.transAxes, va="top")
for n, (x, y) in enumerate([(0.36, -0.45), (0.36, 2.6), (0.08, 8.0), (0.2, 12.8)]):   # each next to its band
    ax.text(x, y, f"$n={n+1}$", fontsize=7, color="#08519c")

qs = np.linspace(1, 900, 300)
ex = [abs(rho(1, 0, k0, q)[0]) for q in qs]
bx.plot(qs / 1e3, ex, color="#08519c", lw=1.4, label=r"exact, $|\rho_{21}(k,q)|$")
bx.plot(qs / 1e3, [two_wave_rho21(k0, q) for q in qs], color="#41ab5d", ls=":", lw=1.4, label="two plane waves")
bx.plot(qs / 1e3, qs * abs(v21) / (e_k0[1] - e_k0[0]), color="#cb181d", ls="--", lw=1.0,
        label=r"optical limit $q|v_{21}|/(\varepsilon_{2k}-\varepsilon_{1k})$")
bx.axvline(qmin / 1e3, color="0.5", lw=0.6)
bx.text(qmin / 1e3 - 0.01, 0.96, r"$2|U_{G_1}|/v_{\max}$", fontsize=7, color="0.35", ha="right")   # left of the line, off the optical limit
bx.set_xlim(0, 0.9)
bx.set_ylim(0, 1.05)
bx.set_xlabel(r"$q$ [keV]")
bx.set_ylabel(r"$|\rho_{21}(k{=}-\pi/a,\,q)|$")
bx.legend(fontsize=7, loc="lower right", frameon=False)
bx.text(0.02, 0.97, "(b)", fontsize=9, va="top")
fig.tight_layout()
out = os.path.join(os.path.dirname(__file__), "..", "..", "tex", "figures", "ch03", "fig3_4.pdf")
fig.savefig(out)
print("wrote", os.path.normpath(out))
