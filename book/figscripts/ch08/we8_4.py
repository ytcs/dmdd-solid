"""Numbers of Sect. 8.3, Worked example 8.4: the mixed electron-nucleus third moment of silicon.

Formula (derived in Sect. 8.3 and App. D.26, for point nuclei, nonrelativistic electrons, local potentials, a density
spherical about the nucleus):
    M3_ek(q) = -(Z e^2 q^2 n_k / (m_e M_k)) * B(q),
    B(q)     = n_e^(k)/3 + 2 * int_0^inf drho nbar(rho) j_2(q rho)/rho,
with nbar the spherically averaged electron density about the nucleus and n_e^(k) = nbar(0) the contact density.
Limits: B -> [n_e^(k) + 2 n_e]/3 as q -> 0 in the crystal (n_e = mean electron density; the 2 n_e/3 is the uniform part,
which a free-atom density lacks), B -> n_e^(k) for q >> inverse core size (since int_0^inf j_2(x)/x dx = 1/3).
Equivalent momentum-space form (cross-check below): B(q) = int d^3p/(2pi)^3 A(p/q) ntilde(p),
    A(x) = (1/2) int_{-1}^{1} du (1 - x u)^2 / (1 + x^2 - 2 x u),  A(0) = 1, A(inf) = 1/3.

Inputs and modelling choices:
  - Free-atom Si density from all-electron restricted open-shell Hartree-Fock (3P ground state, PySCF), basis: the
    uncontracted cc-pwCV5Z set for Si plus six even-tempered tight s functions (ratio 3). Total energy compared with the
    Roothaan-HF value -288.854 hartree of Bunge et al. (1993), as quoted in Sect. 4.3. Contact density converges to
    ~0.1 % with the tight functions (printed). The crystal valence is replaced by the atomic 3s^2 3p^2 shell (modelling
    choice; at q = 10 keV the kernel samples rho ~ 1/q = 0.37 bohr, inside the atom).
  - Core = 1s 2s 2p (10 electrons), valence = 3s 3p (4 electrons).
  - Mean electron density of silicon, all 14 electrons: 7.00e23 cm^-3 (Sect. 4.3).
  - Z = 14; M_Si = 26.16 GeV (natural mass, Sect. 5.6); m_e = 510998.95 eV; 1/a0 = 3728.94 eV (alpha m_e).
  - Nonrelativistic point-nucleus density; the relativistic finite-nucleus correction (+8 % in Si) belongs to Sect. 12.5.
Units: hartree atomic units inside; e^2 (Heaviside-Lorentz, as in the book) = 4 pi in these units.
Runtime: about 1.5 min (three ROHF runs).
"""
import numpy as np
from scipy.special import spherical_jn
from scipy.integrate import quad
from pyscf import gto, scf

a0_cm = 0.529177210903e-8
au_to_cm3 = 1 / a0_cm**3          # 1 bohr^-3 in cm^-3
inv_a0_eV = 3728.94               # alpha m_e in eV (1 bohr^-1)
Ha_eV = 27.211386
Z = 14

# --- atomic ROHF ---------------------------------------------------------------------------------------
b = gto.uncontract(gto.load('cc-pwcv5z', 'Si'))
smax = max(e[1][0] for e in b if e[0] == 0)
extra = [[0, [smax * 3.0 ** (k + 1), 1.0]] for k in range(6)]
mol = gto.M(atom='Si 0 0 0', basis={'Si': b + extra}, spin=2, verbose=0)
mf = scf.ROHF(mol)
mf.conv_tol = 1e-10
E = mf.kernel()
print(f"ROHF total energy {E:.5f} hartree (Bunge et al. 1993: -288.854)")

C = mf.mo_coeff
occ = mf.mo_occ
order = np.argsort(mf.mo_energy)
occ_idx = [i for i in order if occ[i] > 0]
core_idx = occ_idx[:5]            # 1s, 2s, 2p x3
val_idx = occ_idx[5:]             # 3s (2), 3p (1 + 1)
print("orbital energies (hartree):", np.round(mf.mo_energy[occ_idx], 3), "occ:", occ[occ_idx])
print(f"1s orbital energy: {-mf.mo_energy[occ_idx[0]]*27.211386/1e3:.3f} keV")

