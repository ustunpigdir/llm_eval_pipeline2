### 1. Entanglement Threshold

For a two-qubit state, the Peres-Horodecki criterion (PPT criterion) is necessary and sufficient for separability. The Werner state is given by:
$$ \rho = p\,|\Psi^-\rangle\langle\Psi^-| + (1-p)\,\frac{\mathbb{1}}{4} $$
where $|\Psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$ is the singlet state.
The partial transpose of $\rho$ has eigenvalues that determine separability. For the Werner state, the state is separable if and only if $p \le 1/3$.
Therefore, the state is entangled (non-separable) if and only if:
$$ p > \frac{1}{3} $$
The exact entanglement threshold is $p_{\text{ent}} = 1/3$.

### 2. CHSH Violation Threshold

The problem statement specifies that the maximal quantum CHSH value for this state is $S_{\max} = 2\sqrt{2}\,p$.
The CHSH inequality states that for any local hidden variable theory, the correlation value $S$ must satisfy $S \le 2$.
To violate the CHSH inequality (demonstrate Bell nonlocality), we require:
$$ S_{\max} > 2 $$
Substituting the expression for $S_{\max}$:
$$ 2\sqrt{2}\,p > 2 $$
Dividing by $2\sqrt{2}$:
$$ p > \frac{1}{\sqrt{2}} $$
The exact CHSH threshold is $p_{\text{chsh}} = 1/\sqrt{2}$.

### 3. Calculations at $p = 0.500$

**Concurrence ($C$):**
The problem provides the formula for concurrence: $C = \max(0, (3p-1)/2)$.
Substituting $p = 0.5$:
$$ C = \frac{3(0.5) - 1}{2} = \frac{1.5 - 1}{2} = \frac{0.5}{2} = 0.25 $$
Since $0.25 > 0$, the concurrence is $0.25$.

**Maximal CHSH Value ($S$):**
Using the given formula $S = 2\sqrt{2}\,p$:
$$ S = 2\sqrt{2}(0.5) = \sqrt{2} \approx 1.414 $$
Since $\sqrt{2} < 2$, the state does not violate the CHSH inequality at this $p$.

### 4. Entanglement vs. Bell Nonlocality

At $p = 0.500$:
- The state is entangled because $0.500 > 1/3 \approx 0.333$.
- The state does not violate CHSH because $0.500 < 1/\sqrt{2} \approx 0.707$.

This demonstrates that entanglement and Bell nonlocality are distinct properties. Entanglement is a property of the quantum state's structure (non-separability), whereas Bell nonlocality is a property of the correlations observed in measurements that cannot be explained by local hidden variables. Werner's 1989 paper showed that there exists a range of entangled states (specifically $1/3 < p \le 1/\sqrt{2}$) that admit a local hidden variable model and thus do not violate Bell inequalities. This proves that entanglement is a necessary but not sufficient condition for Bell nonlocality.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{entanglement\_threshold} &= \frac{1}{3} \\
\mathrm{chsh\_threshold} &= \frac{1}{\sqrt{2}} \\
\mathrm{concurrence\_at\_p05} &= 0.25 \\
\mathrm{chsh\_S\_at\_p05} &= \sqrt{2}
\end{aligned}
\]