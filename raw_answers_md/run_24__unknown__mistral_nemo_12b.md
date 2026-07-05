**Derivation:**

The equation of motion for a particle in a central force field is given by:

\[
\frac{d^2 \mathbf{r}}{dt^2} = -\frac{k}{m} r^{n-1} \hat{\mathbf{r}}
\]

For nearly circular orbits, we can use the following approximation for the radial coordinate:

\[
r(t) = r_0 + \delta r \cos(\omega t)
\]

where $r_0$ is the mean radius, $\delta r$ is the amplitude of the radial oscillation, and $\omega$ is the angular frequency. Substituting this into the equation of motion and keeping terms up to first order in $\delta r$, we get:

\[
\omega^2 \delta r \cos(\omega t) = -\frac{k}{m} (r_0 + \delta r \cos(\omega t))^{n-1} (r_0 + \delta r \cos(\omega t))
\]

Expanding and keeping terms up to first order, we get:

\[
\omega^2 \delta r \cos(\omega t) = -\frac{k}{m} r_0^{n-1} \delta r \cos(\omega t) - \frac{k}{m} (n-1) r_0^{n-2} \delta r^2 \cos^2(\omega t)
\]

Dividing by $\delta r \cos(\omega t)$ and using the identity $\cos^2(\omega t) = \frac{1 + \cos(2\omega t)}{2}$, we get:

\[
\omega^2 = -\frac{k}{m} r_0^{n-1} - \frac{k}{m} (n-1) r_0^{n-2} \frac{1 + \cos(2\omega t)}{2}
\]

The first term on the right-hand side gives the mean angular frequency, and the second term gives the precession of the orbit. The precession per radial period is given by:

\[
\Delta \Phi = \frac{1}{2} \int_0^{2\pi/\omega} \frac{k}{m} (n-1) r_0^{n-2} \frac{1 + \cos(2\omega t)}{2} dt
\]

\[
\Delta \Phi = \frac{1}{2} \frac{k}{m} (n-1) r_0^{n-2} \frac{1}{2} \int_0^{2\pi/\omega} (1 + \cos(2\omega t)) dt
\]

\[
\Delta \Phi = \frac{1}{2} \frac{k}{m} (n-1) r_0^{n-2} \frac{1}{2} \left( \frac{2\pi}{\omega} + \frac{1}{2\omega} \sin(2\omega t) \right) \bigg|_0^{2\pi/\omega}
\]

\[
\Delta \Phi = \frac{1}{2} \frac{k}{m} (n-1) r_0^{n-2} \frac{\pi}{\omega}
\]

**Tasks:**

1. For $n = -2$ (Kepler's law), we have:

\[
\Phi = \frac{\pi}{\sqrt{3+n}} = \frac{\pi}{\sqrt{1}} = \pi \approx 180^\circ
\]

For $n = +1$ (harmonic oscillator), we have:

\[
\Phi = \frac{\pi}{\sqrt{3+n}} = \frac{\pi}{\sqrt{2}} \approx 127.3^\circ
\]

2. For $n = -1$, we have:

\[
\Phi = \frac{\pi}{\sqrt{3+n}} = \frac{\pi}{\sqrt{2}} \approx 127.3^\circ
\]

3. For $n = -1$, the orbit is not closed. The apsidal precession per radial period is:

\[
\Delta \Phi = \frac{1}{2} \frac{k}{m} (n-1) r_0^{n-2} \frac{\pi}{\omega} - 360^\circ
\]

\[
\Delta \Phi = \frac{1}{2} \frac{k}{m} r_0^{-1} \frac{\pi}{\omega} - 360^\circ
\]

**Bertrand's Theorem:**

Bertrand's theorem states that the only central force laws that admit closed orbits are those of the form $F(r) = -k/r^n$ where $n = -1, -2, -3$. Our results illustrate this theorem for $n = -1$ and $n = -2$. However, for $n \le -3$, the force becomes infinite at the origin, which is not physically meaningful.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180^\circ \\
\mathrm{apsidal\_harmonic\_deg} &= 127.3^\circ \\
\mathrm{apsidal\_n\_minus1\_deg} &= 127.3^\circ \\
\mathrm{precession\_per\_period\_deg} &= \mathrm{INVALID}
\end{aligned}
\]