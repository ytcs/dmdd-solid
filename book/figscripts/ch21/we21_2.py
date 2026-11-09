"""Worked example 21.2 (we:21-stream): one stream saturating the halo-independent bound for silicon at m_chi = 10 MeV, heavy
mediator, u0 = 500 km/s. Prints every number of the example (we21_2.log).

Search (as fig21_2.py): 1 kg yr, no events in the one-, two- and three-pair bins of the cascade of Sect. 18.3 (E_g = 1.160 eV,
eps_eh = 3.749 eV; bin probabilities P_casc(n|omega), hib21.pbin), N_up = ln 30 = 3.401 per bin. Step columns A_i(v) from hib21.column (Essig et al. table).
Primal: one stream of laboratory speed u0 (any direction: the response is angle-averaged), weight c chosen to saturate the
tightest bin j; its eta-tilde(u0) = c/u0 (u0 in units of c). Dual: lambda_j = 1/A_j(u0), lambda_i = 0 otherwise;
certificate condition lambda_j k_j(v) >= Theta(v - u0)/v for all v, i.e. A_j(v) >= A_j(u0) for v >= u0 (checked on a 0.1 km/s
grid up to v_max).
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import hib21 as B  # noqa: E402
import halo21 as H  # noqa: E402

M, U0 = 10e6, 500.0
NUP = np.log(30.0)
BINS = (1, 2, 3)
LOG = open(os.path.join(HERE, "we21_2.log"), "w")


def say(s):
    print(s)
    LOG.write(s + "\n")


mu = M * B.ME / (M + B.ME)
say(f"m_chi = 10 MeV: mu = {mu/1e3:.2f} keV; prefactor Expo alpha m_e^2/(M_cell mu^2) = {B.pref(M):.4e} yr")
say("bins: N = 1, 2, 3 pairs with the cascade probabilities P_casc(N|omega) of Sect. 18.3")
for n in BINS:
    pb = B.pbin(n)
    say(f"  bin {n}: P > 0.5 for omega in [{B._E[pb > 0.5].min():.1f}, {B._E[pb > 0.5].max():.1f}] eV; P > 0 from {B._E[pb > 0].min():.1f} eV")
A = {n: B.column(M, n, U0) for n in BINS}
for n in BINS:
    say(f"A_{n}(u0 = {U0:.0f} km/s) = {A[n]:.4e} yr; single-bin bound N_up/A = {NUP/A[n]:.4e} yr^-1")
j = min(BINS, key=lambda n: NUP / A[n])
bound = NUP / A[j]
say(f"tightest bin j = {j}; bound eta-tilde(500) <= {bound:.4e} yr^-1")
u0n = U0 / B.CKM
c = NUP * u0n / A[j]          # Xi-weight: counts = c k_i(u0) = c A_i(u0)/u0n
say(f"stream at |v| = {U0:.0f} km/s = {u0n:.4e} c: weight c = N_up u0 / A_j(u0) = {c:.4e} yr^-1 (natural speed units)")
for n in BINS:
    say(f"  counts of the stream in bin {n}: {c * A[n] / u0n:.4f} (bound {NUP:.3f})")
say(f"  eta-tilde of the stream at u0: c/u0 = {c/u0n:.4e} yr^-1 (equals the bound)")
lam = 1 / A[j]
say(f"dual certificate lambda_{j} = 1/A_{j}(u0) = {lam:.4e} yr^-1 per count; dual value lambda N_up = {lam*NUP:.4e}")
vv = np.arange(U0, B.VMAX + 1e-9, 0.1)
Aj = B.column(M, j, vv)
say(f"  check A_{j}(v)/A_{j}(u0) over u0 <= v <= v_max: min {Aj.min()/A[j]:.6f}, max {Aj.max()/A[j]:.4f} (min >= 1: certificate holds)")
# galactic speed of the stream: |v + v_E| ranges from |u0 - v_E| to u0 + v_E; allowed if some direction has |v + v_E| <= v_esc
say(f"  galactic speed of a 500 km/s laboratory stream: {abs(U0 - B.VE):.1f} (against the wind) to {U0 + B.VE:.1f} km/s; "
    f"allowed directions exist since {abs(U0 - B.VE):.1f} <= v_esc = {B.VESC:.0f}")
# comparison with the standard halo at its own limit
unit1 = B.etatilde_unit(M, 1.0)
Nn = {n: B.counts_eta(M, n, lambda v: unit1 * H.eta_shm(v)) for n in BINS}
sig = min(NUP / Nn[n] for n in BINS)
e500 = sig * unit1 * H.eta_shm(U0)
say(f"standard halo: sigma_lim = {sig:.4e} cm^2; eta-tilde_SHM(500) at sigma_lim = {e500:.4e} yr^-1; bound/SHM = {bound/e500:.3f}")
say(f"  eta_SHM(500) = {H.eta_shm(U0)*B.CKM:.2f} (natural units), <1/v> = {H.eta_shm(0.0)*B.CKM:.1f}")
# fraction of the SHM counts in each bin from particles faster than 500 km/s in the lab (same sigma)
for n in BINS:
    vm, w, _ = B.cells(M, n)
    full = np.sum(w * unit1 * sig * H.eta_shm(vm))
    # contribution of particles with v > U0: eta_>(vmin) = eta(max(vmin, U0))
    fast = np.sum(w * unit1 * sig * H.eta_shm(np.maximum(vm, U0)))
    say(f"  SHM at sigma_lim, bin {n}: {full:.3f} counts, of which {fast:.3f} from particles faster than 500 km/s")
# what the SHM shape would need: scale factor
say(f"  a standard-halo eta-tilde scaled by {bound/e500:.3f} touches the bound at 500 km/s")
# decomposition of the factor bound/SHM for the tightest bin
vm, w, _ = B.cells(M, j)
fast = np.sum(w * unit1 * sig * H.eta_shm(np.maximum(vm, U0)))
atu0 = e500 * A[j]
say(f"decomposition (bin {j}): eta-tilde_SHM(500) A_j(500) = {atu0:.3f} counts; fast particles give {fast:.3f}; total {NUP:.3f}")
say(f"  bound/SHM = (N_up/fast) x (fast/[eta A_j(u0)]) = {NUP/fast:.3f} x {fast/atu0:.3f} = {NUP/atu0:.3f}")
# comparison: the step model of Sect. 1.5 (E_g = 1.11 eV, eps_eh = 3.6 eV) on the same table
say("comparison, step model of Sect. 1.5 (1.11 eV, 3.6 eV per pair):")
As = {n: B.column(M, n, U0, model="step") for n in BINS}
say("  A_i(500) = " + ", ".join(f"{n}: {As[n]:.4e}" for n in BINS) + f" yr; bound {min(NUP/As[n] for n in BINS):.4e} yr^-1 (bin {min(BINS, key=lambda n: NUP/As[n])})")
Ns = {n: B.counts_eta(M, n, lambda v: unit1 * H.eta_shm(v), model="step") for n in BINS}
sigs = min(NUP / Ns[n] for n in BINS)
say(f"  SHM sigma_lim {sigs:.4e} cm^2 (bin {min(BINS, key=lambda n: NUP/Ns[n])}); SHM counts per cm^2 step/cascade: "
    + ", ".join(f"bin {n}: {Ns[n]:.4e}/{Nn[n]:.4e} = {Ns[n]/Nn[n]:.3f}" for n in BINS))
