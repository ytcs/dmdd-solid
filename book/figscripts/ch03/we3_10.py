"""Worked example of Sect. 3.6 (we:3-w1d): Wannier interpolation of a one-dimensional two-band model.

Tight-binding chain, lattice constant a, two orbitals per cell (sites a and b), orthonormal orbitals:
  on-site energies E_a = +E0, E_b = -E0 with E0 = 0.5 eV;
  intra-cell hopping  <a,0|H|b,0>  = -t_hop  with t_hop  = 2.0 eV;
  inter-cell hopping  <a,0|H|b,-1> = -t'_hop with t'_hop = 1.0 eV (and its Hermitian partner).
These are model values chosen for illustration (no material is fitted). Bloch Hamiltonian in the orbital basis
(phase convention exp(ikR), intra-cell positions not included):
  H(k) = [[E0, -t - t' e^{-ika}], [-t - t' e^{ika}, -E0]],  bands  e_{+-}(k) = +- sqrt(E0^2 + t^2 + t'^2 + 2 t t' cos ka).
Gap at ka = pi: 2 sqrt(E0^2 + (t - t')^2) = 2.236 eV.

What the script does (every number quoted in the worked example is printed here):
  1. "code" eigenvectors on a coarse grid k_j = 2 pi j/(n_k a), j = 0..n_k-1, with random phases on every column;
  2. gauge by projection on the two orbitals, U(k) = A (A^+ A)^{-1/2} with A_mn = <psi_mk|g_n>; here U = C^+;
  3. H^W(R) = (1/n_k) sum_j e^{-i k_j R} U^+ E U on the Wigner-Seitz supercell (weight 1/2 at R = +-n_k/2 for even n_k);
  4. H(k) = sum_R e^{ikR} H^W(R) at 2001 points off the grid, diagonalized, compared with the exact bands;
  5. the lower band alone (one Wannier function, gauge-free): error against n_k, compared with exp(-kappa n_k a/2),
     kappa a = arccosh[(E0^2 + t^2 + t'^2)/(2 t t')] (complex branch point of e_-(k));
  6. gauge test: velocity operator V(k) = dH/dk (orbital basis) given in the band basis of one set of phases and
     rotated with the eigenvectors of another set; |v_12| interpolated both ways against the exact value.
"""
import numpy as np

E0, T1, T2 = 0.5, 2.0, 1.0      # eV, model values (see docstring)
RNG = np.random.default_rng(20261102)


def Hk(k):
    off = -T1 - T2 * np.exp(-1j * k)
    return np.array([[E0, off], [np.conj(off), -E0]])


def Vk(k):  # dH/dk in units of eV * a
    off = 1j * T2 * np.exp(-1j * k)
    return np.array([[0, off], [np.conj(off), 0]])


def exact_bands(k):
    e = np.sqrt(E0**2 + T1**2 + T2**2 + 2 * T1 * T2 * np.cos(k))
    return np.array([-e, e])


