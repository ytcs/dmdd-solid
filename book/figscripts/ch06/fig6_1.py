"""Fig. 6.1 and worked example 6.1 (Sect. 6.1): adiabatic and sudden responses of an electron to a moving nucleus.
Output: tex/figures/ch06/fig6_1.pdf. Prints (and asserts) every number quoted in Sect. 6.1.

Model (modelling choices, named in the caption):
  One electron (mass m) bound harmonically, frequency w_e, to a nucleus whose position X(t) is a prescribed classical
  trajectory. In the frame of the nucleus, y = x - X(t), the Hamiltonian is p^2/2m + m w_e^2 y^2/2 + m Xddot(t) y
  (a forced oscillator). Units: m = w_e = 1.
  Velocity ramp: v(t) = (v_N/2) [1 + tanh(t/tau)], Xddot = (v_N / 2 tau) sech^2(t/tau).
  Exact result (coherent state, App. C.6): survival P_0 = exp(-|a|^2), with
     |a|^2 = (m v_N^2 / 2 w_e) * S(w_e tau),   S(x) = [ (pi x/2) / sinh(pi x/2) ]^2 ,
  from |a|^2 = (m / 2 w_e) | int dt Xddot e^{i w_e t} |^2 and int sech^2(s) e^{iks} ds = pi k / sinh(pi k / 2).
  Sudden limit tau -> 0: |a|^2 = (m v_N)^2 <y^2>, <y^2> = 1/(2 m w_e): the boost formula |<0|e^{-i m v_N y}|0>|^2.
  Checks: (1) classical ODE for <y>(t) -> free-oscillation energy / w_e = |a|^2; (2) split-operator TDSE of the
  quantum forced oscillator -> P_0 against exp(-|a|^2); (3) kicked nucleus bound harmonically at w_ph:
  |a|^2 = (m v_N^2 / 2 w_e) [w_e^2 / (w_e^2 - w_ph^2)]^2.
Inputs and sources:
  alpha = 1/137.035999 (CODATA 2018); m_e = 0.51099895 MeV; hydrogen-atom mass 1.00782503 u, proton 938.272 MeV,
  u = 931.49410242 MeV (CODATA 2018); natural Si mass 28.0855 u = 26.16 GeV (Sect. 1.3); v_max = 2.650e-3 (Sect. 1.2);
  E(2p) - E(1s) of hydrogen = (3/8) alpha^2 m_e = 10.2 eV (Sect. 2.2); F_1s(k) = 16/(4 + k^2 a0^2)^2 (Sect. 2.2);
  Si: omega_opt = 64.1 meV, E_g = 1.17 eV (Sect. 5.1).
Run: python fig6_1.py   (numpy, scipy, matplotlib; < 1 min)
"""
import os
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch06", "fig6_1.pdf")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

ALPHA = 1 / 137.035999
ME = 0.51099895e6                     # eV
U = 931.49410242e6                    # eV
HBAR_S = 6.582119569e-16              # eV s
C_KMS = 299792.458


def S(x):
    x = np.asarray(x, float)
    z = np.pi * x / 2
    out = np.ones_like(z)
    m = z > 1e-8
    out[m] = (z[m] / np.sinh(z[m])) ** 2
    return out


def xdd(t, tau, vN=1.0):
    return vN / (2 * tau) / np.cosh(t / tau) ** 2


# ---------- check 1: classical <y>(t) and the free-oscillation energy ----------
def classical(tau, vN=1.0, T=None):
    T = T or max(12.0, 14 * tau)
    if tau == 0:
        t = np.linspace(0, T, 4000)
        return t, -vN * np.sin(t), vN ** 2 / 2          # y(0+) = 0, ydot(0+) = -vN
    sol = solve_ivp(lambda t, z: [z[1], -z[0] - xdd(t, tau, vN)], (-T, T), [0.0, 0.0],
                    rtol=1e-11, atol=1e-13, dense_output=True, max_step=0.01)
    t = np.linspace(-T, T, 6000)
    y, yd = sol.sol(T)
    return t, sol.sol(t)[0], 0.5 * (y ** 2 + yd ** 2)    # energy / w_e = |a|^2 (m = w_e = 1)


for tau in [0.3, 1.0, 2.0, 3.0]:
    _, _, a2 = classical(tau)
    assert abs(a2 / (0.5 * S(tau)) - 1) < 1e-6, (tau, a2, 0.5 * S(tau))
print("classical check: |a|^2 = (v_N^2/2) S(w_e tau) to 1e-6 for w_e tau = 0.3, 1, 2, 3")


