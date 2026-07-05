### 1. Entanglement Threshold (PPT Criterion for Two Qubits)

The Werner state is given by:
\[
\rho = p\,|\Psi^-\rangle\langle\Psi^-| + (1-p)\,\frac{\mathbb{1}}{4}.
\]

#### Step 1: Write the density matrix explicitly
The singlet state \(|\Psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)\) has the density matrix:
\[
|\Psi^-\rangle\langle\Psi^-| = \frac{1}{2} \begin{pmatrix}
0 & 0 & 0 & -1 \\
0 & 0 & -1 & 0 \\
0 & -1 & 0 & 0 \\
-1 & 0 & 0 & 0
\end{pmatrix}.
\]
The maximally mixed state \(\frac{\mathbb{1}}{4}\) is:
\[
\frac{\mathbb{1}}{4} = \frac{1}{4} \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}.
\]
Thus, the Werner state is:
\[
\rho = p \cdot \frac{1}{2} \begin{pmatrix}
0 & 0 & 0 & -1 \\
0 & 0 & -1 & 0 \\
0 & -1 & 0 & 0 \\
-1 & 0 & 0 & 0
\end{pmatrix} + (1-p) \cdot \frac{1}{4} \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}.
\]
Simplifying:
\[
\rho = \frac{1}{4} \begin{pmatrix}
(1-p) & 0 & 0 & -2p \\
0 & (1-p) & -2p & 0 \\
0 & -2p & (1-p) & 0 \\
-2p & 0 & 0 & (1-p)
\end{pmatrix}.
\]

#### Step 2: Compute the partial transpose \(\rho^T_A\)
The partial transpose with respect to the first qubit swaps the signs of the off-diagonal elements in the first two rows/columns:
\[
\rho^T_A = \frac{1}{4} \begin{pmatrix}
(1-p) & 0 & 0 & 2p \\
0 & (1-p) & 2p & 0 \\
0 & 2p & (1-p) & 0 \\
-2p & 0 & 0 & (1-p)
\end{pmatrix}.
\]

#### Step 3: Check the PPT (Positive Partial Transpose) condition
A state is separable if and only if \(\rho^T_A\) is positive semidefinite. The PPT condition is equivalent to all eigenvalues of \(\rho^T_A\) being non-negative.

The eigenvalues of \(\rho^T_A\) can be found by solving the characteristic polynomial. The matrix \(\rho^T_A\) has the form:
\[
\rho^T_A = \frac{1}{4} \begin{pmatrix}
a & 0 & 0 & b \\
0 & a & b & 0 \\
0 & b & a & 0 \\
-b & 0 & 0 & a
\end{pmatrix}, \quad \text{where } a = 1-p, \, b = 2p.
\]

The characteristic polynomial is:
\[
\det(\rho^T_A - \lambda \mathbb{1}) = 0.
\]
This can be computed as follows:
\[
\det \begin{pmatrix}
a - \lambda & 0 & 0 & b \\
0 & a - \lambda & b & 0 \\
0 & b & a - \lambda & 0 \\
-b & 0 & 0 & a - \lambda
\end{pmatrix} = 0.
\]

This determinant can be evaluated by noting the block structure. The eigenvalues are:
1. \(\lambda_1 = a - b\) (with multiplicity 1),
2. \(\lambda_2 = a + b\) (with multiplicity 1),
3. \(\lambda_3 = a\) (with multiplicity 2).

Explicitly:
\[
\lambda_1 = \frac{1-p}{4} - \frac{2p}{4} = \frac{1 - 3p}{4},
\]
\[
\lambda_2 = \frac{1-p}{4} + \frac{2p}{4} = \frac{1 + p}{4},
\]
\[
\lambda_3 = \frac{1-p}{4} \quad \text{(double eigenvalue)}.
\]

For \(\rho^T_A\) to be positive semidefinite, all eigenvalues must be non-negative:
1. \(\lambda_1 = \frac{1 - 3p}{4} \geq 0 \implies 1 - 3p \geq 0 \implies p \leq \frac{1}{3}\),
2. \(\lambda_2 = \frac{1 + p}{4} \geq 0\) (always true for \(p \geq 0\)),
3. \(\lambda_3 = \frac{1-p}{4} \geq 0 \implies p \leq 1\).

The most restrictive condition is \(p \leq \frac{1}{3}\). Thus, the state is entangled when \(p > \frac{1}{3}\).

---

### 2. CHSH Threshold

The maximal CHSH value for the Werner state is given as \(2\sqrt{2}\,p\). The CHSH inequality is violated if \(S > 2\). Thus, we set:
\[
2\sqrt{2}\,p > 2 \implies p > \frac{2}{2\sqrt{2}} = \frac{1}{\sqrt{2}}.
\]

---

### 3. At \(p = 0.500\):

#### Concurrence
The concurrence \(C\) for the Werner state is given by:
\[
C = \max\left(0, \frac{3p - 1}{2}\right).
\]
Substituting \(p = 0.5\):
\[
C = \max\left(0, \frac{3 \cdot 0.5 - 1}{2}\right) = \max\left(0, \frac{1.5 - 1}{2}\right) = \max\left(0, \frac{0.5}{2}\right) = \max\left(0, 0.25\right) = 0.25.
\]

#### Maximal CHSH value \(S\)
The maximal CHSH value is:
\[
S = 2\sqrt{2}\,p = 2\sqrt{2} \cdot 0.5 = \sqrt{2} \approx 1.414.
\]
Since \(1.414 < 2\), the state does not violate CHSH at \(p = 0.5\).

---

### 4. Explanation of Entanglement vs. Bell Nonlocality

At \(p = 0.5\), the state is entangled (since \(p > \frac{1}{3}\)) but does not violate the CHSH inequality (since \(p < \frac{1}{\sqrt{2}}\)). This demonstrates that:
- **Entanglement** is a property of the quantum state where it cannot be written as a classical mixture of product states. It is a resource for quantum correlations.
- **Bell nonlocality** (or CHSH violation) is a stronger condition where the quantum correlations cannot be explained by any local hidden variable theory. Not all entangled states violate Bell inequalities; some entangled states are "locally hidden variable" states (e.g., bound entangled states in higher dimensions).

Werner's 1989 paper highlighted this distinction by showing that the Werner state can be entangled without violating CHSH, illustrating that entanglement and Bell nonlocality are not equivalent properties.

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{entanglement\_threshold} &= \frac{1}{3}, \\
\mathrm{chsh\_threshold} &= \frac{1}{\sqrt{2}}, \\
\mathrm{concurrence\_at\_p05} &= 0.25, \\
\mathrm{chsh\_S\_at\_p05} &= \sqrt{2}.
\end{aligned}
\]