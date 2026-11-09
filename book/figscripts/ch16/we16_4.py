"""Worked example 16.4 (we:16-davydov): the Davydov splitting of the lowest singlet band of anthracene and the binned sum,
in the pi-electron model of frenkel16_4.py.  Every number printed here is quoted in Sect. 16.4.

Energy convention: the binned form (frenkel16_4.E_X) puts the L_a line at the measured crystal S1 = 3.1 eV, which already
contains the whole gas-to-crystal shift.  When J is added explicitly, the molecular levels are shifted by a common
amount so that the lowest optically allowed exciton at Q -> 0 sits at 3.1 eV (as in limit16_4a.py), so that the crystal
shift is counted once.  E_mol below is that molecular level set.
(1) Frenkel Hamiltonian of the lowest band at Q -> 0: the two lowest molecular singlets (L_a, bright, short axis; L_b,
    dark in the model) on the two molecules of the cell, coupled by J(Q) (macroscopic term removed).  Davydov components,
    their polarizations and oscillator strengths; the Davydov sum of oscillator strengths.
(2) Exciton band of the same states over the Brillouin zone (width of the manifold).
(3) Binned sum at one momentum transfer: the weights |sum A* F|^2 of the four exciton states of the lowest band at
    q = 3 keV along b and along c', against the incoherent sum of molecular |f|^2.
(4) The static screening of the model, eps(q, 0) - 1 = (2 e^2/(Omega q^2)) sum_{o,x} |f|^2/E_x (eq:4.9-eps2 with the
    singlet factor inside f), direction-averaged, pi electrons only.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")   # small matrices: threading only adds overhead
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import frenkel16_4 as F  # noqa: E402

np.set_printoptions(precision=4, suppress=True)
low = [0, 1]
ns = len(low)
Q0 = 1e-3 * F.RECIP[1]
J = F.frenkel_J(Q0, low)
H0 = np.diag(np.concatenate([F.E_X[low], F.E_X[low]])) + J
SHW = F.S1_EXP - np.linalg.eigvalsh(H0)[0]       # common shift: lowest allowed exciton at 3.1 eV
E_mol = F.E_X + SHW
print(f"common shift of the molecular levels so that E_- = {F.S1_EXP} eV: {SHW:+.4f} eV; molecular L_a level E_La = {E_mol[0]:.4f} eV"
      f" (gas S1 3.5 eV, crystal S1 3.1 eV)")
H = np.diag(np.concatenate([E_mol[low], E_mol[low]])) + J
E, A = np.linalg.eigh(H)
print("(1) lowest band at Q -> 0 (basis: molecule 1 [L_a, L_b], molecule 2 [L_a, L_b])")
print("  molecular energies (eV):", E_mol[low])
print("  J (meV):\n", np.round(J.real * 1e3, 2))
print(f"  L_a: J11 = {J[0,0].real*1e3:.1f} meV (shift by the translational images), |J12| = {abs(J[0,2])*1e3:.1f} meV,"
      f" Davydov splitting 2|J12| = {2*abs(J[0,2])*1e3:.1f} meV (2x2, L_a only)")
d1 = F.dipoles(F.R1)
d2 = F.dipoles(F.R2)
dvec = np.vstack([d1[low], d2[low]])          # (4, 3), e A
for lam in range(4):
    dl = A[:, lam].conj() @ dvec
    fo = 2 * E[lam] * np.abs(dl) ** 2 / F.H2M  # f^osc along a, b, c'
    print(f"  exciton {lam}: E = {E[lam]:.4f} eV, |d| components along (a, b, c') = {np.round(np.abs(dl), 3)} eA,"
          f" f_osc along (a, b, c') = {np.round(fo, 4)}, total {fo.sum():.4f}; |d|^2 = {(np.abs(dl)**2).sum():.4f} e^2 A^2")
fmol = F.osc_strength(F.R1)[0] * E_mol[0] / F.E_X[0]   # free-molecule f_osc at the molecular level E_La
ftot = sum((2 * E[lam] * np.abs(A[:, lam].conj() @ dvec) ** 2 / F.H2M).sum() for lam in range(4)) / 3
print(f"  Davydov sum: sum over components of the direction-averaged f_osc = {ftot:.4f}; two molecules x f_osc(L_a) ="
      f" {2*fmol:.4f}; ratio {ftot/(2*fmol):.4f} (equal up to E_lambda/E_x)")
dip2 = sum((np.abs(A[:, lam].conj() @ dvec) ** 2).sum() for lam in range(4))
print(f"  energy ratio (E_- + E_+)/(2 E_La) = {(E[0]+E[1])/(2*E_mol[0]):.4f}; separation of the two lines = {(E[1]-E[0])*1e3:.1f} meV")
print(f"  dipole strength sum_lambda |d_lambda|^2 = {dip2:.5f} vs sum_o |d_o|^2 = {(np.abs(dvec)**2).sum():.5f} (exact)")

print("\n(2) exciton band over the zone (lowest band, 4 states), 6^3 grid of Q:")
g = (np.arange(6) + 0.5) / 6 - 0.5
Es = []
for i in g:
    for j in g:
        for k in g:
            Q = i * F.RECIP[0] + j * F.RECIP[1] + k * F.RECIP[2]
            Jq = F.frenkel_J(Q, low)
            Es.append(np.linalg.eigvalsh(np.diag(np.concatenate([E_mol[low]] * 2)) + Jq))
Es = np.array(Es)
print(f"  lowest band spans {Es.min():.3f} to {Es.max():.3f} eV (width {Es.max()-Es.min():.3f} eV);"
      f" lowest branch {Es[:,0].min():.3f}-{Es[:,0].max():.3f}")

print("\n(3) binned sum at q = 3 keV:")
for name, e in (("b", np.array([0, 1.0, 0])), ("c'", np.array([0, 0, 1.0])), ("L1", F.AX1[0]), ("M1", F.AX1[1])):
    qv = e * 3.0 / F.KEV_PER_INVA
    Jq = F.frenkel_J(qv, low)
    Hq = np.diag(np.concatenate([E_mol[low]] * 2)) + Jq
    Eq, Aq = np.linalg.eigh(Hq)
    Fv = F.F_cell(qv[None, :], low)[:, 0]
    w = np.abs(Aq.conj().T @ Fv) ** 2
    inc = np.abs(Fv) ** 2
    print(f"  q along {name}: exciton energies {np.round(Eq,4)} eV, weights {np.round(w,5)}; sum {w.sum():.6f};"
          f" incoherent sum over molecules and states {inc.sum():.6f}; L_a alone per molecule {np.round(inc[[0,2]],5)}")

print("\n(4) static screening of the pi-electron model, direction-averaged (300 directions):")
dirs = F.fib_sphere(300)
allst = list(range(len(F.E_X)))
for qk in (0.3, 0.5, 1.0, 1.17, 2.0, 3.0, 5.0):
    qv = dirs * qk / F.KEV_PER_INVA
    s = 0.0
    for mol in (1, 2):
        f = F.formfactors(qv, mol, allst)
        s += (np.abs(f) ** 2 / F.E_X[:, None]).sum(0)
    q2 = (qk / F.KEV_PER_INVA) ** 2
    eps1 = 2 * 4 * np.pi * F.E2 / (F.OMEGA * q2) * s.mean()
    print(f"  q = {qk:5.2f} keV (q a_mol = {qk/F.KEV_PER_INVA*2.660:.2f}): eps(q,0) - 1 = {eps1:.4f}, 1/eps^2 = {1/(1+eps1)**2:.3f}")
