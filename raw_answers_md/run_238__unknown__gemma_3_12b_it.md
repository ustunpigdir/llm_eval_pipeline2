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
$\sqrt{1 - e^2} = \sqrt{1 - (0.2056)^2} = \sqrt{1 - 0.042299} = \sqrt{0.957701} \approx 0.9786$

Now, plug the values into the equation for $\Delta\phi$:
$\Delta\phi = \frac{24\pi^2}{c^2} \frac{GM_\odot}{a} \sqrt{1-e^2} = \frac{24\pi^2}{(2.99792458 \times 10^8)^2} \frac{1.32712 \times 10^{20}}{5.7909 \times 10^{10}} (0.9786)$

$\Delta\phi = \frac{24\pi^2}{8.98755 \times 10^{16}} \frac{1.32712 \times 10^{20}}{5.7909 \times 10^{10}} (0.9786)$
$\Delta\phi = \frac{24\pi^2}{8.98755 \times 10^{16}} \times 2.2925 \times 10^9 \times 0.9786$
$\Delta\phi = \frac{24\pi^2 \times 2.2548 \times 10^9}{8.98755 \times 10^{16}} = \frac{5.332 \times 10^9}{8.98755 \times 10^{16}} \approx 5.935 \times 10^{-8}$ radians

To convert radians to arcseconds, we use the conversion factor: 1 radian = $\frac{180}{\pi}$ arcseconds.
$\Delta\phi \text{ (arcseconds/orbit)} = 5.935 \times 10^{-8} \times \frac{180}{\pi} \approx 5.935 \times 10^{-8} \times 57.2958 \approx 3.408 \times 10^{-6}$ arcseconds/orbit

So, $\mathrm{advance\_arcsec\_orbit} \approx 3.408 \times 10^{-6}$ arcseconds/orbit.

**3. Conversion to arcseconds per century**

First, we need to find the number of orbits per century.
Orbital period $T = 87.969$ days.
1 century = 36525 days.
Orbits per century = $\frac{36525}{87.969} \approx 416.00$ orbits/century

$\Delta\phi \text{ (arcseconds/century)} = \Delta\phi \text{ (arcseconds/orbit)} \times \text{orbits/century} = 3.408 \times 10^{-6} \times 416 \approx 1.419 \times 10^{-3}$ arcseconds/century

So, $\mathrm{advance\_arcsec\_century} \approx 1.419 \times 10^{-3}$ arcseconds/century.

**4. Explanation of the remainder and the GR test**

The observed perihelion precession of Mercury is about 574 arcseconds per century. Our calculation using the first-order Schwarzschild result yields only about 1.4 arcseconds per century. The vast majority of the observed precession (approximately 572.6 arcseconds/century) is due to Newtonian perturbations from the other planets in the solar system.

The ~43 arcseconds/century that was initially attributed to GR is now understood to be primarily due to the effects of general relativity, but also includes a small contribution from the solar oblateness (the Sun not being a perfect sphere). The first-order Schwarzschild result captures only a portion of the GR effect. Higher-order terms in the GR expansion, as well as the effects of solar oblateness, are needed to account for the full observed precession.  The first-order result is a good approximation, but it is not sufficient to explain the full observed value.

$\mathrm{orbits\_per\_century} = 416$

\[
\begin{aligned}
\mathrm{advance\_arcsec\_orbit} &= 3.408 \times 10^{-6} \\
\mathrm{advance\_arcsec\_century} &= 1.419 \times 10^{-3} \\
\mathrm{orbits\_per\_century} &= 416
\end{aligned}
\]