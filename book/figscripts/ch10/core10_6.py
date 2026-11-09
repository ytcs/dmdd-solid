"""Shared model of Sect. 10.6: shell-resolved responses of silicon and germanium atoms in the plane-wave approximation,
and the number of electrons per atom that dark matter can reach at each momentum transfer.

Natural units, energies and momenta in eV unless a name says keV.

Orbitals (not computed here): all-electron free atoms from ld1.x (Quantum ESPRESSO 7.6), PBE, scalar-relativistic,
configurations [Ne]3s2 3p2 (Si) and [Ar]3d10 4s2 4p2 (Ge); files ../ch03/ld1/si_r1.wfc, ge_r1.wfc, made for Fig. 3.10
(Sect. 3.5; loader and Bessel transform reused from ../ch03/fig3_10.py). Ge 1s is not in the file; it opens only above
q = 4.2 MeV and is left out.

Shell response per atom (Sect. 10.6, eq:10.6-Sat; from eq:2.2-fion-pw and S = |f_ion|^2/(4 E_ej) per unit omega):
    S_at_nl(q, omega) = (N_nl/2) (m_e/q) int_{|p-q|}^{p+q} k phi_nl(k)^2 dk ,   p = [2 m_e (omega - E_core)]^{1/2},
with phi_nl normalized to int k^2 phi^2 dk = 1 and N_nl the occupation (2(2l+1) for a full shell, as eq:2.2-fion-pw;
2 for the spherically averaged valence 3p2 / 4p2); int domega S_at_nl = N_nl (closure).
Modelling choices (stated in the caption of Fig. 10.5): plane-wave final states whose kinetic energy is counted from
the valence-band maximum, as for the free final states of Griffin et al., arXiv:2105.05253, Eq. (3.21); every shell,
the valence included, from the free atom; valence initial energy at the valence maximum (E_core = 0); threshold
omega >= E_g + E_core; no Fermi factor; no orthogonalization (its size is printed by fig10_5.py).

Accessible electrons per atom: N_acc_nl(q) = int_{E_g + E_core}^{q v_max} S_at_nl(q, omega) domega, the window that dark
matter of any mass allows at momentum transfer q (eq:1.3-vmin with q/2m_chi -> 0), v_max = 2.650e-3 (Sect. 1.2).

Binding energies relative to the valence maximum: X-Ray Data Booklet Table 1-1 (Williams 2009), extract
../../sources/3.5/xdb_table1-1.txt: Si 2p 99.42/99.82 (centroid 99.55), 2s 149.7, 1s 1839 eV; Ge 3d 29.2/29.8
(centroid 29.44), 3p 120.8/124.9 (centroid 122.2), 3s 180.1, 2p 1217.0/1248.1 (centroid 1227.4), 2s 1414.6 eV.
Gaps: 1.17 eV (Si) and 0.744 eV (Ge), low temperature (Sect. 3.3).
"""
import os
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import spherical_jn

HERE = os.path.dirname(os.path.abspath(__file__))
LD1 = os.path.join(HERE, "..", "ch03", "ld1")
ME = 510998.95
ALPHA = 1 / 137.035999084
AU = 3728.94                      # eV per bohr^-1 (alpha m_e)
VMAX = 2.650e-3
LMAP = {"S": 0, "P": 1, "D": 2}
EG = {"Si": 1.17, "Ge": 0.744}
ECORE = {"Si": {"3S": 0.0, "3P": 0.0, "2P": (4 * 99.42 + 2 * 99.82) / 6, "2S": 149.7, "1S": 1839.0},
         "Ge": {"4S": 0.0, "4P": 0.0, "3D": (6 * 29.2 + 4 * 29.8) / 10, "3P": (4 * 120.8 + 2 * 124.9) / 6,
                "3S": 180.1, "2P": (4 * 1217.0 + 2 * 1248.1) / 6, "2S": 1414.6}}
FILES = {"Si": "si_r1", "Ge": "ge_r1"}
OCC = {"Si": {"3S": 2, "3P": 2, "2P": 6, "2S": 2, "1S": 2},
       "Ge": {"4S": 2, "4P": 2, "3D": 10, "3P": 6, "3S": 2, "2P": 6, "2S": 2}}
CACHE = os.path.join(HERE, "core10_6_orbitals.npz")
VALENCE = {"Si": ("3S", "3P"), "Ge": ("4S", "4P")}


def load(name):
    path = os.path.join(LD1, name + ".wfc")
    heads = open(path).readline().split()[2:]
    d = np.loadtxt(path)
    return d[:, 0], {h: d[:, i + 1] for i, h in enumerate(heads)}


