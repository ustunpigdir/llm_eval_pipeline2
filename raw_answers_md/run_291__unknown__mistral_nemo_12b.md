**1. Physical Origin and Regularization:**

The Casimir effect arises due to the exclusion of vacuum modes between two parallel, perfectly conducting plates. In the absence of the plates, the vacuum modes are continuous and infinite. However, when the plates are introduced, the modes that have a wavelength smaller than the plate separation $d$ are excluded, as their wavelengths cannot fit between the plates. This exclusion of modes leads to a change in the zero-point energy of the vacuum, resulting in the Casimir force.

Regularization is needed to handle the infinite sum of zero-point energies from all possible modes. The zeta-function regularization method is used to subtract the infinite vacuum energy of the empty space from the infinite vacuum energy of the space between the plates, leaving us with a finite Casimir energy.

**2. Casimir Pressure Magnitude at $d = 100$ nm:**

The Casimir pressure $P$ is given by the Lifshitz formula:

\[P = \frac{\hbar c}{2\pi}\int_0^\infty \frac{dk}{k} \sum_{n=0}^\infty \rho_n(k) \ln\left[1 - e^{-2kd}\left(1 - \frac{k^2c^2}{\omega_n^2}\right)\right]\]

where $\rho_n(k)$ is the density of states, $\omega_n$ are the frequencies of the modes, and $k$ is the wave number. For two parallel plates, this simplifies to:

\[P = -\frac{\pi^2\hbar c}{240d^4}\]

The pressure is attractive, as the negative sign indicates.

At $d = 100$ nm, the magnitude of the pressure is:

\[|P| = \frac{\pi^2\hbar c}{240(100 \times 10^{-9})^4} \approx 1.3 \times 10^{-3} \text{ Pa}\]

**3. Energy per Unit Area Magnitude:**

The energy per unit area $E/A$ is given by:

\[\frac{E}{A} = \frac{\hbar c}{2\pi}\int_0^\infty \frac{dk}{k} \sum_{n=0}^\infty \rho_n(k) \ln\left[1 + e^{-2kd}\left(1 - \frac{k^2c^2}{\omega_n^2}\right)\right]\]

This simplifies to:

\[\frac{E}{A} = -\frac{\pi^2\hbar c}{720d^3}\]

The magnitude of the energy per unit area is:

\[|\frac{E}{A}| = \frac{\pi^2\hbar c}{720(100 \times 10^{-9})^3} \approx 6.5 \times 10^{-4} \text{ } \mu\text{J/m}^2\]

**4. Pressure Change if $d$ Doubles:**

The pressure scales as $1/d^4$. If $d$ doubles, the new pressure $P'$ is:

\[P' = \frac{P}{16} = -\frac{\pi^2\hbar c}{240(200 \times 10^{-9})^4} \approx 1.6 \times 10^{-5} \text{ Pa}\]

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{pressure\_pa} &= 1.3 \times 10^{-3} \text{ Pa} \\
\mathrm{energy\_per\_area\_uJ\_m2} &= 6.5 \times 10^{-4} \text{ } \mu\text{J/m}^2 \\
\mathrm{pressure\_double\_d\_pa} &= 1.6 \times 10^{-5} \text{ Pa}
\end{aligned}
\]