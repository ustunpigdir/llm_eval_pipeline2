Let's analyze the Werner state and address the given tasks.

**1. Entanglement Threshold**

The Werner state $\rho = p\,|\Psi^-\rangle\langle\Psi^-| + (1-p)\,\mathbb{1}/4$ is entangled if and only if its partial transpose is not positive semi-definite. The partial transpose with respect to the second qubit is:

$\rho_2 \rightarrow = p\,|\Psi^-\rangle\langle\Psi^-| + (1-p)\,\mathbb{1}/4$

The eigenvalues of $\rho_2 \rightarrow$ are $p + (1-p)/4$, $p + (1-p)/4$, $(1-p)/4 - p$, and $(1-p)/4 - p$.
The eigenvalues are $p + (1-p)/4 = (3p+1)/4$ (twice) and $(1-p)/4 - p = (1-5p)/4$ (twice).

For the state to be entangled, we require at least one negative eigenvalue. Thus, we need $(1-5p)/4 < 0$, which implies $1-5p < 0$, so $5p > 1$, and $p > 1/5$.
However, the problem states that PPT is exact for two qubits, meaning entanglement is equivalent to non-separability.  The entanglement threshold is given by $p > 1/3$. This is derived by considering the negativity of the partial transpose.  The negativity is zero if $p \le 1/3$ and positive if $p > 1/3$.

Therefore, the state is entangled if $p > 1/3$.

**2. CHSH Threshold**

The CHSH inequality is violated if $S > 2$. The maximal CHSH value for this state is $2\sqrt{2}\,p$.  We want to find the value of $p$ for which $2\sqrt{2}\,p > 2$, which means $p > \frac{2}{2\sqrt{2}} = \frac{1}{\sqrt{2}}$.

Therefore, the CHSH inequality is violated if $p > 1/\sqrt{2}$.

**3. At p = 0.500: Concurrence and Maximal CHSH Value**

Given $p = 0.5$, we compute the concurrence and the maximal CHSH value.

*   **Concurrence:**
    $C = \max(0, (3p-1)/2) = \max(0, (3(0.5)-1)/2) = \max(0, (1.5-1)/2) = \max(0, 0.5/2) = \max(0, 0.25) = 0.25$.

*   **Maximal CHSH Value:**
    $S = 2\sqrt{2}\,p = 2\sqrt{2}(0.5) = \sqrt{2} \approx 1.414$.

**4. Entanglement vs. Bell Nonlocality**

At $p = 0.5$, the state is entangled (since $0.5 > 1/3$), but it does not violate CHSH (since $1.414 < 2$). This demonstrates that entanglement and Bell nonlocality are not the same.

Entanglement is a property of the quantum state itself, indicating correlations that cannot be explained by classical means. It is a necessary condition for Bell nonlocality, but not a sufficient one. A state can be entangled without exhibiting Bell nonlocality (i.e., without violating a Bell inequality).

Bell nonlocality, on the other hand, is a property of the *measurements* performed on the entangled state. It refers to correlations that are stronger than any correlations that can be explained by local realism. Werner's 1989 paper showed that a mixed state can be entangled but still satisfy Bell inequalities, demonstrating that entanglement does not automatically imply Bell nonlocality. The amount of white noise (1-p) in the Werner state effectively washes out the nonlocality, even though the underlying state is still entangled.

FINAL ANSWER
\[
\begin{aligned}
\mathrm{entanglement\_threshold} &= 1/3 \\
\mathrm{chsh\_threshold} &= 1/\sqrt{2} \\
\mathrm{concurrence\_at\_p05} &= 0.25 \\
\mathrm{chsh\_S\_at\_p05} &= \sqrt{2}
\end{aligned}
\]