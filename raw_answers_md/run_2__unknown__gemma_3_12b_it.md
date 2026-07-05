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
Precession per period = $2\Phi - 360^\circ = 180\sqrt{2} - 360^\circ \approx 254.56^\circ - 360^\circ = -105.44^\circ$.

**4. Bertrand's Theorem and Explanation**

Bertrand's theorem states that for a central force $F(r) = -k r^n$, where $k$ is a constant, the orbit is closed (i.e., periodic) if and only if $n = -2$.  In other words, only Kepler's inverse-square law produces closed orbits.

The given formula $\Phi = \pi/\sqrt{3+n}$ arises from a perturbation analysis of the Keplerian orbit.  It assumes that the central force is *nearly* Keplerian, meaning that the deviation from the inverse-square law is small.  When $n \neq -2$, the orbit is not closed, and the apsidal angle reflects the rate of precession due to the deviation from the Keplerian case.

For $n \le -3$, the integral required to determine the orbit's shape becomes divergent. This means the orbit is not well-defined, and the concept of an apsidal angle loses its meaning. The force becomes too weak at large distances, and the particle's motion is not bounded. The perturbation analysis used to derive the formula for $\Phi$ is not valid in this regime. The assumptions of a "nearly circular" orbit break down because the particle can escape to infinity.

\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180 \\
\mathrm{apsidal\_harmonic\_deg} &= 90 \\
\mathrm{apsidal\_n\_minus1\_deg} &= 127.28 \\
\mathrm{precession\_per\_period\_deg} &= -105.44
\end{aligned}
\]