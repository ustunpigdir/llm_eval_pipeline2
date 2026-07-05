### Task 1: Mean-field estimate for \( k_B T_c^{MF}/J \)

The mean-field approximation for the ferromagnetic Ising model on a lattice with coordination number \( z \) assumes that each spin interacts with an effective field due to the average magnetization of all other spins. The mean-field Hamiltonian is:

\[
\mathcal{H}_{MF} = -J z m \sum_i s_i
\]

where \( m = \langle s_i \rangle \) is the average magnetization. The mean-field critical temperature is derived from the condition that the uniform magnetization becomes unstable to small fluctuations. This occurs when the susceptibility diverges, which happens at:

\[
k_B T_c^{MF} = J z
\]

For the square lattice, \( z = 4 \), so:

\[
k_B T_c^{MF}/J = z = 4
\]

Thus, the mean-field estimate is:

\[
\mathrm{tc\_meanfield} = 4
\]

---

### Task 2: Onsager's exact result for \( k_B T_c/J \)

Onsager solved the 2D Ising model exactly in 1944 and found the critical temperature to be:

\[
k_B T_c/J = \frac{2}{\ln(1 + \sqrt{2})}
\]

This is the exact result for the 2D Ising model on a square lattice. Numerically evaluating this:

\[
\ln(1 + \sqrt{2}) \approx \ln(1 + 1.4142) \approx \ln(2.4142) \approx 0.8814
\]

Thus:

\[
k_B T_c/J \approx \frac{2}{0.8814} \approx 2.2692
\]

So the exact result is:

\[
\mathrm{tc\_exact} = \frac{2}{\ln(1 + \sqrt{2})}
\]

---

### Task 3: Ratio \( T_c^{exact}/T_c^{MF} \) and why mean field overestimates \( T_c \)

The ratio is:

\[
\frac{T_c^{exact}}{T_c^{MF}} = \frac{\frac{2}{\ln(1 + \sqrt{2})}}{4} = \frac{2}{4 \ln(1 + \sqrt{2})} = \frac{1}{2 \ln(1 + \sqrt{2})}
\]

Numerically:

\[
\frac{1}{2 \times 0.8814} \approx \frac{1}{1.7628} \approx 0.5674
\]

Thus:

\[
\mathrm{ratio\_exact\_mf} = \frac{1}{2 \ln(1 + \sqrt{2})}
\]

#### Why mean field overestimates \( T_c \):

Mean-field theory ignores spatial fluctuations and correlations between spins beyond nearest neighbors. In low dimensions (like 2D), fluctuations are significant and reduce the effective interaction strength, lowering the critical temperature below the mean-field prediction. The mean-field approximation assumes that the system behaves as if each spin interacts with the average magnetization of all other spins, which is a poor approximation in low dimensions where correlations decay slowly.

---

### Task 4: One-dimensional Ising model

#### Exact 1D result:
The 1D Ising model has no phase transition at finite temperature. The exact solution (transfer matrix method) shows that the magnetization decays exponentially with temperature, and there is no critical temperature where the susceptibility diverges. Thus, the critical temperature is:

\[
\mathrm{INVALID}
\]

#### Physical reason:
In one dimension, thermal fluctuations are strong enough to completely destroy long-range order. The correlations between spins decay exponentially with distance, and there is no phase transition to a ferromagnetic state at any finite temperature. This is a consequence of the Mermin-Wagner theorem, which states that continuous symmetries cannot be spontaneously broken in systems with short-range interactions in dimensions \( d < 2 \).

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{tc\_exact} &= \frac{2}{\ln(1+\sqrt{2})} \\
\mathrm{tc\_meanfield} &= 4 \\
\mathrm{ratio\_exact\_mf} &= \frac{1}{2 \ln(1+\sqrt{2})}
\end{aligned}
\]