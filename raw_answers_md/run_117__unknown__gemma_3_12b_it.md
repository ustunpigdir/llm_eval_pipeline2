Let's break down the problem step by step.

1. **Temperature Scaling:**

The temperature of the CMB scales with the redshift as $T \propto 1/(1+z)$. This is derived from the adiabatic condition, which states that for a closed universe, the entropy per comoving volume is constant.  For a blackbody photon gas, the entropy is proportional to $T^3 N$, where $N$ is the number of photons.  The comoving volume scales as $(1+z)^{-3}$.  Therefore, $T^3 N / (1+z)^3 = \text{constant}$, which implies $T \propto 1/(1+z)$.

To find the temperature at recombination ($z = 1100$), we have:
$T_{rec} = T_0 / (1 + z_{rec}) = 2.725 \text{ K} / (1 + 1100) = 2.725 \text{ K} / 1101 \approx 0.00247 \text{ K}$.

$T_{rec\_K} = 0.00247$ K

2. **Number Density Scaling:**

The number density of photons, $n$, scales as $n \propto (1+z)^{-3}$. This is because the volume scales as $(1+z)^3$, and the number density is inversely proportional to the volume.  Mathematically, $n(z) = n_0 (1+z)^{-3}$.

The ratio of number densities is:
$n(z_{rec})/n_0 = (1+z_{rec})^{-3} = (1101)^{-3} \approx 2.42 \times 10^{-10}$.

$\log_{10}(n(z_{rec})/n_0) = \log_{10}((1101)^{-3}) = -3 \log_{10}(1101) \approx -3 \times 3.041 = -9.123$.
Since $n \propto a^{-3}$, we have $\log_{10} \left( \frac{n(z)}{n_0} \right) = 3 \log_{10} \left( \frac{1}{1+z} \right) = -3 \log_{10}(1+z) = -3 \log_{10}(1101) \approx -9.123$.

$\log10\_number\_ratio = -9.123$

3. **Energy Density Scaling:**

The energy density of a blackbody photon gas is given by $\rho = \frac{\pi^2}{30} T^4$.  Since $T \propto 1/(1+z)$, we have $\rho \propto (1/(1+z))^4 \propto (1+z)^{-4}$.

The ratio of energy densities is:
$\rho(z_{rec}) / \rho_0 = (1+z_{rec})^{-4} = (1101)^{-4} \approx 1.92 \times 10^{-13}$.

$\log_{10}(\rho(z_{rec}) / \rho_0) = \log_{10}((1101)^{-4}) = -4 \log_{10}(1101) \approx -4 \times 3.041 = -12.164$.

The extra factor of $(1+z)$ compared to the number density scaling comes from the fact that the energy per photon scales as $E = h\nu = kT$, where $k$ is Boltzmann's constant.  Since $T \propto 1/(1+z)$, the energy per photon scales as $1/(1+z)$.  The energy density is the product of the number density and the energy per photon, so $\rho \propto n \times (1/(1+z)) \propto n / (1+z) \propto n (1+z)^{-1}$. However, the blackbody spectrum is assumed, so the energy density is $\rho = \frac{\pi^2}{30} T^4$.  Since $T \propto (1+z)^{-1}$, $\rho \propto (1+z)^{-4}$.  The number density scales as $n \propto (1+z)^{-3}$.  Therefore, $\rho/n \propto (1+z)^{-1}$.

$\log10\_energy\_ratio = -12.164$

4. **Why the CMB remains a blackbody:**

The CMB remains a blackbody because the expansion of the universe is slow enough that the photons have not had enough time to rethermalize through interactions.  The universe was opaque at recombination due to Thomson scattering.  Photons were constantly scattering off electrons, maintaining thermal equilibrium.  As the universe expanded and cooled, the electron-photon coupling ceased, and the photons effectively decoupled.  However, the expansion rate was slow enough that the photons retained their blackbody spectrum.  While there are some small deviations from a perfect blackbody due to the integrated Sachs-Wolfe effect and other phenomena, the CMB is remarkably close to a blackbody.  The expansion is adiabatic, meaning no energy is added or removed from the system.



FINAL ANSWER
\[
\begin{aligned}
\mathrm{T\_rec\_K} &= 0.00247 \\
\mathrm{log10\_number\_ratio} &= -9.123 \\
\mathrm{log10\_energy\_ratio} &= -12.164
\end{aligned}
\]