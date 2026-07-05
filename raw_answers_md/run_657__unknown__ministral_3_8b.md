### Task 1: Mean-field estimate of \( k_B T_c^{MF}/J \)

The mean-field approximation for the ferromagnetic Ising model assumes that each spin interacts with an average (mean-field) magnetization rather than with its neighbors explicitly. The mean-field Hamiltonian is given by:

\[
\mathcal{H}_{MF} = -J z m S_i - \mu_0 H m N,
\]

where \( m \) is the average magnetization per spin (\( m = \langle S_i \rangle \)), \( z \) is the coordination number (4 for the square lattice), and \( H = 0 \) (zero external field). The mean-field critical temperature \( T_c^{MF} \) is derived from the self-consistency condition for the magnetization:

\[
m = \tanh\left(\frac{J z m}{k_B T}\right).
\]

At the critical point, the magnetization \( m \) vanishes (\( m \to 0 \)), and we linearize the equation:

\[
m \approx \frac{J z m}{k_B T} \implies T_c^{MF} = \frac{J z}{k_B}.
\]

Thus, the dimensionless mean-field critical temperature is:

\[
\frac{k_B T_c^{MF}}{J} = z = 4.
\]

### Task 2: Onsager's exact result for the 2D Ising model

Onsager solved the 2D Ising model exactly in 1944 and found the critical temperature to be:

\[
\frac{k_B T_c}{J} = \frac{2}{\ln(1 + \sqrt{2})}.
\]

This result is exact and does not rely on approximations. Numerically, this evaluates to:

\[
\frac{2}{\ln(1 + \sqrt{2})} \approx \frac{2}{\ln(1 + 1.4142)} \approx \frac{2}{\ln(2.4142)} \approx \frac{2}{0.8814} \approx 2.2692.
\]

### Task 3: Ratio \( T_c^{exact}/T_c^{MF} \) and why mean field overestimates \( T_c \)

The ratio of the exact critical temperature to the mean-field critical temperature is:

\[
\frac{T_c^{exact}}{T_c^{MF}} = \frac{\frac{2}{\ln(1 + \sqrt{2})}}{4} = \frac{2}{4 \ln(1 + \sqrt{2})} = \frac{1}{2 \ln(1 + \sqrt{2})}.
\]

Numerically:

\[
\frac{1}{2 \ln(1 + \sqrt{2})} \approx \frac{1}{2 \times 0.8814} \approx \frac{1}{1.7628} \approx 0.5674.
\]

Mean field overestimates \( T_c \) because it neglects fluctuations. In low dimensions (like 2D), thermal fluctuations are significant and reduce the effective interaction strength, lowering the actual critical temperature compared to the mean-field prediction. The mean-field approximation assumes that the system is always in a state where local interactions are averaged over, but in reality, fluctuations (e.g., spin waves, domain walls) play a crucial role in stabilizing the disordered phase at lower temperatures.

### Task 4: One-dimensional Ising model

In one dimension (\( z = 2 \)), the Ising model does not exhibit a phase transition at any finite temperature. The exact solution (derived by Onsager in 1D) shows that the partition function can be computed exactly, and the magnetization decays exponentially with temperature:

\[
m(T) = \left(\frac{\tanh(\beta J)}{\sqrt{1 - \tanh^2(\beta J)}}\right)^{1/2},
\]

where \( \beta = \frac{1}{k_B T} \). However, as \( T \to 0 \), \( m(T) \to 1 \), and as \( T \to \infty \), \( m(T) \to 0 \), but there is no discontinuity or divergence in the susceptibility or magnetization at any finite temperature. Thus, there is no phase transition in 1D.

The physical reason is that in 1D, thermal fluctuations are so strong that they can always "flip" spins to destroy long-range order. The correlation length remains finite at all temperatures, and the system remains disordered at all \( T > 0 \).

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{tc\_exact} &= \frac{2}{\ln(1+\sqrt{2})}, \\
\mathrm{tc\_meanfield} &= 4, \\
\mathrm{ratio\_exact\_mf} &= \frac{1}{2 \ln(1+\sqrt{2})}.
\end{aligned}
\]