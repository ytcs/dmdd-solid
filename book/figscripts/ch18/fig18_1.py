"""Fig. 18.1 (fig:18-tree): one sampled cascade tree started by an electron with 50 eV of kinetic energy in silicon,
in the energy-only random-k model of Sect. 18.1, and the Monte Carlo statistics quoted in Sect. 18.1.
Output: tex/figures/ch18/fig18_1.pdf; numbers in fig18_1.log.

Model (every choice named here is named in the caption and the text):
  - carriers are electrons (e) or holes (h) with kinetic energy x above their band edge;
  - random-k impact-ionization kernel: a carrier of type t at x > Eg ionizes into (t, x1) + (t, x2) + (tbar, x3) with
    x1 + x2 + x3 = x - Eg and joint density proportional to sqrt(x1 x2 x3) (constant matrix elements, parabolic
    densities of states rho(x) ~ x^(1/2)): (x1, x2, x3)/(x - Eg) ~ Dirichlet(3/2, 3/2, 3/2). Holes are confined to the
    valence band width B_h = 12 eV (draws with a hole above B_h are rejected), as in [RK, Sect. II A];
  - threshold theta_ii = 1 (random-k ignores crystal-momentum conservation);
  - phonon channel: emission of one optical phonon of energy omega_AB = 63 meV [RK, Sect. II B];
  - ratio of the two rates, [RK, Eq. (8)]: Gamma_ph/Gamma_ii = A_AB (105/2pi) (x - omega_AB)^(1/2)/(x - Eg)^(7/2),
    energies in eV; probability of ionization at the next event 1/(1 + ratio) [RK, Eq. (10)];
  - no plasmon channel (its weight is part of the impact-ionization channel, Sect. 18.1);
  - the one silicon set of Chap. 18 (si_cascade18.py): Eg = 1.160 eV (123 K), A_AB = 5.703 eV^3, the continuum calibration
    on the measured pair energy 3.749 eV (Sect. 18.4).
  [RK] K. Ramanathan and N. Kurinsky, Phys. Rev. D 102, 063026 (2020), arXiv:2004.10709.
The statistics quoted in the text (50 eV electron; 10 eV pair seeds) are deterministic: the generating-function solver of
casc18_3.py (cell-mass densities, grid E_g/184, the same model) gives the distribution of the pair number exactly; the Monte Carlo
here only draws the tree of the figure and cross-checks the mean.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from si_cascade18 import A_AB, EG_SI, OM_SI, BH_SI

EG, WAB, A, BH = EG_SI, OM_SI, A_AB, BH_SI
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "tex", "figures", "ch18", "fig18_1.pdf")
LOG = os.path.join(HERE, "fig18_1.log")


NPH_LOW = [0]  # phonon emissions from carriers below 6 eV (running counter)


def p_ii(x):
    if x <= EG:
        return 0.0
    r = A * 105.0 / (2 * np.pi) * np.sqrt(max(x - WAB, 0.0)) / (x - EG) ** 3.5
    return 1.0 / (1.0 + r)


def split(rng, t, x):
    y = x - EG
    while True:
        f = rng.dirichlet([1.5, 1.5, 1.5]) * y
        types = (t, t, "h" if t == "e" else "e")
        if all(not (tt == "h" and ff > BH) for tt, ff in zip(types, f)):
            return list(zip(types, f))


def cascade(rng, seeds, record=False):
    """Run one cascade from a list of (type, x). Returns (new pairs, heat, phonons, tree)."""
    stack = [(t, x, None, 0) for t, x in seeds]
    tree = []  # per carrier: dict(type, path [(step, x)], parent, birth_x, events)
    npairs, heat, nph = 0, 0.0, 0
    while stack:
        t, x, parent, depth = stack.pop()
        node = dict(type=t, birth=x, parent=parent, path=[x], ii=[], depth=depth)
        idx = len(tree)
        tree.append(node)
        while True:
            p = p_ii(x)
            if p == 0.0 and x <= EG:
                heat += x  # relaxes to the band edge
                node["path"].append(0.0)
                break
            if rng.random() < p:
                prods = split(rng, t, x)
                npairs += 1
                # the carrier itself continues as the first product of its own type
                x_new = prods[0][1]
                node["ii"].append((len(node["path"]) - 1, x, x_new))
                for tt, ff in prods[1:]:
                    stack.append((tt, ff, (idx, x), depth + 1))
                x = x_new
                node["path"].append(x)
            else:
                if x < 6.0:
                    NPH_LOW[0] += 1
                x -= WAB
                heat += WAB
                nph += 1
                node["path"].append(x)
    return npairs, heat, nph, tree


def stats(rng, seeds_fn, n):
    N = np.empty(n)
    for i in range(n):
        N[i] = cascade(rng, seeds_fn(rng))[0]
    return N


def main():
    rng = np.random.default_rng(20261106)
    lines = []
    lines.append("Energy-only random-k cascade, Eg = %.3f eV, omega_AB = %.3f eV, A_AB = %.3f eV^3, B_h = %.0f eV" % (EG, WAB, A, BH))
    for x in (EG + 3 * WAB, EG + 5 * WAB, 1.5, 2.0, 2.5, 3.0, 5.0, 8.0, 10.0):
        lines.append("p_ii(%.3f eV) = %.2e" % (x, p_ii(x)))
    # crossover p_ii = 1/2 by bisection
    lo, hi = 2.0, 20.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if p_ii(mid) < 0.5:
            lo = mid
        else:
            hi = mid
    lines.append("p_ii = 1/2 at x = %.3f eV (bisection)" % (0.5 * (lo + hi)))

    # deterministic statistics (generating function, casc18_3.Casc)
    import casc18_3 as G
    cb = G.Casc(X=46.0)
    P50 = cb.pair(50.0, 0.0)                      # seed electron at 50 eV, hole at the edge: N - 1 = new pairs
    n = np.arange(len(P50))
    md = ((n - 1) * P50).sum()
    vd = ((n - 1) ** 2 * P50).sum() - md ** 2
    lines.append("50 eV electron (generating function, exact on its grid): mean new pairs %.3f, var %.3f, var/mean %.3f, "
                 "50/mean = %.2f eV per pair, mean heat 50 - mean*Eg = %.2f eV" % (md, vd, vd / md, 50.0 / md, 50.0 - md * EG))
    n50 = 4000
    N = stats(rng, lambda r: [("e", 50.0)], n50)
    m, v = N.mean(), N.var(ddof=1)
    lines.append("   Monte Carlo cross-check, %d cascades: mean new pairs %.2f +- %.2f, var/mean %.3f" %
                 (n50, m, N.std(ddof=1) / np.sqrt(n50), v / m))
    tot = 10.0 - EG
    for name, args in (("equal split", G.beta_seed(np.inf, tot)), ("uniform split", G.beta_seed(1.0, tot)),
                       ("all to the electron", (np.array([tot]), np.array([0.0]), np.array([1.0])))):
        P = cb.pair(*args)
        mm, vv = G.moments(P)
        lines.append("omega = 10 eV pair seed (excess %.2f eV), %s: mean N_eh %.3f, var %.3f, P(2) %.3f, P(3) %.3f, P(4) %.3f" %
                     (tot, name, mm, vv, P[2], P[3], P[4]))

    # representative tree: first seed whose new-pair count equals round(mean)
    target = int(round(md))
    seed = 0
    while True:
        r = np.random.default_rng(1000 + seed)
        NPH_LOW[0] = 0
        npairs, heat, nph, tree = cascade(r, [("e", 50.0)])
        if npairs == target:
            break
        seed += 1
    lines.append("plotted tree: rng seed %d, new pairs %d, carriers %d, phonons %d (%d emitted below 6 eV), heat %.2f eV, check 50 = %.4f" %
                 (1000 + seed, npairs, len(tree), nph, NPH_LOW[0], heat, npairs * EG + heat))
    draw(tree)
    with open(LOG, "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


def draw(tree):
    # order carriers depth-first by parent so children sit to the right of their parent
    children = {i: [] for i in range(len(tree))}
    roots = []
    for i, n in enumerate(tree):
        if n["parent"] is None:
            roots.append(i)
        else:
            children[n["parent"][0]].append(i)
    order = []

    def visit(i):
        order.append(i)
        # children in order of the energy at which they were created (highest first)
        for c in sorted(children[i], key=lambda c: -tree[c]["parent"][1]):
            visit(c)
    for r0 in roots:
        visit(r0)
    xpos = {i: k for k, i in enumerate(order)}
    col = {"e": "#1f5aa6", "h": "#c8641e"}
    fig, ax = plt.subplots(figsize=(5.4, 3.6))
    ymin = 0.05
    for i, n in enumerate(tree):
        xs = xpos[i]
        path = np.maximum(np.array(n["path"]), ymin)
        jumps = {k for (k, _, _) in n["ii"]}
        # phonon steps drawn solid (a run of 63 meV losses), impact-ionization jumps dotted
        start = 0
        for k in range(len(path) - 1):
            if k in jumps:
                if k > start:
                    ax.plot([xs, xs], [path[start], path[k]], color=col[n["type"]], lw=1.4, solid_capstyle="butt")
                ax.plot([xs, xs], [path[k], path[k + 1]], color=col[n["type"]], lw=0.7, ls=":")
                start = k + 1
        if len(path) - 1 > start:
            ax.plot([xs, xs], [path[start], path[-1]], color=col[n["type"]], lw=1.4, solid_capstyle="butt")
        for (_, e_before, e_after) in n["ii"]:
            ax.plot([xs], [e_before], "o", ms=2.6, color="0.15", zorder=5)
        if n["parent"] is not None:
            p, e_evt = n["parent"]
            ax.plot([xpos[p], xs], [e_evt, e_evt], color="0.55", lw=0.5)
            ax.plot([xs, xs], [e_evt, max(n["birth"], ymin)], color="0.55", lw=0.5, ls=":")
    ax.axhline(EG, color="0.3", lw=0.6, ls="--")
    ax.text(len(tree) - 0.4, EG * 1.12, r"$E_{\mathrm{g}}$", fontsize=8, ha="right", va="bottom", color="0.3")
    ax.set_yscale("log")
    ax.set_ylim(ymin, 70)
    ax.set_xlim(-0.8, len(tree) - 0.2)
    ax.set_xticks([])
    ax.set_xlabel("carriers of the cascade", fontsize=8)
    ax.set_ylabel("kinetic energy above the band edge (eV)", fontsize=8)
    ax.tick_params(labelsize=7.5)
    ax.plot([], [], color=col["e"], lw=1.4, label="electron")
    ax.plot([], [], color=col["h"], lw=1.4, label="hole")
    ax.plot([], [], "o", ms=2.6, color="0.15", label="impact ionization")
    ax.legend(fontsize=7, frameon=False, loc="upper right")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.tight_layout()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    fig.savefig(OUT)


if __name__ == "__main__":
    main()
