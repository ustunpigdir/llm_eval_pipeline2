### 1. Derivation and Closed Form
In the Schwarzschild metric, the geodesic equation for a test particle in the equatorial plane leads to the orbital equation:
$$\frac{d^2u}{d\phi^2} + u = \frac{GM}{h^2} + \frac{3GM}{c^2}u^2$$
where $u = 1/r$ and $h$ is the specific angular momentum. In Newtonian mechanics, the term $\frac{3GM}{c^2}u^2$ is absent, resulting in closed elliptical orbits. Treating the GR term as a small perturbation, the shift in the perihelion per orbit $\Delta\phi$ is derived as:
$$\Delta\phi = \frac{6\pi GM_\odot}{c^2 a (1-e^2)}$$
where $a$ is the semi-major axis and $e$ is the eccentricity.

### 2. Numerical Evaluation per Orbit
**Constants:**
- $GM_\odot = 1.32712 \times 10^{20} \text{ m}^3/\text{s}^2$
- $c = 2.99792458 \times 10^8 \text{ m/s}$
- $a = 5.7909 \times 10^{10} \text{ m}$
- $e = 0.2056$

**Calculation:**
First, compute the Schwarzschild radius $r_s = \frac{2GM_\odot}{c^2}$:
$$r_s = \frac{2(1.32712 \times 10^{20})}{(2.99792458 \times 10^8)^2} \approx 2953.36 \text{ m}$$
Now substitute into the $\Delta\phi$ formula:
$$\Delta\phi = \frac{3\pi r_s}{a(1-e^2)} = \frac{3\pi (2953.36)}{(5.7909 \times 10^{10})(1 - 0.2056^2)}$$
$$1 - e^2 = 1 - 0.04227136 = 0.95772864$$
$$\Delta\phi = \frac{27834.45}{5.5462 \times 10^{10}} \approx 5.0186 \times 10^{-7} \text{ radians/orbit}$$
Convert radians to arcseconds ($1 \text{ rad} = \frac{180}{\pi} \times 3600 \text{ arcsec} \approx 206264.8 \text{ arcsec}$):
$$\Delta\phi_{\text{arcsec}} = 5.0186 \times 10^{-7} \times 206264.8 \approx 0.103517 \text{ arcsec/orbit}$$

### 3. Conversion to Arcseconds per Century
**Orbits per century:**
- Period $T = 87.969 \text{ d}$
- Days per century $= 36525 \text{ d}$
$$\text{Orbits/century} = \frac{36525}{87.969} \approx 415.203 \text{ orbits/century}$$
**Advance per century:**
$$\Delta\phi_{\text{century}} = 0.103517 \times 415.203 \approx 42.98 \text{ arcsec/century}$$

### 4. Explanation of the Remainder
The observed precession of Mercury is $\approx 574''/\text{century}$. The GR contribution is only $\approx 43''/\text{century}$. The remainder ($\approx 531''/\text{century}$) is caused by the gravitational perturbations from other planets in the solar system (primarily Jupiter and Venus), which can be calculated using Newtonian N-body mechanics. Because the planetary perturbations are computable within Newtonian physics, the "excess" precession that cannot be explained by other masses is the specific test for General Relativity.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{advance\_arcsec\_orbit} &= 0.1035 \\
\mathrm{advance\_arcsec\_century} &= 42.98 \\
\mathrm{orbits\_per\_century} &= 415.20
\end{aligned}
\]