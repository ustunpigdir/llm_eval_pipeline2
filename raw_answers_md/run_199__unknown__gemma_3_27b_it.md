
Here's the derivation of the GPS relativistic clock corrections, following the requested format.

**1. Gravitational Rate Difference (Blueshift)**

The gravitational time dilation effect is given by:

$\frac{\Delta t_s}{\Delta t_g} = \sqrt{1 - \frac{2GM_E}{r c^2}}$

where $\Delta t_s$ is the time interval on the satellite, $\Delta t_g$ is the time interval on the ground, $G$ is the gravitational constant, $M_E$ is Earth's mass, $r$ is the orbital radius, and $c$ is the speed of light.  Since we want the *difference* in rates, we need to compute $1/\Delta t_s - 1/\Delta t_g$.  It's easier to work with the fractional difference directly.  The satellite clock runs *faster* due to being in a weaker gravitational potential.

First, calculate the gravitational potential difference:

$\phi_g - \phi_s = \frac{GM_E}{R_E} - \frac{GM_E}{r}$

$\phi_g - \phi_s = GM_E (\frac{1}{R_E} - \frac{1}{r})$

$R_E = 6371 \times 10^3$ m
$r = 26562 \times 10^3$ m
$GM_E = 3.986 \times 10^{14}$ m$^3$/s$^2$

$\phi_g - \phi_s = 3.986 \times 10^{14} (\frac{1}{6371 \times 10^3} - \frac{1}{26562 \times 10^3})$
$\phi_g - \phi_s = 3.986 \times 10^{14} (1.5696 \times 10^{-7} - 3.7645 \times 10^{-8})$
$\phi_g - \phi_s = 3.986 \times 10^{14} (1.19315 \times 10^{-7})$
$\phi_g - \phi_s = 4.758 \times 10^7$ m$^2$/s$^2$

The fractional difference in time rates is approximately $\frac{\phi_g - \phi_s}{c^2}$.

$\frac{\Delta t_g}{\Delta t_s} = 1 + \frac{\phi_g - \phi_s}{c^2}$
$\frac{\Delta t_s}{\Delta t_g} = \frac{1}{1 + \frac{\phi_g - \phi_s}{c^2}} \approx 1 - \frac{\phi_g - \phi_s}{c^2}$

The rate difference is $\frac{1}{\Delta t_s} - \frac{1}{\Delta t_g} = \frac{\Delta t_g - \Delta t_s}{\Delta t_s \Delta t_g} \approx \frac{\phi_g - \phi_s}{c^2}$.

$\frac{\Delta t_g - \Delta t_s}{\Delta t_s \Delta t_g} = \frac{4.758 \times 10^7}{(3 \times 10^8)^2} = \frac{4.758 \times 10^7}{9 \times 10^{16}} = 5.2867 \times 10^{-10}$

This is the fractional difference per second.  To convert to microseconds per day:

$5.2867 \times 10^{-10} \text{ s}^{-1} \times 86400 \text{ s/day} \times 10^6 \text{ } \mu\text{s/s} = 45.68 \mu\text{s/day}$

The satellite clock runs faster.

**2. Velocity Rate Difference (Time Dilation)**

The special relativistic time dilation effect is given by:

$\frac{\Delta t_s}{\Delta t_g} = \sqrt{1 - \frac{v^2}{c^2}}$

where $v$ is the orbital speed.  We are given $v^2 = \frac{GM_E}{r}$.

$\frac{\Delta t_s}{\Delta t_g} = \sqrt{1 - \frac{GM_E}{r c^2}}$

$\frac{\Delta t_s}{\Delta t_g} = \sqrt{1 - \frac{3.986 \times 10^{14}}{(26562 \times 10^3) \times (3 \times 10^8)^2}} = \sqrt{1 - \frac{3.986 \times 10^{14}}{2.395 \times 10^{17}}} = \sqrt{1 - 0.001660} = \sqrt{0.99834} = 0.999169$

The rate difference is $\frac{1}{\Delta t_s} - \frac{1}{\Delta t_g} = \frac{1}{0.999169 \Delta t_g} - \frac{1}{\Delta t_g} = \frac{1 - 0.999169}{\Delta t_g \times 0.999169} = \frac{0.000831}{0.999169 \Delta t_g}$

The fractional difference is $\frac{1}{\Delta t_s} - \frac{1}{\Delta t_g} = \frac{1}{0.999169} - 1 = 1.000831 - 1 = 0.000831$

Converting to microseconds per day:

$0.000831 \text{ s}^{-1} \times 86400 \text{ s/day} \times 10^6 \text{ } \mu\text{s/s} = 7.18 \mu\text{s/day}$

The satellite clock runs slower.

**3. Net Rate Difference**

The net rate difference is the sum of the gravitational and velocity effects:

$45.68 \mu\text{s/day} - 7.18 \mu\text{s/day} = 38.50 \mu\text{s/day}$

**4. Ranging Error**

If uncorrected, the ranging error accumulates at a rate of 38.50 microseconds per day.  This means that after one day, the position estimate will be off by 38.50 microseconds multiplied by the speed of light.

Error = $38.50 \times 10^{-6} \text{ s} \times 3 \times 10^8 \text{ m/s} = 11.55 \text{ km}$

The two effects have opposite signs because the gravitational effect is due to the difference in gravitational potential, causing the satellite clock to run faster, while the velocity effect is due to special relativity, causing the satellite clock to run slower.  The gravitational effect dominates at the GPS satellite's altitude.



FINAL ANSWER

\[
\begin{aligned}
\mathrm{grav\_shift\_us\_day} &= 45.68 \\
\mathrm{velocity\_shift\_us\_day} &= -7.18 \\
\mathrm{net\_shift\_us\_day} &= 38.50
\end{aligned}
\]