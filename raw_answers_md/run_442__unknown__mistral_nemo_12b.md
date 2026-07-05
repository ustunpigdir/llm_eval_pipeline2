**Solution:**

1. **Entanglement Threshold:**
   The Werner state $\rho$ is entangled if it is not separable. For two qubits, this is equivalent to the state not being positive partial transpose (PPT). The partial transpose of $\rho$ is:
   \[
   \rho^PT = p\,|\Psi^+\rangle\langle\Psi^+| + (1-p)\,\mathbb{1}/4
   \]
   where $|\Psi^+\rangle = (|01\rangle + |10\rangle)/\sqrt{2}$. The state is PPT if and only if $p \leq 1/3$. Therefore, the state is entangled if $p > 1/3$.

2. **CHSH Violation Threshold:**
   The CHSH inequality states that $S \leq 2$ for any local realistic theory. The maximal quantum CHSH value for the Werner state is $2\sqrt{2}p$. Setting this greater than 2 gives $p > 1/\sqrt{2}$. Thus, the state violates CHSH if $p > 1/\sqrt{2}$.

3. **At $p = 0.500$:**
   - **Concurrence:** The concurrence of a state $\rho$ is given by $C = \max(0, \sqrt{2\lambda_1} - \sqrt{2\lambda_2})$, where $\lambda_1$ and $\lambda_2$ are the two largest eigenvalues of $\rho\tilde{\rho}$, with $\tilde{\rho} = \rho^PT$. For the Werner state at $p = 0.5$, $\lambda_1 = 0.5$ and $\lambda_2 = 0.25$, so $C = \max(0, \sqrt{2(0.5)} - \sqrt{2(0.25)}) = \max(0, 1 - 1) = 0$. However, the given formula for concurrence is $C = \max(0, (3p-1)/2)$. Substituting $p = 0.5$ gives $C = \max(0, (3(0.5)-1)/2) = 0.5$.
   - **Maximal CHSH value $S$:** At $p = 0.5$, the maximal CHSH value is $2\sqrt{2}p = 2\sqrt{2}(0.5) = \sqrt{4} = 2$.

4. **Entanglement vs Bell Nonlocality:**
   Entanglement and Bell nonlocality are not the same property. A state can be entangled but not violate CHSH (as shown above), and vice versa. Entanglement is a necessary but not sufficient condition for Bell nonlocality. The Werner state at $p = 0.5$ is entangled but does not violate CHSH because the maximal CHSH value is exactly 2, which is the classical limit.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{entanglement\_threshold} &= \frac{1}{3} \\
\mathrm{chsh\_threshold} &= \frac{1}{\sqrt{2}} \\
\mathrm{concurrence\_at\_p05} &= 0.5 \\
\mathrm{chsh\_S\_at\_p05} &= 2
\end{aligned}
\]