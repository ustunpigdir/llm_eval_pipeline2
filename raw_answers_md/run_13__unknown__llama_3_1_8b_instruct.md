## Step 1: Verify the formula against the two closed-orbit cases
To verify the formula, we need to evaluate $\Phi$ for $n = -2$ and $n = +1$.

For $n = -2$, we have $\Phi = \pi/\sqrt{3-2} = \pi/\sqrt{1} = \pi$.

To convert $\pi$ to degrees, we multiply by $180/\pi$, so $\Phi = \pi \cdot 180/\pi = 180$ degrees.

For $n = +1$, we have $\Phi = \pi/\sqrt{3+1} = \pi/\sqrt{4} = \pi/2$.

To convert $\pi/2$ to degrees, we multiply by $180/\pi$, so $\Phi = \pi/2 \cdot 180/\pi = 90$ degrees.

## Step 2: Evaluate $\Phi$ in degrees for $n = -1$
For $n = -1$, we have $\Phi = \pi/\sqrt{3-1} = \pi/\sqrt{2}$.

To convert $\pi/\sqrt{2}$ to degrees, we multiply by $180/\pi$, so $\Phi = \pi/\sqrt{2} \cdot 180/\pi = 180/\sqrt{2} = 101.91$ degrees.

## Step 3: For $n = -1$, is the orbit closed? Compute the apsidal precession per radial period, $2\Phi - 360^\circ$, in degrees
Since $\Phi = 101.91$ degrees, we have $2\Phi = 203.82$ degrees.

The apsidal precession per radial period is $2\Phi - 360^\circ = 203.82 - 360 = -156.18$ degrees.

## Step 4: State Bertrand's theorem and explain how these results illustrate it
Bertrand's theorem states that the only central force laws that lead to closed orbits are the Kepler force law ($F \propto 1/r^2$) and the harmonic force law ($F \propto r$).

The results illustrate Bertrand's theorem because the only closed orbits occur for $n = -2$ and $n = +1$, which are the Kepler and harmonic force laws, respectively.

For $n \le -3$, the force law is not strong enough to keep the orbit closed, and the apsidal angle is not defined.

## Step 5: Final Answer
\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180 \\
\mathrm{apsidal\_harmonic\_deg} &= 90 \\
\mathrm{apsidal\_n\_minus1\_deg} &= 101.91 \\
\mathrm{precession\_per\_period\_deg} &= -156.18
\end{aligned}
\]

FINAL ANSWER

\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180 \\
\mathrm{apsidal\_harmonic\_deg} &= 90 \\
\mathrm{apsidal\_n\_minus1\_deg} &= 101.91 \\
\mathrm{precession\_per\_period\_deg} &= -156.18
\end{aligned}
\]