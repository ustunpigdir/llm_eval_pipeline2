**Derivation:**

1. **Resonance Condition:**
   The wavefunction inside the well is given by $\psi(x) = A \sin(k'x + \phi)$, where $k' = \sqrt{2m(E+V_0)}/\hbar$. For perfect transmission, the wavefunction must match at the boundaries, i.e., $\psi(0) = \psi(L)$. This gives us:
   \[
   A \sin(\phi) = A \sin(k'L + \phi)
   \]
   Since $A \neq 0$, we have:
   \[
   \sin(k'L) = \sin(\phi)
   \]
   Using the identity $\sin(\theta) = \sin(\theta + n\pi)$, we get:
   \[
   k'L = n\pi \quad \text{where } n \in \mathbb{Z}
   \]
   Solving for $E$, we get:
   \[
   E = \frac{n^2 \pi^2 \hbar^2}{2mL^2} - V_0
   \]

2. **Energy Unit in eV:**
   \[
   \text{Energy unit} = \frac{\pi^2 \hbar^2}{2mL^2} = \frac{(3.14159)^2 (1.05457 \times 10^{-34})^2}{2 \times 9.10939 \times 10^{-31} \times (4.00 \times 10^{-10})^2} \approx 1.23 \times 10^{-4} \text{ eV}
   \]

3. **Smallest $n$ with $E_n > 0$:**
   We need to find the smallest $n$ such that:
   \[
   \frac{n^2 \pi^2 \hbar^2}{2mL^2} > V_0
   \]
   Substituting the values, we get:
   \[
   n^2 > \frac{2mL^2 V_0}{\pi^2 \hbar^2} \approx \frac{2 \times 9.10939 \times 10^{-31} \times (4.00 \times 10^{-10})^2 \times 10.0}{3.14159^2 \times (1.05457 \times 10^{-34})^2} \approx 1.61
   \]
   The smallest integer $n$ satisfying this is $n = 2$.

4. **Ramsauer-Townsend Minimum:**
   The electron transmits perfectly at special energies because the de Broglie wavelength inside the well matches the width of the well. This is a resonant scattering phenomenon, where the incident wave interferes constructively with the scattered wave.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{energy\_unit\_ev} &= 1.23 \times 10^{-4} \text{ eV} \\
\mathrm{n\_lowest} &= 2 \\
\mathrm{first\_resonance\_ev} &= \frac{2^2 \pi^2 \hbar^2}{2mL^2} - V_0 \approx 1.23 \times 10^{-4} \text{ eV} - 10.0 \text{ eV} = -9.999877 \text{ eV}
\end{aligned}
\]