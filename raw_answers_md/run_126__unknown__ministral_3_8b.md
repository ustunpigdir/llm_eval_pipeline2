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
The number density \( n \) of photons scales as \( a^{-3} \) because the volume scales as \( a^3 \) and the number of photons is conserved (no creation or annihilation in adiabatic expansion).

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

The extra factor of \( (1+z) \) relative to the number density comes from the fact that each photon's energy scales as \( 1/a \propto (1+z) \), while the number density scales as \( a^{-3} \propto (1+z)^3 \). Thus, the energy density scales as \( (1+z)^4 \).

#### 4. Why the CMB Remains a Perfect Blackbody
The CMB remains a perfect blackbody as it redshifts because:
- The expansion is adiabatic (no heat exchange with surroundings), so the photon distribution function is scaled uniformly in energy.
- The redshift affects all photons equally, preserving the blackbody spectrum. The shape of the blackbody spectrum is determined by the distribution of photon energies, and since all energies are scaled by the same factor \( (1+z) \), the spectrum remains a blackbody with a rescaled temperature.
- No rethermalization is required because the adiabatic expansion itself preserves the blackbody form. The photons do not need to collide to rethermalize; the expansion itself enforces the blackbody scaling.

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{T\_rec\_K} &= 3000 \\
\mathrm{log10\_number\_ratio} &= 9.1242 \\
\mathrm{log10\_energy\_ratio} &= 12.1656 \\
\end{aligned}
\]