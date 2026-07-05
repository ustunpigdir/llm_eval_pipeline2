**1. Mean-field estimate of $k_B T_c/J$:**

The mean-field approximation for the critical temperature of the Ising model is given by $k_B T_c^{MF}/J = z$, where $z$ is the coordination number. For the 2D square lattice, $z = 4$. Thus,

\[k_B T_c^{MF}/J = z = 4\]

**2. Onsager's exact result for $k_B T_c/J$:**

Onsager's exact solution for the 2D Ising model gives the critical temperature as

\[k_B T_c/J = \frac{2}{\ln(1+\sqrt{2})}\]

Calculating this value,

\[k_B T_c/J \approx \frac{2}{\ln(1+\sqrt{2})} \approx 2.269\]

**3. Ratio $T_c^{exact}/T_c^{MF}$:**

Now, let's find the ratio of the exact critical temperature to the mean-field critical temperature:

\[\frac{T_c^{exact}}{T_c^{MF}} = \frac{\frac{2}{\ln(1+\sqrt{2})}}{4} \approx 0.562\]

Mean field overestimates $T_c$ because it neglects fluctuations, which are more important in lower dimensions. In mean-field theory, each spin interacts with a uniform field from all other spins, leading to an overestimation of the ordering temperature.

**4. One-dimensional Ising model:**

In one dimension, the exact critical temperature is $k_B T_c/J = 2/\ln(2)$. The physical reason is that in 1D, there are no closed loops that can support long-range order, so the system cannot exhibit a phase transition at any finite temperature. The mean-field theory, which assumes infinite-range interactions, fails completely in 1D.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{tc\_exact} &= \frac{2}{\ln(1+\sqrt{2})} \approx 2.269 \\
\mathrm{tc\_meanfield} &= 4 \\
\mathrm{ratio\_exact\_mf} &= \frac{2}{\ln(1+\sqrt{2}) \cdot 4} \approx 0.562
\end{aligned}
\]