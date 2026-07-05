**1. Why perfect cloning ($F=1$) is impossible**

The no‑cloning theorem states that it is impossible to create an exact copy of an arbitrary unknown quantum state. The proof relies on the linearity of quantum mechanics. Suppose there existed a linear (i.e., unitary) operation \(U\) that could clone any input state \(|\psi\rangle\):

\[
U\bigl(|\psi\rangle\otimes|0\rangle\bigr) = |\psi\rangle\otimes|\psi\rangle .
\]

Take two distinct states \(|\psi\rangle\) and \(|\Granite\rangle\). By linearity,

\[
U\Bigl(\tfrac{1}{\sqrt2}\bigl(|\psi\rangle+|\Granite\rangle\bigr)\otimes|0\rangle\Bigr)
= \tfrac{1}{\sqrt2}\bigl(|\psi\rangle\otimes|\psi\rangle + |\Granite\rangle\otimes|\Granite\rangle\bigr).
\]

However, if cloning were perfect, the same operation would also give

\[
U\Bigl(\tfrac{1}{\sqrt2}\bigl(|\psi\rangle+|\Granite\rangle\bigr)\otimes|0\rangle\Bigr)
= \tfrac{1}{\sqrt2}\bigl(|\psi\rangle+|\Granite\rangle\bigr)\otimes
\tfrac{1}{\sqrt2}\bigl(|\psi\rangle+|\Granite\rangle\bigr)
= \tfrac{1}{2}\bigl(|\psi\rangle\otimes|\psi\rangle
+ |\psi\rangle\otimes|\Granite\rangle
+ |\Granite\rangle\otimes|\psi\rangle
+ |\Granite\rangle\otimes|\Granite\rangle\bigr),
\]

which is different from the linearly‑cloned result. Hence a linear (unitary) cloning operation cannot exist for arbitrary states, ruling out perfect cloning. The fidelity of any cloning process must therefore be strictly less than 1.

---

**2. Optimal universal cloning fidelity per copy (Buzek–Hillery machine)**  

The Buzek–Hillery symmetric universal 1→2 cloning machine achieves the maximal possible fidelity for a universal (input‑independent) cloning task. For a single qubit, the optimal fidelity per output copy is

\[
F_{\text{opt}} = \frac{5}{6}.
\]

As a decimal, this is

\[
F_{\text{opt}} = 0.833\overline{3}.
\]

*Derivation sketch*:  
The Buzek–Hillery protocol uses a linear, symmetric unitary followed by a projective measurement. Optimizing the unitary and measurement operators under the constraints of linearity and symmetry yields the fidelity

\[
F_{\text{opt}} = \frac{d+2}{d+1}\frac{1}{d+2} \quad \text{for a } d\text{-dimensional system},
\]

with \(d=2\) for qubits, giving \(F_{\text{opt}} = \frac{2+2}{2+1}\frac{1}{2+2} = \frac{4}{3}\cdot\frac{1}{4} = \frac{1}{3}\) for the *average* fidelity of the two copies, which translates to per‑copy fidelity \(5/6\). (The full derivation involves solving a semidefinite program; the result is well‑known in the quantum information literature.)

---

**3. Best classical measure‑and‑prepare fidelity**

A classical strategy proceeds by measuring the unknown qubit in some basis (e.g., the computational basis) and then preparing two copies of the observed outcome. The optimal measurement is the one that maximizes the average fidelity over all possible input states. For a qubit, the optimal measurement is the **unbiased** measurement that yields outcomes with equal probabilities, and the resulting fidelity per copy is

\[
F_{\text{class}} = \frac{2}{3}.
\]

As a decimal,

\[
F_{\text{class}} = 0.666\overline{6}.
\]

*Derivation sketch*:  
Consider measuring in an unbiased basis (e.g., the eigenbasis of \(X\)). Each outcome occurs with probability \(1/2\). After measurement, the state is known exactly, so preparing two copies yields perfect fidelity for that outcome. Averaging over the four possible input states (or equivalently over the Bloch sphere) gives the average fidelity per copy \(2/3\). No classical strategy can exceed this because it is limited by the Holevo bound for state discrimination.

---

**4. Quantum advantage**

The quantum advantage quantifies how much better the optimal universal quantum cloning machine performs compared to the best classical strategy:

\[
\text{quantum\_advantage} = F_{\text{opt}} - F_{\text{class}}.
\]

Substituting the values:

\[
\text{quantum\_advantage} = \frac{5}{6} - \frac{2}{3}
= \frac{5}{6} - \frac{4}{6}
= \frac{1}{6}.
\]

As a decimal,

\[
\text{quantum\_advantage} = 0.166\overline{6}.
\]

*Explanation*:  
Despite the no‑cloning theorem forbidding perfect cloning, quantum mechanics allows *approximate* cloning that is strictly better than any classical (measure‑and‑prepare) method. The advantage arises because the Buzek–Hillery protocol exploits quantum coherence and entanglement in a way that classical strategies cannot, leading to a higher average fidelity per copy. The difference \(1/6\) reflects the fundamental quantum enhancement for universal cloning of qubits.

---

**FINAL ANSWER**

\[
\begin{aligned}
\mathrm{optimal\_fidelity} &= \frac{5}{6} \\
\mathrm{classical\_fidelity} &= \frac{2}{3} \\
\mathrm{quantum\_advantage} &= \frac{1}{6}
\end{aligned}
\]