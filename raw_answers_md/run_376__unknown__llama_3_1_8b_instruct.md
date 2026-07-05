To tackle this problem, we'll break it down into the required steps.

## Step 1: Understanding the No-Cloning Theorem and Linearity
The no-cloning theorem states that it's impossible to create a perfect copy of an arbitrary unknown quantum state. This is because any linear transformation applied to a qubit can be represented as a unitary operation, and the set of unitary operations on a qubit is a group under composition. This group is isomorphic to the special unitary group SU(2), which is compact and connected. The only way to map two distinct points in a compact connected space to the same point is through a non-injective mapping, which contradicts the requirement for a cloning machine to produce identical copies of the input state.

## Step 2: Deriving the Optimal Universal Cloning Fidelity
The Buzek-Hillery symmetric universal quantum cloning machine (UQCM) is known to achieve the optimal fidelity for universal cloning. This machine takes one unknown qubit and produces two identical copies. The fidelity of the output states with respect to the input state is given by the formula:

\[ F = \frac{5}{6} \]

This is derived from the properties of the Buzek-Hillery machine, which is designed to minimize the average fidelity loss across all possible input states.

## Step 3: Deriving the Best Classical Measure-and-Prepare Fidelity
The best classical strategy for cloning a qubit is to measure it in the standard basis (i.e., in the computational basis) and then prepare two copies of the outcome. The fidelity of this process is given by the probability of correctly identifying the state of the qubit, which is 1/2 for each outcome (0 or 1), since the qubit is equally likely to be in either state. Therefore, the average fidelity of the two copies prepared by the classical strategy is:

\[ F_{classical} = \frac{1}{2} \cdot \frac{1}{2} + \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{2} \]

## Step 4: Computing the Quantum Advantage
The quantum advantage is the difference between the optimal universal cloning fidelity and the best classical measure-and-prepare fidelity:

\[ \text{quantum advantage} = F_{optimal} - F_{classical} = \frac{5}{6} - \frac{1}{2} = \frac{1}{3} \]

This advantage arises because the quantum cloning machine can exploit the coherence of the input state to produce more accurate copies, whereas the classical strategy relies solely on measurement and preparation, which inherently introduces errors due to the probabilistic nature of measurement outcomes.

## FINAL ANSWER

\[
\begin{aligned}
\mathrm{optimal\_fidelity} &= \frac{5}{6} \\
\mathrm{classical\_fidelity} &= \frac{1}{2} \\
\mathrm{quantum\_advantage} &= \frac{1}{3}
\end{aligned}
\]