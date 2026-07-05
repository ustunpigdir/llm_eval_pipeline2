### Derivation of the One-Loop QED Anomalous Magnetic Moment (Schwinger 1948)

We compute the leading QED correction to the electron's magnetic moment using dimensional regularization and the Feynman rules for QED. The anomalous magnetic moment is defined as \( a_e = \frac{g-2}{2} \), where \( g \) is the gyromagnetic ratio of the electron. The tree-level Dirac electron has \( g = 2 \), so the anomaly measures the deviation from this value due to quantum corrections.

---

#### 1. One-loop Schwinger result for \( a_e \)

The one-loop QED correction to the electron's anomalous magnetic moment arises from the self-energy diagram with a photon insertion (vertex correction). The leading-order contribution is given by the Schwinger formula:

\[
a_e = \frac{\alpha}{2\pi}
\]

where \( \alpha = \frac{e^2}{4\pi \hbar c} \) is the fine-structure constant. This result is derived by evaluating the one-loop vertex correction in QED, keeping only the leading term in \( \alpha \).

---

#### 2. Intermediate steps for the Schwinger result

The anomalous magnetic moment is computed from the electron's spin precession frequency in a magnetic field. The one-loop vertex correction (with a photon insertion) contributes to the electron's magnetic moment via the following steps:

- The electron propagator with a photon insertion (vertex correction) is computed in dimensional regularization.
- The photon propagator is \( \frac{-i g_{\mu\nu}}{q^2} \), and the electron propagator is \( \frac{i (\not{p} + m)}{p^2 - m^2 + i\epsilon} \).
- The vertex correction involves a loop integral of the form:

\[
\Sigma^\mu(p) = \frac{e^2}{2\pi^4} \int d^4k \gamma^\mu \frac{(\not{p} + \not{k} + m)}{(p+k)^2 - m^2 + i\epsilon} \frac{1}{k^2 + i\epsilon}
\]

- The anomalous magnetic moment is extracted from the coefficient of the term proportional to \( \sigma^{\mu\nu} \) in the vertex correction:

\[
\Sigma^\mu(p) = \frac{e}{2m} \sigma^{\mu\nu} q_\nu a_e + \text{other terms}
\]

- After performing the loop integral (using dimensional regularization and keeping only the leading term in \( \alpha \)), the result is:

\[
a_e = \frac{\alpha}{2\pi}
\]

---

#### 3. Numerical evaluation

Given \( \alpha = \frac{1}{137.036} \), we compute:

\[
a_e = \frac{\alpha}{2\pi} = \frac{1}{137.036 \times 2\pi}
\]

First, compute \( 2\pi \):

\[
2\pi \approx 6.283185307
\]

Now compute \( a_e \):

\[
a_e = \frac{1}{137.036 \times 6.283185307} \approx \frac{1}{854.443727}
\]

\[
a_e \approx 0.0011698
\]

Now multiply by \( 10^3 \):

\[
a_e \times 10^3 \approx 1.1698
\]

---

#### 4. Evaluation of the \( g \)-factor

The \( g \)-factor is given by:

\[
g = 2(1 + a_e) = 2 \left(1 + \frac{\alpha}{2\pi}\right)
\]

Substitute \( a_e \):

\[
g = 2 \left(1 + 0.0011698\right) = 2 \times 1.0011698 = 2.0023396
\]

Rounding to 6 decimal places:

\[
g \approx 2.002340
\]

---

#### 5. Physical interpretation

- The tree-level Dirac electron has \( g = 2 \), meaning its magnetic moment is exactly \( \mu = -g \frac{e}{2m} \frac{\hbar}{2} = -\frac{e}{m} \frac{\hbar}{2} \), which is the Bohr magneton.
- The one-loop QED correction (Schwinger term) modifies this value, leading to \( g = 2(1 + a_e) \). The anomaly \( a_e \) measures the deviation from the Dirac value due to quantum corrections.
- The same leading coefficient \( \frac{\alpha}{2\pi} \) applies to the muon because the muon is also a Dirac fermion with the same QED interactions (except for mass differences). The mass dependence enters only in higher-order corrections (e.g., logarithmic terms involving \( \ln(m_e/m_\mu) \)).

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{anomaly\_times\_1e3} &= 1.1698 \\
\mathrm{g\_factor} &= 2.002340
\end{aligned}
\]