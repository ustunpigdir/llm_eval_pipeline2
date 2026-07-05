**1. Derivation of GR perihelion advance per orbit**

The Schwarzschild metric for a static, spherically symmetric spacetime is given by:

\[ds^2 = -\left(1 - \frac{2GM_\odot}{rc^2}\right)c^2dt^2 + \left(1 + \frac{2GM_\odot}{rc^2}\right)dr^2 + r^2d\Omega^2\]

For a test particle in a circular orbit at radius $r$, the orbital period $T$ is given by:

\[T = \frac{2\pi r^2}{GM_\odot}\]

The angular velocity $\omega$ is:

\[\omega = \frac{2\pi}{T} = \frac{GM_\odot}{r^2}\]

The first-order GR correction to the angular velocity is:

\[\omega_{GR} = \frac{3GM_\odot}{2c^2r^3}\]

The GR perihelion advance per orbit $\Delta\phi$ is the difference between the GR angular velocity and the Newtonian angular velocity, multiplied by the orbital period:

\[\Delta\phi = \left(\omega_{GR} - \omega\right)T = \frac{3GM_\odot}{2c^2r^3} \cdot \frac{2\pi r^2}{GM_\odot} = \frac{3\pi}{2}\frac{r^2}{c^2}\]

**2. GR perihelion advance per orbit in arcseconds**

Substituting the given values:

\[a = 5.7909\times 10^{10} \text{ m}, \quad e = 0.2056\]

The semi-latus rectum $p$ is:

\[p = a(1 - e^2) = 5.6657\times 10^{10} \text{ m}\]

The radius of the orbit is:

\[r = a(1 + e) = 6.9857\times 10^{10} \text{ m}\]

The GR perihelion advance per orbit in radians is:

\[\Delta\phi = \frac{3\pi}{2}\frac{r^2}{c^2} = \frac{3\pi}{2}\frac{(6.9857\times 10^{10})^2}{(3\times 10^8)^2} = 4.287\times 10^{-7} \text{ rad}\]

Converting to arcseconds:

\[\Delta\phi = 4.287\times 10^{-7} \text{ rad} \cdot \frac{180}{\pi} \cdot \frac{3600''}{180^\circ} = 0.000257''\]

**3. GR perihelion advance per century**

The orbital period $T$ is:

\[T = \frac{2\pi r^2}{GM_\odot} = 87.969 \text{ d}\]

The number of orbits per century is:

\[N = \frac{100 \text{ yr}}{T} = 1.137 \text{ orbits/yr} \cdot 100 = 113.7 \text{ orbits/century}\]

The GR perihelion advance per century is:

\[\Delta\phi_{century} = \Delta\phi \cdot N = 0.000257'' \cdot 113.7 = 0.0292''\]

**4. Remaining precession**

The observed precession is about $574''$/century. The remaining precession is:

\[574'' - 0.0292'' = 573.97''\]

This is primarily due to the oblateness of the Sun, which causes a precession of about $2.4''$/century. The rest is due to other effects such as the general relativistic effect of the other planets, the Moon, and the general relativistic effect of the Sun's quadrupole moment.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{advance\_arcsec\_orbit} &= 0.000257'' \\
\mathrm{advance\_arcsec\_century} &= 0.0292'' \\
\mathrm{orbits\_per\_century} &= 113.7
\end{aligned}
\]