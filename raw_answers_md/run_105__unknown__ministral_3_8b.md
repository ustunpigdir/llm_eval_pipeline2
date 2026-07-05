### 1. Hubble Time in Gyr

The Hubble time is defined as \( t_H = \frac{1}{H_0} \). We are given \( H_0 = 70.0 \, \text{km/s/Mpc} \).

First, convert \( H_0 \) to SI units to compute \( t_H \):

- \( 1 \, \text{Mpc} = 3.0857 \times 10^{19} \, \text{km} \), so
  \[
  H_0 = 70.0 \, \frac{\text{km/s}}{\text{Mpc}} = 70.0 \times \frac{1 \, \text{km/s}}{3.0857 \times 10^{19} \, \text{km}} = \frac{70.0}{3.0857 \times 10^{19}} \, \text{s}^{-1}.
  \]

- Compute the numerical value:
  \[
  H_0 = \frac{70.0}{3.0857 \times 10^{19}} \approx 2.268 \times 10^{-18} \, \text{s}^{-1}.
  \]

- The Hubble time is:
  \[
  t_H = \frac{1}{H_0} = \frac{1}{2.268 \times 10^{-18}} \approx 4.41 \times 10^{17} \, \text{s}.
  \]

- Convert seconds to gigayears (Gyr):
  \[
  1 \, \text{Gyr} = 3.154 \times 10^{16} \, \text{s},
  \]
  so
  \[
  t_H = \frac{4.41 \times 10^{17}}{3.154 \times 10^{16}} \approx 13.98 \, \text{Gyr}.
  \]

### 2. Age of a Flat Matter-Only Universe in Gyr

For a flat matter-only (Einstein-de Sitter) universe, the age \( t_0 \) is given by:
\[
t_0 = \frac{2}{3 H_0}.
\]

Using \( H_0 = 2.268 \times 10^{-18} \, \text{s}^{-1} \):
\[
t_0 = \frac{2}{3 \times 2.268 \times 10^{-18}} = \frac{2}{6.804 \times 10^{-18}} \approx 2.94 \times 10^{17} \, \text{s}.
\]

Convert to Gyr:
\[
t_0 = \frac{2.94 \times 10^{17}}{3.154 \times 10^{16}} \approx 9.32 \, \text{Gyr}.
\]

**Why is this less than \( 1/H_0 \)?**
In a matter-only universe, the expansion rate \( H(t) \) decreases over time (decelerating expansion), so the universe is younger than the Hubble time. The factor \( \frac{2}{3} \) arises from integrating the Friedmann equation for a matter-dominated universe:
\[
t = \frac{2}{3 H_0}.
\]

### 3. LCDM Age in Gyr

For the flat LCDM model with \( \Omega_m = 0.3 \) and \( \Omega_\Lambda = 0.7 \), the age is given by:
\[
t_0 = \frac{2}{3 H_0 \sqrt{\Omega_\Lambda}} \, \mathrm{asinh}\left( \sqrt{\frac{\Omega_\Lambda}{\Omega_m}} \right).
\]

First, compute \( \sqrt{\Omega_\Lambda} \) and \( \sqrt{\frac{\Omega_\Lambda}{\Omega_m}} \):
\[
\sqrt{\Omega_\Lambda} = \sqrt{0.7} \approx 0.8367,
\]
\[
\sqrt{\frac{\Omega_\Lambda}{\Omega_m}} = \sqrt{\frac{0.7}{0.3}} \approx \sqrt{2.333} \approx 1.5275.
\]

Now compute \( \mathrm{asinh}(1.5275) \):
\[
\mathrm{asinh}(x) = \ln(x + \sqrt{x^2 + 1}),
\]
so
\[
\mathrm{asinh}(1.5275) = \ln(1.5275 + \sqrt{1.5275^2 + 1}) = \ln(1.5275 + \sqrt{2.333 + 1}) = \ln(1.5275 + 1.8257) = \ln(3.3532) \approx 1.210.
\]

Now plug into the age formula:
\[
t_0 = \frac{2}{3 \times 2.268 \times 10^{-18} \times 0.8367} \times 1.210.
\]

First compute the denominator:
\[
3 \times 2.268 \times 10^{-18} \times 0.8367 \approx 5.80 \times 10^{-18}.
\]

Now compute the age:
\[
t_0 = \frac{2}{5.80 \times 10^{-18}} \times 1.210 \approx 3.45 \times 10^{17} \times 1.210 \approx 4.17 \times 10^{17} \, \text{s}.
\]

Convert to Gyr:
\[
t_0 = \frac{4.17 \times 10^{17}}{3.154 \times 10^{16}} \approx 13.22 \, \text{Gyr}.
\]

### 4. Why the LCDM Age is Close to \( 1/H_0 \)

The LCDM age is close to the Hubble time due to the interplay of early deceleration and late acceleration:

- **Early deceleration**: In the past, the universe was matter-dominated, so expansion was decelerating, making the age less than \( 1/H_0 \) if only matter were present.
- **Late acceleration**: The presence of dark energy (cosmological constant) causes the expansion to accelerate in the recent past. This acceleration "stretches" the age closer to \( 1/H_0 \), as the universe spends more time expanding slowly in the distant past and more time expanding rapidly in the recent past.

The exact balance of these effects leads to the LCDM age being close to the Hubble time.

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{hubble\_time\_gyr} &= 13.98 \\
\mathrm{matter\_age\_gyr} &= 9.32 \\
\mathrm{lcdm\_age\_gyr} &= 13.22 \\
\end{aligned}
\]