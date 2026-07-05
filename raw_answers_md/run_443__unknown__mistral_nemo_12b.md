**1. Entanglement Threshold:**

The Werner state $\rho = p\,|\Psi^-\rangle\langle\Psi^-| + (1-p)\,\mathbb{1}/4$ is entangled if it is not separable. For two qubits, this is equivalent to the state not being positive semi-definite under partial transpose (PPT). The partial transpose of $\rho$ is:

$\rho^PT = p\,|\Psi^+\rangle\langle\Psi^+| + (1-p)\,\mathbb{1}/4$

The state is PPT if there exists a vector $v$ such that $\rho^PT v \geq 0$. However, for the Werner state, $\rho^PT$ has a negative eigenvalue $-(1-3p)/4$ when $p > 1/3$. Therefore, the state is entangled for $p > 1/3$.

**2. CHSH Threshold:**

The CHSH inequality states that $S = 2\sqrt{2} \max_{\alpha,\beta} |\langle \alpha\beta|\rho|\alpha\beta\rangle| \leq 2$. For the Werner state, the maximal value of $S$ is $2\sqrt{2}p$. Setting this greater than 2 gives $p > 1/\sqrt{2}$. Therefore, the state violates CHSH for $p > 1/\sqrt{2}$.

**3. At $p = 0.500$:**

- **Concurrence:** The concurrence of the Werner state is given by $C = \max(0, (3p-1)/2)$. At $p = 0.5$, $C = \max(0, 0) = 0$. However, the state is still entangled because entanglement is a non-local property that cannot be detected by local measurements alone.

- **Maximal CHSH value:** At $p = 0.5$, the maximal CHSH value is $S = 2\sqrt{2}p = 2\sqrt{2} \times 0.5 = \sqrt{2} < 2$. Therefore, the state does not violate CHSH.

**4. Entanglement vs. Bell Nonlocality:**

The Werner state at $p = 0.5$ is entangled but does not violate CHSH. This shows that entanglement and Bell nonlocality are not the same property. Entanglement is a necessary but not sufficient condition for Bell nonlocality. The CHSH inequality is a test for non-local correlations, not entanglement. A state can be entangled but still have local hidden variable models that satisfy the CHSH inequality.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{entanglement\_threshold} &= \frac{1}{3} \\
\mathrm{chsh\_threshold} &= \frac{1}{\sqrt{2}} \\
\mathrm{concurrence\_at\_p05} &= 0 \\
\mathrm{chsh\_S\_at\_p05} &= \sqrt{2}
\end{aligned}
\]