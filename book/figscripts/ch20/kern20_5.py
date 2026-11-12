"""Collection kernels in the mean-field limit and the collection ratio r_coll (Sect. 20.5).

Every number printed in Sect. 20.5.2-20.5.3 (mean-field estimate, sub-gap share of Luke phonons, near-gap gain,
collection ratio with the Sect. 20.4 cascade yield and film escape, collection contrast), the primary arrival band
quoted in Sect. 20.4, and Fig. 20.6 (fig:20-rcoll).
Run:  python kern20_5.py > kern20_5.log   (about 5 minutes; film20_5.py and qp20_4.py are imported).
Output: tex/figures/ch20/fig20_rcoll.pdf

Physics (derived in Sect. 20.5)
  Mean-field limit: diffusion across the crystal faster than absorption, grey diffuse faces, so the collection kernel
  does not depend on the event position.  Time-integrated number of phonons N(E) in energy bin E obeys
      (Gamma_abs(E) + gamma(E)) N(E) = n0(E) + sum_{E' > E} gamma(E') N(E') P(E | E') [+ returned phonons],
  gamma(E) = f_LA A_anh (E/h)^5 (only longitudinal phonons decay; isotope scattering keeps their share at f_LA),
  P(E | E') the daughters in bin E from a decay at E' (two daughters, energy fraction y with number density
  Beta(3,3) = 30 y^2 (1 - y)^2, i.e. the energy-weighted P_d(y) = 60 y^3 (1 - y)^2 of Sect. 20.2; renormalized on the
  grid so that the daughters carry exactly E').
      Gamma_abs(E) = (v/2d) [ sum_s c_s tbar p_s(E) 1(E >= 2 Delta_s) + c_Al tbar kappa 1(E < 2 Delta_Al)
                              + (1 - sum_s c_s) l_bare ]
  v/2d the rate at which a phonon of an isotropic population hits one of the two faces of a slab of thickness d,
  c_s the face share of film s, tbar the transmission into it, l_bare the loss per hit on a bare face, and
  p_s(E) = p_first(E/Delta_s; r) the probability that a phonon entering film s breaks a pair before it escapes
  (eq:20.4-ppb; a phonon that escapes unbroken re-enters the crystal unchanged, so it is a reflection).
  Signal of film s: S_s = sum_E E Gamma_s(E) N(E) Y_s(E), Y_s(E) = Y(E/Delta_s; r) the Kaplan-cascade yield of
  Sect. 20.4 (qp20_4.Cascade, film20_5.FilmResponse), r = t_l/t0 the film escape ratio of Sect. 20.3.  r = inf is the
  thick film (no escape): Y = 2 Delta/E below 4 Delta, 0.5997 at 5.46 Delta, 0.590 above 10 Delta.
  Phonons that leave a film after its first pair break (escaped above-gap phonons and relaxation phonons) re-enter the
  crystal with the spectrum film20_5.FilmResponse.spectrum and are absorbed again (variant "conserved", the default,
  for every film; energy is conserved).  Only returned phonons below 2 Delta_Al = 0.36 meV are dropped: no film
  absorbs them, so they end on the bare faces without signal (kappa = 0); with kappa = 1 they are counted as part of the
  emitting film's own sub-gap loss, not given to the tungsten sensor.  Variant "lost" (the lumped film of Sect. 20.4):
  phonons leaving a film after its first pair break are deleted, while phonons that escape unbroken are reflected.
  That is a selective sink; it is kept as an upper envelope, not a detector value.  Variant "uniform sink": the
  conserved model with the bare-face loss raised to 0.01, 0.1, 0.3 per hit, a signal-free sink acting on all phonons.
  sub-gap phonons of aluminum: kappa = 0 ("sub-gap lost": reflected by every film, eventually lost on bare faces) or
  kappa = 1 ("sub-gap absorbed": a tungsten sensor takes them and converts them with the efficiency of the primaries
  in that film, Ybar_prim = S_Al(prim)/absorbed_Al(prim); this reduces to Y_inf = 0.59 for thick films with flat yield).
  The niobium-like film reflects sub-gap phonons.  Both films have the same r (a film-thickness scale).
  Efficiency eps_pop = (S_1 + S_2)/E_pop; r_coll = eps_Luke / eps_prim; channel fraction a_pop = S_Al/(S_Nb + S_Al);
  contrast varpi_O = a_Luke - a_prim.
  Single-film identity (one film type, sub-gap weight kappa):
      r_coll - 1 = s_ng - (1 - kappa) s_sub,  s_sub = Luke energy share below 2 Delta,
      s_ng = int_{2 Delta} u_L(E) [Y(E)/Ybar_prim - 1] dE / E_L  (near-gap gain), Ybar_prim = yield of the primaries
  as absorbed; exact when absorption per hit is the same for every phonon above the gap (flat p_s); checked below.

Inputs (book values and sources)
  Si: c_L = 9.00, c_T = 5.40 km/s (isotropic Voigt tensor, App. C.18).  Number-weighted mean speed
      v = (c_L^-2 + 2 c_T^-2)/(c_L^-3 + 2 c_T^-3) = 5.75 km/s.  f_LA = 0.093, the equilibrium longitudinal share of
      Sect. 20.2 (Kelsey et al. 2302.05998 Sect. 2.2.2); the isotropic-continuum value at the speeds above,
      c_L^-3/(c_L^-3 + 2 c_T^-3) = 0.0975, is printed as a check.  A_anh = 7.41e-56 s^4 (1109.1193 Table I).
      Primaries born as a line at the top of the acoustic band, h x 15 THz = 62.0 meV (Sect. 20.2; their spectrum is
      forgotten by the absorption time).
  Slab d = 4 mm (the 1 x 1 x 0.4 cm^3 Si chip of Ren et al. 2012.12430, Sect. IV).
  Films (MODELLING CHOICE, the mean-field estimate of App. E.25): film 1 niobium-like, 2 Delta = 3.0 meV; film 2
  aluminum, 2 Delta_BCS = 0.36 meV (Sect. 1.5, 7.2); c_1 = c_2 = 0.05 (two films) or c_Al = 0.10 (one Al film);
  tbar = 0.9 (AMM Si -> Al average 0.938 with the 0 K Al constants, Sect. 20.3); l_bare = 1e-3 per hit
  ("a loss of ~0.1% for each phonon-surface interaction", Leman 1109.1193 Sect. III G).
  Film escape ratios r = t_l/t0 (Sect. 20.3, 0 K Al): 60 nm Al film 0.72 (AMM) - 0.94 (DMM); t_l is proportional to the
  thickness, so r = 4 is a film of 330 nm (AMM) / 260 nm (DMM) and r = 8 one of 670 / 510 nm.
  Luke birth spectra, parametrized by the number-mean phonon energy <E_L> (Sect. 20.1, eq:20.1-Eluke):
    shape A (one carrier speed): number density ~ E^2 on [0, E_max], <E_L> = 3 E_max/4, energy share below x (x/E_max)^4;
    shape B (spread of speeds): number density flat on [0, 2 <E_L>], energy share below x (x / 2<E_L>)^2.
  Operating point: <E_L> = 0.84 meV for silicon electrons at 1 V/cm, from a carrier-transport Monte Carlo (CMPMC,
    validated; 20.1's balance estimate 1.09 meV is higher by construction).  The Monte Carlo
    gives 0.84 / 1.90 / 4.62 meV for silicon electrons at 1 / 10 / 100 V/cm; the
    scan 0.75-4.7 meV used below is a parametric range that includes germanium (0.755 meV at 1 V/cm).
  Germanium near-surface Luke phonons ~300 GHz (electrons) and ~700 GHz (holes), Hertel & Pyle 1109.4343 Sect. 1,
    i.e. 1.24 and 2.90 meV (comparison marks only).
  Target band of Sect. 19.5: collection alone requires r_coll = 1.128 (band 1.099-1.152) (bal19_5.log).
"""
import os
import numpy as np
from scipy.optimize import brentq
from scipy.stats import beta as beta_dist
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker
from film20_5 import FilmResponse, p_first, BW

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "..", "tex", "figures", "ch20")
os.makedirs(FIG, exist_ok=True)

