**Step 1: Evaluate $\kappa$ in nm$^{-1}$ and the dimensionless product $\kappa L$**

Given:
- Electron mass $m = 9.11 \times 10^{-31}$ kg
- Planck's constant $\hbar = 6.63 \times 10^{-34}$ J s
- Barrier height $V_0 = 5.00$ eV
- Electron energy $E = 1.00$ eV
- Barrier width $L = 1.00$ nm

First, convert $V_0$ and $E$ to joules:
- $V_0 = 5.00$ eV = $5.00 \times 1.6 \times 10^{-19}$ J
- $E = 1.00$ eV = $1.00 \times 1.6 \times 10^{-19}$ J

Now, calculate $\kappa$:
\[
\kappa = \sqrt{\frac{2m(V_0 - E)}{\hbar^2}} = \sqrt{\frac{2 \times 9.11 \times 10^{-31} \times (5.00 - 1.00) \times 1.6 \times 10^{-19}}{(6.63 \times 10^{-34})^2}} \approx 1.05 \times 10^{10} \text{ nm}^{-1}
\]

Then, calculate $\kappa L$:
\[
\kappa L = (1.05 \times 10^{10} \text{ nm}^{-1}) \times (1.00 \text{ nm}) = 1.05 \times 10^{10}
\]

**Step 2: Evaluate the prefactor $16E(V_0-E)/V_0^2$**

\[
\text{prefactor} = 16 \times \frac{E(V_0 - E)}{V_0^2} = 16 \times \frac{(1.00 \times 1.6 \times 10^{-19})(5.00 - 1.00) \times (1.6 \times 10^{-19})^2}{(5.00 \times 1.6 \times 10^{-19})^2} \approx 0.016
\]

**Step 3: Evaluate $\log_{10} T$ including the prefactor**

\[
\log_{10} T = \log_{10} \left( \frac{16E(V_0-E)}{V_0^2} e^{-2\kappa L} \right) = \log_{10} (0.016) - \log_{10} (e^{2 \times 1.05 \times 10^{10}}) \approx -1.8 - 2 \times 1.05 \times 10^{10} \approx -2.05 \times 10^{10}
\]

**Step 4: Change in $T$ if $L$ doubles**

If $L$ doubles to $2.00$ nm, then $\kappa L = 2.10 \times 10^{10}$. Re-evaluating $\log_{10} T$:

\[
\log_{10} T = \log_{10} (0.016) - \log_{10} (e^{2 \times 2.10 \times 10^{10}}) \approx -1.8 - 2 \times 2.10 \times 10^{10} \approx -4.20 \times 10^{10}
\]

The exponential sensitivity is evident as the transmission probability decreases significantly when the barrier width is doubled.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{kappa\_per\_nm} &= 1.05 \times 10^{10} \text{ nm}^{-1} \\
\mathrm{kappa\_L} &= 1.05 \times 10^{10} \\
\mathrm{prefactor} &= 0.016 \\
\mathrm{log10\_T} &= -2.05 \times 10^{10}
\end{aligned}
\]