### Derivation and Reasoning

**1. Temperature Scaling**
For an adiabatic expansion of a photon gas (radiation), the entropy $S$ is conserved. For a blackbody, the entropy density scales as $s \propto T^3$. Since the total entropy in a comoving volume $V \propto a^3$ is constant:
$S = s \cdot a^3 \propto T^3 a^3 = \text{constant} \implies T \propto a^{-1}$
Using the relationship between the scale factor $a$ and redshift $z$, $a = \frac{1}{1+z}$, we have:
$T(z) = T_0 (1+z)$
Given $T_0 = 2.725\text{ K}$ and $z = 1100$:
$T_{rec} = 2.725 \times (1 + 1100) = 2.725 \times 1101$
$T_{rec} = 3000.225\text{ K}$

**2. Photon Number Density Scaling**
The number density $n$ of photons in a blackbody distribution is given by:
$n = \int \frac{d^3p}{(2\pi\hbar)^3} \frac{1}{e^{pc/kT}-1} \propto T^3$
Since $T \propto (1+z)$, the number density scales as:
$n(z) = n_0 (1+z)^3$
The ratio is:
$\frac{n(z_{rec})}{n_0} = (1101)^3$
$\log_{10}\left(\frac{n(z_{rec})}{n_0}\right) = 3 \log_{10}(1101) \approx 3 \times 3.04179 = 9.12537$

**3. Photon Energy Density Scaling**
The energy density $\rho$ of a blackbody is given by the Stefan-Boltzmann law:
$\rho = a_{SB} T^4 \propto T^4$
Since $T \propto (1+z)$, the energy density scales as:
$\rho(z) = \rho_0 (1+z)^4$
The ratio is:
$\frac{\rho(z_{rec})}{\rho_0} = (1101)^4$
$\log_{10}\left(\frac{\rho(z_{rec})}{\rho_0}\right) = 4 \log_{10}(1101) \approx 4 \times 3.04179 = 12.16716$

**Explanation of the extra factor of $(1+z)$:**
The number density $n$ scales as $a^{-3}$ due to the dilution of particles as the volume increases. However, the energy density $\rho$ accounts for both the dilution of the number of photons ($a^{-3}$) and the loss of energy per photon due to the cosmological redshift of the wavelength ($\lambda \propto a \implies E = hc/\lambda \propto a^{-1}$). Thus, $\rho \propto a^{-3} \cdot a^{-1} = a^{-4}$.

**4. Preservation of Blackbody Spectrum**
The CMB remains a blackbody because the redshift affects all frequencies equally. The spectral radiance of a blackbody is:
$B_\nu(T) = \frac{2h\nu^3}{c^2} \frac{1}{e^{h\nu/kT}-1}$
As the universe expands, $\nu \to \nu' = \nu / (1+z)$ and $T \to T' = T / (1+z)$.
Substituting these into the expression:
$B_{\nu'}(T') = \frac{2h(\nu')^3}{c^2} \frac{1}{e^{h\nu'/kT'}-1} = \frac{2h(\nu/(1+z))^3}{c^2} \frac{1}{e^{h\nu/(1+z) / (T/(1+z))}-1}$
$B_{\nu'}(T') = (1+z)^{-3} B_\nu(T)$
The functional form of the Planck distribution is preserved; only the temperature parameter changes. No rethermalization (scattering) is required to maintain the blackbody shape.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{T\_rec\_K} &= 3000.225 \\
\mathrm{log10\_number\_ratio} &= 9.12537 \\
\mathrm{log10\_energy\_ratio} &= 12.16716
\end{aligned}
\]