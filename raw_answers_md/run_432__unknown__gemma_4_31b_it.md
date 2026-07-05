To analyze the Werner state $\rho = p|\Psi^-\rangle\langle\Psi^-| + (1-p)\frac{\mathbb{1}}{4}$, we proceed step-by-step.

### 1. Entanglement Threshold
For two-qubit states, the Peres-Horodecki criterion (PPT) is necessary and sufficient for separability. The state is entangled if and only if the partial transpose $\rho^{T_B}$ has at least one negative eigenvalue.
The singlet state $|\Psi^-\rangle\langle\Psi^-|$ has eigenvalues $(1, 0, 0, 0)$ and its partial transpose has eigenvalues $(1/2, 1/2, 1/2, -1/2)$.
The identity part $\mathbb{1}/4$ is invariant under partial transposition.
The eigenvalues of $\rho^{T_B}$ are:
$\lambda_1 = \lambda_2 = \lambda_3 = \frac{p}{2} + \frac{1-p}{4} = \frac{p+1}{4}$
$\lambda_4 = -\frac{p}{2} + \frac{1-p}{4} = \frac{1-3p}{4}$
The state is entangled if $\lambda_4 < 0 \implies 1-3p < 0 \implies p > 1/3$.
**Entanglement threshold: $p > 1/3$.**

### 2. CHSH Violation Threshold
The maximal CHSH value for a Werner state is given as $S = 2\sqrt{2}p$.
A state violates the CHSH inequality if $S > 2$.
$2\sqrt{2}p > 2 \implies \sqrt{2}p > 1 \implies p > \frac{1}{\sqrt{2}}$.
**CHSH threshold: $p > 1/\sqrt{2} \approx 0.707$.**

### 3. Calculations at $p = 0.500$
**Concurrence:**
Using the provided formula $C = \max(0, \frac{3p-1}{2})$:
$C = \max(0, \frac{3(0.5) - 1}{2}) = \max(0, \frac{1.5 - 1}{2}) = \frac{0.5}{2} = 0.25$.

**Maximal CHSH value $S$:**
Using $S = 2\sqrt{2}p$:
$S = 2\sqrt{2}(0.5) = \sqrt{2} \approx 1.414$.

### 4. Entanglement vs. Bell Nonlocality
At $p = 0.5$, we have $1/3 < 0.5 < 1/\sqrt{2}$.
The state is entangled ($C = 0.25 > 0$), but it does not violate the CHSH inequality ($S = \sqrt{2} < 2$).
This demonstrates that entanglement is a necessary but not sufficient condition for Bell nonlocality. Werner (1989) showed that there exist entangled states that admit a Local Hidden Variable (LHV) model for all possible projective measurements, meaning they cannot violate any Bell inequality despite being non-separable.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{entanglement\_threshold} &= 1/3 \\
\mathrm{chsh\_threshold} &= 1/\sqrt{2} \\
\mathrm{concurrence\_at\_p05} &= 0.25 \\
\mathrm{chsh\_S\_at\_p05} &= \sqrt{2}
\end{aligned}
\]