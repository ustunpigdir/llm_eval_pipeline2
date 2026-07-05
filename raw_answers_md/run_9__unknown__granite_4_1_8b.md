To verify the given formula for the apsidal angle \(\Phi = \frac{\pi}{\sqrt{3+n}}\) for different values of \(n\) and to address the subsequent tasks, we proceed as follows:

### 1. Verification for Closed-Orbit Cases

**Keplerian case (\(n = -2\)):**

\[
\Phi = \frac{\pi}{\sqrt{3 + (-2)}} = \frac{\pi}{\sqrt{1}} = \pi \text{ radians}
\]

Convert to degrees:

\[
\Phi = \pi \text{ rad} \times \frac{180^\circ}{\pi} = 180^\circ
\]

Thus, for \(n = -2\), the apsidal angle is \(180^\circ\).

**Harmonic oscillator case (\(n = +1\)):**

\[
\Phi = \frac{\pi}{\sqrt{3 + 1}} = \frac{\pi}{\sqrt{4}} = \frac{\pi}{2} \text{ radians}
\]

Convert to degrees:

\[
\Phi = \frac{\pi}{2} \text{ rad} \times \frac{180^\circ}{\pi} = 90^\circ
\]

Thus, for \(n = +1\), the apsidal angle is \(90^\circ\).

### 2. Evaluation for \(n = -1\)

For \(n = -1\):

\[
\Phi = \frac{\pi}{\sqrt{3 + (-1)}} = \frac{\pi}{\sqrt{2}} \text{ radians}
\]

Convert to degrees:

\[
\Phi = \frac{\pi}{\sqrt{2}} \text{ rad} \times \frac{180^\circ}{\pi} = \frac{180^\circ}{\sqrt{2}} \approx 127.28^\circ
\]

Thus, the apsidal angle for \(n = -1\) is approximately \(127.28^\circ\).

### 3. Orbit Closure and Apsidal Precession for \(n = -1\)

For \(n = -1\), the orbit is **not closed** because the apsidal angle is not a rational fraction of \(360^\circ\). The apsidal precession per radial period (which corresponds to two successive perihelia, i.e., one full radial oscillation) is given by:

\[
2\Phi - 360^\circ = 2 \times \frac{\pi}{\sqrt{2}} - 360^\circ
\]

Calculate \(2\Phi\):

\[
2\Phi = 2 \times \frac{\pi}{\sqrt{2}} = \sqrt{2}\pi \text{ radians}
\]

Convert to degrees:

\[
2\Phi = \sqrt{2}\pi \text{ rad} \times \frac{180^\circ}{\pi} = 180^\circ \sqrt{2} \approx 254.56^\circ
\]

Thus, the precession per radial period is:

\[
2\Phi - 360^\circ \approx 254.56^\circ - 360^\circ = -105.44^\circ
\]

Since we are interested in the magnitude of precession, we take the positive value:

\[
\text{Precession per radial period} \approx 105.44^\circ
\]

### 4. Bertrand's Theorem and Implications

**Bertrand's Theorem:**  
Bertrand's theorem states that only two types of central force potentials produce closed orbits for all bound particles: the inverse-square law (\(F \propto -1/r^2\), \(n = -2\)) and the linear restoring force (\(F \propto -r\), \(n = +1\)). No other central force law yields closed orbits for all initial conditions.

**Illustration with Results:**  
- For \(n = -2\) (Keplerian force), the apsidal angle is \(180^\circ\), indicating that each orbit completes a full ellipse, confirming closed orbits.
- For \(n = +1\) (harmonic oscillator), the apsidal angle is \(90^\circ\), corresponding to a rotation of a figure-eight shape, also a closed orbit.
- For \(n = -1\), the apsidal angle is approximately \(127.28^\circ\), leading to a non‑closed orbit with a precession of about \(105.44^\circ\) per radial period, consistent with Bertrand's theorem.

**Failure for \(n \le -3\):**  
For \(n \le -3\), the central force leads to potentials that do not satisfy the conditions of Bertrand's theorem. Such forces result in orbits that precess significantly and do not close, as the angular advance per revolution exceeds the conditions for periodicity. This is because the effective potential introduces additional terms that prevent the orbit from repeating exactly after each revolution.

### FINAL ANSWER
\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180 \\
\mathrm{apsidal\_harmonic\_deg} &= 90 \\
\mathrm{apsidal\_n\_minus1\_deg} &\approx 127.28 \\
\mathrm{precession\_per\_period\_deg} &\approx 105.44
\end{aligned}
\]