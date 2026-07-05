### Task 1: Entanglement Threshold

The Werner state is given by:
\[
\rho = p\,|\Psi^-\rangle\langle\Psi^-| + (1-p)\,\frac{\mathbb{1}}{4}
\]
where \(|\Psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)\).

#### Step 1: Partial Transpose Criterion for Entanglement
For two-qubit states, entanglement is equivalent to the state being **not** positive semidefinite under partial transpose (PPT). The PPT criterion is exact for two qubits.

The partial transpose of \(\rho\) is:
\[
\rho^T_A = p\,|\Psi^-\rangle\langle\Psi^-|^T_A + (1-p)\,\frac{\mathbb{1}}{4}^T_A
\]
The term \(|\Psi^-\rangle\langle\Psi^-|^T_A\) is:
\[
|\Psi^-\rangle\langle\Psi^-|^T_A = \frac{1}{2} \begin{pmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & -1 \\
0 & 0 & 0 & 0 \\
0 & -1 & 0 & 0
\end{pmatrix}
\]
The identity matrix \(\frac{\mathbb{1}}{4}\) is unchanged under partial transpose.

Thus:
\[
\rho^T_A = p \begin{pmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & -1 \\
0 & 0 & 0 & 0 \\
0 & -1 & 0 & 0
\end{pmatrix} + \frac{1-p}{4} \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
\]

#### Step 2: Eigenvalues of \(\rho^T_A\)
The matrix \(\rho^T_A\) is:
\[
\rho^T_A = \begin{pmatrix}
\frac{1-p}{4} & 0 & 0 & 0 \\
0 & \frac{1-p}{4} & 0 & -\frac{p}{2} \\
0 & 0 & \frac{1-p}{4} & 0 \\
0 & -\frac{p}{2} & 0 & \frac{1-p}{4}
\end{pmatrix}
\]

The eigenvalues of \(\rho^T_A\) can be found by solving the characteristic equation. The matrix has the following structure:
- Two eigenvalues are \(\frac{1-p}{4}\) (from the diagonal elements corresponding to \(|00\rangle\) and \(|11\rangle\)).
- The remaining two eigenvalues come from the \(2 \times 2\) block:
\[
\begin{pmatrix}
\frac{1-p}{4} & -\frac{p}{2} \\
-\frac{p}{2} & \frac{1-p}{4}
\end{pmatrix}
\]
The eigenvalues of this block are:
\[
\lambda = \frac{1-p}{4} \pm \frac{p}{2}
\]
Thus:
\[
\lambda_1 = \frac{1-p}{4} + \frac{p}{2} = \frac{1-p + 2p}{4} = \frac{1 + p}{4}
\]
\[
\lambda_2 = \frac{1-p}{4} - \frac{p}{2} = \frac{1-p - 2p}{4} = \frac{1 - 3p}{4}
\]

#### Step 3: PPT Condition
For \(\rho^T_A\) to be positive semidefinite, all eigenvalues must be non-negative:
1. \(\frac{1-p}{4} \geq 0\) (always true for \(p \geq 0\)),
2. \(\frac{1 + p}{4} \geq 0\) (always true for \(p \geq 0\)),
3. \(\frac{1 - 3p}{4} \geq 0\).

The third condition gives:
\[
1 - 3p \geq 0 \implies p \leq \frac{1}{3}
\]

Thus, \(\rho^T_A\) is **not** positive semidefinite when \(p > \frac{1}{3}\), meaning the state is entangled for \(p > \frac{1}{3}\).

### Task 2: CHSH Threshold

The maximal CHSH value for the Werner state is given as \(2\sqrt{2}\,p\). The CHSH inequality is violated if \(S > 2\).

Thus, we set:
\[
2\sqrt{2}\,p > 2 \implies \sqrt{2}\,p > 1 \implies p > \frac{1}{\sqrt{2}} \approx 0.707
\]

### Task 3: At \(p = 0.500\)

#### Concurrence
The concurrence \(C\) for the Werner state is given by:
\[
C = \max\left(0, \frac{3p - 1}{2}\right)
\]
For \(p = 0.5\):
\[
C = \max\left(0, \frac{3(0.5) - 1}{2}\right) = \max\left(0, \frac{1.5 - 1}{2}\right) = \max\left(0, \frac{0.5}{2}\right) = \max\left(0, 0.25\right) = 0.25
\]

#### Maximal CHSH Value
The maximal CHSH value is:
\[
S = 2\sqrt{2}\,p = 2\sqrt{2} \times 0.5 = \sqrt{2} \approx 1.414
\]
Since \(1.414 < 2\), the state does not violate CHSH at \(p = 0.5\).

### Task 4: Explanation of Entanglement vs. Bell Nonlocality

At \(p = 0.5\), the state is entangled (since \(p > \frac{1}{3}\)) but does not violate the CHSH inequality (since \(p < \frac{1}{\sqrt{2}}\)). This demonstrates that:
- **Entanglement** refers to the non-separability of the state (i.e., it cannot be written as a convex combination of product states).
- **Bell nonlocality** (or CHSH violation) is a stronger condition that requires the state to produce correlations that cannot be explained by any local hidden variable theory.

Not all entangled states violate Bell inequalities. Some entangled states (called "bound entangled" states) do not exhibit Bell nonlocality but are still entangled. The Werner state at \(p = 0.5\) is an example of such a state.

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{entanglement\_threshold} &= \frac{1}{3} \\
\mathrm{chsh\_threshold} &= \frac{1}{\sqrt{2}} \\
\mathrm{concurrence\_at\_p05} &= 0.25 \\
\mathrm{chsh\_S\_at\_p05} &= \sqrt{2}
\end{aligned}
\]