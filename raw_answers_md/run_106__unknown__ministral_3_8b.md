### Task 1: Evaluate the Hubble time in Gyr

The Hubble time is defined as \( t_H = \frac{1}{H_0} \). We are given \( H_0 = 70.0 \, \text{km/s/Mpc} \).

First, we need to convert \( H_0 \) into units of \( \text{s}^{-1} \) to compute \( t_H \) in seconds, then convert to gigayears (Gyr).

#### Step 1: Convert Mpc to km
Given \( 1 \, \text{Mpc} = 3.0857 \times 10^{19} \, \text{km} \), so:
\[
H_0 = 70.0 \, \frac{\text{km/s}}{\text{Mpc}} = 70.0 \times \frac{\text{km/s}}{3.0857 \times 10^{19} \, \text{km}} = \frac{70.0}{3.0857 \times 10^{19}} \, \text{s}^{-1}
\]

#### Step 2: Compute \( H_0 \) in \( \text{s}^{-1} \)
\[
H_0 = \frac{70.0}{3.0857 \times 10^{19}} \approx 2.268 \times 10^{-18} \, \text{s}^{-1}
\]

#### Step 3: Compute Hubble time \( t_H = \frac{1}{H_0} \) in seconds
\[
t_H = \frac{1}{2.268 \times 10^{-18}} \approx 4.409 \times 10^{17} \, \text{s}
\]

#### Step 4: Convert \( t_H \) to Gyr
We know that:
\[
1 \, \text{Gyr} = 10^9 \, \text{yr} = 10^9 \times 365.25 \times 24 \times 3600 \, \text{s} \approx 3.15576 \times 10^{16} \, \text{s}
\]
Thus:
\[
t_H = \frac{4.409 \times 10^{17}}{3.15576 \times 10^{16}} \approx 13.97 \, \text{Gyr}
\]

### Task 2: Evaluate the age of a flat matter-only universe in Gyr

For a flat matter-only universe (Einstein-de Sitter), the age \( t_0 \) is given by:
\[
t_0 = \frac{2}{3} \frac{1}{H_0}
\]
This is because the scale factor \( a(t) \propto t^{2/3} \) in this case, and the age is \( \frac{2}{3} t_H \).

#### Step 1: Compute \( t_0 \) in seconds
\[
t_0 = \frac{2}{3} \times 4.409 \times 10^{17} \approx 2.939 \times 10^{17} \, \text{s}
\]

#### Step 2: Convert to Gyr
\[
t_0 = \frac{2.939 \times 10^{17}}{3.15576 \times 10^{16}} \approx 9.31 \, \text{Gyr}
\]

#### Why is this less than \( 1/H_0 \)?
In a matter-dominated universe, the expansion slows down over time, so the universe is younger than the Hubble time. The age is \( \frac{2}{3} t_H \) because the scale factor grows as \( t^{2/3} \), not linearly.

---

### Task 3: Evaluate the LCDM age in Gyr with the given formula

The LCDM age is given by:
\[
t_0 = \frac{2}{3 H_0 \sqrt{\Omega_\Lambda}} \, \text{asinh} \left( \sqrt{\frac{\Omega_\Lambda}{\Omega_m}} \right)
\]
with \( \Omega_m = 0.3 \), \( \Omega_\Lambda = 0.7 \).

#### Step 1: Compute \( \sqrt{\Omega_\Lambda} \)
\[
\sqrt{\Omega_\Lambda} = \sqrt{0.7} \approx 0.83666
\]

#### Step 2: Compute \( \sqrt{\Omega_\Lambda / \Omega_m} \)
\[
\sqrt{\frac{\Omega_\Lambda}{\Omega_m}} = \sqrt{\frac{0.7}{0.3}} \approx \sqrt{2.333} \approx 1.5275
\]

#### Step 3: Compute \( \text{asinh}(1.5275) \)
The inverse hyperbolic sine is:
\[
\text{asinh}(x) = \ln(x + \sqrt{x^2 + 1})
\]
\[
\text{asinh}(1.5275) = \ln(1.5275 + \sqrt{1.5275^2 + 1}) \approx \ln(1.5275 + \sqrt{2.333 + 1}) \approx \ln(1.5275 + 1.8257) \approx \ln(3.3532) \approx 1.210
\]

#### Step 4: Compute the denominator \( 3 H_0 \sqrt{\Omega_\Lambda} \)
We already have \( H_0 \approx 2.268 \times 10^{-18} \, \text{s}^{-1} \), so:
\[
3 H_0 \sqrt{\Omega_\Lambda} = 3 \times 2.268 \times 10^{-18} \times 0.83666 \approx 5.878 \times 10^{-18} \, \text{s}^{-1}
\]

#### Step 5: Compute \( t_0 \) in seconds
\[
t_0 = \frac{2}{5.878 \times 10^{-18}} \times 1.210 \approx \frac{2.420}{5.878 \times 10^{-18}} \approx 4.117 \times 10^{17} \, \text{s}
\]

#### Step 6: Convert to Gyr
\[
t_0 = \frac{4.117 \times 10^{17}}{3.15576 \times 10^{16}} \approx 13.05 \, \text{Gyr}
\]

---

### Task 4: Explain why the LCDM age comes out close to \( 1/H_0 \)

The LCDM age is close to the Hubble time because:
1. **Early deceleration**: In the past, matter dominated, and the universe expanded slowly (decelerated). This means the universe was younger than the Hubble time in the early stages.
2. **Late acceleration**: In the recent past, dark energy dominated, causing the universe to accelerate. This acceleration means the universe is "catching up" in age relative to the Hubble time, making the age closer to \( 1/H_0 \).

The combination of these two effects (early deceleration and late acceleration) results in the age being approximately equal to the Hubble time, unlike the matter-only case where the age is significantly less.

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{hubble\_time\_gyr} &= 13.97 \\
\mathrm{matter\_age\_gyr} &= 9.31 \\
\mathrm{lcdm\_age\_gyr} &= 13.05
\end{aligned}
\]