H_MEVS = 4.135667696e-12          # Planck constant, meV s
CL, CT = 9.00e3, 5.40e3           # m/s
VBAR = (CL**-2 + 2 * CT**-2) / (CL**-3 + 2 * CT**-3)
FLA = 0.093
FLA_ISO = CL**-3 / (CL**-3 + 2 * CT**-3)
A_ANH = 7.41e-56                  # s^4
D_SLAB = 4e-3                     # m
E_PRIM = 1.5e13 * H_MEVS          # meV, top of the acoustic band
TWO_D_AL, TWO_D_NB = 0.36, 3.0    # meV
COV, TBAR, LSURF = 0.05, 0.9, 1e-3
E_OP = 0.84                       # meV, Si electrons at 1 V/cm (transport Monte Carlo)
TARGET, TLO, THI = 1.128, 1.099, 1.152
RS = [np.inf, 8.0, 4.0, 0.94, 0.72]

print(f"mean speed v = {VBAR/1e3:.3f} km/s, f_LA = {FLA} (isotropic-continuum value {FLA_ISO:.4f}), "
      f"face-hit rate v/2d = {VBAR/(2*D_SLAB):.4e} /s")
print(f"primary line h x 15 THz = {E_PRIM:.2f} meV")

# ---------------------------------------------------------------- energy grid (bins, log spaced)
NB = 1400
edges = np.geomspace(0.002, 70.0, NB + 1)
E = np.sqrt(edges[:-1] * edges[1:])
gam = FLA * A_ANH * (E / H_MEVS) ** 5
P = np.zeros((NB, NB))
for j in range(1, NB):
    lo, hi = edges[:j] / E[j], np.minimum(edges[1:j + 1] / E[j], 1.0)
    w = 2.0 * (beta_dist.cdf(hi, 3, 3) - beta_dist.cdf(lo, 3, 3))
    if w.sum() > 0:
        s = (w * E[:j]).sum()
        P[:j, j] = w * E[j] / s            # exact energy conservation on the grid