def momentum(r, u, l, p, rmax=20.0, dr=2e-4):
    """phi(p) = sqrt(2/pi) int dr r u(r) j_l(p r) (bohr units), normalized to int p^2 phi^2 dp = 1."""
    sp = CubicSpline(r, u)
    x = np.arange(dr, rmax, dr)
    ux = np.where(x >= r[0], sp(x), u[0] * (x / r[0]) ** (l + 1))
    return np.array([np.sqrt(2 / np.pi) * np.trapezoid(x * ux * spherical_jn(l, pp * x), x) for pp in p])


class Shell:
    def __init__(self, mat, name, pk, ph, rmean):
        self.mat, self.name, self.l = mat, name, LMAP[name[1]]
        self.occ = OCC[mat][name]
        self.ecore = ECORE[mat][name]
        self.eth = EG[mat] + self.ecore
        norm = np.trapezoid(pk ** 2 * ph ** 2, pk)
        self.norm = norm
        self.k = np.concatenate([[0.0], pk]) * AU                     # eV
        phi2 = np.concatenate([[ph[0] ** 2 if self.l == 0 else 0.0], ph ** 2]) / norm / AU ** 3   # eV^-3
        self.phi2 = phi2
        integrand = self.k * phi2
        self.C = np.concatenate([[0.0], np.cumsum(0.5 * (integrand[1:] + integrand[:-1]) * np.diff(self.k))])
        self.rmean = rmean   # bohr

    def cum(self, k):
        return np.interp(k, self.k, self.C, right=self.C[-1])

    def S(self, q, w):
        """per-atom shell response [eV^-1] at momentum q, energy w (arrays broadcast)."""
        q, w = np.broadcast_arrays(np.asarray(q, float), np.asarray(w, float))
        x = np.maximum(w - self.ecore, 0.0)
        p = np.sqrt(2 * ME * x)
        val = 0.5 * self.occ * ME / q * (self.cum(p + q) - self.cum(np.abs(p - q)))
        return np.where(w >= self.eth, val, 0.0)

    def nacc(self, q, wmax=None, n=600):
        """electrons per atom reachable at q in the window E_th <= omega <= q v_max (or wmax)."""
        q = np.atleast_1d(np.asarray(q, float))
        out = np.zeros_like(q)
        for i, qq in enumerate(q):
            top = qq * VMAX if wmax is None else wmax
            if top <= self.eth:
                continue
            w = np.linspace(self.eth, top, n)
            out[i] = np.trapezoid(self.S(qq, w), w)
        return out

    def zeroth(self, q, wtop=2e5, n=20000):
        """int S domega over all energies (closure check, = N_nl at large q)."""
        w = self.eth + np.geomspace(1e-3, wtop, n)
        return np.trapezoid(self.S(q, w), w)


PK = np.concatenate([np.linspace(0, 2, 801)[1:], np.geomspace(2.0, 300e3 / AU, 1500)[1:]])   # bohr^-1


def _transforms():
    """Bessel transforms of every orbital, cached (about two minutes to build)."""
    if os.path.exists(CACHE):
        d = np.load(CACHE)
        return {k: d[k] for k in d.files}
    out = {}
    for mat in FILES:
        r, wf = load(FILES[mat])
        for h, u in wf.items():
            out[f"{mat}_{h}"] = momentum(r, u, LMAP[h[1]], PK)
            out[f"{mat}_{h}_rmean"] = np.array(np.trapezoid(r * u ** 2, r) / np.trapezoid(u ** 2, r))
    np.savez(CACHE, **out)
    return out


def atom(mat):
    t = _transforms()
    names = [k.split("_")[1] for k in t if k.startswith(mat + "_") and not k.endswith("rmean")]
    return {h: Shell(mat, h, PK, t[f"{mat}_{h}"], float(t[f"{mat}_{h}_rmean"])) for h in names}


HBARC = 1973.269804


def table(mat):
    """Crystal valence IP eps2 tables (Knapen-Kozaczuk-Lin): Ge from ge_ip_reduce.py, Si from si_elf_reduce.py.
    Returns omega, |q| bins, eps2 (n_omega, n_q), cell volume (eV^-3); lattice constants Ge 5.658, Si 5.431 A."""
    fname, a = ("ge_ip_binned.npz", 5.658) if mat == "Ge" else ("si_elf_binned.npz", 5.431)
    d = np.load(os.path.join(HERE, fname))
    return d["omega"], d["q"], d["ip"], a ** 3 / 4 / HBARC ** 3


def fermi(p, z=1.0):
    """Fermi factor of eq:2.2-fermi."""
    xi = z * ALPHA * ME / p
    return 2 * np.pi * xi / (1 - np.exp(-2 * np.pi * xi))
