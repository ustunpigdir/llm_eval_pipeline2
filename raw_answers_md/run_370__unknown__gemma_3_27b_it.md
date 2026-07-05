
## Quantum Cloning Bounds Analysis

Here's an analysis of quantum cloning bounds, addressing the given tasks.

**1. Why perfect cloning is impossible and the role of linearity**

The no-cloning theorem states that it is impossible to create an identical copy of an arbitrary unknown quantum state. This is a direct consequence of the linearity of quantum mechanics.  Let's demonstrate this.

Suppose a cloning machine exists, represented by a unitary operator $U$, that can clone an arbitrary qubit $|\psi\rangle = \alpha |0\rangle + \beta |1\rangle$ into two identical copies:

$U(|\psi\rangle \otimes |0\rangle) = |\psi\rangle \otimes |\psi\rangle$

Applying the linearity property of $U$:

$U(\alpha |0\rangle + \beta |1\rangle \otimes |0\rangle) = \alpha U(|0\rangle \otimes |0\rangle) + \beta U(|1\rangle \otimes |0\rangle)$

This must equal $|\psi\rangle \otimes |\psi\rangle = (\alpha |0\rangle + \beta |1\rangle) \otimes (\alpha |0\rangle + \beta |1\rangle) = \alpha^2 |00\rangle + \alpha\beta |01\rangle + \beta\alpha |10\rangle + \beta^2 |11\rangle$.

Now, consider the input $|0\rangle \otimes |1\rangle$.  The cloning machine must also work for this input:

$U(|0\rangle \otimes |1\rangle) = |0\rangle \otimes |0\rangle$

Applying linearity:

$U(|0\rangle \otimes |1\rangle) = U(|0\rangle \otimes |1\rangle) = \alpha U(|0\rangle \otimes |1\rangle) + \beta U(|1\rangle \otimes |1\rangle)$

This must equal $|0\rangle \otimes |0\rangle$.  However, if we consider the input $|\psi\rangle \otimes |1\rangle$, we have:

$U(|\psi\rangle \otimes |1\rangle) = U(\alpha |0\rangle + \beta |1\rangle \otimes |1\rangle) = \alpha U(|0\rangle \otimes |1\rangle) + \beta U(|1\rangle \otimes |1\rangle)$

If we assume the cloning machine is linear, then $U(|1\rangle \otimes |1\rangle) = U(|1\rangle \otimes |0\rangle)$.  This implies that $U(|\psi\rangle \otimes |1\rangle) = \alpha |0\rangle \otimes |0\rangle + \beta |1\rangle \otimes |0\rangle = (\alpha |0\rangle + \beta |1\rangle) \otimes |0\rangle = |\psi\rangle \otimes |0\rangle$.

But this contradicts the initial requirement that $U(|\psi\rangle \otimes |0\rangle) = |\psi\rangle \otimes |\psi\rangle$.  Therefore, a linear cloning machine cannot exist, and perfect cloning is impossible.

**2. Optimal universal cloning fidelity per copy**

The Buzek-Hillery optimal universal 1->2 cloning machine achieves a fidelity of $\frac{1}{2}$ per copy. This is derived by considering the optimal unitary transformation for the cloning machine. The output state is:

$\rho_{out} = \frac{1}{2} (I + S_x \otimes S_x) |\psi\rangle \langle \psi | (I + S_x \otimes S_x)^\dagger$

where $S_x$ is the Pauli-X operator. The fidelity is then calculated as:

$F = \langle \psi | \rho_{out} | \psi \rangle = \frac{1}{2} (1 + |\langle 0| \psi \rangle|^2 |\langle 0| \psi \rangle|^2 + |\langle 1| \psi \rangle|^2 |\langle 1| \psi \rangle|^2 + 2 Re(\langle 0| \psi \rangle \langle 1| \psi \rangle^*)) $

This simplifies to $F = \frac{1}{2}(1 + |\langle \psi | \psi \rangle|^2) = \frac{1}{2}(1+1) = \frac{1}{2}$ for any $|\psi\rangle$.

**3. Best classical measure-and-prepare fidelity**

The optimal classical strategy involves measuring the qubit in the computational basis and preparing copies of the measured outcome.  If we measure the qubit and find it in state $|0\rangle$ with probability $|\alpha|^2$, we prepare two $|0\rangle$ states. If we measure it in state $|1\rangle$ with probability $|\beta|^2$, we prepare two $|1\rangle$ states. The resulting state is:

$\rho_{out} = |\alpha|^2 |00\rangle \langle 00| + |\beta|^2 |11\rangle \langle 11|$

The fidelity is then:

$F = \langle \psi | \rho_{out} | \psi \rangle = |\alpha|^2 \langle \psi | 00 \rangle \langle 00 | \psi \rangle + |\beta|^2 \langle \psi | 11 \rangle \langle 11 | \psi \rangle$

Since $|\psi\rangle = \alpha |0\rangle + \beta |1\rangle$, we have:

$F = |\alpha|^2 |\alpha|^2 + |\beta|^2 |\beta|^2 = |\alpha|^4 + |\beta|^4$

To minimize this (worst-case scenario), we set $|\alpha|^2 = |\beta|^2 = \frac{1}{2}$.  Then, $F = (\frac{1}{2})^2 + (\frac{1}{2})^2 = \frac{1}{4} + \frac{1}{4} = \frac{1}{2}$. However, we want the *best* classical fidelity, which occurs when $|\alpha|^2 = 1$ or $|\beta|^2 = 1$. In this case, $F = 1$.  However, this is only for specific states.  The average fidelity over all pure states is 1/2.  The best we can do is 1/2.

**4. Quantum advantage and explanation**

The quantum advantage is the difference between the optimal quantum fidelity and the best classical fidelity:

Quantum Advantage = Optimal Fidelity - Classical Fidelity = $\frac{1}{2} - \frac{1}{2} = 0$.

However, this is misleading. The quantum cloning machine provides a *uniform* fidelity of 1/2 for *all* input states. The classical strategy achieves a fidelity of 1 for specific states, but its average fidelity over all states is 1/2. The quantum advantage lies in the fact that the quantum machine's performance is independent of the input state, while the classical machine's performance varies significantly depending on the input.  The no-cloning theorem prevents perfect cloning, but the quantum machine can still outperform the classical measure-and-prepare strategy in terms of *average* fidelity and state-independence.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{optimal\_fidelity} &= 0.5 \\
\mathrm{classical\_fidelity} &= 0.5 \\
\mathrm{quantum\_advantage} &= 0
\end{aligned}
\]