# ---------------------------------------------------------------- film responses
FR = {}
for r in RS:
    FR[r] = FilmResponse(r)
print("\nfilm responses (Kaplan cascade, 0.01 Delta grid to 120 Delta, held above):")
for r in RS:
    F = FR[r]
    print(f"  r = t_l/t0 = {r}: Y at 3, 4, 5, 5.46, 6, 10, 24, 60 Delta = "
          + ", ".join(f"{v:.4f}" for v in F.Y([3, 4.0000001, 5, 5.456, 6, 10, 24, 60]))
          + f"; p_first at 2.01, 3, 10, 24 Delta = " + ", ".join(f"{v:.3f}" for v in p_first([2.01, 3, 10, 24], r)))


def film_tables(two_d, r):
    w = E / (two_d / 2)
    above = E >= two_d
    p = np.where(above, p_first(np.maximum(w, 2.0), r), 0.0)
    y = np.where(above, FR[r].Y(np.maximum(w, 2.0)), 0.0)
    return above, p, y


_RET = {}


def return_matrix(two_d, r):
    """Ret[i, j]: phonons returned into substrate bin i per first-broken phonon absorbed in bin j (film gap two_d)."""
    if (two_d, r) in _RET:
        return _RET[(two_d, r)]
    F = FR[r]
    D = two_d / 2
    Ret = np.zeros((NB, NB))
    jj = np.where(E >= two_d)[0]
    S = F.spectrum(E[jj] / D)                                  # energy per output bin (Delta units) per first-broken phonon
    ec = (np.arange(S.shape[1]) + 0.5) * BW * D                 # output-bin centers in meV
    ib = np.clip(np.searchsorted(edges, ec) - 1, 0, NB - 1)
    keep = ec >= TWO_D_AL                                       # phonons below 2 Delta_Al are not returned (see docstring)
    for k, j in enumerate(jj):
        n = np.where(keep, S[k] * D / ec, 0.0)                  # number of phonons per output bin
        np.add.at(Ret[:, j], ib, n)
        Ret[j:, j] = 0.0                                        # returned phonons are softer than the absorbed one
    _RET[(two_d, r)] = Ret
    return Ret


