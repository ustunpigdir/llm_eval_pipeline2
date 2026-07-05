**1. Horizon radius $c/H$ in Gpc:**

Given $H = 70.0$ km/s/Mpc, we first convert this to Gpc units:
\[ H = 70.0 \times 10^3 \text{ km/Mpc} \times \frac{1 \text{ Mpc}}{3.086 \times 10^{24} \text{ km}} = 2.27 \times 10^{-42} \text{ Gpc}^{-1} \]

Now, calculate the horizon radius:
\[ r = \frac{c}{H} = \frac{1}{2.27 \times 10^{-42} \text{ Gpc}^{-1}} \approx 4.40 \text{ Gpc} \]

**2. Gibbons-Hawking temperature in units of $10^{-30}$ K:**

\[ T_{GH} = \frac{\hbar H}{2\pi k_B} = \frac{6.626 \times 10^{-34} \text{ J s} \times 2.27 \times 10^{-42} \text{ Gpc}^{-1}}{2\pi \times 1.38 \times 10^{-23} \text{ J/K}} \times \frac{1 \text{ Gpc}}{3.086 \times 10^{24} \text{ km}} \times \frac{1 \text{ km}}{10^3 \text{ m}} \times \frac{1 \text{ m/s}}{c} \times \frac{1 \text{ K}}{1.38 \times 10^{-23} \text{ J/K}} \]

\[ T_{GH} \approx 1.23 \times 10^{-30} \text{ K} \]

**3. Cooling of radiation background:**

The CMB temperature today is 2.725 K. Assuming $T \propto a^{-1}$, the number of e-folds needed for the background to cool below $T_{GH}$ is:
\[ \ln\left(\frac{2.725}{T_{GH}}\right) = \ln\left(\frac{2.725}{1.23 \times 10^{-30}}\right) \approx 112.5 \]

**4. Observations in pure de Sitter space:**

An observer in pure de Sitter space would detect a thermal bath at the Gibbons-Hawking temperature, similar to the Unruh effect (particle creation in accelerating frames) and the Hawking effect (particle creation at event horizons). This is because de Sitter space has a cosmological horizon, and the observer is accelerating away from it.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{horizon\_gpc} &= 4.40 \text{ Gpc} \\
\mathrm{gh\_temp\_e30\_K} &= 1.23 \times 10^{-30} \\
\mathrm{efolds\_to\_gh} &= 112.5
\end{aligned}
\]