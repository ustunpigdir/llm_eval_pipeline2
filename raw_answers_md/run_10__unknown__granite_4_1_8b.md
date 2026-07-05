To verify the given formula for the apsidal angle \(\Phi = \frac{\pi}{\sqrt{3+n}}\) for different values of \(n\) and to address the subsequent tasks, we proceed as follows:

### 1. Verification for Closed-Orbit Cases

**Keplerian case (\(n = -2\)):**

\[
\Phi = \frac{\pi}{\sqrt{3 + (-2)}} = \frac{\pi}{\sqrt{1}} = \pi \text{ radians}
\]

Convert to degrees:

\[
\Phi = \pi \text{ radians} \times \frac{180^\circ}{\pi} = 180^\circ
\]

Thus, for \(n = -2\), the apsidal angle is \(180^\circ\).

**Harmonic oscillator case (\(n = +1\)):**

\[
\Phi = \frac{\pi}{\sqrt{3 + 1}} = \frac{\pi}{\sqrt{4}} = \frac{\pi}{2} \text{ radians}
\]

Convert to degrees:

\[
\Phi = \frac{\pi}{2} \text{ radians} \times \frac{180^\circ}{\pi} = 90^\circ
\]

Thus, for \(n = +1\), the apsidal angle is \(90^\circ\).

### 2. Evaluation for \(n = -1\)

For \(n = -1\):

\[
\Phi = \frac{\pi}{\sqrt{3 + (-1)}} = \frac{\pi}{\sqrt{2}} \text{ radians}
\]

Convert to degrees:

\[
\Phi = \frac{\pi}{\sqrt{2}} \times \frac{180^\circ}{\pi} = \frac{180^\circ}{\sqrt{2}} \approx 127.28^\circ
\]

Thus, the apsidal angle for \(n = -1\) is approximately \(127.28^\circ\).

### 3. Orbit Closure and Precession for \(n = -1\)

For \(n = -1\), the apsidal angle \(\Phi \approx 127.28^\circ\) is not a rational fraction of \(360^\circ\). Therefore, the orbit is **not closed**.

The apsidal precession per radial period (i.e., per complete cycle from perihelion back to perihelion) is given by:

\[
2\Phi - 360^\circ = 2 \times 127.28^\circ - 360^\circ \approx 254.56^\circ - 360^\circ = -105.44^\circ
\]

Thus, the apsidal precession per radial period for \(n = -1\) is approximately \(-105.44^\circ\).

### 4. Bertrand's Theorem and Implications

**Bertrand's Theorem:**  
Bertrand's theorem states that only two types of central force potentials produce closed orbits for all bound particles: the inverse-square law (\(F \propto -1/r^2\), \(n = -2\)) and the linear restoring force (\(F \propto -r\), \(n = +1\)). No other central force law yields closed orbits for all initial conditions.

**Illustration with Results:**  
- For \(n = -2\) (Keplerian force), the apsidal angle is \(180^\circ\), indicating that each orbit is a closed ellipse (a special case of a closed orbit).
- For \(n = +1\) (harmonic oscillator), the apsidal angle is \(90^\circ\), corresponding to a closed orbit (a circle or ellipse with a constant precession that completes a cycle in two radial periods).
- For \(n = -1\), the apsidal angle is approximately \(127.28^\circ\), leading to non-closed orbits, consistent with Bertrand's theorem.

**Failure for \(n \le -3\):**  
For \(n \le -3\), the central force becomes stronger than the inverse-square law at large distances, leading to trajectories that are not closed. The apsidal angle formula \(\Phi = \frac{\pi}{\sqrt{3+n}}\) becomes undefined or yields angles that do not correspond to closed orbits, violating Bertrand's theorem. These forces result in increasingly rapid precession, preventing the return to the initial position after a finite number of revolutions.

### FINAL ANSWER
\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180.0 \\
\mathrm{apsidal\_harmonic\_deg} &= 90.0 \\
\mathrm{apsidal\_n\_minus1\_deg} &= 127.28 \\
\mathrm{precession\_per\_period\_deg} &= -105.44
\end{aligned}
\]