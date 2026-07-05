## Casimir Effect Calculation for Parallel Plates

Here's a derivation and calculation of the Casimir effect for two parallel, ideal conducting plates.

**1. Physical Origin and Regularization**

The Casimir effect arises from the modification of the vacuum energy of the electromagnetic field due to the presence of the conducting plates.  In free space, the electromagnetic field can exist in a superposition of all possible modes (wavelengths).  However, between the plates, only those modes with wavelengths that fit an integer number of half-wavelengths within the gap are allowed.  This means that modes with wavelengths longer than $2d$ are excluded, where $d$ is the separation between the plates.

The energy density of these excluded modes is infinite if we simply sum over all forbidden wavelengths. This is because the number of modes increases with frequency (or inversely with wavelength).  This divergence necessitates a regularization procedure.  A common method is to use the zeta-function regularization, which effectively sums over the modes with a complex parameter and then analytically continues the result to remove the divergence.  Alternatively, a cutoff frequency can be introduced, and the result taken in the limit as the cutoff goes to infinity.  The final result is independent of the regularization scheme used.

**2. Casimir Pressure Calculation**

The Casimir pressure $P$ is given by:

$P = -\frac{\pi^2 \hbar c}{720 d^4} \times 2 - \frac{\pi^2 \hbar c}{720 d^4} \times 2 = -\frac{\pi^2 \hbar c}{240 d^4}$

The negative sign indicates that the pressure is attractive.  We are asked to report the magnitude, so we take the absolute value.

Let's calculate the magnitude at $d = 100 \text{ nm} = 100 \times 10^{-9} \text{ m}$. We have:

$\hbar = 1.0545718 \times 10^{-34} \text{ J s}$
$c = 2.99792458 \times 10^8 \text{ m/s}$

$P = \frac{\pi^2 \hbar c}{240 d^4} = \frac{\pi^2 (1.0545718 \times 10^{-34} \text{ J s}) (2.99792458 \times 10^8 \text{ m/s})}{240 (100 \times 10^{-9} \text{ m})^4}$

$P = \frac{\pi^2 (3.1566 \times 10^{-26} \text{ J m})}{240 \times 10^{-36} \text{ m}^4} = \frac{31.005 \times 10^{-26}}{240 \times 10^{-36}} \text{ Pa}$

$P = 129.1875 \times 10^{10} \text{ Pa} = 1.291875 \times 10^{-4} \text{ Pa}$

The pressure is attractive.

**3. Energy per Unit Area Calculation**

The energy per unit area $E/A$ is given by:

$E/A = -\frac{\pi^2 \hbar c}{720 d^3}$

Again, the negative sign indicates an attractive force, and we are asked for the magnitude.

$E/A = \frac{\pi^2 \hbar c}{720 d^3} = \frac{\pi^2 (1.0545718 \times 10^{-34} \text{ J s}) (2.99792458 \times 10^8 \text{ m/s})}{720 (100 \times 10^{-9} \text{ m})^3}$

$E/A = \frac{\pi^2 (3.1566 \times 10^{-26} \text{ J m})}{720 \times 10^{-27} \text{ m}^3} = \frac{31.005 \times 10^{-26}}{720 \times 10^{-27}} \text{ J/m}^2$

$E/A = 43.0625 \times 10^{-26+27} \text{ J/m}^2 = 4.30625 \times 10^{-5} \text{ J/m}^2$

Converting to $\mu$J/m$^2$:

$E/A = 4.30625 \times 10^{-5} \text{ J/m}^2 \times \frac{10^6 \mu\text{J}}{1 \text{ J}} = 43.0625 \mu\text{J/m}^2$

**4. Pressure Change with Doubled Distance**

The pressure scales as $P \propto \frac{1}{d^4}$. If $d$ doubles to $2d$, the new pressure $P'$ is:

$P' = \frac{1}{(2d)^4} P = \frac{1}{16d^4} P = \frac{1}{16} P$

So, the pressure is reduced by a factor of 16.

The new pressure at $d = 200 \text{ nm}$ is:

$P' = \frac{1}{16} (1.291875 \times 10^{-4} \text{ Pa}) = 8.07421875 \times 10^{-6} \text{ Pa}$

\[
\begin{aligned}
\mathrm{pressure\_pa} &= 1.29 \times 10^{-5} \\
\mathrm{energy\_per\_area\_uJ_m2} &= 43.1 \\
\mathrm{pressure\_double\_d\_pa} &= 8.07 \times 10^{-6}
\end{aligned}
\]