# ---------- check 2: quantum TDSE, split operator ----------
def tdse(tau, vN=1.0):
    L, n = 24.0, 512
    y = np.linspace(-L / 2, L / 2, n, endpoint=False)
    dy = y[1] - y[0]
    k = 2 * np.pi * np.fft.fftfreq(n, dy)
    psi0 = np.pi ** -0.25 * np.exp(-y ** 2 / 2)
    psi = psi0.astype(complex)
    T = 14 * tau + 10
    dt = 0.002
    nt = int(2 * T / dt)
    kin = np.exp(-0.5j * k ** 2 * dt)
    t = -T
    for _ in range(nt):
        V = 0.5 * y ** 2 + xdd(t + dt / 2, tau, vN) * y
        psi *= np.exp(-0.5j * V * dt)
        psi = np.fft.ifft(kin * np.fft.fft(psi))
        psi *= np.exp(-0.5j * V * dt)
        t += dt
    return abs(np.sum(psi0 * psi) * dy) ** 2


tq = [0.5, 1.0, 2.0]
P0q = [tdse(tau) for tau in tq]
for tau, p in zip(tq, P0q):
    assert abs(p / np.exp(-0.5 * S(tau)) - 1) < 2e-4, (tau, p)
print("TDSE check: P_0 = exp(-|a|^2) to 2e-4 for w_e tau =", tq, [f"{p:.5f}" for p in P0q])

# sudden: exp(-|a|^2) with |a|^2 = v_N^2/2 equals |<0|e^{-i v_N y}|0>|^2 = exp(-v_N^2 <y^2>), <y^2> = 1/2
print(f"sudden survival for v_N = 1 (m = w_e = 1): {np.exp(-0.5):.4f}")
for x in [1.0, 2.0, 3.0]:
    print(f"S({x:.0f}) = {S(x):.4g}; adiabatic asymptote pi^2 x^2 e^(-pi x) = {np.pi**2*x**2*np.exp(-np.pi*x):.4g}")
x10 = 1.0
while S(x10) > 0.1:
    x10 += 1e-4
assert 0.90 < S(0.3) < 0.95; print(f"S(0.3) = {S(0.3):.3f} (shaded sudden region: within 10 percent)")
print(f"S = 0.1 at w_e tau = {x10:.2f}; S = 0.5 at w_e tau = "
      f"{[x for x in np.arange(0, 3, 1e-4) if S(x) <= 0.5][0]:.3f}")


# ---------- check 3: nucleus kicked and then bound at w_ph ----------
def bound(wph, vN=1.0):
    T = 400.0
    sol = solve_ivp(lambda t, z: [z[1], -z[0] + vN * wph * np.sin(wph * t)], (0, T), [0.0, -vN],
                    rtol=1e-11, atol=1e-13, dense_output=True, max_step=0.01)
    t = np.linspace(0, T, 200001)
    y = sol.sol(t)[0] - vN * wph / (1 - wph ** 2) * np.sin(wph * t)    # remove the adiabatic following
    B = np.max(np.abs(y[t > 200]))
    return 0.5 * B ** 2


for wph in [0.0548, 0.2, 0.4]:
    a2 = bound(wph)
    assert abs(a2 / (0.5 / (1 - wph ** 2) ** 2) - 1) < 1e-5, (wph, a2)
r = 0.0641 / 1.17
print(f"bound-nucleus check passed; Si omega_opt/E_g = {r:.4f}, factor [1 - r^2]^-2 = {1/(1-r**2)**2:.4f}")

# ---------- numbers of the section ----------
M_SI = 28.0855 * U
q = 5.10e6                          # Sect. 1.3: 1 GeV on Si at v_max
vN = q / M_SI
print(f"Si kick: v_N = {vN:.4e} = {vN*C_KMS:.1f} km/s; v_N/alpha = {vN/ALPHA:.4f}; (v_N/alpha)^2 = {(vN/ALPHA)**2:.2e}; "
      f"m_e v_N = {ME*vN:.1f} eV; E_R = {q**2/2/M_SI:.0f} eV; alpha/v_N = {ALPHA/vN:.1f}")
kap = (ME / M_SI) ** 0.25
print(f"kappa^3 = {kap**3:.3e}; alpha kappa^3 = {ALPHA*kap**3:.3e}; v_N/(alpha kappa^3) = {vN/(ALPHA*kap**3):.0f}")
# electronic time scales
dE = 3 / 8 * ALPHA ** 2 * ME
print(f"hydrogen 1s-2p: {dE:.2f} eV; 1/dE = {HBAR_S/dE*1e15:.4f} fs; Si 1/E_g = {HBAR_S/1.17*1e15:.3f} fs")
# crossing times at v_max: Si Helm radius 3.47 fm (Sect. 2.2); proton charge radius 0.84 fm (CODATA 2022, mohr2025codata: 0.84075 fm)
for R_fm in [0.84, 3.47]:
    tcross = R_fm * 1e-15 / (2.650e-3 * C_KMS * 1e3)
    print(f"crossing time of {R_fm} fm at v_max: {tcross:.2e} s; times 10.2 eV/hbar: {tcross*dE/HBAR_S:.1e}")

