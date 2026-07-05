### 1. Impossibility of Perfect Cloning and Linearity

The no-cloning theorem states that there is no unitary operator $U$ that can perform the transformation $|\psi\rangle |0\rangle \to |\psi\rangle |\psi\rangle$ for an arbitrary unknown state $|\psi\rangle$.

**Reasoning via Linearity:**
Suppose such a machine exists. For two orthogonal states $|0\rangle$ and $|1\rangle$, we have:
$U(|0\rangle |0\rangle) = |0\rangle |0\rangle$
$U(|1\rangle |0\rangle) = |1\rangle |1\rangle$

Now consider a superposition $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$. By the linearity of quantum mechanics:
$U(|\psi\rangle |0\rangle) = \alpha U(|0\rangle |0\rangle) + \beta U(|1\rangle |0\rangle) = \alpha|00\rangle + \beta|11\rangle$

However, a perfect clone would require:
$|\psi\rangle |\psi\rangle = (\alpha|0\rangle + \beta|1\rangle)(\alpha|0\rangle + \beta|1\rangle) = \alpha^2|00\rangle + \alpha\beta|01\rangle + \beta\alpha|10\rangle + \beta^2|11\rangle$

These two results are only identical if $\alpha\beta = 0$, meaning the state must be one of the basis states. Thus, a linear operator cannot clone an arbitrary superposition.

### 2. Optimal Universal Quantum Cloning Fidelity (Buzek-Hillery)

The Buzek-Hillery machine is a symmetric universal quantum cloning machine (UQCM). For a $1 \to 2$ qubit cloner, the optimal transformation maps the input state $|\psi\rangle$ to a global state $\rho_{out}$ such that the reduced density matrix for each copy is:
$\rho_{copy} = \eta |\psi\rangle\langle\psi| + (1-\eta) \frac{I}{2}$

For the optimal symmetric cloner, the shrinking factor is $\eta = \frac{2}{3}$.
The fidelity $F$ is defined as:
$F = \langle\psi|\rho_{copy}|\psi\rangle = \eta \langle\psi|\psi\rangle\langle\psi|\psi\rangle + \frac{1-\eta}{2} \langle\psi|I|\psi\rangle$
$F = \eta(1) + \frac{1-\eta}{2}(1) = \frac{2\eta + 1 - \eta}{2} = \frac{\eta + 1}{2}$

Substituting $\eta = \frac{2}{3}$:
$F_{opt} = \frac{2/3 + 1}{2} = \frac{5/3}{2} = \frac{5}{6}$
Decimal value: $5/6 \approx 0.8333...$

### 3. Classical Measure-and-Prepare Fidelity

In a classical strategy, we perform a measurement on the single qubit $|\psi\rangle$ to estimate its state and then prepare two copies based on the result. To be universal, we use a POVM or a random basis measurement.

The optimal strategy for an unknown qubit is to measure along a random axis. The average fidelity of estimating a state $|\psi\rangle$ from a single copy is $2/3$.
Specifically, if we measure in a basis $\{|m\rangle, |m^\perp\rangle\}$, the probability of getting outcome $|m\rangle$ is $|\langle m|\psi\rangle|^2$. We then prepare copies in state $|m\rangle$.
The fidelity for one copy is:
$F_{class} = \int d\psi \int d\Omega \left( |\langle m|\psi\rangle|^2 \langle\psi|m\rangle\langle m|\psi\rangle + |\langle m^\perp|\psi\rangle|^2 \langle\psi|m^\perp\rangle\langle m^\perp|\psi\rangle \right)$
$F_{class} = \int d\Omega \left( |\langle m|\psi\rangle|^4 + |\langle m^\perp|\psi\rangle|^4 \right)$

For a qubit, the average of $\cos^4(\theta/2) + \sin^4(\theta/2)$ over the sphere is $2/3$.
Alternatively, using the formula for optimal state estimation fidelity $F = \frac{N+1}{N+2}$ for $N=1$ copy:
$F_{class} = \frac{1+1}{1+2} = \frac{2}{3}$
Decimal value: $2/3 \approx 0.6666...$

### 4. Quantum Advantage

The quantum advantage is the difference between the optimal quantum fidelity and the best classical fidelity:
$\Delta F = F_{opt} - F_{class} = \frac{5}{6} - \frac{2}{3} = \frac{5}{6} - \frac{4}{6} = \frac{1}{6}$
Decimal value: $1/6 \approx 0.1666...$

**Explanation:**
Beating the measure-and-prepare limit is possible because the UQCM does not attempt to "learn" the state (which collapses it) and then recreate it. Instead, it uses a unitary interaction to distribute the quantum information of the original qubit across a larger Hilbert space (including an ancillary system). This allows the machine to preserve more of the original coherence and phase information than any measurement-based strategy could, even though it cannot produce a perfect copy.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{optimal\_fidelity} &= 5/6 \\
\mathrm{classical\_fidelity} &= 2/3 \\
\mathrm{quantum\_advantage} &= 1/6
\end{aligned}
\]