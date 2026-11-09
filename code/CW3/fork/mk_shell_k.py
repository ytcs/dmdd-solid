#!/usr/bin/env python3
"""Write EPW filkf = shell_k.txt: uniform N^3 crystal-coordinate list (default N = 24) for elecselfen.
The Gamma/delta map needs Gamma_n(k) for all bands within fsthick of the gap; a uniform list is then
interpolated in energy (spec in returns/R16/CW3.md, LE-76). Usage: python3 mk_shell_k.py [N] > shell_k.txt"""
import sys
N = int(sys.argv[1]) if len(sys.argv) > 1 else 24
pts = [(i/N, j/N, k/N) for i in range(N) for j in range(N) for k in range(N)]
print(f"{len(pts)} crystal")
for a, b, c in pts: print(f"  {a:.8f} {b:.8f} {c:.8f} {1/len(pts):.10e}")
