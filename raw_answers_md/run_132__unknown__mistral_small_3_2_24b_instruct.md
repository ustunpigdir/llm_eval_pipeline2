To solve this problem, we need to understand how the properties of the Cosmic Microwave Background (CMB) photon gas scale with redshift under adiabatic expansion. Let's go through each task step by step.

### 1. Scaling of Photon Temperature with Redshift

In an adiabatic expansion, the temperature \( T \) of the photon gas scales inversely with the scale factor \( a \). The scale factor \( a \) is related to the redshift \( z \) by:
\[ a = \frac{1}{1 + z} \]

Given that the temperature today is \( T_0 = 2.725 \) K, the temperature at redshift \( z \) is:
\[ T(z) = T_0 (1 + z) \]

At recombination, \( z = 1100 \), so:
\[ T_{rec} = 2.725 \times (1 + 1100) = 2.725 \times 1101 \]

Calculating this:
\[ T_{rec} = 2.725 \times 1101 = 2999.725 \, \text{K} \]

### 2. Scaling of Photon Number Density

The number density \( n \) of photons scales with the cube of the scale factor \( a \):
\[ n(z) = n_0 \left( \frac{a_0}{a} \right)^3 = n_0 (1 + z)^3 \]

The ratio of the number density at recombination to today is:
\[ \frac{n(z_{rec})}{n_0} = (1 + 1100)^3 = 1101^3 \]

Taking the logarithm base 10:
\[ \log_{10} \left( \frac{n(z_{rec})}{n_0} \right) = 3 \log_{10}(1101) \]

Calculating \( \log_{10}(1101) \):
\[ \log_{10}(1101) \approx 3.0414 \]

Thus:
\[ \log_{10} \left( \frac{n(z_{rec})}{n_0} \right) \approx 3 \times 3.0414 = 9.1242 \]

### 3. Scaling of Photon Energy Density

The energy density \( \rho \) of photons scales with the fourth power of the scale factor \( a \):
\[ \rho(z) = \rho_0 \left( \frac{a_0}{a} \right)^4 = \rho_0 (1 + z)^4 \]

The ratio of the energy density at recombination to today is:
\[ \frac{\rho(z_{rec})}{\rho_0} = (1 + 1100)^4 = 1101^4 \]

Taking the logarithm base 10:
\[ \log_{10} \left( \frac{\rho(z_{rec})}{\rho_0} \right) = 4 \log_{10}(1101) \]

Using the same value for \( \log_{10}(1101) \):
\[ \log_{10} \left( \frac{\rho(z_{rec})}{\rho_0} \right) \approx 4 \times 3.0414 = 12.1656 \]

The extra factor of \( (1 + z) \) relative to the number density comes from the fact that the energy of each photon scales with \( (1 + z) \), in addition to the number density scaling with \( (1 + z)^3 \).

### 4. Why the CMB Remains a Perfect Blackbody

The CMB remains a perfect blackbody as it redshifts because the adiabatic expansion of the universe does not introduce any new processes that would disturb the thermal equilibrium of the photon gas. The photons simply redshift, maintaining their blackbody spectrum but at a lower temperature. No rethermalization is needed because the expansion is adiabatic, meaning there is no heat exchange with the surroundings.

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{T\_rec\_K} &= 2999.725 \\
\mathrm{log10\_number\_ratio} &= 9.1242 \\
\mathrm{log10\_energy\_ratio} &= 12.1656
\end{aligned}
\]