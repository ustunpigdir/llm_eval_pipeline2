**1. Physical Origin and Regularization:**

The Casimir effect arises due to the exclusion of vacuum modes between two parallel, perfectly conducting plates. In quantum field theory, the vacuum is not empty but filled with virtual particles (pair creation and annihilation). When two conducting plates are placed parallel to each other, the boundary conditions imposed by the plates exclude certain vacuum modes, leading to a net attractive force between the plates.

Regularization is needed to handle the infinite sum of vacuum energy that arises from the infinite number of modes. The zeta-function regularization method is used to compute the Casimir energy and pressure by subtracting the energy of the interacting system from the energy of a reference system (usually the energy of the vacuum without the plates).

**2. Casimir Pressure Magnitude at d = 100 nm:**

The Casimir pressure $P$ between two parallel plates separated by a distance $d$ is given by:

\[P = -\frac{\hbar c}{240 \pi d^4} \sum_{n=1}^{\infty} \sum_{m=1}^{\infty} \sum_{l=1}^{\infty} \frac{1}{n^2 + m^2 + l^2 - 1}\]

where $\hbar$ is the reduced Planck's constant, $c$ is the speed of light, and the sum is over all positive integers $n$, $m$, and $l$. This sum is regularized using the zeta-function method, leading to:

\[P = -\frac{\pi^2 \hbar c}{240 d^4}\]

Since the pressure is negative, it is attractive.

**3. Energy per Unit Area Magnitude:**

The energy per unit area $E/A$ is given by:

\[\frac{E}{A} = -\frac{\hbar c}{720 \pi d^3} \sum_{n=1}^{\infty} \sum_{m=1}^{\infty} \sum_{l=1}^{\infty} \frac{1}{n^2 + m^2 + l^2 - 1}\]

Regularizing this sum, we get:

\[\frac{E}{A} = -\frac{\pi^2 \hbar c}{720 d^3}\]

Since the energy per unit area is negative, it is attractive.

**4. Pressure Change if d Doubles:**

The Casimir pressure scales as $P \propto d^{-4}$. Therefore, if $d$ doubles, the pressure becomes:

\[P_{new} = P_{old} \left(\frac{d_{new}}{d_{old}}\right)^{-4} = P_{old} \left(\frac{1}{2}\right)^{-4} = 16 P_{old}\]

So, the new pressure at $d = 200$ nm is $16$ times the pressure at $d = 100$ nm.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{pressure\_pa} &= -\frac{\pi^2 \hbar c}{240 (100 \times 10^{-9})^4} \approx -6.25 \times 10^{-4} \text{ Pa} \\
\mathrm{energy\_per\_area\_uJ\_m2} &= -\frac{\pi^2 \hbar c}{720 (100 \times 10^{-9})^3} \approx -1.56 \times 10^{-7} \text{ J/m}^2 \\
\mathrm{pressure\_double\_d\_pa} &= 16 \times (-6.25 \times 10^{-4} \text{ Pa}) \approx -1.00 \times 10^{-3} \text{ Pa}
\end{aligned}
\]