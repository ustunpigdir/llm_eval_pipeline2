### 1. Mean-Field Estimate
In the mean-field approximation, we assume that each spin interacts with the average magnetization of its neighbors rather than with individual fluctuating spins. The effective field acting on a spin is $B_{eff} = z J \langle s \rangle$. The self-consistency equation for the magnetization is:
$$\langle s \rangle = \tanh\left(\frac{z J \langle s \rangle}{k_B T}\right)$$
The phase transition occurs when the slope of the right-hand side at $\langle s \rangle = 0$ equals 1:
$$\left. \frac{d}{d\langle s \rangle} \tanh\left(\frac{z J \langle s \rangle}{k_B T}\right) \right|_{\langle s \rangle = 0} = \frac{z J}{k_B T_c^{MF}} = 1$$
Solving for $k_B T_c^{MF}/J$:
$$\frac{k_B T_c^{MF}}{J} = z$$
For a square lattice, $z = 4$, so:
$$\frac{k_B T_c^{MF}}{J} = 4$$

### 2. Onsager's Exact Result
The exact solution for the 2D Ising model on a square lattice was derived by Lars Onsager. The critical temperature is given by the condition $\sinh(2J/k_B T_c) = 1$. This leads to:
$$\frac{k_B T_c}{J} = \frac{2}{\ln(1 + \sqrt{2})}$$
Evaluating the numerical value:
$\ln(1 + \sqrt{2}) \approx \ln(2.4142) \approx 0.88137$
$$\frac{k_B T_c}{J} \approx \frac{2}{0.88137} \approx 2.27126$$

### 3. Ratio and Physical Reasoning
We compute the ratio of the exact critical temperature to the mean-field estimate:
$$\text{Ratio} = \frac{T_c^{exact}}{T_c^{MF}} = \frac{2.27126}{4} \approx 0.5678$$
**Why Mean Field Overestimates $T_c$:**
Mean-field theory ignores local fluctuations and correlations. It assumes that every spin "feels" the average magnetization of the entire system. In reality, fluctuations (clusters of spins flipping) act to destabilize the ordered phase. Because mean-field theory neglects these destabilizing fluctuations, it predicts that the ordered state is more robust than it actually is, thereby overestimating the temperature at which the transition to the disordered state occurs.

### 4. The One-Dimensional Case
In one dimension ($z=2$), the exact result is:
$$T_c = 0$$
**Physical Reason:**
In 1D, the energy cost to create a "domain wall" (flipping all spins to the right of a certain point) is constant ($2J$), regardless of the size of the system. However, the entropy gained by placing this domain wall anywhere in the chain of $N$ sites grows as $\ln(N)$. For any $T > 0$, the free energy $F = E - TS$ is minimized by the creation of domain walls, which destroys long-range order. Thus, no phase transition occurs at any finite temperature.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{tc\_exact} &= 2.27126 \\
\mathrm{tc\_meanfield} &= 4 \\
\mathrm{ratio\_exact\_mf} &= 0.5678
\end{aligned}
\]