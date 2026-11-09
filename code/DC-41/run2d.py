"""DC-41: the spec's 2-D quadrature on the whole production table at (nmu, n_eta) = (6, 10); doubled (12, 20) on every 4th row (and every row done before the
machine load forced the thinning).  Resumable; empty doubled columns mean "not doubled".  Writes data/table_2d.csv."""
import csv, os, time
import numpy as np
import bcs1d as b, bubbles2d as d
H = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(H, "data")
rows = list(csv.DictReader(open(os.path.join(D, "table_grid.csv"))))
out = os.path.join(D, "table_2d.csv")
hdr = ["y", "Q", "v_2d", "v_2d_doubled", "dv_doubling", "v_1d", "dv_2d_1d", "ImP33_2d", "ReP33_2d", "ImPg_2d", "RePg_2d", "dPg_2d_1d"]
done = len(list(csv.reader(open(out)))) - 1 if os.path.exists(out) else 0
f = open(out, "a", newline=""); w = csv.writer(f)
if done <= 0:
    w.writerow(hdr); done = 0
t0 = time.time()
for i, r in enumerate(rows):
    if i < done: continue
    y, Q = float(r["y"]), float(r["Q"])
    B1 = d.bubbles(y, Q, nmu=6, n=10); g1 = d.grpa(B1); v1 = g1.imag / B1["P33"].imag - 1
    p, g = b.Pg(y, Q); v = g.imag / p.imag - 1
    if i % 4 == 0:
        B2 = d.bubbles(y, Q, nmu=12, n=20); g2 = d.grpa(B2); v2 = g2.imag / B2["P33"].imag - 1; Bf, gf, vf = B2, g2, v2; dd = "%.7g" % abs(v1 - v2); v2s = "%.7g" % v2
    else:
        Bf, gf, vf = B1, g1, v1; dd = ""; v2s = ""
    w.writerow(["%.7g" % y, "%.7g" % Q, "%.7g" % v1, v2s, dd] + ["%.7g" % z for z in (v, abs(vf - v), Bf["P33"].imag, Bf["P33"].real, gf.imag, gf.real, abs(gf - g))]); f.flush()
print("done", time.time() - t0)