# radial grid (log) and product angular grid (Gauss-Legendre in cos theta x uniform phi): exact for the low-l density
r = np.logspace(-7, np.log10(40.0), 6000)
xg, wg = np.polynomial.legendre.leggauss(16)
nphi = 32
phi = 2 * np.pi * np.arange(nphi) / nphi
ct, ph = np.meshgrid(xg, phi, indexing='ij')
st = np.sqrt(1 - ct**2)
dirs = np.stack([st * np.cos(ph), st * np.sin(ph), ct], axis=-1).reshape(-1, 3)
wang = (np.repeat(wg, nphi) * (2 * np.pi / nphi)) / (4 * np.pi)     # sums to 1


def nbar(idx):
    out = np.zeros_like(r)
    for k in range(0, len(r), 500):
        rr = r[k:k + 500]
        pts = (rr[:, None, None] * dirs[None, :, :]).reshape(-1, 3)
        ao = mol.eval_gto('GTOval', pts)
        mo = ao @ C[:, idx]
        dens = (mo**2 * occ[idx]).sum(axis=1).reshape(len(rr), -1)
        out[k:k + 500] = dens @ wang
    return out


n_core = nbar(core_idx)
n_val = nbar(val_idx)
n_tot = n_core + n_val
lnr = np.log(r)
N_check = np.trapezoid(4 * np.pi * r**3 * n_tot, lnr)
print(f"electron count from the radial density: {N_check:.5f}")

ao0 = mol.eval_gto('GTOval', np.zeros((1, 3)))
mo0 = (ao0 @ C)[0]
rho0_core = float((mo0[core_idx]**2 * occ[core_idx]).sum())
rho0_val = float((mo0[val_idx]**2 * occ[val_idx]).sum())
rho0 = rho0_core + rho0_val
print(f"contact density n_e^(k) = {rho0:.1f} bohr^-3 = {rho0*au_to_cm3:.3e} cm^-3 (core {rho0_core:.1f}, valence {rho0_val:.2f}, "
      f"valence share {rho0_val/rho0:.2e})")

# convergence of the contact density with the tight s functions
for nt in (0, 3):
    m2 = gto.M(atom='Si 0 0 0', basis={'Si': b + extra[:nt]}, spin=2, verbose=0)
    f2 = scf.ROHF(m2); f2.conv_tol = 1e-10; f2.kernel()
    d2 = f2.make_rdm1(); d2 = d2[0] + d2[1]
    a2 = m2.eval_gto('GTOval', np.zeros((1, 3)))
    print(f"  contact density with {nt} tight s functions: {float(a2[0] @ d2 @ a2[0]):.1f}")

# --- the bracket B(q) ---------------------------------------------------------------------------------
I_j2 = quad(lambda x: spherical_jn(2, x) / x, 0, 200, limit=2000)[0]
print(f"int_0^200 j_2(x)/x dx = {I_j2:.5f} (exact 1/3 to the upper limit)")


def far(nb, q):
    return 2 * np.trapezoid(nb * spherical_jn(2, q * r) / r * r, lnr)


ne_mean_cm3 = 7.00e23
ne_mean = ne_mean_cm3 / au_to_cm3
print(f"mean electron density 7.00e23 cm^-3 = {ne_mean:.4f} bohr^-3; 2 n_e / n_e^(k) = {2*ne_mean/rho0:.2e}")

q_keV = 10.0
q = q_keV * 1e3 / inv_a0_eV
print(f"q = {q_keV} keV = {q:.3f} bohr^-1, 1/q = {1/q:.3f} bohr = {0.529177/q:.4f} A")
Bc_contact, Bv_contact = rho0_core / 3, rho0_val / 3
Bc_far, Bv_far = far(n_core, q), far(n_val, q)
B = Bc_contact + Bv_contact + Bc_far + Bv_far
print(f"B(10 keV) = {B:.1f} bohr^-3: core contact {Bc_contact:.1f}, core far {Bc_far:.2f}, valence contact {Bv_contact:.2f}, "
      f"valence far {Bv_far:.2f}")
print(f"  core share {(Bc_contact+Bc_far)/B:.4f}, valence share {(Bv_contact+Bv_far)/B:.2e}")
print(f"  B / n_e^(k) = {B/rho0:.4f} (1/3 at q -> 0, 1 at q -> inf)")
B0 = (rho0 + 2 * ne_mean) / 3
print(f"B(q->0) in the crystal = {B0:.2f} bohr^-3; B(10 keV)/B(0) = {B/B0:.4f}")
print(f"crystal uniform term at most n_e = {ne_mean:.3f} bohr^-3 = {ne_mean/B:.1e} of B(10 keV)")
for qq in (1.0, 3.0, 10.0, 30.0, 100.0):
    qa = qq * 1e3 / inv_a0_eV
    Bq = rho0 / 3 + far(n_tot, qa)
    print(f"  q = {qq:6.1f} keV: B/n_e^(k) = {Bq/rho0:.4f}")

