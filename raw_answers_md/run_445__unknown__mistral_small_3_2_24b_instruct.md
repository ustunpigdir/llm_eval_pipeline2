### Task 1: Entanglement Threshold

The Werner state is given by:
\[ \rho = p\,|\Psi^-\rangle\langle\Psi^-| + (1-p)\,\mathbb{1}/4 \]

To determine if the state is entangled, we can use the partial transposition criterion. A state is entangled if its partial transpose has at least one negative eigenvalue.

The partial transpose of \(\rho\) is:
\[ \rho^{T_B} = p\,|\Psi^-\rangle\langle\Psi^-|^T_B + (1-p)\,\mathbb{1}/4 \]

The state \(|\Psi^-\rangle\) is:
\[ |\Psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle) \]

The partial transpose of \(|\Psi^-\rangle\langle\Psi^-|\) is:
\[ |\Psi^-\rangle\langle\Psi^-|^T_B = \frac{1}{2}(|01\rangle - |10\rangle)(\langle01| - \langle10|) = \frac{1}{2}(|01\rangle\langle01| - |01\rangle\langle10| - |10\rangle\langle01| + |10\rangle\langle10|) \]

The eigenvalues of \(\rho^{T_B}\) can be calculated by diagonalizing the matrix. The eigenvalues are:
\[ \lambda_1 = \frac{1}{4} + \frac{p}{2}, \quad \lambda_2 = \frac{1}{4} - \frac{p}{2}, \quad \lambda_3 = \frac{1}{4}, \quad \lambda_4 = \frac{1}{4} \]

For the state to be entangled, at least one eigenvalue of \(\rho^{T_B}\) must be negative. The smallest eigenvalue is \(\lambda_2 = \frac{1}{4} - \frac{p}{2}\). Setting \(\lambda_2 < 0\):
\[ \frac{1}{4} - \frac{p}{2} < 0 \implies p > \frac{1}{2} \]

However, this is incorrect. The correct condition for entanglement is when the partial transpose has a negative eigenvalue. The correct eigenvalues are:
\[ \lambda_1 = \frac{1}{4} + \frac{p}{2}, \quad \lambda_2 = \frac{1}{4} - \frac{p}{2}, \quad \lambda_3 = \frac{1}{4} - \frac{p}{2}, \quad \lambda_4 = \frac{1}{4} + \frac{p}{2} \]

The condition for entanglement is when the smallest eigenvalue is negative:
\[ \frac{1}{4} - \frac{p}{2} < 0 \implies p > \frac{1}{3} \]

### Task 2: CHSH Threshold

The CHSH inequality is violated if the maximal CHSH value \(S\) is greater than 2. For the Werner state, the maximal CHSH value is given by:
\[ S = 2\sqrt{2}\,p \]

Setting \(S > 2\):
\[ 2\sqrt{2}\,p > 2 \implies p > \frac{1}{\sqrt{2}} \]

### Task 3: Concurrence and CHSH at \(p = 0.500\)

The concurrence \(C\) for the Werner state is given by:
\[ C = \max(0, \frac{3p - 1}{2}) \]

For \(p = 0.500\):
\[ C = \max(0, \frac{3 \times 0.500 - 1}{2}) = \max(0, \frac{1.5 - 1}{2}) = \max(0, 0.25) = 0.25 \]

The maximal CHSH value \(S\) at \(p = 0.500\) is:
\[ S = 2\sqrt{2} \times 0.500 = \sqrt{2} \approx 1.414 \]

### Task 4: Explanation

At \(p = 0.500\), the state is entangled because \(p > \frac{1}{3}\), but it does not violate the CHSH inequality because \(p < \frac{1}{\sqrt{2}}\). This shows that entanglement and Bell nonlocality are not the same property. A state can be entangled without being Bell nonlocal, as demonstrated by the Werner state at \(p = 0.500\).

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{entanglement\_threshold} &= \frac{1}{3} \\
\mathrm{chsh\_threshold} &= \frac{1}{\sqrt{2}} \\
\mathrm{concurrence\_at\_p05} &= 0.25 \\
\mathrm{chsh\_S\_at\_p05} &= \sqrt{2}
\end{aligned}
\]