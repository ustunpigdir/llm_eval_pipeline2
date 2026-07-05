To tackle this problem, we'll break it down into the required steps.

## Step 1: Understanding the No-Cloning Theorem and Linearity
The no-cloning theorem states that it's impossible to create a perfect copy of an arbitrary unknown quantum state. This is because any attempt to clone a quantum state would require a linear operation, which cannot distinguish between the original and the copy. Linearity in quantum mechanics means that the state of a system is preserved under unitary transformations, and any attempt to clone a state would imply a non-unitary operation, violating the principles of quantum mechanics.

## Step 2: Deriving the Optimal Universal Cloning Fidelity
The Buzek-Hillery symmetric universal quantum cloning machine (UQCM) is known to be the optimal UQCM. This machine takes one unknown pure qubit $|\psi\rangle$ and outputs two identical approximate copies. The fidelity of the output states with the original state is given by $F = \frac{5}{6}$ for both copies. This is derived from the fact that the UQCM is symmetric and that the fidelity is maximized when the output states are as close as possible to the original state.

## Step 3: Deriving the Best Classical Measure-and-Prepare Fidelity
The best classical measure-and-prepare strategy involves measuring the qubit in the computational basis and preparing copies of the outcome. Since the qubit is uniformly random, the fidelity of the output states with the original state is given by $F = \frac{1}{2}$. This is because the measurement outcome is equally likely to be $|0\rangle$ or $|1\rangle$, and the fidelity of the prepared state with the original state is $\frac{1}{2}$ in both cases.

## Step 4: Computing the Quantum Advantage
The quantum advantage is the difference between the optimal universal cloning fidelity and the best classical measure-and-prepare fidelity. This is given by $F_{\text{UQCM}} - F_{\text{classical}} = \frac{5}{6} - \frac{1}{2} = \frac{1}{3}$.

## Step 5: Explaining the Quantum Advantage
The quantum advantage arises because the UQCM can exploit the quantum nature of the input state to produce more accurate copies than the classical measure-and-prepare strategy. The UQCM can do this by using a non-linear operation to create the output states, which is not possible in the classical case. This non-linearity allows the UQCM to produce output states that are closer to the original state than the classical strategy, resulting in a higher fidelity.

## FINAL ANSWER

\[
\begin{aligned}
\mathrm{optimal\_fidelity} &= \frac{5}{6} \\
\mathrm{classical\_fidelity} &= \frac{1}{2} \\
\mathrm{quantum\_advantage} &= \frac{1}{3}
\end{aligned}
\]