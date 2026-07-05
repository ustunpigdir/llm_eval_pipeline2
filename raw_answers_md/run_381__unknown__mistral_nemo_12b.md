**1. Perfect cloning is impossible due to the no-cloning theorem.**

The no-cloning theorem states that it's impossible to create an exact copy of an arbitrary unknown quantum state. This is because quantum states are represented by vectors in a complex Hilbert space, and copying such a state would require a linear operation, which is impossible due to the linearity of quantum mechanics. If a perfect cloning machine existed, it would imply a linear operator that maps any input state to an identical output state, which contradicts the no-cloning theorem.

**2. Optimal universal cloning fidelity per copy.**

The optimal universal quantum cloning machine (UQCM) proposed by Buzek and Hillery has a fidelity per copy given by:

\[F = \frac{3}{4}\]

This is derived by considering the action of the UQCM on an arbitrary input state $|\psi\rangle$ and optimizing the fidelity over all possible input states. The derivation involves finding the unitary transformation that maximizes the fidelity and solving the resulting optimization problem.

**3. Best classical measure-and-prepare fidelity.**

The best classical measure-and-prepare strategy has a fidelity given by:

\[F = \frac{2}{3}\]

This is derived by considering the average fidelity over all possible input states, where the input state is measured and then used to prepare two copies. The derivation involves averaging the fidelity over the uniform distribution of input states.

**4. Quantum advantage and beating measure-and-prepare.**

The quantum advantage is the difference between the optimal universal cloning fidelity and the best classical measure-and-prepare fidelity:

\[Q = F_{\text{optimal}} - F_{\text{classical}} = \frac{3}{4} - \frac{2}{3} = \frac{1}{12}\]

Despite the no-cloning theorem, the UQCM can beat the classical strategy because it exploits the quantum nature of the input state. The UQCM uses a unitary transformation to create entanglement between the input state and an ancilla, which allows it to create approximate copies of the input state. This is not possible with a classical strategy, which can only measure and prepare copies of the input state.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{optimal\_fidelity} &= \frac{3}{4} \\
\mathrm{classical\_fidelity} &= \frac{2}{3} \\
\mathrm{quantum\_advantage} &= \frac{1}{12}
\end{aligned}
\]