# momentum-space cross-check of the kernel (identity check on Gaussian model densities with analytic transforms)
uu, ww = np.polynomial.legendre.leggauss(200)


def A(x):
    x = np.atleast_1d(x)[:, None]
    return 0.5 * np.sum(ww * (1 - x * uu)**2 / (1 + x**2 - 2 * x * uu), axis=1)


p = np.logspace(-4, 3, 3000)
for sg in (0.05, 0.37, 2.0):          # widths below, at and above 1/q (bohr)
    ng = np.exp(-r**2 / (2 * sg**2))
    B_real = 1 / 3 + far(ng, q)
    ntg = (2 * np.pi * sg**2)**1.5 * np.exp(-p**2 * sg**2 / 2)
    B_mom = np.trapezoid(4 * np.pi * p**3 * A(p / q) * ntg / (2 * np.pi)**3, np.log(p))
    print(f"  Gaussian width {sg} bohr: B/n(0) real space {B_real:.5f}, momentum space {B_mom:.5f}")
print(f"  A(0) = {A(1e-6)[0]:.4f}, A(inf) = {A(1e4)[0]:.4f}")

# --- numbers quoted in the worked example ---------------------------------------------------------------
e2 = 4 * np.pi                                     # Heaviside-Lorentz e^2 in hartree units (m_e = 1)
ratio = Z * e2 * B                                  # -M3_ek / M1_kk = Z e^2 B / m_e, hartree^2
print(f"-M3_ek / M1_kk = Z e^2 B / m_e = ({np.sqrt(ratio)*Ha_eV/1e3:.2f} keV)^2")
ratio0 = Z * e2 * B0
print(f"   q -> 0: ({np.sqrt(ratio0)*Ha_eV/1e3:.2f} keV)^2")
# Ward check: the q^2 part of M3_ee / M1_ee = e^2 B Z n_k/n_e / m_e with Z n_k = n_e for neutral monatomic
print(f"q^2 part of M3_ee / M1_ee = e^2 B(0)/m_e = ({np.sqrt(e2*B0)*Ha_eV/1e3:.2f} keV)^2; at 10 keV with B: ({np.sqrt(e2*B)*Ha_eV/1e3:.2f} keV)^2")
m_e = 510998.95
Kbar = 561.0
qe = q_keV * 1e3
print(f"kinetic terms of M3_ee/M1_ee at 10 keV: (q^2/2m)^2 = ({qe**2/(2*m_e):.1f} eV)^2, 2 q^2 Kbar/m = ({np.sqrt(2*qe**2*Kbar/m_e):.0f} eV)^2")

# --- cache: key numbers (json) and the radial densities (npz), so that the quoted values can be checked without PySCF --------
import json
import os
_here = os.path.dirname(os.path.abspath(__file__))
_Bq = {f"{qq:g}": float((rho0 / 3 + far(n_tot, qq * 1e3 / inv_a0_eV)) / rho0) for qq in (1.0, 3.0, 10.0, 30.0, 100.0)}
with open(os.path.join(_here, "we8_4_out.json"), "w") as fh:
    json.dump(dict(E_ROHF_hartree=float(E), contact_density_bohr3=rho0, contact_core=rho0_core, contact_valence=rho0_val,
                   contact_density_cm3=rho0 * au_to_cm3, electron_count=float(N_check), B_over_n0=_Bq,
                   core_share_10keV=float((Bc_contact + Bc_far) / B), sqrt_ratio_keV=float(np.sqrt(ratio) * Ha_eV / 1e3),
                   sqrt_ratio0_keV=float(np.sqrt(ratio0) * Ha_eV / 1e3),
                   e1s_keV=float(-mf.mo_energy[occ_idx[0]] * Ha_eV / 1e3)), fh, indent=1)
np.savez_compressed(os.path.join(_here, "we8_4_density.npz"), r_bohr=r, n_core=n_core, n_val=n_val)
print("cached we8_4_out.json and we8_4_density.npz")
