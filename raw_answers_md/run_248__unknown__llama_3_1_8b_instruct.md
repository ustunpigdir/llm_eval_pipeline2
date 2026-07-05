## Step 1: State the GR perihelion advance per orbit in closed form
The first-order GR result for the perihelion advance per orbit is given by:

$$\Delta\phi = \frac{6\pi GM_\odot}{c^2a(1-e^2)}$$

where $GM_\odot$ is the gravitational constant times the mass of the Sun, $a$ is the semi-major axis, $e$ is the eccentricity, and $c$ is the speed of light.

## Step 2: Evaluate $\Delta\phi$ in arcseconds per orbit
To evaluate $\Delta\phi$ in arcseconds per orbit, we need to plug in the given values:

$$\Delta\phi = \frac{6\pi (1.32712\times 10^{20}\,\mathrm{m}^3/\mathrm{s}^2)}{(3\times 10^8\,\mathrm{m}/\mathrm{s})^2(5.7909\times 10^{10}\,\mathrm{m})(1-0.2056^2)}$$

$$\Delta\phi = \frac{6\pi (1.32712\times 10^{20})}{(9\times 10^{16})(5.7909\times 10^{10})(0.9604)}$$

$$\Delta\phi = \frac{6\pi (1.32712\times 10^{20})}{(5.273\times 10^{27})}$$

$$\Delta\phi = 3.083\times 10^{-7}\,\mathrm{rad}$$

To convert this to arcseconds, we use the conversion factor $1\,\mathrm{rad} = 206265''$:

$$\Delta\phi = 3.083\times 10^{-7}\,\mathrm{rad} \times 206265''/\mathrm{rad} = 6.37''$$

## Step 3: Convert to arcseconds per century
To convert the perihelion advance per orbit to arcseconds per century, we need to divide by the number of orbits per century. The orbital period of Mercury is $87.969$ days, so the number of orbits per century is:

$$\mathrm{orbits\_per\_century} = \frac{36525\,\mathrm{d}}{87.969\,\mathrm{d}} = 415.17$$

The perihelion advance per century is then:

$$\mathrm{advance\_arcsec\_century} = \frac{\mathrm{advance\_arcsec\_orbit}}{\mathrm{orbits\_per\_century}} = \frac{6.37''}{415.17} = 0.0153''$$

## Step 4: Explain what accounts for the remainder
The full observed precession is about $574''$/century, which is much larger than the GR prediction of $0.0153''$. This suggests that there are other effects contributing to the precession, such as the effects of the other planets in the solar system.

## Step 5: Explain why only the ~43'' is the GR test
The GR prediction of $0.0153''$ is much smaller than the observed precession, so it is not a significant contributor to the total precession. However, the fact that the GR prediction is consistent with the observed precession is still a test of GR, and the $0.0153''$ is the GR contribution to the total precession.

## FINAL ANSWER

\[
\begin{aligned}
\mathrm{advance\_arcsec\_orbit} &= 6.37'' \\
\mathrm{advance\_arcsec\_century} &= 0.0153'' \\
\mathrm{orbits\_per\_century} &= 415.17
\end{aligned}
\]