# Worked example 6.1: hydrogen, m_chi = 1 GeV, v_max
MH = 1.00782503 * U
MP = 938.27208816e6
mchi = 1e9
mu = mchi * MH / (mchi + MH)
qH = 2 * mu * 2.650e-3
vNH = qH / MP
x = vNH / ALPHA
F = 16 / (4 + x ** 2) ** 2
P0 = F ** 2
print(f"WE: M_H = {MH/1e6:.3f} MeV, mu = {mu/1e6:.1f} MeV, q = {qH/1e6:.3f} MeV, v_N = q/m_p = {vNH:.4e} = "
      f"{vNH*C_KMS:.0f} km/s, x = v_N/alpha = {x:.4f}, F_1s = {F:.4f}, P_0 = {P0:.4f}, 1-P_0 = {1-P0:.4f}, x^2 = {x**2:.4f}, "
      f"E_R = q^2/2M_H = {qH**2/2/MH:.0f} eV")
# half survival
xh = [xx for xx in np.arange(0, 2, 1e-5) if (16 / (4 + xx ** 2) ** 2) ** 2 <= 0.5][0]
qh = xh * ALPHA * MP
print(f"P_0 = 1/2 at v_N/alpha = {xh:.3f}: v_N = {xh*ALPHA:.3e}, q = {qh/1e6:.2f} MeV, E_R = {qh**2/2/MH/1e3:.1f} keV")
# hydrogen kick with the same v_N as the Si example
xs = vN / ALPHA
print(f"for v_N = {vN:.3e}: 1 - F_1s^2 = {1-(16/(4+xs**2)**2)**2:.2e}")
# exact reduced-mass identity: (m_e q/M_H) a_mu = q/(alpha m_p)
amu = 1 / (ALPHA * ME * MP / (ME + MP))
assert abs((ME * qH / MH) * amu / (qH / (ALPHA * MP)) - 1) < 1e-7

# ---------- figure ----------
plt.rcParams.update({"font.size": 8.5})
CS, CM, CA, CK = "C3", "C1", "C0", "0.45"
fig, (ax, bx, cx) = plt.subplots(1, 3, figsize=(6.6, 2.4), gridspec_kw={"wspace": 0.55})
cases = [(0.0, CS, "0"), (1.0, CM, "1"), (4.0, CA, "4")]   # legend title carries omega_e tau_acc
tt = np.linspace(-20, 25, 3000)
for tau, col, lab in cases:
    v = np.where(tt > 0, 1.0, 0.0) if tau == 0 else 0.5 * (1 + np.tanh(tt / tau))
    ax.plot(tt, v, color=col, lw=1.2, label=lab)
    if tau == 0:
        t, y, _ = classical(0.0, T=25)
        t = np.concatenate([[-20, 0], t]); y = np.concatenate([[0, 0], y])
    else:
        t, y, _ = classical(tau, T=25)
    bx.plot(t, y, color=col, lw=1.0)
ax.set_xlim(-20, 25); bx.set_xlim(-20, 25)
ax.set_xlabel(r"$\omega_{\mathrm{e}} t$"); ax.set_ylabel(r"$\dot X/v_N$")
ax.legend(fontsize=6.5, title=r"$\omega_{\mathrm{e}}\tau_{\mathrm{acc}}$", title_fontsize=6.5, frameon=False,
          loc="center right", bbox_to_anchor=(1.0, 0.35), handlelength=1.5)   # narrow: below the plateau, right of the steps
ax.set_title("(a) nuclear velocity", fontsize=8.5, loc="left")
bx.axhline(0, color="0.8", lw=0.5)
bx.set_xlabel(r"$\omega_{\mathrm{e}} t$"); bx.set_ylabel(r"$\langle y\rangle\,\omega_{\mathrm{e}}/v_N$")
bx.set_title("(b) electron behind nucleus", fontsize=8.5, loc="left")
xs_ = np.linspace(0, 4, 400)
cx.semilogy(xs_, S(xs_), color="k", lw=1.2, label="exact")
xa = np.linspace(0.8, 4, 200)
cx.semilogy(xa, np.pi ** 2 * xa ** 2 * np.exp(-np.pi * xa), color=CK, lw=0.9, ls="--", label="asymptote")
cx.semilogy(tq, [-np.log(p) / 0.5 for p in P0q], "o", color=CS, ms=3.5, label="TDSE")
cx.axvspan(0, 0.3, color="0.92", lw=0)
cx.text(0.06, 3e-3, "sudden", fontsize=6.5, rotation=90)
cx.text(2.6, 0.25, "adiabatic", fontsize=6.5)
cx.set_xlim(0, 4); cx.set_ylim(1e-4, 2)
cx.set_xlabel(r"$\omega_{\mathrm{e}}\tau_{\mathrm{acc}}$"); cx.set_ylabel(r"$|\alpha_{\mathrm{d}}|^2 / |\alpha_{\mathrm{d}}|^2_0$")
cx.legend(fontsize=6.5, frameon=False, loc="lower left", bbox_to_anchor=(0.1, 0.0))
cx.set_title("(c) excitation", fontsize=8.5, loc="left")
fig.savefig(OUT, bbox_inches="tight")
print("wrote", os.path.normpath(OUT))
