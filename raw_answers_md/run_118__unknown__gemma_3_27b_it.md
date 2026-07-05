Here's a derivation of the adiabatic scalings of the CMB photon gas, addressing each task step-by-step.

**1. Temperature Scaling with Redshift**

For an adiabatically expanding photon gas, the temperature scales with the scale factor *a* as $T \propto a^{-1}$.  Since $1+z = a_0/a$, we have $a = a_0/(1+z)$, where $a_0$ is the scale factor today. Therefore, $T \propto (1+z)^{-1}$.

We are given $T_0 = 2.725$ K today (at $z=0$).  At recombination, $z_{rec} = 1100$.  Thus, the temperature at recombination is:

$T_{rec} = T_0 (1+z_{rec})^{-1} = 2.725 \text{ K} \times (1+1100)^{-1} = 2.725 \text{ K} \times (1101)^{-1} \approx 2.725 \text{ K} \times 9.08 \times 10^{-4} \approx 0.00247 \text{ K} \times 1000 \approx 2.47 \text{ K}$
More precisely:
$T_{rec} = \frac{2.725}{1101} \approx 0.00247636 \times 10^3 \text{ K} \approx 2.476 \text{ K}$

**2. Number Density Scaling**

The number density of photons scales with the volume, which is proportional to $a^3$.  Therefore, $n \propto a^{-3}$.  Using $a = a_0/(1+z)$, we have $n \propto (1+z)^3$.  The ratio of number densities is:

$\frac{n(z)}{n_0} = (1+z)^3$

At recombination, $z = 1100$, so:

$\frac{n(z_{rec})}{n_0} = (1+1100)^3 = (1101)^3 \approx 1.334 \times 10^9$

Taking the base-10 logarithm:

$\log_{10} \left( \frac{n(z_{rec})}{n_0} \right) = \log_{10} (1101^3) = 3 \log_{10} (1101) \approx 3 \times 3.04139 \approx 9.124$

**3. Energy Density Scaling**

The energy density of the photon gas scales with the number density and the energy per photon. The energy per photon is proportional to the temperature, $E \propto T$.  Therefore, the energy density scales as $\rho \propto nT \propto a^{-3} a^{-1} = a^{-4}$.  Using $a = a_0/(1+z)$, we have $\rho \propto (1+z)^4$.  The ratio of energy densities is:

$\frac{\rho(z)}{\rho_0} = (1+z)^4$

At recombination, $z = 1100$, so:

$\frac{\rho(z_{rec})}{\rho_0} = (1+1100)^4 = (1101)^4 \approx 1.468 \times 10^{12}$

Taking the base-10 logarithm:

$\log_{10} \left( \frac{\rho(z_{rec})}{\rho_0} \right) = \log_{10} (1101^4) = 4 \log_{10} (1101) \approx 4 \times 3.04139 \approx 12.166$

The extra factor of $(1+z)$ relative to the number density scaling comes from the fact that the energy density is proportional to both the number of photons *and* the energy of each photon. As the universe expands, the number of photons decreases (as $a^{-3}$), but the energy of each photon also decreases (as $a^{-1}$).  The combined effect is a decrease in energy density as $a^{-4}$.

**4. CMB as a Perfect Blackbody**

The CMB remains a perfect blackbody because the photons are free-streaming.  The expansion of the universe simply stretches the wavelengths of the photons, reducing their energy and temperature. This process does *not* introduce any new photons or alter the distribution of existing photons.  The photons are not interacting with each other or with any matter in a way that would cause them to be rethermalized.  The adiabatic expansion preserves the blackbody spectrum; it simply shifts it to longer wavelengths (lower energies).  The lack of scattering or absorption ensures that the shape of the spectrum remains unchanged, only its amplitude (and therefore temperature) is reduced.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{T\_rec\_K} &= 2.476 \\
\mathrm{log10\_number\_ratio} &= 9.124 \\
\mathrm{log10\_energy\_ratio} &= 12.166
\end{aligned}
\]