def ws_vectors(nk):
    """Integer R of the Wigner-Seitz supercell of nk cells and their degeneracy weights."""
    R = np.arange(-(nk // 2), nk // 2 + 1)
    w = np.ones(len(R))
    if nk % 2 == 0:
        w[0] = w[-1] = 0.5
    return R, w


def code_eigs(k):
    """Eigenpairs as a code returns them: arbitrary phase on every eigenvector."""
    e, C = np.linalg.eigh(Hk(k))
    return e, C * np.exp(2j * np.pi * RNG.random(2))[None, :]


def wannier_HR(nk, nb=2):
    ks = 2 * np.pi * np.arange(nk) / nk
    R, w = ws_vectors(nk)
    HR = np.zeros((len(R), nb, nb), complex)
    for k in ks:
        e, C = code_eigs(k)
        if nb == 2:
            A = C.conj().T                          # A_mn = <psi_m|g_n>, trial orbitals = the two orbitals
            S = A.conj().T @ A
            ev, Q = np.linalg.eigh(S)
            U = A @ Q @ np.diag(ev**-0.5) @ Q.conj().T   # Loewdin: U = A S^{-1/2}
            HW = U.conj().T @ np.diag(e) @ U
        else:
            HW = np.array([[e[0]]])                 # lower band alone; 1x1, phase-free
        for i, r in enumerate(R):
            HR[i] += np.exp(-1j * k * r) * HW / nk
    return R, w, HR


def interp(R, w, HR, k):
    return np.einsum("r,r,rij->ij", w, np.exp(1j * k * R), HR)


kfine = np.linspace(-np.pi, np.pi, 2001)
print(f"gap at ka = pi: {2*np.sqrt(E0**2+(T1-T2)**2):.3f} eV; band edges:",
      exact_bands(np.pi), exact_bands(0.0))

print("\n-- two Wannier functions (composite manifold): max band error over 2001 off-grid points --")
for nk in (2, 3, 4, 6):
    R, w, HR = wannier_HR(nk)
    err = max(np.abs(np.linalg.eigvalsh(interp(R, w, HR, k)) - exact_bands(k)).max() for k in kfine)
    print(f"n_k = {nk}: max |error| = {err:.2e} eV")
R, w, HR = wannier_HR(4)
print("H^W(R) for n_k = 4 (eV):")
for r, wi, h in zip(R, w, HR):
    print(" R =", r, "weight", wi, np.round(wi * h, 12).tolist())

print("\n-- lower band alone (one Wannier function) --")
kap = np.arccosh((E0**2 + T1**2 + T2**2) / (2 * T1 * T2))
print(f"kappa a = arccosh({(E0**2+T1**2+T2**2)/(2*T1*T2):.4f}) = {kap:.4f}; exp(-kappa a/2) per added point = {np.exp(-kap/2):.3f}")
errs = {}
for nk in (2, 4, 6, 8, 10, 12, 16, 20, 24):
    R, w, HR = wannier_HR(nk, nb=1)
    err = max(abs(interp(R, w, HR, k)[0, 0].real - exact_bands(k)[0]) for k in kfine)
    errs[nk] = err
    print(f"n_k = {nk:2d}: max |error| = {err:.2e} eV   ratio to exp(-kappa n_k a/2) = {err/np.exp(-kap*nk/2):.3f}")
# decay of the single-band H^W(R) itself (dense grid stands in for the infinite crystal)
R, w, HR = wannier_HR(400, nb=1)
h = {r: abs(HR[list(R).index(r), 0, 0]) for r in range(0, 9)}
print("|H^W(R)| of the lower band (eV), R = 0..8:", {r: f"{v:.2e}" for r, v in h.items()})
print("successive ratios:", [f"{h[r+1]/h[r]:.3f}" for r in range(1, 8)], " exp(-kappa a) =", f"{np.exp(-kap):.3f}")
nk_target = None
for nk in sorted(errs):
    if errs[nk] < 1e-3:
        nk_target = nk
        break
print("smallest listed n_k with max error < 1 meV:", nk_target)

print("\n-- one gauge: velocity matrix element |v_12| (eV a) --")
nk = 6
ks = 2 * np.pi * np.arange(nk) / nk
R, w = ws_vectors(nk)
VR_same = np.zeros((len(R), 2, 2), complex)
VR_mixed = np.zeros((len(R), 2, 2), complex)
HR = np.zeros((len(R), 2, 2), complex)
for k in ks:
    eA, CA = code_eigs(k)          # run A: states used to compute v in the band basis
    eB, CB = code_eigs(k)          # run B: same states, other phases (an independent calculation)
    vH = CA.conj().T @ Vk(k) @ CA  # v_mn(k) in the band basis of run A
    for i, r in enumerate(R):
        ph = np.exp(-1j * k * r) / nk
        HR[i] += ph * CA @ np.diag(eA) @ CA.conj().T
        VR_same[i] += ph * CA @ vH @ CA.conj().T     # rotated with the states it was computed from
        VR_mixed[i] += ph * CB @ vH @ CB.conj().T    # rotated with the states of run B
errs_same, errs_mixed, ex = [], [], []
for k in kfine:
    e, C = np.linalg.eigh(interp(R, w, HR, k))
    v_ex = abs((np.linalg.eigh(Hk(k))[1].conj().T @ Vk(k) @ np.linalg.eigh(Hk(k))[1])[0, 1])
    v_s = abs((C.conj().T @ interp(R, w, VR_same, k) @ C)[0, 1])
    v_m = abs((C.conj().T @ interp(R, w, VR_mixed, k) @ C)[0, 1])
    ex.append(v_ex); errs_same.append(abs(v_s - v_ex)); errs_mixed.append(abs(v_m - v_ex))
ex = np.array(ex)
print(f"n_k = {nk}: exact |v_12| ranges {ex.min():.3f}..{ex.max():.3f} eV a")
print(f"  same gauge:  max error {max(errs_same):.1e} eV a")
print(f"  mixed gauge: max error {max(errs_mixed):.2f} eV a (mean {np.mean(errs_mixed):.2f})")
i = np.argmin(abs(kfine - 0.37 * 2 * np.pi))
print(f"  at ka = 0.74 pi: exact {ex[i]:.3f}, mixed-gauge error {errs_mixed[i]:.3f}")
# at the six coarse-grid points themselves the mixed-gauge moduli are right (the error there is only a phase)
for k in ks:
    e, C = np.linalg.eigh(interp(R, w, HR, k))
    v_ex = abs((np.linalg.eigh(Hk(k))[1].conj().T @ Vk(k) @ np.linalg.eigh(Hk(k))[1])[0, 1])
    v_m = abs((C.conj().T @ interp(R, w, VR_mixed, k) @ C)[0, 1])
    print(f"  grid point ka = {k:.3f}: |v_12| mixed - exact = {v_m - v_ex:.1e} eV a")
