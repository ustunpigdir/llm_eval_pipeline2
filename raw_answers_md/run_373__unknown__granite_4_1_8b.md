**1. Why perfect cloning ($F=1$) is impossible**

The no‑cloning theorem states that it is impossible to create an exact copy of an arbitrary unknown quantum state. The proof relies on the linearity of quantum mechanics. Suppose there existed a linear (hence unitary) operation \(U\) that could clone any input state \(|\psi\rangle\):

\[
U\bigl(|\psi\rangle\otimes|0\rangle\bigr) = |\psi\rangle\otimes|\psi\rangle .
\]

Consider two distinct states \(|\psi\rangle\) and \(|\Granite\rangle\). Linearity requires

\[
U\Bigl(\alpha|\psi\rangle+\beta|\Granite\rangle\Bigr)\otimes|0\rangle
= \alpha U\bigl(|\psi\rangle\otimes|0\rangle\bigr) + \beta U\bigl(|\Granite\rangle\otimes|0\rangle\bigr)
= \alpha|\psi\rangle\otimes|\psi\rangle + \beta|\Granite\rangle\otimes|\Granite\rangle .
\]

But the exact cloning condition would demand

\[
U\Bigl(\alpha|\psi\rangle+\beta|\Granite\rangle\Bigr)\otimes|0\rangle
= \bigl(\alpha|\psi\rangle+\beta|\Granite\rangle\bigr)\otimes\bigl(\alpha|\psi\rangle+\beta|\Granite\rangle\bigr)
= \alpha^{2}|\psi\rangle\otimes|\psi\rangle + \alpha\beta\bigl(|\psi\rangle\otimes|\Granite\rangle + |\Granite\rangle\otimes|\psi\rangle\bigr) + \beta^{2}|\Granite\rangle\otimes|\Granite\rangle .
\]

The cross terms \(\alpha\beta(|\psi\rangle\otimes|\Granite\rangle + |\Granite\rangle\otimes|\psi\rangle)\) appear in the exact clone but not in the linear combination \(\alpha|\psi\rangle\otimes|\psi\rangle + \beta|\Granite\rangle\otimes|\Granite\rangle\). Hence no linear (unitary) map can satisfy the cloning requirement for all \(|\psi\rangle,|\Granite\rangle\). Therefore perfect cloning is impossible, and any cloning operation must be imperfect, leading to a fidelity \(F<1\).

---

**2. Optimal universal cloning fidelity per copy (Buzek–Hillery machine)**  

The Buzek–Hillery symmetric universal 1→2 cloning machine achieves the highest possible fidelity for a universal 1→2 cloner. For a single qubit, the optimal fidelity per output copy is

\[
F_{\text{opt}} = \frac{5}{6}.
\]

As a decimal, this is

\[
F_{\text{opt}} = 0.833\overline{3}.
\]

---

**3. Best classical measure‑and‑prepare fidelity**  

A classical strategy involves measuring the unknown qubit in some basis (e.g., the computational basis), obtaining a classical outcome, and then preparing two copies of that outcome. The optimal measurement is the projective measurement in the basis that maximizes the average fidelity over all possible input states. For a qubit, the optimal classical fidelity per copy is

\[
F_{\text{class}} = \frac{2}{3}.
\]

As a decimal, this is

\[
F_{\text{class}} = 0.666\overline{6}.
\]

---

**4. Quantum advantage (difference)**  

The quantum advantage quantifies how much better the optimal universal quantum cloning machine performs compared to the best classical strategy:

\[
\text{quantum\_advantage} = F_{\text{opt}} - F_{\text{class}}
= \frac{5}{6} - \frac{2}{3}
= \frac{5}{6} - \frac{4}{6}
= \frac{1}{6}.
\]

As a decimal, this is

\[
\text{quantum\_advantage} = 0.166\overline{6}.
\]

**Why beating measure‑and‑prepare is possible despite the no‑cloning theorem**

The no‑cloning theorem forbids *perfect* cloning of an arbitrary unknown state, but it does **not** forbid *imperfect* cloning. The Buzek–Hillery machine exploits quantum superposition and entanglement to produce approximate copies that are indistinguishable from the original on average, achieving a fidelity higher than any classical measurement‑and‑preparation scheme. The quantum advantage arises because the cloning operation can be designed to be *symmetric* (the same for all input states) and *universal* (works for any qubit), leveraging the linear structure of quantum mechanics in a way that classical strategies cannot. Thus, while perfect cloning is impossible, quantum mechanics allows for optimal imperfect cloning that surpasses classical limits.

---

FINAL ANSWER
\[
\begin{aligned}
\mathrm{optimal\_fidelity} &= \frac{5}{6} \approx 0.8333\\
\mathrm{classical\_fidelity} &= \frac{2}{3} \approx 0.6667\\
\mathrm{quantum\_advantage} &= \frac{1}{6} \approx 0.1667
\end{aligned}
\]