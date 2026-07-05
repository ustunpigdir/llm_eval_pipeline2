Okay, let's break down the calculation of Mercury's perihelion precession using the first-order Schwarzschild result.

**1. GR Perihelion Advance per Orbit ($\Delta\phi$)**

The first-order GR perihelion advance per orbit is given by:

$\Delta\phi = \frac{24\pi^2}{c^2} \frac{GM_\odot a (1 - e^2)^{1/2}}{a^2\sqrt{1 - e^2}} e^2$

where:
* $G$ is the gravitational constant
* $M_\odot$ is the mass of the Sun
* $a$ is the semi-major axis
* $e$ is the eccentricity
* $c$ is the speed of light

We are given $GM_\odot$, $a$, $e$, and we know $c = 2.99792458 \times 10^8$ m/s.

**2. Evaluate $\Delta\phi$ in arcseconds per orbit**

First, let's calculate the value inside the parentheses:

$\frac{GM_\odot a (1 - e^2)^{1/2}}{a^2\sqrt{1 - e^2}} e^2 = \frac{(1.32712\times 10^{20} \text{ m}^3/\text{s}^2)(5.7909\times 10^{10} \text{ m}) (1 - 0.2056^2)^{1/2}}{(5.7909\times 10^{10} \text{ m})^2 \sqrt{1 - 0.2056^2}} (0.2056)^2$

$1 - e^2 = 1 - 0.2056^2 = 1 - 0.04229856 = 0.95770144$
$(1 - e^2)^{1/2} = \sqrt{0.95770144} \approx 0.978665$
$\sqrt{1 - e^2} = \sqrt{0.95770144} \approx 0.978665$

So, the term becomes:
$\frac{(1.32712\times 10^{20})(5.7909\times 10^{10})(0.978665)}{(5.7909\times 10^{10})^2 (0.978665)} (0.2056)^2 = \frac{(1.32712\times 10^{20})(5.7909\times 10^{10})(0.978665)}{(3.35 \times 10^{21})(0.978665)} (0.04229856) = \frac{7.553 \times 10^{30}}{3.268 \times 10^{21}} (0.04229856) = 23.12 \times 10^8 (0.04229856) = 9.77 \times 10^6$

Now, we can calculate $\Delta\phi$:

$\Delta\phi = \frac{24\pi^2}{c^2} (9.77 \times 10^6) = \frac{24\pi^2}{(2.99792458 \times 10^8)^2} (9.77 \times 10^6) = \frac{24\pi^2}{8.98755 \times 10^{16}} (9.77 \times 10^6) = \frac{2375.9}{8.98755 \times 10^{16}} (9.77 \times 10^6) = 2.64 \times 10^{-14} (9.77 \times 10^6) = 2.58 \times 10^{-7}$ radians

To convert to arcseconds, we multiply by $\frac{180}{\pi} \frac{3600}{\pi}$:

$\Delta\phi \text{ (arcseconds/orbit)} = 2.58 \times 10^{-7} \times \frac{180}{\pi} \times \frac{3600}{\pi} \approx 2.58 \times 10^{-7} \times 57.2958 \times 114.592 \approx 2.58 \times 10^{-7} \times 6550 \approx 0.00168$ arcseconds/orbit.
Let's recalculate:
$\Delta\phi = \frac{24\pi^2}{c^2} \frac{GM_\odot a (1 - e^2)^{1/2}}{a^2\sqrt{1 - e^2}} e^2 = \frac{24\pi^2}{c^2} \frac{GM_\odot a}{a^2} (1-e^2)^{-1} e^2 = \frac{24\pi^2}{c^2} \frac{GM_\odot}{a} \frac{e^2}{1-e^2}$
$\Delta\phi = \frac{24\pi^2}{(2.99792458 \times 10^8)^2} \frac{(1.32712\times 10^{20})}{(5.7909\times 10^{10})} \frac{(0.2056)^2}{1-0.2056^2} = \frac{24\pi^2}{8.98755 \times 10^{16}} \frac{1.32712\times 10^{20}}{5.7909\times 10^{10}} \frac{0.04229856}{0.95770144} = \frac{2375.9}{8.98755 \times 10^{16}} (2.29 \times 10^9) (0.04425) = 2.64 \times 10^{-14} (2.29 \times 10^9) (0.04425) = 2.64 \times 10^{-14} (1.01 \times 10^8) = 2.66 \times 10^{-6}$ radians.
$\Delta\phi \text{ (arcseconds/orbit)} = 2.66 \times 10^{-6} \times \frac{180}{\pi} \times \frac{3600}{\pi} \approx 2.66 \times 10^{-6} \times 57.2958 \times 114.592 \approx 2.66 \times 10^{-6} \times 6550 \approx 0.0173$ arcseconds/orbit.

**3. Convert to arcseconds per century**

Number of orbits per century:
$87.969 \text{ d/orbit} \times 365.25 \text{ d/year} \times 100 \text{ years/century} = 31557.5 \text{ orbits/century}$

$\Delta\phi \text{ (arcseconds/century)} = 0.0173 \text{ arcseconds/orbit} \times 31557.5 \text{ orbits/century} \approx 545.5$ arcseconds/century.

**4. Explanation of the Remainder**

The observed precession is about 574 arcseconds per century. Our calculation using the first-order GR result gives approximately 545 arcseconds per century. The difference (approximately 29 arcseconds per century) is due to several factors:

*   **Higher-order GR terms:** The first-order result is an approximation. Higher-order terms in the GR expansion contribute to the precession.
*   **Relativistic effects of other planets:** The gravitational influence of other planets in the solar system (particularly Jupiter and Venus) perturbs Mercury's orbit.
*   **Solar oblateness:** The Sun is not a perfect sphere; it is slightly flattened at the poles. This oblateness introduces additional precession.
*   **Post-Newtonian approximation:** The first-order GR result is derived using the post-Newtonian approximation, which is valid for weak gravitational fields.

Only the ~43 arcseconds per century is considered a direct test of GR because it is the portion of the precession that cannot be explained by Newtonian mechanics and the effects of other planets. The remaining precession is due to the combined effects of higher-order GR terms and solar oblateness.

\[
\begin{aligned}
\mathrm{advance\_arcsec\_orbit} &= 0.0173 \\
\mathrm{advance\_arcsec\_century} &= 545.5 \\
\mathrm{orbits\_per\_century} &= 31557.5
\end{aligned}
\]