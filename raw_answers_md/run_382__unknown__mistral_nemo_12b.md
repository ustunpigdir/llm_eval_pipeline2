**1. Perfect cloning and linearity**

The no-cloning theorem states that it's impossible to create an exact copy of an arbitrary unknown quantum state. This is fundamentally due to the linearity of quantum mechanics. If a machine could clone an arbitrary state $|\psi\rangle$ perfectly, it would also clone any superposition $\alpha|\psi\rangle + \beta|\phi\rangle$, where $|\phi\rangle$ is an orthogonal state and $\alpha, \beta \in \mathbb{C}$. However, this would imply creating multiple copies of $|\phi\rangle$ from a single input, which violates the no-cloning theorem.

**2. Optimal universal cloning fidelity**

The optimal universal quantum cloning machine (UQCM) proposed by Buzek and Hillery achieves a fidelity of:

\[F_{UQCM} = \frac{5}{6}\]

for each copy. This is derived by maximizing the fidelity over all possible unitary transformations that map the input state to the output states.

**3. Best classical measure-and-prepare fidelity**

The best classical measure-and-prepare strategy has a fidelity of:

\[F_{classical} = \frac{2}{3}\]

This is because measuring a qubit in the computational basis and preparing copies of the outcome results in a mixed state with this fidelity.

**4. Quantum advantage**

The quantum advantage, or the difference in fidelity between the optimal UQCM and the best classical strategy, is:

\[F_{UQCM} - F_{classical} = \frac{5}{6} - \frac{2}{3} = \frac{1}{6}\]

**5. Beating measure-and-prepare despite no-cloning**

The quantum advantage arises from the ability of the UQCM to process the input state coherently, without first measuring it. This allows the machine to create approximate copies that are closer to the original state than what can be achieved by measuring and preparing copies of the outcome.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{optimal\_fidelity} &= \frac{5}{6} \\
\mathrm{classical\_fidelity} &= \frac{2}{3} \\
\mathrm{quantum\_advantage} &= \frac{1}{6}
\end{aligned}
\]