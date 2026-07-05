Let's break down the problem step by step.

1. **Temperature Scaling:**

The temperature of the CMB scales with the redshift as $T \propto 1/(1+z)$. This is derived from the adiabatic condition, which states that for a closed universe, the entropy per comoving volume is constant.  For a blackbody photon gas, the entropy is proportional to $T^3 N$, where $N$ is the number of photons per volume.  Since the comoving volume scales as $a^{-3}$, we have:

$T^3 N a^{-3} = \text{constant}$

Since $N \propto a^{-3}$ (number density scales as $a^{-3}$), we get:

$T^3 a^{-3} a^{-3} = \text{constant}$
$T^3 = \text{constant}$
$T \propto 1/a$

And since $a = 1/(1+z)$, we have $T \propto 1/(1+z)$.

Now, let's calculate the temperature at recombination ($z = 1100$):

$T_{rec} = T_0 / (1 + z_{rec}) = 2.725 \text{ K} / (1 + 1100) = 2.725 \text{ K} / 1101 \approx 0.00247 \text{ K}$

$T_{rec} = 2.725 / 1101 \approx 0.00247$ K.

2. **Number Density Scaling:**

The number density of photons scales as $n \propto a^{-3} \propto (1+z)^3$. This is because the volume expands as $a^3$, and the number of photons is conserved (in an adiabatic expansion).  Therefore, the number density decreases as $1/a^3$, or increases as $(1+z)^3$.

The ratio of number densities is:

$n(z_{rec})/n_0 = (1+z_{rec})^3 = (1+1100)^3 = 1101^3 \approx 1.333 \times 10^9$

$\log_{10}(n(z_{rec})/n_0) = \log_{10}(1101^3) = 3 \log_{10}(1101) \approx 3 \times 3.041 = 9.123$

3. **Energy Density Scaling:**

The energy density of a blackbody photon gas is given by $\rho = \frac{\pi^2}{30} T^4$.  Since $T \propto 1/(1+z)$, we have $\rho \propto \frac{1}{(1+z)^4}$.  Therefore, the energy density scales as $1/(1+z)^4$.

The ratio of energy densities is:

$\rho(z_{rec}) / \rho_0 = \frac{1}{(1+z_{rec})^4} = \frac{1}{1101^4} \approx \frac{1}{1.47 \times 10^{15}}$

$\log_{10}(\rho(z_{rec}) / \rho_0) = \log_{10}\left(\frac{1}{1101^4}\right) = -4 \log_{10}(1101) \approx -4 \times 3.041 = -12.164$

The extra factor of $(1+z)$ compared to the number density scaling comes from the fact that the energy per photon scales as $T$, and $T \propto (1+z)$.  The energy density is the product of the number density and the energy per photon.  So, $\rho = n \times E$, where $E = kT = \frac{1}{2} h \nu$.  Since $T \propto (1+z)$, $E \propto (1+z)$.  Therefore, $\rho \propto n (1+z)$.  However, the energy density is also proportional to $T^4$, and $T \propto 1/(1+z)$, so $\rho \propto (1/(1+z))^4$.  Combining these, we get $\rho \propto \frac{n}{(1+z)^3} (1+z) = \frac{n}{(1+z)^2}$.  This is incorrect.

Let's re-examine.  $\rho = \frac{\pi^2}{30} T^4$.  $T \propto \frac{1}{1+z}$.  So $\rho \propto \frac{1}{(1+z)^4}$.
$n \propto (1+z)^3$.
$\frac{\rho(z)}{\rho(0)} = \frac{T(z)^4}{T(0)^4} = \frac{(1/(1+z))^4}{1} = \frac{1}{(1+z)^4}$.
$\frac{n(z)}{n(0)} = (1+z)^3$.
$\frac{\rho(z)/n(z)}{\rho(0)/n(0)} = \frac{T(z)^4/(1+z)^3}{T(0)^4/1} = \frac{1/(1+z)^4}{(1+z)^3} = \frac{1}{(1+z)^7}$.

The energy density scales as $1/(1+z)^4$.  The number density scales as $(1+z)^3$.  The ratio is $\frac{\rho(z)}{\rho(0)} = \frac{1}{(1+z)^4}$.
$\log_{10} \left( \frac{\rho(z)}{\rho(0)} \right) = -4 \log_{10}(1+z) = -4 \log_{10}(1101) \approx -4(3.041) = -12.164$.

4. **Why remains a blackbody:**

The CMB remains a perfect blackbody because the expansion of the universe is adiabatic. This means that there is no exchange of energy with the surroundings, and the entropy of the system is conserved.  The expansion simply stretches the wavelengths of the photons, causing a decrease in their energy and temperature, but it does not change their spectral distribution.  There is no rethermalization because the expansion rate is much faster than the rate at which photons can interact with each other.  The photons are effectively decoupled from matter at recombination, and the expansion continues to dilute them, preventing any further interactions that could lead to rethermalization.

\[
\begin{aligned}
\mathrm{T\_rec\_K} &= 0.00247 \\
\mathrm{log10\_number\_ratio} &= 9.123 \\
\mathrm{log10\_energy\_ratio} &= -12.164
\end{aligned}
\]