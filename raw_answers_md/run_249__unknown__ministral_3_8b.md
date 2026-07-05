### Derivation of the General-Relativistic Perihelion Precession

We start with the first-order Schwarzschild metric result for the perihelion precession of a test particle in a circular orbit (later generalized to eccentric orbits). The key result for the advance of the perihelion angle \(\Delta\phi\) per orbit is derived from the geodesic equation in the Schwarzschild metric.

---

#### **1. Closed-form expression for \(\Delta\phi\) per orbit**

The general-relativistic correction to the orbital angular momentum and the resulting perihelion advance per orbit is given by:

\[
\Delta\phi = \frac{6\pi GM_\odot}{c^2 a(1-e^2)}
\]

where:
- \(G\) is the gravitational constant,
- \(M_\odot\) is the mass of the Sun,
- \(c\) is the speed of light,
- \(a\) is the semi-major axis,
- \(e\) is the orbital eccentricity.

This formula is derived from the first-order post-Newtonian (1PN) correction to the orbital motion in the Schwarzschild metric. The eccentricity factor \((1-e^2)\) arises because the perihelion advance depends on the orbital geometry and the shape of the orbit.

---

#### **2. Evaluate \(\Delta\phi\) in arcseconds per orbit**

First, we need to compute \(\Delta\phi\) in radians per orbit and then convert it to arcseconds.

Given:
- \(GM_\odot = 1.32712 \times 10^{20} \, \text{m}^3/\text{s}^2\),
- \(a = 5.7909 \times 10^{10} \, \text{m}\),
- \(e = 0.2056\),
- \(c = 2.99792 \times 10^8 \, \text{m/s}\).

Plugging in the values:

\[
\Delta\phi = \frac{6\pi \times 1.32712 \times 10^{20}}{(2.99792 \times 10^8)^2 \times 5.7909 \times 10^{10} \times (1 - 0.2056^2)}
\]

First, compute the denominator:

\[
(2.99792 \times 10^8)^2 = 8.98755 \times 10^{16} \, \text{m}^2/\text{s}^2
\]

\[
1 - e^2 = 1 - 0.2056^2 = 1 - 0.042273 = 0.957727
\]

Now, compute the denominator:

\[
8.98755 \times 10^{16} \times 5.7909 \times 10^{10} \times 0.957727 = 8.98755 \times 5.7909 \times 0.957727 \times 10^{27}
\]

\[
8.98755 \times 5.7909 \approx 52.03
\]

\[
52.03 \times 0.957727 \approx 49.97
\]

So,

\[
\text{denominator} \approx 49.97 \times 10^{27} = 4.997 \times 10^{28}
\]

Now, numerator:

\[
6\pi \times 1.32712 \times 10^{20} \approx 6 \times 3.1416 \times 1.32712 \times 10^{20} = 1.979 \times 10^{21}
\]

Thus,

\[
\Delta\phi \approx \frac{1.979 \times 10^{21}}{4.997 \times 10^{28}} = 3.96 \times 10^{-8} \, \text{radians per orbit}
\]

Now, convert radians to arcseconds:

\[
1 \, \text{radian} = \frac{180 \times 3600}{\pi} \, \text{arcseconds} \approx 206265 \, \text{arcseconds}
\]

So,

\[
\Delta\phi \approx 3.96 \times 10^{-8} \times 206265 \approx 0.00817 \, \text{arcseconds per orbit}
\]

This seems too small, so let's recheck the calculation more carefully.

---

#### **Recomputing \(\Delta\phi\) more carefully:**

\[
\Delta\phi = \frac{6\pi GM_\odot}{c^2 a (1-e^2)}
\]

Compute \(c^2\):

\[
c^2 = (2.99792 \times 10^8)^2 = 8.98755 \times 10^{16}
\]

Compute \(a(1-e^2)\):

\[
a(1-e^2) = 5.7909 \times 10^{10} \times 0.957727 = 5.533 \times 10^{10}
\]

Now,

\[
\Delta\phi = \frac{6\pi \times 1.32712 \times 10^{20}}{8.98755 \times 10^{16} \times 5.533 \times 10^{10}}
\]

\[
= \frac{6\pi \times 1.32712}{8.98755 \times 5.533} \times 10^{20 - 16 - 10} = \frac{6\pi \times 1.32712}{49.97} \times 10^{-6}
\]

\[
= \frac{25.33}{49.97} \times 10^{-6} \approx 0.507 \times 10^{-6} = 5.07 \times 10^{-7} \, \text{radians per orbit}
\]

Now, convert to arcseconds:

\[
5.07 \times 10^{-7} \times 206265 \approx 0.1047 \, \text{arcseconds per orbit}
\]

This is more reasonable. The earlier mistake was in the order of magnitude of the denominator.

---

#### **3. Convert to arcseconds per century**

First, compute the number of orbits per century.

Given:
- Orbital period \(T = 87.969 \, \text{days}\),
- 1 century = 36525 days.

Number of orbits per century:

\[
\text{orbits per century} = \frac{36525}{87.969} \approx 415.2
\]

Now, multiply the perihelion advance per orbit by the number of orbits per century:

\[
\Delta\phi_{\text{century}} = 0.1047 \, \text{arcsec/orbit} \times 415.2 \approx 43.5 \, \text{arcseconds per century}
\]

---

#### **4. Explanation of the remainder in the observed precession**

The full observed precession of Mercury's perihelion is about \(574''/\text{century}\). The general-relativistic contribution accounts for approximately \(43''/\text{century}\). The remainder (\(574'' - 43'' = 531''\)) is due to:

1. **Planetary perturbations**: The gravitational influence of other planets (Venus, Earth, Jupiter, etc.) causes perturbations in Mercury's orbit, contributing significantly to the observed precession. These perturbations are calculated using Newtonian mechanics and account for most of the remaining precession.

2. **Astronomical conventions and observational uncertainties**: Small corrections due to the definition of the solar system's coordinate system, the shape of the Sun, and other minor effects contribute to the remaining discrepancy.

3. **Higher-order relativistic corrections**: While the first-order Schwarzschild result is dominant, higher-order post-Newtonian corrections (e.g., from the Lense-Thirring effect or frame-dragging) are negligible for Mercury's orbit.

The GR test is only the \(43''\) because the rest is dominated by classical (Newtonian) planetary perturbations, which are well understood and accounted for separately. The GR prediction is a small but crucial confirmation of Einstein's theory, as it matches the residual precession not explained by classical mechanics.

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{advance\_arcsec\_orbit} &= 0.1047 \\
\mathrm{advance\_arcsec\_century} &= 43.5 \\
\mathrm{orbits\_per\_century} &= 415.2
\end{aligned}
\]