def solve(n0, films, kappa=0.0, lsurf=LSURF, ret=False, ybar=None):
    """films: list of (coverage, 2Delta, r); the last is aluminum.  Returns per-film signal, absorbed energy, bare loss,
    the absorbed-energy spectrum per film (meV weights per bin), and N."""
    wall = VBAR / (2 * D_SLAB)
    gs, ys = [], []
    for k_, (c, td, r) in enumerate(films):
        above, p, y = film_tables(td, r)
        g = wall * c * TBAR * p
        if k_ == len(films) - 1 and kappa > 0:
            g = g + wall * c * TBAR * kappa * (~above)
            y = np.where(above, y, ybar if ybar is not None else 0.0)
        gs.append(g)
        ys.append(y)
    gloss = wall * (1 - sum(c for c, _, _ in films)) * lsurf * np.ones(NB)
    gabs = sum(gs) + gloss
    Rets = [return_matrix(td, r) if ret else None for (c, td, r) in films]
    N = np.zeros(NB)
    src = n0.copy()
    for j in range(NB - 1, -1, -1):
        N[j] = src[j] / (gabs[j] + gam[j])
        if j > 0:
            src[:j] += gam[j] * N[j] * P[:j, j]
            if ret:
                for (c, td, r), g, R in zip(films, gs, Rets):
                    if E[j] >= td:
                        src[:j] += g[j] * N[j] * R[:j, j]
    sig = np.array([(E * g * N * y).sum() for g, y in zip(gs, ys)])
    global LAST_DROP
    LAST_DROP = 0.0
    if ret:   # energy leaving the films that is not returned (below 2 Delta_Al), for the closure check
        for (c, td, r), g, y, R in zip(films, gs, ys, Rets):
            m = E >= td
            retE = (R * E[:, None]).sum(axis=0)
            LAST_DROP += (g * N * (E * (1 - y) - retE))[m].sum()
    absd = np.array([(E * g * N).sum() for g in gs])
    spec = [E * g * N for g in gs]
    loss = (E * gloss * N).sum()
    return sig, absd, loss, spec, N


def line(e0):
    n0 = np.zeros(NB)
    i = np.argmin(abs(E - e0))
    n0[i] = 1.0 / E[i]
    return n0


def luke(emean, shape):
    if shape == "A":
        emax = 4 * emean / 3
        cdf = np.clip(edges / emax, 0, 1) ** 3
    else:
        emax = 2 * emean
        cdf = np.clip(edges / emax, 0, 1)
    n = np.diff(cdf)
    return n / (n * E).sum()


def s_below(x, emean, shape):
    return (x / (4 * emean / 3)) ** 4 if shape == "A" else (x / (2 * emean)) ** 2


def s_ng(emean, shape, r, ybar):
    n = luke(emean, shape)
    _, _, y = film_tables(TWO_D_AL, r)
    m = E >= TWO_D_AL
    return ((n * E)[m] * (y[m] / ybar - 1)).sum()


def wquant(x, w, q):
    c = np.cumsum(w) / w.sum()
    return np.interp(q, c, x)


# ---------------------------------------------------------------- primaries, two thick films (flat yield 0.59)
two_inf = [(COV, TWO_D_NB, np.inf), (COV, TWO_D_AL, np.inf)]
print("\n== primaries, two films ==")
wall = VBAR / (2 * D_SLAB)
gh = wall * (2 * COV * TBAR + (1 - 2 * COV) * LSURF)
gl = wall * (COV * TBAR + (1 - 2 * COV) * LSURF)
print(f"absorption time above 3 meV {1e6/gh:.1f} us; between 0.36 and 3 meV {1e6/gl:.1f} us; "
      f"bare-loss share {wall*(1-2*COV)*LSURF/gh:.4f} / {wall*(1-2*COV)*LSURF/gl:.4f}")
sp, ap, lp, specp, Np = solve(line(E_PRIM), two_inf)
print(f"closure: absorbed + bare loss = {ap.sum() + lp:.6f} of the birth energy")
print(f"absorbed by film 1 (Nb-like) {ap[0]:.4f}, film 2 (Al) {ap[1]:.4f}, bare loss {lp:.4f}")
wabs = specp[0] + specp[1]
print(f"absorbed primary energy: energy-weighted mean phonon energy {(wabs*E).sum()/wabs.sum():.2f} meV, "
      f"number-weighted {wabs.sum()/(wabs/E).sum():.2f} meV; share below 3 meV {wabs[E < TWO_D_NB].sum()/wabs.sum():.3f} "
      f"(of the Al film's absorbed energy {specp[1][E < TWO_D_NB].sum()/specp[1].sum():.3f})")
