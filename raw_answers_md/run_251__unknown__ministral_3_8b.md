### Derivation of the General-Relativistic Perihelion Advance

#### 1. Closed-form expression for the GR perihelion advance per orbit \(\Delta\phi\)

In the Schwarzschild metric, the first-order post-Newtonian correction to the orbital angular momentum leads to a precession of the perihelion. The standard result for the advance of the perihelion per orbit \(\Delta\phi\) for a bound orbit is given by:

\[
\Delta\phi = \frac{6\pi GM_\odot}{c^2 a (1 - e^2)}
\]

where:
- \(GM_\odot\) is the standard gravitational parameter of the Sun,
- \(a\) is the semi-major axis,
- \(e\) is the eccentricity,
- \(c\) is the speed of light.

This formula accounts for the first-order correction in the weak-field limit (\(v^2/c^2 \ll 1\)) and is derived from the effective potential in general relativity.

---

#### 2. Evaluate \(\Delta\phi\) in arcseconds per orbit

First, we need the numerical values of the constants and parameters:

- \(GM_\odot = 1.32712 \times 10^{20} \, \text{m}^3/\text{s}^2\),
- \(a = 5.7909 \times 10^{10} \, \text{m}\),
- \(e = 0.2056\),
- \(c = 2.99792458 \times 10^8 \, \text{m/s}\).

Plugging these into the formula:

\[
\Delta\phi = \frac{6\pi \times 1.32712 \times 10^{20}}{c^2 a (1 - e^2)}
\]

First, compute the denominator:

\[
c^2 = (2.99792458 \times 10^8)^2 \approx 8.98755 \times 10^{16} \, \text{m}^2/\text{s}^2
\]

\[
a (1 - e^2) = 5.7909 \times 10^{10} \times (1 - 0.2056^2)
\]

Calculate \(e^2\):

\[
e^2 = 0.2056^2 \approx 0.04227
\]

\[
1 - e^2 = 1 - 0.04227 = 0.95773
\]

\[
a (1 - e^2) = 5.7909 \times 10^{10} \times 0.95773 \approx 5.545 \times 10^{10} \, \text{m}
\]

Now compute the denominator:

\[
c^2 a (1 - e^2) = 8.98755 \times 10^{16} \times 5.545 \times 10^{10} \approx 4.987 \times 10^{27} \, \text{m}^3/\text{s}^2
\]

Now compute the numerator:

\[
6\pi \times 1.32712 \times 10^{20} \approx 6 \times 3.14159 \times 1.32712 \times 10^{20} \approx 2.499 \times 10^{21} \, \text{m}^3/\text{s}^2
\]

Now divide:

\[
\Delta\phi = \frac{2.499 \times 10^{21}}{4.987 \times 10^{27}} \approx 5.01 \times 10^{-7} \, \text{radians}
\]

Convert radians to arcseconds (1 radian = 206265 arcseconds):

\[
\Delta\phi \approx 5.01 \times 10^{-7} \times 206265 \approx 0.1033 \, \text{arcseconds per orbit}
\]

---

#### 3. Convert to arcseconds per century

First, compute the number of orbits per century.

The orbital period \(T\) is given as 87.969 days. Convert this to seconds:

\[
T = 87.969 \, \text{days} \times 24 \, \text{hours/day} \times 3600 \, \text{seconds/hour} \approx 7.629 \times 10^6 \, \text{seconds}
\]

One century is 36525 days:

\[
\text{century in seconds} = 36525 \times 24 \times 3600 \approx 3.15576 \times 10^9 \, \text{seconds}
\]

Number of orbits per century:

\[
\text{orbits per century} = \frac{3.15576 \times 10^9}{7.629 \times 10^6} \approx 413.7
\]

Now multiply the advance per orbit by the number of orbits per century:

\[
\Delta\phi_{\text{century}} = 0.1033 \, \text{arcseconds/orbit} \times 413.7 \approx 42.8 \, \text{arcseconds/century}
\]

---

#### 4. Explanation of the remainder in the observed precession

The full observed precession of Mercury's perihelion is about 574 arcseconds per century. The general-relativistic contribution accounts for approximately 43 arcseconds per century. The remainder (~531 arcseconds) is primarily due to:

- **Planetary perturbations**: The gravitational influence of other planets (Venus, Earth, Jupiter, etc.) causes perturbations in Mercury's orbit that contribute significantly to the observed precession.
- **Non-spherical shape of the Sun**: The Sun is not a perfect sphere; its oblateness and other non-spherical features also contribute to the precession.
- **Other relativistic effects**: While the Schwarzschild metric accounts for the leading-order post-Newtonian correction, higher-order corrections and frame-dragging effects (Lense-Thirring effect) are negligible for Mercury's orbit.

The GR test is only for the ~43 arcseconds because this is the part of the precession that arises purely from the curvature of spacetime around the Sun, as predicted by general relativity. The rest is due to classical (Newtonian) perturbations and other effects.

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{advance\_arcsec\_orbit} &= 0.1033 \\
\mathrm{advance\_arcsec\_century} &= 42.8 \\
\mathrm{orbits\_per\_century} &= 413.7
\end{aligned}
\]