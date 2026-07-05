**Solution:**

1. **Photon Temperature Scaling:**
   The photon temperature scales inversely with the scale factor $a$. Since $T_0 = 2.725$ K, at recombination ($z = 1100$), the temperature is:
   \[
   T_{rec} = T_0 (1 + z_{rec})^{-1} = 2.725 \times (1 + 1100)^{-1} \approx 0.235 \text{ K}
   \]

2. **Photon Number Density Scaling:**
   The number density of photons scales as $a^{-3}$. Thus, the ratio of number densities at recombination to today is:
   \[
   \frac{n(z_{rec})}{n_0} = (1 + z_{rec})^{-3} \implies \log_{10} \left( \frac{n(z_{rec})}{n_0} \right) = 3 \log_{10} (1 + 1100) \approx -0.42
   \]

3. **Photon Energy Density Scaling:**
   The energy density of photons scales as $a^{-4}$. Thus, the ratio of energy densities at recombination to today is:
   \[
   \frac{\rho(z_{rec})}{\rho_0} = (1 + z_{rec})^{-4} \implies \log_{10} \left( \frac{\rho(z_{rec})}{\rho_0} \right) = 4 \log_{10} (1 + 1100) \approx -1.68
   \]
   The extra factor of $(1+z)$ comes from the fact that the energy of each photon redshifts as $E \propto a^{-1}$, so the total energy density redshifts faster than the number density.

4. **CMB Remaining a Perfect Blackbody:**
   The CMB remains a perfect blackbody as it redshifts because photons do not interact with each other or other particles in the universe after recombination. The blackbody spectrum is preserved because the photons are redshifted but not scattered or absorbed.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{T\_rec\_K} &= 0.235 \text{ K} \\
\mathrm{log10\_number\_ratio} &= -0.42 \\
\mathrm{log10\_energy\_ratio} &= -1.68
\end{aligned}
\]