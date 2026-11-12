"""Worked example 14.2: the hybridization gap of a model ferromagnet (Sect. 14.2). Log: we14_2.log.

Model (named in the worked example): a continuum ferromagnet with the long-wavelength constants of yttrium iron garnet,
magnetization along z, wavevector k along z (no magnetostatic term for k parallel to M), one effective spin of length
|S| = M_s a^3 / (2 mu_B) per cubic cell, magnon energy omega_m(k) = omega_Lar + D_sw k^2, transverse acoustic phonons
omega_p = c_TA k, the shear magnetoelastic energy density f = B_2 sum_{alpha != beta} m_alpha m_beta X_alpha beta
(m = M/M_s, X the strain), which gives per cell the magnon-phonon vertex of Sect. 14.2,
   g_k = B_me k / (2 |S| M_cell omega_p(k))^(1/2),   B_me = B_2 a^3,  M_cell = rho_T a^3,
coupling the magnon to the co-rotating circular transverse phonon.  Illustrative field B = 0.1 T (omega_Lar = 2 mu_B B).
Inputs (sources):
  a = 12.3750 A: Nakatsuka, Yoshiasa and Takeno, Acta Cryst. B 51, 737 (1995) (state/DATA-ADDENDA.csv, YIG a_exp);
  rho_T = 5.17 g/cm^3, c_TA = 3.843e5 cm/s, B_2 = 6.96e6 erg/cm^3, 4 pi M_s = 1750 G, exchange stiffness
     D_sw = 2 mu_B x 5.17e-9 Oe cm^2: Rueckriegel et al., PRB 89, 184413 (2014), arXiv:1402.6575, Eqs. (2.13),
     (3.7), (3.15), (3.16) and the text after Eq. (2.4).
  mu_B = 5.7883818e-5 eV/T; hbar = 6.582119569e-16 eV s; hbar c = 197.3269804 eV nm; u = 931.494e6 eV;
  1 erg = 6.241509e11 eV; c = 2.99792458e10 cm/s (CODATA).
Check: the rotating-wave gap 2 g is compared with the exact eigenvalues of the full quadratic boson Hamiltonian of the
  modes +-k (magnon, two transverse phonons, all counter-rotating terms kept), diagonalized by Colpa's method.
"""
import numpy as np

MUB, HBAR, HBARC, ERG = 5.7883818e-5, 6.582119569e-16, 197.3269804, 6.241509e11
CLIGHT = 2.99792458e10
a_nm = 1.23750
a_cm = a_nm * 1e-7
rho, cta_cms, B2, fourpiMs = 5.17, 3.843e5, 6.96e6, 1750.0
Bfield = 0.1  # tesla, illustrative

Ms = fourpiMs / (4 * np.pi)                       # emu/cm^3 = erg G^-1 cm^-3
mub_erg = 9.2740100783e-21                        # erg/G
S = Ms * a_cm**3 / (2 * mub_erg)
Bme = B2 * a_cm**3 * ERG                          # eV per cell
Mcell = rho * a_cm**3 / 1.66053906660e-24 * 931.49410242e6   # eV (rest energy)
cta = cta_cms / CLIGHT                            # dimensionless
Dsw = 2 * MUB * 5.17e-9 * 1e-4 * 1e-4             # eV m^2: Oe -> T (1e-4), cm^2 -> m^2 (1e-4)
Dsw_nm2 = Dsw * 1e18                              # eV nm^2
wlar = 2 * MUB * Bfield                           # eV
print(f"effective spin |S| = {S:.2f}; B_me = B_2 a^3 = {Bme*1e3:.3f} meV; M_cell = {Mcell/1e12:.3f} TeV")
print(f"c_TA = {cta:.4e} (hbar c_TA = {cta*HBARC*1e3:.3f} meV nm); D_sw = {Dsw_nm2*1e3:.3f} meV nm^2; "
      f"omega_Lar(0.1 T) = {wlar*1e6:.2f} ueV = {wlar/HBAR/2/np.pi/1e9:.3f} GHz")

# crossings omega_Lar + D k^2 = c k, k in nm^-1
cn = cta * HBARC                                  # eV nm
disc = cn**2 - 4 * Dsw_nm2 * wlar
kx = [(cn - np.sqrt(disc)) / (2 * Dsw_nm2), (cn + np.sqrt(disc)) / (2 * Dsw_nm2)]


def g_of_k(k_nm):
    k_ev = k_nm * HBARC
    wp = cta * k_ev
    return Bme * k_ev / np.sqrt(2 * S * Mcell * wp)


for i, k in enumerate(kx):
    w = cn * k
    g = g_of_k(k)
    slope_diff = abs(cn - 2 * Dsw_nm2 * k)
    dk = 2 * g / slope_diff
    print(f"crossing {i+1}: k = {k:.4e} nm^-1 (k a = {k*a_nm:.3e}); omega = {w*1e6:.3f} ueV = {w/HBAR/2/np.pi/1e9:.3f} GHz; "
          f"g = {g*1e9:.2f} neV; gap 2g = {2*g*1e6:.4f} ueV = {2*g/HBAR/2/np.pi/1e6:.1f} MHz; 2g/omega = {2*g/w:.4f}; "
          f"k window 2g/|c - 2Dk| = {dk:.3e} nm^-1 = {dk/k:.4f} k")


