Okay, let's break down this cosmological age calculation step-by-step.

**1. Evaluate the Hubble time in Gyr.**

First, we need to convert $H_0$ to units of Gyr$^{-1}$.

$H_0 = 70.0 \frac{\text{km}}{\text{s}\cdot\text{Mpc}}$

1 Mpc = $3.0857 \times 10^{19}$ km
1 year = 365.25 days $\approx 3.15576 \times 10^7$ s

So, $H_0 = 70.0 \frac{\text{km}}{\text{s}\cdot(3.0857 \times 10^{19} \text{ km})} = \frac{70.0}{3.0857 \times 10^{19}} \frac{1}{\text{s}} = 2.27 \times 10^{-18} \frac{1}{\text{s}}$

The Hubble time is $1/H_0 = \frac{1}{2.27 \times 10^{-18} \text{ s}} \approx 4.41 \times 10^{18} \text{ s}$.

Now, convert this to Gyr:

$1 \text{ Gyr} = 3.15576 \times 10^{17} \text{ s}$

$1/H_0 = \frac{4.41 \times 10^{18} \text{ s}}{3.15576 \times 10^{17} \text{ s/Gyr}} \approx 13.99 \text{ Gyr} \approx 14.0 \text{ Gyr}$

**2. Evaluate the age of a flat matter-only universe in Gyr, and explain why it is LESS than $1/H_0$.**

For a flat matter-only (Einstein-de Sitter) universe, the Friedmann equation simplifies to:

$H(z) = H_0 (1+z)^{3/2}$

The age of the universe is given by integrating from the present ($z=0$) to infinity:

$t_0 = \int_0^\infty \frac{dz}{H(z)} = \int_0^\infty \frac{dz}{H_0 (1+z)^{3/2}} = \frac{1}{H_0} \int_0^\infty (1+z)^{-3/2} dz$

$t_0 = \frac{1}{H_0} \left[ -2(1+z)^{-1/2} \right]_0^\infty = \frac{1}{H_0} \left[ 0 - (-2)(1)^{-1/2} \right] = \frac{2}{H_0}$

However, this is incorrect. The correct integral is:

$t_0 = \int_0^\infty \frac{dz}{H_0 (1+z)^{3/2}} = \frac{1}{H_0} \int_0^\infty (1+z)^{-3/2} dz = \frac{1}{H_0} \left[ -2(1+z)^{-1/2} \right]_0^\infty = \frac{1}{H_0} [0 - (-2)] = \frac{2}{H_0}$

The age of a flat matter-only universe is $t_0 = \frac{2}{3H_0}$.

$t_0 = \frac{2}{3 \times 2.27 \times 10^{-18} \text{ s}} = \frac{2}{6.81 \times 10^{-18} \text{ s}} \approx 2.93 \times 10^{17} \text{ s}$

Converting to Gyr:

$t_0 = \frac{2.93 \times 10^{17} \text{ s}}{3.15576 \times 10^{17} \text{ s/Gyr}} \approx 0.93 \text{ Gyr}$

The age is less than $1/H_0$ because in a matter-dominated universe, the expansion rate was higher in the past.  The universe expanded more slowly in the past, so it took longer to reach its current size.  The integral accounts for this slowing expansion.

**3. Evaluate the LCDM age in Gyr with the given formula.**

We are given the formula: $t_0 = \frac{2}{3H_0\sqrt{\Omega_\Lambda}}\,\mathrm{asinh}\sqrt{\Omega_\Lambda/\Omega_m}$.

We have $H_0 = 2.27 \times 10^{-18}$ s$^{-1}$, $\Omega_m = 0.3$, and $\Omega_\Lambda = 0.7$.

$\sqrt{\Omega_\Lambda/\Omega_m} = \sqrt{0.7/0.3} = \sqrt{7/3} \approx 1.5275$

$\mathrm{asinh}(1.5275) \approx 1.2355$

$t_0 = \frac{2}{3(2.27 \times 10^{-18} \text{ s}^{-1})\sqrt{0.7}} (1.2355) = \frac{2}{3(2.27 \times 10^{-18} \text{ s}^{-1})(0.8366)} (1.2355) = \frac{2}{5.51 \times 10^{-18}} (1.2355) = 3.63 \times 10^{17} \text{ s} (1.2355) = 4.49 \times 10^{17} \text{ s}$

Converting to Gyr:

$t_0 = \frac{4.49 \times 10^{17} \text{ s}}{3.15576 \times 10^{17} \text{ s/Gyr}} \approx 1.42 \text{ Gyr}$

**4. Explain why the LCDM age comes out close to $1/H_0$ (the roles of early deceleration and late acceleration).**

The LCDM age is close to $1/H_0$ because of the interplay between early deceleration and late acceleration. In the early universe, matter dominated, and the expansion decelerated. However, as the universe expanded, the density of matter decreased, while the density of dark energy (represented by $\Omega_\Lambda$) remained constant. Eventually, dark energy became the dominant component, and the expansion began to accelerate. This late acceleration stretches out the time axis, making the age of the universe closer to the Hubble time. The $\mathrm{asinh}$ term accounts for the effect of this acceleration. Without the acceleration, the age would be significantly less than $1/H_0$.

\[
\begin{aligned}
\mathrm{hubble\_time\_gyr} &= 14.0 \\
\mathrm{matter\_age\_gyr} &= 0.93 \\
\mathrm{lcdm\_age\_gyr} &= 1.42
\end{aligned}
\]