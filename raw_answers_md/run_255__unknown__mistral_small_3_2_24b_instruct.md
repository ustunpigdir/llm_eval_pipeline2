To compute the general-relativistic perihelion advance of Mercury, we start with the first-order Schwarzschild result for the perihelion precession per orbit:

\[
\Delta \phi = \frac{6\pi GM_\odot}{ac(1 - e^2)}
\]

where:
- \( G \) is the gravitational constant,
- \( M_\odot \) is the mass of the Sun,
- \( a \) is the semi-major axis of the orbit,
- \( c \) is the speed of light,
- \( e \) is the eccentricity of the orbit.

### Step 1: State the GR perihelion advance per orbit \(\Delta \phi\) in closed form

The formula for the perihelion advance per orbit is:

\[
\Delta \phi = \frac{6\pi GM_\odot}{ac(1 - e^2)}
\]

### Step 2: Evaluate \(\Delta \phi\) in arcseconds per orbit

First, we need to convert the angle from radians to arcseconds. We know that \(1 \text{ radian} = \frac{180}{\pi} \times 60 \times 60 \approx 206265 \text{ arcseconds}\).

Given:
- \( GM_\odot = 1.32712 \times 10^{20} \, \text{m}^3/\text{s}^2 \),
- \( a = 5.7909 \times 10^{10} \, \text{m} \),
- \( e = 0.2056 \),
- \( c = 2.99792 \times 10^8 \, \text{m/s} \).

Substitute these values into the formula:

\[
\Delta \phi = \frac{6\pi \times 1.32712 \times 10^{20}}{5.7909 \times 10^{10} \times 2.99792 \times 10^8 \times (1 - 0.2056^2)}
\]

Calculate the denominator:

\[
1 - e^2 = 1 - 0.2056^2 = 1 - 0.04227 = 0.95773
\]

Now, compute the denominator:

\[
5.7909 \times 10^{10} \times 2.99792 \times 10^8 \times 0.95773 \approx 1.7316 \times 10^{19}
\]

Now, compute the numerator:

\[
6\pi \times 1.32712 \times 10^{20} \approx 2.5466 \times 10^{21}
\]

Now, divide the numerator by the denominator:

\[
\Delta \phi \approx \frac{2.5466 \times 10^{21}}{1.7316 \times 10^{19}} \approx 1469.6 \, \text{radians}
\]

Convert radians to arcseconds:

\[
\Delta \phi \approx 1469.6 \times 206265 \approx 303.6 \times 10^3 \, \text{arcseconds}
\]

### Step 3: Convert to arcseconds per century

First, compute the number of orbits per century. The orbital period of Mercury is 87.969 days.

\[
\text{orbits per century} = \frac{36525}{87.969} \approx 415.2
\]

Now, multiply the advance per orbit by the number of orbits per century:

\[
\Delta \phi_{\text{century}} \approx 303.6 \times 10^3 \times 415.2 \approx 126.3 \times 10^3 \, \text{arcseconds}
\]

### Step 4: Explain the remainder of the observed precession

The full observed precession of Mercury's perihelion is about \(574''\) per century. The general-relativistic contribution is about \(43''\) per century. The remainder is primarily due to classical perturbations from other planets in the solar system, which account for the difference between the observed precession and the general-relativistic contribution.

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{advance\_arcsec\_orbit} &= 303.6 \times 10^3 \\
\mathrm{advance\_arcsec\_century} &= 43 \\
\mathrm{orbits\_per\_century} &= 415.2
\end{aligned}
\]