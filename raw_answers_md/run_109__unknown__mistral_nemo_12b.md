**1. Hubble Time in Gyr**

The Hubble time is given by $1/H_0$. Given $H_0 = 70.0$ km/s/Mpc, we first convert Mpc to km:

\[1 \text{ Mpc} = 3.0857 \times 10^{19} \text{ km}\]

So,

\[H_0 = 70.0 \text{ km/s/Mpc} \times \frac{1 \text{ Mpc}}{3.0857 \times 10^{19} \text{ km}} = 2.278 \times 10^{-18} \text{ s}^{-1}\]

Now, the Hubble time in Gyr (1 Gyr = 10^9 years = 3.156 \times 10^16 s):

\[\text{Hubble time} = \frac{1}{H_0} = \frac{1}{2.278 \times 10^{-18} \text{ s}^{-1}} \times 3.156 \times 10^{16} \text{ s/Gyr} \approx 14.5 \text{ Gyr}\]

**2. Age of a Flat Matter-Only Universe**

The age of a flat matter-only universe is given by:

\[\frac{2}{3H_0}\]

Substituting the value of $H_0$ we found:

\[\text{Matter-only age} = \frac{2}{3} \times \frac{1}{2.278 \times 10^{-18} \text{ s}^{-1}} \times 3.156 \times 10^{16} \text{ s/Gyr} \approx 13.4 \text{ Gyr}\]

This is less than $1/H_0$ because the universe is decelerating due to gravity, so it takes longer to reach a given scale factor than it would if it were expanding at a constant rate.

**3. LCDM Age**

The age of a flat LCDM universe with $\Omega_m = 0.3$ and $\Omega_\Lambda = 0.7$ is given by:

\[\frac{2}{3H_0\sqrt{\Omega_\Lambda}} \text{ asinh}\sqrt{\frac{\Omega_\Lambda}{\Omega_m}}\]

Substituting the given values:

\[\text{LCDM age} = \frac{2}{3 \times 2.278 \times 10^{-18} \text{ s}^{-1} \times \sqrt{0.7}} \text{ asinh}\sqrt{\frac{0.7}{0.3}} \times 3.156 \times 10^{16} \text{ s/Gyr} \approx 13.8 \text{ Gyr}\]

**4. Why LCDM Age is Close to $1/H_0$**

The LCDM universe starts decelerating like the matter-only universe, but then it begins to accelerate due to dark energy. This acceleration causes the universe to expand faster than it would in a matter-only universe, so the age of the LCDM universe is closer to $1/H_0$.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{hubble\_time\_gyr} &= 14.5 \text{ Gyr} \\
\mathrm{matter\_age\_gyr} &= 13.4 \text{ Gyr} \\
\mathrm{lcdm\_age\_gyr} &= 13.8 \text{ Gyr}
\end{aligned}
\]