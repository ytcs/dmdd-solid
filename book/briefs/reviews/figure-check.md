# Final figure check (SPINE production directive, user 2026-11-02)
Book: /home/user/dmdd-solid/book. Figures are PDFs in tex/figures/chNN/, made by scripts in figscripts/chNN/. Captions and limitbox plots are in the chapter tex. You check the chapters assigned to you, every figure and every Limit Check plot in them.

For each figure:
1. Render it to PNG at 150 dpi with `pdftoppm -png -r 150 <pdf> <scratch>/name` into your own scratch folder under /tmp/claude-0/figcheck-<part>/, then look at the image (Read tool).
2. Read its caption and the paragraph that cites it in the tex (grep the includegraphics path).
3. Check:
   - **Visual overlaps:** annotations, labels, legends, curves or tick labels that collide, are clipped at the frame, or run outside the axes.
   - **Semantic placement:** each label, arrow, bracket and marker sits on the curve, region, edge or threshold it names. Colours and line styles match the legend and the caption. Axis labels and units match the caption and text. Numbers printed in the figure agree with the text and the script log.
   - **Legibility at print size:** fonts not smaller than about 6 pt at the included width.
4. Fix every problem in the figure SCRIPT, never in the PDF. Rerun the script, which regenerates the PDF and its log, then re-render and look again to confirm. If a fix changes a number in the log, update the text to match. If the caption is wrong rather than the figure, fix the caption with an exact edit.

Rules: change no physics; touch only your chapters' figscripts, figures and captions. Run only light Python; if a script needs heavy cached data that is missing, log it instead of recomputing. Afterwards build privately (cd tex && latexmk -pdf -interaction=nonstopmode -outdir=/tmp/claude-0/build-fig-<part> main.tex; rerun once on the pass limit): 0 errors. Write ledgers/REVIEWS/figures/<part>.md: figure → OK / FIXED (what) / LOGGED (why). Do not commit. Final message ≤ 8 lines with counts.