# ---- Colpa check at the lower crossing ------------------------------------------------------------------------------
def colpa(terms, n):
    """terms: list of (coef, (i, dag_i), (j, dag_j)); returns positive eigenvalues of eta H for H = sum coef X Y."""
    H0 = np.zeros((2 * n, 2 * n), complex)

    def left(i, d):   # X as a component of Psi^dagger = (c^dag, c)
        return i if d else n + i

    def right(j, d):  # Y as a component of Psi = (c, c^dag)
        return n + j if d else j
    for c, (i, di), (j, dj) in terms:
        H0[left(i, di), right(j, dj)] += c
    # XY = YX + const: symmetrize, H = (1/2) Psi^dag (H0 + H0_swap) Psi
    Hs = np.zeros_like(H0)
    for x in range(2 * n):
        for y in range(2 * n):
            xb = (x + n) % (2 * n)
            yb = (y + n) % (2 * n)
            Hs[yb, xb] += H0[x, y]
    Hm = H0 + Hs
    assert np.allclose(Hm, Hm.conj().T)
    eta = np.diag([1] * n + [-1] * n)
    ev = np.linalg.eigvals(eta @ Hm)
    return np.sort(ev.real[ev.real > 0])


k = kx[0]
k_ev = k * HBARC
wm = wlar + Dsw * 1e18 * k**2
wp = cta * k_ev
C = Bme * np.sqrt(2 / S)
idx = {"b+": 0, "b-": 1, "x+": 2, "x-": 3, "y+": 4, "y-": 5}
terms = []
for s in ("+", "-"):
    terms.append((wm, (idx["b" + s], True), (idx["b" + s], False)))
    terms.append((wp, (idx["x" + s], True), (idx["x" + s], False)))
    terms.append((wp, (idx["y" + s], True), (idx["y" + s], False)))
# H_int = sum_{kappa = +-k} i g0_kappa [beta_{-kappa} phi_{kappa x} + gamma_{-kappa} phi_{kappa y}]
# beta_kappa = b_kappa + b^dag_{-kappa}; gamma_kappa = -i (b_kappa - b^dag_{-kappa}); phi_{kappa a} = a_{kappa a} + a^dag_{-kappa a}
for s, sgn in (("+", 1), ("-", -1)):
    ms = "-" if s == "+" else "+"
    g0 = sgn * C * k_ev / (2 * np.sqrt(2 * Mcell * wp))
    beta = [(1, (idx["b" + ms], False)), (1, (idx["b" + s], True))]           # b_{-kappa} + b^dag_{kappa}
    gamma = [(-1j, (idx["b" + ms], False)), (1j, (idx["b" + s], True))]       # -i b_{-kappa} + i b^dag_{kappa}
    phix = [(1, (idx["x" + s], False)), (1, (idx["x" + ms], True))]
    phiy = [(1, (idx["y" + s], False)), (1, (idx["y" + ms], True))]
    for cb, ob in beta:
        for cp, op in phix:
            terms.append((1j * g0 * cb * cp, ob, op))
    for cb, ob in gamma:
        for cp, op in phiy:
            terms.append((1j * g0 * cb * cp, ob, op))
ev = colpa(terms, 6)
g = g_of_k(k)
w_rwa = [0.5 * (wm + wp) - np.sqrt(0.25 * (wm - wp)**2 + g**2), 0.5 * (wm + wp) + np.sqrt(0.25 * (wm - wp)**2 + g**2)]
print("Colpa eigenvalues at the lower crossing (ueV):", np.round(ev * 1e6, 6))
hyb = [e for e in ev if abs(e - wp) < 10 * g]
gap_full = max(hyb) - min(hyb)
print(f"  full gap = {gap_full*1e6:.6f} ueV; rotating-wave 2g = {(w_rwa[1]-w_rwa[0])*1e6:.6f} ueV; "
      f"relative difference = {(gap_full-(w_rwa[1]-w_rwa[0]))/(w_rwa[1]-w_rwa[0]):.2e}; (g/omega)^2 = {(g/wp)**2:.2e}")

# ---- off-resonant leakage relevant to absorption -------------------------------------------------------------------
v = 1e-3
p = wlar * v                     # momentum of a field of mass omega_Lar (eV)
gp = Bme * p / np.sqrt(2 * S * Mcell * cta * p)
det = wlar - cta * p
print(f"absorption at m_phi = omega_Lar: p = m v = {p:.3e} eV = {p/HBARC:.3e} nm^-1 (k_x/p = {kx[0]*HBARC/p:.2e}); "
      f"g(p) = {gp:.3e} eV; phonon content (g/Delta)^2 = {(gp/det)**2:.2e}")
# phonon content at a detuning of 10 g near the lower crossing
print(f"  hybrid contents at detuning Delta = omega_m - omega_p: |X^p|^2 = (1/2)(1 - |Delta|/sqrt(Delta^2 + 4 g^2)); "
      f"Delta = 2g: {0.5*(1-2/np.sqrt(4+4)):.3f}; Delta = 10g: {0.5*(1-10/np.sqrt(100+4)):.4f}")
