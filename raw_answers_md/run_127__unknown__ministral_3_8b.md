### Derivation and Reasoning

#### 1. Photon Temperature Scaling with Redshift
The CMB is a blackbody photon gas undergoing adiabatic expansion. For a photon gas, the temperature \( T \) scales with the scale factor \( a \) as follows:

\[
T \propto \frac{1}{a}
\]

Since redshift \( z \) is defined by \( 1 + z = \frac{a_0}{a} \), where \( a_0 \) is the scale factor today, we can rewrite the temperature scaling in terms of redshift:

\[
T(z) = T_0 (1 + z)
\]

This is because \( a \propto \frac{1}{1+z} \), so \( T \propto (1+z) \).

Now, evaluate \( T \) at recombination (\( z = 1100 \)):

\[
T_{\text{rec}} = T_0 (1 + z_{\text{rec}}) = 2.725 \, \text{K} \times (1 + 1100) = 2.725 \times 1101 \approx 3000 \, \text{K}
\]

#### 2. Photon Number Density Scaling
The number density \( n \) of photons scales as \( a^{-3} \) because the volume scales as \( a^3 \) and the number of photons is conserved in adiabatic expansion (no creation or annihilation).

Thus:

\[
n(z) = n_0 \left( \frac{a_0}{a} \right)^3 = n_0 (1 + z)^3
\]

The ratio of the number density at recombination to today is:

\[
\frac{n(z_{\text{rec}})}{n_0} = (1 + z_{\text{rec}})^3 = (1101)^3
\]

Taking the logarithm base 10:

\[
\log_{10} \left( \frac{n(z_{\text{rec}})}{n_0} \right) = 3 \log_{10}(1 + z_{\text{rec}}) = 3 \log_{10}(1101)
\]

Calculate \( \log_{10}(1101) \):

\[
\log_{10}(1101) \approx \log_{10}(1.101 \times 10^3) = \log_{10}(1.101) + 3 \approx 0.0414 + 3 = 3.0414
\]

Thus:

\[
\log_{10} \left( \frac{n(z_{\text{rec}})}{n_0} \right) \approx 3 \times 3.0414 = 9.1242
\]

#### 3. Photon Energy Density Scaling
The energy density \( \rho \) of a photon gas scales as \( a^{-4} \) because the energy of each photon scales as \( 1/a \) (due to redshift) and the number density scales as \( a^{-3} \). Thus:

\[
\rho(z) = \rho_0 \left( \frac{a_0}{a} \right)^4 = \rho_0 (1 + z)^4
\]

The ratio of the energy density at recombination to today is:

\[
\frac{\rho(z_{\text{rec}})}{\rho_0} = (1 + z_{\text{rec}})^4 = (1101)^4
\]

Taking the logarithm base 10:

\[
\log_{10} \left( \frac{\rho(z_{\text{rec}})}{\rho_0} \right) = 4 \log_{10}(1 + z_{\text{rec}}) = 4 \log_{10}(1101) \approx 4 \times 3.0414 = 12.1656
\]

The extra factor of \( (1+z) \) relative to the number density comes from the fact that each photon's energy scales as \( 1/a \) (or \( (1+z) \)) due to redshift, while the number density scales as \( a^{-3} \). Thus, the energy density scales as \( a^{-4} \), which is \( (1+z)^4 \).

#### 4. Why the CMB Remains a Perfect Blackbody
The CMB remains a perfect blackbody as it redshifts because:
- The expansion is adiabatic (no heat exchange with surroundings), so the photon distribution function is scaled uniformly in energy.
- The photon-photon scattering (Compton scattering) maintains thermal equilibrium during the radiation-dominated era. Even though the photons are redshifted, the relative energy distribution remains unchanged because the scattering processes preserve the blackbody form (the distribution function is scaled by \( (1+z) \) but retains its Planck form).
- After recombination, the photons decouple from matter and free-stream, but their blackbody nature is preserved because the initial distribution was a perfect blackbody and the subsequent redshifting does not alter the shape of the distribution.

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{T\_rec\_K} &= 3000 \\
\mathrm{log10\_number\_ratio} &= 9.124 \\
\mathrm{log10\_energy\_ratio} &= 12.17
\end{aligned}
\]