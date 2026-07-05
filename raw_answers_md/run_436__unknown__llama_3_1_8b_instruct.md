To solve this problem, we will follow the given steps and show our reasoning normally.

**Task 1: Entanglement Threshold**

The Werner state is entangled if and only if it is non-separable. For two-qubit states, this is equivalent to the partial transpose (PPT) being exact. We can check this by computing the PPT of the state.

The PPT of the Werner state is given by:

$$\rho^{T_B} = p\,|\Psi^-\rangle\langle\Psi^-|^{T_B} + (1-p)\,\mathbb{1}/4$$

Since $|\Psi^-\rangle = \frac{1}{\sqrt{2}}(|00\rangle - |11\rangle)$, we have:

$$|\Psi^-\rangle\langle\Psi^-|^{T_B} = \frac{1}{2}(|00\rangle\langle 00| + |11\rangle\langle 11|)$$

Therefore, the PPT of the Werner state is:

$$\rho^{T_B} = \frac{p}{2}(|00\rangle\langle 00| + |11\rangle\langle 11|) + \frac{1-p}{4}\mathbb{1}$$

For the state to be entangled, the PPT must be non-identical to the original state. This means that the two terms in the PPT must be different. Since the first term is proportional to $|00\rangle\langle 00|$ and the second term is proportional to $\mathbb{1}$, we can see that the two terms are different if and only if $p > 1/3$.

Therefore, the entanglement threshold is:

$$\mathrm{entanglement\_threshold} = \boxed{\frac{1}{3}}$$

**Task 2: CHSH Threshold**

The maximal quantum CHSH value for the Werner state is given by $2\sqrt{2}\,p$. For the state to violate CHSH, we need $S > 2$. Since $S = 2\sqrt{2}\,p$, we have:

$$2\sqrt{2}\,p > 2$$

Solving for $p$, we get:

$$p > \frac{1}{\sqrt{2}}$$

Therefore, the CHSH threshold is:

$$\mathrm{chsh\_threshold} = \boxed{\frac{1}{\sqrt{2}}}$$

**Task 3: Concurrence and Maximal CHSH Value at $p = 0.5$**

At $p = 0.5$, the state is:

$$\rho = \frac{1}{2}|\Psi^-\rangle\langle\Psi^-| + \frac{1}{4}\mathbb{1}$$

The concurrence is given by:

$$C = \max(0, (3p-1)/2)$$

Substituting $p = 0.5$, we get:

$$C = \max(0, (3(0.5)-1)/2) = \max(0, 0) = 0$$

The maximal CHSH value is given by:

$$S = 2\sqrt{2}\,p$$

Substituting $p = 0.5$, we get:

$$S = 2\sqrt{2}\,(0.5) = \sqrt{2}$$

Therefore, at $p = 0.5$:

$$\mathrm{concurrence\_at\_p05} = \boxed{0}$$

$$\mathrm{chsh\_S\_at\_p05} = \boxed{\sqrt{2}}$$

**Task 4: Entanglement and Bell Nonlocality**

At $p = 0.5$, the state is entangled but does not violate CHSH. This means that entanglement and Bell nonlocality are not the same property. In fact, the Werner state at $p = 0.5$ is a counterexample to the idea that entanglement implies Bell nonlocality.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{entanglement\_threshold} &= \frac{1}{3} \\
\mathrm{chsh\_threshold} &= \frac{1}{\sqrt{2}} \\
\mathrm{concurrence\_at\_p05} &= 0 \\
\mathrm{chsh\_S\_at\_p05} &= \sqrt{2}
\end{aligned}
\]