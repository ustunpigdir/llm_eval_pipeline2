To verify the given formula for the apsidal angle \(\Phi = \frac{\pi}{\sqrt{3+n}}\) for different values of the force exponent \(n\), we proceed as follows:

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

\[
\Phi = \frac{\pi}{\sqrt{3 + (-1)}} = \frac{\pi}{\sqrt{2}} \text{ radians}
\]

Convert to degrees:

\[
\Phi = \frac{\pi}{\sqrt{2}} \text{ rad} \times \frac{180^\circ}{\pi} = \frac{180^\circ}{\sqrt{2}} \approx 127.28^\circ
\]

Thus, for \(n = -1\), the apsidal angle is approximately \(127.28^\circ\).

### 3. Apsidal Precession per Radial Period for \(n = -1\)

The apsidal precession per radial period is given by:

\[
2\Phi - 360^\circ
\]

Substitute \(\Phi \approx 127.28^\circ\):

\[
2\Phi \approx 2 \times 127.28^\circ = 254.56^\circ
\]

\[
2\Phi - 360^\circ \approx 254.56^\circ - 360^\circ = -105.44^\circ
\]

The negative sign indicates a retrograde precession. Thus, the apsidal precession per radial period for \(n = -1\) is approximately \(-105.44^\circ\).

### 4. Bertrand's Theorem and Its Implications

**Bertrand's Theorem:**  
Bertrand's theorem states that only two types of central force potentials produce closed orbits for all bound particles: the inverse-square law (\(F \propto -1/r^2\), \(n = -2\)) and the linear restoring force (\(F \propto -r\), \(n = +1\)). No other central force law yields closed orbits for all initial conditions.

**Illustration with Results:**  
- For \(n = -2\) (Keplerian force), the apsidal angle is \(180^\circ\), indicating that each orbit is a closed ellipse, consistent with Bertrand's theorem.
- For \(n = +1\) (harmonic oscillator), the apsidal angle is \(90^\circ\), corresponding to a closed Lissajous figure, again consistent with the theorem.
- For \(n = -1\) (inverse linear force), the apsidal angle is approximately \(127.28^\circ\), leading to a non‑closed orbit with a precession of about \(-105.44^\circ\) per radial period, illustrating that this force does not satisfy Bertrand's condition for closed orbits.

**Failure for \(n \le -3\):**  
For \(n \le -3\), the central force becomes more singular than the inverse-square law, leading to even larger deviations from closed orbits. The apsidal angle increases, causing significant precession, and the orbits become highly elliptical or even unbound, violating the conditions of Bertrand's theorem. Thus, such forces do not produce closed orbits for all bound particles.

### FINAL ANSWER
\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180 \\
\mathrm{apsidal\_harmonic\_deg} &= 90 \\
\mathrm{apsidal\_n\_minus1\_deg} &\approx 127.28 \\
\mathrm{precession\_per\_period\_deg} &\approx -105.44
\end{aligned}
\]