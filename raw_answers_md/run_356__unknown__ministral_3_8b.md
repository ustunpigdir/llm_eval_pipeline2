### 1. Yukawa Potential and Mediator Mass in the Exponential

The Yukawa potential describes the force between two nucleons mediated by a virtual pion exchange. The potential \( V(r) \) is given by:

\[
V(r) = -\frac{g^2}{4\pi} \frac{e^{-\mu r}}{r}
\]

where:
- \( g \) is the coupling constant,
- \( \mu \) is the mass of the exchanged particle (the pion, \( m_{\pi^\pm} \)),
- \( r \) is the distance between the nucleons.

The exponential term \( e^{-\mu r} \) determines the **range** of the force. Here, \( \mu \) is the **reduced mass** of the pion, defined as:

\[
\mu = \frac{m_{\pi^\pm} c}{\hbar}
\]

This is because the Yukawa potential is derived from the propagator of a spinless particle in quantum field theory, where the mass parameter in the propagator is the **reduced mass** (i.e., \( m c^2 / \hbar c \) is dimensionless when combined with \( \hbar c \) units). Thus, the exponential depends on the **reduced Compton wavelength** \( \lambda = \hbar / (m_{\pi^\pm} c) \), where the range of the force is approximately \( \lambda \).

---

### 2. Evaluation of the Reduced Compton Wavelength \( \hbar / (m_{\pi^\pm} c) \) in femtometers (fm)

Given:
- \( m_{\pi^\pm} c^2 = 139.57 \) MeV,
- \( \hbar c = 197.327 \) MeV fm.

The reduced Compton wavelength is:

\[
\lambda = \frac{\hbar}{m_{\pi^\pm} c}
\]

We can express this in terms of the given quantities:

\[
\lambda = \frac{\hbar c}{m_{\pi^\pm} c^2} = \frac{197.327 \text{ MeV fm}}{139.57 \text{ MeV}} \approx 1.413 \text{ fm}
\]

Thus, the range of the Yukawa potential is approximately **1.413 fm**.

---

### 3. Non-Reduced Compton Wavelength \( h / (m_{\pi^\pm} c) \) and Why the Reduced One Belongs in the Exponential

The **non-reduced Compton wavelength** is defined as:

\[
\lambda_{\text{non-reduced}} = \frac{h}{m_{\pi^\pm} c}
\]

where \( h = 2\pi \hbar \). Thus:

\[
\lambda_{\text{non-reduced}} = 2\pi \lambda = 2\pi \times 1.413 \text{ fm} \approx 8.87 \text{ fm}
\]

However, the Yukawa potential depends on the **reduced Compton wavelength** \( \hbar / (m_{\pi^\pm} c) \), not the non-reduced one. This is because:

- The Yukawa potential arises from the propagator of a quantum field theory, where the mass parameter in the propagator is \( m c^2 / \hbar c \), which is dimensionless when combined with \( \hbar c \) units. The reduced mass \( \mu = m c / \hbar \) is the correct parameter for the exponential.
- The non-reduced Compton wavelength \( h / (m c) \) would introduce an extra factor of \( 2\pi \) in the exponential, which is not physically meaningful in this context. The Yukawa potential is derived from the Fourier transform of the propagator, and the reduced mass is the natural parameter.

---

### 4. Historical Inversion: Mass Scale Implied by a 2.0 fm Range

Yukawa reasoned that the range of the nuclear force (~2 fm) corresponds to the Compton wavelength of the mediating particle. The **reduced Compton wavelength** is:

\[
\lambda = \frac{\hbar}{m c}
\]

Given \( \lambda = 2.0 \) fm, we solve for \( m \):

\[
m c = \frac{\hbar}{\lambda} = \frac{\hbar c}{\lambda c}
\]

Using \( \hbar c = 197.327 \) MeV fm and \( c = 1 \) (natural units), we have:

\[
m c^2 = \frac{\hbar c}{\lambda} = \frac{197.327 \text{ MeV fm}}{2.0 \text{ fm}} = 98.6635 \text{ MeV}
\]

Thus, the predicted mass scale is approximately **98.7 MeV**. This is close to the actual pion mass (~140 MeV), but Yukawa's initial estimate was off due to uncertainties in the force range and other factors. However, the method was correct in principle.

---

### FINAL ANSWER

\[
\begin{aligned}
\mathrm{range\_fm} &= 1.413 \\
\mathrm{nonreduced\_fm} &= 8.87 \\
\mathrm{mass\_for\_2fm\_mev} &= 98.7
\end{aligned}
\]