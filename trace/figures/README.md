# Publication Figures

These figures are rendered from the manuscript-reported CSV files, not new experiment runs. All fourteen figures use a shared serif-font style, thin black frames, light gray grids and restrained colors. Explanatory titles and provenance are kept outside the plot area so figures can be placed directly into a manuscript. `manifest.json` records each figure's title and source.

## Table 2

Use **`transfer.pdf`** for a LaTeX manuscript. `transfer.svg` is also vector-based; `transfer.png` is exported at 600 dpi (2400 x 1680 pixels). The nominal figure size is 4.0 x 2.8 inches.

- The three plotted observations are DeepSeek-V3.2: 47/50 (94.0%), GPT-4o: 46/50 (92.0%), and LLaVA-v1.5-7B: 47/50 (94.0%).
- The dashed line is the arithmetic mean of the three backbone-level percentages, displayed as 93.3%. With equal trial counts it also equals 140/150 after rounding.
- The x-axis contains categorical target models. Connecting segments guide the eye; they are not training dynamics, an ordered scale, or interpolation between models.
- The percentage axis starts at zero. No unreported baseline, standard deviation, confidence interval, or additional observation is introduced.

Suggested caption:

> Frozen cross-backbone evaluation of TRACE. The same acquired probing repertoire and router are evaluated on 50 trials for each target backbone without target-time acquisition or updates. Labels show VSR and trials with verified exposure. The dashed line indicates the arithmetic mean across backbones (93.3%). Connecting segments are visual guides between categorical models, not a temporal trajectory.

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=\columnwidth]{figures/transfer.pdf}
  \caption{Frozen cross-backbone evaluation of TRACE. Labels show VSR and trials
  with verified exposure out of 50 per backbone. The same acquired repertoire
  and router are reused without target-time updates. The dashed line is the
  arithmetic mean (93.3\%); connecting segments are visual guides between models.}
  \label{fig:trace-cross-backbone}
\end{figure}
```

## Other Figure Captions

Use the title and source in `manifest.json` when writing captions. Preserve these qualifications:

- `rq1_methods`: hatched bars are single-run references; the other four are five-seed means.
- `rq1_seeds`: acquisition seeds are categorical repeated runs, not a training trajectory.
- `evolution`: the seed-21 development trajectory is not the held-out shadow curve.
- `candidates`: stages are not mutually exclusive; subsequent pruning is a subset of admission.
- `low_transfer_runs`: displayed order is not a known seed-ID mapping. Displayed values average to 24.66%; the manuscript reports 24.67%.
- `local_rounds`: cumulative VSR uses the fixed 200-trial denominator, including failures.
- `output_controls`: displayed utility-loss values preserve manuscript rounding.

No supplied result CSV is altered by plotting. Figures do not establish an independent reproduction of the reported measurements.
