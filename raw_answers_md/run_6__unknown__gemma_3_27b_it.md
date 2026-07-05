Let's analyze the apsidal angle for a central force $F(r) = -k r^{n}$. The apsidal angle $\Phi$ is given by $\Phi = \pi/\sqrt{3+n}$.

1. **Verification against closed-orbit cases:**

   * **Kepler (n = -2):**
     $\Phi = \pi/\sqrt{3 + (-2)} = \pi/\sqrt{1} = \pi$ radians.  Converting to degrees: $\pi \times 180/\pi = 180^\circ$.

   * **Harmonic (n = +1):**
     $\Phi = \pi/\sqrt{3 + 1} = \pi/\sqrt{4} = \pi/2$ radians. Converting to degrees: $(\pi/2) \times 180/\pi = 90^\circ$.

2. **Evaluate $\Phi$ for n = -1:**

   $\Phi = \pi/\sqrt{3 + (-1)} = \pi/\sqrt{2}$ radians. Converting to degrees: $(\pi/\sqrt{2}) \times 180/\pi = 90\sqrt{2} \approx 127.279^\circ$.

3. **Orbit closure and precession for n = -1:**

   For $n = -1$, the force is $F(r) = -k/r$, which is an inverse-square law with a sign change. This is not a central force that allows for closed orbits. The orbit is not closed because the potential is $V(r) = k \ln(r)$, which is not bounded below.  The orbit is not elliptical.

   The apsidal precession per radial period is given by $2\Phi - 360^\circ$.  Since $\Phi \approx 127.279^\circ$, the precession is $2(127.279^\circ) - 360^\circ = 254.558^\circ - 360^\circ = -105.442^\circ$.  This is equivalent to a precession of $360^\circ - 105.442^\circ = 254.558^\circ$.  However, the question asks for the precession *per radial period*.  Since the orbit is not closed, the concept of a radial period is not well-defined.  The apsidal angle is still calculated as $\Phi = \pi/\sqrt{2}$, but it doesn't represent the angle between successive perihelion and aphelion because there are no well-defined perihelion and aphelion.  The precession is the change in the angle of the major axis per orbit.  The given formula for $\Phi$ is still valid for calculating the rate of apsidal precession, even if the orbit isn't closed.  The precession per orbit is $2\Phi - 360^\circ$.

4. **Bertrand's theorem and its illustration:**

   Bertrand's theorem states that the only central force laws for which all initial conditions lead to closed orbits are the inverse-square law ($F \propto 1/r^2$, $n = -2$) and the harmonic oscillator potential ($F \propto r$, $n = +1$).

   Our results illustrate this theorem. For $n = -2$ (Kepler), $\Phi = 180^\circ$, and for $n = +1$ (harmonic), $\Phi = 90^\circ$, both resulting in closed orbits.  For $n = -1$, the orbit is not closed, and we have a precession of approximately $-105.442^\circ$ per orbit.

   For $n \le -3$, the potential $V(r) = -k/(n+1)r^{n+1}$ is unbounded below. This means that the particle can always lower its potential energy by moving closer to the center, and there is no stable orbit. The particle will spiral into the center. The formula for $\Phi$ becomes imaginary for $n < -3$, indicating that the concept of a stable apsidal angle is not applicable.  The derivation of the formula relies on small oscillations around a stable equilibrium point, which does not exist for $n \le -3$.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180 \\
\mathrm{apsidal\_harmonic\_deg} &= 90 \\
\mathrm{apsidal\_n\_minus1\_deg} &= 127.279 \\
\mathrm{precession\_per\_period\_deg} &= -105.442
\end{aligned}
\]