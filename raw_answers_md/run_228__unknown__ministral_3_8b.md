### Solution

#### 1. Radii of the event horizon, photon sphere, and ISCO in units of \(GM/c^2\), and ISCO radius in km

In Schwarzschild geometry, the following radii are defined in terms of \(GM/c^2\):

- **Event horizon radius (\(r_s\))**:
  The event horizon occurs at the radius where the metric coefficient \(g_{tt} = -(1 - 2GM/rc^2)\) vanishes. Thus,
  \[
  r_s = \frac{2GM}{c^2}.
  \]
  In units of \(GM/c^2\), this is simply \(r_s = 2\).

- **Photon sphere radius (\(r_{ph}\))**:
  The photon sphere is the radius where light can orbit the black hole in a circular path. For Schwarzschild geometry, this occurs at
  \[
  r_{ph} = \frac{3GM}{c^2}.
  \]
  In units of \(GM/c^2\), this is \(r_{ph} = 3\).

- **ISCO radius (\(r_{isco}\))**:
  The Innermost Stable Circular Orbit (ISCO) is the smallest radius at which a test particle can orbit stably in the Schwarzschild metric. For circular orbits in Schwarzschild geometry, the effective potential for radial motion has a minimum at
  \[
  r_{isco} = 6GM/c^2.
  \]
  In units of \(GM/c^2\), this is \(r_{isco} = 6\).

Now, we evaluate the ISCO radius in km for \(M = 10M_\odot\):

Given:
\[
M = 10M_\odot = 10 \times 1.989 \times 10^{30} \text{ kg} = 1.989 \times 10^{31} \text{ kg},
\]
\[
G = 6.674 \times 10^{-11} \text{ m}^3 \text{ kg}^{-1} \text{ s}^{-2},
\]
\[
c = 2.998 \times 10^8 \text{ m/s}.
\]

Compute \(GM/c^2\):
\[
\frac{GM}{c^2} = \frac{6.674 \times 10^{-11} \times 1.989 \times 10^{31}}{(2.998 \times 10^8)^2}.
\]

Calculate the denominator:
\[
(2.998 \times 10^8)^2 = 8.988 \times 10^{16}.
\]

Calculate the numerator:
\[
6.674 \times 1.989 \times 10^{20} = 1.327 \times 10^{21}.
\]

Thus,
\[
\frac{GM}{c^2} = \frac{1.327 \times 10^{21}}{8.988 \times 10^{16}} = 1.477 \times 10^4 \text{ m} = 1.477 \times 10^1 \text{ km} = 14.77 \text{ km}.
\]

Now, the ISCO radius is:
\[
r_{isco} = 6 \times \frac{GM}{c^2} = 6 \times 14.77 \text{ km} = 88.62 \text{ km}.
\]

#### 2. Orbital frequency \(f = \Omega/2\pi\) at the ISCO in Hz

The problem states that for circular orbits in Schwarzschild coordinates, the exact relation is
\[
\Omega^2 = \frac{GM}{r^3}.
\]

At the ISCO, \(r = r_{isco} = 6GM/c^2\). Substituting this into the equation for \(\Omega^2\):
\[
\Omega^2 = \frac{GM}{(6GM/c^2)^3} = \frac{GM}{216 (GM/c^2)^3} = \frac{c^6}{216 G^2 M^2}.
\]

Taking the square root:
\[
\Omega = \frac{c^3}{6 \sqrt{6} G M}.
\]

Now, compute the orbital frequency \(f = \Omega / 2\pi\):
\[
f = \frac{c^3}{12 \sqrt{6} \pi G M}.
\]

Substitute the values:
\[
f = \frac{(2.998 \times 10^8)^3}{12 \sqrt{6} \pi \times 6.674 \times 10^{-11} \times 1.989 \times 10^{31}}.
\]

Calculate the numerator:
\[
(2.998 \times 10^8)^3 = 2.693 \times 10^{25}.
\]

Calculate the denominator:
\[
12 \sqrt{6} \pi \times 6.674 \times 10^{-11} \times 1.989 \times 10^{31}.
\]

First, compute \(\sqrt{6} \approx 2.449\):
\[
12 \times 2.449 \times \pi \approx 12 \times 2.449 \times 3.1416 \approx 94.9.
\]

Now multiply by the rest:
\[
94.9 \times 6.674 \times 10^{-11} \times 1.989 \times 10^{31} = 94.9 \times 1.327 \times 10^{21} = 1.255 \times 10^{23}.
\]

Thus,
\[
f = \frac{2.693 \times 10^{25}}{1.255 \times 10^{23}} = 214.6 \text{ Hz}.
\]

#### 3. Dominant gravitational-wave emission frequency \(f_{GW}\)

The dominant gravitational-wave emission frequency is at twice the orbital frequency:
\[
f_{GW} = 2f = 2 \times 214.6 \text{ Hz} = 429.2 \text{ Hz}.
\]

#### 4. Explanation of why the GW signal 'shuts off' near this frequency and scaling of ISCO frequency with \(M\)

- **Why the GW signal 'shuts off' near this frequency**:
  As a compact binary system inspiral, the orbital frequency increases due to energy loss via gravitational radiation. The ISCO represents the smallest stable orbit around a black hole. When the binary reaches the ISCO, the orbital frequency reaches its maximum stable value. Beyond this point, the orbits are unstable, and the binary merges directly into the black hole. Thus, the GW signal 'shuts off' because the stable orbital motion ceases, and the system transitions to a merger phase.

- **Scaling of ISCO frequency with \(M\)**:
  From the expression for \(f\):
  \[
  f \propto \frac{1}{M}.
  \]
  This means that for a larger black hole mass \(M\), the ISCO frequency is lower, and for a smaller black hole mass, the ISCO frequency is higher.

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{r\_isco\_km} &= 88.62 \\
\mathrm{f\_orbital\_hz} &= 214.6 \\
\mathrm{f\_gw\_hz} &= 429.2 \\
\end{aligned}
\]