### Derivation of the One-Loop QED Anomalous Magnetic Moment (Schwinger 1948)

We compute the leading QED correction to the electron's magnetic moment using dimensional regularization and the Feynman rules for QED. The anomalous magnetic moment is defined as \( a_e = \frac{g-2}{2} \), where \( g \) is the gyromagnetic ratio. The tree-level Dirac electron has \( g = 2 \), so the anomaly measures the deviation from this value due to quantum corrections.

---

#### 1. One-loop Schwinger result for \( a_e \)

The one-loop QED correction to the electron's anomalous magnetic moment arises from the self-energy diagram with a virtual photon. The anomalous magnetic moment is given by the coefficient of the \( \sigma^{\mu\nu} \) term in the electron's effective vertex function. The Schwinger result (1948) is derived as follows:

- The electron propagator with a virtual photon insertion (self-energy) is computed in dimensional regularization.
- The self-energy correction to the electron propagator is:
  \[
  \Sigma(p) = \frac{e^2}{4\pi^2} \int \frac{d^4k}{(2\pi)^4} \frac{\gamma^\mu (p - k)_{\mu} + m}{k^2 - m^2 + i\epsilon} \frac{\gamma^\nu (p + k)_{\nu} + m}{(p - k)^2 - m^2 + i\epsilon}
  \]
- The anomalous magnetic moment arises from the \( \sigma^{\mu\nu} \) term in the expansion of the vertex correction. The leading term is proportional to \( \alpha = \frac{e^2}{4\pi} \), and the coefficient is derived by evaluating the integral in dimensional regularization.

The result for the anomalous magnetic moment at one loop is:
\[
a_e = \frac{\alpha}{2\pi}
\]
This is the leading-order QED correction to the electron's magnetic moment.

---

#### 2. Evaluation of \( a_e \times 10^3 \)

Given \( \alpha = \frac{1}{137.036} \), we compute:
\[
a_e = \frac{\alpha}{2\pi} = \frac{1}{137.036 \times 2\pi}
\]
First, compute the denominator:
\[
137.036 \times 2\pi \approx 137.036 \times 6.283185307 \approx 864.241
\]
Now compute \( a_e \):
\[
a_e \approx \frac{1}{864.241} \approx 0.001157
\]
Multiply by \( 10^3 \):
\[
a_e \times 10^3 \approx 1.157
\]

---

#### 3. Evaluation of the \( g \)-factor to 6 decimal places

The \( g \)-factor is given by:
\[
g = 2(1 + a_e) = 2 \left(1 + \frac{\alpha}{2\pi}\right)
\]
Substitute \( a_e \approx 0.001157 \):
\[
g = 2(1 + 0.001157) = 2.002314
\]

---

#### 4. Physical interpretation of the anomaly

- **Tree-level Dirac electron**: The Dirac equation predicts \( g = 2 \) for the electron's magnetic moment. This is the classical result where the electron's spin is perfectly aligned with its magnetic moment.
- **Loop corrections**: The one-loop QED correction (and higher-order corrections) modify this value. The anomalous magnetic moment \( a_e \) measures the deviation from \( g = 2 \) due to quantum effects (virtual photons, virtual electron-positron pairs, etc.).
- **Same leading coefficient for the muon**: The leading-order QED correction to the muon's anomalous magnetic moment also has the same coefficient \( \frac{\alpha}{2\pi} \). This is because the leading term in the self-energy correction is independent of the fermion mass (it arises from the ultraviolet behavior of the integral). The muon's mass is much larger than the electron's, but the leading QED correction is the same because it is dominated by high-energy (ultraviolet) contributions where the mass dependence drops out.

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{anomaly\_times\_1e3} &= 1.157 \\
\mathrm{g\_factor} &= 2.002314
\end{aligned}
\]