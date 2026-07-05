### Derivation and Analysis

The apsidal angle $\Phi$ is the angle swept by the particle between the minimum radius (perihelion) and maximum radius (aphelion). For nearly circular orbits in a central force $F(r) = -k r^n$, the formula is given as:
$$\Phi = \frac{\pi}{\sqrt{3+n}}$$

#### 1. Verification for Closed-Orbit Cases
A closed orbit requires the particle to return to the same radial position after a full $2\pi$ rotation. This occurs if $2\Phi$ is a rational multiple of $2\pi$.

*   **Kepler Case ($n = -2$):**
    $$\Phi = \frac{\pi}{\sqrt{3 + (-2)}} = \frac{\pi}{\sqrt{1}} = \pi \text{ radians}$$
    Converting to degrees: $\Phi = 180^\circ$.
    (The radial period is $2\pi$, and the orbit is an ellipse with the center of force at one focus).

*   **Harmonic Case ($n = +1$):**
    $$\Phi = \frac{\pi}{\sqrt{3 + 1}} = \frac{\pi}{\sqrt{4}} = \frac{\pi}{2} \text{ radians}$$
    Converting to degrees: $\Phi = 90^\circ$.
    (The radial period is $4\Phi = 2\pi$, and the orbit is an ellipse with the center of force at the center).

#### 2. Evaluation for $n = -1$
For a force $F(r) = -k r^{-1}$ (inverse-linear force):
$$\Phi = \frac{\pi}{\sqrt{3 + (-1)}} = \frac{\pi}{\sqrt{2}} \text{ radians}$$
Converting to degrees:
$$\Phi = \frac{180^\circ}{\sqrt{2}} \approx \frac{180^\circ}{1.4142} \approx 127.279^\circ$$

#### 3. Orbit Closure and Precession for $n = -1$
An orbit is closed if $2\Phi$ is a rational multiple of $360^\circ$.
For $n = -1$, $2\Phi = \frac{2\pi}{\sqrt{2}} = \pi\sqrt{2}$. Since $\sqrt{2}$ is irrational, the orbit is **not closed**.

The apsidal precession per radial period is the difference between the angle swept in one full radial cycle (from perihelion to aphelion and back) and a full circle:
$$\Delta \theta = 2\Phi - 360^\circ$$
$$\Delta \theta = 2 \left( \frac{180^\circ}{\sqrt{2}} \right) - 360^\circ = \frac{360^\circ}{\sqrt{2}} - 360^\circ = 360^\circ \left( \frac{1}{\sqrt{2}} - 1 \right)$$
$$\Delta \theta \approx 360^\circ (0.7071 - 1) = 360^\circ (-0.2929) \approx -105.44^\circ$$

#### 4. Bertrand's Theorem and Stability
**Bertrand's Theorem** states that the only central forces for which all bounded orbits are closed are the inverse-square law ($n=-2$) and Hooke's law ($n=1$). Our results illustrate this: for $n=-1$, the orbit does not close.

**Stability for $n \le -3$:**
The formula for $\Phi$ involves $\sqrt{3+n}$. If $n = -3$, the denominator becomes zero ($\Phi \to \infty$), indicating a transition in stability. If $n < -3$, the term under the square root becomes negative, making $\Phi$ imaginary. Physically, this corresponds to the case where circular orbits are unstable; any small perturbation causes the particle to either spiral into the center or escape to infinity.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180^\circ \\
\mathrm{apsidal\_harmonic\_deg} &= 90^\circ \\
\mathrm{apsidal\_n\_minus1\_deg} &= 127.28^\circ \\
\mathrm{precession\_per\_period\_deg} &= -105.44^\circ
\end{aligned}
\]