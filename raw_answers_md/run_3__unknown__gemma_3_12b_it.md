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

For $n = -1$, the orbit is *not* closed. Bertrand's theorem (stated later) will explain why.  The apsidal precession per radial period is given by $2\Phi - 360^\circ$.

$2\Phi - 360^\circ = 2 \times \frac{180}{\sqrt{2}} - 360^\circ = \frac{360}{\sqrt{2}} - 360^\circ = 360^\circ (\frac{1}{\sqrt{2}} - 1) \approx 360^\circ (0.707 - 1) = -127.28^\circ$.
The negative sign indicates that the apses (perihelion and aphelion) rotate in the opposite direction to what would be expected for a closed orbit.

**4. Bertrand's Theorem and Implications**

Bertrand's theorem states that for a central force $F(r) = -k r^n$, the orbit is closed (i.e., periodic) if and only if $n = -2$.  In other words, only Kepler's inverse-square law produces closed orbits.

The given formula for $\Phi$ is derived under the assumption of *nearly* circular orbits.  This means we are considering small deviations from a circular orbit.  For $n = -2$, the apsidal angle is $\Phi = 180^\circ$, which implies no precession (the orbit is closed). For $n = +1$, $\Phi = 90^\circ$, and for $n = -1$, $\Phi \approx 127.28^\circ$.  These values demonstrate that orbits are not closed for $n \neq -2$.

What goes wrong for $n \le -3$?  Bertrand's theorem tells us that for $n \le -3$, the orbits are *wild*. They are not closed, and they are not even periodic. The particle's energy is not conserved, and the orbit spirals outwards. The formula $\Phi = \pi/\sqrt{3+n}$ is not valid in this regime because the assumption of a "nearly circular" orbit breaks down completely. The particle escapes to infinity. The concept of an apsidal angle becomes meaningless as the orbit is not bounded.

\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180 \\
\mathrm{apsidal\_harmonic\_deg} &= 90 \\
\mathrm{apsidal\_n\_minus1\_deg} &= 127.28 \\
\mathrm{precession\_per\_period\_deg} &= -127.28
\end{aligned}
\]