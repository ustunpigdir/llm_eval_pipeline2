**1. Radii of the event horizon, photon sphere, and ISCO**

- **Event Horizon**: The radius of the event horizon in Schwarzschild coordinates is $r_{EH} = 2GM/c^2$. For $M = 10\,M_\odot$, this is:
  \[
  r_{EH} = \frac{2 \times 6.674 \times 10^{-11} \times 10 \times 1.989 \times 10^{30}}{(2.998 \times 10^{8})^2} \approx 29.5 \text{ km}
  \]

- **Photon Sphere**: The radius of the photon sphere is $3GM/c^2$. For $M = 10\,M_\odot$, this is:
  \[
  r_{PS} = \frac{3 \times 6.674 \times 10^{-11} \times 10 \times 1.989 \times 10^{30}}{(2.998 \times 10^{8})^2} \approx 88.5 \text{ km}
  \]

- **ISCO**: The radius of the Innermost Stable Circular Orbit (ISCO) is $6GM/c^2$. For $M = 10\,M_\odot$, this is:
  \[
  r_{ISCO} = \frac{6 \times 6.674 \times 10^{-11} \times 10 \times 1.989 \times 10^{30}}{(2.998 \times 10^{8})^2} \approx 175.5 \text{ km}
  \]

**2. Orbital frequency at the ISCO**

Using the relation $\Omega^2 = GM/r^3$, we find the orbital frequency at the ISCO:
\[
\Omega = \sqrt{\frac{GM}{r_{ISCO}^3}} = \sqrt{\frac{6.674 \times 10^{-11} \times 10 \times 1.989 \times 10^{30}}{(175.5 \times 10^3)^3}} \approx 125.5 \text{ Hz}
\]
Thus, the orbital frequency $f = \Omega/2\pi \approx 20.08 \text{ Hz}$.

**3. Dominant gravitational-wave emission frequency**

The dominant gravitational-wave emission frequency is twice the orbital frequency:
\[
f_{GW} = 2f = 2 \times 20.08 \approx 40.16 \text{ Hz}
\]

**4. Shut-off of GW signal and ISCO frequency scaling**

The GW signal from a compact binary shuts off near the ISCO frequency because the binary's orbital energy and angular momentum decrease as it inspirals, leading to a decrease in the GW emission. The ISCO frequency scales with $M^{-1}$ because the orbital frequency is inversely proportional to the orbital radius, which in turn scales with $M$.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{r\_isco\_km} &= 175.5 \text{ km} \\
\mathrm{f\_orbital\_hz} &= 20.08 \text{ Hz} \\
\mathrm{f\_gw\_hz} &= 40.16 \text{ Hz}
\end{aligned}
\]