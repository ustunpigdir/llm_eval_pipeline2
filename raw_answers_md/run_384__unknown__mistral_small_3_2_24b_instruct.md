1. **Why perfect cloning is impossible and the role of linearity:**

   The no-cloning theorem states that it is impossible to create an identical copy of an arbitrary unknown quantum state. This is a direct consequence of the linearity of quantum mechanics. If we could clone an arbitrary state, we could also clone states that are in a superposition, leading to a violation of the linearity of quantum mechanics. Specifically, if we could clone a state \(|\psi\rangle\) to produce two identical copies, we could also clone a superposition \(|\psi_1\rangle + |\psi_2\rangle\) to produce \(|\psi_1\rangle + |\psi_2\rangle\) and \(|\psi_1\rangle + |\psi_2\rangle\). However, this would imply that we could distinguish between non-orthogonal states, which is not possible due to the linearity of quantum mechanics.

2. **Optimal universal cloning fidelity per copy:**

   The optimal universal cloning fidelity for a 1-to-2 cloning machine can be derived using the Buzek-Hillery symmetric universal quantum cloning machine (UQCM). The fidelity \(F\) for each copy is given by:

   \[
   F = \frac{2I + 3d}{5d}
   \]

   where \(I\) is the identity operator and \(d\) is the dimension of the Hilbert space. For a qubit, \(d = 2\). Thus,

   \[
   F = \frac{2 \times 1 + 3 \times 2}{5 \times 2} = \frac{2 + 6}{10} = \frac{8}{10} = 0.8
   \]

3. **Best classical measure-and-prepare fidelity:**

   In the classical strategy, we measure the qubit and prepare copies of the outcome. The fidelity in this case is given by the average fidelity of the measurement outcomes. For a uniformly random input, the optimal measure-and-prepare fidelity is:

   \[
   F_{\text{classical}} = \frac{1 + \frac{1}{d}}{2} = \frac{1 + \frac{1}{2}}{2} = \frac{3}{4} = 0.75
   \]

4. **Quantum advantage:**

   The quantum advantage is the difference between the optimal universal cloning fidelity and the classical measure-and-prepare fidelity:

   \[
   \text{Quantum Advantage} = F - F_{\text{classical}} = 0.8 - 0.75 = 0.05
   \]

   Beating the measure-and-prepare strategy is possible despite the no-cloning theorem because the no-cloning theorem only forbids perfect cloning. Imperfect cloning is still possible and can outperform classical strategies in certain cases.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{optimal\_fidelity} &= 0.8 \\
\mathrm{classical\_fidelity} &= 0.75 \\
\mathrm{quantum\_advantage} &= 0.05
\end{aligned}
\]