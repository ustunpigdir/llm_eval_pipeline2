To compute the tunneling probability $T$ for an electron through a rectangular barrier, we follow the provided parameters:
$E = 1.00$ eV, $V_0 = 5.00$ eV, $L = 1.00$ nm.

### 1. Evaluation of $\kappa$ and $\kappa L$
The decay constant $\kappa$ is given by:
$$\kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar}$$
Using the constants:
- $m = 9.109 \times 10^{-31}$ kg
- $V_0 - E = 4.00$ eV $= 4.00 \times 1.602 \times 10^{-19}$ J $= 6.408 \times 10^{-19}$ J
- $\hbar = 1.05457 \times 10^{-34}$ J$\cdot$s

$$\kappa = \frac{\sqrt{2 \cdot (9.109 \times 10^{-31} \text{ kg}) \cdot (6.408 \times 10^{-19} \text{ J})}}{1.05457 \times 10^{-34} \text{ J}\cdot\text{s}}$$
$$\kappa = \frac{\sqrt{1.167 \times 10^{-48}}}{1.05457 \times 10^{-34}} = \frac{1.080 \times 10^{-24}}{1.05457 \times 10^{-34}} \approx 1.024 \times 10^{10} \text{ m}^{-1}$$
Converting to nm$^{-1}$ ($1 \text{ nm} = 10^{-9} \text{ m}$):
$$\kappa = 10.24 \text{ nm}^{-1}$$
The dimensionless product $\kappa L$ for $L = 1.00$ nm is:
$$\kappa L = 10.24 \times 1.00 = 10.24$$

### 2. Evaluation of the Prefactor
The prefactor is given by:
$$P = \frac{16 E (V_0 - E)}{V_0^2}$$
Substituting the values in eV:
$$P = \frac{16 \cdot (1.00) \cdot (5.00 - 1.00)}{5.00^2} = \frac{16 \cdot 4.00}{25.00} = \frac{64}{25} = 2.56$$

### 3. Evaluation of $\log_{10} T$
The transmission coefficient is:
$$T = P e^{-2\kappa L} = 2.56 \cdot e^{-2(10.24)} = 2.56 \cdot e^{-20.48}$$
Calculating the value:
$$e^{-20.48} \approx 1.27 \times 10^{-9}$$
$$T \approx 2.56 \cdot 1.27 \times 10^{-9} \approx 3.25 \times 10^{-9}$$
Taking the base-10 logarithm:
$$\log_{10} T = \log_{10}(2.56) + \log_{10}(e^{-20.48})$$
$$\log_{10} T = 0.4082 - (20.48 \cdot \log_{10} e) = 0.4082 - (20.48 \cdot 0.4343)$$
$$\log_{10} T = 0.4082 - 8.893 = -8.485$$

### 4. Effect of Doubling $L$
If $L$ doubles to $2.00$ nm, the exponent $2\kappa L$ doubles to $40.96$.
$$T_{new} = 2.56 \cdot e^{-40.96}$$
$$\log_{10} T_{new} = 0.4082 - (40.96 \cdot 0.4343) = 0.4082 - 17.786 = -17.378$$
The transmission probability decreases by approximately 9 orders of magnitude, demonstrating the extreme exponential sensitivity of tunneling to the barrier width.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{kappa\_per\_nm} &= 10.24 \\
\mathrm{kappa\_L} &= 10.24 \\
\mathrm{prefactor} &= 2.56 \\
\mathrm{log10\_T} &= -8.485
\end{aligned}
\]