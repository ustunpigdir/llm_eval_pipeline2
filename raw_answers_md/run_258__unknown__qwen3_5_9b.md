To compute the general-relativistic perihelion advance of Mercury, we use the first-order Schwarzschild metric result for a test particle orbiting a massive body.

### 1. General-Relativistic Perihelion Advance Formula

The standard first-order GR correction for the perihelion advance per orbit, $\Delta\phi$, is given by:
$$ \Delta\phi = \frac{6\pi GM}{c^2 a (1-e^2)} $$
where:
- $G$ is the gravitational constant.
- $M$ is the mass of the central body (Sun).
- $c$ is the speed of light in vacuum.
- $a$ is the semi-major axis of the orbit.
- $e$ is the orbital eccentricity.
- $p = a(1-e^2)$ is the semi-latus rectum.

### 2. Given Data and Constants

We use the following values provided in the problem statement and standard physical constants:
- $GM_\odot = 1.32712 \times 10^{20} \text{ m}^3/\text{s}^2$
- $a = 5.7909 \times 10^{10} \text{ m}$
- $e = 0.2056$
- $c = 2.99792458 \times 10^8 \text{ m/s}$ (Standard value)
- Orbital Period $T = 87.969 \text{ d}$
- 1 Century $= 36525 \text{ d}$

### 3. Calculation of Advance per Orbit

First, we calculate the term $(1-e^2)$:
$$ 1 - e^2 = 1 - (0.2056)^2 = 1 - 0.04227136 = 0.95772864 $$

Next, we calculate the semi-latus rectum $p = a(1-e^2)$:
$$ p = (5.7909 \times 10^{10} \text{ m}) \times 0.95772864 \approx 5.54622 \times 10^{10} \text{ m} $$

Now, we calculate the denominator $c^2 p$:
$$ c^2 = (2.99792458 \times 10^8 \text{ m/s})^2 \approx 8.98755 \times 10^{16} \text{ m}^2/\text{s}^2 $$
$$ c^2 p \approx (8.98755 \times 10^{16}) \times (5.54622 \times 10^{10}) \approx 4.98453 \times 10^{27} \text{ m}^3/\text{s}^2 $$

Next, we calculate the numerator $6\pi GM$:
$$ 6\pi GM \approx 6 \times 3.14159265 \times (1.32712 \times 10^{20}) \approx 2.50560 \times 10^{21} \text{ m}^3/\text{s}^2 $$

Now, we compute $\Delta\phi$ in radians:
$$ \Delta\phi_{\text{rad}} = \frac{2.50560 \times 10^{21}}{4.98453 \times 10^{27}} \approx 5.02677 \times 10^{-7} \text{ rad} $$

Convert radians to arcseconds ($1 \text{ rad} = \frac{180 \times 3600}{\pi} \text{ arcsec} \approx 206264.806 \text{ arcsec}$):
$$ \Delta\phi_{\text{arcsec}} = (5.02677 \times 10^{-7}) \times 206264.806 \approx 0.10368 \text{ arcsec} $$

Rounding to 4 significant figures (limited by eccentricity $e$):
$$ \Delta\phi_{\text{arcsec}} \approx 0.1037 \text{ arcsec} $$

### 4. Calculation of Advance per Century

First, calculate the number of orbits per century ($N$):
$$ N = \frac{36525 \text{ d}}{87.969 \text{ d}} \approx 415.203 \text{ orbits} $$

Now, calculate the total advance per century:
$$ \Delta\phi_{\text{century}} = \Delta\phi_{\text{arcsec}} \times N \approx 0.10368 \times 415.203 \approx 43.049 \text{ arcsec} $$

Rounding to 4 significant figures:
$$ \Delta\phi_{\text{century}} \approx 43.05 \text{ arcsec} $$

### 5. Explanation of the Remainder

The total observed precession of Mercury's perihelion is approximately $574''$ per century.
- **Newtonian Contribution:** Classical celestial mechanics predicts a precession of approximately $531''$ per century due to gravitational perturbations from other planets (primarily Venus, Jupiter, and Earth).
- **GR Contribution:** The remaining discrepancy is approximately $574'' - 531'' = 43''$ per century.
- **Conclusion:** The General Relativity prediction of $\approx 43''$ per century matches this discrepancy exactly. Therefore, the $\sim 43''$ is the specific test of General Relativity, while the $\sim 531''$ is accounted for by Newtonian planetary perturbations.

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{advance\_arcsec\_orbit} &= 0.1037 \\
\mathrm{advance\_arcsec\_century} &= 43.05 \\
\mathrm{orbits\_per\_century} &= 415.2
\end{aligned}
\]