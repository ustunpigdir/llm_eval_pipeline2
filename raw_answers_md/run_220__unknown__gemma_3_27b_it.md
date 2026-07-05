Here's the solution to the Schwarzschild orbital mechanics problem, following the specified conventions and requirements.

**1. Radii of Event Horizon, Photon Sphere, and ISCO**

*   **Event Horizon:** The event horizon radius is given by $r_s = 2GM/c^2$.  In units of $GM/c^2$, this is $r_s = 2 \times (GM/c^2)$.
*   **Photon Sphere:** The photon sphere radius is given by $r_p = 3GM/c^2$. In units of $GM/c^2$, this is $r_p = 3 \times (GM/c^2)$.
*   **ISCO (Innermost Stable Circular Orbit):** For a non-rotating Schwarzschild black hole, the ISCO is at $r_{ISCO} = 6GM/c^2$. In units of $GM/c^2$, this is $r_{ISCO} = 6 \times (GM/c^2)$.

Now, let's calculate the ISCO radius in km.

$M = 10\,M_\odot = 10 \times 1.989 \times 10^{30} \text{ kg} = 1.989 \times 10^{31} \text{ kg}$
$GM = (6.674 \times 10^{-11} \text{ SI})(1.989 \times 10^{31} \text{ kg}) = 1.327 \times 10^{21} \text{ m}^3\text{/s}^2$
$c^2 = (2.998 \times 10^8 \text{ m/s})^2 = 8.988 \times 10^{16} \text{ m}^2\text{/s}^2$
$GM/c^2 = (1.327 \times 10^{21} \text{ m}^3\text{/s}^2) / (8.988 \times 10^{16} \text{ m}^2\text{/s}^2) = 1.477 \times 10^4 \text{ m} = 14.77 \text{ km}$
$r_{ISCO} = 6 \times (GM/c^2) = 6 \times 14.77 \text{ km} = 88.62 \text{ km}$

**2. Orbital Frequency at the ISCO**

We are given that $\Omega^2 = GM/r^3$ for circular orbits in Schwarzschild coordinates.  At the ISCO, $r = 6GM/c^2$. Therefore:

$\Omega^2 = GM / (6GM/c^2)^3 = GM / (216 (GM)^3 / c^6) = c^6 / (216 (GM)^2)$
$\Omega = c^3 / (6\sqrt{6} GM)$
The orbital frequency is $f = \Omega / 2\pi = c^3 / (12\pi\sqrt{6} GM)$.

Let's calculate the value:
$f = (2.998 \times 10^8)^3 / (12\pi\sqrt{6} \times 1.327 \times 10^{21}) = 2.695 \times 10^{25} / (1.25 \times 10^{23}) \approx 215.6 \text{ Hz}$

**3. Dominant Gravitational-Wave Frequency at the ISCO**

The dominant gravitational-wave emission is at twice the orbital frequency, so $f_{GW} = 2f = 2 \times 215.6 \text{ Hz} = 431.2 \text{ Hz}$.

**4. GW Signal Shutoff and Scaling with Mass**

As the binary system inspirals, the orbital frequency increases.  When the orbit reaches the ISCO, the orbit is no longer stable and the objects rapidly plunge into the black hole. This plunge phase is very short and produces a different type of gravitational wave signal than the inspiral.  The inspiral signal, which is much stronger and easier to detect, "shuts off" at the ISCO frequency because the stable orbital motion ceases.

The ISCO radius scales as $r_{ISCO} = 6GM/c^2$.  The orbital frequency at the ISCO is $f = c^3 / (12\pi\sqrt{6} GM)$.  Therefore, $f \propto 1/M$.  This means the ISCO frequency is *inversely* proportional to the mass of the black hole.  A more massive black hole will have a lower ISCO frequency.  The gravitational wave frequency, being twice the orbital frequency, also scales inversely with mass.

\[
\begin{aligned}
\mathrm{r\_isco\_km} &= 88.62 \\
\mathrm{f\_orbital\_hz} &= 215.6 \\
\mathrm{f\_gw\_hz} &= 431.2
\end{aligned}
\]