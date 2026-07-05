**Derivations and Calculations:**

1. **Radii of Event Horizon, Photon Sphere, and ISCO:**

   - **Event Horizon:** The radius of the event horizon in Schwarzschild coordinates is $r_{EH} = 2GM/c^2$. For $M = 10\,M_\odot$, this is:
     \[
     r_{EH} = \frac{2 \times 6.674 \times 10^{-11} \times 10 \times 1.989 \times 10^{30}}{(2.998 \times 10^{8})^2} \approx 29.5 \text{ km}
     \]

   - **Photon Sphere:** The radius of the photon sphere is $3GM/c^2$. For $M = 10\,M_\odot$, this is:
     \[
     r_{PS} = \frac{3 \times 6.674 \times 10^{-11} \times 10 \times 1.989 \times 10^{30}}{(2.998 \times 10^{8})^2} \approx 88.5 \text{ km}
     \]

   - **ISCO:** The radius of the Innermost Stable Circular Orbit (ISCO) is approximately $6GM/c^2$. For $M = 10\,M_\odot$, this is:
     \[
     r_{ISCO} = \frac{6 \times 6.674 \times 10^{-11} \times 10 \times 1.989 \times 10^{30}}{(2.998 \times 10^{8})^2} \approx 175.5 \text{ km}
     \]

2. **Orbital Frequency at ISCO:**

   Using the relation $\Omega^2 = GM/r^3$, we find the orbital frequency at the ISCO:
   \[
   \Omega = \sqrt{\frac{GM}{r_{ISCO}^3}} = \sqrt{\frac{6.674 \times 10^{-11} \times 10 \times 1.989 \times 10^{30}}{(175.5 \times 10^3)^3}} \approx 1.27 \times 10^3 \text{ rad/s}
   \]
   The orbital frequency in Hz is:
   \[
   f_{orbital} = \frac{\Omega}{2\pi} \approx \frac{1.27 \times 10^3}{2\pi} \approx 202.6 \text{ Hz}
   \]

3. **Dominant Gravitational-Wave Frequency at ISCO:**

   The dominant gravitational-wave emission is at twice the orbital frequency, so:
   \[
   f_{GW} = 2f_{orbital} \approx 2 \times 202.6 \approx 405.2 \text{ Hz}
   \]

4. **Shut-off of GW Signal and ISCO Frequency Scaling:**

   The GW signal from a compact binary shuts off near the ISCO frequency because the binary's orbital separation cannot decrease below the ISCO radius. The ISCO frequency scales with the mass of the black hole as $f_{ISCO} \propto M^{-3/2}$. This is because the ISCO radius scales as $r_{ISCO} \propto M$, and the orbital frequency scales as $f_{ISCO} \propto r_{ISCO}^{-3/2}$.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{r\_isco\_km} &= 175.5 \text{ km} \\
\mathrm{f\_orbital\_hz} &= 202.6 \text{ Hz} \\
\mathrm{f\_gw\_hz} &= 405.2 \text{ Hz}
\end{aligned}
\]