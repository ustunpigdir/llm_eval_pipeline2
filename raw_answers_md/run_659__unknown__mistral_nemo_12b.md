**1. Mean-field estimate of $T_c$:**

The mean-field approximation for the Ising model in an infinite system is given by the self-consistency equation:

\[m = \tanh\left(\frac{zJm}{k_BT}\right)\]

where $m$ is the magnetization per spin, $z$ is the coordination number, $J$ is the coupling constant, $k_B$ is the Boltzmann constant, and $T$ is the temperature. At the critical temperature, $m=0$, so we have:

\[\tanh\left(\frac{zJ}{k_BT_c^{MF}}\right) = 0\]

which implies:

\[\frac{zJ}{k_BT_c^{MF}} = 0\]

Thus, the mean-field estimate of the critical temperature is:

\[k_B T_c^{MF}/J = z = 4\]

**2. Onsager's exact result for $T_c$:**

Onsager solved the 2D Ising model exactly using transfer matrix methods and found the critical temperature to be:

\[k_B T_c/J = 2/\ln(1+\sqrt{2})\]

**3. Ratio of exact to mean-field $T_c$:**

Now, let's compute the ratio of the exact critical temperature to the mean-field estimate:

\[\frac{T_c^{exact}}{T_c^{MF}} = \frac{2/\ln(1+\sqrt{2})}{4} = \frac{1}{2\ln(1+\sqrt{2})}\]

**4. One-dimensional Ising model:**

In one dimension, the exact solution can be found using the transfer matrix method or by mapping the problem to a free fermion model. The critical temperature is:

\[k_B T_c/J = 2/\ln(2)\]

The mean-field estimate in one dimension is $z=2$, so:

\[k_B T_c^{MF}/J = 2\]

The ratio of exact to mean-field $T_c$ in one dimension is:

\[\frac{T_c^{exact}}{T_c^{MF}} = \frac{1}{\ln(2)}\]

**Why does mean field overestimate $T_c$?**

Mean-field theory neglects fluctuations, which become more important in lower dimensions. In two dimensions, fluctuations are strong enough to lower the critical temperature compared to the mean-field estimate. In one dimension, fluctuations are even stronger, leading to an even lower critical temperature.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{tc\_exact} &= \frac{2}{\ln(1+\sqrt{2})} \approx 2.269 \\
\mathrm{tc\_meanfield} &= 4 \\
\mathrm{ratio\_exact\_mf} &= \frac{1}{2\ln(1+\sqrt{2})} \approx 0.447
\end{aligned}
\]