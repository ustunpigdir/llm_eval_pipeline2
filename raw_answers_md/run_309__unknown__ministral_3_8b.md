### Derivation of the One-Loop QED Correction to the Electron's Magnetic Moment

We compute the leading QED correction to the electron's anomalous magnetic moment using the Schwinger formula (1948). The anomalous magnetic moment \( a_e \) is defined as:

\[
a_e = \frac{g - 2}{2},
\]

where \( g \) is the gyromagnetic ratio. The tree-level Dirac electron has \( g = 2 \), so \( a_e = 0 \) at tree level. The one-loop QED correction modifies this value.

---

#### 1. One-loop (Schwinger) result for \( a_e \) in terms of \( \alpha \)

The Schwinger formula for the anomalous magnetic moment at one loop is:

\[
a_e = \frac{\alpha}{2 \pi}.
\]

Here, \( \alpha \) is the fine-structure constant, given as \( \alpha = \frac{1}{137.036} \).

---

#### 2. Evaluation of \( a_e \times 10^3 \)

We compute:

\[
a_e = \frac{\alpha}{2 \pi} = \frac{1}{137.036 \times 2 \pi}.
\]

First, compute the denominator:

\[
2 \pi \approx 6.283185307.
\]

Now multiply by \( \alpha \):

\[
a_e = \frac{1}{137.036 \times 6.283185307} \approx \frac{1}{854.441746}.
\]

Now compute \( a_e \):

\[
a_e \approx 1.170847 \times 10^{-3}.
\]

Multiply by \( 10^3 \):

\[
a_e \times 10^3 \approx 1.170847.
\]

---

#### 3. Evaluation of the \( g \)-factor to 6 decimal places

Recall that:

\[
g = 2(1 + a_e).
\]

Substitute \( a_e \):

\[
g = 2 \left(1 + 1.170847 \times 10^{-3}\right) = 2 \times 1.001170847 = 2.002341694.
\]

Rounding to 6 decimal places:

\[
g \approx 2.002342.
\]

---

#### 4. Physical interpretation of the anomaly

- **Tree-level Dirac electron**: The Dirac equation predicts \( g = 2 \) exactly, meaning the electron's magnetic moment is precisely \( \mu = -g \frac{e}{2m} \mathbf{S} = -\frac{e}{m} \mathbf{S} \), where \( \mathbf{S} \) is the spin. This is the minimal coupling of spin to the electromagnetic field.

- **Loop corrections**: The one-loop QED correction arises from virtual photon exchange diagrams (self-energy and vertex corrections). These diagrams introduce a deviation from \( g = 2 \), leading to the anomalous magnetic moment \( a_e \). The leading term is proportional to \( \alpha / (2 \pi) \), which is a dimensionless loop factor.

- **Same leading coefficient for the muon**: The leading one-loop correction to the muon's anomalous magnetic moment is also \( \alpha / (2 \pi) \), because the muon is also a Dirac fermion with charge \( -e \). The same QED interaction applies, and the loop integral structure is identical (up to mass-dependent logarithmic factors, which are subleading in the limit of heavy muon). Thus, the leading coefficient is the same.

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{anomaly\_times\_1e3} &= 1.170847 \\
\mathrm{g\_factor} &= 2.002342
\end{aligned}
\]