for q in (0.1, 0.5, 0.9):
    v = wquant(E, wabs, q)
    print(f"  absorbed-energy quantile {q:.1f}: {v:.2f} meV = {v/0.18:.1f} Delta_Al = {v/4.135667696:.2f} THz")
for x in (6.5, 10.8, 21.6):
    print(f"  absorbed primary energy above {x} meV ({x/0.18:.0f} Delta_Al): {wabs[E > x].sum()/wabs.sum():.2e}")
print(f"Al film alone: absorbed-energy-weighted mean {(specp[1]*E).sum()/specp[1].sum():.2f} meV")
print(f"eps_prim = {sp.sum():.4f}; a_prim = {sp[1]/sp.sum():.4f}")

# ---------------------------------------------------------------- sub-gap share
print("\n== Luke energy share below 2 Delta_Al = 0.36 meV, s_sub ==")
grid = [0.5, 0.75, E_OP, 1.0, 1.24, 1.5, 2.0, 2.9, 4.7]
for sh in "AB":
    print(f"  shape {sh}: " + ", ".join(f"{em:.2f} meV {s_below(TWO_D_AL, em, sh):.4f}" for em in grid))

# ---------------------------------------------------------------- one aluminum film (coverage 0.10)
LAST_DROP = 0.0
RSET = [np.inf, 8.0, 4.0, 0.94, 0.72]
ONE, ONEL = {}, {}
print("\n== one aluminum film (coverage 0.10), conserved variant (escaped and relaxation phonons return) ==")
for r in RSET:
    one = [(2 * COV, TWO_D_AL, r)]
    s0, a0, l0, sp0, _ = solve(line(E_PRIM), one, ret=True)
    drop = LAST_DROP
    # Ybar for kappa = 1: signal per energy first absorbed above threshold (lost-variant definition, thick-film 0.590)
    sl0, al0, _, _, _ = solve(line(E_PRIM), one)
    ybar = sl0[0] / al0[0]
    print(f"r = {r}: eps_prim = {s0.sum():.4f}; closure signal + bare loss + dropped sub-gap = {s0.sum() + l0 + drop:.5f}")
    for kap in (0.0, 1.0):
        s0k, _, _, _, _ = solve(line(E_PRIM), one, kappa=kap, ybar=ybar, ret=True)
        for sh in "AB":
            vals = []
            for em in grid:
                sl, _, _, _, _ = solve(luke(em, sh), one, kappa=kap, ybar=ybar, ret=True)
                ONE[(r, kap, sh, em)] = sl.sum() / s0k.sum()
                vals.append(ONE[(r, kap, sh, em)])
            print(f"   kappa {kap:.0f}, shape {sh}: r_coll at " + ", ".join(f"{em:.2f}:{v:.4f}" for em, v in zip(grid, vals)))
    if np.isinf(r):
        for sh in "AB":
            for em in (0.75, E_OP, 2.0):
                ident = 1 + s_ng(em, sh, r, ybar) - s_below(TWO_D_AL, em, sh)
                print(f"   identity, shape {sh}, {em:.2f} meV, kappa 0: s_ng = {s_ng(em, sh, r, ybar):+.4f}, "
                      f"1 + s_ng - s_sub = {ident:.4f}, solve {ONE[(r, 0.0, sh, em)]:.4f}")
    dev = max(abs(ONE[(r, 0.0, sh, em)] - ONE[(np.inf, 0.0, sh, em)]) for sh in "AB" for em in grid)
    print(f"   max |r_coll(r) - r_coll(thick)| over the grid, kappa 0: {dev:.4f}")

print("\n== one aluminum film, lost variant (selective sink: phonons leaving after a pair break deleted) ==")
for r in RSET:
    one = [(2 * COV, TWO_D_AL, r)]
    s0, _, _, _, _ = solve(line(E_PRIM), one)
    for sh in "AB":
        for em in grid:
            sl, _, _, _, _ = solve(luke(em, sh), one)
            ONEL[(r, sh, em)] = sl.sum() / s0.sum()
    print(f"r = {r}: eps_prim = {s0.sum():.4f}; " + "; ".join(
        f"{sh}: " + ", ".join(f"{em:.2f}:{ONEL[(r, sh, em)]:.4f}" for em in (0.75, E_OP, 1.0, 2.0)) for sh in "AB"))
    for sh in "AB":
        em = 0.75
        print(f"   s_ng (lost), shape {sh}, 0.75 meV: {s_ng(em, sh, r, solve(line(E_PRIM), one)[0][0] / solve(line(E_PRIM), one)[1][0]):+.4f}")

