Let's solve the problem step by step.

### 1. Radii of the event horizon, the photon sphere, and the ISCO

In Schwarzschild coordinates, the radii are given by:

- Event horizon: \( r_s = \frac{2GM}{c^2} \)
- Photon sphere: \( r_p = 3GM/c^2 \)
- ISCO (Innermost Stable Circular Orbit): \( r_{isco} = 6GM/c^2 \)

Given \( M = 10 M_\odot \) and \( M_\odot = 1.989 \times 10^{30} \) kg, we can calculate \( GM/c^2 \):

\[
\frac{GM}{c^2} = \frac{6.674 \times 10^{-11} \times 10 \times 1.989 \times 10^{30}}{(2.998 \times 10^8)^2} = \frac{6.674 \times 10^{-11} \times 1.989 \times 10^{31}}{8.988 \times 10^{16}} \approx 1.485 \times 10^4 \, \text{m} = 14.85 \, \text{km}
\]

Now, we can find the radii:

- Event horizon: \( r_s = 2 \times 14.85 \, \text{km} = 29.7 \, \text{km} \)
- Photon sphere: \( r_p = 3 \times 14.85 \, \text{km} = 44.55 \, \text{km} \)
- ISCO: \( r_{isco} = 6 \times 14.85 \, \text{km} = 89.1 \, \text{km} \)

### 2. Orbital frequency at the ISCO

The orbital frequency \( \Omega \) is given by \( \Omega^2 = GM/r^3 \). At the ISCO, \( r = 6GM/c^2 \), so:

\[
\Omega^2 = \frac{GM}{(6GM/c^2)^3} = \frac{c^6}{36G^3M^2}
\]

Taking the square root:

\[
\Omega = \frac{c^3}{6\sqrt{6}G^{3/2}M}
\]

The orbital frequency \( f \) is \( \Omega/2\pi \):

\[
f = \frac{\Omega}{2\pi} = \frac{c^3}{12\sqrt{6}\pi G^{3/2}M}
\]

Substituting the values:

\[
f = \frac{(2.998 \times 10^8)^3}{12\sqrt{6}\pi (6.674 \times 10^{-11})^{3/2} \times 10 \times 1.989 \times 10^{30}}
\]

First, calculate the denominator:

\[
(6.674 \times 10^{-11})^{3/2} = (6.674 \times 10^{-11})^{1.5} \approx 2.546 \times 10^{-16}
\]

Now, the denominator becomes:

\[
12\sqrt{6}\pi \times 2.546 \times 10^{-16} \times 10 \times 1.989 \times 10^{30} \approx 12 \times 2.449 \times 2.546 \times 10^{-16} \times 1.989 \times 10^{31}
\]

\[
\approx 12 \times 2.449 \times 2.546 \times 1.989 \times 10^{15} \approx 147.6 \times 10^{15} \approx 1.476 \times 10^{17}
\]

Now, the numerator:

\[
(2.998 \times 10^8)^3 \approx 2.691 \times 10^{25}
\]

So,

\[
f \approx \frac{2.691 \times 10^{25}}{1.476 \times 10^{17}} \approx 1.823 \times 10^8 \, \text{Hz}
\]

### 3. Dominant gravitational-wave frequency at the ISCO

The dominant gravitational-wave frequency \( f_{GW} \) is twice the orbital frequency:

\[
f_{GW} = 2f \approx 2 \times 1.823 \times 10^8 \, \text{Hz} \approx 3.646 \times 10^8 \, \text{Hz}
\]

### 4. Explanation

The gravitational-wave signal 'shuts off' near the ISCO because the orbit becomes unstable, and the particle plunges into the black hole. The ISCO frequency scales with \( M \) as \( f \propto M^{-1} \), because \( f \propto \frac{c^3}{G^{3/2}M} \).

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{r\_isco\_km} &= 89.1 \\
\mathrm{f\_orbital\_hz} &= 1.823 \times 10^8 \\
\mathrm{f\_gw\_hz} &= 3.646 \times 10^8
\end{aligned}
\]