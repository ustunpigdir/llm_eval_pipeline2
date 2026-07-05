### Solution

#### 1. Radii of the event horizon, photon sphere, and ISCO in units of \(GM/c^2\), and ISCO radius in km

In Schwarzschild geometry, the following radii are defined in terms of \(GM/c^2\):

- **Event horizon radius** (\(r_H\)):
  The event horizon occurs at the Schwarzschild radius, where \(r_H = 2GM/c^2\).

- **Photon sphere radius** (\(r_{ph}\)):
  The photon sphere is the unstable circular orbit for photons, located at \(r_{ph} = 3GM/c^2\).

- **ISCO radius** (\(r_{ISCO}\)):
  For a Schwarzschild black hole, the innermost stable circular orbit (ISCO) is at \(r_{ISCO} = 6GM/c^2\).

Now, we compute the numerical value of \(r_{ISCO}\) in km for \(M = 10M_\odot\):

Given:
- \(M_\odot = 1.989 \times 10^{30}\) kg,
- \(G = 6.674 \times 10^{-11}\) SI,
- \(c = 2.998 \times 10^8\) m/s.

First, compute \(GM/c^2\) for \(M = 10M_\odot\):

\[
GM = (10 \times 1.989 \times 10^{30} \, \text{kg}) \times (6.674 \times 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2})
= 1.322 \times 10^{28} \, \text{m}^3 \text{s}^{-2}
\]

\[
\frac{GM}{c^2} = \frac{1.322 \times 10^{28} \, \text{m}^3 \text{s}^{-2}}{(2.998 \times 10^8 \, \text{m/s})^2}
= \frac{1.322 \times 10^{28}}{8.988 \times 10^{16}} \, \text{m}
= 1.471 \times 10^3 \, \text{m}
\]

Now, multiply by \(6\) to get \(r_{ISCO}\):

\[
r_{ISCO} = 6 \times 1.471 \times 10^3 \, \text{m} = 8.826 \times 10^3 \, \text{m} = 8.826 \, \text{km}
\]

#### 2. Orbital frequency \(f = \Omega/2\pi\) at the ISCO in Hz

The orbital frequency \(\Omega\) for circular orbits in Schwarzschild coordinates is given by:

\[
\Omega^2 = \frac{GM}{r^3}
\]

At \(r = r_{ISCO} = 6GM/c^2\), we have:

\[
\Omega^2 = \frac{GM}{(6GM/c^2)^3} = \frac{GM}{216 (GM/c^2)^3} = \frac{c^6}{216 G^2 M^2}
\]

Taking the square root:

\[
\Omega = \frac{c^3}{6 \sqrt{6} G M}
\]

Now, compute \(\Omega\) numerically:

\[
\Omega = \frac{(2.998 \times 10^8 \, \text{m/s})^3}{6 \sqrt{6} \times (6.674 \times 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2}) \times (1.322 \times 10^{28} \, \text{kg} \cdot \text{m}^3 \text{s}^{-2})}
\]

First, compute the denominator:

\[
6 \sqrt{6} \approx 6 \times 2.449 = 14.695
\]

\[
6 \sqrt{6} \times G \times M = 14.695 \times 6.674 \times 10^{-11} \times 1.322 \times 10^{28}
\]

\[
= 14.695 \times 8.84 \times 10^{17} \approx 1.301 \times 10^{19}
\]

Now, compute \(\Omega\):

\[
\Omega = \frac{2.687 \times 10^{25}}{1.301 \times 10^{19}} \approx 2.066 \times 10^6 \, \text{rad/s}
\]

Finally, compute the frequency \(f = \Omega / 2\pi\):

\[
f = \frac{2.066 \times 10^6}{2 \times 3.1416} \approx 3.29 \times 10^5 \, \text{Hz}
\]

#### 3. Dominant gravitational-wave emission frequency \(f_{GW}\)

The dominant gravitational-wave emission frequency is at twice the orbital frequency:

\[
f_{GW} = 2f = 2 \times 3.29 \times 10^5 \, \text{Hz} = 6.58 \times 10^5 \, \text{Hz}
\]

#### 4. Why the GW signal 'shuts off' near this frequency and how the ISCO frequency scales with \(M\)

- **Why the GW signal shuts off near the ISCO frequency:**
  The ISCO is the innermost stable orbit. When the binary system's separation reaches the ISCO, the orbital motion becomes unstable, and the two objects cannot maintain a stable orbit. The system merges, and the gravitational-wave signal abruptly changes character (e.g., from quasi-periodic to a more complex waveform). This is why the GW signal "shuts off" near this frequency.

- **Scaling of the ISCO frequency with \(M\):**
  From the expression for \(\Omega\):

  \[
  \Omega \propto \frac{1}{M}
  \]

  Thus, the orbital frequency \(f = \Omega / 2\pi\) scales as:

  \[
  f \propto \frac{1}{M}
  \]

  This means that for larger black holes, the ISCO frequency is lower, and for smaller black holes, it is higher.

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{r\_isco\_km} &= 8.826 \\
\mathrm{f\_orbital\_hz} &= 3.29 \times 10^5 \\
\mathrm{f\_gw\_hz} &= 6.58 \times 10^5 \\
\end{aligned}
\]