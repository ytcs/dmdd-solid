"""Sect. 22.2 (exact gaps in the theory): every number printed in Sect. 22.2 that is not quoted from another section.
Log: gaps22_2.log.   Run: python gaps22_2.py > gaps22_2.log   (< 1 s).

Part A. Counts of Table 22.2 (tab:22-gaps) by what each gap limits and by the kind of missing step.
  The rows below are the rows of the table, in table order, one per gap, keyed by home section.  The class of
  each row follows the definitions of Sect. 22.2:
    proof     : a theorem is missing; no number printed in the book changes when it is supplied;
    bounded   : a number is missing, but the book gives a bound or a two-sided bracket for it;
    estimated : a number is missing, and the book gives an estimate (a model value or a factor) that is not a bound;
    unsized   : a number is missing and the book assigns it no size (the third case of Sect. 8.8);
    test      : the book's number is computed, and the missing step is an independent check of it.
  Kind of missing step: theory (a proof or a method), calc (a specified calculation), meas (a measurement).
  Every statement, size and class is read from the section named in the key (tex/chNN/sNN-M.tex as accepted).
  Ch9 revision (ruling R2): one grouped row for the eight circle cells of tab:9-atlas (unsized, calc).
  Revision (Ch22 reviews, ruling R2): each row names ONE missing step; 14.5 is split into two rows; 11.5 is a method
  (kind theory); 17.1 electron-following and both 18.2 rows are unsized, as in tab:17-nuisances and tab:18-nuisances.
Part B. Worked example 22.2 (we:22-constant): the constant term of the yield, read from Sect. 18.2.
  Inputs (all quoted from Ch18, not recomputed here):
    E_g = 1.160 eV and eps_eh = 3.232 E_g of the calibrated energy-only cascade (fig:18-limit-moments caption, s18-2);
    b_N = 0.35 (seed with all the energy on one carrier) and 0.008 (uniform split), s18-3 l.86 (casc18_3.log);
    the step model's mean omega/eps_eh + 0.19, s18-3 l.93.
"""

ROWS = [
    # key, class, kind
    ("8.6 labels outside the off-shell window", "proof", "theory"),
    ("8.6 uniformity in the number of nuclei", "proof", "theory"),
    ("8.6 dressing of gapless targets", "proof", "theory"),
    ("9.1 symmetry-allowed cells of the channel atlas", "unsized", "calc"),  # Ch9 ruling R2: the eight circle cells
    ("10.4 local fields of the transverse current", "bounded", "calc"),
    ("10.5 finite-q BSE with coupling block and lines", "estimated", "calc"),
    ("10.5 triplet beyond independent particles", "estimated", "calc"),
    ("10.5 self-trapped excitons of NaI", "unsized", "calc"),
    ("10.6 four-component finite-q response", "bounded", "calc"),
    ("10.6 spin-orbit mixing at the Ge edge", "estimated", "calc"),
    ("10.8 contact/second-order interference", "unsized", "calc"),
    ("10.8 bound shells in dark Compton scattering", "unsized", "calc"),
    ("10.9 fermionic absorption on bound shells", "bounded", "calc"),
    ("10.9 retarded density row of boosted dark matter", "bounded", "calc"),
    ("11.3 valence deformation above the zone", "unsized", "calc"),
    ("11.5 strongly anharmonic targets", "bounded", "theory"),  # R2: the missing step is a method
    ("11.6 cold in-band dielectric function of Si", "bounded", "meas"),
    ("11.7 cubic harmonics of the Si loss function", "estimated", "calc"),
    ("12.3 non-rigid Wannier ratio", "bounded", "calc"),
    ("12.3 off-diagonal dielectric elements in the Migdal probability", "estimated", "calc"),
    ("12.5 finite-q contact density beyond spherical atoms", "estimated", "calc"),
    ("12.6 site-resolved dynamical Born charges", "bounded", "calc"),
    ("12.6 scalar absorption with non-mass couplings", "unsized", "calc"),
    ("12.6 tagged-recoil Migdal measurement", "test", "meas"),
    ("13.8 converged exciton-phonon replicas", "estimated", "calc"),
    ("13.9 onset on one set of force constants", "test", "calc"),
    ("13.9 zero-phonon to phonon-assisted ratio", "estimated", "calc"),
    ("13.9 rate and reach at first-principles level", "estimated", "calc"),
    ("13.9 plane-wave f-sum check", "test", "calc"),
    ("13.9 germanium window and phonons", "unsized", "calc"),
    ("13.9 screening beyond the optical calibration", "estimated", "calc"),
    ("13.9 GaAs control of the window", "estimated", "calc"),
    ("13.9 cold absorption edge of Si", "test", "meas"),
    ("14.2 two-magnon interactions and bound pairs", "unsized", "calc"),
    ("14.4 longitudinal spin response from neutrons", "bounded", "meas"),
    ("14.5 chirality after three-phonon decay", "unsized", "calc"),
    ("14.5 phonon magnetic moments of order mu_B", "unsized", "calc"),  # R2: split from the chirality row
    ("14.5 optical activity at keV momenta", "unsized", "calc"),
    ("14.5 multiferroic response near ordering", "unsized", "calc"),
    ("15.3 amorphous WSi", "unsized", "calc"),
    ("15.4 strong-coupling Holstein factor", "estimated", "calc"),
    ("15.4 phonon-assisted spin current near the edge", "unsized", "calc"),
    ("15.4 scalar absorption near the edge", "unsized", "calc"),
    ("16.1 Dirac targets at strong coupling", "unsized", "theory"),
    ("16.3 depolarization of quantum dots", "unsized", "meas"),
    ("16.5 impurity band", "unsized", "calc"),
    ("16.5 local-field ratio of a donor", "estimated", "calc"),
    ("16.6 color-center yields at mK", "unsized", "meas"),
    ("16.7 tunneling-model parameters of films", "unsized", "meas"),
    ("16.8 interacting two-level systems", "unsized", "calc"),
    ("17.1 coherent Migdal response at small q", "unsized", "calc"),
    ("17.1 electron-following density at finite q", "unsized", "calc"),  # R2: unsized in tab:17-nuisances
    ("18.2 constant term and variance", "unsized", "theory"),  # R2: "model; unsized" in tab:18-nuisances
    ("18.2 renewal estimate as a lower value", "unsized", "theory"),  # R2: "computed; unsized" in tab:18-nuisances
    ("18.5 capture and terminal energies", "unsized", "calc"),
    ("18.5 impact ionization beyond first order", "unsized", "calc"),
    ("18.5 memory of crystal momentum", "estimated", "calc"),
    ("18.5 exciton and trapping rates at mK", "unsized", "meas"),
    ("19.2 charge yield below the binary threshold", "unsized", "calc"),
    ("19.6 release of close pairs at mK", "unsized", "calc"),
    ("19.6 stored energy in ionic crystals", "unsized", "meas"),
    ("19.6 size law and rate of the excess", "unsized", "calc"),
    ("19.6 carrier-driven defect reactions", "unsized", "calc"),
    ("19.6 sufficiency of the marks", "unsized", "calc"),
    ("20.1 trap emission and space charge", "unsized", "calc"),
    ("20.1 Luke spectrum beyond longitudinal phonons", "unsized", "calc"),
    ("20.1 validation of transport", "test", "calc"),
    ("20.4 thick-film offset of the quasiparticle yield", "estimated", "calc"),
    ("20.5 return of the gap energy at zero field", "unsized", "calc"),
    ("21.7 loss functions of the survivors", "bounded", "calc"),
    ("21.7 elastic constants", "estimated", "meas"),
    ("21.7 internal backgrounds", "estimated", "meas"),
    ("22.3 charged-current absorption", "unsized", "calc"),
    ("22.3 charge-density-wave collective modes", "unsized", "calc"),
]

