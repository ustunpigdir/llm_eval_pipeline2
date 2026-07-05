**1. Photon temperature scaling**

The photon temperature scales inversely with the scale factor $a$ of the universe. This is because the photons are redshifted as the universe expands. The relationship is given by:

\[T(z) = T_0 (1 + z)\]

where $T_0$ is the present-day temperature and $z$ is the redshift. At recombination ($z = 1100$), the temperature is:

\[T_{rec} = T_0 (1 + 1100) = 2.725 \times 1100 \text{ K} = 3000.25 \text{ K}\]

**2. Photon number density scaling**

The number density of photons scales as $a^{-3}$. This is because the number of photons in a comoving volume remains constant, but the physical volume increases as $a^3$. Therefore, the number density ratio is:

\[\frac{n(z)}{n_0} = a^{-3} = (1 + z)^{-3}\]

Taking the logarithm base 10, we get:

\[\log_{10} \left( \frac{n(z)}{n_0} \right) = \log_{10} (1 + z)^{-3} = -3 \log_{10} (1 + z)\]

At recombination ($z = 1100$), this becomes:

\[\log_{10} \left( \frac{n_{rec}}{n_0} \right) = -3 \log_{10} (1 + 1100) = -3 \log_{10} 1101 \approx -3.03\]

**3. Photon energy density scaling**

The energy density of a blackbody photon gas scales as $a^{-4}$. This is because the energy density is proportional to $T^4$, and since $T \propto a^{-1}$, we have $\rho \propto a^{-4}$. Therefore, the energy density ratio is:

\[\frac{\rho(z)}{\rho_0} = a^{-4} = (1 + z)^{-4}\]

Taking the logarithm base 10, we get:

\[\log_{10} \left( \frac{\rho(z)}{\rho_0} \right) = \log_{10} (1 + z)^{-4} = -4 \log_{10} (1 + z)\]

At recombination ($z = 1100$), this becomes:

\[\log_{10} \left( \frac{\rho_{rec}}{\rho_0} \right) = -4 \log_{10} (1 + 1100) = -4 \log_{10} 1101 \approx -4.04\]

The extra factor of $(1+z)$ relative to the number density comes from the fact that the energy density is proportional to $nT$, and while $n \propto a^{-3}$, $T \propto a^{-1}$, so $\rho \propto a^{-4}$.

**4. Why the CMB remains a perfect blackbody**

The CMB remains a perfect blackbody as it redshifts because the universe has been transparent to photons since recombination. This means that the photons have had no interactions with matter since then, and thus their energy distribution has not changed. The redshift is a purely kinematic effect due to the expansion of the universe.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{T\_rec\_K} &= 3000.25 \\
\mathrm{log10\_number\_ratio} &= -3.03 \\
\mathrm{log10\_energy\_ratio} &= -4.04
\end{aligned}
\]