**1. Verification for closed orbits:**

For $n = -2$ (Kepler's law), the force is $F(r) = -k/r^2$. The orbit is an ellipse, and the apsidal angle is $\Phi = 180^\circ$ (half a period).

For $n = +1$ (harmonic oscillator), the force is $F(r) = -k r$. The orbit is a circle, and the apsidal angle is $\Phi = 360^\circ$ (a full period).

**2. Apsidal angle for $n = -1$:**

For $n = -1$, the force is $F(r) = -k/r$. Using the given formula for the apsidal angle, we have:

\[
\Phi = \frac{\pi}{\sqrt{3+n}} = \frac{\pi}{\sqrt{3-1}} = \frac{\pi}{\sqrt{2}} \approx 127.3^\circ
\]

**3. Orbit closure and precession for $n = -1$:**

For $n = -1$, the orbit is not closed. The radial period is $2\pi$ radians, and the apsidal angle is $\frac{\pi}{\sqrt{2}}$ radians. The apsidal precession per radial period is:

\[
2\Phi - 360^\circ = 2 \cdot \frac{\pi}{\sqrt{2}} - 360^\circ \approx 127.3^\circ - 360^\circ = -232.7^\circ
\]

**4. Bertrand's theorem:**

Bertrand's theorem states that the only central forces that admit closed orbits are those of the form $F(r) = -k/r^n$ for $n = -1$ or $n = -2$. Our results illustrate this theorem, as we found closed orbits for $n = -1$ and $n = -2$. However, for $n \le -3$, the force becomes too strong at small radii, and the orbit may not be closed or may not exist at all.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180^\circ \\
\mathrm{apsidal\_harmonic\_deg} &= 360^\circ \\
\mathrm{apsidal\_n\_minus1\_deg} &= 127.3^\circ \\
\mathrm{precession\_per\_period\_deg} &= -232.7^\circ
\end{aligned}
\]