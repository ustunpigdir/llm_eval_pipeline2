## Step 1: Verify the formula against the two closed-orbit cases
To verify the formula for the apsidal angle $\Phi = \pi/\sqrt{3+n}$, we need to evaluate it for $n = -2$ and $n = +1$.

For $n = -2$, we have $\Phi = \pi/\sqrt{3-2} = \pi/\sqrt{1} = \pi$ radians. To convert this to degrees, we multiply by $180/\pi$, so $\Phi = 180^\circ$.

For $n = +1$, we have $\Phi = \pi/\sqrt{3+1} = \pi/\sqrt{4} = \pi/2$ radians. To convert this to degrees, we multiply by $180/\pi$, so $\Phi = 90^\circ$.

## Step 2: Evaluate $\Phi$ in degrees for $n = -1$
For $n = -1$, we have $\Phi = \pi/\sqrt{3-1} = \pi/\sqrt{2}$ radians. To convert this to degrees, we multiply by $180/\pi$, so $\Phi = 63.435^\circ$.

## Step 3: For $n = -1$, is the orbit closed? Compute the apsidal precession per radial period, $2\Phi - 360^\circ$, in degrees
Since the orbit is not closed, we cannot compute the apsidal precession per radial period. However, we can compute the apsidal precession per radial period in degrees as $2\Phi - 360^\circ = 2(63.435^\circ) - 360^\circ = -267.9^\circ$.

## Step 4: State Bertrand's theorem and explain how these results illustrate it
Bertrand's theorem states that the only central force laws that lead to closed orbits are the inverse square law ($n = -2$) and the harmonic law ($n = +1$). The results we obtained for $n = -2$ and $n = +1$ illustrate this theorem, as we obtained closed orbits for these values of $n$. For $n = -1$, the orbit is not closed, illustrating that this force law does not lead to closed orbits.

## Step 5: What goes wrong for $n \le -3$?
For $n \le -3$, the force law is not a central force law, as it would lead to a force that is not a function of the distance from the center. Therefore, the formula for the apsidal angle is not applicable for these values of $n$.

## Step 6: FINAL ANSWER
\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180 \\
\mathrm{apsidal\_harmonic\_deg} &= 90 \\
\mathrm{apsidal\_n\_minus1\_deg} &= 63.435 \\
\mathrm{precession\_per\_period\_deg} &= -267.9
\end{aligned}
\]