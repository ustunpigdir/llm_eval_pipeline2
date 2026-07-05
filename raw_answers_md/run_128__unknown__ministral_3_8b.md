### **1. Photon Temperature Scaling with Redshift**

The CMB is a blackbody photon gas undergoing **adiabatic expansion**. For a photon gas, the temperature scales with the scale factor \(a\) as:

\[
T \propto \frac{1}{a}
\]

Since redshift \(z\) is defined by \(1 + z = a_0 / a\), where \(a_0\) is the present scale factor, we can rewrite this as:

\[
T(z) = T_0 (1 + z)
\]

This is because \(a \propto 1/(1+z)\), so \(T \propto (1+z)\).

Now, evaluating \(T\) at recombination (\(z = 1100\)):

\[
T_{\text{rec}} = T_0 (1 + z_{\text{rec}}) = 2.725 \, \text{K} \times (1 + 1100) = 2.725 \times 1101 \approx 3000 \, \text{K}
\]

---

### **2. Photon Number Density Scaling**

The number density of photons \(n\) scales as:

\[
n \propto \frac{1}{a^3}
\]

This is because the volume scales as \(a^3\), and the number of photons is conserved in adiabatic expansion (no creation or annihilation).

In terms of redshift:

\[
n(z) = n_0 \left( \frac{a_0}{a} \right)^3 = n_0 (1 + z)^3
\]

Thus, the ratio is:

\[
\frac{n(z_{\text{rec}})}{n_0} = (1 + z_{\text{rec}})^3 = (1101)^3
\]

Taking the logarithm base 10:

\[
\log_{10} \left( \frac{n(z_{\text{rec}})}{n_0} \right) = 3 \log_{10}(1101)
\]

Calculating \(\log_{10}(1101)\):

\[
\log_{10}(1101) \approx 3.0418
\]

Thus:

\[
\log_{10} \left( \frac{n(z_{\text{rec}})}{n_0} \right) \approx 3 \times 3.0418 = 9.1254
\]

---

### **3. Photon Energy Density Scaling**

The energy density of photons \(\rho\) is given by:

\[
\rho = a T^4
\]

where \(a\) is the radiation constant. Since \(T \propto 1/a\), we have:

\[
\rho \propto \frac{1}{a^4}
\]

In terms of redshift:

\[
\rho(z) = \rho_0 \left( \frac{a_0}{a} \right)^4 = \rho_0 (1 + z)^4
\]

Thus, the ratio is:

\[
\frac{\rho(z_{\text{rec}})}{\rho_0} = (1 + z_{\text{rec}})^4 = (1101)^4
\]

Taking the logarithm base 10:

\[
\log_{10} \left( \frac{\rho(z_{\text{rec}})}{\rho_0} \right) = 4 \log_{10}(1101) \approx 4 \times 3.0418 = 12.1672
\]

#### **Explanation of the Extra Factor of \((1+z)\) Relative to Number Density**

- The **number density** scales as \(n \propto (1+z)^3\) because the volume scales as \(a^{-3} = (1+z)^3\).
- The **energy density** scales as \(\rho \propto T^4 \propto (1/a)^4 = (1+z)^4\) because the energy of each photon scales as \(T\) (due to redshift), and there are \((1+z)^3\) photons per unit volume. However, the energy per photon also scales as \(T\), so the total energy density scales as \((1+z)^3 \times T \propto (1+z)^3 \times (1+z) = (1+z)^4\).

---

### **4. Why the CMB Remains a Perfect Blackbody**

The CMB remains a perfect blackbody because:

1. **Adiabatic expansion preserves the blackbody spectrum**: As the universe expands, photons redshift, but the relative occupation numbers of different photon energies remain unchanged. This is because the expansion is homogeneous and isotropic, and there are no interactions that would alter the distribution function (e.g., no scattering or absorption that would distort the spectrum).

2. **No rethermalization is required**: The blackbody spectrum is preserved by the **redshift of individual photons**, not by collisions or interactions. The shape of the spectrum is determined by the distribution of energies, and since all photons redshift uniformly, the shape remains unchanged.

3. **Photon-photon and photon-matter interactions are negligible at late times**: After recombination, the CMB photons are free-streaming, and their interactions with matter are minimal. The only effect is the uniform redshift due to cosmic expansion.

---

### **FINAL ANSWER**

\[
\begin{aligned}
\mathrm{T\_rec\_K} &= 3000 \\
\mathrm{log10\_number\_ratio} &= 9.1254 \\
\mathrm{log10\_energy\_ratio} &= 12.1672 \\
\end{aligned}
\]