Okay, let's analyze the central-force motion and apsidal angles.

**1. Verification for n = -2 (Kepler) and n = +1 (Harmonic)**

The given formula for the apsidal angle is $\Phi = \pi/\sqrt{3+n}$.

For $n = -2$ (Kepler):
$\Phi = \pi / \sqrt{3 + (-2)} = \pi / \sqrt{1} = \pi$ radians.
Converting to degrees: $\Phi = \pi \times \frac{180}{\pi} = 180^\circ$.

For $n = +1$ (Harmonic):
$\Phi = \pi / \sqrt{3 + 1} = \pi / \sqrt{4} = \pi / 2$ radians.
Converting to degrees: $\Phi = (\pi / 2) \times \frac{180}{\pi} = 90^\circ$.

**2. Evaluation for n = -1 (Inverse Square Law)**

For $n = -1$ (Inverse Square Law):
$\Phi = \pi / \sqrt{3 + (-1)} = \pi / \sqrt{2}$ radians.
Converting to degrees: $\Phi = (\pi / \sqrt{2}) \times \frac{180}{\pi} = \frac{180}{\sqrt{2}} = 90\sqrt{2} \approx 127.28^\circ$.

**3. Orbit Closure and Precession for n = -1**

For $n = -1$, the orbit is *not* closed. Bertrand's theorem (stated below) will explain why.

To compute the apsidal precession per radial period, we calculate $2\Phi - 360^\circ$.
$2\Phi = 2 \times \frac{180}{\sqrt{2}} = \frac{360}{\sqrt{2}} = 180\sqrt{2} \approx 254.56^\circ$.
$2\Phi - 360^\circ = 180\sqrt{2} - 360^\circ \approx 254.56^\circ - 360^\circ = -105.44^\circ$.

**4. Bertrand's Theorem and Implications**

Bertrand's theorem states that for a central force $F(r) = -k r^n$, the orbit is closed (i.e., conic section is an ellipse, parabola, or hyperbola) if and only if $n = -2$.  If $n \neq -2$, the orbit is not closed; it precesses.

The given formula $\Phi = \pi/\sqrt{3+n}$ is derived under the assumption of near-circular orbits.  For $n = -2$, $\Phi = 180^\circ$, which corresponds to no precession (a closed orbit). For $n = +1$, $\Phi = 90^\circ$, indicating precession. For $n = -1$, $\Phi \approx 127.28^\circ$, also indicating precession.

What goes wrong for $n \le -3$?  The derivation of the formula for $\Phi$ relies on a small eccentricity approximation. When $n \le -3$, the potential energy becomes very large at small distances, and the orbit can become highly eccentric. The small eccentricity approximation breaks down, and the formula for $\Phi$ is no longer valid.  Furthermore, the orbits become increasingly unstable and can escape to infinity. The assumption of a near-circular orbit is no longer reasonable. The force becomes very strong at small radii, leading to chaotic behavior.

\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180 \\
\mathrm{apsidal\_harmonic\_deg} &= 90 \\
\mathrm{apsidal\_n\_minus1\_deg} &= 127.28 \\
\mathrm{precession\_per\_period\_deg} &= -105.44
\end{aligned}
\]