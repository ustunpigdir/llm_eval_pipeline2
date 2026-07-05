To analyze the stability of near-circular orbits and the apsidal angles in central-force motion, we start by considering the given central force \( F(r) = -k r^n \). The apsidal angle \(\Phi\) for nearly circular orbits is given by \(\Phi = \frac{\pi}{\sqrt{3+n}}\).

### Task 1: Verify the formula for \( n = -2 \) and \( n = +1 \)

1. **For \( n = -2 \) (Kepler's law):**
   \[
   \Phi = \frac{\pi}{\sqrt{3 + (-2)}} = \frac{\pi}{\sqrt{1}} = \pi \text{ radians}
   \]
   Converting to degrees:
   \[
   \pi \text{ radians} = 180^\circ
   \]

2. **For \( n = +1 \) (Harmonic oscillator):**
   \[
   \Phi = \frac{\pi}{\sqrt{3 + 1}} = \frac{\pi}{\sqrt{4}} = \frac{\pi}{2} \text{ radians}
   \]
   Converting to degrees:
   \[
   \frac{\pi}{2} \text{ radians} = 90^\circ
   \]

### Task 2: Evaluate \(\Phi\) for \( n = -1 \)

For \( n = -1 \):
\[
\Phi = \frac{\pi}{\sqrt{3 + (-1)}} = \frac{\pi}{\sqrt{2}} \text{ radians}
\]
Converting to degrees:
\[
\frac{\pi}{\sqrt{2}} \text{ radians} \approx 127.28^\circ
\]

### Task 3: Is the orbit closed for \( n = -1 \)?

For the orbit to be closed, the apsidal angle \(\Phi\) must be a rational multiple of \(\pi\). Here, \(\Phi = \frac{\pi}{\sqrt{2}}\) is not a rational multiple of \(\pi\), so the orbit is not closed.

The apsidal precession per radial period is:
\[
2\Phi - 360^\circ = 2 \times 127.28^\circ - 360^\circ \approx 254.56^\circ - 360^\circ = -105.44^\circ
\]

### Task 4: Bertrand's Theorem

Bertrand's theorem states that the only central-force potentials that permit closed orbits are the inverse-square law (Kepler's law) and the harmonic oscillator potential. This theorem is illustrated by our results:
- For \( n = -2 \) (Kepler's law), \(\Phi = 180^\circ\), which is a rational multiple of \(\pi\), leading to closed orbits.
- For \( n = +1 \) (Harmonic oscillator), \(\Phi = 90^\circ\), which is also a rational multiple of \(\pi\), leading to closed orbits.
- For \( n = -1 \), \(\Phi \approx 127.28^\circ\), which is not a rational multiple of \(\pi\), leading to non-closed orbits.

For \( n \le -3 \), the orbits become unstable, and the apsidal angle formula may not hold, leading to non-closed and unstable orbits.

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{apsidal\_kepler\_deg} &= 180 \\
\mathrm{apsidal\_harmonic\_deg} &= 90 \\
\mathrm{apsidal\_n\_minus1\_deg} &= 127.28 \\
\mathrm{precession\_per\_period\_deg} &= -105.44
\end{aligned}
\]