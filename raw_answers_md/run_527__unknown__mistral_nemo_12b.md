**Step 1: Calculate $\kappa$**

Given:
- Electron mass $m = 9.11 \times 10^{-31}$ kg
- Planck's constant $\hbar = 6.63 \times 10^{-34}$ J s
- Barrier height $V_0 = 5.00$ eV = $5.00 \times 1.6 \times 10^{-19}$ J
- Electron energy $E = 1.00$ eV = $1.00 \times 1.6 \times 10^{-19}$ J
- Barrier width $L = 1.00$ nm = $1.00 \times 10^{-9}$ m

First, calculate $\kappa$:
\[
\kappa = \sqrt{\frac{2m(V_0 - E)}{\hbar^2}} = \sqrt{\frac{2 \times 9.11 \times 10^{-31} \times (5.00 - 1.00) \times 1.6 \times 10^{-19}}{(6.63 \times 10^{-34})^2}} \approx 1.05 \times 10^{10} \text{ m}^{-1}
\]
Convert $\kappa$ to nm$^{-1}$:
\[
\kappa_{\text{per nm}} = \kappa \times 10^9 \approx 1.05 \times 10^{19} \text{ nm}^{-1}
\]

**Step 2: Calculate $\kappa L$**

\[
\kappa L = (1.05 \times 10^{19}) \times (1.00 \times 10^{-9}) = 1.05
\]

**Step 3: Calculate the prefactor**

\[
\text{prefactor} = \frac{16 E (V_0 - E)}{V_0^2} = \frac{16 \times 1.00 \times 1.6 \times 10^{-19} \times (5.00 - 1.00) \times 1.6 \times 10^{-19}}{ (5.00 \times 1.6 \times 10^{-19})^2} \approx 0.016
\]

**Step 4: Calculate $\log_{10} T$**

\[
\log_{10} T = \log_{10} \left( 0.016 \times e^{-2 \times 1.05} \right) = \log_{10} 0.016 + \log_{10} e^{-2.1} \approx -2.8 - 2.1 = -4.9
\]

**Step 5: Change in $T$ if $L$ doubles**

If $L$ doubles, $\kappa L = 2.1$. Then,
\[
\log_{10} T = \log_{10} \left( 0.016 \times e^{-4.2} \right) \approx -2.8 - 4.2 = -7.0
\]
The exponential sensitivity is evident as the transmission probability decreases significantly when the barrier width increases.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{kappa\_per\_nm} &= 1.05 \times 10^{19} \text{ nm}^{-1} \\
\mathrm{kappa\_L} &= 1.05 \\
\mathrm{prefactor} &= 0.016 \\
\mathrm{log10\_T} &= -4.9
\end{aligned}
\]