print("\n== uniform signal-free sink: bare-face loss raised, conserved variant, 0.84 meV ==")
SINK = {}
for films_lab, films in (("one Al film, thick", [(2 * COV, TWO_D_AL, np.inf)]), ("one Al film, 60 nm", [(2 * COV, TWO_D_AL, 0.72)]),
                         ("two films, thick", [(COV, TWO_D_NB, np.inf), (COV, TWO_D_AL, np.inf)]),
                         ("two films, 60 nm", [(COV, TWO_D_NB, 0.72), (COV, TWO_D_AL, 0.72)])):
    for ls in (1e-3, 0.01, 0.1, 0.3):
        s0, _, _, _, _ = solve(line(E_PRIM), films, lsurf=ls, ret=True)
        v = [solve(luke(E_OP, sh), films, lsurf=ls, ret=True)[0].sum() / s0.sum() for sh in "AB"]
        SINK[(films_lab, ls)] = (s0.sum(), v)
        print(f"  {films_lab}, l_bare = {ls:g}: eps_prim = {s0.sum():.4f}; r_coll A {v[0]:.4f}, B {v[1]:.4f}")
print("max r_coll over the uniform-sink scan: " + f"{max(max(x[1]) for x in SINK.values()):.4f}")

# ---------------------------------------------------------------- two films
print("\n== two films (Nb-like + Al, coverage 0.05 each, same r), conserved variant ==")
TWO = {}
emg = np.geomspace(0.4, 6.0, 41)
for r in RSET:
    two = [(COV, TWO_D_NB, r), (COV, TWO_D_AL, r)]
    s0, _, l0, _, _ = solve(line(E_PRIM), two, ret=True)
    drop = LAST_DROP
    sl0, al0, _, _, _ = solve(line(E_PRIM), two)
    ybar_al = sl0[1] / al0[1]
    print(f"r = {r}: eps_prim = {s0.sum():.4f}, a_prim = {s0[1]/s0.sum():.4f}; closure {s0.sum() + l0 + drop:.5f}")
    for kap in (0.0, 1.0):
        s0k, _, _, _, _ = solve(line(E_PRIM), two, kappa=kap, ybar=ybar_al, ret=True)
        for sh in "AB":
            pts, wps = [], []
            for em in grid:
                sl, _, _, _, _ = solve(luke(em, sh), two, kappa=kap, ybar=ybar_al, ret=True)
                pts.append(sl.sum() / s0k.sum())
                wps.append(sl[1] / sl.sum() - s0k[1] / s0k.sum())
                TWO[(r, kap, sh, em)] = pts[-1]
            rr = None
            if kap == 0.0 and r in (np.inf, 0.72):
                rr, ww = [], []
                for em in emg:
                    sl, _, _, _, _ = solve(luke(em, sh), two, ret=True)
                    rr.append(sl.sum() / s0k.sum()); ww.append(sl[1] / sl.sum() - s0k[1] / s0k.sum())
                TWO[(r, kap, sh)] = (np.array(rr), np.array(ww))
                m = (emg >= 0.75) & (emg <= 4.7)
                print(f"   varpi_O (kappa 0, shape {sh}) at " + ", ".join(f"{em:.2f}:{v:+.3f}" for em, v in zip(grid, wps)))
                print(f"   range over 0.75-4.7 meV (fine grid), shape {sh}: {np.array(rr)[m].min():.3f}-{np.array(rr)[m].max():.3f}"
                      f" (max at {emg[m][np.array(rr)[m].argmax()]:.2f} meV)")
            print(f"   kappa {kap:.0f}, shape {sh}: r_coll at " + ", ".join(f"{em:.2f}:{v:.4f}" for em, v in zip(grid, pts)))
