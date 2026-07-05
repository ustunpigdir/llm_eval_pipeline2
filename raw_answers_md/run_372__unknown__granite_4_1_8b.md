**1. Why perfect cloning ($F=1$) is impossible**

The no‑cloning theorem follows directly from the linearity of quantum mechanics.  
Suppose there existed a linear (i.e., completely positive, trace‑preserving) map \( \mathcal{E} \) that could clone any pure qubit state \(|\psi\rangle\) perfectly:

\[
\mathcal{E}\bigl(|\psi\rangle\langle\psi|\bigr)=|\psi\rangle\langle\psi|\otimes|\psi\rangle\langle\psi| .
\]

Take two distinct pure states \(|\psi\rangle\) and \(|\Granite\rangle\). Linearity demands

\[
\mathcal{E}\!\Bigl(\tfrac{1}{2}\bigl(|\psi\rangle\langle\psi|+|\Granite\rangle\langle\Granite|\bigr)\Bigr)
   =\tfrac{1}{2}\bigl(\mathcal{E}(|\psi\rangle\langle\psi|)+\mathcal{E}(|\Granite\rangle\langle\Granite|)\bigr).
\]

But the right‑hand side would be

\[
\tfrac{1}{2}\bigl(|\psi\rangle\langle\psi|\otimes|\psi\rangle\langle\psi|
                +|\Granite\rangle\langle\Granite|\otimes|\Granite\rangle\langle\Granite|\bigr),
\]

which is **not** equal to \(\mathcal{E}\bigl(\tfrac{1}{2}(|\psi\rangle\langle\psi|+|\Granite\rangle\langle\Granite|)\bigr)\) if \(\mathcal{E}\) were to map the mixed state to a pure product state of the same form. Hence a linear map cannot satisfy the cloning requirement for all \(|\psi\rangle\). Therefore perfect cloning is impossible.

---

**2. Optimal universal cloning fidelity per copy (Buzek–Hillery machine)**  

The Buzek–Hillery symmetric universal 1→2 cloning machine achieves the maximal fidelity for any unknown pure qubit. The fidelity of each output copy is

\[
F_{\text{opt}} = \frac{5}{6}.
\]

As a decimal:

\[
F_{\text{opt}} = 0.833\overline{3}.
\]

---

**3. Best classical measure‑and‑prepare fidelity**  

A classical strategy proceeds by measuring the input qubit in some basis (e.g., the computational basis) and then preparing the outcome state for each copy. The optimal measurement is the **unbiased** measurement that yields outcomes with equal probabilities for all possible input states. Averaging over a uniformly random pure qubit \(|\psi\rangle\) gives the maximal fidelity

\[
F_{\text{class}} = \frac{2}{3}.
\]

As a decimal:

\[
F_{\text{class}} = 0.666\overline{6}.
\]

---

**4. Quantum advantage (difference)**  

The quantum advantage quantifies how much better the optimal universal quantum cloning machine is compared with the best classical (measure‑and‑prepare) method:

\[
\text{quantum\_advantage}
   = F_{\text{opt}} - F_{\text{class}}
   = \frac{5}{6} - \frac{2}{3}
   = \frac{5}{6} - \frac{4}{6}
   = \frac{1}{6}.
\]

As a decimal:

\[
\text{quantum\_advantage} = 0.166\overline{6}.
\]

**Why beating measure‑and‑prepare is possible despite the no‑cloning theorem**

The no‑cloning theorem forbids *perfect* cloning of an unknown quantum state, but it does **not** forbid *imperfect* cloning. The Buzek–Hillery machine exploits the linearity of quantum operations in a way that is allowed: it treats the input state probabilistically (by applying a unitary that mixes the input with ancillary states) and then measures. This process is linear and respects the no‑cloning constraint, yet it yields a fidelity higher than any classical measurement‑and‑preparation scheme because it can partially “guess” the state before measurement, thereby preserving more of the original quantum information than a purely classical strategy can.

---

FINAL ANSWER
\[
\begin{aligned}
\mathrm{optimal\_fidelity} &= \frac{5}{6} \approx 0.8333\\[4pt]
\mathrm{classical\_fidelity} &= \frac{2}{3} \approx 0.6667\\[4pt]
\mathrm{quantum\_advantage} &= \frac{1}{6} \approx 0.1667
\end{aligned}
\]