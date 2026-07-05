To solve this problem, we will follow the given steps and show our reasoning normally.

**Task 1: Entanglement Threshold**

The Werner state is entangled if it is non-separable. For two-qubit states, PPT (positive partial transpose) is an exact criterion for separability. We need to find the condition for which the state $\rho$ has a positive partial transpose.

The partial transpose of $\rho$ is given by:

$$\rho^{T_B} = p\,|\Psi^-\rangle\langle\Psi^-|^{T_B} + (1-p)\,\mathbb{1}/4$$

where $T_B$ denotes the partial transpose with respect to the second qubit.

Since $|\Psi^-\rangle = \frac{1}{\sqrt{2}}(|00\rangle - |11\rangle)$, we have:

$$|\Psi^-\rangle\langle\Psi^-|^{T_B} = \frac{1}{2}(|00\rangle\langle00| + |11\rangle\langle11| - |00\rangle\langle11| - |11\rangle\langle00|)$$

Now, we need to find the condition for which $\rho^{T_B}$ is positive semi-definite.

The eigenvalues of $\rho^{T_B}$ are given by:

$$\lambda_1 = p + \frac{1-p}{4} = \frac{3p+1}{4}$$

$$\lambda_2 = \lambda_3 = \frac{1-p}{4}$$

$$\lambda_4 = \frac{1-p}{4}$$

For $\rho^{T_B}$ to be positive semi-definite, we need $\lambda_1 \geq 0$ and $\lambda_2, \lambda_3, \lambda_4 \geq 0$.

This gives us the condition:

$$\frac{3p+1}{4} \geq 0 \quad \text{and} \quad \frac{1-p}{4} \geq 0$$

Simplifying, we get:

$$p \geq -\frac{1}{3} \quad \text{and} \quad p \leq 1$$

Since $p$ is a probability, we have $0 \leq p \leq 1$. Therefore, the entanglement threshold is:

$$\mathrm{entanglement\_threshold} = \boxed{\frac{1}{3}}$$

**Task 2: CHSH Threshold**

The maximal quantum CHSH value for the Werner state is given by $2\sqrt{2}\,p$. For CHSH to be violated, we need $S > 2$.

We have:

$$S = 2\sqrt{2}\,p$$

For $S > 2$, we need:

$$2\sqrt{2}\,p > 2$$

Simplifying, we get:

$$p > \frac{1}{\sqrt{2}}$$

Therefore, the CHSH threshold is:

$$\mathrm{chsh\_threshold} = \boxed{\frac{1}{\sqrt{2}}}$$

**Task 3: Concurrence and CHSH at $p = 0.5$**

At $p = 0.5$, we have:

$$\rho = \frac{1}{2}|\Psi^-\rangle\langle\Psi^-| + \frac{1}{4}\mathbb{1}$$

The concurrence is given by:

$$C = \max(0, (3p-1)/2)$$

Substituting $p = 0.5$, we get:

$$C = \max(0, (3(0.5)-1)/2) = \max(0, 0) = 0$$

The maximal CHSH value is given by:

$$S = 2\sqrt{2}\,p = 2\sqrt{2}(0.5) = \sqrt{2}$$

Therefore, at $p = 0.5$:

$$\mathrm{concurrence\_at\_p05} = \boxed{0}$$

$$\mathrm{chsh\_S\_at\_p05} = \boxed{\sqrt{2}}$$

**Task 4: Entanglement and Bell Nonlocality**

At $p = 0.5$, the state is entangled but does not violate CHSH. This shows that entanglement and Bell nonlocality are not the same property.

The Werner state is entangled for $p > 1/3$, but it does not violate CHSH for $p > 1/\sqrt{2}$. This means that entanglement is a necessary but not sufficient condition for Bell nonlocality.

Therefore, entanglement and Bell nonlocality are distinct properties of quantum states.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{entanglement\_threshold} &= \frac{1}{3} \\
\mathrm{chsh\_threshold} &= \frac{1}{\sqrt{2}} \\
\mathrm{concurrence\_at\_p05} &= 0 \\
\mathrm{chsh\_S\_at\_p05} &= \sqrt{2}
\end{aligned}
\]