**Derivation Steps**

1. **Photon temperature scaling with redshift**  
   For an adiabatically expanding blackbody photon gas, the temperature scales inversely with the scale factor \(a\):  
   \[
   T \propto \frac{1}{a} \quad \Rightarrow \quad T(z) = \frac{T_0}{1+z},
   \]
   where \(T_0 = 2.725\ \text{K}\) is the present‑day CMB temperature.

   At recombination, \(z_{\text{rec}} = 1100\):  
   \[
   T_{\text{rec}} = \frac{2.725\ \text{K}}{1 + 1100} = \frac{2.725}{1101}\ \text{K}
   \approx 0.002475\ \text{K}.
   \]

2. **Photon number density scaling**  
   The number density of photons follows the volume expansion as \(n \propto a^{-3}\). Hence:  
   \[
   \frac{n(z)}{n_0} = \left(\frac{a_0}{a(z)}\right)^3 = (1+z)^3.
   \]

   Taking the base‑10 logarithm:  
   \[
   \log_{10}\!\left(\frac{n(z)}{n_0}\right) = \log_{10}\bigl[(1+z)^3\bigr] = 3\log_{10}(1+z).
   \]

   For \(z = 1100\):  
   \[
   \log_{10}\!\left(\frac{n(z_{\text{rec}})}{n_0}\right) = 3\log_{10}(1101) \approx 3 \times 3.0414 \approx 9.124.
   \]

3. **Photon energy density scaling**  
   The energy density of a blackbody photon gas scales as \(\rho \propto a^{-4}\) (since each photon's energy scales as \(T\) and the number density scales as \(a^{-3}\)):  
   \[
   \frac{\rho(z)}{\rho_0} = \left(\frac{a_0}{a(z)}\right)^4 = (1+z)^4.
   \]

   Taking the base‑10 logarithm:  
   \[
   \log_{10}\!\left(\frac{\rho(z)}{\rho_0}\right) = \log_{10}\bigl[(1+z)^4\bigr] = 4\log_{10}(1+z).
   \]

   For \(z = 1100\):  
   \[
   \log_{10}\!\left(\frac{\rho(z_{\text{rec}})}{\rho_0}\right) = 4\log_{10}(1101) \approx 4 \times 3.0414 \approx 12.166.
   \]

   **Explanation of the extra factor \((1+z)\):**  
   The number density scales as \(a^{-3}\) because the photon count per comoving volume decreases with the expansion. Energy density, however, also includes the redshift of each photon's energy (\(E \propto T \propto a^{-1}\)). Multiplying the energy per photon by the number density gives an extra factor of \(a^{-1}\), leading to \(a^{-4}\) overall.

4. **Why the CMB remains a perfect blackbody**  
   The CMB photons decouple from matter at recombination and subsequently undergo only gravitational redshift and the universal expansion. These processes are linear and conserve the detailed spectral shape of a blackbody: each photon's frequency is uniformly stretched by the same factor \((1+z)\). No scattering, absorption, or emission processes redistribute photon energies during this adiabatic expansion, so the Planck spectrum is preserved. Thus, the CMB remains an ideal blackbody without any need for rethermalization.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{T\_rec\_K} &= \frac{2.725}{1101} \approx 0.002475\ \text{K},\\[4pt]
\mathrm{log10\_number\_ratio} &= 3\log_{10}(1101) \approx 9.124,\\[4pt]
\mathrm{log10\_energy\_ratio} &= 4\log_{10}(1101) \approx 12.166.
\end{aligned}
\]