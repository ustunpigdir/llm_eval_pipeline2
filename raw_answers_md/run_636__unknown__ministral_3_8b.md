### Derivation of the BEC Critical Temperature \( k_B T_c \)

We start with the condition for Bose-Einstein condensation (BEC) in an ideal gas, which occurs when the thermal de Broglie wavelength \(\lambda_T\) satisfies the relation:

\[
n \lambda_T^3 = \zeta\left(\frac{3}{2}\right) = 2.612,
\]

where:
- \( n \) is the particle density,
- \( \lambda_T \) is the thermal de Broglie wavelength,
- \( \zeta(3/2) \) is the Riemann zeta function evaluated at \( 3/2 \), which accounts for the quantum statistical effects in the ideal Bose gas.

The thermal de Broglie wavelength is given by:

\[
\lambda_T = \sqrt{\frac{2 \pi \hbar^2}{m k_B T}},
\]

where:
- \( \hbar \) is the reduced Planck constant,
- \( m \) is the mass of the particle,
- \( k_B \) is the Boltzmann constant,
- \( T \) is the temperature.

Substitute \(\lambda_T\) into the BEC condition:

\[
n \left( \sqrt{\frac{2 \pi \hbar^2}{m k_B T}} \right)^3 = 2.612.
\]

Simplify the expression inside the parentheses:

\[
n \left( \frac{2 \pi \hbar^2}{m k_B T} \right)^{3/2} = 2.612.
\]

Rearrange to solve for \( T \):

\[
\left( \frac{2 \pi \hbar^2}{m k_B T} \right)^{3/2} = \frac{2.612}{n}.
\]

Take both sides to the power of \( \frac{2}{3} \):

\[
\frac{2 \pi \hbar^2}{m k_B T} = \left( \frac{2.612}{n} \right)^{2/3}.
\]

Now, solve for \( k_B T \):

\[
k_B T = \frac{2 \pi \hbar^2}{m} \left( \frac{n}{2.612} \right)^{2/3}.
\]

Since \( \zeta(3/2) = 2.612 \), we can write:

\[
k_B T_c = \frac{2 \pi \hbar^2}{m} \left( \frac{n}{\zeta(3/2)} \right)^{2/3}.
\]

This is the desired expression for the critical temperature \( T_c \).

---

### Evaluation of \( T_c \) in nanokelvin (nK)

Given:
- \( n = 1.00 \times 10^{19} \, \text{m}^{-3} \),
- \( m = 1.443 \times 10^{-25} \, \text{kg} \),
- \( \zeta(3/2) = 2.612 \),
- \( \hbar = 1.0545718 \times 10^{-34} \, \text{J s} \),
- \( k_B = 1.380649 \times 10^{-23} \, \text{J K}^{-1} \).

Substitute these values into the expression for \( k_B T_c \):

\[
k_B T_c = \frac{2 \pi (1.0545718 \times 10^{-34})^2}{1.443 \times 10^{-25}} \left( \frac{1.00 \times 10^{19}}{2.612} \right)^{2/3}.
\]

First, compute the numerator:

\[
2 \pi (1.0545718 \times 10^{-34})^2 = 2 \pi (1.112 \times 10^{-68}) = 6.96 \times 10^{-68} \, \text{J}^2 \text{s}^2.
\]

Now, divide by the mass:

\[
\frac{6.96 \times 10^{-68}}{1.443 \times 10^{-25}} = 4.82 \times 10^{-43} \, \text{J s}^2 \text{ kg}^{-1}.
\]

Next, compute the term inside the parentheses:

\[
\frac{1.00 \times 10^{19}}{2.612} = 3.83 \times 10^{18}.
\]

Now, raise this to the power of \( \frac{2}{3} \):

\[
(3.83 \times 10^{18})^{2/3} = (3.83)^{2/3} \times (10^{18})^{2/3}.
\]

Calculate \( (3.83)^{2/3} \):

\[
(3.83)^{2/3} \approx 2.48.
\]

Calculate \( (10^{18})^{2/3} \):

\[
(10^{18})^{2/3} = 10^{12}.
\]

Thus:

