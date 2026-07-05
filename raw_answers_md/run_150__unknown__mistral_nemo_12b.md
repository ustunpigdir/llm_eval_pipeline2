**1. Horizon radius $c/H$ in Gpc:**

Given $H = 70.0$ km/s/Mpc, we first convert this to Gpc units:
\[ H = 70.0 \times 10^3 \text{ km/Mpc} \times \frac{1 \text{ Mpc}}{10^6 \text{ pc}} \times \frac{1 \text{ pc}}{3.086 \times 10^{18} \text{ m}} \times \frac{1 \text{ Gpc}}{3.24 \times 10^8 \text{ pc}} \]
\[ H \approx 6.63 \times 10^{-11} \text{ Gpc}^{-1} \]
Now, calculate the horizon radius:
\[ r = \frac{c}{H} \approx \frac{3 \times 10^5 \text{ m/s}}{6.63 \times 10^{-11} \text{ Gpc}^{-1}} \approx 4.52 \text{ Gpc} \]

**2. Gibbons-Hawking temperature in units of $10^{-30}$ K:**

\[ T_{GH} = \frac{\hbar H}{2\pi k_B} \approx \frac{1.05 \times 10^{-34} \text{ J s}}{2\pi \times 1.38 \times 10^{-23} \text{ J/K}} \times 6.63 \times 10^{-11} \text{ Gpc}^{-1} \]
\[ T_{GH} \approx 1.35 \times 10^{-30} \text{ K} \]

**3. Cooling of radiation background:**

The CMB temperature today is $T_0 = 2.725$ K. Assuming $T \propto a^{-1}$, the number of e-folds $N$ for the temperature to cool from $T_0$ to $T_{GH}$ is:
\[ 2.725 \times 10^{-3} \text{ K} \times e^{-N} = 1.35 \times 10^{-30} \text{ K} \]
\[ N = \ln\left(\frac{2.725 \times 10^{-3}}{1.35 \times 10^{-30}}\right) \approx 101.5 \]

**4. Observations in pure de Sitter space:**

An observer in pure de Sitter space would detect a thermal bath at the Gibbons-Hawking temperature, similar to the Unruh effect (particle creation in accelerating frames) and the Hawking effect (particle creation at event horizons). This is because de Sitter space has a cosmological horizon, and the observer is accelerating away from it.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{horizon\_gpc} &= 4.52 \text{ Gpc} \\
\mathrm{gh\_temp\_e30\_K} &= 1.35 \\
\mathrm{efolds\_to\_gh} &= 101.5
\end{aligned}
\]