**1. Perfect Cloning is Impossible**

Perfect cloning ($F=1$ for both copies) is impossible because it would imply that the cloner can distinguish between any two non-orthogonal states, which is a contradiction. This is due to the fact that any two non-orthogonal states are indistinguishable in a Hilbert space of finite dimension. In other words, if we have two non-orthogonal states $|\psi\rangle$ and $|\phi\rangle$, there is no way to determine which one is which, and therefore, we cannot have a cloner that can perfectly clone both states.

Linearity has to do with it because any linear transformation on a Hilbert space preserves the inner product. If we had a perfect cloner, it would be a linear transformation that maps the input state to the output state. However, since the input state is a superposition of two non-orthogonal states, the output state would also be a superposition of the same two states. But then, the cloner would have to be able to distinguish between the two states, which is impossible.

**2. Optimal Universal Cloning Fidelity**

The optimal universal cloning fidelity is given by the Buzek-Hillery symmetric universal machine. The fidelity of the output state is given by:

$$F = \frac{5}{6}$$

This is the maximum fidelity that can be achieved by any universal cloner.

**3. Best Classical Measure-and-Prepare Fidelity**

The best classical measure-and-prepare fidelity is given by the average fidelity of the output state when the input state is measured and prepared classically. This is given by:

$$F = \frac{1}{2} + \frac{1}{2} \cdot \frac{1}{2} = \frac{3}{4}$$

This is the maximum fidelity that can be achieved by any classical measure-and-prepare strategy.

**4. Quantum Advantage**

The quantum advantage is the difference between the optimal universal cloning fidelity and the best classical measure-and-prepare fidelity:

$$\mathrm{quantum\_advantage} = F_{optimal} - F_{classical} = \frac{5}{6} - \frac{3}{4} = \frac{1}{12}$$

This shows that the quantum cloner has a small advantage over the classical measure-and-prepare strategy.

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{optimal\_fidelity} &= \frac{5}{6} \\
\mathrm{classical\_fidelity} &= \frac{3}{4} \\
\mathrm{quantum\_advantage} &= \frac{1}{12}
\end{aligned}
\]