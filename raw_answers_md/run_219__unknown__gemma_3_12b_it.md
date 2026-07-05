Okay, let's break down this Schwarzschild orbital mechanics problem step-by-step.

**1. Radii of Event Horizon, Photon Sphere, and ISCO**

*   **Event Horizon (r<sub>H</sub>):** The event horizon is defined as the Schwarzschild radius, where $r_H = 2GM/c^2$.
*   **Photon Sphere (r<sub>ph</sub>):** The photon sphere is at $r_{ph} = 3GM/c^2$.
*   **ISCO (Innermost Stable Circular Orbit) (r<sub>isco</sub>):** For a non-rotating (Schwarzschild) black hole, the ISCO radius for a circular equatorial orbit is $r_{isco} = 6GM/c^2$.

Now, let's calculate these values:

*   $M = 10\,M_\odot = 10 \times 1.989 \times 10^{30} \, \text{kg} = 1.989 \times 10^{31} \, \text{kg}$
*   $GM = (6.674 \times 10^{-11} \, \text{N m}^2/\text{kg}^2) \times (1.989 \times 10^{31} \, \text{kg}) = 1.327 \times 10^{21} \, \text{N m}^2$
*   $GM/c^2 = (1.327 \times 10^{21} \, \text{N m}^2) / (2.998 \times 10^{8} \, \text{m/s})^2 = (1.327 \times 10^{21}) / (9.0 \times 10^{16}) \approx 14.75 \, \text{m}$

Therefore:

*   $r_H = 2GM/c^2 = 2 \times 14.75 = 29.5 \, \text{m}$
*   $r_{ph} = 3GM/c^2 = 3 \times 14.75 = 44.25 \, \text{m}$
*   $r_{isco} = 6GM/c^2 = 6 \times 14.75 = 88.5 \, \text{m}$

To express the ISCO radius in km:

$r_{isco} = 88.5 \, \text{m} = 0.0885 \, \text{km}$

**2. Orbital Frequency at the ISCO (f)**

We are given that $\Omega^2 = GM/r^3$ for circular orbits.  At the ISCO, $r = r_{isco} = 6GM/c^2$.  Therefore:

$\Omega^2 = \frac{GM}{(6GM/c^2)^3} = \frac{GM}{(216(GM)^3/c^6)} = \frac{c^6}{216(GM)^2}$

$\Omega = \frac{c^3}{6\sqrt{6}(GM)} = \frac{c^3}{6\sqrt{6} (1.327 \times 10^{21})} = \frac{(2.998 \times 10^8)^3}{6\sqrt{6} (1.327 \times 10^{21})} \approx \frac{2.685 \times 10^{25}}{1.125 \times 10^{22}} \approx 2387 \, \text{rad/s}$

The orbital frequency is $f = \Omega / (2\pi) = 2387 / (2\pi) \approx 379.4 \, \text{Hz}$.

**3. Dominant GW Frequency (f<sub>GW</sub>)**

The dominant gravitational wave emission frequency is twice the orbital frequency:

$f_{GW} = 2f = 2 \times 379.4 = 758.8 \, \text{Hz}$.

**4. GW Signal Shutoff and ISCO Scaling**

The gravitational wave signal "shuts off" near the ISCO frequency because, as the test particle spirals inward, it reaches a point where further inspiral becomes very slow.  The rate of change of the orbital parameters (which drive the gravitational wave emission) diminishes significantly.  Beyond the ISCO, the orbit is unstable, and the particle plunges rapidly into the black hole, producing a short, intense burst of gravitational waves that is not well-characterized by the inspiral model.

The ISCO frequency scales with $M$ as $f \propto 1/M^3$.  This can be seen from the equation $\Omega = \frac{c^3}{6\sqrt{6}(GM)}$.  Since $c$ is constant, and $6\sqrt{6}$ is a constant, we have $f \propto \frac{1}{GM}$.  Since $r_{isco} = 6GM/c^2$, we have $GM = \frac{c^2 r_{isco}}{6}$.  Substituting this into the frequency equation, we get $f \propto \frac{1}{c^2 r_{isco}/6} = \frac{6}{c^2 r_{isco}}$.  Since $r_{isco} \propto M$, we have $f \propto \frac{6}{c^2 M} \propto \frac{1}{M^3}$.

\[
\begin{aligned}
\mathrm{r\_isco\_km} &= 0.0885 \\
\mathrm{f\_orbital\_hz} &= 379.4 \\
\mathrm{f\_gw\_hz} &= 758.8
\end{aligned}
\]