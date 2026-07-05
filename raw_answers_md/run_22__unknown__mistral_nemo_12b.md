**1. Verification for closed orbits:**

For $n = -2$ (Kepler's law), the force is $F(r) = -k/r^2$. The orbit is an ellipse, and the apsidal angle $\Phi = \pi/\sqrt{3+n} = \pi/\sqrt{1} = \pi \approx 180^\circ$. This is correct as the major axis of an ellipse is aligned with the line joining the perihelion and aphelion.

For $n = +1$ (harmonic oscillator), the force is $F(r) = -kr$. The orbit is a circle, and the apsidal angle $\Phi = \pi/\sqrt{3+n} = \pi/\sqrt{4} = \pi/2 \approx 90^\circ$. This is correct as in a circle, the angle between any two points is $90^\circ$.

**2. Apsidal angle for $n = -1$:**

For $n = -1$, the force is $F(r) = -k/r$. Substituting into the formula for $\Phi$, we get $\Phi = \pi/\sqrt{3+n} = \pi/\sqrt{2} \approx 135^\circ$.

**3. Orbit closure and precession for $n = -1$:**

For $n = -1$, the orbit is not closed. The apsidal precession per radial period is $2\Phi - 360^\circ = 2(135^\circ) - 360^\circ = -90^\circ$. This means the orbit precesses $90^\circ$ per radial period.

**4. Bertrand's theorem:**

Bertrand's theorem states that the only central force inverse laws that admit closed orbits are those of the form $F(r) = -kr^n$ where $n = -1$ or $n = -2$. Our results illustrate this theorem as we found closed orbits for $n = -2$ and $n = -1$, but not for $n = +1$.

For $n \le -3$, the force becomes too strong at small radii, causing the orbit to collapse to a point. This is why Bertrand's theorem does not include these cases.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180^\circ \\
\mathrm{apsidal\_harmonic\_deg} &= 90^\circ \\
\mathrm{apsidal\_n\_minus1\_deg} &= 135^\circ \\
\mathrm{precession\_per\_period\_deg} &= -90^\circ
\end{aligned}
\]