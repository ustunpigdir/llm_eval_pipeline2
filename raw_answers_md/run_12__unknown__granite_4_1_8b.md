To verify the given formula for the apsidal angle \(\Phi = \frac{\pi}{\sqrt{3+n}}\) for different values of the force exponent \(n\), we proceed as follows:

### 1. Verification for Closed-Orbit Cases

#### (a) Keplerian case (\(n = -2\)):
\[
\Phi = \frac{\pi}{\sqrt{3 + (-2)}} = \frac{\pi}{\sqrt{1}} = \pi \text{ radians}
\]
Convert to degrees:
\[
\Phi = \pi \text{ rad} \times \frac{180^\circ}{\pi} = 180^\circ
\]
Thus, for \(n = -2\):
\[
\mathrm{apsidal\_kepler\_deg} = 180^\circ
\]

#### (b) Harmonic oscillator case (\(n = +1\)):
\[
\Phi = \frac{\pi}{\sqrt{3 + 1}} = \frac{\pi}{\sqrt{4}} = \frac{\pi}{2} \text{ radians}
\]
Convert to degrees:
\[
\Phi = \frac{\pi}{2} \text{ rad} \times \frac{180^\circ}{\pi} = 90^\circ
\]
Thus, for \(n = +1\):
\[
\mathrm{apsidal\_harmonic\_deg} = 90^\circ
\]

### 2. Evaluation for \(n = -1\)

For \(n = -1\):
\[
\Phi = \frac{\pi}{\sqrt{3 + (-1)}} = \frac{\pi}{\sqrt{2}} \text{ radians}
\]
Convert to degrees:
\[
\Phi = \frac{\pi}{\sqrt{2}} \text{ rad} \times \frac{180^\circ}{\pi} = \frac{180^\circ}{\sqrt{2}} \approx 127.28^\circ
\]
Thus, for \(n = -1\):
\[
\mathrm{apsidal\_n\_minus1\_deg} \approx 127.28^\circ
\]

### 3. Apsidal Precession per Radial Period for \(n = -1\)

The apsidal precession per radial period is given by:
\[
2\Phi - 360^\circ
\]
Substituting \(\Phi \approx 127.28^\circ\):
\[
2\Phi \approx 2 \times 127.28^\circ = 254.56^\circ
\]
\[
\text{Precession per period} = 254.56^\circ - 360^\circ = -105.44^\circ
\]
Since precession is typically expressed as a positive magnitude, we take the absolute value:
\[
\mathrm{precession\_per\_period\_deg} \approx 105.44^\circ
\]

### 4. Bertrand's Theorem and Implications

**Bertrand's Theorem:**  
Bertrand's theorem states that only two types of central force potentials produce closed orbits for all bound particles:  
1. The inverse-square law, \(F(r) \propto -\frac{1}{r^2}\) (Kepler problem, \(n = -2\)).  
2. The linear restoring force, \(F(r) \propto -kr\) (isotropic harmonic oscillator, \(n = +1\)).

**Illustration with Results:**  
- For \(n = -2\) (Kepler), the apsidal angle is \(180^\circ\), indicating that each orbit completes a full ellipse, confirming closed orbits.  
- For \(n = +1\) (harmonic), the apsidal angle is \(90^\circ\), leading to a closed orbit after two radial periods, again consistent with Bertrand's theorem.  
- For \(n = -1\) (inverse linear force), the apsidal angle is approximately \(127.28^\circ\), resulting in a non‑closed orbit with a precession of about \(105.44^\circ\) per radial period, illustrating that this force does **not** satisfy Bertrand's condition for closed orbits.

**Failure for \(n \le -3\):**  
For \(n \le -3\), the potential leads to more complex radial dynamics. The effective potential does not produce the simple closed‑orbit behavior required by Bertrand's theorem. Specifically, the apsidal angle becomes less than \(180^\circ\), and the orbits exhibit significant precession, indicating that the trajectories are not closed. This is because the force law \(F(r) \propto -r^{n}\) with \(n \le -3\) does not yield the necessary conditions for the conservation of the Laplace‑Runge‑Lenz vector that ensures closed orbits.

### FINAL ANSWER
\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180 \\
\mathrm{apsidal\_harmonic\_deg} &= 90 \\
\mathrm{apsidal\_n\_minus1\_deg} &\approx 127.28 \\
\mathrm{precession\_per\_period\_deg} &\approx 105.44
\end{aligned}
\]