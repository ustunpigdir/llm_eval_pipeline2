Let's analyze the apsidal angle for a central force $F(r) = -k r^{n}$. The apsidal angle $\Phi$ is given by $\Phi = \pi/\sqrt{3+n}$.

1. **Verification against closed-orbit cases:**

   * **Kepler (n = -2):**
     $\Phi = \pi/\sqrt{3 + (-2)} = \pi/\sqrt{1} = \pi$ radians.
     In degrees, $\Phi = \pi \times 180/\pi = 180^\circ$.

   * **Harmonic (n = +1):**
     $\Phi = \pi/\sqrt{3 + 1} = \pi/\sqrt{4} = \pi/2$ radians.
     In degrees, $\Phi = (\pi/2) \times 180/\pi = 90^\circ$.

2. **Evaluation for n = -1:**
   $\Phi = \pi/\sqrt{3 + (-1)} = \pi/\sqrt{2}$ radians.
   In degrees, $\Phi = (\pi/\sqrt{2}) \times 180/\pi = 180/\sqrt{2} = 90\sqrt{2} \approx 127.279^\circ$.

3. **Orbit closure and precession for n = -1:**

   For $n = -1$, the force is $F(r) = -k/r$, which is an inverse-square law with a sign change. This is not a typical central force problem because the potential is not well-defined (it diverges as $r \to 0$). However, we can still analyze the apsidal precession using the given formula.

   The orbit is *not* closed for $n = -1$. The apsidal angle is $\Phi \approx 127.279^\circ$.  A closed orbit requires $\Phi = 180^\circ$ (Kepler) or $\Phi = 90^\circ$ (harmonic).

   The apsidal precession per radial period is given by $2\Phi - 360^\circ$.
   Precession per period = $2(127.279^\circ) - 360^\circ = 254.558^\circ - 360^\circ = -105.442^\circ$.
   Since we are interested in the amount of precession, we can take the absolute value or consider the precession as a positive quantity.  The precession is $105.442^\circ$ per radial period.

4. **Bertrand's Theorem and its illustration:**

   Bertrand's theorem states that the only central force laws for which all initial conditions yield bounded orbits are the inverse-square law ($n = -2$) and the linear restoring force ($n = +1$).  In other words, these are the only two force laws that guarantee that orbits will not escape to infinity.

   Our results illustrate this theorem. For $n = -2$ (Kepler), we have a closed orbit with $\Phi = 180^\circ$. For $n = +1$ (harmonic), we have a closed orbit with $\Phi = 90^\circ$.  For $n = -1$, the orbit is not closed, and there is apsidal precession.  This indicates that the orbit is not as stable as the Kepler or harmonic cases.

   For $n \le -3$, the potential energy becomes unbounded from below, meaning that there is no minimum energy state.  The particle can escape to infinity even with zero initial energy. The formula $\Phi = \pi/\sqrt{3+n}$ becomes invalid because the derivation relies on a small eccentricity approximation, which breaks down for highly unstable orbits.  The square root becomes imaginary for $n < -3$, indicating that the formula is not applicable.  The orbits are not bounded, and the concept of a well-defined apsidal angle loses its meaning.

\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180 \\
\mathrm{apsidal\_harmonic\_deg} &= 90 \\
\mathrm{apsidal\_n\_minus1\_deg} &= 127.279 \\
\mathrm{precession\_per\_period\_deg} &= -105.442
\end{aligned}
\]