CLASSES = ["proof", "bounded", "estimated", "unsized", "test"]
KINDS = ["theory", "calc", "meas"]


def part_a():
    print("Part A. Table 22.2 counts")
    print(f"  rows: {len(ROWS)}")
    for c in CLASSES:
        n = sum(1 for _, cl, _ in ROWS if cl == c)
        print(f"  class {c:9s}: {n}")
    for k in KINDS:
        n = sum(1 for _, _, kd in ROWS if kd == k)
        print(f"  kind  {k:9s}: {n}")
    n_number = sum(1 for _, cl, _ in ROWS if cl in ("bounded", "estimated", "unsized"))
    print(f"  rows that limit a number (bounded + estimated + unsized): {n_number}")
    # by chapter, for the reading paragraph
    chapters = {}
    for key, cl, _ in ROWS:
        ch = key.split(".")[0]
        chapters.setdefault(ch, []).append(cl)
    print("  per chapter (rows; unsized):")
    for ch, cls in chapters.items():
        print(f"    Ch{ch}: {len(cls)}; {cls.count('unsized')}")
    ro = [k for k, cl, _ in ROWS if cl == "unsized" and k.split(".")[0] in ("18", "19", "20")]
    print(f"  unsized rows in Ch18-20: {len(ro)} of {sum(1 for k, _, _ in ROWS if k.split('.')[0] in ('18','19','20'))}")
    el = [k for k, cl, _ in ROWS if k.split(".")[0] in ("10", "11", "12", "13")]
    el_uns = [k for k, cl, _ in ROWS if k.split(".")[0] in ("10", "11", "12", "13") and cl == "unsized"]
    print(f"  unsized rows in Ch10-13: {len(el_uns)} of {len(el)}")


def part_ranges():
    print("  chapter ranges (rows; unsized; bounded; estimated; test; proof):")
    for lo, hi in ((8, 9), (10, 13), (14, 17), (18, 20), (21, 22)):
        sel = [cl for k, cl, _ in ROWS if lo <= int(k.split(".")[0]) <= hi]
        print(f"    Ch{lo}-{hi}: {len(sel)}; " + "; ".join(f"{c} {sel.count(c)}" for c in CLASSES))
    meas = [k for k, _, kd in ROWS if kd == "meas"]
    print(f"  measurement rows ({len(meas)}): " + " | ".join(meas))
    th = [k for k, _, kd in ROWS if kd == "theory"]
    print(f"  proof/method rows ({len(th)}): " + " | ".join(th))


def part_b():
    print("Part B. Worked example 22.2")
    Eg = 1.160
    eps = 3.232 * Eg
    w = 10.0
    lead = w / eps
    print(f"  eps_eh = 3.232 x {Eg} eV = {eps:.3f} eV")
    print(f"  omega/eps_eh at 10 eV = {lead:.3f}")
    for name, b in (("one-sided seed", 0.35), ("uniform split", 0.008), ("step model", 0.19)):
        print(f"  {name:15s}: b = {b}, mean = {lead + b:.3f}, b/(omega/eps) = {b / lead:.4f} ({100 * b / lead:.1f} %)")
    # energy at which the one-sided constant term falls below 1 % of the leading term
    w1 = 0.35 / 0.01 * eps
    print(f"  one-sided b_N below 1 % of omega/eps_eh for omega > {w1:.0f} eV")


if __name__ == "__main__":
    part_a()
    part_ranges()
    part_b()
