Let's analyze the Werner state and address the given tasks.

**1. Entanglement Threshold**

The Werner state $\rho = p\,|\Psi^-\rangle\langle\Psi^-| + (1-p)\,\mathbb{1}/4$ is entangled if and only if its partial transpose is not positive semi-definite. The partial transpose with respect to the second qubit is:

$\rho_2 \rightarrow = p\,|\Psi^-\rangle\langle\Psi^-| + (1-p)\,\mathbb{1}/4$

The eigenvalues of $\rho_2 \rightarrow$ are $p + (1-p)/4$, $p + (1-p)/4$, $(1-p)/4 - p$, $(1-p)/4 - p$.
For $\rho_2 \rightarrow$ to be positive semi-definite, all eigenvalues must be non-negative.
$p + (1-p)/4 \ge 0 \implies 4p + 1 - p \ge 0 \implies 3p + 1 \ge 0 \implies p \ge -1/3$
$(1-p)/4 - p \ge 0 \implies 1 - p - 4p \ge 0 \implies 1 - 5p \ge 0 \implies p \le 1/5$

However, the PPT criterion is exact for two qubits.  The state is entangled if and only if it is not separable.  The separability condition is that the state can be written as a convex combination of product states.  The Werner state is entangled if $p > 1/3$.  This is because if $p < 1/3$, the white noise term dominates, and the state can be written as a convex combination of product states. If $p = 1/3$, the state is PPT but not entangled. If $p > 1/3$, the state is entangled.

Therefore, the entanglement threshold is $p = 1/3$.

**2. CHSH Threshold**

The CHSH inequality states that for any local hidden variable theory, $|S| \le 2$, where $S = E(A \cdot B) + E(A \cdot B') + E(A' \cdot B) - E(A' \cdot B')$.  For the Werner state, the maximal CHSH value is $S = 2\sqrt{2}\,p$.  CHSH violation occurs when $S > 2$.

$2\sqrt{2}\,p > 2 \implies \sqrt{2}\,p > 1 \implies p > \frac{1}{\sqrt{2}}$

Therefore, the CHSH threshold is $p = 1/\sqrt{2}$.

**3. Computation at p = 0.5**

At $p = 0.5$, we compute the concurrence and the maximal CHSH value.

Concurrence: $C = \max(0, (3p-1)/2) = \max(0, (3(0.5)-1)/2) = \max(0, (1.5-1)/2) = \max(0, 0.5/2) = \max(0, 0.25) = 0.25$.

Maximal CHSH value: $S = 2\sqrt{2}\,p = 2\sqrt{2}(0.5) = \sqrt{2} \approx 1.414$.

**4. Entanglement vs. Bell Nonlocality**

At $p = 0.5$, the state is entangled (since $0.5 > 1/3$), but it does not violate CHSH (since $\sqrt{2} < 2$). This demonstrates that entanglement and Bell nonlocality are not the same.

Entanglement is a property of the quantum state itself, indicating correlations that cannot be explained by classical means. It is a necessary condition for Bell nonlocality, but not a sufficient one. A state can be entangled without exhibiting Bell nonlocality (i.e., without violating the CHSH inequality).

Werner's 1989 paper showed that a mixed state can be entangled but still satisfy the CHSH inequality. The degree of entanglement is not directly related to the degree of Bell nonlocality.  The CHSH inequality is violated when the correlations are *stronger* than what is allowed by local realism, and this requires a certain level of "purity" of the state (i.e., a sufficiently large $p$).  A state with a small $p$ can be entangled but still have correlations that are consistent with local realism.

\[
\begin{aligned}
\mathrm{entanglement\_threshold} &= 1/3 \\
\mathrm{chsh\_threshold} &= 1/\sqrt{2} \\
\mathrm{concurrence\_at\_p05} &= 0.25 \\
\mathrm{chsh\_S\_at\_p05} &= \sqrt{2}
\end{aligned}
\]