Okay, let's break down the calculation of Mercury's perihelion precession using the first-order Schwarzschild result.

**1. GR Perihelion Advance per Orbit ($\Delta\phi$)**

The first-order GR perihelion advance per orbit is given by:

$\Delta\phi = \frac{24\pi^2}{c^2} \frac{GM_\odot a (1 - e^2)^{1/2}}{a^2} = \frac{24\pi^2}{c^2} \frac{GM_\odot}{a} \sqrt{1-e^2}$

where:
* $G$ is the gravitational constant
* $M_\odot$ is the mass of the Sun
* $a$ is the semi-major axis
* $e$ is the eccentricity
* $c$ is the speed of light

**2. Evaluation of $\Delta\phi$ in arcseconds per orbit**

We are given:
* $a = 5.7909 \times 10^{10}$ m
* $e = 0.2056$
* $GM_\odot = 1.32712 \times 10^{20}$ m$^3$/s$^2$
* $c = 2.99792458 \times 10^8$ m/s

First, calculate $\sqrt{1-e^2}$:
$\sqrt{1-e^2} = \sqrt{1 - (0.2056)^2} = \sqrt{1 - 0.042299} = \sqrt{0.957701} \approx 0.9786$

Now, plug the values into the equation for $\Delta\phi$:
$\Delta\phi = \frac{24\pi^2}{c^2} \frac{GM_\odot}{a} \sqrt{1-e^2} = \frac{24\pi^2}{(2.99792458 \times 10^8)^2} \frac{1.32712 \times 10^{20}}{5.7909 \times 10^{10}} (0.9786)$

$\Delta\phi = \frac{24\pi^2}{8.98755 \times 10^{16}} \frac{1.32712 \times 10^{20}}{5.7909 \times 10^{10}} (0.9786)$
$\Delta\phi = \frac{24\pi^2}{8.98755 \times 10^{16}} \times 2.2925 \times 10^9 \times 0.9786$
$\Delta\phi = \frac{24\pi^2 \times 2.2468 \times 10^9}{8.98755 \times 10^{16}} = \frac{4.715 \times 10^{10}}{8.98755 \times 10^{16}} \approx 5.24 \times 10^{-7}$ radians

To convert radians to arcseconds, we multiply by $\frac{180}{\pi} \times \frac{3600}{\pi}$:
$\Delta\phi \text{ (arcseconds)} = 5.24 \times 10^{-7} \times \frac{180}{\pi} \times \frac{3600}{\pi} \approx 5.24 \times 10^{-7} \times 57.2958 \times 3600 \approx 5.24 \times 10^{-7} \times 205786 \approx 0.1077$ arcseconds per orbit.

Therefore,
$\mathrm{advance\_arcsec\_orbit} = 0.1077$ arcseconds

**3. Conversion to arcseconds per century**

First, calculate the number of orbits per century:
$T = 87.969 \text{ d} \times \frac{1 \text{ year}}{365.25 \text{ d}} \times \frac{100 \text{ years}}{1 \text{ century}} \approx 87.969 \times \frac{100}{365.25} \approx 24.06$ orbits per century.

$\Delta\phi \text{ (arcseconds/century)} = \Delta\phi \text{ (arcseconds/orbit)} \times \text{orbits/century} = 0.1077 \times 24.06 \approx 2.59$ arcseconds per century.

Therefore,
$\mathrm{advance\_arcsec\_century} = 2.59$ arcseconds

$\mathrm{orbits\_per\_century} = 24.06$

**4. Explanation of the remainder of the observed precession**

The observed perihelion precession of Mercury is approximately 574 arcseconds per century. The first-order GR calculation only accounts for about 43 arcseconds per century. The remaining ~530 arcseconds per century are due to several factors:

*   **Relativistic effects beyond the first order:** The first-order GR calculation is an approximation. Higher-order terms in the GR expansion contribute to the precession.
*   **Post-Newtonian approximation:** The Schwarzschild metric is a simplified model of spacetime around a massive object. A more accurate model, incorporating post-Newtonian corrections, would provide a better estimate.
*   **Influence of other planets:** The gravitational perturbations from other planets in the solar system (particularly Jupiter and Venus) significantly contribute to the observed precession. These perturbations are not accounted for in the simple two-body GR calculation.
*   **General Relativistic effects beyond the Schwarzschild metric:** The Schwarzschild metric assumes a spherically symmetric, non-rotating mass distribution. The Sun is not perfectly spherically symmetric, and its rotation introduces additional relativistic effects.

Therefore, only the ~43 arcseconds per century derived from the first-order GR calculation can be considered a direct test of general relativity, as it isolates the effect of spacetime curvature due to the Sun's mass. The rest is due to Newtonian gravitational interactions and other relativistic effects.

FINAL ANSWER
\[
\begin{aligned}
\mathrm{advance\_arcsec\_orbit} &= 0.1077 \\
\mathrm{advance\_arcsec\_century} &= 2.59 \\
\mathrm{orbits\_per\_century} &= 24.06
\end{aligned}
\]