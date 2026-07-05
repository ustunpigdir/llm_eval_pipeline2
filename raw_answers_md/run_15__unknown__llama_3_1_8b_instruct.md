To solve this problem, we need to derive the formula for the apsidal angle $\Phi$ in terms of the force-law exponent $n$.

## Step 1: Derive the formula for the apsidal angle $\Phi$
The apsidal angle $\Phi$ is the angle swept between successive perihelion and aphelion. For a nearly circular orbit, we can use the following equation:

$$\Phi = \frac{2\pi}{\sqrt{3+n}}$$

This equation is derived by considering the time it takes for the particle to complete one orbit, which is given by the period $T$. The period $T$ is related to the angular frequency $\omega$ by $T = 2\pi/\omega$. The angular frequency $\omega$ is related to the force $F$ by $\omega^2 = F/mr$, where $m$ is the mass of the particle and $r$ is the radius of the orbit.

## Step 2: Verify the formula against the two closed-orbit cases
We need to evaluate $\Phi$ for $n = -2$ and $n = +1$ in degrees.

For $n = -2$, we have:

$$\Phi = \frac{2\pi}{\sqrt{3-2}} = \frac{2\pi}{1} = 2\pi \approx 360^\circ$$

For $n = +1$, we have:

$$\Phi = \frac{2\pi}{\sqrt{3+1}} = \frac{2\pi}{2} = \pi \approx 180^\circ$$

## Step 3: Evaluate $\Phi$ in degrees for $n = -1$
We need to evaluate $\Phi$ for $n = -1$ in degrees.

$$\Phi = \frac{2\pi}{\sqrt{3-1}} = \frac{2\pi}{\sqrt{2}} \approx 2.51 \times 2\pi \approx 157.08^\circ$$

## Step 4: Determine if the orbit is closed for $n = -1$
To determine if the orbit is closed, we need to check if the apsidal angle $\Phi$ is equal to $360^\circ$.

Since $\Phi \approx 157.08^\circ$ is not equal to $360^\circ$, the orbit is not closed.

## Step 5: Compute the apsidal precession per radial period for $n = -1$
The apsidal precession per radial period is given by $2\Phi - 360^\circ$.

$$2\Phi - 360^\circ = 2 \times 157.08^\circ - 360^\circ \approx 14.16^\circ$$

## Step 6: State Bertrand's theorem and explain how these results illustrate it
Bertrand's theorem states that the only central force laws that lead to closed orbits are the Kepler force law ($F \propto 1/r^2$) and the harmonic force law ($F \propto r$).

Our results illustrate Bertrand's theorem because we have shown that the apsidal angle $\Phi$ is not equal to $360^\circ$ for $n = -1$, which means that the orbit is not closed. This is consistent with Bertrand's theorem, which states that only the Kepler and harmonic force laws lead to closed orbits.

## Step 7: Explain what goes wrong for $n \le -3$
For $n \le -3$, the force law becomes repulsive, and the particle will not be bound to the central force. As a result, the orbit will not be closed, and the apsidal angle $\Phi$ will not be equal to $360^\circ$.

## FINAL ANSWER

\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 360 \\
\mathrm{apsidal\_harmonic\_deg} &= 180 \\
\mathrm{apsidal\_n\_minus1\_deg} &= 157.08 \\
\mathrm{precession\_per\_period\_deg} &= 14.16
\end{aligned}
\]