print("two films, lost variant (selective sink, as in the lumped film), for comparison:")
TWOL = {}
for r in (np.inf, 0.72):
    two = [(COV, TWO_D_NB, r), (COV, TWO_D_AL, r)]
    s0, _, _, _, _ = solve(line(E_PRIM), two)
    for sh in "AB":
        TWOL[(r, sh)] = [solve(luke(em, sh), two)[0].sum() / s0.sum() for em in emg]
        TWOL[(r, sh, E_OP)] = solve(luke(E_OP, sh), two)[0].sum() / s0.sum()
    m = (emg >= 0.75) & (emg <= 4.7)
    allv = np.concatenate([np.array(TWOL[(r, sh)])[m] for sh in "AB"])
    print(f"  r = {r}: eps_prim = {s0.sum():.4f}; 0.75-4.7 meV {allv.min():.3f}-{allv.max():.3f}; at 0.84 meV "
          f"{min(TWOL[(r, sh, E_OP)] for sh in 'AB'):.3f}-{max(TWOL[(r, sh, E_OP)] for sh in 'AB'):.3f}")

# flat-yield reference (sub-gap and bare-face effects alone; no film relaxation spectrum)
print("\n== two thick films with a flat yield 0.59 above each gap (sub-gap and bare-face effects alone) ==")


def solve_flat(n0, films, kappa=0.0, lsurf=LSURF):
    wall = VBAR / (2 * D_SLAB)
    gs = []
    kap = [0.0] * (len(films) - 1) + [kappa]
    for (c, td), k in zip(films, kap):
        above = (E >= td).astype(float)
        gs.append(wall * c * TBAR * (above + k * (1 - above)))
    gloss = wall * (1 - sum(c for c, _ in films)) * lsurf * np.ones(NB)
    gabs = sum(gs) + gloss
    N = np.zeros(NB)
    src = n0.copy()
    for j in range(NB - 1, -1, -1):
        N[j] = src[j] / (gabs[j] + gam[j])
        if j > 0:
            src[:j] += gam[j] * N[j] * P[:j, j]
    sig = np.array([(E * g * N * 0.59).sum() for g in gs])
    return sig, (E * gloss * N).sum()


twof = [(COV, TWO_D_NB), (COV, TWO_D_AL)]
for kap in (0.0, 1.0):
    spf, _ = solve_flat(line(E_PRIM), twof, kappa=kap)
    for sh in "AB":
        pts = [solve_flat(luke(em, sh), twof, kappa=kap)[0].sum() / spf.sum() for em in grid]
        print(f"  kappa {kap:.0f}, shape {sh}: " + ", ".join(f"{em:.2f}:{v:.4f}" for em, v in zip(grid, pts)))
spf, _ = solve_flat(line(E_PRIM), twof, lsurf=10 * LSURF)
for sh in "AB":
    sl, _ = solve_flat(luke(0.75, sh), twof, lsurf=10 * LSURF)
    print(f"  bare loss x10, shape {sh}, 0.75 meV, sub-gap lost: r_coll = {sl.sum()/spf.sum():.4f}")

# ---------------------------------------------------------------- band summary
print("\n== band summary (conserved variant; kappa 0 and 1; shapes A, B) ==")
allc = [v for k, v in ONE.items() if 0.75 <= k[3] <= 4.7] + [v for k, v in TWO.items() if len(k) == 4 and 0.75 <= k[3] <= 4.7]
for r in RSET:
    sub = [v for k, v in ONE.items() if k[0] == r and 0.75 <= k[3] <= 4.7] + \
          [v for k, v in TWO.items() if len(k) == 4 and k[0] == r and 0.75 <= k[3] <= 4.7]
    op = [v for k, v in ONE.items() if k[0] == r and k[3] == E_OP] + [v for k, v in TWO.items() if len(k) == 4 and k[0] == r and k[3] == E_OP]
    print(f"r = {r}: 0.75-4.7 meV {min(sub):.3f}-{max(sub):.3f}; at 0.84 meV {min(op):.3f}-{max(op):.3f}")
op_all = [v for k, v in ONE.items() if k[3] == E_OP] + [v for k, v in TWO.items() if len(k) == 4 and k[3] == E_OP]
print(f"all conserved cases (r = inf ... 0.72, one and two films, kappa 0/1, A/B): 0.75-4.7 meV {min(allc):.3f}-{max(allc):.3f}; "
      f"at 0.84 meV {min(op_all):.3f}-{max(op_all):.3f}; with the uniform-sink scan max {max(max(x[1]) for x in SINK.values()):.3f}")
