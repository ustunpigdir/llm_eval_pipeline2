**1. Derivation of GR perihelion advance per orbit**

The Schwarzschild metric for a spherically symmetric, non-rotating mass is given by:

\[ds^2 = -\left(1 - \frac{2GM_\odot}{rc^2}\right)c^2dt^2 + \left(1 - \frac{2GM_\odot}{rc^2}\right)^{-1}dr^2 + r^2d\Omega^2\]

For a test particle in an elliptical orbit, the orbit is described by:

\[r = \frac{a(1-e^2)}{1+e\cos\theta}\]

where $a$ is the semi-major axis, $e$ is the eccentricity, and $\theta$ is the eccentric anomaly. The orbital period $P$ is given by:

\[P = 2\pi a^{3/2}\sqrt{\frac{1}{GM_\odot}}\]

The perihelion advance per orbit $\Delta\phi$ is given by the difference between the relativistic and Newtonian orbital periods:

\[\Delta\phi = \frac{P_{\text{GR}} - P_{\text{Newton}}}{2\pi}\]

Using the first-order post-Newtonian approximation, the relativistic orbital period is:

\[P_{\text{GR}} = P_{\text{Newton}} + \frac{6\pi GM_\odot}{c^2a(1-e^2)}\]

Substituting and simplifying, we get:

\[\Delta\phi = \frac{6\pi GM_\odot}{c^2a(1-e^2)}\]

**2. GR perihelion advance per orbit in arcseconds**

Converting to arcseconds:

\[\Delta\phi = \frac{6\pi GM_\odot}{c^2a(1-e^2)} \times \frac{180}{\pi} \times \frac{1}{3600} \text{ arcsec}\]

Substituting the given values:

\[a = 5.7909\times 10^{10} \text{ m}, \quad e = 0.2056, \quad GM_\odot = 1.32712\times 10^{20} \text{ m}^3/\text{s}^2, \quad c = 2.9979\times 10^8 \text{ m/s}\]

\[\Delta\phi = \frac{6\pi \times 1.32712\times 10^{20} \text{ m}^3/\text{s}^2}{2.9979\times 10^8 \text{ m/s}^2 \times 5.7909\times 10^{10} \text{ m} \times (1-0.2056^2)} \times \frac{180}{\pi} \times \frac{1}{3600} \text{ arcsec}\]

\[\Delta\phi \approx 42.98 \text{ arcsec/orbit}\]

**3. GR perihelion advance per century**

Mercury's orbital period is 87.969 days, so the number of orbits per century is:

\[N = \frac{36525 \text{ days/century}}{87.969 \text{ days/orbit}} \approx 415.7 \text{ orbits/century}\]

Thus, the advance per century is:

\[\Delta\phi_{\text{century}} = \Delta\phi \times N \approx 42.98 \times 415.7 \text{ arcsec/century}\]

\[\Delta\phi_{\text{century}} \approx 17656.6 \text{ arcsec/century}\]

**4. Remaining precession**

The observed precession is about $574''$/century. The remaining precession is due to other effects not included in the first-order GR calculation, such as:

- **Second-order GR effects**: These are much smaller than the first-order effects and are typically neglected.
- **Planetary perturbations**: Other planets in the solar system can cause a small amount of precession.
- **General relativity with a spinning mass**: The Sun is not a static, spherically symmetric mass. Its rotation can cause a small amount of precession.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{advance\_arcsec\_orbit} &= 42.98 \text{ arcsec/orbit} \\
\mathrm{advance\_arcsec\_century} &= 17656.6 \text{ arcsec/century} \\
\mathrm{orbits\_per\_century} &= 415.7 \text{ orbits/century}
\end{aligned}
\]