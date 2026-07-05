Let's tackle each task step by step.

### 1. Evaluate the Hubble time in Gyr

The Hubble time is defined as \( t_H = \frac{1}{H_0} \).

Given:
- \( H_0 = 70.0 \, \text{km/s/Mpc} \)
- \( 1 \, \text{Mpc} = 3.0857 \times 10^{19} \, \text{km} \)

First, convert \( H_0 \) to units of \( \text{s}^{-1} \):

\[
H_0 = 70.0 \, \text{km/s/Mpc} = 70.0 \times \frac{10^3 \, \text{m}}{3.0857 \times 10^{19} \, \text{m}} \, \text{s}^{-1}
\]

\[
H_0 = 70.0 \times \frac{10^3}{3.0857 \times 10^{19}} \, \text{s}^{-1}
\]

\[
H_0 = 70.0 \times 3.2408 \times 10^{-19} \, \text{s}^{-1}
\]

\[
H_0 \approx 2.2686 \times 10^{-18} \, \text{s}^{-1}
\]

Now, calculate the Hubble time \( t_H \):

\[
t_H = \frac{1}{H_0} = \frac{1}{2.2686 \times 10^{-18}} \, \text{s}
\]

\[
t_H \approx 4.4096 \times 10^{17} \, \text{s}
\]

Convert seconds to years (1 year = \( 3.1536 \times 10^7 \) s):

\[
t_H \approx \frac{4.4096 \times 10^{17}}{3.1536 \times 10^7} \, \text{yr}
\]

\[
t_H \approx 14.01 \, \text{Gyr}
\]

### 2. Evaluate the age of a flat matter-only universe in Gyr, and explain why it is LESS than \( 1/H_0 \)

For a flat matter-only universe (Einstein-de Sitter universe), the age of the universe \( t_0 \) is given by:

\[
t_0 = \frac{2}{3} t_H
\]

\[
t_0 = \frac{2}{3} \times 14.01 \, \text{Gyr}
\]

\[
t_0 \approx 9.34 \, \text{Gyr}
\]

The age of a flat matter-only universe is less than the Hubble time because the expansion of the universe is decelerating due to the gravitational attraction of matter. This deceleration means that the universe has been expanding more slowly in the past, so it takes longer to reach the current state, resulting in a younger age compared to the Hubble time.

### 3. Evaluate the LCDM age in Gyr with the given formula

For a flat LCDM universe with \( \Omega_m = 0.3 \) and \( \Omega_\Lambda = 0.7 \), the age of the universe \( t_0 \) is given by:

\[
t_0 = \frac{2}{3H_0\sqrt{\Omega_\Lambda}} \, \mathrm{asinh}\left(\sqrt{\frac{\Omega_\Lambda}{\Omega_m}}\right)
\]

First, calculate \( \sqrt{\Omega_\Lambda} \) and \( \sqrt{\frac{\Omega_\Lambda}{\Omega_m}} \):

\[
\sqrt{\Omega_\Lambda} = \sqrt{0.7} \approx 0.8367
\]

\[
\sqrt{\frac{\Omega_\Lambda}{\Omega_m}} = \sqrt{\frac{0.7}{0.3}} \approx 1.5275
\]

Next, calculate \( \mathrm{asinh}(1.5275) \). The inverse hyperbolic sine function \( \mathrm{asinh}(x) \) is given by:

\[
\mathrm{asinh}(x) = \ln(x + \sqrt{x^2 + 1})
\]

\[
\mathrm{asinh}(1.5275) = \ln(1.5275 + \sqrt{1.5275^2 + 1})
\]

\[
\mathrm{asinh}(1.5275) = \ln(1.5275 + \sqrt{2.3333 + 1})
\]

\[
\mathrm{asinh}(1.5275) = \ln(1.5275 + 1.8526)
\]

\[
\mathrm{asinh}(1.5275) = \ln(3.3801)
\]

\[
\mathrm{asinh}(1.5275) \approx 1.2176
\]

Now, calculate \( t_0 \):

\[
t_0 = \frac{2}{3 \times 2.2686 \times 10^{-18} \times 0.8367} \times 1.2176
\]

\[
t_0 = \frac{2 \times 1.2176}{3 \times 2.2686 \times 10^{-18} \times 0.8367}
\]

\[
t_0 = \frac{2.4352}{5.6026 \times 10^{-18}}
\]

\[
t_0 \approx 4.3466 \times 10^{17} \, \text{s}
\]

Convert seconds to years:

\[
t_0 \approx \frac{4.3466 \times 10^{17}}{3.1536 \times 10^7} \, \text{yr}
\]

\[
t_0 \approx 13.78 \, \text{Gyr}
\]

### 4. Explain why the LCDM age comes out close to \( 1/H_0 \) (the roles of early deceleration and late acceleration)

The LCDM age comes out close to the Hubble time due to the balance between early deceleration and late acceleration. In the early universe, the expansion was decelerating due to the gravitational attraction of matter, which would normally make the age less than the Hubble time. However, in the late universe, the expansion is accelerating due to the presence of dark energy (cosmological constant), which counteracts the deceleration and brings the age closer to the Hubble time. The combination of these effects results in an age that is close to the Hubble time.

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{hubble\_time\_gyr} &= 14.01 \\
\mathrm{matter\_age\_gyr} &= 9.34 \\
\mathrm{lcdm\_age\_gyr} &= 13.78
\end{aligned}
\]