print(f"target band of Sect. 19.5: {TLO}-{THI}; reached by a conserved case: {any(TLO <= v for v in allc)}")
lostop = [ONEL[(r, sh, E_OP)] for r in RSET for sh in "AB"]
print(f"lost variant (selective sink), one Al film at 0.84 meV: r = 4 {min(ONEL[(4.0, s, E_OP)] for s in 'AB'):.3f}-"
      f"{max(ONEL[(4.0, s, E_OP)] for s in 'AB'):.3f}; 60 nm {min(ONEL[(r, s, E_OP)] for r in (0.94, 0.72) for s in 'AB'):.3f}-"
      f"{max(ONEL[(r, s, E_OP)] for r in (0.94, 0.72) for s in 'AB'):.3f}")

# ---------------------------------------------------------------- Mach number scale for silicon electrons
ME = 510998.95e3   # meV
mc = 3 / (1 / 0.916 + 2 / 0.191)
scale = 2 * mc * ME * (CL / 2.99792458e8) ** 2
print(f"\nSi electron conductivity mass m_c = {mc:.4f} m_e; E_max = {scale:.4f} meV x (M - 1)")

# ---------------------------------------------------------------- figure
plt.rcParams.update({"font.size": 9, "font.family": "serif", "mathtext.fontset": "cm"})
fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.6, 3.7))
ax.axhspan(TLO, THI, color="#fde9c9", lw=0)
ax.axhline(TARGET, color="#d08a2a", lw=0.7, ls="--")
ax.plot(emg, TWO[(np.inf, 0.0, "A")][0], color="C0", lw=1.1, label="two thick films, one speed")
ax.plot(emg, TWO[(np.inf, 0.0, "B")][0], color="C3", lw=1.1, label="two thick films, spread")
ax.plot(emg, TWO[(0.72, 0.0, "B")][0], color="C3", lw=1.0, ls="--", label=r"two 60 nm films, spread")
ax.plot(emg, TWOL[(np.inf, "B")], color="0.45", lw=0.9, ls=":", label="two thick films, spread, relaxation phonons deleted")
yy = []
for em in emg:
    one = [(2 * COV, TWO_D_AL, 0.72)]
    s0, _, _, _, _ = solve(line(E_PRIM), one)
    yy.append(solve(luke(em, "B"), one)[0].sum() / s0.sum())
ax.plot(emg, yy, color="C4", ls="-.", lw=1.0, label=r"one 60 nm Al film, spread, selective sink")
print("fig: one 60 nm Al film, lost variant, spread, at 0.5, 1, 2, 5 meV: " + ", ".join(f"{np.interp(x, emg, yy):.3f}" for x in (0.5, 1, 2, 5)))
ax.axhline(1.0, color="k", lw=0.6)
ax.axvline(E_OP, color="0.5", lw=0.7, ls="--")
for x in (1.24, 2.9):
    ax.axvline(x, color="0.6", lw=0.6, ls=":")
    bx.axvline(x, color="0.6", lw=0.6, ls=":")
bx.plot(emg, TWO[(np.inf, 0.0, "A")][1], color="C0", lw=1.1)
bx.plot(emg, TWO[(np.inf, 0.0, "B")][1], color="C3", lw=1.1)
ax.set_xscale("log"); bx.set_xscale("log")
ax.set_xlim(0.4, 6); bx.set_xlim(0.4, 6); ax.set_ylim(0.7, 1.5)
for a in (ax, bx):
    a.set_xlabel(r"mean Luke-phonon energy $\langle E_{\mathrm{L}}\rangle$ (meV)")
    a.set_xticks([0.5, 1, 2, 5]); a.set_xticklabels(["0.5", "1", "2", "5"])
    a.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.set_ylabel(r"collection ratio $\mathfrak{r}_{\mathrm{coll}}$")
bx.set_ylabel(r"collection contrast $\varpi_O$")
ax.set_title("(a)", fontsize=8); bx.set_title("(b)", fontsize=8)
# legend below both panels, clear of the curves and of the reference lines
fig.legend(*ax.get_legend_handles_labels(), fontsize=7, frameon=False, loc="lower center", ncol=2)
fig.tight_layout(rect=(0, 0.17, 1, 1))
fig.savefig(os.path.join(FIG, "fig20_rcoll.pdf"))
print("\nwrote fig20_rcoll.pdf")
