Let's break down the problem step by step.

1. **Temperature Scaling:**

The temperature of the CMB scales with the redshift as $T \propto 1/(1+z)$. This is derived from the adiabatic condition, which states that for a closed universe, the entropy per comoving volume is constant.  For a blackbody photon gas, the entropy is proportional to $T^3 N$, where $N$ is the number of photons.  The comoving volume scales as $(1+z)^{-3}$.  Therefore, $T^3 N / (1+z)^3 = \text{constant}$, which implies $T \propto 1/(1+z)$.

To find the temperature at recombination ($z = 1100$), we have:
$T_{rec} = T_0 / (1 + z_{rec}) = 2.725 \text{ K} / (1 + 1100) = 2.725 \text{ K} / 1101 \approx 0.00247 \text{ K}$.
$T_{rec} = 2.725 / 1101 \approx 0.00247$ K.

2. **Number Density Scaling:**

The number density of photons, $n$, scales as $n \propto (1+z)^{-3}$. This is because the volume scales as $(1+z)^3$, and the number density is inversely proportional to the volume.  Mathematically, $n(z) = n_0 (1+z)^{-3}$.

The ratio of number densities is:
$n(z_{rec})/n_0 = (1+z_{rec})^{-3} = (1101)^{-3} \approx 0.000000901$.
$\log_{10}(n(z_{rec})/n_0) = \log_{10}((1101)^{-3}) = -3 \log_{10}(1101) \approx -3 \times 3.04576 = -9.13728$.
So, $\log_{10}(n(z_{rec})/n_0) \approx -9.137$.

3. **Energy Density Scaling:**

The energy density of a blackbody photon gas is given by $\rho = \frac{\pi^2}{30} T^4 n$.  Since $T \propto (1+z)^{-1}$ and $n \propto (1+z)^{-3}$, we have:
$\rho(z) = \frac{\pi^2}{30} [(1+z)^{-1}]^4 (1+z)^{-3} = \frac{\pi^2}{30} (1+z)^{-7}$.
$\rho(z) = \frac{\pi^2}{30} (1+z)^{-7}$.
$\rho_0 = \frac{\pi^2}{30} (1+0)^{-7} = \frac{\pi^2}{30}$.
The ratio of energy densities is:
$\rho(z_{rec}) / \rho_0 = (1+z_{rec})^{-7} = (1101)^{-7} \approx 2.22 \times 10^{-12}$.
$\log_{10}(\rho(z_{rec}) / \rho_0) = -7 \log_{10}(1101) \approx -7 \times 3.04576 = -21.32032$.
So, $\log_{10}(\rho(z_{rec}) / \rho_0) \approx -21.32$.

The extra factor of $(1+z)$ compared to the number density scaling comes from the temperature dependence of the energy density. The energy density is proportional to $T^4$, and the temperature scales as $T \propto (1+z)^{-1}$. Therefore, the energy density scales as $\rho \propto (1+z)^{-4} \times (1+z)^{-3} = (1+z)^{-7}$. The number density scales as $n \propto (1+z)^{-3}$. The ratio of energy density to number density is then proportional to $(1+z)^{-4}$.  Since each photon has energy $E = h\nu = h c / \lambda = h c T / (k_B)$, the energy per photon is proportional to $T$.  Thus, $\rho = n \times E \propto n \times T \propto (1+z)^{-3} (1+z)^{-1} = (1+z)^{-4}$.  Therefore, the energy density scales as $(1+z)^{-7}$, while the number density scales as $(1+z)^{-3}$.

4. **Why the CMB remains a blackbody:**

The CMB remains a blackbody because the expansion of the universe is adiabatic. Adiabatic expansion means that there is no heat exchange with the surroundings. The photons are not interacting with matter in a way that would change their energy distribution.  While the universe was opaque before recombination, once recombination occurred, the photons decoupled from matter. Since there has been no significant interaction between photons since then, the blackbody spectrum established at recombination has been preserved.  There has been no rethermalization process to alter the spectrum. The expansion simply redshifts the photons, but it doesn't change the underlying blackbody distribution.

\[
\begin{aligned}
\mathrm{T\_rec\_K} &= 0.00247 \\
\mathrm{log10\_number\_ratio} &= -9.137 \\
\mathrm{log10\_energy\_ratio} &= -21.320
\end{aligned}
\]