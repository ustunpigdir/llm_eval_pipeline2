### Derivation of the General-Relativistic Perihelion Advance

We start with the first-order Schwarzschild metric result for the perihelion advance of a test particle in a weak gravitational field. The classical Keplerian orbit is perturbed by the relativistic correction, leading to an additional advance of the perihelion angle per orbit given by:

\[
\Delta\phi = \frac{6\pi GM_\odot}{c^2 a (1 - e^2)}
\]

where:
- \( G \) is the gravitational constant,
- \( M_\odot \) is the mass of the Sun,
- \( c \) is the speed of light,
- \( a \) is the semi-major axis,
- \( e \) is the eccentricity.

This formula is derived from the post-Newtonian approximation of the Schwarzschild metric, where the leading-order correction to the orbital motion is proportional to \( \frac{GM_\odot}{c^2 a} \). The factor of \( 6\pi \) arises from integrating the relativistic correction over one orbit, and the denominator includes the eccentricity factor \( (1 - e^2) \) to account for the shape of the orbit.

---

### Step 1: State the GR perihelion advance per orbit \(\Delta\phi\) in closed form

The closed-form expression for the GR perihelion advance per orbit is:

\[
\Delta\phi = \frac{6\pi GM_\odot}{c^2 a (1 - e^2)}
\]

---

### Step 2: Evaluate \(\Delta\phi\) in arcseconds per orbit

First, we need the numerical values of the constants and given parameters:

- \( GM_\odot = 1.32712 \times 10^{20} \, \text{m}^3/\text{s}^2 \)
- \( a = 5.7909 \times 10^{10} \, \text{m} \)
- \( e = 0.2056 \)
- \( c = 2.99792458 \times 10^8 \, \text{m/s} \)

Compute the denominator \( a(1 - e^2) \):

\[
1 - e^2 = 1 - (0.2056)^2 = 1 - 0.04227936 = 0.95772064
\]

\[
a(1 - e^2) = 5.7909 \times 10^{10} \times 0.95772064 = 5.537 \times 10^{10} \, \text{m}
\]

Now compute the numerator \( 6\pi GM_\odot / c^2 \):

\[
c^2 = (2.99792458 \times 10^8)^2 = 8.98755179 \times 10^{16} \, \text{m}^2/\text{s}^2
\]

\[
\frac{GM_\odot}{c^2} = \frac{1.32712 \times 10^{20}}{8.98755179 \times 10^{16}} = 1.477 \times 10^{-4} \, \text{m}
\]

\[
6\pi \times 1.477 \times 10^{-4} = 6 \times 3.1416 \times 1.477 \times 10^{-4} = 2.763 \times 10^{-3} \, \text{m}
\]

Now divide by \( a(1 - e^2) \):

\[
\Delta\phi = \frac{2.763 \times 10^{-3}}{5.537 \times 10^{10}} = 4.99 \times 10^{-14} \, \text{radians}
\]

Convert radians to arcseconds (1 radian = \( 206265 \) arcseconds):

\[
\Delta\phi = 4.99 \times 10^{-14} \times 206265 = 1.03 \times 10^{-8} \, \text{arcseconds}
\]

Wait, this seems too small! There must be a mistake in the calculation. Let's re-examine the numerator calculation.

The correct approach is to compute \( \frac{6\pi GM_\odot}{c^2 a (1 - e^2)} \) directly:

\[
\frac{6\pi GM_\odot}{c^2 a (1 - e^2)} = \frac{6\pi \times 1.32712 \times 10^{20}}{(8.98755179 \times 10^{16}) \times 5.537 \times 10^{10}}
\]

Calculate denominator:

\[
(8.98755179 \times 10^{16}) \times 5.537 \times 10^{10} = 4.977 \times 10^{27}
\]

Numerator:

\[
6\pi \times 1.32712 \times 10^{20} = 2.506 \times 10^{21}
\]

Now divide:

\[
\frac{2.506 \times 10^{21}}{4.977 \times 10^{27}} = 5.03 \times 10^{-7} \, \text{radians}
\]

Convert to arcseconds:

\[
5.03 \times 10^{-7} \times 206265 = 0.1037 \, \text{arcseconds per orbit}
\]

This is more reasonable.

---

### Step 3: Convert to arcseconds per century

First, compute the number of orbits per century.

Given:
- Orbital period \( T = 87.969 \, \text{days} \)
- 1 century = 36525 days

Number of orbits per century:

\[
\text{orbits per century} = \frac{36525}{87.969} = 415.2
\]

Now multiply the advance per orbit by the number of orbits per century:

\[
\Delta\phi_{\text{century}} = 0.1037 \times 415.2 = 43.1 \, \text{arcseconds per century}
\]

---

### Step 4: Explain the remainder in the observed precession

The full observed precession of Mercury's perihelion is about \( 574''/\text{century} \). The GR prediction accounts for approximately \( 43''/\text{century} \). The remainder comes from:

1. **Classical (Newtonian) perturbations**: The gravitational influence of other planets (Venus, Earth, Jupiter, etc.) causes small perturbations in Mercury's orbit that accumulate over time. These perturbations are not accounted for in the simple test-particle GR calculation.

2. **Relativistic effects beyond the Schwarzschild metric**: The Schwarzschild metric assumes a spherically symmetric, non-rotating Sun. The Sun is actually an oblate spheroid (due to rotation) and has a quadrupole moment, which introduces additional relativistic corrections (e.g., frame-dragging and the Lense-Thirring effect). These effects are small but contribute to the total precession.

3. **Other relativistic effects**: Higher-order post-Newtonian corrections (e.g., terms involving \( \frac{GM_\odot}{c^2} \) squared) could contribute, though they are typically negligible for Mercury.

The GR test is only for the part of the precession that arises from the curvature of spacetime due to the Sun's mass, which is the \( 43''/\text{century} \) component. The rest is due to classical and other relativistic effects.

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{advance\_arcsec\_orbit} &= 0.1037 \\
\mathrm{advance\_arcsec\_century} &= 43.1 \\
\mathrm{orbits\_per\_century} &= 415.2
\end{aligned}
\]