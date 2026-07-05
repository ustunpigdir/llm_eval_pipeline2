
Here's the derivation and calculation of the GR perihelion advance for Mercury.

**1. GR Perihelion Advance per Orbit**

The first-order GR perihelion advance per orbit is given by:

$\Delta \phi = \frac{6\pi G M_\odot}{a(1-e^2)c^2}$ radians per orbit.

To convert this to arcseconds, we use the conversion factor $1 \text{ radian} = \frac{180}{\pi} \text{ degrees} = \frac{180}{\pi} \times 3600 \text{ arcseconds}$.  Therefore,

$\Delta \phi = \frac{6\pi G M_\odot}{a(1-e^2)c^2} \times \frac{180}{\pi} \times 3600 \text{ arcseconds per orbit}$
$\Delta \phi = \frac{6 \times 180 \times 3600 G M_\odot}{a(1-e^2)c^2} \text{ arcseconds per orbit}$
$\Delta \phi = \frac{3888000 G M_\odot}{a(1-e^2)c^2} \text{ arcseconds per orbit}$

**2. Evaluate $\Delta\phi$ in arcseconds per orbit**

We are given:
$a = 5.7909 \times 10^{10}$ m
$e = 0.2056$
$GM_\odot = 1.32712 \times 10^{20}$ m$^3$/s$^2$
$c = 299792458$ m/s

$1-e^2 = 1 - (0.2056)^2 = 1 - 0.0422 = 0.9578$

$\Delta \phi = \frac{3888000 \times 1.32712 \times 10^{20}}{(5.7909 \times 10^{10}) \times 0.9578 \times (299792458)^2} \text{ arcseconds per orbit}$
$\Delta \phi = \frac{5.1655 \times 10^{26}}{5.7909 \times 10^{10} \times 0.9578 \times 8.98755 \times 10^{16}} \text{ arcseconds per orbit}$
$\Delta \phi = \frac{5.1655 \times 10^{26}}{4.725 \times 10^{28}} \text{ arcseconds per orbit}$
$\Delta \phi = 0.01093 \text{ arcseconds per orbit}$

**3. Convert to arcseconds per century**

The orbital period of Mercury is $T = 87.969$ days.
The number of orbits per century (36525 days) is:
$\text{orbits per century} = \frac{36525}{87.969} \approx 415.05$

$\Delta \phi_{\text{century}} = \Delta \phi \times \text{orbits per century} = 0.01093 \text{ arcseconds/orbit} \times 415.05 \text{ orbits/century}$
$\Delta \phi_{\text{century}} = 4.532 \text{ arcseconds per century}$

**4. Observed Precession and GR Test**

The observed perihelion precession of Mercury is approximately $574''$/century. The GR calculation gives about $4.532''$/century. The difference ($574 - 4.532 \approx 569.468''$/century) is primarily due to perturbations from other planets in the solar system, especially Venus, Jupiter, and Saturn.  These perturbations were known before GR, and the remaining precession *after* accounting for these Newtonian effects was the key test of General Relativity.  The GR calculation accurately predicts the remaining, unexplained portion of the precession.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{advance\_arcsec\_orbit} &= 0.01093 \\
\mathrm{advance\_arcsec\_century} &= 4.532 \\
\mathrm{orbits\_per\_century} &= 415.05
\end{aligned}
\]