\[
(3.83 \times 10^{18})^{2/3} \approx 2.48 \times 10^{12}.
\]

Now, multiply by the previous result:

\[
k_B T_c = 4.82 \times 10^{-43} \times 2.48 \times 10^{12} = 1.19 \times 10^{-30} \, \text{J}.
\]

Finally, divide by \( k_B \) to find \( T_c \):

\[
T_c = \frac{1.19 \times 10^{-30}}{1.380649 \times 10^{-23}} = 8.62 \times 10^{-8} \, \text{K} = 86.2 \, \text{nK}.
\]

---

### Phase-Space Density at \( T_c \) and \( 2 T_c \)

At \( T_c \), the phase-space density is defined by the BEC condition:

\[
n \lambda_T^3 = \zeta(3/2) = 2.612.
\]

At \( 2 T_c \), the thermal de Broglie wavelength changes as \( \lambda_T \propto T^{-1/2} \), so:

\[
\lambda_{2T_c} = \lambda_{T_c} \times \sqrt{\frac{T_c}{2 T_c}} = \lambda_{T_c} \times \frac{1}{\sqrt{2}}.
\]

Thus:

\[
n \lambda_{2T_c}^3 = n \left( \frac{\lambda_{T_c}}{\sqrt{2}} \right)^3 = n \lambda_{T_c}^3 \times \frac{1}{2^{3/2}} = 2.612 \times \frac{1}{2^{3/2}}.
\]

Calculate \( 2^{3/2} \):

\[
2^{3/2} = 2 \sqrt{2} \approx 2.828.
\]

Thus:

\[
n \lambda_{2T_c}^3 = \frac{2.612}{2.828} \approx 0.924.
\]

---

### Evaluation of \( T_c \) if \( \zeta(3/2) \) is Dropped (i.e., \( n \lambda^3 = 1 \))

If the student drops \( \zeta(3/2) \) and sets \( n \lambda_T^3 = 1 \), the condition becomes:

\[
n \left( \frac{2 \pi \hbar^2}{m k_B T} \right)^{3/2} = 1.
\]

Following the same steps as before:

\[
\left( \frac{2 \pi \hbar^2}{m k_B T} \right)^{3/2} = \frac{1}{n}.
\]

Taking to the power of \( \frac{2}{3} \):

\[
\frac{2 \pi \hbar^2}{m k_B T} = \left( \frac{1}{n} \right)^{2/3}.
\]

Solving for \( k_B T \):

\[
k_B T = \frac{2 \pi \hbar^2}{m} n^{2/3}.
\]

Now, substitute the values:

\[
k_B T_c = 4.82 \times 10^{-43} \times (1.00 \times 10^{19})^{2/3}.
\]

Calculate \( (1.00 \times 10^{19})^{2/3} \):

\[
(1.00 \times 10^{19})^{2/3} = 10^{12.666} \approx 4.64 \times 10^{12}.
\]

Thus:

\[
k_B T_c = 4.82 \times 10^{-43} \times 4.64 \times 10^{12} = 2.23 \times 10^{-30} \, \text{J}.
\]

Now, divide by \( k_B \):

\[
T_c = \frac{2.23 \times 10^{-30}}{1.380649 \times 10^{-23}} = 1.61 \times 10^{-7} \, \text{K} = 161 \, \text{nK}.
\]

**Physical Meaning of \( \zeta(3/2) = 2.612 \):**
The zeta function \( \zeta(3/2) \) accounts for the quantum statistical distribution of bosons in the ideal gas. It represents the normalization factor for the Bose-Einstein distribution summed over all quantum states (excluding the ground state, which is occupied by the condensate). Without this factor, the critical temperature would be overestimated because the phase-space density condition would not correctly account for the occupation of excited states. The factor \( 2.612 \) ensures that the correct fraction of particles occupy the excited states at \( T_c \), leading to the correct critical temperature.

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{tc\_nK} &= 86.2 \\
\mathrm{phase\_space\_density\_tc} &= 2.612 \\
\mathrm{psd\_at\_2tc} &= 0.924 \\
\mathrm{tc\_no\_zeta\_nK} &= 161
\end{aligned}
\]