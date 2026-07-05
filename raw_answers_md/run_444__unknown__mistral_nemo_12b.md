**Solution:**

1. **Entanglement Threshold:**
   The Werner state $\rho$ is entangled if it is not separable. For two qubits, this is equivalent to the state not being positive under partial transpose (PPT). The partial transpose of $\rho$ is:
   \[
   \rho^PT = p\,|\Psi^+\rangle\langle\Psi^+| + (1-p)\,\mathbb{1}/4
   \]
   where $|\Psi^+\rangle = (|01\rangle + |10\rangle)/\sqrt{2}$. The state is PPT if and only if the eigenvalues of $\rho^PT$ are non-negative. The largest eigenvalue of $\rho^PT$ is $p + (1-p)/4 = (5p + 1)/4$. This is non-negative for all $p$, so $\rho$ is PPT for all $p$. Therefore, the state is entangled if and only if $p > 0$. Thus, the entanglement threshold is $p = 0$.

   \[
   \mathrm{entanglement\_threshold} = 0
   \]

2. **CHSH Threshold:**
   The CHSH inequality states that $S = |\langle A_1B_1\rangle + \langle A_1B_2\rangle + \langle A_2B_1\rangle - \langle A_2B_2\rangle| \leq 2$ for all measurements $A_1, A_2, B_1, B_2$. The maximal quantum CHSH value for the Werner state is $2\sqrt{2}p$. Setting this greater than 2 gives $p > 1/\sqrt{2}$. Thus, the CHSH threshold is $p = 1/\sqrt{2}$.

   \[
   \mathrm{chsh\_threshold} = \frac{1}{\sqrt{2}}
   \]

3. **Concurrence and CHSH at $p = 0.500$:**
   The concurrence of a state $\rho$ is given by $C = \max(0, \lambda_1 - \lambda_2 - \lambda_3 - \lambda_4)$, where $\lambda_i$ are the square roots of the eigenvalues of $\rho\sigma_y\otimes\sigma_y\rho^*$ in descending order. For the Werner state at $p = 0.5$, this gives $C = \max(0, (3p-1)/2) = 0$. The maximal CHSH value at $p = 0.5$ is $2\sqrt{2}p = \sqrt{2}$.

   \[
   \mathrm{concurrence\_at\_p05} = 0
   \]
   \[
   \mathrm{chsh\_S\_at\_p05} = \sqrt{2}
   \]

4. **Entanglement vs. Bell Nonlocality:**
   The Werner state at $p = 0.5$ is entangled (as shown above) but does not violate CHSH. This shows that entanglement and Bell nonlocality are not the same property. Entanglement is a necessary but not sufficient condition for Bell nonlocality. The Werner state at $p = 0.5$ is entangled but not sufficiently so to violate CHSH.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{entanglement\_threshold} &= 0 \\
\mathrm{chsh\_threshold} &= \frac{1}{\sqrt{2}} \\
\mathrm{concurrence\_at\_p05} &= 0 \\
\mathrm{chsh\_S\_at\_p05} &= \sqrt{2}
\end{aligned}
\]