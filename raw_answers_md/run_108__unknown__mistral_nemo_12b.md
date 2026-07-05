**1. Hubble time in Gyr:**

Given $H_0 = 70.0$ km/s/Mpc, we first convert the Hubble constant to Gyr$^{-1}$:

\[H_0 = 70.0 \text{ km/s/Mpc} \times \frac{1 \text{ Mpc}}{3.0857 \times 10^{19} \text{ km}} \times \frac{1 \text{ Gyr}}{3.1557 \times 10^{16} \text{ s}} \approx 2.157 \times 10^{-18} \text{ Gyr}^{-1}\]

Now, the Hubble time is:

\[\frac{1}{H_0} \approx \frac{1}{2.157 \times 10^{-18} \text{ Gyr}^{-1}} \approx 4.63 \times 10^{17} \text{ Gyr} \approx 13.8 \text{ Gyr}\]

**2. Age of a flat matter-only universe in Gyr:**

For a flat matter-only universe (Einstein-de Sitter), the age is given by:

\[t_0 = \frac{2}{3H_0}\]

Substituting the value of $H_0$ we found:

\[t_0 = \frac{2}{3 \times 2.157 \times 10^{-18} \text{ Gyr}^{-1}} \approx 1.40 \times 10^{17} \text{ Gyr} \approx 4.14 \text{ Gyr}\]

This is less than $1/H_0$ because the universe was expanding faster in the past, so it has been around for less time than the current expansion rate would suggest.

**3. LCDM age in Gyr:**

For a flat LCDM universe with $\Omega_m = 0.3$ and $\Omega_\Lambda = 0.7$, the age is given by:

\[t_0 = \frac{2}{3H_0\sqrt{\Omega_\Lambda}} \mathrm{asinh}\sqrt{\frac{\Omega_\Lambda}{\Omega_m}}\]

Substituting the given values:

\[t_0 = \frac{2}{3 \times 2.157 \times 10^{-18} \text{ Gyr}^{-1} \times \sqrt{0.7}} \mathrm{asinh}\sqrt{\frac{0.7}{0.3}} \approx 1.36 \times 10^{17} \text{ Gyr} \approx 4.01 \text{ Gyr}\]

**4. Why the LCDM age is close to $1/H_0$:**

The LCDM universe starts decelerating (due to matter dominance) and then accelerates (due to dark energy dominance). The early deceleration and late acceleration cause the age to be close to $1/H_0$. The universe was expanding faster in the past, but the late acceleration slows down the expansion rate, making the age closer to $1/H_0$.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{hubble\_time\_gyr} &= 13.8 \text{ Gyr} \\
\mathrm{matter\_age\_gyr} &= 4.14 \text{ Gyr} \\
\mathrm{lcdm\_age\_gyr} &= 4.01 \text{ Gyr}
\end{aligned}
\]