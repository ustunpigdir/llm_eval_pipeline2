### Derivation and Calculations

**1. Photon Temperature Scaling**
In an adiabatically expanding universe described by the FLRW metric, the wavelength $\lambda$ of a photon stretches proportionally to the scale factor $a(t)$. Thus, $\lambda \propto a$. Since the frequency is $\nu = c/\lambda$, the frequency scales as $\nu \propto a^{-1}$.
The temperature $T$ of a blackbody radiation field is proportional to the characteristic frequency (Wien's displacement law), so $T \propto \nu \propto a^{-1}$.
Using the definition of redshift $1+z = a_0/a$, we have:
$$ T(z) = T_0 (1+z) $$
Given $T_0 = 2.725$ K and $z = 1100$:
$$ 1+z = 1101 $$
$$ T_{rec} = 2.725 \, \text{K} \times 1101 $$
$$ T_{rec} = 3000.225 \, \text{K} $$

**2. Photon Number Density Scaling**
The number density $n$ is the number of photons per unit volume. As the universe expands, the volume scales as $V \propto a^3$. Assuming photon number conservation (no creation or destruction of photons after decoupling), the number density scales inversely with volume:
$$ n \propto a^{-3} $$
In terms of redshift:
$$ \frac{n(z)}{n_0} = \left( \frac{a_0}{a} \right)^3 = (1+z)^3 $$
We need the base-10 logarithm of this ratio:
$$ \log_{10}\left( \frac{n(z)}{n_0} \right) = \log_{10}\left( (1+z)^3 \right) = 3 \log_{10}(1+z) $$
Using $1+z = 1101$:
$$ \log_{10}(1101) \approx 3.04179 $$
$$ \log_{10}\left( \frac{n(z)}{n_0} \right) = 3 \times 3.04179 \approx 9.12537 $$

**3. Photon Energy Density Scaling**
The energy density $\rho$ is the total energy per unit volume. It is the product of the number density $n$ and the average energy per photon $\langle E \rangle$.
- Number density scales as $n \propto a^{-3}$.
- The energy of a single photon is $E = h\nu$. Since $\nu \propto a^{-1}$, the energy per photon scales as $E \propto a^{-1}$.
Combining these:
$$ \rho \propto n \times E \propto a^{-3} \times a^{-1} = a^{-4} $$
In terms of redshift:
$$ \frac{\rho(z)}{\rho_0} = (1+z)^4 $$
We need the base-10 logarithm of this ratio:
$$ \log_{10}\left( \frac{\rho(z)}{\rho_0} \right) = \log_{10}\left( (1+z)^4 \right) = 4 \log_{10}(1+z) $$
Using $1+z = 1101$:
$$ \log_{10}\left( \frac{\rho(z)}{\rho_0} \right) = 4 \times 3.04179 \approx 12.16716 $$
**Explanation of the extra factor:**
The number density ratio accounts for the dilution of photons due to the expansion of volume ($a^{-3}$). The energy density ratio includes an additional factor of $(1+z)$ (or $a^{-1}$) because the energy of each individual photon decreases due to cosmological redshift. Thus, the total energy density drops faster than the number density.

**4. Blackbody Preservation**
The CMB remains a perfect blackbody because the expansion of the universe is adiabatic for the photon gas. According to Liouville's theorem, the phase space distribution function $f(\mathbf{x}, \mathbf{p})$ is conserved along the trajectories of particles in a collisionless gas. For a blackbody, the distribution is $f(p) \propto (e^{p/T} - 1)^{-1}$. As the universe expands, the momentum $p$ of each photon scales as $a^{-1}$, and the temperature $T$ scales as $a^{-1}$. Consequently, the ratio $p/T$ remains constant. Since the functional form of the distribution is preserved, the spectrum remains a blackbody without requiring rethermalization processes (which would be necessary if the expansion were non-adiabatic or if interactions were significant).

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{T\_rec\_K} &= 3000.225 \\
\mathrm{log10\_number\_ratio} &= 9.125 \\
\mathrm{log10\_energy\_ratio} &= 12.167
\end{aligned}
\]