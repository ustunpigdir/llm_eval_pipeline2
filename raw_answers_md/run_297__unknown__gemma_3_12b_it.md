Okay, let's compute the one-loop QED anomalous magnetic moment of the electron.

**1. State the one-loop (Schwinger) result for *a<sub>e</sub>* in terms of α.**

The one-loop QED anomalous magnetic moment, as calculated by Schwinger (1948), is given by:

$$a_e = \frac{\alpha}{2\pi}$$

where α is the fine-structure constant.

**2. Evaluate *a<sub>e</sub>* × 10<sup>3</sup>.**

We are given α = 1/137.036.  Therefore:

$$a_e = \frac{1/137.036}{2\pi} = \frac{1}{2\pi \times 137.036} \approx \frac{1}{863.875} \approx 0.00116006$$

Multiplying by 10<sup>3</sup>:

$$a_e \times 10^3 \approx 0.00116006 \times 10^3 = 1.16006$$

**3. Evaluate the *g*-factor to 6 decimal places.**

The *g*-factor is related to the anomaly by:

$$g = 2(1 + a_e)$$

Substituting the value of *a<sub>e</sub>*:

$$g = 2(1 + 0.00116006) = 2(1.00116006) = 2.00232012$$

Rounding to 6 decimal places:

$$g \approx 2.002320$$

**4. Explain physically what the anomaly measures (tree-level Dirac vs loop corrections), and why the SAME leading coefficient applies to the muon.**

*Physically, the anomaly measures the deviation of the electron's magnetic moment from the Dirac prediction.*

*Tree-level Dirac Prediction:*  The Dirac equation predicts a magnetic moment of exactly *g* = 2 for a spin-1/2 particle like the electron. This is a direct consequence of the particle's spin and charge.

*Loop Corrections:* Quantum Electrodynamics (QED) introduces loop corrections to this prediction. These corrections arise from the electron constantly emitting and reabsorbing virtual photons.  These virtual particles create a "cloud" around the electron, effectively screening its charge and altering its magnetic moment. The one-loop Schwinger correction is the leading-order contribution to this effect.

The anomaly, *a<sub>e</sub>* = (g - 2)/2, quantifies this deviation.  A non-zero anomaly means the electron's magnetic moment is slightly different from the Dirac prediction due to quantum effects.

*Why the SAME leading coefficient applies to the muon:* The leading coefficient, α/(2π), arises from the fundamental interaction between the charged particle (electron or muon) and the electromagnetic field. The calculation is based on Feynman diagrams involving virtual photons. The structure of these diagrams and the underlying QED Lagrangian are the same for both the electron and the muon. The only difference is the mass of the particle.  The mass enters in higher-order corrections, but the leading-order term is independent of the particle's mass.  Therefore, the same α/(2π) coefficient applies to both particles.  The muon's anomaly is also given by α/(2π), but the *magnitude* of the anomaly is smaller for the muon because α is the same, but the muon's mass is larger, and higher-order corrections become more important.

FINAL ANSWER

\[
\begin{aligned}
\mathrm{anomaly\_times\_1e3} &= 1.16006 \\
\mathrm{g\_factor} &= 2.002320
\end{aligned}
\]