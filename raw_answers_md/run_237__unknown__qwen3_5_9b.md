**1. Radii of Event Horizon, Photon Sphere, and ISCO**

First, we define the gravitational radius $r_g = GM/c^2$.
Given:
$M = 10 M_\odot = 10 \times 1.989 \times 10^{30} \text{ kg} = 1.989 \times 10^{31} \text{ kg}$
$G = 6.674 \times 10^{-11} \text{ m}^3 \text{ kg}^{-1} \text{ s}^{-2}$
$c = 2.998 \times 10^8 \text{ m/s}$

Calculate $r_g$:
$$ r_g = \frac{GM}{c^2} = \frac{(6.674 \times 10^{-11})(1.989 \times 10^{31})}{(2.998 \times 10^8)^2} $$
$$ r_g = \frac{13.274586 \times 10^{20}}{8.988004 \times 10^{16}} \text{ m} $$
$$ r_g \approx 1.47692 \times 10^4 \text{ m} = 14.7692 \text{ km} $$

The radii in Schwarzschild coordinates are:
- Event Horizon ($r_h$): $r_h = 2GM/c^2 = 2 r_g$
- Photon Sphere ($r_{ph}$): $r_{ph} = 3GM/c^2 = 3 r_g$
- Innermost Stable Circular Orbit ($r_{isco}$): $r_{isco} = 6GM/c^2 = 6 r_g$

Evaluating $r_{isco}$ in km:
$$ r_{isco} = 6 \times 14.7692 \text{ km} \approx 88.615 \text{ km} $$
Rounding to 4 significant figures: $r_{isco} \approx 88.62 \text{ km}$.

**2. Orbital Frequency at ISCO**

The problem states the convention $\Omega^2 = GM/r^3$ for circular orbits in Schwarzschild coordinates.
At the ISCO, $r = r_{isco} = 6GM/c^2$.
$$ \Omega_{isco} = \sqrt{\frac{GM}{(6GM/c^2)^3}} = \sqrt{\frac{GM}{216 G^3 M^3 / c^6}} = \sqrt{\frac{c^6}{216 G^2 M^2}} = \frac{c^3}{\sqrt{216} GM} $$
Since $\sqrt{216} = 6\sqrt{6}$:
$$ \Omega_{isco} = \frac{c^3}{6\sqrt{6} GM} $$
The orbital frequency $f = \Omega/2\pi$:
$$ f_{orb} = \frac{c^3}{12\pi\sqrt{6} GM} $$

Substituting values:
$$ c^3 = (2.998 \times 10^8)^3 \approx 2.6941 \times 10^{25} \text{ m}^3/\text{s}^3 $$
$$ GM = 1.32746 \times 10^{21} \text{ m}^3/\text{s}^2 $$
$$ 12\pi\sqrt{6} \approx 12 \times 3.14159 \times 2.44949 \approx 92.328 $$
$$ f_{orb} = \frac{2.6941 \times 10^{25}}{92.328 \times 1.32746 \times 10^{21}} \text{ Hz} $$
$$ f_{orb} = \frac{2.6941 \times 10^{25}}{1.2256 \times 10^{23}} \text{ Hz} \approx 219.79 \text{ Hz} $$
Rounding to 4 significant figures: $f_{orb} \approx 219.8 \text{ Hz}$.

**3. Gravitational-Wave Frequency at ISCO**

The dominant gravitational-wave emission is at twice the orbital frequency:
$$ f_{GW} = 2 f_{orb} \approx 2 \times 219.79 \text{ Hz} = 439.58 \text{ Hz} $$
Rounding to 4 significant figures: $f_{GW} \approx 439.6 \text{ Hz}$.

**4. Explanation of Signal 'Shut Off' and Scaling**

- **Signal Shut Off:** The ISCO represents the innermost stable circular orbit. Inside this radius ($r < 6GM/c^2$), circular orbits are unstable. As the binary inspirals due to gravitational wave emission, it approaches the ISCO. Once it crosses the ISCO, the orbit becomes unstable and the particle plunges into the black hole on a dynamical timescale rather than continuing a slow adiabatic inspiral. This transition marks the end of the "inspiral" phase in the frequency domain, where the signal frequency increases gradually. The signal effectively "shuts off" the inspiral chirp and transitions into the merger and ringdown phases, which are distinct in waveform morphology.
- **Scaling:** From the derived formula $f_{orb} = \frac{c^3}{12\pi\sqrt{6} GM}$, we see that the orbital frequency is inversely proportional to the mass of the black hole ($f_{orb} \propto M^{-1}$). Consequently, the gravitational wave frequency also scales as $f_{GW} \propto M^{-1}$. A more massive black hole has a larger ISCO radius and a deeper gravitational potential well, resulting in a lower orbital frequency for a given coordinate time.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{r\_isco\_km} &= 88.62 \\
\mathrm{f\_orbital\_hz} &= 219.8 \\
\mathrm{f\_gw\_hz} &= 439.6
\end{aligned}
\]