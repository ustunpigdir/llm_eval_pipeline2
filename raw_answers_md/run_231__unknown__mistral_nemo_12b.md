**Solution:**

1. **Radii of event horizon, photon sphere, and ISCO:**

   - **Event Horizon:** The radius of the event horizon is $r_s = 2GM/c^2$. For $M = 10\,M_\odot$, this is:
     \[
     r_s = \frac{2 \times 6.674 \times 10^{-11} \times 10 \times 1.989 \times 10^{30}}{2.998 \times 10^{8}} \approx 29.5 \text{ km}
     \]
   - **Photon Sphere:** The radius of the photon sphere is $3r_s$. So,
     \[
     r_{photon} = 3 \times 29.5 \approx 88.5 \text{ km}
     \]
   - **ISCO:** The ISCO radius is where the specific orbital energy $\mathcal{E}$ and specific angular momentum $l$ are:
     \[
     \mathcal{E} = \frac{1 - \sqrt{6}}{3}, \quad l = \sqrt{12 - 4\sqrt{3}}
     \]
     Solving for $r$ in $\mathcal{E}^2 = 1 - \frac{2GM}{r} - \frac{l^2}{r^2}$, we get:
     \[
     r_{isco} = 6GM/c^2 \approx 6 \times 29.5 \approx 177 \text{ km}
     \]

2. **Orbital frequency at ISCO:**

   Using $\Omega^2 = GM/r^3$ at the ISCO:
   \[
   \Omega^2 = \frac{6.674 \times 10^{-11} \times 10 \times 1.989 \times 10^{30}}{177^3} \approx 1.04 \times 10^{-4} \text{ rad/s}
   \]
   So,
   \[
   f_{orbital} = \frac{\Omega}{2\pi} \approx \frac{1.04 \times 10^{-4}}{2\pi} \approx 16.2 \text{ Hz}
   \]

3. **Dominant GW frequency at ISCO:**

   The dominant GW frequency is $2f_{orbital}$:
   \[
   f_{GW} = 2 \times 16.2 \approx 32.4 \text{ Hz}
   \]

4. **Shutoff of GW signal and ISCO frequency scaling:**

   The GW signal shuts off near the ISCO frequency because the orbital separation decreases, reducing the GW amplitude. The ISCO frequency scales with $M^{-1/2}$:
   \[
   f_{isco} \propto M^{-1/2}
   \]

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{r\_isco\_km} &= 177 \text{ km} \\
\mathrm{f\_orbital\_hz} &= 16.2 \text{ Hz} \\
\mathrm{f\_gw\_hz} &= 32.4 \text{ Hz}
\end{aligned}
\]