To analyze the stability and apsidal angles of nearly circular orbits under a central force $F(r) = -k r^n$, we use the provided formula for the apsidal angle $\Phi$:
$$\Phi = \frac{\pi}{\sqrt{3+n}}$$
The apsidal angle $\Phi$ is the angle swept by the particle as it moves from perihelion (minimum radius) to aphelion (maximum radius).

### 1. Verification for Closed-Orbit Cases
A closed orbit requires the particle to return to the same radial position after a full rotation of $2\pi$. This occurs if $2\Phi$ is a rational multiple of $2\pi$.

**Case $n = -2$ (Kepler Problem):**
$$\Phi = \frac{\pi}{\sqrt{3 + (-2)}} = \frac{\pi}{\sqrt{1}} = \pi \text{ radians}$$
Converting to degrees: $\Phi = 180^\circ$.
In this case, $2\Phi = 360^\circ$, meaning the orbit closes after one radial period.

**Case $n = +1$ (Isotropic Harmonic Oscillator):**
$$\Phi = \frac{\pi}{\sqrt{3 + 1}} = \frac{\pi}{\sqrt{4}} = \frac{\pi}{2} \text{ radians}$$
Converting to degrees: $\Phi = 90^\circ$.
In this case, $2\Phi = 180^\circ$, meaning the orbit closes after two radial periods (the path is an ellipse centered at the origin).

### 2. Evaluation for $n = -1$
For a force $F(r) = -k r^{-1}$:
$$\Phi = \frac{\pi}{\sqrt{3 + (-1)}} = \frac{\pi}{\sqrt{2}} \text{ radians}$$
Converting to degrees:
$$\Phi = \frac{180^\circ}{\sqrt{2}} \approx \frac{180^\circ}{1.4142} \approx 127.279^\circ$$

### 3. Orbit Closure and Precession for $n = -1$
An orbit is closed if $2\Phi$ is a rational multiple of $360^\circ$.
For $n = -1$, $2\Phi = \frac{2\pi}{\sqrt{2}} = \pi\sqrt{2}$. Since $\sqrt{2}$ is irrational, the orbit is **not closed**.

The apsidal precession per radial period is the difference between the angle swept in one full radial cycle (from perihelion to aphelion and back) and a full circle:
$$\Delta \theta = 2\Phi - 360^\circ$$
$$\Delta \theta = 2 \left( \frac{180^\circ}{\sqrt{2}} \right) - 360^\circ = \frac{360^\circ}{\sqrt{2}} - 360^\circ = 360^\circ \left( \frac{1}{\sqrt{2}} - 1 \right)$$
$$\Delta \theta \approx 360^\circ (0.7071 - 1) = 360^\circ (-0.2929) \approx -105.44^\circ$$

### 4. Bertrand's Theorem and Stability
**Bertrand's Theorem** states that the only central force laws for which all bounded orbits are closed are the inverse-square law ($n=-2$) and Hooke's law ($n=1$). Our results illustrate this: for $n=-1$, the orbit does not close.

**Stability for $n \le -3$:**
The formula $\Phi = \pi/\sqrt{3+n}$ involves a square root. If $n = -3$, the denominator becomes zero ($\Phi \to \infty$), indicating the orbit is no longer "nearly circular" in a stable sense. If $n < -3$, the term under the square root is negative, making $\Phi$ imaginary. Physically, this corresponds to the condition for circular orbit stability: $\frac{d}{dr} \left( F(r) + \frac{L^2}{mr^3} \right) < 0$. For $n \le -3$, circular orbits are unstable; any small perturbation causes the particle to either spiral into the center or escape to infinity.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180^\circ \\
\mathrm{apsidal\_harmonic\_deg} &= 90^\circ \\
\mathrm{apsidal\_n\_minus1\_deg} &= 127.28^\circ \\
\mathrm{precession\_per\_period\_deg} &= -105.44^\circ
\end{aligned}
\]