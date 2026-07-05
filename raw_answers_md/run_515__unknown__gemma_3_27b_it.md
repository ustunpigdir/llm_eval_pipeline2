Here's the derivation and calculation of the tunneling probability through the rectangular barrier, following the given instructions.

1. **Evaluate $\kappa$ and $\kappa L$**

First, we need to calculate $\kappa = \sqrt{2m(V_0-E)}/\hbar$.  We are given $E = 1.00$ eV and $V_0 = 5.00$ eV, so $V_0 - E = 4.00$ eV.  We need to convert this to Joules: $4.00 \text{ eV} \times 1.602 \times 10^{-19} \text{ J/eV} = 6.408 \times 10^{-19} \text{ J}$.

The mass of an electron is $m = 9.109 \times 10^{-31}$ kg, and $\hbar = 1.054 \times 10^{-34}$ J s.

Therefore,
$\kappa = \frac{\sqrt{2 \times 9.109 \times 10^{-31} \text{ kg} \times 6.408 \times 10^{-19} \text{ J}}}{1.054 \times 10^{-34} \text{ J s}} = \frac{\sqrt{1.169 \times 10^{-49}}}{1.054 \times 10^{-34}} = \frac{3.419 \times 10^{-25}}{1.054 \times 10^{-34}} \approx 3.243 \times 10^9 \text{ m}^{-1}$.

Since we want $\kappa$ in nm$^{-1}$, we divide by $10^9$:
$\kappa_{\text{per nm}} = 3.243 \text{ nm}^{-1}$.

The width of the barrier is $L = 1.00$ nm.  Thus, the dimensionless product is:
$\kappa L = 3.243 \times 1.00 = 3.243$.

2. **Evaluate the prefactor**

The prefactor is given by $16E(V_0-E)/V_0^2$.  We have $E = 1.00$ eV and $V_0 = 5.00$ eV, so $V_0 - E = 4.00$ eV.
$\text{prefactor} = \frac{16 \times 1.00 \text{ eV} \times 4.00 \text{ eV}}{(5.00 \text{ eV})^2} = \frac{64}{25} = 2.56$.

3. **Evaluate $\log_{10} T$**

The transmission probability is approximately $T \approx \frac{16 E (V_0-E)}{V_0^2} e^{-2\kappa L} = \text{prefactor} \times e^{-2\kappa L}$.
We have $\text{prefactor} = 2.56$ and $\kappa L = 3.243$, so $2\kappa L = 6.486$.
$T \approx 2.56 \times e^{-6.486} \approx 2.56 \times 9.85 \times 10^{-4} \approx 2.52 \times 10^{-3}$.

Now, we calculate $\log_{10} T$:
$\log_{10} T = \log_{10} (2.52 \times 10^{-3}) = \log_{10} 2.52 + \log_{10} 10^{-3} = 0.4017 - 3 = -2.5983$.

4. **How does $T$ change if $L$ doubles?**

If $L$ doubles, the new width is $L' = 2.00$ nm.  Then $\kappa L' = 3.243 \times 2.00 = 6.486$.
The new transmission probability is $T' \approx 2.56 \times e^{-2\kappa L'} = 2.56 \times e^{-12.972} \approx 2.56 \times 5.03 \times 10^{-6} \approx 1.288 \times 10^{-5}$.

The new $\log_{10} T'$ is:
$\log_{10} T' = \log_{10} (1.288 \times 10^{-5}) = \log_{10} 1.288 + \log_{10} 10^{-5} = 0.1104 - 5 = -4.8896$.

The difference between the original and new $\log_{10} T$ is $-4.8896 - (-2.5983) = -2.2913$. This demonstrates the exponential sensitivity of tunneling to the barrier width. Doubling the width reduces the transmission by a factor of approximately $e^{6.486} \approx 640$.

\[
\begin{aligned}
\mathrm{kappa\_per\_nm} &= 3.243 \\
\mathrm{kappa\_L} &= 3.243 \\
\mathrm{prefactor} &= 2.56 \\
\mathrm{log10\_T} &= -2.598
\end{aligned}
\]