### Solution

We work in Schwarzschild coordinates, where the exact relation for circular orbits is
\[
\Omega^2 = \frac{GM}{r^3}.
\]

---

#### 1. Key radii in units of \(GM/c^2\)

- **Event horizon radius** \(r_H\):
  In Schwarzschild geometry, the horizon is at \(r_H = 2GM/c^2\).

- **Photon sphere radius** \(r_{ph}\):
  The photon sphere is the unstable circular null geodesic, located at \(r_{ph} = 3GM/c^2\).

- **ISCO radius** \(r_{ISCO}\):
  For a Schwarzschild black hole, the innermost stable circular orbit (ISCO) is at \(r_{ISCO} = 6GM/c^2\).

---

#### 2. Numerical evaluation of \(r_{ISCO}\) in km

Given:
\[
M = 10\,M_\odot = 10 \times 1.989\times10^{30}\,\mathrm{kg} = 1.989\times10^{31}\,\mathrm{kg},
\]
\[
G = 6.674\times10^{-11}\,\mathrm{m^3\,kg^{-1}\,s^{-2}},
\]
\[
c = 2.998\times10^{8}\,\mathrm{m/s}.
\]

Compute \(GM/c^2\):
\[
\frac{GM}{c^2}
= \frac{6.674\times10^{-11} \times 1.989\times10^{31}}{(2.998\times10^{8})^2}
\approx 4.926\times10^{3}\,\mathrm{m}.
\]

Thus,
\[
r_{ISCO} = 6\,\frac{GM}{c^2} = 6 \times 4.926\times10^{3}\,\mathrm{m} = 2.956\times10^{4}\,\mathrm{m} = 2.956\times10^{1}\,\mathrm{km}.
\]

---

#### 3. Orbital frequency \(f = \Omega/2\pi\) at the ISCO

Using \(\Omega^2 = GM/r^3\) with \(r = r_{ISCO} = 6GM/c^2\):
\[
\Omega^2 = \frac{GM}{(6GM/c^2)^3} = \frac{GM \cdot c^6}{216\,(GM)^3} = \frac{c^6}{216\,G^2\,M^2}.
\]
Taking the square root:
\[
\Omega = \frac{c^3}{6\sqrt{6}\,GM}.
\]

Convert to frequency \(f = \Omega/2\pi\):
\[
f = \frac{c^3}{12\sqrt{6}\,\pi\,GM}.
\]

Substitute numerical values:
\[
f = \frac{(2.998\times10^{8})^3}{12\sqrt{6}\,\pi\,(6.674\times10^{-11})(1.989\times10^{31})}.
\]

Calculate denominator:
\[
12\sqrt{6}\,\pi\,(6.674\times10^{-11})(1.989\times10^{31})
\approx 12 \times 2.449 \times 3.1416 \times 1.328\times10^{20}
\approx 1.257\times10^{22}.
\]

Calculate numerator:
\[
(2.998\times10^{8})^3 \approx 2.704\times10^{25}.
\]

Thus,
\[
f \approx \frac{2.704\times10^{25}}{1.257\times10^{22}} \approx 2.152\times10^{3}\,\mathrm{Hz}.
\]

---

#### 4. Dominant gravitational‐wave frequency \(f_{GW}\)

The dominant GW emission is at twice the orbital frequency:
\[
f_{GW} = 2f = 2 \times 2.152\times10^{3}\,\mathrm{Hz} = 4.304\times10^{3}\,\mathrm{Hz}.
\]

---

#### 5. Why the GW signal “shuts off” near this frequency

- **ISCO as the last stable orbit**: At the ISCO, the orbit is the innermost stable circular orbit. Inside this radius, circular orbits are unstable, and matter or radiation cannot remain in a stable orbit. The binary system cannot inspiral further in a stable fashion, so the GW signal (which is powered by the orbital energy loss) ceases when the orbit reaches the ISCO.
- **Frequency scaling with mass**: The orbital frequency at the ISCO scales as \(f \propto M^{-1}\) (from \(\Omega \propto M^{-1}\)). This is because the ISCO radius is fixed at \(6GM/c^2\), and the orbital frequency \(\Omega = \sqrt{GM/r^3}\) depends inversely on the mass.

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{r\_isco\_km} &= 2.956\times10^{1}, \\
\mathrm{f\_orbital\_hz} &= 2.152\times10^{3}, \\
\mathrm{f\_gw\_hz} &= 4.304\times10^{3}.
\end{aligned}
\]