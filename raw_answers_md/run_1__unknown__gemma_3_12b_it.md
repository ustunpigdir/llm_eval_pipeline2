Okay, let's analyze the central-force motion and apsidal angles.

**1. Verification for Kepler (n = -2) and Harmonic (n = +1)**

The given formula for the apsidal angle is $\Phi = \pi/\sqrt{3+n}$.

For $n = -2$ (Kepler):
$\Phi = \pi/\sqrt{3+(-2)} = \pi/\sqrt{1} = \pi$ radians.
Converting to degrees: $\Phi = \pi \times (180/\pi) = 180^\circ$.

For $n = +1$ (Harmonic):
$\Phi = \pi/\sqrt{3+1} = \pi/\sqrt{4} = \pi/2$ radians.
Converting to degrees: $\Phi = (\pi/2) \times (180/\pi) = 90^\circ$.

**2. Evaluation for n = -1**

For $n = -1$ (inverse square law):
$\Phi = \pi/\sqrt{3+(-1)} = \pi/\sqrt{2}$ radians.
Converting to degrees: $\Phi = (\pi/\sqrt{2}) \times (180/\pi) = 180/\sqrt{2} = 90\sqrt{2} \approx 127.28^\circ$.

**3. Orbit Closure and Precession for n = -1**

For $n = -1$, the orbit is *not* closed. Bertrand's theorem (stated later) will explain why.  The apsidal precession per radial period is given by $2\Phi - 360^\circ$.

$2\Phi - 360^\circ = 2(180/\sqrt{2}) - 360^\circ = 360/\sqrt{2} - 360^\circ = 360(1/\sqrt{2} - 1) \approx 360(0.7071 - 1) = 360(-0.2929) \approx -105.44^\circ$.

**4. Bertrand's Theorem and Implications**

Bertrand's theorem states that for a central force $F(r) = -k r^n$, where $k$ is a constant, the orbit is closed (i.e., conic section) if and only if $n = -2$.  In other words, only for Kepler's inverse-square law do we get closed orbits (ellipses, parabolas, or hyperbolas).

The given formula for $\Phi$ is derived under the assumption of near-circular orbits.  For $n = -2$, $\Phi = 180^\circ$, which implies no precession (a perfect circle). For $n = +1$, $\Phi = 90^\circ$, and for $n = -1$, $\Phi \approx 127.28^\circ$.

What goes wrong for $n \le -3$?  Bertrand's theorem tells us that for $n \le -3$, the motion is not bounded. The particle escapes to infinity.  The formula for $\Phi$ is derived assuming bounded orbits.  When $n \le -3$, the potential energy goes to infinity as $r$ approaches zero, and the particle's energy is not sufficient to keep it bound.  Therefore, the concept of apsidal angle and precession becomes meaningless because the orbit is not a closed curve.  The formula is invalid because the assumptions of bounded, near-circular orbits are violated.

\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180 \\
\mathrm{apsidal\_harmonic\_deg} &= 90 \\
\mathrm{apsidal\_n\_minus1\_deg} &= 127.28 \\
\mathrm{precession\_per\_period\_deg} &= -105.44
\end{aligned}
\]