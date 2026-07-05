**1. Perfect cloning and linearity**

The no-cloning theorem states that it's impossible to create an exact copy of an arbitrary unknown quantum state. This is fundamentally due to the linearity of quantum mechanics. If a cloning machine existed, it would map the input state $|\psi\rangle$ to two identical output states. However, quantum evolution is linear, meaning that if $U$ is the unitary operator describing the cloning machine, then $U(|\psi\rangle + |\phi\rangle) = U|\psi\rangle + U|\phi\rangle$. This implies that if the machine could clone $|\psi\rangle$, it could also clone $|\phi\rangle$, leading to a contradiction when $|\psi\rangle$ and $|\phi\rangle$ are orthogonal.

**2. Optimal universal cloning fidelity**

The optimal universal cloning machine (UQCM) proposed by Buzek and Hillery has a fidelity per copy given by:

\[F = \frac{5}{9}\]

This can be derived by considering the most general form of the UQCM and minimizing the distance between the output states and the input state, subject to the constraint that the output states are identical.

**3. Best classical measure-and-prepare fidelity**

The best classical measure-and-prepare strategy has a fidelity given by:

\[F = \frac{2}{3}\]

This can be derived by considering the average fidelity over all possible input states, where the strategy involves measuring the input state and preparing copies of the outcome.

**4. Quantum advantage**

The quantum advantage, or the difference in fidelity between the optimal UQCM and the best classical strategy, is:

\[F_{quantum} - F_{classical} = \frac{5}{9} - \frac{2}{3} = \frac{1}{9}\]

This shows that, despite the no-cloning theorem, quantum mechanics allows for a better cloning performance than classical strategies.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{optimal\_fidelity} &= \frac{5}{9} \\
\mathrm{classical\_fidelity} &= \frac{2}{3} \\
\mathrm{quantum\_advantage} &= \frac{1}{9}
\end{aligned}
\]